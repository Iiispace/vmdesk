import bpy

Operator = bpy.types.Operator

# <<< 1mp (bpy.props
props = bpy.props
BoolProperty = props.BoolProperty
EnumProperty = props.EnumProperty
FloatProperty = props.FloatProperty
StringProperty = props.StringProperty
# >>>

class OpInternal(Operator):
    __slots__ = ()
    bl_idname = "wm.vmd_internal"
    bl_label = "VMD Internal"
    bl_options = {'INTERNAL'}

    MAIN = None

    def invoke(self, context, event):

        OpInternal.MAIN()
        return {'FINISHED'}
        #|
    #|
    #|
class OpBevelProfile(Operator):
    bl_idname = "wm.vmd_bevel_profile"
    bl_label = "Custom Profile"
    bl_options = {'INTERNAL'}

    md = None

    def execute(self, context): return {'FINISHED'}
    def invoke(self, context, event): return context.window_manager.invoke_props_dialog(self)
    def draw(self, context): self.layout.template_curveprofile(OpBevelProfile.md, "custom_profile")
    #|
    #|
class OpFalloffCurve(Operator):
    bl_idname = "wm.vmd_falloff_curve"
    bl_label = "Falloff Curve"
    bl_options = {'INTERNAL'}

    md = None
    attr = None

    def execute(self, context): return {'FINISHED'}
    def invoke(self, context, event): return context.window_manager.invoke_props_dialog(self)
    def draw(self, context): self.layout.template_curve_mapping(OpFalloffCurve.md, OpFalloffCurve.attr)
    #|
    #|
class OpColorRamp(Operator):
    bl_idname = "wm.vmd_color_ramp"
    bl_label = "Color Ramp"
    bl_options = {'INTERNAL'}

    md = None
    attr = None

    def execute(self, context): return {'FINISHED'}
    def invoke(self, context, event): return context.window_manager.invoke_props_dialog(self)
    def draw(self, context): self.layout.template_color_ramp(OpColorRamp.md, OpColorRamp.attr)
    #|
    #|
class OpScanFile(Operator):
    bl_idname = "wm.vmd_scan_file"
    bl_label = "Accept"
    bl_options = {'INTERNAL'}
    filepath: StringProperty(subtype="FILE_PATH", default="")
    check_existing: BoolProperty(default=False, options={"HIDDEN"})
    filter_glob: StringProperty(default="*", options={'HIDDEN'})

    end_fn = None

    def execute(self, context):
        self.check_existing = True
        try:    self.fin(self.filepath)
        except: pass
        return {'FINISHED'}

    def invoke(self, context, event):
        self.fin = OpScanFile.end_fn
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    #|
    #|
class OpScanFolder(Operator):
    bl_idname = "wm.vmd_scan_folder"
    bl_label = "Accept"
    bl_options = {'INTERNAL'}

    end_fn = None

    directory: StringProperty(name="Directory", description="Folder Directory")
    filter_folder: BoolProperty(default=True, options={"HIDDEN"})

    def execute(self, context):
        try:    self.fin(self.directory)
        except: pass
        return {'FINISHED'}

    def invoke(self, context, event):
        self.fin = OpScanFolder.end_fn
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
    #|
    #|
class OpsIDPreview(Operator):
    __slots__ = '_ID', '_scale_y', '_show_name'
    bl_idname = "wm.vmd_id_preview"
    bl_label = "ID Preview"
    bl_options = {'INTERNAL'}

    ID = None
    scale_y = 1.0
    show_name = False

    preview_scale: FloatProperty(min=1.0, max=8.0)

    def __del__(self):
        self.__class__.ID = None
        super.__del__()

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        cls = self.__class__
        cls.scale_y = 0.95  if cls.scale_y == 1.0 else 1.0
        self._ID = cls.ID
        self._show_name = cls.show_name
        self._scale_y = cls.scale_y * self.preview_scale
        return context.window_manager.invoke_popup(self, width=round(150 * self.preview_scale))

    def draw(self, context):
        if self._show_name:
            self.layout.label(text=self._ID.name)
        self.layout.scale_y = self._scale_y
        self.layout.template_preview(self._ID, show_buttons=False)
    #|
    #|

