import bpy

Operator = bpy.types.Operator

# <<< 1mp (bpy.props
props = bpy.props
StringProperty = props.StringProperty
EnumProperty = props.EnumProperty
BoolProperty = props.BoolProperty
IntVectorProperty = props.IntVectorProperty
FloatVectorProperty = props.FloatVectorProperty
FloatProperty = props.FloatProperty
# >>>

from json import loads as json_loads


class OpsReport(Operator):
    __slots__ = ()

    def execute(self, context):
        try:
            return self.i_execute(context)
        except:
            if hasattr(self, 'except_with'):
                self.except_with()

            m.call_bug_report_dialog()
            return {'CANCELLED'}
        #|
    #|
    #|
class OpsReportModal(Operator):
    __slots__ = ()

    def invoke(self, context, event):
        try:
            return self.i_invoke(context, event)
        except:
            if hasattr(self, 'except_with'):
                self.except_with()

            m.call_bug_report_dialog()
            return {'CANCELLED'}
        #|
    def modal(self, context, event):
        try:
            return self.i_modal(context, event)
        except:
            if hasattr(self, 'except_with'):
                self.except_with()

            m.call_bug_report_dialog()
            return {'CANCELLED'}
        #|
    def execute(self, context):
        try:
            return self.i_execute(context)
        except:
            if hasattr(self, 'except_with'):
                self.except_with()

            m.call_bug_report_dialog()
            return {'CANCELLED'}
        #|
    #|
    #|
class PollEditMesh:
    __slots__ = ()

    @classmethod
    def poll(cls, context):
        if context.area.type == "VIEW_3D":
            ob = context.object
            if hasattr(ob, "mode") and ob.mode == "EDIT":
                if hasattr(ob, "type") and ob.type == "MESH": return True
        return False
        #|
    #|
    #|
class GrabCursor:
    __slots__ = ()

    def invoke_grab_cursor(self, context, event):
        self.mou_limit = min(context.area.width, context.area.height) // 2
        self.mou = [event.mouse_x, event.mouse_y]
        #|
    #|
    #|
class Bmesh:
    __slots__ = 'bm', 'verts_sel', 'edges_sel', 'faces_sel'

    def __init__(self, bm, verts_sel, edges_sel, faces_sel):
        self.bm = bm
        self.verts_sel = verts_sel
        self.edges_sel = edges_sel
        self.faces_sel = faces_sel
        #|
    #|
    #|

KEYMAP_DEFAULT_slowdown_speedup = (
    {"cancel": {"RIGHTMOUSE"}, "confirm": {"LEFTMOUSE", "RET", "NUMPAD_ENTER"}, "slowdown": {"shift"}, "speedup": {"ctrl"}},
    # <<< 1precompile (type="modalKeymap")
    "{'cancel': ['RIGHTMOUSE'], 'confirm': ['LEFTMOUSE', 'RET', 'NUMPAD_ENTER'], 'slowdown': ['shift'], 'speedup': ['ctrl']}"
    # >>>
)

def modalKeymap(
        KEYMAP_DEFAULT={"cancel": {"RIGHTMOUSE"}, "confirm": {"LEFTMOUSE", "RET", "NUMPAD_ENTER"}},
        KEYMAP_STR='"cancel": "RIGHTMOUSE", "confirm": ["LEFTMOUSE", "RET", "NUMPAD_ENTER"]'
    ):
    class ModalKeymap:
        __slots__ = ()

        modal_keymap: StringProperty(
            name = "Modal Keymap",
            default = KEYMAP_STR,
            options = {'HIDDEN'})
        invoke_default: BoolProperty(
            name = "Invoke",
            default = True,
            options = {'HIDDEN'})

        def keymap_load(self):
            try:
                keymaps = {k: (set(e)  if isinstance(e, list) else {e})  for k, e in json_loads(self.modal_keymap).items()}
            except:
                keymaps = KEYMAP_DEFAULT

            if "cancel" not in keymaps:
                keymaps["cancel"] = set()
            if "confirm" not in keymaps:
                keymaps["confirm"] = set()

            self.keymaps = keymaps
            #|
        #|
        #|
    return ModalKeymap
    #|

class ModalSlowdownSpeedup:
    __slots__ = ()

    drag_speed: FloatProperty(
        name = "Drag Speed",
        default = 0.001,
        min = 0.00001,
        max = 10000.0,
        options = {'HIDDEN'})

    def get_trigger_slowdown_speedup(self):
        keymaps = self.keymaps
        if "slowdown" in keymaps:
            slowdown = keymaps["slowdown"] & {'alt', 'ascii', 'ctrl', 'oskey', 'shift'}
            self.trigger_slowdown = lambda event: any(getattr(event, k)  for k in slowdown)
        else:
            self.trigger_slowdown = lambda event: False

        if "speedup" in keymaps:
            speedup = keymaps["speedup"] & {'alt', 'ascii', 'ctrl', 'oskey', 'shift'}
            self.trigger_speedup = lambda event: any(getattr(event, k)  for k in speedup)
        else:
            self.trigger_speedup = lambda event: False

        self.drag_speed_fast = self.drag_speed * 10.0
        self.drag_speed_slow = self.drag_speed * 0.1
        #|
    #|
    #|


class OpsWinman(Operator):
    __slots__ = ()

    bl_idname = "wm.vmd_window_manager"
    bl_label = "VMD Window Manager"
    bl_options = {"REGISTER"}
    bl_description = "Open Window Manager in 3D Viewport"
    bl_keycategory = "3D View"

    def invoke(self, context, event):
        if call_admin(context):
            if m.P.is_first_use:
                from . dd import call_dd_license
                call_dd_license()

        m.Admin.REDRAW()
        return {'FINISHED'}
        #|
    #|
    #|

class OpsEditor(Operator):
    __slots__ = ()

    bl_idname = "wm.vmd_editor"
    bl_label = "VMD Editor"
    bl_options = {"REGISTER"}
    bl_description = "Open Editor in 3D Viewport"
    bl_keycategory = "3D View"

    # id_class: 
    use_pos: BoolProperty(
        name = "Override Position",
        description = "Use cursor position instead of default position.",
        default = True,
        options = set())
    pos_offset: IntVectorProperty(
        name = "Offset",
        description = "Window offset when Override Position is enabled.",
        size = 2,
        default = (-150, 15),
        subtype = "TRANSLATION",
        options = set())
    use_fit: BoolProperty(
        name = "Auto Size",
        description = "Use Auto Size instead of default size.",
        default = True,
        options = set())


    def invoke(self, context, event):
        if call_admin(context):
            if m.P.is_first_use:
                from . dd import call_dd_license
                call_dd_license()
            else:
                m.D_EDITOR[self.id_class](
                id_class = self.id_class,
                use_pos = self.use_pos,
                use_fit = self.use_fit,
                pos_offset = self.pos_offset,

                event = event)

        return {'FINISHED'}
        #|

class OpsLoadFactory(Operator):
    __slots__ = ()

    bl_idname = "wm.vmd_addon_factory"
    bl_label = "VMD Load Addon Factory Setting"
    bl_options = {"REGISTER"}
    bl_description = "Load vmdesk Factory Setting, this process cannot be 'Undo'"
    bl_keycategory = "Window"

    @classmethod
    def poll(cls, context):
        if m.P: return True
        return False

    def execute(self, context):
        if m.ADMIN: m.ADMIN.evt_sys_off(sleep=False)

        from . apps.settingeditor.areas import P_BL_RNA_PROPS

        def reset_prefs(pp):
            for identifier, rna in pp.bl_rna.properties.items():
                if identifier in {'bl_idname', 'name', 'rna_type'}: continue

                if rna.type == "POINTER":
                    reset_prefs(getattr(pp, identifier))
                    continue

                if hasattr(rna, "is_array") and rna.is_array:
                    setattr(pp, identifier, rna.default_array)
                else:
                    if rna.subtype == "BYTE_STRING":
                        setattr(pp, identifier, rna.default.encode('utf-8'))
                    else:
                        setattr(pp, identifier, rna.default)

        reset_prefs(m.P)
        self.report({'INFO'}, "Reset successful, requires manual saving of preferences")
        return {'FINISHED'}
        #|
    #|
    #|


class OpsReloadIcon(Operator):
    __slots__ = ()

    bl_idname = "wm.vmd_reload_icon"
    bl_label = "VMD Reload Icon"
    bl_options = {"REGISTER"}
    bl_description = "Reload icons after changing UI size"
    bl_keycategory = "Window"

    @classmethod
    def poll(cls, context):
        if m.P: return True
        return False

    def invoke(self, context, event):
        blg.reload_icon()
        return {'FINISHED'}
        #|
    #|
    #|
class OpsReloadFont(Operator):
    __slots__ = ()

    bl_idname = "wm.vmd_reload_font"
    bl_label = "VMD Reload Font"
    bl_options = {"REGISTER"}
    bl_description = "Reload UI Fonts after changing blender Theme / Text Rendering settings (like Subpixel Anti-Aliasing)"
    bl_keycategory = "Window"

    @classmethod
    def poll(cls, context):
        if m.P: return True
        return False

    def invoke(self, context, event):
        blg.reload_font()
        return {'FINISHED'}
        #|
    #|
    #|