class OpClothBake(Operator):
    __slots__ = ()
    bl_idname = "wm.vmd_cloth_bake"
    bl_label = "VMD Cloth Bake"
    bl_options = {'INTERNAL'}

    init_data = None

    def execute(self, context):
        from . general import r_library_or_override_message, update_scene_push
        from .. m import jumpout_head

        init_data = OpClothBake.init_data
        ob = init_data["object"]
        s = r_library_or_override_message(ob)
        if s:
            self.report({'INFO'}, s)
            return {'FINISHED'}

        operation = init_data["operation"]
        cache = init_data["point_cache"]
        with bpy.context.temp_override(object=ob, point_cache=cache):
            if operation == "FRAME":
                jumpout_head()
                bpy.ops.ptcache.bake_all("INVOKE_DEFAULT", bake=False)
            elif operation == "DEL_ALL":
                bpy.ops.ptcache.free_bake_all()
                update_scene_push("Delete all bakes")
            elif operation == "BAKE_ALL":
                jumpout_head()
                bpy.ops.ptcache.bake_all("INVOKE_DEFAULT", bake=True)
            elif operation == "CALC":
                jumpout_head()
                bpy.ops.ptcache.bake("INVOKE_DEFAULT", bake=False)
            elif operation == "FROM":
                bpy.ops.ptcache.bake_from_cache()
                update_scene_push("Current cache to bake")
            elif operation == "BAKE":
                is_liboverride = cache.id_data.override_library is not None
                if is_liboverride and not cache.use_disk_cache:
                    jumpout_head()
                    bpy.ops.ptcache.bake("INVOKE_DEFAULT")
                elif cache.is_baked is True:
                    bpy.ops.ptcache.free_bake()
                    update_scene_push("Delete bake")
                else:
                    jumpout_head()
                    bpy.ops.ptcache.bake("INVOKE_DEFAULT", bake=True)
            else:
                raise ValueError("Wrong Operation")
        return {'FINISHED'}
        #|
    #|
    #|

class OpsWrapperRelease(Operator):
    __slots__ = 'keytypes'
    bl_idname = "wm.vmd_wrapper_release"
    bl_label = "VMD Wrapper Release"
    bl_options = {'REGISTER', 'BLOCKING'}

    idname: StringProperty(name="ID Name", description="Operator ID name", options={"HIDDEN"})
    use_invoke: BoolProperty(name="Use Invoke Default", options={"HIDDEN"})
    undopush: StringProperty(name="Undo Push", options={"HIDDEN"})
    keytype0: StringProperty(name="Key Type 0", options={"HIDDEN"})
    keytype1: StringProperty(name="Key Type 1", options={"HIDDEN"})
    keytype2: StringProperty(name="Key Type 2", options={"HIDDEN"})

    def execute(self, context):
        try:
            ats = self.idname.split(".")

            e = bpy.ops
            for at in ats:
                if hasattr(e, at):
                    e = getattr(e, at)

            e("INVOKE_DEFAULT")  if self.use_invoke is True else e()
        except Exception as ex:
            try:
                self.report({'WARNING'}, str(ex))
            except: pass

        keytypes = set()
        if self.keytype0: keytypes.add(self.keytype0)
        if self.keytype1: keytypes.add(self.keytype1)
        if self.keytype2: keytypes.add(self.keytype2)

        self.keytypes = keytypes
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
        #|

    def fin(self):
        if self.undopush: bpy.ops.ed.undo_push(message=self.undopush)
        return {'FINISHED'}
        #|

    def modal(self, context, event):
        if event.type == "ESC": return self.fin()
        if event.value == "RELEASE":
            if event.type in self.keytypes:
                self.keytypes.remove(event.type)

        if self.keytypes: return {'RUNNING_MODAL'}
        return self.fin()
        #|
    #|
    #|

classes = (
    OpInternal,
    OpBevelProfile,
    OpFalloffCurve,
    OpColorRamp,
    OpScanFile,
    OpScanFolder,
    OpsIDPreview,
    OpClothBake,
    OpsWrapperRelease,
)