class OpsUiScale(Operator):
    __slots__ = ()

    bl_idname = "wm.vmd_ui_scale"
    bl_label = "VMD UI Scale"
    bl_options = {"REGISTER"}
    bl_description = "Set add-on UI scale"
    bl_keycategory = "Window"

    factor: FloatProperty(default=1.0)

    @classmethod
    def poll(cls, context):
        if m.P: return True
        return False

    def execute(self, context):
        fac = self.factor
        P = m.P
        pp = P.size

        if fac < 1.32:
            rnas = pp.bl_rna.properties
            pp.widget[:] = rnas["widget"].default_array
            pp.title[:] = rnas["title"].default_array
            pp.border[:] = rnas["border"].default_array
            pp.dd_border[:] = rnas["dd_border"].default_array
            pp.filter[:] = rnas["filter"].default_array
            pp.tb[:] = rnas["tb"].default_array
            pp.win_shadow_offset[:] = rnas["win_shadow_offset"].default_array
            pp.dd_shadow_offset[:] = rnas["dd_shadow_offset"].default_array
            pp.shadow_softness[:] = rnas["shadow_softness"].default_array
            pp.setting_list_border[:] = rnas["setting_list_border"].default_array
            pp.block[:] = rnas["block"].default_array
            pp.button[:] = rnas["button"].default_array

            P.ModifierEditor.area_list_inner = 8
        elif fac <= 1.34:
            pp.widget[:] = (24, 2, 8, 1)
            pp.title[:] = (36, 30)
            pp.border[:] = (5, 4, 1, 1)
            pp.dd_border[:] = (1, 1, 1)
            pp.filter[:] = (266, 2, 2, 2)
            pp.tb[:] = (36, 400, 4)
            pp.win_shadow_offset[:] = (-13, 27, -30, 8)
            pp.dd_shadow_offset[:] = (-8, 11, -15, 5)
            pp.shadow_softness[:] = (57, 20)
            pp.setting_list_border[:] = (11, 7, 1)
            pp.block[:] = (3, 3, 4, 4, 4, 20, 13, 1, 3, 3)
            pp.button[:] = (11, 1, 4, 340)

            P.ModifierEditor.area_list_inner = 11
        elif fac <= 1.67:
            pp.widget[:] = (30, 3, 10, 2)
            pp.title[:] = (45, 37)
            pp.border[:] = (7, 5, 2, 2)
            pp.dd_border[:] = (2, 2, 2)
            pp.filter[:] = (332, 3, 3, 3)
            pp.tb[:] = (45, 498, 5)
            pp.win_shadow_offset[:] = (-17, 33, -38, 10)
            pp.dd_shadow_offset[:] = (-10, 13, -18, 7)
            pp.shadow_softness[:] = (57, 20)
            pp.setting_list_border[:] = (13, 8, 2)
            pp.block[:] = (3, 3, 5, 5, 5, 25, 17, 2, 3, 3)
            pp.button[:] = (13, 2, 5, 425)

            P.ModifierEditor.area_list_inner = 13
        else:
            pp.widget[:] = (36, 4, 12, 2)
            pp.title[:] = (54, 44)
            pp.border[:] = (8, 6, 2, 2)
            pp.dd_border[:] = (2, 2, 2)
            pp.filter[:] = (400, 4, 4, 4)
            pp.tb[:] = (54, 600, 6)
            pp.win_shadow_offset[:] = (-20, 40, -46, 12)
            pp.dd_shadow_offset[:] = (-12, 16, -22, 8)
            pp.shadow_softness[:] = (57, 20)
            pp.setting_list_border[:] = (16, 10, 2)
            pp.block[:] = (4, 4, 6, 6, 6, 30, 20, 2, 4, 4)
            pp.button[:] = (16, 3, 6, 512)

            P.ModifierEditor.area_list_inner = 16

        blg.reload_icon()
        return {'FINISHED'}
    #|
    #|


classes = (
    OpsWinman,
    OpsEditor,
    OpsLoadFactory,
    OpsReloadIcon,
    OpsReloadFont,
    OpsUiScale,
)

## _file_ ##
def late_import():
    #|
    from .  import VMD

    m = VMD.m
    call_admin = m.call_admin
    kill_admin = m.kill_admin

    blg = VMD.utilbl.blg

    globals().update(locals())
    #|
