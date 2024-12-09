











import bpy, blf
from math import ceil

from .  import VMD

escape_identifier = bpy.utils.escape_identifier

blfSize = blf.size
blfColor = blf.color
blfPos = blf.position
blfDraw = blf.draw
blfDimen = blf.dimensions

bpytypes = bpy.types

# <<< 1mp (bpytypes
CacheFile = bpytypes.CacheFile
UVProjector = bpytypes.UVProjector
GreasePencilTimeModifierSegment = bpytypes.GreasePencilTimeModifierSegment
GreasePencilDashModifierSegment = bpytypes.GreasePencilDashModifierSegment
DynamicPaintSurface = bpytypes.DynamicPaintSurface
DynamicPaintBrushSettings = bpytypes.DynamicPaintBrushSettings
FluidDomainSettings = bpytypes.FluidDomainSettings
FluidFlowSettings = bpytypes.FluidFlowSettings
FluidEffectorSettings = bpytypes.FluidEffectorSettings
EffectorWeights = bpytypes.EffectorWeights
ParticleSettings = bpytypes.ParticleSettings
ParticleSystem = bpytypes.ParticleSystem
# >>>

# <<< 1mp (VMD.area
area = VMD.area
StructAreaModal = area.StructAreaModal
AreaBlockTab = area.AreaBlockTab
# >>>

# <<< 1mp (VMD.util.deco
deco = VMD.util.deco
catch = deco.catch
noRecursive = deco.noRecursive
oneRecursive = deco.oneRecursive
# >>>

# <<< 1mp (VMD.util.types
types = VMD.util.types
RnaButton = types.RnaButton
RnaEnum = types.RnaEnum
RnaString = types.RnaString
RnaBool = types.RnaBool
Dictlist = types.Dictlist
r_rna_enum_from_bl_rna = types.r_rna_enum_from_bl_rna
BlRna = types.BlRna
RnaDataDefaultValue = types.RnaDataDefaultValue
OB_FAKE = types.OB_FAKE
Name = types.Name
r_rna_string_from_bl_rna = types.r_rna_string_from_bl_rna
# >>>


ed_undo_push = bpy.ops.ed.undo_push
UVProjector_bl_rnas = UVProjector.bl_rna.properties
DynamicPaintSurface_bl_rnas = DynamicPaintSurface.bl_rna.properties
DynamicPaintBrushSettings_bl_rnas = DynamicPaintBrushSettings.bl_rna.properties
FluidDomainSettings_bl_rnas = FluidDomainSettings.bl_rna.properties
FluidFlowSettings_bl_rnas = FluidFlowSettings.bl_rna.properties
FluidEffectorSettings_bl_rnas = FluidEffectorSettings.bl_rna.properties
EffectorWeights_bl_rnas = EffectorWeights.bl_rna.properties
ParticleSettings_bl_rnas = ParticleSettings.bl_rna.properties
ParticleSystem_bl_rnas = ParticleSystem.bl_rna.properties

def update_scene_and_ref():
    update_scene()
    upd_link_data()
    #|


class AreaBlockTabModifierEditor(AreaBlockTab):
    __slots__ = 'object_fcurves', 'object_drivers', 'upd_data_callback', 'search_data'

    def rrr_fcurve_driver(self, at0):
        def rr_fcurve_driver(attr):
            def r_fcurve():
                if self.object_fcurves:
                    return self.object_fcurves.find(f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{at0}.{attr}')
                return None
            def r_driver():
                if self.object_drivers:
                    return self.object_drivers.find(f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{at0}.{attr}')
                return None
            return r_fcurve, r_driver
        return rr_fcurve_driver
        #|
    def rrr_fcurve_driver_array(self, at0):
        def rr_fcurve_driver_array(attr, array_range):
            array_length = len(array_range)

            def r_fcurve():
                if self.object_fcurves:
                    dp = f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{at0}.{attr}'
                    return [self.object_fcurves.find(dp, index=r)  for r in array_range]
                return [None] * array_length
            def r_driver():
                if self.object_drivers:
                    dp = f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{at0}.{attr}'
                    return [self.object_drivers.find(dp, index=r)  for r in array_range]
                return [None] * array_length
            return r_fcurve, r_driver
        return rr_fcurve_driver_array
        #|
    def rrr_fcurve_driver_object(self, at0):
        def rr_fcurve_driver(attr):
            def r_fcurve():
                if self.object_fcurves:
                    return self.object_fcurves.find(f'{at0}.{attr}')
                return None
            def r_driver():
                if self.object_drivers:
                    return self.object_drivers.find(f'{at0}.{attr}')
                return None
            return r_fcurve, r_driver
        return rr_fcurve_driver
        #|
    def rrr_fcurve_driver_array_object(self, at0):
        def rr_fcurve_driver_array(attr, array_range):
            array_length = len(array_range)

            def r_fcurve():
                if self.object_fcurves:
                    dp = f'{at0}.{attr}'
                    return [self.object_fcurves.find(dp, index=r)  for r in array_range]
                return [None] * array_length
            def r_driver():
                if self.object_drivers:
                    dp = f'{at0}.{attr}'
                    return [self.object_drivers.find(dp, index=r)  for r in array_range]
                return [None] * array_length
            return r_fcurve, r_driver
        return rr_fcurve_driver_array
        #|
    def rr_fcurve_driver(self, attr):
        def r_fcurve():
            if self.object_fcurves:
                return self.object_fcurves.find(f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{attr}')
            return None
        def r_driver():
            if self.object_drivers:
                return self.object_drivers.find(f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{attr}')
            return None
        return r_fcurve, r_driver
        #|
    def rr_fcurve_driver_array(self, attr, array_range):
        array_length = len(array_range)

        def r_fcurve():
            if self.object_fcurves:
                dp = f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{attr}'
                return [self.object_fcurves.find(dp, index=r)  for r in array_range]
            return [None] * array_length
        def r_driver():
            if self.object_drivers:
                dp = f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{attr}'
                return [self.object_drivers.find(dp, index=r)  for r in array_range]
            return [None] * array_length
        return r_fcurve, r_driver
        #|
    def rr_fcurve_driver_gn(self, attr, array_range=False):
        if array_range:
            array_length = len(array_range)

            def r_fcurve():
                if self.object_fcurves:
                    dp = f'modifiers["{escape_identifier(self.w.active_modifier_name)}"]["{escape_identifier(attr)}"]'
                    return [self.object_fcurves.find(dp, index=r)  for r in array_range]
                return [None] * array_length
            def r_driver():
                if self.object_drivers:
                    dp = f'modifiers["{escape_identifier(self.w.active_modifier_name)}"]["{escape_identifier(attr)}"]'
                    return [self.object_drivers.find(dp, index=r)  for r in array_range]
                return [None] * array_length
        else:
            def r_fcurve():
                if self.object_fcurves:
                    return self.object_fcurves.find(f'modifiers["{escape_identifier(self.w.active_modifier_name)}"]["{escape_identifier(attr)}"]')
                return None
            def r_driver():
                if self.object_drivers:
                    return self.object_drivers.find(f'modifiers["{escape_identifier(self.w.active_modifier_name)}"]["{escape_identifier(attr)}"]')
                return None
        return r_fcurve, r_driver
        #|
    def rr_fcurve_driver_object(self, attr):
        def r_fcurve():
            if self.object_fcurves:
                return self.object_fcurves.find(attr)
            return None
        def r_driver():
            if self.object_drivers:
                return self.object_drivers.find(attr)
            return None
        return r_fcurve, r_driver
        #|
    def rr_refdriver(self, attr):
        def r_refdriver():
            if self.object_drivers:
                return self.object_drivers.find(f'["modifiers[\\\"{escape_identifier(self.w.active_modifier_name)}\\\"].{attr}"]')
            return None
        return r_refdriver
        #|
    def rr_datapath_head(self, at0):
        def r_datapath_head(full=False):
            if full:
                return f'{r_ID_dp(self.w.active_object)}.modifiers["{escape_identifier(self.w.active_modifier_name)}"].{at0}.'
            return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].{at0}.'
        return r_datapath_head
        #|
    def rr_datapath_head_object(self, at0):
        def r_datapath_head(full=False):
            if full:
                return f'{r_ID_dp(self.w.active_object)}.{at0}.'
            return f'{at0}.'
        return r_datapath_head
        #|
    def r_datapath_head(self, full=False):
        if full:
            return f'{r_ID_dp(self.w.active_object)}.modifiers["{escape_identifier(self.w.active_modifier_name)}"].'
        return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].'
        #|
    def r_datapath_head_gn(self, full=False):
        if full:
            return f'{r_ID_dp(self.w.active_object)}.modifiers["{escape_identifier(self.w.active_modifier_name)}"]'
        return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"]'
        #|
    def r_datapath_head_object(self, full=False):
        if full:
            return f'{r_ID_dp(self.w.active_object)}.'
        return ""
        #|
    def r_modifier(self): return self.w.active_modifier
    def r_object(self): return self.w.active_object
    def r_object_set(self): return {self.w.active_object}

    def r_object_vertex_groups(self):
        ob = self.w.active_object
        if hasattr(ob, "vertex_groups"):
            return ob.vertex_groups
        return []
        #|
    def r_object_uvs(self):
        ob = self.w.active_object
        if hasattr(ob, "data") and hasattr(ob.data, "uv_layers") and ob.data.uv_layers:
            return ob.data.uv_layers
        return []
        #|
    def r_object_vertex_colors(self):
        ob = self.w.active_object
        if hasattr(ob, "data") and hasattr(ob.data, "vertex_colors") and ob.data.vertex_colors:
            return ob.data.vertex_colors
        return []
        #|
    def r_object_layers(self):
        ob = self.w.active_object
        if hasattr(ob, "data") and hasattr(ob.data, "layers") and ob.data.layers:
            return ob.data.layers
        return []
        #|
    def rr_bones(self, r_ob):
        def r_bones():
            ob = r_ob()
            if ob:
                if hasattr(ob, "data") and hasattr(ob.data, "bones"):
                    if ob.data.bones:
                        return ob.data.bones
            return []
        return r_bones
        #|

    def r_button_width_150(self):
        return round(D_SIZE['widget_width'] * 1.5)
        #|
    def r_button_width_200(self):
        return D_SIZE['widget_width'] * 2
        #|
    def r_button_width_201(self):
        return D_SIZE['widget_width'] * 2 + SIZE_border[3]
        #|
    def r_button_width_133(self):
        return round(D_SIZE['widget_width'] * 1.3333)
        #|
    def r_button_width_166(self):
        return round(D_SIZE['widget_width'] * 1.6667)
        #|
    def r_button_width_join_bool(self):
        return D_SIZE['widget_width'] + D_SIZE['font_main_title_offset'] + D_SIZE['widget_bool_full_h']
        #|
    def r_button_width_comb_3(self):
        return round(D_SIZE['widget_width'] + D_SIZE['widget_full_h'] * 2.5)
        #|
    def r_button_width_FULL_head(self):
        return SIZE_border[3] - D_SIZE['font_main_title_offset']
        #|
    def r_label_offset_L(self):
        return D_SIZE['font_main_title_offset'] - SIZE_border[3] * 3
        #|
    def rr_dph(self, at0):
        def r_dph():
            return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"]{at0}'
        return r_dph
        #|

    def init_tab_ARMATURE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT", "TYPES":{"ARMATURE"}})
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.sep(2)
        b0.prop("use_deform_preserve_volume")
        b0.prop("use_multi_modifier")
        b0.sep(2)
        b0.prop("use_vertex_groups", text=("Bind To", "Vertex Groups"))
        b0.prop("use_bone_envelopes")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_ARRAY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        b0.prop("fit_type")
        b0.prop("count")
        b0.prop("fit_length")
        b0.prop("curve", options={"ID":"OBJECT", "TYPES":{"CURVE"}})
        props = b0.props
        r_prop = b0.r_prop

        b1 = ui.new_block(title=r_prop("use_relative_offset", options={"HEAD"}))
        b1.prop("relative_offset_displace", text="Factor")

        b2 = ui.new_block(title=r_prop("use_constant_offset", options={"HEAD"}))
        b2.prop("constant_offset_displace", text="Distance")

        b3 = ui.new_block(title=r_prop("use_object_offset", options={"HEAD"}))
        b3.prop("offset_object", text="Object", options={"ID":"OBJECT"})

        b4 = ui.new_block(title=r_prop("use_merge_vertices", text="Merge", options={"HEAD"}))
        b4.prop("merge_threshold", text="Distance")
        b4.prop("use_merge_vertices_cap", text="First and Last Copies")

        b5 = ui.new_block(title="UVs")
        b5.prop("offset_u", text="Offset U")
        b5.join_prop("offset_v", text="V")

        b6 = ui.new_block(title="Caps")
        b6.prop("start_cap", text="Cap Start", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b6.prop("end_cap", text="End", options={"ID":"OBJECT", "TYPES":{"MESH"}})

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.fit_type, md.use_relative_offset, md.use_constant_offset, md.use_object_offset, md.use_merge_vertices]: return
            ui_state[:] = [ui_anim_data.library_state, md.fit_type, md.use_relative_offset, md.use_constant_offset, md.use_object_offset, md.use_merge_vertices]


            if ui_anim_data.library_state == 1: return

            if md.fit_type == 'FIXED_COUNT':
                props["count"].light()
                props["fit_length"].dark()
                props["curve"].dark()
            elif md.fit_type == 'FIT_LENGTH':
                props["count"].dark()
                props["fit_length"].light()
                props["curve"].dark()
            elif md.fit_type == 'FIT_CURVE':
                props["count"].dark()
                props["fit_length"].dark()
                props["curve"].light()
            else:
                props["count"].dark()
                props["fit_length"].dark()
                props["curve"].dark()

            if md.use_relative_offset:
                props["relative_offset_displace"].light()
            else:
                props["relative_offset_displace"].dark()

            if md.use_constant_offset:
                props["constant_offset_displace"].light()
            else:
                props["constant_offset_displace"].dark()

            if md.use_object_offset:
                props["offset_object"].light()
            else:
                props["offset_object"].dark()

            if md.use_merge_vertices:
                props["merge_threshold"].light()
                props["use_merge_vertices_cap"].light()
            else:
                props["merge_threshold"].dark()
                props["use_merge_vertices_cap"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_BEVEL(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props
        b0.prop_flag("affect")
        b0.sep(2)
        b0.prop("offset_type")
        b0.prop("width", text="Amount")
        b0.prop("width_pct")
        b0.prop("segments")
        b0.sep(2)
        b0.prop("limit_method")
        items_b0 = b0.w.buttons[:]
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        o_vg = b0.w.buttons[-1]
        o_angle_limit = b0.r_prop("angle_limit")
        if "edge_weight" in ui_anim_data.rnas:
            # blender4.3
            o_edge_weight = b0.r_prop_search("edge_weight", GpuImg_SPREADSHEET, rr_items_gn_attributes(self.r_object), pollred=False)
            o_edge_weight.geticon = geticon_obj_attr
            o_edge_weight.getinfo = getinfo_obj_attr
            o_edge_weight.rna = r_rna_string_from_bl_rna(o_edge_weight.rna)
            o_edge_weight.rna.default = "bevel_weight_edge"
            o_vertex_weight = b0.r_prop_search("vertex_weight", GpuImg_SPREADSHEET, rr_items_gn_attributes(self.r_object), pollred=False)
            o_vertex_weight.geticon = geticon_obj_attr
            o_vertex_weight.getinfo = getinfo_obj_attr
            o_vertex_weight.rna = r_rna_string_from_bl_rna(o_vertex_weight.rna)
            o_vertex_weight.rna.default = "bevel_weight_vert"
        else:
            o_edge_weight = ButtonSep(0)
            o_vertex_weight = ButtonSep(0)

        b1 = ui.new_block(title="Profile")
        b1.prop_flag("profile_type", text="")
        props["profile_type"].r_button_width = self.r_button_width_200
        b1.prop("profile")
        edit_profile = b1.function(RNA_edit_profile, self.bufn_BEVEL_edit_profile)

        b2 = ui.new_block(title="Geometry")
        b2.prop_flag("miter_outer", text="Miter Outer")
        props["miter_outer"].r_button_width = self.r_button_width_150
        b2.prop_flag("miter_inner", text="Inner")
        b2.prop("spread")
        b2.sep(2)
        b2.prop_flag("vmesh_method", text="Intersections")
        b2.prop("use_clamp_overlap")
        b2.prop("loop_slide")

        b3 = ui.new_block(title="Shading")
        b3.sep(1)
        b3.prop("harden_normals")
        b3.sep(2)
        b3.prop("mark_seam", text=("Mark", "Seam"))
        b3.prop("mark_sharp", text="Sharp")
        b3.sep(2)
        b3.prop("material")
        b3.prop("face_strength_mode")

        ui_state = []
        _md = self.w.active_modifier
        _limit_method = _md.limit_method
        _affect = _md.affect
        ui_limit_method = [_limit_method, _affect]

        b0.w.buttons[:] = items_b0
        if _limit_method == "ANGLE":
            b0.w.buttons.append(o_angle_limit)
        elif _limit_method == "VGROUP":
            b0.w.buttons.append(o_vg)
        elif _limit_method == "WEIGHT":
            b0.w.buttons.append(o_vertex_weight  if _affect == "VERTICES" else o_edge_weight)

        def fn_darklight(md):
            if ui_limit_method == [md.limit_method, md.affect]: pass
            else:
                _limit_method = md.limit_method
                _affect = md.affect
                ui_limit_method[0] = _limit_method
                ui_limit_method[1] = _affect

                b0.w.buttons[:] = items_b0
                if _limit_method == "ANGLE":
                    b0.w.buttons.append(o_angle_limit)
                elif _limit_method == "VGROUP":
                    b0.w.buttons.append(o_vg)
                elif _limit_method == "WEIGHT":
                    b0.w.buttons.append(o_vertex_weight  if _affect == "VERTICES" else o_edge_weight)

                ui_anim_data.tag_update()
                self.redraw_from_headkey()
                self.upd_data()
                return

            if ui_state == [ui_anim_data.library_state, md.offset_type, md.limit_method, (True  if md.vertex_group else False), md.profile_type, md.affect, md.miter_inner, md.miter_outer]: return
            ui_state[:] = [ui_anim_data.library_state, md.offset_type, md.limit_method, (True  if md.vertex_group else False), md.profile_type, md.affect, md.miter_inner, md.miter_outer]


            if ui_anim_data.library_state == 1:
                edit_profile.isdarkhard = True
                edit_profile.dark()
                return

            edit_profile.isdarkhard = False

            if md.offset_type == "PERCENT":
                props["width"].dark()
                props["width_pct"].light()
            else:
                props["width"].light()
                props["width_pct"].dark()

            if md.limit_method == "ANGLE":
                o_angle_limit.light()
                props["vertex_group"].dark()
                props["invert_vertex_group"].dark()
                o_edge_weight.dark()
            elif md.limit_method == "VGROUP":
                o_angle_limit.dark()
                props["vertex_group"].light()
                if md.vertex_group:
                    props["invert_vertex_group"].light()
                else:
                    props["invert_vertex_group"].dark()

                o_edge_weight.dark()
            elif md.limit_method == "WEIGHT":
                o_angle_limit.dark()
                props["vertex_group"].dark()
                props["invert_vertex_group"].dark()
                o_edge_weight.light()
            else:
                o_angle_limit.dark()
                props["vertex_group"].dark()
                props["invert_vertex_group"].dark()
                o_edge_weight.dark()

            if md.profile_type == "SUPERELLIPSE":
                props["profile"].set_text("Shape")
                props["profile"].light()
                edit_profile.dark()
            elif md.profile_type == "CUSTOM":
                props["profile"].set_text("Miter Shape")
                edit_profile.light()

                if md.affect == "VERTICES" or (md.miter_inner == "MITER_SHARP" and md.miter_outer == "MITER_SHARP"):
                    props["profile"].dark()
                else:
                    props["profile"].light()
            else:
                props["profile"].set_text("Shape")
                props["profile"].dark()
                edit_profile.dark()

            if md.affect == "VERTICES":
                props["miter_outer"].dark()
                props["miter_inner"].dark()
                props["vmesh_method"].dark()
                props["loop_slide"].dark()
                props["mark_seam"].dark()
                props["mark_sharp"].dark()
                props["spread"].dark()
            else:
                props["miter_outer"].light()
                props["miter_inner"].light()
                props["vmesh_method"].light()
                props["loop_slide"].light()
                props["mark_seam"].light()
                props["mark_sharp"].light()
                if md.miter_inner == "MITER_ARC":
                    props["spread"].light()
                else:
                    props["spread"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_BOOLEAN(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        def r_button_width():
            return round(D_SIZE['widget_width'] * 0.6) * 2
        def r_button_width_head():
            return round(D_SIZE['widget_width'] * 0.6) * 3

        b0 = ui.new_block()
        props = b0.props
        b0.prop_flag("operation")
        props["operation"].r_button_width = self.r_button_width_150
        b0.sep(2)
        b0.prop_flag("operand_type")
        b0.prop("object", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b0.prop("collection", options={"ID":"COLLECTION"})
        b0.prop_flag("solver")

        b1 = ui.new_block(title="Solver Options")
        b1.prop("double_threshold")
        b1.prop_flag("material_mode")
        b1.sep(1)
        b1.prop("use_self")
        b1.prop("use_hole_tolerant")

        for e in props.values():
            e.r_button_width = r_button_width
        props["operation"].r_button_width = r_button_width_head

        def r_target():
            return self.w.active_modifier.object
        def r_target_display():
            target = self.w.active_modifier.object
            if target:
                return target.display
            return None
        def r_collection():
            return self.w.active_modifier.collection

        ui.set_fold_state(True)
        b2 = ui.new_block(title="Target")
        b2.sep(0.5)
        ui_anim_data_target = b2.set_pp_id_data(r_target, bpytypes.Object)
        b2_0 = b2.new_block(title="Visibility")
        props_target = b2_0.props
        b2_0.sep(1)
        b2_0.prop("hide_select", text=("Hide", "Selection"))
        b2_0.prop("hide_viewport", text="Viewport")
        b2_0.prop("hide_render", text="Render")
        b2_0.sep(2)
        b2_0.prop("is_shadow_catcher", text=("Mask", "Shadow Catcher"))
        b2_0.prop("is_holdout", text="Holdout")
        b2_0.sep(1)

        b2_0_0 = b2_0.new_block(title="Ray")
        b2_0_0.sep(1)
        b2_0_0.prop("visible_camera", text="Camera")
        b2_0_0.prop("visible_diffuse", text="Diffuse")
        b2_0_0.prop("visible_glossy", text="Glossy")
        b2_0_0.prop("visible_transmission", text="Transmission")
        b2_0_0.prop("visible_volume_scatter", text="Volume Scatter")
        b2_0_0.prop("visible_shadow", text="Shadow")

        b2_1 = b2.new_block(title="Viewport Display")
        b2_1.sep(1)
        b2_1.prop("show_name", text=("Show", "Name"))
        b2_1.prop("show_axis", text="Axis")
        b2_1.prop("show_wire", text="WireFrame")
        b2_1.prop("show_all_edges", text="All Edges")
        b2_1.prop("show_texture_space", text="Texture Space")
        ui_anim_data_target_display = b2_1.set_pp(r_target_display, bpytypes.ObjectDisplay, lambda: "display")
        b2_1.prop("show_shadows")
        b2_1.set_pp_from(ui_anim_data_target)
        b2_1.prop("show_in_front")
        b2_1.sep(2)
        b2_1.prop("color")
        b2_1.sep(0)
        b2_1.prop("display_type")
        b2_1.sep(1)
        b2_1_0 = b2_1.new_block(title=b2_1.r_prop("show_bounds", text="Bounds", options={"HEAD"}))
        b2_1_0.prop("display_bounds_type", text="Display Type")

        b2_2 = b2.new_block(title="Collection")
        ui_anim_data_collection = b2_2.set_pp_id_data(r_collection, bpytypes.Collection)
        b2_2.sep(1)
        b2_2.prop("hide_select", text=("Hide", "Selection"))
        b2_2.prop("hide_viewport", text="Viewport")
        b2_2.prop("hide_render", text="Render")

        ui_state = []
        ui_state_target = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.operand_type, md.solver]: return
            ui_state[:] = [ui_anim_data.library_state, md.operand_type, md.solver]


            if ui_anim_data.library_state == 1: return

            if md.operand_type == "COLLECTION":
                props["object"].dark()
                props["collection"].light()

                if md.solver == "EXACT":
                    props["double_threshold"].dark()
                    props["use_self"].dark()
                    props["use_hole_tolerant"].light()
                    props["material_mode"].light()
                else:
                    props["double_threshold"].light()
                    props["use_self"].dark()
                    props["use_hole_tolerant"].dark()
                    props["material_mode"].dark()
            else:
                props["object"].light()
                props["collection"].dark()

                if md.solver == "EXACT":
                    props["double_threshold"].dark()
                    props["use_self"].light()
                    props["use_hole_tolerant"].light()
                    props["material_mode"].light()
                else:
                    props["double_threshold"].light()
                    props["use_self"].dark()
                    props["use_hole_tolerant"].dark()
                    props["material_mode"].dark()

        def fn_darklight_target(target):
            if target:
                if ui_state_target == [ui_anim_data_target.library_state, target.display_type, target.show_bounds]: return
                ui_state_target[:] = [ui_anim_data_target.library_state, target.display_type, target.show_bounds]


                if ui_anim_data_target.library_state == 1: return

                if target.show_bounds or target.display_type == "BOUNDS":
                    props_target["display_bounds_type"].light()
                else:
                    props_target["display_bounds_type"].dark()
            else:
                if ui_state_target == [ui_anim_data_target.library_state]: return
                ui_state_target[:] = [ui_anim_data_target.library_state]


        n1 = N1

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)
            ui_anim_data_target.update_with(fn_darklight_target)
            ui_anim_data_target_display.update_with(n1)
            ui_anim_data_collection.update_with(n1)

        self.upd_data_callback = upd_data_callback        
        #|
    def init_tab_BUILD(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props
        b0.prop("frame_start")
        b0.prop("frame_duration")
        b0.prop("use_reverse")

        b1 = ui.new_block(title=b0.r_prop("use_random_order", options={"HEAD"}))
        b1.prop("seed")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_random_order]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_random_order]

            if ui_anim_data.library_state == 1: return

            if md.use_random_order:
                props["seed"].light()
            else:
                props["seed"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_CAST(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props
        b0.prop_flag("cast_type")
        props["cast_type"].r_button_width = self.r_button_width_150
        b0.sep(2)
        b0.prop_flag(["use_x", "use_y", "use_z"], text="Axis", options={"NAMES": "XYZ"})
        b0.prop("factor")
        b0.prop("radius")
        b0.prop("size")
        b0.prop("use_radius_as_size")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("object", options={"ID":"OBJECT"})
        b0.prop("use_transform")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, (True  if md.object else False)]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, (True  if md.object else False)]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.object:
                props["use_transform"].light()
            else:
                props["use_transform"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_CLOTH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        rr_dph = self.rr_dph
        r_vgroups = self.r_object_vertex_groups

        def r_settings(): return self.w.active_modifier.settings
        def r_collision_settings(): return self.w.active_modifier.collision_settings
        def r_point_cache(): return self.w.active_modifier.point_cache
        def r_settings_effector_weights(): return self.w.active_modifier.settings.effector_weights

        uianim_settings = ui.set_pp(r_settings, bpytypes.ClothSettings, rr_dph(".settings"))

        b0 = ui.new_block()
        props = b0.props
        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        button_quality = b0.r_prop("quality", text="Quality Steps")
        b0.items.append(ButtonOverlay(button_quality.w, button_search, button_quality))
        b0.prop("time_scale", text="Speed Multiplier")

        b1 = ui.new_block(title="Physical Properties")
        b1.prop("mass", text="Vertex Mass")
        b1.prop("air_damping", text="Air Viscosity")
        b1.prop_flag("bending_model")
        b1.sep(1)

        b1_0 = b1.new_block(title="Stiffness")
        b1_0.prop("tension_stiffness", text="Tension")
        b1_0.prop("compression_stiffness", text="Compression")
        b1_0.prop("shear_stiffness", text="Shear")
        b1_0.prop("bending_stiffness", text="Bending")

        b1_1 = b1.new_block(title="Damping")
        b1_1.prop("tension_damping", text="Tension")
        b1_1.prop("compression_damping", text="Compression")
        b1_1.prop("shear_damping", text="Shear")
        b1_1.prop("bending_damping", text="Bending")

        r_prop = b1.r_prop
        b1_2 = b1.new_block(title=r_prop("use_internal_springs", text="Internal Springs", options={"HEAD"}))
        b1_2.prop("internal_spring_max_length", text="Max Spring Creation Length")
        b1_2.prop("internal_spring_max_diversion", text="Max Creation Diversion")
        b1_2.prop("internal_spring_normal_check", text="Check Surface Normals", options={"FLIP"})
        b1_2.prop("internal_tension_stiffness", text="Tension")
        b1_2.prop("internal_tension_stiffness_max", text="Max")
        b1_2.prop("internal_compression_stiffness", text="Compression")
        b1_2.prop("internal_compression_stiffness_max", text="Max")
        b1_2.prop_search("vertex_group_intern", GpuImg_GROUP_VERTEX, r_vgroups, text="Vertex Group")

        b1_3 = b1.new_block(title=r_prop("use_pressure", text="Pressure", options={"HEAD"}))
        b1_3.prop("uniform_pressure_force")
        b1_3.prop("use_pressure_volume", text="Custom Volume")
        b1_3.prop("target_volume")
        b1_3.prop("pressure_factor")
        b1_3.prop("fluid_density")
        b1_3.prop_search("vertex_group_pressure", GpuImg_GROUP_VERTEX, r_vgroups, text="Vertex Group")

        uianim_cache, fn_darklight_cache, blocklis_caches, media_caches, extra_buttons = ui_point_cache(
            "CLOTH", ui, r_point_cache, rr_dph(".point_cache"), self.r_object)

        b3 = ui.new_block(title="Shape")
        b3.prop_search("vertex_group_mass", GpuImg_GROUP_VERTEX, r_vgroups, text="Pin Group")
        b3.prop("pin_stiffness", text="Stiffness")
        b3.sep(2)
        b3.prop("use_sewing_springs", text="Sewing")
        b3.prop("sewing_force_max", text="Max Sewing Force")
        b3.sep(2)
        b3.prop("shrink_min", text="Shrinking Factor")
        b3.prop("use_dynamic_mesh", text="Dynamic Mesh")
        b3.sep(2)
        b3.prop("rest_shape_key", options={"r_items": lambda: self.w.active_object.data.shape_keys.key_blocks})

        b4 = ui.new_block(title="Collisions")
        uianim_collision_settings = b4.set_pp(r_collision_settings, bpytypes.ClothCollisionSettings, rr_dph(".collision_settings"))
        b4.prop("collision_quality", text="Quality")
        b4.sep(1)
        r_prop = b4.r_prop

        b4_0 = b4.new_block(title=r_prop("use_collision", text="Object Collisions", options={"HEAD"}))
        b4_0.prop("distance_min", text="Distance")
        b4_0.prop("impulse_clamp")
        b4_0.prop_search("vertex_group_object_collisions", GpuImg_GROUP_VERTEX, r_vgroups, text="Vertex Group")
        b4_0.prop("collection", options={"ID":"COLLECTION"})

        b4_1 = b4.new_block(title=r_prop("use_self_collision", text="Self Collisions", options={"HEAD"}))
        b4_1.prop("self_friction", text="Friction")
        b4_1.prop("self_distance_min", text="Distance")
        b4_1.prop("self_impulse_clamp", text="Impulse Clamping")
        b4_1.prop_search("vertex_group_self_collisions", GpuImg_GROUP_VERTEX, r_vgroups, text="Vertex Group")

        b5 = ui.new_block(title="Property Weights")
        b5.set_pp_from(uianim_settings)
        b5.prop_search("vertex_group_structural_stiffness", GpuImg_GROUP_VERTEX, r_vgroups, text="Structural Group")
        b5.prop("tension_stiffness_max", text="Max Tension")
        b5.prop("compression_stiffness_max", text="Max Compression")
        b5.sep(2)
        b5.prop_search("vertex_group_shear_stiffness", GpuImg_GROUP_VERTEX, r_vgroups, text="Shear Group")
        b5.prop("shear_stiffness_max", text="Max Shearing")
        b5.sep(2)
        b5.prop_search("vertex_group_bending", GpuImg_GROUP_VERTEX, r_vgroups, text="Bending Group")
        b5.prop("bending_stiffness_max", text="Max Bending")
        b5.sep(2)
        b5.prop_search("vertex_group_shrink", GpuImg_GROUP_VERTEX, r_vgroups, text="Shrinking Group")
        b5.prop("shrink_max", text="Max Shrinking")

        uianim_effector_weights, fn_darklight_effector_weights = ui_effector_weights(
            "CLOTH", ui, r_settings_effector_weights, rr_dph(".settings.effector_weights"))

        ui_state = []
        ui_state_col = []

        def fn_darklight(cloth):
            md = self.w.active_modifier
            cache = md.point_cache
            enabled = cache.is_baked is False

            if ui_state == [uianim_settings.library_state, enabled, cloth.bending_model, cloth.use_internal_springs, cloth.use_pressure, cloth.use_pressure_volume, (cloth.vertex_group_mass == ""), cloth.use_sewing_springs, cloth.use_dynamic_mesh]: return
            ui_state[:] = [uianim_settings.library_state, enabled, cloth.bending_model, cloth.use_internal_springs, cloth.use_pressure, cloth.use_pressure_volume, (cloth.vertex_group_mass == ""), cloth.use_sewing_springs, cloth.use_dynamic_mesh]

            if uianim_settings.library_state == 1: return

            if enabled:
                props["mass"].light()
                props["air_damping"].light()
                props["bending_model"].light()

                if cloth.bending_model == "ANGULAR":
                    props["tension_damping"].set_text("Tension")
                    props["compression_stiffness"].light()
                    props["compression_damping"].light()

                    if cloth.use_internal_springs:
                        b1_2.w.light()
                    else:
                        b1_2.w.dark()
                else:
                    props["tension_damping"].set_text("Structural")
                    props["compression_stiffness"].dark()
                    props["compression_damping"].dark()

                    b1_2.w.dark()

                props["tension_stiffness"].light()
                props["shear_stiffness"].light()
                props["bending_stiffness"].light()
                props["tension_damping"].light()
                props["shear_damping"].light()
                props["bending_damping"].light()
                props["use_internal_springs"].light()

                if cloth.use_pressure:
                    b1_3.w.light()
                    if cloth.use_pressure_volume:
                        props["target_volume"].light()
                    else:
                        props["target_volume"].dark()
                else:
                    b1_3.w.dark()

                b3.w.light()
                props["use_pressure"].light()

                if cloth.vertex_group_mass == "":
                    props["pin_stiffness"].dark()
                else:
                    props["pin_stiffness"].light()

                if cloth.use_sewing_springs:
                    props["sewing_force_max"].light()
                else:
                    props["sewing_force_max"].dark()

                if cloth.use_dynamic_mesh:
                    props["rest_shape_key"].dark()
                else:
                    props["rest_shape_key"].light()

            else:
                props["mass"].dark()
                props["air_damping"].dark()
                props["bending_model"].dark()
                props["tension_stiffness"].dark()
                props["shear_stiffness"].dark()
                props["bending_stiffness"].dark()
                props["compression_stiffness"].dark()
                props["tension_damping"].dark()
                props["compression_damping"].dark()
                props["shear_damping"].dark()
                props["bending_damping"].dark()

                b1_2.w.dark()
                b1_3.w.dark()
                b3.w.dark()

        def fn_darklight_collision_settings(cloth_col):
            md = self.w.active_modifier
            cache = md.point_cache
            enabled = cache.is_baked is False

            if ui_state_col == [uianim_collision_settings.library_state, enabled, cloth_col.use_collision, cloth_col.use_self_collision]: return
            ui_state_col[:] = [uianim_collision_settings.library_state, enabled, cloth_col.use_collision, cloth_col.use_self_collision]

            if uianim_collision_settings.library_state == 1: return

            ps = uianim_collision_settings.props

            if enabled:
                if cloth_col.use_collision or cloth_col.use_self_collision:
                    ps["collision_quality"].light()
                else:
                    ps["collision_quality"].dark()

                b5.w.light()

                if cloth_col.use_collision:
                    b4_0.w.light()
                else:
                    b4_0.w.dark()

                if cloth_col.use_self_collision:
                    b4_1.w.light()
                else:
                    b4_1.w.dark()

                ps["use_collision"].light()
                ps["use_self_collision"].light()
            else:
                b5.w.dark()
                b4_0.w.dark()
                b4_1.w.dark()

                ps["collision_quality"].dark()
                ps["use_collision"].dark()
                ps["use_self_collision"].dark()

        def upd_data_callback():
            uianim_settings.update_with(fn_darklight)
            uianim_cache.update_with(fn_darklight_cache)
            uianim_collision_settings.update_with(fn_darklight_collision_settings)
            uianim_effector_weights.update_with(fn_darklight_effector_weights)

            blocklis_caches.upd_data()
            media_caches.upd_data()

        button_search.fn = self.r_bufn_search(upd_data_callback, [
                uianim_settings,
                uianim_cache,
                uianim_collision_settings,
                uianim_effector_weights,
            ],
            extra_buttons = extra_buttons,
            search_data = search_data)
        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_COLLISION(self):

        if self.w.active_modifier.settings: pass
        else:
            b0 = Blocks(self)
            b0.buttons = [Title("No collision settings available")]
            self.items[:] = [b0]
            return

        def r_settings(): return self.w.active_object.collision

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        uianim_settings = ui.set_pp(r_settings, bpytypes.CollisionSettings, lambda: "collision")

        b0 = ui.new_block()
        props = b0.props

        b0.prop("use")
        b0.prop("absorption", text="Field Absorption")

        b1 = ui.new_block(title="Particle")
        b1prop = b1.prop
        b1prop("permeability")
        b1prop("stickiness")
        b1prop("use_particle_kill")
        b1.sep(2)
        b1prop("damping_factor", text="Damping")
        b1.join_prop("damping_random", text="Randomize")
        b1.sep(2)
        b1prop("friction_factor", text="Friction")
        b1.join_prop("friction_random", text="Randomize")

        b2 = ui.new_block(title="Softbody & Cloth")
        b2prop = b2.prop
        b2prop("damping", text="Damping")
        b2prop("thickness_outer", text="Thickness Outer")
        b2prop("thickness_inner", text="Inner")
        b2prop("cloth_friction")
        b2.sep(2)
        b2prop("use_culling")
        b2prop("use_normal")

        ui_state = []

        def fn_darklight(collision):
            if self.w.active_modifier.settings: pass
            else:
                self.init_tab(self.active_tab, push=False, evtkill=False)
                return True

            if ui_state == [uianim_settings.library_state, collision.use]: return
            ui_state[:] = [uianim_settings.library_state, collision.use]

            if uianim_settings.library_state == 1: return

            if collision.use:
                props["absorption"].light()
                b1.w.light()
                b2.w.light()
            else:
                props["absorption"].dark()
                b1.w.dark()
                b2.w.dark()

        def upd_data_callback():
            uianim_settings.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_CORRECTIVE_SMOOTH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0prop = b0.prop
        b0prop("factor", text="Factor")
        b0prop("iterations")
        b0prop("scale")
        b0.sep(2)
        b0prop("smooth_type")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.sep(1)
        b0prop("use_only_smooth")
        b0prop("use_pin_boundary")
        b0.sep(2)
        b0prop("rest_source")
        b0.sep(1)
        bind = b0.function(RNA_CORRECTIVE_SMOOTH_bind, self.bufn_CORRECTIVE_SMOOTH_bind, isdarkhard=True)
        label0 = b0.label([""])

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.rest_source, md.is_bind]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.rest_source, md.is_bind]

            if ui_anim_data.library_state == 1:
                bind.dark()
                label0.blf_label[0].text = ""
                return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if ui_anim_data.library_state == 2:
                bind.dark()
                label0.blf_label[0].text = ""
            else:
                bind.light()

                if md.rest_source == "BIND":
                    bind.light()
                    label0.blf_label[0].text = ""  if md.is_bind else "⚠ Bind data required"
                else:
                    bind.dark()
                    label0.blf_label[0].text = ""

            if md.is_bind:
                bind.set_button_text("Unbind")
            else:
                bind.set_button_text("Bind")

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_CURVE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT", "TYPES":{"CURVE"}})
        b0.sep(2)
        b0.prop_flag("deform_axis", options={"ROW_LENGTH": 3})
        props["deform_axis"].set_button_text([" X", " Y", " Z", "-X", "-Y", "-Z"])
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_DATA_TRANSFER(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props
        r_prop = b0.r_prop
        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        button_object = r_prop("object", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b0.items.append(ButtonOverlay(button_object.w, button_search, button_object))
        b0.prop("use_object_transform")
        b0.sep(2)
        b0.prop("mix_mode")
        b0.prop("mix_factor")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.sep(2)
        gen = b0.function(RNA_DATA_TRANSFER_gen, self.bufn_DATA_TRANSFER_gen, isdarkhard=True)
        label0 = b0.label([""])
        # label0.blf_label[0].color = COL_box_val_fg_error

        b1 = ui.new_block(title=r_prop("use_vert_data", options={"HEAD"}))
        b1.prop("data_types_verts", text="Types")
        props["data_types_verts"].r_button_width = self.r_button_width_200
        b1.sep(1)
        b1.prop("vert_mapping", text="Mapping")
        props["vert_mapping"].r_button_width = self.r_button_width_133
        b1.sep(2)

        b1_0 = b1.new_block(title="Vertex Groups")
        b1_0.prop("layers_vgroup_select_src", text="Layer Selection")
        b1_0.prop("layers_vgroup_select_dst", text="Layer Mapping")

        b1_1 = b1.new_block(title="Colors")
        b1_1.prop("layers_vcol_vert_select_src", text="Layer Selection")
        b1_1.prop("layers_vcol_vert_select_dst", text="Layer Mapping")

        b2 = ui.new_block(title=r_prop("use_edge_data", options={"HEAD"}))
        b2.prop("data_types_edges", text="Types", options={"ROW_LENGTH": 3})
        props["data_types_edges"].r_button_width = self.r_button_width_200
        b2.sep(1)
        b2.prop("edge_mapping", text="Mapping")
        props["edge_mapping"].r_button_width = self.r_button_width_133

        b3 = ui.new_block(title=r_prop("use_loop_data", options={"HEAD"}))
        b3.prop("data_types_loops", text="Types", options={"ROW_LENGTH": 1})
        b3.label(["Mapping :"])
        b3.prop("loop_mapping", text="")
        props["loop_mapping"].r_button_width = self.r_label_offset_L
        props["loop_mapping"].set_align("FULL")
        b3.sep(2)

        b3_0 = b3.new_block(title="Colors")
        b3_0.prop("layers_vcol_loop_select_src", text="Layer Selection")
        b3_0.prop("layers_vcol_loop_select_dst", text="Layer Mapping")

        b3_1 = b3.new_block(title="UVs")
        b3_1.prop("layers_uv_select_src", text="Layer Selection")
        b3_1.prop("layers_uv_select_dst", text="Layer Mapping")
        b3_1.prop("islands_precision")

        b4 = ui.new_block(title=r_prop("use_poly_data", options={"HEAD"}))
        b4.prop("data_types_polys", text="Types")
        props["data_types_polys"].r_button_width = self.r_button_width_166
        b4.sep(0)
        b4.prop("poly_mapping", text="Mapping")
        props["poly_mapping"].r_button_width = self.r_button_width_166

        b5 = ui.new_block(title="Topology Mapping")
        b5.prop("use_max_distance", options={"FLIP"})
        b5.prop("max_distance")
        b5.prop("ray_radius")

        ui_state = []

        def fn_darklight(md):
            if md.object:
                me = md.object.data
                mesh = md.id_data.data
                ll_v0 = len(me.vertices)
                ll_v1 = len(mesh.vertices)
                ll_e0 = len(me.edges)
                ll_e1 = len(mesh.edges)
                ll_l0 = len(me.loops)
                ll_l1 = len(mesh.loops)
                ll_p0 = len(me.polygons)
                ll_p1 = len(mesh.polygons)
                has_polygon = False  if ll_p0 == 0 else True
                has_polygon_source = False  if ll_p1 == 0 else True
            else:
                ll_v0 = -1
                ll_v1 = -2
                ll_e0 = -1
                ll_e1 = -2
                ll_l0 = -1
                ll_l1 = -2
                ll_p0 = -1
                ll_p1 = -2
                has_polygon = False
                has_polygon_source = False

            if ui_state == [ui_anim_data.library_state, md.mix_mode, md.vertex_group, md.use_vert_data, md.data_types_verts, md.data_types_loops, ll_v0, ll_v1, ll_e0, ll_e1, ll_l0, ll_l1, ll_p0, ll_p1, md.vert_mapping, md.use_edge_data, md.data_types_edges, md.edge_mapping, md.use_loop_data, md.loop_mapping, md.use_poly_data, md.data_types_polys, md.poly_mapping, md.use_max_distance]: return
            ui_state[:] = [ui_anim_data.library_state, md.mix_mode, md.vertex_group, md.use_vert_data, md.data_types_verts, md.data_types_loops, ll_v0, ll_v1, ll_e0, ll_e1, ll_l0, ll_l1, ll_p0, ll_p1, md.vert_mapping, md.use_edge_data, md.data_types_edges, md.edge_mapping, md.use_loop_data, md.loop_mapping, md.use_poly_data, md.data_types_polys, md.poly_mapping, md.use_max_distance]

            if ui_anim_data.library_state in {1, -1}:
                gen.dark()
                return

            gen.light()
            data_types_verts = md.data_types_verts
            data_types_loops = md.data_types_loops
            tx_info = ""

            if md.mix_mode in {"ABOVE_THRESHOLD", "BELOW_THRESHOLD"}:
                props["mix_factor"].dark()
            else:
                props["mix_factor"].light()

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_vert_data:
                props["data_types_verts"].light()
                props["vert_mapping"].light()

                if "VGROUP_WEIGHTS" in data_types_verts:
                    props["layers_vgroup_select_src"].light()
                    props["layers_vgroup_select_dst"].light()
                else:
                    props["layers_vgroup_select_src"].dark()
                    props["layers_vgroup_select_dst"].dark()

                if "COLOR_VERTEX" in data_types_verts:
                    props["layers_vcol_vert_select_src"].light()
                    props["layers_vcol_vert_select_dst"].light()
                else:
                    props["layers_vcol_vert_select_src"].dark()
                    props["layers_vcol_vert_select_dst"].dark()

                if data_types_verts:
                    if md.object:
                        if ll_v0 == 0 or ll_v1 == 0:
                            tx_info = "⚠ Source / target meshes do not have any vertices"
                        else:
                            vert_mapping = md.vert_mapping
                            if vert_mapping == "TOPOLOGY":
                                if ll_v0 != ll_v1:
                                    tx_info = "⚠ Source and target meshes have different vertex counts"
                            elif vert_mapping in {"POLY_NEAREST", "POLYINTERP_NEAREST", "POLYINTERP_VNORPROJ"}:
                                if not has_polygon:
                                    tx_info = "⚠ Source mesh doesn't have any faces"
                            elif vert_mapping in {"EDGE_NEAREST", "EDGEINTERP_NEAREST"}:
                                if ll_e0 == 0:
                                    tx_info = "⚠ Source mesh doesn't have any edges"
            else:
                props["data_types_verts"].dark()
                props["vert_mapping"].dark()
                props["layers_vgroup_select_src"].dark()
                props["layers_vgroup_select_dst"].dark()
                props["layers_vcol_vert_select_src"].dark()
                props["layers_vcol_vert_select_dst"].dark()

            if md.use_edge_data:
                props["data_types_edges"].light()
                props["edge_mapping"].light()

                if md.data_types_edges:
                    if md.object:
                        edge_mapping = md.edge_mapping
                        if edge_mapping == "TOPOLOGY":
                            if ll_e0 != ll_e1:
                                tx_info = "⚠ Source and target meshes have different edge counts"
                            elif ll_e0 == 0 or ll_e1 == 0:
                                tx_info = "⚠ Source / target meshes do not have any edges"
                        elif edge_mapping in {"VERT_NEAREST", "NEAREST", "EDGEINTERP_VNORPROJ"}:
                            if ll_e0 == 0 or ll_e1 == 0:
                                tx_info = "⚠ Source / target meshes do not have any edges"
                        elif edge_mapping == "POLY_NEAREST":
                            if not has_polygon:
                                tx_info = "⚠ Source mesh doesn't have any faces"
            else:
                props["data_types_edges"].dark()
                props["edge_mapping"].dark()

            if md.use_loop_data:
                props["data_types_loops"].light()
                props["loop_mapping"].light()

                if "COLOR_CORNER" in data_types_loops:
                    props["layers_vcol_loop_select_src"].light()
                    props["layers_vcol_loop_select_dst"].light()
                else:
                    props["layers_vcol_loop_select_src"].dark()
                    props["layers_vcol_loop_select_dst"].dark()

                if "UV" in data_types_loops:
                    props["layers_uv_select_src"].light()
                    props["layers_uv_select_dst"].light()
                    props["islands_precision"].light()
                else:
                    props["layers_uv_select_src"].dark()
                    props["layers_uv_select_dst"].dark()
                    props["islands_precision"].dark()

                if data_types_loops:
                    if md.object:
                        if md.loop_mapping == "TOPOLOGY":
                            if ll_l0 != ll_l1:
                                tx_info = "⚠ Source mesh has different amount of face corners"
                            elif has_polygon and has_polygon_source: pass
                            else:
                                tx_info = "⚠ Source / target meshes do not have any faces"
                        elif md.loop_mapping in {"NEAREST_POLYNOR", "NEAREST_POLY", "POLYINTERP_NEAREST", "POLYINTERP_LNORPROJ"}:
                            if has_polygon and has_polygon_source: pass
                            else:
                                tx_info = "⚠ Source / target meshes do not have any faces"
            else:
                props["data_types_loops"].dark()
                props["loop_mapping"].dark()
                props["layers_vcol_loop_select_src"].dark()
                props["layers_vcol_loop_select_dst"].dark()
                props["layers_uv_select_src"].dark()
                props["layers_uv_select_dst"].dark()
                props["islands_precision"].dark()

            if md.use_poly_data:
                props["data_types_polys"].light()
                props["poly_mapping"].light()

                if md.data_types_polys:
                    if md.object:
                        if md.poly_mapping == "TOPOLOGY":
                            if ll_p0 != ll_p1:
                                tx_info = "⚠ Source mesh has different amount of faces"
                            elif has_polygon and has_polygon_source: pass
                            else:
                                tx_info = "⚠ Source / target meshes do not have any faces"
                        elif md.poly_mapping in {"NEAREST", "NORMAL", "POLYINTERP_PNORPROJ"}:
                            if has_polygon and has_polygon_source: pass
                            else:
                                tx_info = "⚠ Source / target meshes do not have any faces"
            else:
                props["data_types_polys"].dark()
                props["poly_mapping"].dark()

            if md.use_max_distance:
                props["max_distance"].light()
            else:
                props["max_distance"].dark()

            label0.blf_label[0].text = tx_info

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        button_search.fn = self.r_bufn_search(upd_data_callback, [
                ui_anim_data,
            ],
            extra_buttons = [gen],
            search_data = search_data)
        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_DECIMATE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        _mode = self.w.active_modifier.decimate_type
        if _mode == "COLLAPSE":
            _mode = 0

            b0 = ui.new_block()
            props = b0.props

            b0.prop_flag("decimate_type")
            props["decimate_type"].r_button_width = self.r_button_width_200
            b0.sep(2)
            b0.prop("ratio")
            b0.sep(2)
            b0.prop("use_symmetry")
            b0.prop_flag("symmetry_axis")
            b0.sep(2)
            b0.prop("use_collapse_triangulate")
            b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
            b0.prop("vertex_group_factor")
            label0 = b0.label([""])

            ui_state = []

            def fn_darklight(md):
                if ui_state == [ui_anim_data.library_state, md.vertex_group, md.use_symmetry, md.face_count]: return
                ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.use_symmetry, md.face_count]


                label0.blf_label[0].text = f'Face Count : {md.face_count}'
                if ui_anim_data.library_state == 1: return

                if md.vertex_group:
                    props["invert_vertex_group"].light()
                    props["vertex_group_factor"].light()
                else:
                    props["invert_vertex_group"].dark()
                    props["vertex_group_factor"].dark()

                if md.use_symmetry:
                    props["symmetry_axis"].light()
                else:
                    props["symmetry_axis"].dark()

            def upd_data_callback():
                if self.w.active_modifier.decimate_type == "COLLAPSE": pass
                else:
                    kill_evt_except()
                    self.init_tab(self.active_tab, push=False, evtkill=False)
                    return

                ui_anim_data.update_with(fn_darklight)

        elif _mode == "UNSUBDIV":
            _mode = 1

            b0 = ui.new_block()
            props = b0.props

            b0.prop_flag("decimate_type")
            props["decimate_type"].r_button_width = self.r_button_width_200
            b0.sep(2)
            b0.prop("iterations")
            label0 = b0.label([""])

            ui_state = []

            def fn_darklight(md):
                if ui_state == [ui_anim_data.library_state, md.face_count]: return
                ui_state[:] = [ui_anim_data.library_state, md.face_count]


                label0.blf_label[0].text = f'Face Count : {md.face_count}'

            def upd_data_callback():
                if self.w.active_modifier.decimate_type == "UNSUBDIV": pass
                else:
                    kill_evt_except()
                    self.init_tab(self.active_tab, push=False, evtkill=False)
                    return

                ui_anim_data.update_with(fn_darklight)
        else:
            _mode = 2

            b0 = ui.new_block()
            props = b0.props

            b0.prop_flag("decimate_type")
            props["decimate_type"].r_button_width = self.r_button_width_200
            b0.sep(2)
            b0.prop("angle_limit")
            b0.sep(2)
            b0.prop("delimit", options={"ROW_LENGTH": 1})
            b0.sep(2)
            b0.prop("use_dissolve_boundaries")
            label0 = b0.label([""])

            ui_state = []

            def fn_darklight(md):
                if ui_state == [ui_anim_data.library_state, md.face_count]: return
                ui_state[:] = [ui_anim_data.library_state, md.face_count]


                label0.blf_label[0].text = f'Face Count : {md.face_count}'

            def upd_data_callback():
                if self.w.active_modifier.decimate_type in {"COLLAPSE", "UNSUBDIV"}:
                    kill_evt_except()
                    self.init_tab(self.active_tab, push=False, evtkill=False)
                    return

                ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_DISPLACE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props
        b0prop = b0.prop

        b0prop("texture", text="", options={"RICH":"TEXTURE"})
        props["texture"].r_button_width = self.r_button_width_200
        b0.sep(0)
        b0.prop_flag("texture_coords", text="Coord")
        props["texture_coords"].r_button_width = self.r_button_width_200
        b0.sep(2)
        b0prop("texture_coords_object", text="Object", options={"ID":"OBJECT"})
        b0.prop_search("texture_coords_bone", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().texture_coords_object), text="Bone")
        b0.prop_search("uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)
        b0.sep(2)
        b0prop("direction")
        b0.prop_flag("space")
        b0.sep(2)
        b0prop("strength")
        b0prop("mid_level")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'texture_coords_object'}$)
            if md.texture_coords_object:
                name_texture_coords_object = md.texture_coords_object.name
                state_texture_coords_object = 0  if md.texture_coords_object.type == "ARMATURE" else 1
            else:
                name_texture_coords_object = ""
                state_texture_coords_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.vertex_group, (True  if md.texture else False), md.texture_coords, md.direction, state_texture_coords_object, name_texture_coords_object]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, (True  if md.texture else False), md.texture_coords, md.direction, state_texture_coords_object, name_texture_coords_object]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.texture:
                props["texture_coords"].light()

                if md.texture_coords == "OBJECT":
                    props["texture_coords_object"].light()
                    props["uv_layer"].dark()
                    if state_texture_coords_object == 0:
                        props["texture_coords_bone"].light()
                    else:
                        props["texture_coords_bone"].dark()
                elif md.texture_coords == "UV":
                    props["texture_coords_object"].dark()
                    props["uv_layer"].light()
                    props["texture_coords_bone"].dark()
                else:
                    props["texture_coords_object"].dark()
                    props["uv_layer"].dark()
                    props["texture_coords_bone"].dark()
            else:
                props["texture_coords"].dark()
                props["texture_coords_object"].dark()
                props["uv_layer"].dark()
                props["texture_coords_bone"].dark()

            if md.direction in {"NORMAL", "CUSTOM_NORMAL"}:
                props["space"].dark()
            else:
                props["space"].light()

            props["texture_coords_bone"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_DYNAMIC_PAINT(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        button_ui_type = b0.r_prop_flag("ui_type")
        button_ui_type.set_callback = update_scene_and_ref
        b0.items.append(ButtonOverlay(button_ui_type.w, button_search, button_ui_type))

        _ui_type = self.w.active_modifier.ui_type
        if _ui_type == "CANVAS":
            def bufn_canvas_toggle():
                ob = self.w.active_object
                push_message = "Add canvas"  if self.w.active_modifier.canvas_settings is None else "Remove canvas"
                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.dpaint.type_toggle(type="CANVAS")

                wrapButtonFn(bufn, ob, push_message=push_message)

            if self.w.active_modifier.canvas_settings is None:
                b1 = ui.new_block(title="Settings")

                button_add = b1.function(RNA_add_canvas, bufn_canvas_toggle, isdarkhard=True)

                def fn_darklight(md):
                    if md.ui_type == "CANVAS" and md.canvas_settings is None:
                        if ui_anim_data.library_state == 1:
                            if button_add.isdark is False:
                                button_add.dark()
                        return


                    self.reinit_tab_with(search_data)
                    return True

                def upd_data_callback():
                    ui_anim_data.update_with(fn_darklight)

                button_search.fn = self.r_bufn_search(upd_data_callback, [
                        ui_anim_data,
                    ],
                    extra_buttons = [button_add],
                    search_data = search_data)
            else:
                def r_canvas_surfaces():
                    return self.w.active_modifier.canvas_settings.canvas_surfaces
                def r_canvas_surface():
                    return self.w.active_modifier.canvas_settings.canvas_surfaces.active
                def remove_active_canvas():
                    ob = self.w.active_object
                    def bufn():
                        with bpy.context.temp_override(object=ob):
                            bpy.ops.dpaint.surface_slot_remove()

                    wrapButtonFn(bufn, ob, evtkill=False)
                def add_active_canvas():
                    ob = self.w.active_object
                    def bufn():
                        with bpy.context.temp_override(object=ob):
                            bpy.ops.dpaint.surface_slot_add()

                    wrapButtonFn(bufn, ob, evtkill=False)
                def set_enabled(e, boo):
                    e.is_active = boo
                def r_datapath_settings_canvas_surfaces_eye(e):
                    return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].canvas_settings.canvas_surfaces["{escape_identifier(e.name)}"].is_active'
                def r_datapath_head_canvas_settings_canvas_surfaces(e):
                    return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].canvas_settings.canvas_surfaces["{escape_identifier(e.name)}"]'
                def r_dph_canvas_surface():
                    e = self.w.active_modifier.canvas_settings.canvas_surfaces.active
                    if e:
                        return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].canvas_settings.canvas_surfaces["{escape_identifier(e.name)}"]'
                    return ""
                def r_point_cache():
                    e = self.w.active_modifier.canvas_settings.canvas_surfaces.active
                    if e:
                        return e.point_cache
                    return None
                def r_dph_point_cache():
                    e = self.w.active_modifier.canvas_settings.canvas_surfaces.active
                    if e:
                        return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].canvas_settings.canvas_surfaces["{escape_identifier(e.name)}"].point_cache'
                    return ""
                def r_effector_weights():
                    e = self.w.active_modifier.canvas_settings.canvas_surfaces.active
                    if e:
                        return e.effector_weights
                    return None
                def r_dph_effector_weights():
                    e = self.w.active_modifier.canvas_settings.canvas_surfaces.active
                    if e:
                        return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].canvas_settings.canvas_surfaces["{escape_identifier(e.name)}"].effector_weights'
                    return ""
                def bufn_add_vertex_color():
                    self.r_object().data.vertex_colors.new(name="dp_paintmap")
                def bufn_remove_vertex_color():
                    vertex_colors = self.r_object().data.vertex_colors
                    vertex_colors.remove(vertex_colors[blocklis_vertex_color.active_index])
                def bufn_add_vertex_group():
                    self.r_object().vertex_groups.new(name="dp_weight")
                def bufn_remove_vertex_group():
                    vertex_groups = self.r_object().vertex_groups
                    vertex_groups.remove(vertex_groups[vertex_groups.active_index])
                def bufn_cv_bake_image_sequence():
                    ob = self.r_object()
                    if not ob: return

                    def bufn():
                        with bpy.context.temp_override(object=ob):
                            bpy.ops.dpaint.bake()

                    jumpout_head()
                    wrapButtonFn(bufn, ob)

                button_delete = b0.r_function(RNA_remove_canvas, bufn_canvas_toggle, isdarkhard=True,
                    options={"icon_cls": GpuImg_TRASH, "icon_cls_dark": GpuImgNull})
                button_delete.set_align("R")

                uianim_settings = ui.set_pp(r_canvas_surface, bpytypes.DynamicPaintSurface, r_dph_canvas_surface)
                b1 = ui.new_block(title=ButtonOverlay(None, Title("Settings"), button_delete))

                blocklis_canvas = BlocklistAZEnabled(b1.w,
                    r_pp = r_canvas_surfaces,
                    r_object = self.r_object,
                    r_datapath_head = r_datapath_head_canvas_settings_canvas_surfaces,
                    get_icon = geticon_dynamic_paint_canvas,
                    remove_active_item = remove_active_canvas,
                    add_item = add_active_canvas,
                    update_icons = update_icons_dynamic_paint_canvas,
                    r_enabled = lambda e: e.is_active,
                    r_enabled_datapath = r_datapath_settings_canvas_surfaces_eye,
                    set_enabled = set_enabled)
                blocklis_canvas_media = BlockMediaAZ(b1.w, blocklis_canvas)

                b1.items += [blocklis_canvas, blocklis_canvas_media]
                b1.sep(2)
                ps_surface = uianim_settings.props
                b1.prop_flag("surface_format", text="")
                ps_surface["surface_format"].r_button_width = self.r_button_width_200
                b1.prop("image_resolution")
                b1.prop("use_antialiasing")
                b1.prop("frame_start", text="Frame Start")
                b1.prop("frame_end", text="End")
                b1.prop("frame_substeps")

                b2 = ui.new_block(title="Surface")
                r_prop = b2.r_prop
                o_surface_type = r_prop("surface_type")
                ps_surface["surface_type"].rna = RNA_surface_type
                ps_surface["surface_type"].enum_items = RNA_surface_type.enum_items
                o_brush_collection = r_prop("brush_collection", options={"ID":"COLLECTION"})
                o_brush_influence_scale = r_prop("brush_influence_scale", text="Scale Influence")
                o_brush_radius_scale = r_prop("brush_radius_scale", text="Radius")
                o_depth_clamp = r_prop("depth_clamp")
                o_depth_clamp.set_callback = update_scene_and_ref
                o_displace_factor = r_prop("displace_factor")
                o_use_incremental_displace = r_prop("use_incremental_displace")
                o_use_wave_open_border = r_prop("use_wave_open_border")
                o_wave_timescale = r_prop("wave_timescale")
                o_wave_speed = r_prop("wave_speed")
                o_wave_damping = r_prop("wave_damping")
                o_wave_spring = r_prop("wave_spring")
                o_wave_smoothness = r_prop("wave_smoothness")

                b_dissolve = b2.new_block(title=r_prop("use_dissolve", options={"HEAD"}))
                b_dissolve.prop("dissolve_speed", text="Time")
                b_dissolve.prop("use_dissolve_log")

                b_dry = b2.new_block(title=r_prop("use_drying", options={"HEAD"}))
                b_dry.prop("dry_speed", text="Time")
                b_dry.prop("color_dry_threshold", text="Color")
                b_dry.prop("use_dry_log")

                b_effects = ui.new_block(title="Effects")
                b_spread = b_effects.new_block(title=r_prop("use_spread", text="Spread", options={"HEAD"}))
                b_spread.prop("spread_speed", text="Speed")
                b_spread.prop("color_spread_speed", text="Color")

                b_drip = b_effects.new_block(title=r_prop("use_drip", text="Drip", options={"HEAD"}))
                b_drip.prop("drip_velocity")
                b_drip.prop("drip_acceleration")
                b_drip.sep(1)
                uianim_effector_weights, fn_darklight_effector_weights = ui_effector_weights(
                    "DYNAMIC_PAINT", b_drip, r_effector_weights, r_dph_effector_weights, title="Weights")

                b_shrink = b_effects.new_block(title=r_prop("use_shrink", text="Shrink", options={"HEAD"}))
                b_shrink.prop("shrink_speed", text="Speed")

                b_initial_color = ui.new_block(title="Initial Color")
                r_prop = b_initial_color.r_prop
                o_init_color_type = r_prop("init_color_type", text="Type", options={"D_icon":D_geticon_init_color_type})
                o_init_color = r_prop("init_color")
                o_init_texture = r_prop("init_texture", options={"ID":"TEXTURE"})
                o_init_layername = b_initial_color.r_prop_search("init_layername", GpuImg_GROUP_UVS, self.r_object_uvs, text="UV Map")

                b_output = ui.new_block(title="Output")
                r_prop = b_output.r_prop
                r_prop_search = b_output.r_prop_search
                o_output_name_a = r_prop_search("output_name_a", GpuImg_GROUP_VCOL, self.r_object_vertex_colors, text="Paintmap Layer")
                o_output_name_a.set_callback = update_scene_and_ref
                o_output_name_a_3 = r_prop_search("output_name_a", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Vertex Group")
                o_output_name_a_3.set_callback = update_scene_and_ref
                o_output_name_b = r_prop_search("output_name_b", GpuImg_GROUP_VCOL, self.r_object_vertex_colors, text="Wetmap Layer")
                o_output_name_b.set_callback = update_scene_and_ref
                o_bake_image_sequence = b_output.r_function(RNA_dpaint_bake_image_sequence, bufn_cv_bake_image_sequence, isdarkhard=True)
                o_image_output_path = r_prop("image_output_path", text="Cache Path")
                o_image_output_path.set_align("FULL")
                o_uv_layer = r_prop_search("uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)
                o_image_fileformat = b_output.r_prop_flag("image_fileformat")
                o_use_premultiply = r_prop("use_premultiply")
                o_displace_type = r_prop("displace_type", text="Displace Type")
                o_output_name_a_2 = r_prop("output_name_a", text="Filename")
                o_output_name_a_2.set_callback = update_scene_and_ref
                o_depth_clamp_1 = r_prop("depth_clamp")

                b_paintmaps = b_output.new_block(title=r_prop("use_output_a", text="Paintmaps", options={"HEAD"}))
                b_paintmaps.prop("output_name_a", text="Name")
                b_wetmaps = b_output.new_block(title=r_prop("use_output_b", text="Wetmaps", options={"HEAD"}))
                b_wetmaps.prop("output_name_b", text="Name")
                o_output_name_a_1 = ps_surface["output_name_a"]
                o_output_name_b_1 = ps_surface["output_name_b"]

                blocklis_vertex_color = BlocklistAZ(b_output.w,
                    r_pp = self.r_object_vertex_colors,
                    r_object = self.r_object,
                    r_datapath_head = lambda: "data.vertex_colors",
                    get_icon = lambda e: GpuImg_GROUP_VCOL(),
                    remove_active_item = bufn_remove_vertex_color,
                    add_item = bufn_add_vertex_color,
                    use_ui_active_index = True)
                blocklis_vertex_color_media = BlockMediaAZ(b_output.w, blocklis_vertex_color)

                blocklis_vertex_group = BlocklistAZ(b_output.w,
                    r_pp = self.r_object_vertex_groups,
                    r_object = self.r_object,
                    r_datapath_head = lambda: "vertex_groups",
                    get_icon = lambda e: GpuImg_GROUP_VERTEX(),
                    remove_active_item = bufn_remove_vertex_group,
                    add_item = bufn_add_vertex_group)
                blocklis_vertex_group_media = BlockMediaAZ(b_output.w, blocklis_vertex_group)

                for e in ps_surface.values():
                    e.set_callback = update_scene_and_ref

                uianim_cache, fn_darklight_cache, blocklis_caches, blocklis_caches_media, extra_buttons = ui_point_cache(
                    "DYNAMIC_PAINT", ui, r_point_cache, r_dph_point_cache, self.r_object)

                _allow_update = True
                ui_state_format = []
                ui_state_sub = []
                ui_lib_state = [-2]
                callback_sub = N1


                def fn_darklight(md):
                    if md.ui_type == "CANVAS" and md.canvas_settings is not None: return


                    nonlocal _allow_update
                    _allow_update = False
                    self.reinit_tab_with(search_data)
                    return True

                def fn_darklight_settings(surf):
                    if ui_state_format == [surf.surface_format, surf.surface_type, surf.init_color_type, surf.is_cache_user]: pass
                    else:
                        surface_format = surf.surface_format
                        surface_type = surf.surface_type
                        init_color_type = surf.init_color_type
                        is_cache_user = surf.is_cache_user
                        ui_state_format[:] = [surface_format, surface_type, init_color_type, is_cache_user]

                        nonlocal callback_sub
                        ui_state_sub.clear()
                        ui_lib_state[0] = -2

                        if surface_type == "PAINT":
                            b2.items[:] = [
                                o_surface_type,
                                o_brush_collection,
                                o_brush_influence_scale,
                                o_brush_radius_scale,
                                ButtonSep(1),
                                b_dissolve.w,
                                b_dry.w,
                            ]

                            if init_color_type == "COLOR":
                                b_initial_color.items[:] = [o_init_color_type, o_init_color]
                            elif init_color_type == "TEXTURE":
                                o_init_layername.set_text("UV Map")
                                o_init_layername.box_icon_cls = GpuImg_GROUP_UVS
                                if o_init_layername.isdark is False:
                                    o_init_layername.box_icon.__class__ = GpuImg_GROUP_UVS
                                o_init_layername.enum_items = self.r_object_uvs

                                b_initial_color.items[:] = [o_init_color_type, o_init_texture, o_init_layername]
                            elif init_color_type == "VERTEX_COLOR":
                                o_init_layername.set_text("Color Layer")
                                o_init_layername.box_icon_cls = GpuImg_GROUP_VCOL
                                if o_init_layername.isdark is False:
                                    o_init_layername.box_icon.__class__ = GpuImg_GROUP_VCOL
                                o_init_layername.enum_items = self.r_object_vertex_colors

                                b_initial_color.items[:] = [o_init_color_type, o_init_layername]
                            else:
                                b_initial_color.items[:] = [o_init_color_type, ButtonSep(6)]

                            def darklight_sub(surface):
                                if surface.use_dissolve:
                                    ps_surface["dissolve_speed"].light()
                                    ps_surface["use_dissolve_log"].light()
                                else:
                                    ps_surface["dissolve_speed"].dark()
                                    ps_surface["use_dissolve_log"].dark()

                                if surface.use_drying:
                                    ps_surface["dry_speed"].light()
                                    ps_surface["color_dry_threshold"].light()
                                    ps_surface["use_dry_log"].light()
                                else:
                                    ps_surface["dry_speed"].dark()
                                    ps_surface["color_dry_threshold"].dark()
                                    ps_surface["use_dry_log"].dark()

                                if surface.use_spread:
                                    ps_surface["spread_speed"].light()
                                    ps_surface["color_spread_speed"].light()
                                else:
                                    ps_surface["spread_speed"].dark()
                                    ps_surface["color_spread_speed"].dark()

                                if surface.use_drip:
                                    ps_surface["drip_velocity"].light()
                                    ps_surface["drip_acceleration"].light()
                                    for e in uianim_effector_weights.props.values():
                                        e.light()
                                else:
                                    ps_surface["drip_velocity"].dark()
                                    ps_surface["drip_acceleration"].dark()
                                    for e in uianim_effector_weights.props.values():
                                        e.dark()

                                if surface.use_shrink:
                                    ps_surface["shrink_speed"].light()
                                else:
                                    ps_surface["shrink_speed"].dark()

                            if surface_format == "VERTEX":
                                ps_surface["output_name_a"] = o_output_name_a
                                ps_surface["output_name_b"] = o_output_name_b
                                b_output.items[:] = [
                                    o_output_name_a,
                                    o_output_name_b,
                                    ButtonSep(2),
                                    blocklis_vertex_color,
                                    blocklis_vertex_color_media,
                                ]

                                def callback_sub(surface):
                                    uianim_cache.update_with(fn_darklight_cache)
                                    uianim_effector_weights.update_with(fn_darklight_effector_weights)

                                    blocklis_canvas.upd_data()
                                    blocklis_canvas_media.upd_data()
                                    blocklis_caches.upd_data()
                                    blocklis_caches_media.upd_data()
                                    blocklis_vertex_color.upd_data()
                                    blocklis_vertex_color_media.upd_data()

                                    if ui_anim_data.library_state in {1, -1}: return
                                    if ui_state_sub == [ui_anim_data.library_state, surface.use_dissolve, surface.use_drying, surface.use_spread, surface.use_drip, surface.use_shrink]: return
                                    ui_state_sub[:] = [ui_anim_data.library_state, surface.use_dissolve, surface.use_drying, surface.use_spread, surface.use_drip, surface.use_shrink]


                                    darklight_sub(surface)
                            else:
                                ps_surface["output_name_a"] = o_output_name_a_1
                                ps_surface["output_name_b"] = o_output_name_b_1

                                b_output.items[:] = [
                                    o_image_output_path,
                                    o_bake_image_sequence,
                                    ButtonSep(2),
                                    o_uv_layer,
                                    o_image_fileformat,
                                    o_use_premultiply,
                                    ButtonSep(1),
                                    b_paintmaps.w,
                                    b_wetmaps.w,
                                ]

                                def callback_sub(surface):
                                    uianim_effector_weights.update_with(fn_darklight_effector_weights)

                                    blocklis_canvas.upd_data()
                                    blocklis_canvas_media.upd_data()

                                    if ui_anim_data.library_state in {1, -1}: return
                                    if ui_state_sub == [ui_anim_data.library_state, surface.use_dissolve, surface.use_drying, surface.use_spread, surface.use_drip, surface.use_shrink, surface.use_output_a, surface.use_output_b]: return
                                    ui_state_sub[:] = [ui_anim_data.library_state, surface.use_dissolve, surface.use_drying, surface.use_spread, surface.use_drip, surface.use_shrink, surface.use_output_a, surface.use_output_b]


                                    darklight_sub(surface)

                                    if surface.use_output_a:
                                        o_output_name_a_1.light()
                                    else:
                                        o_output_name_a_1.dark()

                                    if surface.use_output_b:
                                        o_output_name_b_1.light()
                                    else:
                                        o_output_name_b_1.dark()

                            if is_cache_user:
                                self.items[:] = [b0.w, b1.w, b2.w, blocklis_caches.w, b_effects.w, b_initial_color.w, b_output.w]
                            else:
                                self.items[:] = [b0.w, b1.w, b2.w, b_effects.w, b_initial_color.w, b_output.w]
                            #|
                        elif surface_type == "DISPLACE":
                            if surface_format == "VERTEX":
                                ps_surface["depth_clamp"] = o_depth_clamp
                                b2.items[:] = [
                                    o_surface_type,
                                    ButtonSep(2),
                                    o_depth_clamp,
                                    o_displace_factor,
                                    o_use_incremental_displace,
                                    ButtonSep(2),
                                    o_brush_collection,
                                    o_brush_influence_scale,
                                    o_brush_radius_scale,
                                    ButtonSep(1),
                                    b_dissolve.w,
                                ]

                                if is_cache_user:
                                    self.items[:] = [b0.w, b1.w, b2.w, blocklis_caches.w]
                                else:
                                    self.items[:] = [b0.w, b1.w, b2.w]

                                def callback_sub(surface):
                                    uianim_cache.update_with(fn_darklight_cache)

                                    blocklis_canvas.upd_data()
                                    blocklis_canvas_media.upd_data()
                                    blocklis_caches.upd_data()
                                    blocklis_caches_media.upd_data()

                                    if ui_anim_data.library_state in {1, -1}: return
                                    if ui_state_sub == [ui_anim_data.library_state, surface.use_dissolve]: return
                                    ui_state_sub[:] = [ui_anim_data.library_state, surface.use_dissolve]


                                    if surface.use_dissolve:
                                        ps_surface["dissolve_speed"].light()
                                        ps_surface["use_dissolve_log"].light()
                                    else:
                                        ps_surface["dissolve_speed"].dark()
                                        ps_surface["use_dissolve_log"].dark()
                            else:
                                ps_surface["output_name_a"] = o_output_name_a_2
                                ps_surface["depth_clamp"] = o_depth_clamp_1
                                b2.items[:] = [
                                    o_surface_type,
                                    ButtonSep(2),
                                    o_use_incremental_displace,
                                    ButtonSep(2),
                                    o_brush_collection,
                                    o_brush_influence_scale,
                                    o_brush_radius_scale,
                                    ButtonSep(1),
                                    b_dissolve.w,
                                ]
                                b_output.items[:] = [
                                    o_image_output_path,
                                    o_bake_image_sequence,
                                    ButtonSep(2),
                                    o_uv_layer,
                                    o_image_fileformat,
                                    o_use_premultiply,
                                    ButtonSep(2),
                                    o_output_name_a_2,
                                    o_displace_type,
                                    o_depth_clamp_1,
                                ]
                                o_depth_clamp_1.set_text("Max Displace")

                                if is_cache_user:
                                    self.items[:] = [b0.w, b1.w, b2.w, b_output.w, blocklis_caches.w]
                                else:
                                    self.items[:] = [b0.w, b1.w, b2.w, b_output.w]

                                def callback_sub(surface):
                                    uianim_cache.update_with(fn_darklight_cache)

                                    blocklis_canvas.upd_data()
                                    blocklis_canvas_media.upd_data()
                                    blocklis_caches.upd_data()
                                    blocklis_caches_media.upd_data()

                                    if ui_anim_data.library_state in {1, -1}: return
                                    if ui_state_sub == [ui_anim_data.library_state, surface.use_dissolve]: return
                                    ui_state_sub[:] = [ui_anim_data.library_state, surface.use_dissolve]


                                    if surface.use_dissolve:
                                        ps_surface["dissolve_speed"].light()
                                        ps_surface["use_dissolve_log"].light()
                                    else:
                                        ps_surface["dissolve_speed"].dark()
                                        ps_surface["use_dissolve_log"].dark()
                            #|
                        elif surface_type == "WEIGHT":
                            b2.items[:] = [
                                o_surface_type,
                                ButtonSep(2),
                                o_brush_collection,
                                o_brush_influence_scale,
                                o_brush_radius_scale,
                                ButtonSep(1),
                                b_dissolve.w,
                            ]
                            ps_surface["output_name_a"] = o_output_name_a_3
                            b_output.items[:] = [
                                o_output_name_a_3,
                                ButtonSep(2),
                                blocklis_vertex_group,
                                blocklis_vertex_group_media,
                            ]

                            if is_cache_user:
                                self.items[:] = [b0.w, b1.w, b2.w, blocklis_caches.w, b_output.w]
                            else:
                                self.items[:] = [b0.w, b1.w, b2.w, b_output.w]

                            def callback_sub(surface):
                                uianim_cache.update_with(fn_darklight_cache)

                                blocklis_canvas.upd_data()
                                blocklis_canvas_media.upd_data()
                                blocklis_caches.upd_data()
                                blocklis_caches_media.upd_data()
                                blocklis_vertex_group.upd_data()
                                blocklis_vertex_group_media.upd_data()

                                if ui_anim_data.library_state in {1, -1}: return
                                if ui_state_sub == [ui_anim_data.library_state, surface.use_dissolve]: return
                                ui_state_sub[:] = [ui_anim_data.library_state, surface.use_dissolve]


                                if surface.use_dissolve:
                                    ps_surface["dissolve_speed"].light()
                                    ps_surface["use_dissolve_log"].light()
                                else:
                                    ps_surface["dissolve_speed"].dark()
                                    ps_surface["use_dissolve_log"].dark()
                            #|
                        else:
                            b2.items[:] = [
                                o_surface_type,
                                ButtonSep(2),
                                o_use_wave_open_border,
                                o_wave_timescale,
                                o_wave_speed,
                                ButtonSep(2),
                                o_wave_damping,
                                o_wave_spring,
                                o_wave_smoothness,
                                ButtonSep(2),
                                o_brush_collection,
                                o_brush_influence_scale,
                                o_brush_radius_scale,
                                ButtonSep(1),
                            ]

                            if is_cache_user:
                                self.items[:] = [b0.w, b1.w, b2.w, blocklis_caches.w]
                            else:
                                self.items[:] = [b0.w, b1.w, b2.w]

                            if surface_format != "VERTEX":
                                ps_surface["output_name_a"] = o_output_name_a_2
                                ps_surface["depth_clamp"] = o_depth_clamp_1
                                b_output.items[:] = [
                                    o_image_output_path,
                                    o_bake_image_sequence,
                                    ButtonSep(2),
                                    o_uv_layer,
                                    o_image_fileformat,
                                    o_use_premultiply,
                                    ButtonSep(2),
                                    o_output_name_a_2,
                                    o_depth_clamp_1,
                                ]
                                o_depth_clamp_1.set_text("Wave Clamp")
                                self.items.append(b_output.w)

                            def callback_sub(surface):
                                uianim_cache.update_with(fn_darklight_cache)

                                blocklis_canvas.upd_data()
                                blocklis_canvas_media.upd_data()
                                blocklis_caches.upd_data()
                                blocklis_caches_media.upd_data()

                                # if ui_anim_data.library_state in {1, -1}:
                            #|

                        ui_anim_data.tag_update()
                        uianim_settings.tag_update()
                        uianim_effector_weights.tag_update()
                        uianim_cache.tag_update()
                        self.redraw_from_headkey_with(search_data)
                        return True

                    if ui_lib_state[0] == ui_anim_data.library_state: pass
                    else:

                        ui_lib_state[0] = ui_anim_data.library_state

                        if ui_anim_data.library_state == 0:
                            o_output_name_a.set_ui_state_default()
                            o_output_name_a_1.set_ui_state_default()
                            o_output_name_a_2.set_ui_state_default()
                            o_output_name_a_3.set_ui_state_default()
                            o_output_name_b.set_ui_state_default()
                            o_output_name_b_1.set_ui_state_default()
                            o_depth_clamp.set_ui_state_default()
                            o_depth_clamp_1.set_ui_state_default()
                        elif ui_anim_data.library_state == 2:
                            o_output_name_a.set_ui_state_overridden()
                            o_output_name_a_1.set_ui_state_overridden()
                            o_output_name_a_2.set_ui_state_overridden()
                            o_output_name_a_3.set_ui_state_overridden()
                            o_output_name_b.set_ui_state_overridden()
                            o_output_name_b_1.set_ui_state_overridden()
                            o_depth_clamp.set_ui_state_overridden()
                            o_depth_clamp_1.set_ui_state_overridden()
                        else:
                            o_output_name_a.set_ui_state_link()
                            o_output_name_a_1.set_ui_state_link()
                            o_output_name_a_2.set_ui_state_link()
                            o_output_name_a_3.set_ui_state_link()
                            o_output_name_b.set_ui_state_link()
                            o_output_name_b_1.set_ui_state_link()
                            o_depth_clamp.set_ui_state_link()
                            o_depth_clamp_1.set_ui_state_link()

                    callback_sub(surf)

                def upd_data_callback():
                    ui_anim_data.update_with(fn_darklight)

                    if _allow_update is True:
                        uianim_settings.update_with(fn_darklight_settings)

                button_search.fn = self.r_bufn_search(upd_data_callback, [
                        ui_anim_data,
                        uianim_settings,
                        uianim_effector_weights,
                        uianim_cache,
                    ],
                    extra_buttons = list(extra_buttons) + [o_bake_image_sequence],
                    search_data = search_data)
        elif _ui_type == "BRUSH":
            def bufn_canvas_toggle():
                ob = self.w.active_object
                push_message = "Add brush"  if self.w.active_modifier.brush_settings is None else "Remove brush"
                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.dpaint.type_toggle(type="BRUSH")

                wrapButtonFn(bufn, ob, push_message=push_message)

            if self.w.active_modifier.brush_settings is None:
                b1 = ui.new_block(title="Settings")

                button_add = b1.function(RNA_add_brush, bufn_canvas_toggle, isdarkhard=True)

                def fn_darklight(md):
                    if md.ui_type == "BRUSH" and md.brush_settings is None:
                        if ui_anim_data.library_state == 1:
                            if button_add.isdark is False:
                                button_add.dark()
                        return


                    self.reinit_tab_with(search_data)
                    return True

                def upd_data_callback():
                    ui_anim_data.update_with(fn_darklight)

                button_search.fn = self.r_bufn_search(upd_data_callback, [
                        ui_anim_data,
                    ],
                    extra_buttons = [button_add],
                    search_data = search_data)
            else:
                def r_bru():
                    return self.w.active_modifier.brush_settings
                def bufn_color_ramp():
                    kill_evt_except()

                    OpColorRamp.md = r_bru()
                    OpColorRamp.attr = "paint_ramp"
                    bpy.ops.wm.vmd_color_ramp("INVOKE_DEFAULT")
                def bufn_velocity_ramp():
                    kill_evt_except()

                    OpColorRamp.md = r_bru()
                    OpColorRamp.attr = "velocity_ramp"
                    bpy.ops.wm.vmd_color_ramp("INVOKE_DEFAULT")

                button_delete = b0.r_function(RNA_remove_canvas, bufn_canvas_toggle, isdarkhard=True,
                    options={"icon_cls": GpuImg_TRASH, "icon_cls_dark": GpuImgNull})
                button_delete.set_align("R")

                uianim_settings = ui.set_pp(r_bru, bpytypes.DynamicPaintBrushSettings, self.rr_dph(".brush_settings"))
                b1 = ui.new_block(title=ButtonOverlay(None, Title("Settings"), button_delete))
                b1.prop("paint_color")
                b1.prop("paint_alpha", text="Alpha")
                b1.prop("paint_wetness", text="Wetness")
                b1.prop("use_absolute_alpha")
                b1.prop("use_paint_erase")

                b_source = ui.new_block(title="Source")
                ps = b_source.props
                r_prop = b_source.r_prop
                o_paint_source = r_prop("paint_source", text="Paint", options={"D_icon": {
                    "PARTICLE_SYSTEM": GpuImg_ID_PARTICLE,
                    "POINT": GpuImg_EMPTY_AXIS,
                    "DISTANCE": GpuImg_distance,
                    "VOLUME_DISTANCE": GpuImg_META_CUBE,
                    "VOLUME": GpuImg_MATCUBE}
                })
                o_paint_source.r_button_width = self.r_button_width_200
                o_particle_system = r_prop("particle_system", options={"r_items": lambda: self.w.active_object.particle_systems})
                o_solid_radius = r_prop("solid_radius", text="Effect Solid Radius")
                o_use_particle_radius = r_prop("use_particle_radius", text="Particle Radius")
                o_smooth_radius = r_prop("smooth_radius")
                o_paint_distance = r_prop("paint_distance", text="Distance")
                o_proximity_falloff = r_prop("proximity_falloff", options={"D_icon":{"SMOOTH": GpuImg_SPHERECURVE, "CONSTANT": GpuImg_NOCURVE, "RAMP": GpuImg_ID_PALETTE}})
                o_use_proximity_ramp_alpha = r_prop("use_proximity_ramp_alpha")
                o_color_ramp = b_source.r_function(RNA_dpaint_brush_color_ramp, bufn_color_ramp)
                o_use_proximity_project = r_prop("use_proximity_project")
                o_ray_direction = r_prop("ray_direction")
                o_invert_proximity = r_prop("invert_proximity")
                o_use_negative_volume = r_prop("use_negative_volume")

                b_velocity = ui.new_block(title="Velocity")
                po = b_velocity.prop
                po("use_velocity_color")
                po("use_velocity_alpha", text=("Multiply", "Alpha"))
                po("use_velocity_depth", text="Depth")
                b_velocity.sep(1)
                po("velocity_max")
                ps["velocity_max"].set_callback = update_scene_and_ref
                b_velocity.sep(2)
                b_velocity.function(RNA_dpaint_brush_color_ramp, bufn_velocity_ramp)
                b_velocity.sep(1)

                b_smudge = b_velocity.new_block(title=b_velocity.r_prop("use_smudge", text="Smudge", options={"HEAD"}))
                ps["use_smudge"].set_callback = update_scene_and_ref
                b_smudge.prop("smudge_strength", text="Strength")
                ps["smudge_strength"].set_callback = update_scene_and_ref

                b_waves = ui.new_block(title="Waves")
                b_waves.prop("wave_type", text="Type")
                b_waves.prop("wave_factor")
                b_waves.prop("wave_clamp")
                ps["wave_type"].set_callback = update_scene_and_ref
                ps["wave_factor"].set_callback = update_scene_and_ref
                ps["wave_clamp"].set_callback = update_scene_and_ref

                _allow_update = True
                ui_state_format = []
                ui_state_sub = []
                # callback_sub = N1

                def fn_darklight(md):
                    if md.ui_type == "BRUSH" and md.brush_settings is not None: return


                    nonlocal _allow_update
                    _allow_update = False
                    self.reinit_tab_with(search_data)
                    return True

                def fn_darklight_settings(bru):
                    if ui_state_format == [bru.paint_source]: pass
                    else:
                        paint_source = bru.paint_source
                        ui_state_format[:] = [paint_source]


                        if paint_source == "PARTICLE_SYSTEM":
                            b_source.items[:] = [
                                o_paint_source,
                                ButtonSep(2),
                                o_particle_system,
                                o_solid_radius,
                                o_use_particle_radius,
                                o_smooth_radius,
                            ]
                        elif paint_source == "POINT":
                            b_source.items[:] = [
                                o_paint_source,
                                ButtonSep(2),
                                o_paint_distance,
                                o_proximity_falloff,
                                o_color_ramp,
                                o_use_proximity_ramp_alpha,
                            ]
                        elif paint_source == "DISTANCE":
                            b_source.items[:] = [
                                o_paint_source,
                                ButtonSep(2),
                                o_paint_distance,
                                o_proximity_falloff,
                                o_use_proximity_project,
                                o_ray_direction,
                                o_color_ramp,
                                o_use_proximity_ramp_alpha,
                            ]
                        elif paint_source == "VOLUME_DISTANCE":
                            b_source.items[:] = [
                                o_paint_source,
                                ButtonSep(2),
                                o_paint_distance,
                                o_proximity_falloff,
                                o_invert_proximity,
                                o_use_negative_volume,
                                o_use_proximity_project,
                                o_ray_direction,
                                o_color_ramp,
                                o_use_proximity_ramp_alpha,
                            ]
                        else:
                            b_source.items[:] = [
                                o_paint_source,
                                ButtonSep(2),
                            ]

                        ui_anim_data.tag_update()
                        uianim_settings.tag_update()
                        self.redraw_from_headkey_with(search_data)
                        return True

                    if ui_anim_data.library_state in {1, -1}: return
                    if ui_state_sub == [ui_anim_data.library_state, bru.proximity_falloff, bru.use_proximity_project, (True if bru.particle_system else False), bru.use_particle_radius, (bru.use_velocity_alpha or bru.use_velocity_color or bru.use_velocity_depth), bru.use_smudge, bru.wave_type]: return
                    ui_state_sub[:] = [ui_anim_data.library_state, bru.proximity_falloff, bru.use_proximity_project, (True if bru.particle_system else False), bru.use_particle_radius, (bru.use_velocity_alpha or bru.use_velocity_color or bru.use_velocity_depth), bru.use_smudge, bru.wave_type]


                    if bru.proximity_falloff == "RAMP":
                        o_color_ramp.light()
                        o_use_proximity_ramp_alpha.light()
                    else:
                        o_color_ramp.dark()
                        o_use_proximity_ramp_alpha.dark()

                    if bru.use_proximity_project:
                        o_ray_direction.light()
                    else:
                        o_ray_direction.dark()

                    if bru.particle_system:
                        if bru.use_particle_radius:
                            o_solid_radius.dark()
                        else:
                            o_solid_radius.light()

                        o_use_particle_radius.light()
                        o_smooth_radius.light()
                    else:
                        o_solid_radius.dark()
                        o_use_particle_radius.dark()
                        o_smooth_radius.dark()

                    if bru.use_velocity_alpha or bru.use_velocity_color or bru.use_velocity_depth:
                        ps["velocity_max"].light()
                    else:
                        ps["velocity_max"].dark()

                    if bru.use_smudge:
                        ps["smudge_strength"].light()
                    else:
                        ps["smudge_strength"].dark()

                    if bru.wave_type == "REFLECT":
                        ps["wave_factor"].dark()
                        ps["wave_clamp"].dark()
                    else:
                        ps["wave_factor"].light()
                        ps["wave_clamp"].light()

                def upd_data_callback():
                    ui_anim_data.update_with(fn_darklight)

                    if _allow_update is True:
                        uianim_settings.update_with(fn_darklight_settings)

                button_search.fn = self.r_bufn_search(upd_data_callback, [
                        ui_anim_data,
                        uianim_settings,
                    ],
                    extra_buttons = [o_color_ramp, b_velocity],
                    search_data = search_data)
        else:
            def fn_darklight(md):
                if md.ui_type in {"CANVAS", "BRUSH"}:

                    self.reinit_tab_with(search_data)
                    return True

            def upd_data_callback():
                ui_anim_data.update_with(fn_darklight)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                ],
                extra_buttons = None,
                search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_EDGE_SPLIT(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("use_edge_angle")
        b0.prop("split_angle")
        b0.prop("use_edge_sharp")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_edge_angle]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_edge_angle]

            if ui_anim_data.library_state == 1: return

            if md.use_edge_angle:
                props["split_angle"].light()
            else:
                props["split_angle"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_EXPLODE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_search("particle_uv", GpuImg_GROUP_UVS, self.r_object_uvs)
        b0.sep(2)
        b0.prop_flag(["show_alive", "show_dead", "show_unborn"], text="Show", options={"NAMES": ("Alive", "Dead", "Unborn")})
        b0.sep(2)
        b0.prop("use_edge_cut")
        b0.prop("use_size")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        props["vertex_group"].set_callback = update_scene_and_ref

        r_button_width = self.r_button_width_150
        props["particle_uv"].r_button_width = r_button_width
        props["show_alive"].r_button_width = r_button_width
        props["use_edge_cut"].r_button_width = r_button_width
        props["use_size"].r_button_width = r_button_width
        props["vertex_group"].r_button_width = r_button_width

        b0.sep(1)
        b0.prop("protect")
        b0.function(RNA_EXPLODE_refresh, self.bufn_EXPLODE_refresh)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
                props["protect"].light()
            else:
                props["invert_vertex_group"].dark()
                props["protect"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_FLUID(self):

        if not bpy.app.build_options.fluid:
            b0 = Blocks(self)
            b0.buttons = [Title("  Built without Fluid modifier")]
            self.items[:] = [b0]
            return

        # <<< 1copy (0deffluid,, $$)
        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})

        search_data = self.search_data
        search_data.init_with(button_search)

        button_fluid_type = b0.r_prop("fluid_type")
        b0.items.append(ButtonOverlay(button_fluid_type.w, button_search, button_fluid_type))


        _fluid_type = self.w.active_modifier.fluid_type

        if _fluid_type == "DOMAIN":
            def check_domain_has_unbaked_guide(domain):
                return (
                    domain.use_guide and not domain.has_cache_baked_guide and
                    ((domain.guide_source == 'EFFECTOR') or
                        (domain.guide_source == 'DOMAIN' and not domain.guide_parent))
                )
            def r_domain():
                return self.w.active_modifier.domain_settings
            def r_effector_weights():
                domain_settings = self.w.active_modifier.domain_settings
                if domain_settings: return domain_settings.effector_weights
                return None
            def bufn_bake_all():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any or domain.has_cache_baked_data: return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.bake_all("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_free_all():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if not domain.has_cache_baked_data: return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.free_all("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_bake_data():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any or domain.has_cache_baked_data: return
                if check_domain_has_unbaked_guide(domain):
                    report("Need bake the Guides first or disable it", ty="WARNING")
                    return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.bake_data("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_free_data():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if not domain.has_cache_baked_data: return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.free_data("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_bake_guides():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if domain.has_cache_baked_guide: return
                if not domain.use_guide:
                    report("Need to enable Use Guides", ty="WARNING")
                    return
                if domain.guide_source != 'EFFECTOR':
                    report("Guides Source set to Effector first", ty="WARNING")
                    return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.bake_guides("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_free_guides():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if not domain.has_cache_baked_guide: return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.free_guides("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_bake_noise():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if domain.has_cache_baked_noise: return
                if not domain.use_noise:
                    report("Need to enable Use Noise", ty="WARNING")
                    return
                if not domain.cache_resumable:
                    report("Need to enable Resumable", ty="WARNING")
                    return
                if not domain.has_cache_baked_data:
                    report("Need bake data first", ty="WARNING")
                    return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.bake_noise("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_free_noise():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if not domain.has_cache_baked_noise: return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.free_noise("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_bake_mesh():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if domain.is_cache_baking_mesh: return
                if domain.has_cache_baked_mesh: return
                if not domain.use_mesh:
                    report("Need to enable Use Mesh", ty="WARNING")
                    return
                if not domain.cache_resumable:
                    report("Need to enable Resumable", ty="WARNING")
                    return
                if not domain.has_cache_baked_data:
                    report("Need bake data first", ty="WARNING")
                    return
                if ob.mode != "OBJECT":
                    report("Need Object Mode", ty="WARNING")
                    return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.bake_mesh("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_free_mesh():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if domain.is_cache_baking_mesh: return
                if not domain.has_cache_baked_mesh: return
                if ob.mode != "OBJECT":
                    report("Need Object Mode", ty="WARNING")
                    return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.free_mesh("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_bake_particles():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if domain.is_cache_baking_particles: return
                if domain.has_cache_baked_particles: return
                if domain.use_spray_particles or domain.use_bubble_particles or domain.use_foam_particles or domain.use_tracer_particles: pass
                else:
                    report("Need to enable Use Spray/Bubble/Foam/Tracer", ty="WARNING")
                    return
                if not domain.cache_resumable:
                    report("Need to enable Resumable", ty="WARNING")
                    return
                if not domain.has_cache_baked_data:
                    report("Need bake data first", ty="WARNING")
                    return
                if ob.mode != "OBJECT":
                    report("Need Object Mode", ty="WARNING")
                    return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.bake_particles("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_free_particles():
                ob = self.r_object()
                if not ob: return

                try: domain = r_domain()
                except: return

                if domain.is_cache_baking_any: return
                if domain.is_cache_baking_particles: return
                if not domain.has_cache_baked_particles: return
                if ob.mode != "OBJECT":
                    report("Need Object Mode", ty="WARNING")
                    return

                def bufn():
                    with bpy.context.temp_override(object=ob):
                        bpy.ops.fluid.free_particles("INVOKE_DEFAULT")

                jumpout_head()
                wrapButtonFn(bufn, ob)
            def bufn_color_ramp():
                kill_evt_except()

                OpColorRamp.md = r_domain()
                OpColorRamp.attr = "color_ramp"
                bpy.ops.wm.vmd_color_ramp("INVOKE_DEFAULT")

            uianim = ui.set_pp(r_domain, bpytypes.FluidDomainSettings, self.rr_dph(".domain_settings"))
            b_settings = ui.new_block(title="Settings")
            rprop = b_settings.r_prop
            ps = uianim.props
            o_domain_type = b_settings.r_prop_flag("domain_type", isdarkhard=True)
            o_resolution_max = rprop("resolution_max", text="Resolution Divisions", isdarkhard=True)
            o_time_scale = rprop("time_scale", isdarkhard=True)
            o_use_adaptive_timesteps = rprop("use_adaptive_timesteps", text="Adaptive Time Steps", isdarkhard=True)
            o_cfl_condition = rprop("cfl_condition", text="CFL Number", isdarkhard=True)
            o_timesteps_max = rprop("timesteps_max", text="Timesteps Maximum", isdarkhard=True)
            o_timesteps_min = rprop("timesteps_min", text="Minimum", isdarkhard=True)
            o_gravity = rprop("gravity", isdarkhard=True)
            o_clipping = rprop("clipping", text="Empty Space", isdarkhard=True)
            o_delete_in_obstacle = rprop("delete_in_obstacle", text="Delete in Obstacle", isdarkhard=True)

            b_border_collisions = b_settings.new_block(title="Border Collisions")
            po = b_border_collisions.prop
            po("use_collision_border_front", isdarkhard=True)
            po("use_collision_border_back", isdarkhard=True)
            po("use_collision_border_right", isdarkhard=True)
            po("use_collision_border_left", isdarkhard=True)
            po("use_collision_border_top", isdarkhard=True)
            po("use_collision_border_bottom", isdarkhard=True)

            b_adaptive_domain = b_settings.new_block(title=rprop("use_adaptive_domain", isdarkhard=True, options={"HEAD"}))
            po = b_adaptive_domain.prop
            po("additional_res", text="Add Resolution", isdarkhard=True)
            po("adapt_margin", isdarkhard=True)
            b_adaptive_domain.sep(2)
            po("adapt_threshold", text="Threshold", isdarkhard=True)

            b_settings_gas = [
                o_domain_type,
                o_resolution_max,
                o_time_scale,
                o_use_adaptive_timesteps,
                o_cfl_condition,
                o_timesteps_max,
                o_timesteps_min,
                ButtonSep(2),
                o_gravity,
                o_clipping,
                o_delete_in_obstacle,
                ButtonSep(1),
                b_border_collisions.w,
                b_adaptive_domain.w,
            ]

            b_gas = ui.new_block(title="Gas")
            b_gas.prop("alpha", isdarkhard=True)
            b_gas.prop("beta", text="Heat", isdarkhard=True)
            b_gas.prop("vorticity", isdarkhard=True)
            b_gas.sep(1)

            b_dissolve = b_gas.new_block(title=b_gas.r_prop("use_dissolve_smoke", text="Dissolve", isdarkhard=True, options={"HEAD"}))
            b_dissolve.prop("dissolve_speed", text="Time", isdarkhard=True)
            b_dissolve.prop("use_dissolve_smoke_log", text="Slow", isdarkhard=True)

            b_noise = b_gas.new_block(title=b_gas.r_prop("use_noise", text="Noise", isdarkhard=True, options={"HEAD"}))
            b_noise.prop("noise_scale", text="Upres Factor", isdarkhard=True)
            b_noise.prop("noise_strength", isdarkhard=True)
            b_noise.prop("noise_pos_scale", isdarkhard=True)
            b_noise.prop("noise_time_anim", isdarkhard=True)

            b_fire = b_gas.new_block(title="Fire")
            b_fire.prop("burning_rate", text="Reaction Speed", isdarkhard=True)
            b_fire.sep(1)
            b_fire.prop("flame_smoke", text="Flame Smoke", isdarkhard=True)
            b_fire.prop("flame_vorticity", isdarkhard=True)
            b_fire.sep(1)
            b_fire.prop("flame_max_temp", text="Temperature Maximum", isdarkhard=True)
            b_fire.prop("flame_ignition", isdarkhard=True)
            b_fire.sep(1)
            b_fire.prop("flame_smoke_color", isdarkhard=True)

            b_guides = ui.new_block(title=ui.r_prop("use_guide", text="Guides", isdarkhard=True, options={"HEAD"}))
            b_guides.prop("guide_alpha", text="Weight", isdarkhard=True)
            b_guides.prop("guide_beta", text="Size", isdarkhard=True)
            b_guides.prop("guide_vel_factor", text="Velocity Factor", isdarkhard=True)
            b_guides.prop("guide_source", text="Velocity Source", isdarkhard=True)
            b_guides.prop("guide_parent", text="Guide Parent", isdarkhard=True, options={"ID":"OBJECT"})

            b_collections = ui.new_block(title="Collections")
            b_collections.prop("fluid_group", text="Flow", options={"ID":"COLLECTION"})
            b_collections.prop("effector_group", text="Effector", options={"ID":"COLLECTION"})

            b_cache = ui.new_block(title="Cache")
            rp = b_cache.r_prop
            o_cache_directory = rp("cache_directory", text="Path")
            o_cache_directory.set_align("FULL")
            o_cache_frame_start = rp("cache_frame_start", text="Frame Start")
            o_cache_frame_start.set_callback = update_scene_and_ref
            o_cache_frame_end = rp("cache_frame_end")
            o_cache_frame_end.set_callback = update_scene_and_ref
            o_cache_frame_offset = rp("cache_frame_offset", isdarkhard=True)
            o_cache_frame_offset.set_callback = update_scene_and_ref
            o_cache_type = rp("cache_type")
            o_cache_resumable = rp("cache_resumable", text="Resumable", isdarkhard=True)
            o_cache_data_format = rp("cache_data_format", text="Format Volumes", isdarkhard=True)
            o_cache_data_format.rna = RNA_cache_data_format
            o_cache_data_format.enum_items = RNA_cache_data_format.enum_items
            o_cache_mesh_format = rp("cache_mesh_format", text="Meshes", isdarkhard=True)
            o_cache_mesh_format.rna = RNA_cache_mesh_format
            o_cache_mesh_format.enum_items = RNA_cache_mesh_format.enum_items
            r_function = b_cache.r_function
            o_button_bake_all = r_function([RNA_fluid_bake_all, RNA_fluid_free_all], [bufn_bake_all, bufn_free_all], isdarkhard=True)
            o_button_bake_data = r_function([RNA_fluid_bake_data, RNA_fluid_free_data], [bufn_bake_data, bufn_free_data], isdarkhard=True)
            o_button_bake_guides = r_function([RNA_fluid_bake_guides, RNA_fluid_free_guides], [bufn_bake_guides, bufn_free_guides], isdarkhard=True)
            o_button_bake_noise = r_function([RNA_fluid_bake_noise, RNA_fluid_free_noise], [bufn_bake_noise, bufn_free_noise], isdarkhard=True)
            o_button_bake_mesh = r_function([RNA_fluid_bake_mesh, RNA_fluid_free_mesh], [bufn_bake_mesh, bufn_free_mesh], isdarkhard=True)
            o_button_bake_particles = r_function([RNA_fluid_bake_particles, RNA_fluid_free_particles], [bufn_bake_particles, bufn_free_particles], isdarkhard=True)

            b_export = b_cache.new_block(title="Advanced")
            b_export.prop("openvdb_cache_compress_type", text="Compression Volumes", isdarkhard=True)
            b_export.prop("openvdb_data_depth", text="Precision Volumes", isdarkhard=True)

            b_cache_gas = [
                o_cache_directory,
                ButtonSep(2),
                o_cache_frame_start,
                o_cache_frame_end,
                o_cache_frame_offset,
                ButtonSep(2),
                o_cache_type,
                o_cache_resumable,
                o_cache_data_format,
                ButtonSep(2),
                o_button_bake_all,
                o_button_bake_data,
                o_button_bake_guides,
                o_button_bake_noise,
                ButtonSep(1),
                b_export.w,
            ]
            b_cache_liquid = [
                o_cache_directory,
                ButtonSep(2),
                o_cache_frame_start,
                o_cache_frame_end,
                o_cache_frame_offset,
                ButtonSep(2),
                o_cache_type,
                o_cache_resumable,
                o_cache_data_format,
                o_cache_mesh_format,
                ButtonSep(2),
                o_button_bake_all,
                o_button_bake_data,
                o_button_bake_guides,
                o_button_bake_particles,
                o_button_bake_mesh,
                ButtonSep(1),
                b_export.w,
            ]

            uianim_effector_weights, fn_darklight_effector_weights = ui_effector_weights("", ui, r_effector_weights, self.rr_dph(".domain_settings.effector_weights"))
            block_effector_weights = self.items[-1]

            b_vpd = ui.new_block(title="Viewport Display")
            b_vpd.prop("display_thickness", isdarkhard=True)
            b_vpd.prop("display_interpolation", isdarkhard=True)
            b_vpd.prop("slice_per_voxel", isdarkhard=True)

            b_vpd_slice = b_vpd.new_block(b_vpd.r_prop("use_slice", isdarkhard=True, options={"HEAD"}))
            b_vpd_slice.prop("slice_axis", isdarkhard=True)
            b_vpd_slice.prop("slice_depth", isdarkhard=True)
            b_vpd_slice.sep(1)

            b_vpd_gridlines = b_vpd_slice.new_block(b_vpd_slice.r_prop("show_gridlines", isdarkhard=True, options={"HEAD"}))
            b_vpd_gridlines.prop("gridlines_color_field", text="Color Gridlines", isdarkhard=True)
            b_vpd_gridlines.prop("gridlines_lower_bound", isdarkhard=True)
            b_vpd_gridlines.prop("gridlines_upper_bound", isdarkhard=True)
            b_vpd_gridlines.prop("gridlines_range_color", isdarkhard=True)
            b_vpd_gridlines.prop("gridlines_cell_filter", isdarkhard=True)
            b_vpd_gridlines_label0 = b_vpd_gridlines.label([""])

            b_vpd_grid = b_vpd.new_block(title=b_vpd.r_prop("use_color_ramp", isdarkhard=True, options={"HEAD"}))
            b_vpd_grid.prop("color_ramp_field", isdarkhard=True)
            b_vpd_grid.prop("color_ramp_field_scale", isdarkhard=True)
            o_color_ramp = b_vpd_grid.function(RNA_fluid_color_ramp, bufn_color_ramp)

            b_vpd_vector = b_vpd.new_block(title=b_vpd.r_prop("show_velocity", text="Vector Display", isdarkhard=True, options={"HEAD"}))
            po = b_vpd_vector.prop
            po("vector_display_type", text="Display As", isdarkhard=True)
            po("vector_scale_with_magnitude", isdarkhard=True)
            po("vector_field", isdarkhard=True)
            po("vector_scale", isdarkhard=True)
            b_vpd_vector.prop_flag(["vector_show_mac_x", "vector_show_mac_y", "vector_show_mac_z"], text="MAC Grid", isdarkhard=True, options={"NAMES": "XYZ"})
            o_vpd_vector_label0 = b_vpd_vector.label([""])

            b_render = ui.new_block(title="Render")
            b_render.prop("velocity_scale", isdarkhard=True)

            b_liquid = ui.new_block(title=ui.r_prop("use_flip_particles", text="Liquid", isdarkhard=True, options={"HEAD"}))
            po = b_liquid.prop
            b_liquid.prop_flag("simulation_method", isdarkhard=True)
            po("flip_ratio", text="FLIP Ratio", isdarkhard=True)
            po("sys_particle_maximum", text="System Maximum", isdarkhard=True)
            po("particle_radius", text="Particle Radius", isdarkhard=True)
            po("particle_number", text="Sampling", isdarkhard=True)
            po("particle_randomness", text="Randomness", isdarkhard=True)
            po("particle_max", text="Particles Maximum", isdarkhard=True)
            po("particle_min", text="Minimum", isdarkhard=True)
            b_liquid.sep(2)
            po("particle_band_width", text="Narrow Band Width", isdarkhard=True)
            po("use_fractions", text="Fractional Obstacles", isdarkhard=True)
            po("fractions_distance", text="Obstacle Distance", isdarkhard=True)
            po("fractions_threshold", text="Threshold", isdarkhard=True)
            b_liquid.sep(1)

            b_diffusion = b_liquid.new_block(title=b_liquid.r_prop("use_diffusion", text="Diffusion", isdarkhard=True, options={"HEAD"}))
            b_diffusion.prop("viscosity_base", text="Base", isdarkhard=True)
            b_diffusion.prop("viscosity_exponent", text="Exponent", isdarkhard=True)
            b_diffusion.prop("surface_tension", text="Surface Tension", isdarkhard=True)
            b_diffusion.sep(1)

            b_viscosity = b_diffusion.new_block(title=b_diffusion.r_prop("use_viscosity", text="High Viscosity Solver", isdarkhard=True, options={"HEAD"}))
            b_viscosity.prop("viscosity_value", text="Strength", isdarkhard=True)

            b_particles = b_liquid.new_block(title="Particles")
            po = b_particles.prop
            b_particles.prop_flag(["use_spray_particles", "use_foam_particles", "use_bubble_particles"], text="Use", isdarkhard=True, options={"NAMES": ("Spray", "Foam", "Bubble")})
            ps["use_spray_particles"].r_button_width = self.r_button_width_166
            b_particles.sep(2)
            po("sndparticle_combined_export", isdarkhard=True)
            po("particle_scale", text="Upres Factor", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_potential_max_wavecrest", text="Wave Crest Potential Max", isdarkhard=True)
            po("sndparticle_potential_min_wavecrest", text="Minimum", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_potential_max_trappedair", text="Trapped Air Potential Max", isdarkhard=True)
            po("sndparticle_potential_min_trappedair", text="Minimum", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_potential_max_energy", text="Kinetic Energy Potential Max", isdarkhard=True)
            po("sndparticle_potential_min_energy", text="Minimum", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_potential_radius", text="Potential Radius", isdarkhard=True)
            po("sndparticle_update_radius", text="Particle Update Radius", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_sampling_wavecrest", text="Wave Crest Particle Sampling", isdarkhard=True)
            po("sndparticle_sampling_trappedair", text="Trapped Air Particle Sampling", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_life_max", text="Particle Life Maximum", isdarkhard=True)
            po("sndparticle_life_min", text="Minimum", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_bubble_buoyancy", text="Bubble Buoyancy", isdarkhard=True)
            po("sndparticle_bubble_drag", text="Bubble Drag", isdarkhard=True)
            b_particles.sep(2)
            po("sndparticle_boundary", text="Particles in Boundary", isdarkhard=True)

            b_mesh = b_liquid.new_block(title=b_liquid.r_prop("use_mesh", text="Mesh", isdarkhard=True, options={"HEAD"}))
            po = b_mesh.prop
            po("mesh_scale", text="Upres Factor", isdarkhard=True)
            po("mesh_particle_radius", text="Particle Radius", isdarkhard=True)
            po("use_speed_vectors", text="Speed Vectors", isdarkhard=True)
            b_mesh.sep(2)
            po("mesh_generator", text="Mesh Generator", isdarkhard=True)
            po("mesh_smoothen_pos", text="Smoothing Positive", isdarkhard=True)
            po("mesh_smoothen_neg", text="Negative", isdarkhard=True)
            po("mesh_concave_upper", text="Concavity Upper", isdarkhard=True)
            po("mesh_concave_lower", text="Lower", isdarkhard=True)

            items_gas = [
                b0.w,
                b_settings.w,
                b_gas.w,
                b_guides.w,
                b_collections.w,
                b_cache.w,
                block_effector_weights,
                b_vpd.w,
                b_render.w,
            ]
            items_liquid = [
                b0.w,
                b_settings.w,
                b_liquid.w,
                b_guides.w,
                b_collections.w,
                b_cache.w,
                block_effector_weights,
                b_vpd.w,
            ]
            extra_buttons = [
                o_button_bake_all,
                o_button_bake_data,
                o_button_bake_guides,
                o_button_bake_noise,
                o_button_bake_mesh,
                o_button_bake_particles,
                o_color_ramp,
            ]


            ui_type = [""]
            ui_state = []

            def fn_darklight(dom):
                if ui_type[0] == dom.domain_type: pass
                else:
                    ui_type[0] = dom.domain_type


                    if dom.domain_type == "GAS":
                        b_settings.items[:] = b_settings_gas
                        b_cache.items[:] = b_cache_gas

                        b_adaptive_domain.w.light()

                        o_cache_mesh_format.dark()
                        o_button_bake_noise.light()
                        o_button_bake_particles.dark()
                        o_button_bake_mesh.dark()

                        ps["color_ramp_field"].rna = RNA_color_ramp_field_gas
                        ps["color_ramp_field"].enum_items = RNA_color_ramp_field_gas.enum_items

                        b_gas.w.light()
                        b_liquid.w.dark()
                        b_render.w.light()

                        self.items[:] = items_gas
                    else:
                        b_settings.items[:] = b_settings_gas[ : -1]
                        b_cache.items[:] = b_cache_liquid

                        b_adaptive_domain.w.dark()

                        o_cache_mesh_format.light()
                        o_button_bake_noise.dark()
                        o_button_bake_particles.light()
                        o_button_bake_mesh.light()

                        ps["color_ramp_field"].rna = RNA_color_ramp_field_liquid
                        ps["color_ramp_field"].enum_items = RNA_color_ramp_field_liquid.enum_items

                        b_gas.w.dark()
                        b_liquid.w.light()
                        b_render.w.dark()

                        self.items[:] = items_liquid

                    ui_anim_data.tag_update()
                    uianim.tag_update()
                    uianim_effector_weights.tag_update()
                    self.redraw_from_headkey_with(search_data)
                    return True

                if ui_state == [ui_anim_data.library_state, (True if dom else False), dom.is_cache_baking_any, dom.has_cache_baked_any, dom.has_cache_baked_noise, dom.use_guide, dom.guide_source, dom.use_adaptive_domain, dom.use_dissolve_smoke, dom.use_noise, dom.cache_type, dom.has_cache_baked_guide, dom.simulation_method, dom.use_fractions, dom.use_viscosity, dom.use_diffusion, (dom.use_spray_particles or dom.use_foam_particles or dom.use_bubble_particles), dom.sndparticle_combined_export, dom.has_cache_baked_particles, dom.has_cache_baked_mesh, dom.use_mesh, dom.mesh_generator, dom.cache_data_format, dom.use_adaptive_timesteps, bpy.context.scene.use_gravity, dom.has_cache_baked_data, dom.use_color_ramp, dom.color_ramp_field, dom.use_slice, dom.display_interpolation, dom.show_gridlines, dom.gridlines_color_field, dom.show_velocity, dom.vector_display_type, dom.vector_field]: return
                ui_state[:] = [ui_anim_data.library_state, (True if dom else False), dom.is_cache_baking_any, dom.has_cache_baked_any, dom.has_cache_baked_noise, dom.use_guide, dom.guide_source, dom.use_adaptive_domain, dom.use_dissolve_smoke, dom.use_noise, dom.cache_type, dom.has_cache_baked_guide, dom.simulation_method, dom.use_fractions, dom.use_viscosity, dom.use_diffusion, (dom.use_spray_particles or dom.use_foam_particles or dom.use_bubble_particles), dom.sndparticle_combined_export, dom.has_cache_baked_particles, dom.has_cache_baked_mesh, dom.use_mesh, dom.mesh_generator, dom.cache_data_format, dom.use_adaptive_timesteps, bpy.context.scene.use_gravity, dom.has_cache_baked_data, dom.use_color_ramp, dom.color_ramp_field, dom.use_slice, dom.display_interpolation, dom.show_gridlines, dom.gridlines_color_field, dom.show_velocity, dom.vector_display_type, dom.vector_field]

                if ui_anim_data.library_state in {1, -1}: return

                if dom.is_cache_baking_any or dom.has_cache_baked_any or (dom.use_guide and dom.guide_source == 'EFFECTOR'):
                    b_adaptive_domain.w.dark()
                else:
                    if dom.use_adaptive_domain:
                        b_adaptive_domain.w.light()
                    else:
                        b_adaptive_domain.w.dark()

                    ps["use_adaptive_domain"].light()

                if dom:
                    if dom.domain_type == "GAS":
                        o_clipping.light()
                        b_gas.w.light()

                        if dom.use_dissolve_smoke:
                            ps["dissolve_speed"].light()
                            ps["use_dissolve_smoke_log"].light()
                        else:
                            ps["dissolve_speed"].dark()
                            ps["use_dissolve_smoke_log"].dark()
                    else:
                        o_clipping.dark()
                        b_liquid.w.light()

                        if dom.simulation_method == "FLIP":
                            ps["flip_ratio"].light()
                        else:
                            ps["flip_ratio"].dark()

                        if dom.use_fractions:
                            ps["fractions_distance"].light()
                            ps["fractions_threshold"].light()
                        else:
                            ps["fractions_distance"].dark()
                            ps["fractions_threshold"].dark()

                        if dom.has_cache_baked_any:
                            b_diffusion.w.dark()
                        else:
                            b_diffusion.w.light()

                            if dom.use_viscosity:
                                ps["viscosity_value"].light()
                            else:
                                ps["viscosity_value"].dark()

                            if dom.use_diffusion:
                                ps["viscosity_base"].light()
                                ps["viscosity_exponent"].light()
                                ps["surface_tension"].light()
                            else:
                                ps["viscosity_base"].dark()
                                ps["viscosity_exponent"].dark()
                                ps["surface_tension"].dark()
                else:
                    if dom.domain_type == "GAS":
                        b_gas.w.dark()
                    else:
                        b_liquid.w.dark()

                        if dom.is_cache_baking_any:
                            ps["use_flip_particles"].dark()
                        else:
                            ps["use_flip_particles"].light()

                if dom.domain_type == "GAS":
                    if dom.is_cache_baking_any or dom.has_cache_baked_noise:
                        b_noise.w.dark()
                    else:
                        if dom.use_noise:
                            b_noise.w.light()
                        else:
                            b_noise.w.dark(use_head=False)
                            ps["use_noise"].light()

                    if dom.cache_type == "ALL":
                        o_cache_frame_offset.light()
                        o_button_bake_all.light(0)
                        o_button_bake_all.dark(1)
                        o_button_bake_data.dark()
                        o_button_bake_guides.dark()
                        o_button_bake_noise.dark()
                    elif dom.cache_type == "MODULAR":
                        o_cache_frame_offset.light()
                        o_button_bake_all.dark()
                        o_button_bake_data.light()

                        if dom.has_cache_baked_guide:
                            o_button_bake_guides.dark(0)
                            o_button_bake_guides.light(1)
                        else:
                            o_button_bake_guides.light(0)
                            o_button_bake_guides.dark(1)

                        if dom.has_cache_baked_noise:
                            o_button_bake_noise.dark(0)
                            o_button_bake_noise.light(1)
                        else:
                            o_button_bake_noise.light(0)
                            o_button_bake_noise.dark(1)
                    else:
                        o_cache_frame_offset.dark()

                        o_button_bake_all.dark()
                        o_button_bake_data.dark()
                        o_button_bake_guides.dark()
                        o_button_bake_noise.dark()

                    o_cache_resumable.light()
                    o_cache_data_format.light()
                else:
                    if dom.is_cache_baking_any:
                        b_particles.w.dark()
                        b_mesh.w.dark()
                    else:
                        ps["use_mesh"].light()
                        ps["sndparticle_combined_export"].light()

                        if dom.use_spray_particles or dom.use_foam_particles or dom.use_bubble_particles:
                            if dom.sndparticle_combined_export in {'OFF', 'FOAM + BUBBLES'}:
                                ps["use_spray_particles"].light()
                            else:
                                ps["use_spray_particles"].dark()
                        else:
                            ps["use_spray_particles"].dark()

                        if dom.has_cache_baked_particles:
                            ps["particle_scale"].dark()
                            ps["sndparticle_potential_max_wavecrest"].dark()
                            ps["sndparticle_potential_min_wavecrest"].dark()
                            ps["sndparticle_potential_max_trappedair"].dark()
                            ps["sndparticle_potential_min_trappedair"].dark()
                            ps["sndparticle_potential_max_energy"].dark()
                            ps["sndparticle_potential_min_energy"].dark()
                            ps["sndparticle_potential_radius"].dark()
                            ps["sndparticle_update_radius"].dark()
                            ps["sndparticle_sampling_wavecrest"].dark()
                            ps["sndparticle_sampling_trappedair"].dark()
                            ps["sndparticle_life_max"].dark()
                            ps["sndparticle_life_min"].dark()
                            ps["sndparticle_bubble_buoyancy"].dark()
                            ps["sndparticle_bubble_drag"].dark()
                            ps["sndparticle_boundary"].dark()
                        else:
                            ps["particle_scale"].light()
                            ps["sndparticle_potential_max_wavecrest"].light()
                            ps["sndparticle_potential_min_wavecrest"].light()
                            ps["sndparticle_potential_max_trappedair"].light()
                            ps["sndparticle_potential_min_trappedair"].light()
                            ps["sndparticle_potential_max_energy"].light()
                            ps["sndparticle_potential_min_energy"].light()
                            ps["sndparticle_potential_radius"].light()
                            ps["sndparticle_update_radius"].light()
                            ps["sndparticle_sampling_wavecrest"].light()
                            ps["sndparticle_sampling_trappedair"].light()
                            ps["sndparticle_life_max"].light()
                            ps["sndparticle_life_min"].light()
                            ps["sndparticle_bubble_buoyancy"].light()
                            ps["sndparticle_bubble_drag"].light()
                            ps["sndparticle_boundary"].light()

                        if dom.has_cache_baked_mesh or not dom.use_mesh:
                            ps["mesh_scale"].dark()
                            ps["mesh_particle_radius"].dark()
                            ps["use_speed_vectors"].dark()
                            ps["mesh_generator"].dark()
                            ps["mesh_smoothen_pos"].dark()
                            ps["mesh_smoothen_neg"].dark()
                            ps["mesh_concave_upper"].dark()
                            ps["mesh_concave_lower"].dark()
                        else:
                            ps["mesh_scale"].light()
                            ps["mesh_particle_radius"].light()
                            ps["use_speed_vectors"].light()
                            ps["mesh_generator"].light()

                            if dom.mesh_generator == "IMPROVED":
                                ps["mesh_smoothen_pos"].light()
                                ps["mesh_smoothen_neg"].light()
                                ps["mesh_concave_upper"].light()
                                ps["mesh_concave_lower"].light()
                            else:
                                ps["mesh_smoothen_pos"].dark()
                                ps["mesh_smoothen_neg"].dark()
                                ps["mesh_concave_upper"].dark()
                                ps["mesh_concave_lower"].dark()

                    if dom.cache_type == "ALL":
                        o_cache_frame_offset.light()
                        o_button_bake_all.light(0)
                        o_button_bake_all.dark(1)
                        o_button_bake_data.dark()
                        o_button_bake_guides.dark()
                        o_button_bake_mesh.dark()
                        o_button_bake_particles.dark()
                    elif dom.cache_type == "MODULAR":
                        o_cache_frame_offset.light()
                        o_button_bake_all.dark()
                        o_button_bake_data.light(0)
                        o_button_bake_data.dark(1)

                        if dom.has_cache_baked_guide:
                            o_button_bake_guides.dark(0)
                            o_button_bake_guides.light(1)
                        else:
                            o_button_bake_guides.light(0)
                            o_button_bake_guides.dark(1)

                        if dom.has_cache_baked_mesh:
                            o_button_bake_mesh.dark(0)
                            o_button_bake_mesh.light(1)
                        else:
                            o_button_bake_mesh.light(0)
                            o_button_bake_mesh.dark(1)

                        if dom.has_cache_baked_particles:
                            o_button_bake_particles.dark(0)
                            o_button_bake_particles.light(1)
                        else:
                            o_button_bake_particles.light(0)
                            o_button_bake_particles.dark(1)
                    else:
                        o_cache_frame_offset.dark()
                        o_button_bake_all.dark()
                        o_button_bake_data.dark()
                        o_button_bake_guides.dark()
                        o_button_bake_mesh.dark()
                        o_button_bake_particles.dark()

                    o_cache_resumable.light()
                    o_cache_data_format.light()

                    if dom.use_mesh:
                        o_cache_mesh_format.light()
                    else:
                        o_cache_mesh_format.dark()

                if dom:
                    b_settings.w.light(use_head=False)
                    b_guides.w.light(use_head=False)

                    if dom.has_cache_baked_any or dom.cache_data_format != "OPENVDB":
                        ps["openvdb_cache_compress_type"].dark()
                        ps["openvdb_data_depth"].dark()
                    else:
                        ps["openvdb_cache_compress_type"].light()
                        ps["openvdb_data_depth"].light()

                    if dom.has_cache_baked_guide:
                        o_resolution_max.dark()
                        o_time_scale.dark()
                    else:
                        o_resolution_max.light()
                        o_time_scale.light()

                    if dom.use_adaptive_timesteps:
                        o_cfl_condition.light()
                        o_timesteps_max.light()
                        o_timesteps_min.light()
                    else:
                        o_cfl_condition.dark()
                        o_timesteps_max.dark()
                        o_timesteps_min.dark()

                    if bpy.context.scene.use_gravity:
                        o_gravity.set_text("Using Scene Gravity")
                        o_gravity.dark()
                    else:
                        o_gravity.set_text("Gravity")
                        o_gravity.light()

                    if dom.use_guide:
                        ps["guide_alpha"].light()
                        ps["guide_beta"].light()
                        ps["guide_vel_factor"].light()
                        ps["guide_source"].light()

                        if dom.guide_source == "DOMAIN":
                            ps["guide_parent"].light()
                        else:
                            ps["guide_parent"].dark()
                    else:
                        ps["guide_alpha"].dark()
                        ps["guide_beta"].dark()
                        ps["guide_vel_factor"].dark()
                        ps["guide_source"].dark()
                        ps["guide_parent"].dark()
                else:
                    b_settings.w.dark(use_head=False)
                    b_guides.w.dark(use_head=False)
                    ps["openvdb_cache_compress_type"].dark()
                    ps["openvdb_data_depth"].dark()

                    ps["guide_parent"].dark()
                    o_cache_resumable.dark()
                    o_cache_data_format.dark()
                    o_cache_mesh_format.dark()

                    if dom.is_cache_baking_any:
                        o_button_bake_all.dark()
                        o_button_bake_data.dark()
                        o_button_bake_guides.dark()
                        o_button_bake_noise.dark()
                        o_button_bake_mesh.dark()
                        o_button_bake_particles.dark()
                    else:
                        if dom.cache_type == "ALL":
                            if dom.has_cache_baked_data:
                                o_button_bake_all.dark(0)
                                o_button_bake_all.light(1)
                            else:
                                o_button_bake_all.light(0)
                                o_button_bake_all.dark(1)

                            o_button_bake_data.dark()
                            o_button_bake_guides.dark()
                            o_button_bake_noise.dark()
                            o_button_bake_mesh.dark()
                            o_button_bake_particles.dark()
                        elif dom.cache_type == "MODULAR":
                            o_button_bake_all.dark()

                            if dom.has_cache_baked_data:
                                o_button_bake_data.dark(0)
                                o_button_bake_data.light(1)
                            else:
                                o_button_bake_data.light(0)
                                o_button_bake_data.dark(1)

                            if dom.has_cache_baked_guide:
                                o_button_bake_guides.dark(0)
                                o_button_bake_guides.light(1)
                            else:
                                o_button_bake_guides.light(0)
                                o_button_bake_guides.dark(1)

                            if dom.has_cache_baked_noise:
                                o_button_bake_noise.dark(0)
                                o_button_bake_noise.light(1)
                            else:
                                o_button_bake_noise.light(0)
                                o_button_bake_noise.dark(1)

                            if dom.has_cache_baked_mesh:
                                o_button_bake_mesh.dark(0)
                                o_button_bake_mesh.light(1)
                            else:
                                o_button_bake_mesh.light(0)
                                o_button_bake_mesh.dark(1)

                            if dom.has_cache_baked_particles:
                                o_button_bake_particles.dark(0)
                                o_button_bake_particles.light(1)
                            else:
                                o_button_bake_particles.light(0)
                                o_button_bake_particles.dark(1)
                        else:
                            o_button_bake_all.dark()
                            o_button_bake_data.dark()
                            o_button_bake_guides.dark()
                            o_button_bake_noise.dark()
                            o_button_bake_mesh.dark()
                            o_button_bake_particles.dark()

                if dom.use_color_ramp:
                    if dom.color_ramp_field == "FLAGS":
                        ps["display_interpolation"].dark()
                        ps["color_ramp_field_scale"].dark()
                    else:
                        ps["display_interpolation"].light()
                        ps["color_ramp_field_scale"].light()

                    ps["color_ramp_field"].light()

                    if dom.color_ramp_field[:3] != 'PHI' and dom.color_ramp_field not in {'FLAGS', 'PRESSURE'}:
                        o_color_ramp.light()
                    else:
                        o_color_ramp.dark()
                else:
                    ps["display_interpolation"].light()
                    ps["color_ramp_field"].dark()
                    ps["color_ramp_field_scale"].dark()
                    o_color_ramp.dark()

                if dom.use_slice:
                    ps["slice_per_voxel"].dark()
                    ps["slice_axis"].light()
                    ps["slice_depth"].light()

                    if dom.display_interpolation == "CLOSEST" or dom.color_ramp_field == "FLAGS":
                        if dom.show_gridlines:
                            b_vpd_gridlines.w.light()

                            if dom.gridlines_color_field == 'RANGE':
                                if dom.use_color_ramp and dom.color_ramp_field != "FLAGS":
                                    ps["gridlines_lower_bound"].light()
                                    ps["gridlines_upper_bound"].light()
                                    ps["gridlines_range_color"].light()
                                    ps["gridlines_cell_filter"].light()

                                    b_vpd_gridlines_label0.blf_label[0].text = ""
                                else:
                                    ps["gridlines_lower_bound"].dark()
                                    ps["gridlines_upper_bound"].dark()
                                    ps["gridlines_range_color"].dark()
                                    ps["gridlines_cell_filter"].dark()

                                    if dom.use_color_ramp:
                                        b_vpd_gridlines_label0.blf_label[0].text = "⚠ Range highlighting for flags is not available!"
                                    else:
                                        b_vpd_gridlines_label0.blf_label[0].text = "⚠ Enable Grid Display to use range highlighting!"
                            else:
                                ps["gridlines_lower_bound"].dark()
                                ps["gridlines_upper_bound"].dark()
                                ps["gridlines_range_color"].dark()
                                ps["gridlines_cell_filter"].dark()

                                b_vpd_gridlines_label0.blf_label[0].text = ""
                        else:
                            b_vpd_gridlines.w.dark()
                            b_vpd_gridlines_label0.blf_label[0].text = ""

                        ps["show_gridlines"].light()
                    else:
                        b_vpd_gridlines.w.dark()
                        b_vpd_gridlines_label0.blf_label[0].text = ""
                else:
                    ps["slice_per_voxel"].light()
                    ps["slice_axis"].dark()
                    ps["slice_depth"].dark()

                    b_vpd_gridlines.w.dark()
                    b_vpd_gridlines_label0.blf_label[0].text = ""

                if dom.show_velocity:
                    b_vpd_vector.w.light(use_head=False)

                    if dom.vector_display_type == "MAC":
                        ps["vector_show_mac_x"].light()
                        ps["vector_scale_with_magnitude"].dark()
                    else:
                        ps["vector_show_mac_x"].dark()
                        ps["vector_scale_with_magnitude"].light()

                    if not dom.use_guide and dom.vector_field == "GUIDE_VELOCITY":
                        o_vpd_vector_label0.blf_label[0].text = "⚠ Enable Guides first! Defaulting to Fluid Velocity"
                    else:
                        o_vpd_vector_label0.blf_label[0].text = ""
                else:
                    b_vpd_vector.w.dark(use_head=False)

                    o_vpd_vector_label0.blf_label[0].text = ""
                #|

            def upd_data_callback():
                if self.w.active_modifier.fluid_type == "DOMAIN": pass
                else:

                    self.reinit_tab_with(search_data)
                    return

                ui_anim_data.update_with(N1)
                uianim.update_with(fn_darklight)
                uianim_effector_weights.update_with(fn_darklight_effector_weights)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                    uianim,
                    uianim_effector_weights,
                ],
                extra_buttons = extra_buttons,
                search_data = search_data)


        elif _fluid_type == "FLOW":
            def r_flow():
                return self.w.active_modifier.flow_settings

            uianim = ui.set_pp(r_flow, bpytypes.FluidFlowSettings, self.rr_dph(".flow_settings"))
            ps = uianim.props

            b_settings = ui.new_block(title="Settings")
            po = b_settings.prop
            po("flow_type")
            po("flow_behavior")
            po("use_inflow")
            po("subframes", text="Sampling Substeps")
            po("smoke_color", text="Smoke Color")
            po("use_absolute", text="Absolute Density")
            po("temperature", text="Initial Temperature")
            po("density", text="Density")
            po("fuel_amount", text="Fuel")
            b_settings.prop_search("density_vertex_group", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Vertex Group")

            b_flow_source = ui.new_block(title="Flow Source")
            po = b_flow_source.prop
            po("flow_source")
            ps["flow_source"].rna = RNA_flow_source
            ps["flow_source"].enum_items = RNA_flow_source.enum_items
            po("use_plane_init")
            po("surface_distance")
            po("volume_density")
            b_flow_source.sep(2)
            po("particle_system", options={"r_items": lambda: self.w.active_object.particle_systems})
            po("use_particle_size")
            po("particle_size")

            b_initial_velocity = ui.new_block(title=b_settings.r_prop("use_initial_velocity", text="Initial Velocity", options={"HEAD"}))
            b_initial_velocity.prop("velocity_factor")
            b_initial_velocity.prop("velocity_normal")
            b_initial_velocity.prop("velocity_coord")

            b_texture = ui.new_block(title=b_settings.r_prop("use_texture", text="Texture", options={"HEAD"}))
            b_texture.prop("noise_texture", options={"ID":"TEXTURE"})
            b_texture.prop("texture_map_type")
            b_texture.prop_search("uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)
            b_texture.prop("texture_size")
            b_texture.prop("texture_offset")


            ui_state = []

            def fn_darklight(flow):
                if ui_state == [ui_anim_data.library_state, flow.flow_behavior, flow.flow_type, flow.flow_source, flow.use_particle_size, flow.use_initial_velocity, flow.use_texture, flow.texture_map_type]: return
                ui_state[:] = [ui_anim_data.library_state, flow.flow_behavior, flow.flow_type, flow.flow_source, flow.use_particle_size, flow.use_initial_velocity, flow.use_texture, flow.texture_map_type]

                if ui_anim_data.library_state in {1, -1}: return

                if flow.flow_behavior in {"INFLOW", "OUTFLOW"}:
                    ps["use_inflow"].light()
                else:
                    ps["use_inflow"].dark()

                if flow.flow_type in {"SMOKE", "BOTH", "FIRE"} and flow.flow_behavior != "OUTFLOW":
                    ps["use_absolute"].light()
                    ps["density_vertex_group"].light()

                    if flow.flow_type in {"SMOKE", "BOTH"}:
                        ps["smoke_color"].light()
                        ps["temperature"].light()
                        ps["density"].light()
                    else:
                        ps["smoke_color"].dark()
                        ps["temperature"].dark()
                        ps["density"].dark()

                    if flow.flow_type in {"FIRE", "BOTH"}:
                        ps["fuel_amount"].light()
                    else:
                        ps["fuel_amount"].dark()
                else:
                    ps["use_absolute"].dark()
                    ps["smoke_color"].dark()
                    ps["temperature"].dark()
                    ps["density"].dark()
                    ps["fuel_amount"].dark()
                    ps["density_vertex_group"].dark()

                if flow.flow_source == "MESH":
                    ps["use_plane_init"].light()
                    ps["surface_distance"].light()

                    if flow.flow_type in {"SMOKE", "BOTH", "FIRE"}:
                        ps["volume_density"].light()
                    else:
                        ps["volume_density"].dark()

                    ps["particle_system"].dark()
                    ps["use_particle_size"].dark()
                    ps["particle_size"].dark()

                elif flow.flow_source == "PARTICLES":
                    ps["use_plane_init"].dark()
                    ps["surface_distance"].dark()
                    ps["volume_density"].dark()

                    ps["particle_system"].light()
                    ps["use_particle_size"].light()

                    if flow.use_particle_size:
                        ps["particle_size"].light()
                    else:
                        ps["particle_size"].dark()
                else:
                    ps["use_plane_init"].dark()
                    ps["surface_distance"].dark()
                    ps["volume_density"].dark()
                    ps["particle_system"].dark()
                    ps["use_particle_size"].dark()
                    ps["particle_size"].dark()

                if flow.flow_behavior == 'OUTFLOW':
                    b_initial_velocity.w.dark()
                else:
                    if flow.use_initial_velocity:
                        ps["velocity_factor"].light()

                        if flow.flow_source == "MESH":
                            ps["velocity_normal"].light()
                            ps["velocity_coord"].light()
                        else:
                            ps["velocity_normal"].dark()
                            ps["velocity_coord"].dark()
                    else:
                        b_initial_velocity.w.dark()

                    ps["use_initial_velocity"].light()

                if flow.flow_behavior == 'OUTFLOW' or flow.flow_type == 'LIQUID':
                    b_texture.w.dark()
                else:
                    if flow.use_texture:
                        ps["noise_texture"].light()
                        ps["texture_map_type"].light()
                        ps["texture_offset"].light()

                        if flow.texture_map_type == "UV":
                            ps["uv_layer"].light()
                            ps["texture_size"].dark()
                        elif flow.texture_map_type == "AUTO":
                            ps["uv_layer"].dark()
                            ps["texture_size"].light()
                        else:
                            ps["uv_layer"].dark()
                            ps["texture_size"].dark()
                    else:
                        ps["noise_texture"].dark()
                        ps["texture_map_type"].dark()
                        ps["texture_offset"].dark()
                        ps["uv_layer"].dark()
                        ps["texture_size"].dark()

                    ps["use_texture"].light()
                #|

            def upd_data_callback():
                if self.w.active_modifier.fluid_type == "FLOW": pass
                else:

                    self.reinit_tab_with(search_data)
                    return

                ui_anim_data.update_with(N1)
                uianim.update_with(fn_darklight)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                    uianim,
                ],
                extra_buttons = None,
                search_data = search_data)


        elif _fluid_type == "EFFECTOR":
            def r_effector():
                return self.w.active_modifier.effector_settings

            uianim = ui.set_pp(r_effector, bpytypes.FluidEffectorSettings, self.rr_dph(".effector_settings"))
            ps = uianim.props

            b_settings = ui.new_block(title="Settings")
            po = b_settings.prop
            b_settings.prop_flag("effector_type")
            po("subframes", text="Sampling Substeps")
            po("surface_distance", text="Surface Thickness")
            po("use_effector", text="Use Effector")
            po("use_plane_init", text="Is Planar")
            po("velocity_factor", text="Velocity Factor")
            po("guide_mode", text="Guide Mode")

            ui_state = []

            def fn_darklight(ef):
                if ui_state == [ui_anim_data.library_state, ef.effector_type]: return
                ui_state[:] = [ui_anim_data.library_state, ef.effector_type]

                if ui_anim_data.library_state in {1, -1}: return

                if ef.effector_type == "GUIDE":
                    ps["velocity_factor"].light()
                    ps["guide_mode"].light()
                else:
                    ps["velocity_factor"].dark()
                    ps["guide_mode"].dark()
                #|

            def upd_data_callback():
                if self.w.active_modifier.fluid_type == "EFFECTOR": pass
                else:

                    self.reinit_tab_with(search_data)
                    return

                ui_anim_data.update_with(N1)
                uianim.update_with(fn_darklight)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                    uianim,
                ],
                extra_buttons = None,
                search_data = search_data)


        else:
            def upd_data_callback():
                if self.w.active_modifier.fluid_type in {"DOMAIN", "FLOW", "EFFECTOR"}:

                    self.reinit_tab_with(search_data)
                    return

                ui_anim_data.update_with(N1)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                ],
                extra_buttons = None,
                search_data = search_data)

        self.upd_data_callback = upd_data_callback
        # >>>
        #|
    def init_tab_HOOK(self):


        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT"})
        b0.prop_search("subtarget", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().object), text="Bone")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("strength")

        b1 = ui.new_block(title="Falloff")
        b1.prop("falloff_type", text="Type")
        b1.prop("falloff_radius")
        b1.prop("use_falloff_uniform")
        b1.sep(2)
        o_edit_curve = b1.function(RNA_edit_curve, self.bufn_HOOK_edit_curve)

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'object'}$)
            if md.object:
                name_object = md.object.name
                state_object = 0  if md.object.type == "ARMATURE" else 1
            else:
                name_object = ""
                state_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.vertex_group, state_object, md.falloff_type, name_object]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, state_object, md.falloff_type, name_object]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if state_object == 0:
                props["subtarget"].light()
            else:
                props["subtarget"].dark()

            if md.falloff_type == "CURVE":
                o_edit_curve.light()
                props["falloff_radius"].light()
            else:
                o_edit_curve.dark()

                if md.falloff_type == "NONE":
                    props["falloff_radius"].dark()
                else:
                    props["falloff_radius"].light()

            props["subtarget"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_LAPLACIANDEFORM(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("iterations")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        props["vertex_group"].set_callback = update_scene_and_ref
        b0.sep(1)
        o_bind = b0.function(RNA_LAPLACIANDEFORM_bind, self.bufn_LAPLACIANDEFORM_bind)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.is_bind]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.is_bind]

            if ui_anim_data.library_state == 1:
                o_bind.dark()
                return

            if md.vertex_group:
                props["invert_vertex_group"].light()
                o_bind.light()
            else:
                props["invert_vertex_group"].dark()
                o_bind.dark()

            if md.is_bind:
                o_bind.set_button_text("Unbind")
            else:
                o_bind.set_button_text("Bind")

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_LAPLACIANSMOOTH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("iterations")
        b0.prop_flag(["use_x", "use_y", "use_z"], text="Axis", options={"NAMES": "XYZ"})
        b0.prop("lambda_factor")
        b0.prop("lambda_border")
        b0.sep(2)
        b0.prop("use_volume_preserve")
        b0.prop("use_normalized")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_LATTICE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT", "TYPES":{"LATTICE"}})
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("strength")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_MASK(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        props["mode"].r_button_width = self.r_button_width_150
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("use_smooth")
        b0.prop("armature", options={"ID":"OBJECT", "TYPES":{"ARMATURE"}})
        b0.prop("threshold")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.mode]

            if ui_anim_data.library_state == 1: return

            if md.mode == "ARMATURE":
                props["vertex_group"].dark()
                props["invert_vertex_group"].dark()
                props["use_smooth"].dark()
                props["armature"].light()
            else:
                props["vertex_group"].light()
                props["use_smooth"].light()
                props["armature"].dark()

                if md.vertex_group:
                    props["invert_vertex_group"].light()
                else:
                    props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_MESH_CACHE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("cache_format")
        b0.sep(2)
        b0.prop("filepath")
        props["filepath"].set_align("FULL")
        b0.sep(2)
        b0.prop("factor")
        b0.prop_flag("deform_mode")
        b0.prop_flag("interpolation")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        b1 = ui.new_block(title="Time Remapping")
        b1.prop_flag("time_mode")
        props["time_mode"].r_button_width = self.r_button_width_150
        b1.prop_flag("play_mode")
        b1.prop("frame_start")
        b1.prop("frame_scale")
        b1.prop("eval_frame")
        b1.prop("eval_time")
        b1.prop("eval_factor")

        b2 = ui.new_block(title="Axis Mapping")
        b2.prop("forward_axis")
        b2.prop("up_axis")
        b2.prop("flip_axis")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.play_mode, md.time_mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.play_mode, md.time_mode]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.play_mode == "SCENE":
                props["frame_start"].light()
                props["frame_scale"].light()
                props["eval_frame"].dark()
                props["eval_time"].dark()
                props["eval_factor"].dark()
            else:
                props["frame_start"].dark()
                props["frame_scale"].dark()

                if md.time_mode == "FRAME":
                    props["eval_frame"].light()
                    props["eval_time"].dark()
                    props["eval_factor"].dark()
                elif md.time_mode == "TIME":
                    props["eval_frame"].dark()
                    props["eval_time"].light()
                    props["eval_factor"].dark()
                else:
                    props["eval_frame"].dark()
                    props["eval_time"].dark()
                    props["eval_factor"].light()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_MESH_DEFORM(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT", "TYPES":{"MESH"}}, isdarkhard=True)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("precision", isdarkhard=True)
        b0.prop("use_dynamic_bind", isdarkhard=True)
        b0.sep(1)
        o_bind = b0.function(RNA_MESH_DEFORM_bind, self.bufn_MESH_DEFORM_bind, isdarkhard=True)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.is_bound]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.is_bound]

            if ui_anim_data.library_state == 1:
                o_bind.dark()
                return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.is_bound:
                props["object"].dark()
                props["precision"].dark()
                props["use_dynamic_bind"].dark()
                o_bind.set_button_text("Unbind")
            else:
                props["object"].light()
                props["precision"].light()
                props["use_dynamic_bind"].light()
                o_bind.set_button_text("Bind")

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_MESH_SEQUENCE_CACHE(self):

        def r_object_paths():
            cache_file = self.w.active_modifier.cache_file
            if hasattr(cache_file, "object_paths"):
                return [Name(e.path)  for e in cache_file.object_paths]
            return []
            #|

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        o_read_data = b0.r_prop("read_data", text="Read")
        props["read_data"].r_button_width = self.r_button_width_166

        b0.items.append(ButtonOverlay(o_read_data.w, button_search, o_read_data))

        b0.prop_search("object_path", GpuImg_objectpath, r_object_paths)
        props["object_path"].r_button_width = self.r_button_width_166
        b0.sep(1)
        b0.prop("use_vertex_interpolation")
        b0.prop("velocity_scale")

        b1 = ui.new_block(title=ui.r_prop("cache_file", text="Cache", options={"RICH":"CACHEFILE"}))
        props["cache_file"].set_align("FULL")
        props["cache_file"].r_button_width = self.r_button_width_FULL_head

        if self.w.active_modifier.cache_file:
            def r_cache_file():
                return self.w.active_modifier.cache_file
            def r_layers():
                cache_file = self.w.active_modifier.cache_file
                if cache_file:
                    return cache_file.layers
                return None
            def r_active_index():
                cache_file = self.w.active_modifier.cache_file
                if hasattr(cache_file, "active_index"):
                    return cache_file.active_index
                return -1
            def set_active_index(i):
                cache_file = self.w.active_modifier.cache_file
                if hasattr(cache_file, "active_index"):
                    cache_file.active_index = i
            def remove_active_layer():
                cache_file = self.w.active_modifier.cache_file
                if cache_file:
                    i = r_active_index()
                    if i not in {-1, None}:
                        cache_file.layers.remove(cache_file.layers[i])
            def add_active_layer():
                def end_fn(s):
                    try:
                        layers = self.w.active_modifier.cache_file.layers
                        if any(layer.filepath == s  for layer in layers):
                            report("Layer path already exists", ty="WARNING")
                            return
                        layers.new(s)
                    except Exception as ex:
                        report(str(ex), ty="WARNING")

                OpScanFile.end_fn = end_fn
                bpy.ops.wm.vmd_scan_file("INVOKE_DEFAULT", filepath="", filter_glob="*.abc")
            def r_enabled_datapath_layer(i):
                return f'layers[{i}].hide_layer'
            def r_datapath_head_layer(i):
                return f'layers[{i}]'
            def set_enabled_layer(e, boo):
                e.hide_layer = not boo
            @ catch
            def bufn_refresh(button=None):
                cache_file = self.w.active_modifier.cache_file
                cache_file.filepath = cache_file.filepath
                update_scene()
                #|

            uianim = b1.set_pp_id_data(r_cache_file, CacheFile)
            ps = uianim.props

            o_refresh = b1.r_function(RNA_refresh, bufn_refresh, options={"icon_cls": GpuImg_FILE_REFRESH, "icon_cls_dark": GpuImgNull})
            o_refresh.r_button_width = lambda: SIZE_border[3] * 3
            o_filepath = b1.r_prop("filepath")
            o_filepath.set_align("FULL", r_offset_width=lambda: SIZE_widget[0] + SIZE_border[3] * 3)
            b1.items.append(ButtonOverlay(o_filepath.w, o_refresh, o_filepath))
            b1.sep(1)

            b_time = b1.new_block(title="Time")
            b_time.prop("is_sequence")
            b_time.prop("override_frame")
            b_time.prop("frame")
            b_time.prop("frame_offset")

            b_render = b1.new_block(title="Render Procedural")
            b_render.prop("use_render_procedural", options={"FLIP"})
            b_render.prop("use_prefetch", isdarkhard=True)
            b_render.prop("prefetch_cache_size", isdarkhard=True)
            b_render_items = b_render.items[:]
            label0 = b_render.label(["Cycles experimental feature require"])
            b_render_items_label = b_render.items[:]

            b_velocity = b1.new_block(title="Velocity")
            b_velocity.prop("velocity_name")
            b_velocity.prop_flag("velocity_unit")

            b_layers = b1.new_block(title="Override Layers")
            blocklis_layers = BlocklistAZEnabled(b_layers.w,
                r_pp = r_layers,
                r_object = r_cache_file,
                r_datapath_head = r_datapath_head_layer,
                get_icon = lambda e: GpuImg_cache_layer(),
                remove_active_item = remove_active_layer,
                add_item = add_active_layer,
                r_enabled = lambda e: not e.hide_layer,
                r_enabled_datapath = r_enabled_datapath_layer,
                set_enabled = set_enabled_layer,
                name_attr = "filepath",
                use_index = True)
            blocklis_layers.r_active_index = r_active_index
            blocklis_layers.set_active_index = set_active_index
            blocklis_layers_media = BlockMediaAZ(b_layers.w, blocklis_layers)
            extra_buttons = [blocklis_layers, blocklis_layers_media]
            b_layers.items += extra_buttons

            ui_type = [False]
            ui_state = []
            allow_update = True

            def fn_darklight(md):
                if md.cache_file: pass
                else:

                    nonlocal allow_update
                    allow_update = False
                    self.reinit_tab_with(search_data)
                    return True

            def fn_darklight_cache(cac):
                if cac: pass
                else: return True

                if uianim.library_state in {1, -1}: return

                if ui_state == [uianim.library_state, cac.override_frame, bpy.context.scene.cycles.feature_set, cac.use_render_procedural, cac.use_prefetch]: return
                ui_state[:] = [uianim.library_state, cac.override_frame, bpy.context.scene.cycles.feature_set, cac.use_render_procedural, cac.use_prefetch]


                if cac.override_frame:
                    ps["frame"].light()
                else:
                    ps["frame"].dark()

                if bpy.context.scene.cycles.feature_set == "EXPERIMENTAL":
                    ps["use_render_procedural"].light()

                    if cac.use_render_procedural:
                        ps["use_prefetch"].light()

                        if cac.use_prefetch:
                            ps["prefetch_cache_size"].light()
                        else:
                            ps["prefetch_cache_size"].dark()
                    else:
                        ps["use_prefetch"].dark()
                        ps["prefetch_cache_size"].dark()
                else:
                    ps["use_render_procedural"].dark()
                    ps["use_prefetch"].dark()
                    ps["prefetch_cache_size"].dark()
                #|

            def upd_data_callback():
                ui_anim_data.update_with(fn_darklight)

                if ui_type[0] == (bpy.context.scene.cycles.feature_set == "EXPERIMENTAL"): pass
                else:
                    ui_type[0] = (bpy.context.scene.cycles.feature_set == "EXPERIMENTAL")


                    if bpy.context.scene.cycles.feature_set == "EXPERIMENTAL":
                        b_render.items[:] = b_render_items
                    else:
                        b_render.items[:] = b_render_items_label

                    ui_state.clear()
                    ui_anim_data.tag_update()
                    uianim.tag_update()
                    self.redraw_from_headkey_with(search_data)
                    return

                if allow_update is True:
                    uianim.update_with(fn_darklight_cache)

                    blocklis_layers.upd_data()
                    blocklis_layers_media.upd_data()

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                    uianim,
                ],
                extra_buttons = None,
                search_data = search_data)
        else:
            ui_state = []

            def fn_darklight(md):
                if md.cache_file:

                    self.reinit_tab_with(search_data)
                    return True

            def upd_data_callback():
                ui_anim_data.update_with(fn_darklight)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                ],
                extra_buttons = None,
                search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_MIRROR(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        options={"NAMES": "XYZ"}
        b0.prop("use_axis", text="Axis", options=options)
        b0.prop("use_bisect_axis", text="Bisect", options=options)
        b0.prop("use_bisect_flip_axis", text="Flip", options=options)
        b0.sep(2)
        b0.prop("mirror_object", options={"ID":"OBJECT"})
        b0.prop("use_clip", text="Clipping")
        b0.sep(1)
        b0.prop("merge_threshold", text="")
        b0.join_bool("use_mirror_merge", text="Merge")
        b0.prop("bisect_threshold")

        b1 = ui.new_block(title="Data")
        b1.prop("mirror_offset_u", text="")
        b1.join_prop("mirror_offset_v", text="")
        b1.propY(["use_mirror_u", "use_mirror_v"], [None, "V"])
        items = b1.items
        g_use_mirror = items.pop()
        g_mirror_offset = items.pop()
        items.append(ButtonOverlay(g_use_mirror.w, g_use_mirror, g_mirror_offset))
        b1.sep(2)
        b1.prop("offset_u", text="Offset U")
        b1.join_prop("offset_v", text="V")
        b1.sep(2)
        b1.prop("use_mirror_vertex_groups", text="Vertex Groups")
        b1.prop("use_mirror_udim", text="Flip UDIM")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, all(False  if v else True  for v in md.use_bisect_axis), md.use_mirror_merge, md.use_mirror_u, md.use_mirror_v]: return
            ui_state[:] = [ui_anim_data.library_state, all(False  if v else True  for v in md.use_bisect_axis), md.use_mirror_merge, md.use_mirror_u, md.use_mirror_v]

            if ui_anim_data.library_state == 1: return

            if all(False  if v else True  for v in md.use_bisect_axis):
                props["use_bisect_flip_axis"].dark()
                props["bisect_threshold"].dark()
            else:
                props["use_bisect_flip_axis"].light()
                props["bisect_threshold"].light()

            if md.use_mirror_merge:
                props["merge_threshold"].light()
            else:
                props["merge_threshold"].dark()

            if md.use_mirror_u:
                props["mirror_offset_u"].light()
            else:
                props["mirror_offset_u"].dark()

            if md.use_mirror_v:
                props["mirror_offset_v"].light()
            else:
                props["mirror_offset_v"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_MULTIRES(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("levels", text="Level Viewport")
        b0.join_prop("sculpt_levels", text="Sculpt")
        b0.join_prop("render_levels", text="Render")
        b0.prop("use_sculpt_base_mesh")
        b0.prop("show_only_control_edges")

        o_subdivide = ui.r_function(RNA_MULTIRES_subdivide, self.bufn_MULTIRES_subdivide, isdarkhard=True)
        b1 = ui.new_block(title=o_subdivide)
        b1.w.blf_title.text = "Subdivision"
        o_simple_linear = b1.function([RNA_MULTIRES_simple, RNA_MULTIRES_linear], [self.bufn_MULTIRES_simple, self.bufn_MULTIRES_linear], isdarkhard=True)
        o_unsubdivide_higher = b1.function([RNA_MULTIRES_unsubdivide, RNA_MULTIRES_delete_higher], [self.bufn_MULTIRES_unsubdivide, self.bufn_MULTIRES_delete_higher], isdarkhard=True)

        ui.set_fold_state(True)
        b2 = ui.new_block(title="Shape & Generate")
        o_reshape_apply = b2.function([RNA_MULTIRES_reshape, RNA_MULTIRES_apply_base], [self.bufn_MULTIRES_reshape, self.bufn_MULTIRES_apply_base], isdarkhard=True)
        b2.sep(2)
        b2.prop("filepath")
        props["filepath"].set_align("FULL")
        b2.sep(2)
        o_rebuild_save = b2.function([RNA_MULTIRES_rebuild, RNA_MULTIRES_save_external], [self.bufn_MULTIRES_rebuild, self.bufn_MULTIRES_save_external], isdarkhard=True)

        ui.set_fold_state(P_ModifierEditor.is_fold)
        b3 = ui.new_block(title="Advanced")
        b3.prop("quality")
        b3.prop("uv_smooth")
        b3.prop("boundary_smooth")
        b3.prop("use_creases")
        b3.prop("use_custom_normals")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.total_levels, self.w.active_object.mode, md.is_external]: return
            ui_state[:] = [ui_anim_data.library_state, md.total_levels, self.w.active_object.mode, md.is_external]

            if ui_anim_data.library_state == 1:
                o_subdivide.dark()
                o_simple_linear.dark()
                o_unsubdivide_higher.dark()
                o_reshape_apply.dark()
                o_rebuild_save.dark()
                return

            o_rebuild_save.light()
            oj_mode = self.w.active_object.mode

            if md.total_levels == 0:
                b3.w.light()
                o_rebuild_save.light(0)
            else:
                b3.w.dark()
                o_rebuild_save.dark(0)

            if oj_mode == 'SCULPT':
                props["use_sculpt_base_mesh"].light()
            else:
                props["use_sculpt_base_mesh"].dark()

            if oj_mode == 'EDIT':
                o_subdivide.dark()
                o_simple_linear.dark()
                o_unsubdivide_higher.dark()
                o_reshape_apply.dark()
            else:
                o_subdivide.light()
                o_simple_linear.light()
                o_unsubdivide_higher.light()
                o_reshape_apply.light()

            if md.is_external:
                props["filepath"].light()
                o_rebuild_save.set_button_text("Pack External File", 1)
            else:
                props["filepath"].dark()
                o_rebuild_save.set_button_text("Save External File", 1)

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_NODES(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        o_node_group = b0.r_prop("node_group", text="", options={"RICH": "NODETREE"})
        o_node_group.allow_types = {"GEOMETRY"}
        o_node_group.set_align("FULL")
        o_node_group.r_button_width = Ui.r_button_width_FULL_1
        b0.items.append(ButtonOverlay(o_node_group.w, button_search, o_node_group))

        b1 = ui.new_block(title="Input", heavy=True)
        uianim_panel = b1.set_pp(self.r_modifier)
        uianim = b1.set_pp(self.r_modifier)

        b2 = ui.new_block(title="Output", heavy=True)
        uianim_output = b2.set_pp(self.r_modifier)

        b_manage = ui.new_block(title="Manage")
        b_manage.set_pp_from(ui_anim_data)
        b_manage.prop("bake_directory", text="Bake Path")
        o_bake_directory = ui_anim_data.props["bake_directory"]
        o_bake_directory.set_align("FULL")
        o_bake_directory.set_callback = update_scene_and_ref
        if "bake_target" in ui_anim_data.rnas: # blender4.3
            b_manage.prop_flag("bake_target")

        _node_group = self.w.active_modifier.node_group
        _is_gn_rna_dirty = is_gn_rna_dirty  if P_ModifierEditor.use_gn_layout else is_gn_rna_dirty_no_layout
        items_stacks = [b0, b1, b2, b_manage]
        crna_panels = []

        if _node_group:
            def upd_data_callback():
                md = self.w.active_modifier

                if md.node_group: pass
                else:
                    self.reinit_tab_with(search_data)
                    return

                if _is_gn_rna_dirty(self, md, items_stacks, uianim, uianim_output, uianim_panel, crna_panels) is True:

                    ui_anim_data.tag_update()
                    uianim.tag_update()
                    uianim_panel.tag_update()
                    uianim_output.tag_update()
                    self.redraw_from_headkey_with(search_data)
                    return

                ui_anim_data.update_with(N1)
                uianim.update_with(N1)
                uianim_panel.update_with(N1)
                uianim_output.update_with(N1)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                    uianim,
                    uianim_panel,
                    uianim_output,
                ],
                extra_buttons = None,
                search_data = search_data)
        else:
            def upd_data_callback():
                if self.w.active_modifier.node_group:
                    self.reinit_tab_with(search_data)
                    return

                ui_anim_data.update_with(N1)

            button_search.fn = self.r_bufn_search(upd_data_callback, [
                    ui_anim_data,
                ],
                extra_buttons = None,
                search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_NORMAL_EDIT(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        props["mode"].r_button_width = self.r_button_width_200
        b0.sep(1)
        b0.prop("target", options={"ID":"OBJECT"})
        b0.prop("use_direction_parallel")
        b0.prop("offset")

        b1 = ui.new_block(title="Mix")
        b1.prop("mix_mode")
        b1.prop("mix_factor")
        b1.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b1.prop("mix_limit")
        b1.prop("no_polynors_fix")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.mode, (True  if md.target else False), md.use_direction_parallel]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.mode, (True  if md.target else False), md.use_direction_parallel]

            if ui_anim_data.library_state == 1: return

            if ((md.mode == 'RADIAL') and not md.target) or ((md.mode == 'DIRECTIONAL') and md.use_direction_parallel):
                props["offset"].light()
            else:
                props["offset"].dark()

            if md.mode == 'DIRECTIONAL':
                props["use_direction_parallel"].light()
            else:
                props["use_direction_parallel"].dark()

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_OCEAN(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        o_geometry_mode = b0.r_prop_flag("geometry_mode")

        b0.items.append(ButtonOverlay(o_geometry_mode.w, button_search, o_geometry_mode))

        b0.sep(1)
        b0.prop("repeat_x")
        b0.join_prop("repeat_y", text="Y")
        b0.sep(1)
        b0.prop("viewport_resolution", text="Resolution Viewport")
        b0.join_prop("resolution", text="Render")
        b0.sep(1)
        b0.prop("time")
        b0.prop("depth")
        b0.prop("size")
        b0.prop("spatial_size")
        b0.prop("random_seed")
        b0.prop("use_normals")

        b1 = ui.new_block(title="Waves")
        b1.prop("wave_scale", text="Scale")
        b1.prop("wave_scale_min")
        b1.prop("choppiness")
        b1.prop("wind_velocity")
        b1.sep(2)
        b1.prop("wave_alignment", text="Alignment")
        b1.prop("wave_direction", text="Direction")
        b1.prop("damping")

        b2 = ui.new_block(title=ui.r_prop("use_foam", text="Foam", options={"HEAD"}))
        b2.prop("foam_layer_name", text="Data Layer")
        b2.prop("foam_coverage", text="Coverage")
        b2.sep(1)
        b2_0 = b2.new_block(title=b2.r_prop("use_spray", text="Spray", options={"HEAD"}))
        b2_0.prop("spray_layer_name", text="Data Layer")
        b2_0.prop("invert_spray", text="Invert")

        b3 = ui.new_block(title="Spectrum")
        b3.prop("spectrum", text="Type")
        props["spectrum"].set_align("FULL")
        b3.prop("sharpen_peak_jonswap")
        b3.prop("fetch_jonswap")

        o_bake = ui.r_function(RNA_OCEAN_bake, self.bufn_OCEAN_bake)
        b4 = ui.new_block(title=o_bake)
        b4.w.blf_title.text = "Bake"
        b4.prop("filepath")
        props["filepath"].set_align("FULL")
        b4.sep(1)
        b4.prop("frame_start", text="Frame Start", isdarkhard=True)
        b4.join_prop("frame_end", text="End", isdarkhard=True)
        b4.sep(1)
        b4.prop("bake_foam_fade")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.geometry_mode, md.spectrum, (md.wave_alignment > 0.0), md.use_foam, md.use_spray, md.is_cached]: return
            ui_state[:] = [ui_anim_data.library_state, md.geometry_mode, md.spectrum, (md.wave_alignment > 0.0), md.use_foam, md.use_spray, md.is_cached]

            if ui_anim_data.library_state == 1:
                o_bake.dark()
                return

            o_bake.light()

            if md.geometry_mode:
                props["repeat_x"].light()
                props["repeat_y"].light()
            else:
                props["repeat_x"].dark()
                props["repeat_y"].dark()

            if md.spectrum:
                props["sharpen_peak_jonswap"].light()
                props["fetch_jonswap"].light()
            else:
                props["sharpen_peak_jonswap"].dark()
                props["fetch_jonswap"].dark()

            if md.wave_alignment > 0.0:
                props["wave_direction"].light()
                props["damping"].light()
            else:
                props["wave_direction"].dark()
                props["damping"].dark()

            if md.use_foam:
                props["bake_foam_fade"].light()
                props["foam_layer_name"].light()
                props["foam_coverage"].light()
                props["use_spray"].light()

                if md.use_spray:
                    props["spray_layer_name"].light()
                    props["invert_spray"].light()
                else:
                    props["spray_layer_name"].dark()
                    props["invert_spray"].dark()
            else:
                props["bake_foam_fade"].dark()
                props["foam_layer_name"].dark()
                props["foam_coverage"].dark()
                props["use_spray"].dark()

                props["spray_layer_name"].dark()
                props["invert_spray"].dark()

            if md.is_cached:
                o_bake.set_button_text("Free Ocean")
                props["frame_start"].dark()
                props["frame_end"].dark()
            else:
                o_bake.set_button_text("Bake Ocean")
                props["frame_start"].light()
                props["frame_end"].light()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        button_search.fn = self.r_bufn_search(upd_data_callback, [
                ui_anim_data,
            ],
            extra_buttons = [o_bake],
            search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_PARTICLE_INSTANCE(self):

        def r_particle_systems():
            ob = self.w.active_modifier.object
            if hasattr(ob, "particle_systems"):
                return ob.particle_systems
            return []
            #|

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        o_object = b0.r_prop("object", options={"ID":"OBJECT", "TYPES":{"MESH"}})

        b0.items.append(ButtonOverlay(o_object.w, button_search, o_object))
        b0.prop("particle_system", options={"r_items": r_particle_systems})
        b0.prop("particle_system_index", text="Particle System", isdarkhard=True)
        b0.sep(2)
        b0.prop_flag(["use_normal", "use_children", "use_size"], text="Create Instances", options={"NAMES": ("Regular", "Children", "Size")})
        b0.prop_flag(["show_alive", "show_dead", "show_unborn"], text="Show", options={"NAMES": ("Alive", "Dead", "Unborn")})
        props["use_normal"].r_button_width = self.r_button_width_150
        props["show_alive"].r_button_width = self.r_button_width_150
        b0.prop("particle_amount", text="Amount")
        b0.prop("particle_offset", text="Offset")
        b0.sep(2)
        b0.prop_flag("space", text="Coordinate Space")
        b0.prop_flag("axis")

        b1 = ui.new_block(title=ui.r_prop("use_path", text="Create Along Paths", options={"HEAD"}))
        b1.prop("position")
        b1.join_prop("random_position", text="Random")
        b1.sep(1)
        b1.prop("rotation")
        b1.join_prop("random_rotation", text="Random")
        b1.sep(0)
        b1.prop("use_preserve_shape")

        b2 = ui.new_block(title="Layers")
        b2.prop_search("index_layer_name", GpuImg_GROUP_VCOL, self.r_object_vertex_colors, text="Index")
        b2.prop_search("value_layer_name", GpuImg_GROUP_VCOL, self.r_object_vertex_colors, text="Value")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, (True  if md.object else False), md.use_path]: return
            ui_state[:] = [ui_anim_data.library_state, (True  if md.object else False), md.use_path]

            if ui_anim_data.library_state == 1: return

            if md.object:
                props["particle_system"].light()
                props["particle_system_index"].dark()
            else:
                props["particle_system"].dark()
                props["particle_system_index"].light()

            if md.use_path:
                b1.w.light(use_head=False)
            else:
                b1.w.dark(use_head=False)

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        button_search.fn = self.r_bufn_search(upd_data_callback, [
                ui_anim_data,
            ],
            extra_buttons = None,
            search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_PARTICLE_SYSTEM(self):

        self.items.clear()
        return
        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        uianim_psys = ui.set_pp(lambda: self.w.active_modifier.particle_system, ParticleSystem, lambda: "particle_systems")

        b0 = ui.new_block()

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        o_particle_settings = b0.r_prop("settings", text="", isdarkhard=True, options={"RICH": "PARTICLE"})
        o_particle_settings.set_align("FULL")
        o_particle_settings.r_button_width = Ui.r_button_width_FULL_1
        b0.items.append(ButtonOverlay(o_particle_settings.w, button_search, o_particle_settings))

        uianim_part = b0.set_pp(lambda: self.w.active_modifier.particle_system.settings, ParticleSettings, NS)
        uianims = [uianim_psys, uianim_part]
        ps_psys = uianim_psys.props
        ps_part = uianim_part.props

        def bufn_particle_edited_clear():
            with bpy.context.temp_override(
                object = self.w.active_object,
                particle_system = self.w.active_modifier.particle_system
                ):
                bpy.ops.particle.edited_clear()
                update_scene_push("Particle Delete Edit")
            #|
        def bufn_particle_connect_hair():
            with bpy.context.temp_override(
                object = self.w.active_object,
                particle_system = self.w.active_modifier.particle_system
                ):
                bpy.ops.particle.connect_hair(all=False)
                update_scene_push("Particle Connect Hair")
            #|
        def bufn_particle_connect_all():
            with bpy.context.temp_override(
                object = self.w.active_object,
                particle_system = self.w.active_modifier.particle_system
                ):
                bpy.ops.particle.connect_hair(all=True)
                update_scene_push("Particle Connect All")
            #|
        def bufn_particle_disconnect_hair():
            with bpy.context.temp_override(
                object = self.w.active_object,
                particle_system = self.w.active_modifier.particle_system
                ):
                bpy.ops.particle.disconnect_hair(all=False)
                update_scene_push("Particle Disconnect Hair")
            #|
        def bufn_particle_disconnect_all():
            with bpy.context.temp_override(
                object = self.w.active_object,
                particle_system = self.w.active_modifier.particle_system
                ):
                bpy.ops.particle.disconnect_hair(all=True)
                update_scene_push("Particle Disconnect All")
            #|

        o_particle_edited_clear = b0.r_function(RNA_particle_edited_clear, bufn_particle_edited_clear, isdarkhard=True)
        o_particle_connect_hair = b0.r_function([RNA_particle_connect_hair, RNA_particle_connect_all], [bufn_particle_connect_hair, bufn_particle_connect_all], isdarkhard=True)
        o_particle_disconnect_hair = b0.r_function([RNA_particle_disconnect_hair, RNA_particle_disconnect_all], [bufn_particle_disconnect_hair, bufn_particle_disconnect_all], isdarkhard=True)
        extra_buttons = [
            o_particle_edited_clear,
            o_particle_connect_hair,
            o_particle_disconnect_hair,
        ]
        for e in extra_buttons:
            e.dark()
        o_particle_settings.dark()

        b0_state = []
        ps_psys_b0 = {}
        ps_part_b0 = {}

        # <<< 1copy (0defui_particle_create,, $$)
        def create_b0(psys, part, particle_panel_enabled):
            o_particle_edited_clear.dark()
            o_particle_connect_hair.dark()
            o_particle_disconnect_hair.dark()

            if part.is_fluid:
                o_particle_settings.dark()
                b0.label(["{:d} fluid particles for this frame".format(part.count)])
                return

            if particle_panel_enabled:
                o_particle_settings.light()
                b0.set_pp_from(uianim_part)
                b0.prop_flag("type", isdarkhard=True)
                ps_part_b0["type"] = ps_part["type"]
            else:
                o_particle_settings.dark()

            if part.type == 'HAIR':
                if psys.is_edited:
                    b0.items.append(o_particle_edited_clear)
                    o_particle_edited_clear.light()

                    if psys.is_global_hair:
                        b0.items.append(o_particle_connect_hair)
                        o_particle_connect_hair.light()
                    else:
                        b0.items.append(o_particle_disconnect_hair)
                        o_particle_disconnect_hair.light()
                else:
                    if particle_panel_enabled:
                        b0.prop("use_regrow_hair", isdarkhard=True)
                        ps_part_b0["use_regrow_hair"] = ps_part["use_regrow_hair"]
                        b0.prop("use_advanced_hair", isdarkhard=True)
                        ps_part_b0["use_advanced_hair"] = ps_part["use_advanced_hair"]
            else:
                pass
                # if part.type == 'REACTOR' and particle_panel_enabled:
                #     b0.set_pp_from(uianim_psys)
                #     b0.prop("reactor_target_object", isdarkhard=True, options={"ID":"OBJECT"})
                #     ps_psys_b0["reactor_target_object"] = ps_psys["reactor_target_object"]
        # >>>

        def fn_darklight(psys):
            part = psys.settings
            if part.type in {'EMITTER', 'REACTOR'} and part.physics_type in {'NO', 'KEYED'}:
                particle_panel_enabled = True
            else:
                particle_panel_enabled = (psys.point_cache.is_baked is False) and (not psys.is_edited) and (not psys.is_editable)
            is_dirty = False

            if b0_state == [part.is_fluid, particle_panel_enabled]: pass
            else:
                b0_state[:] = [part.is_fluid, particle_panel_enabled]
                is_dirty = True
                for k in ps_psys_b0:
                    del ps_psys[k]
                for k in ps_part_b0:
                    del ps_part[k]
                ps_psys_b0.clear()
                ps_part_b0.clear()
                del b0.items[1 : ]
                create_b0(psys, part, particle_panel_enabled)

            if is_dirty is True: return True
            #|

        def upd_data_callback():
            if uianim_psys.update_with(fn_darklight) is True:

                for e in uianims:
                    e.tag_update()
                self.redraw_from_headkey_with(search_data)
                return

            uianim_part.update_with(N1)

        button_search.fn = self.r_bufn_search(upd_data_callback, uianims,
            extra_buttons = extra_buttons,
            search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_REMESH(self):

        if not bpy.app.build_options.mod_remesh:
            b0 = Blocks(self)
            b0.buttons = [Title("  Built without Remesh modifier")]
            self.items[:] = [b0]
            return

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        props["mode"].r_button_width = self.r_button_width_200
        b0.sep(1)
        b0.prop("use_smooth_shade", isdarkhard=True)
        b0.prop("voxel_size", isdarkhard=True)
        b0.prop("adaptivity", isdarkhard=True)
        b0.sep(2)
        b0.prop("octree_depth", isdarkhard=True)
        b0.prop("scale", isdarkhard=True)
        b0.prop("sharpness", isdarkhard=True)
        b0.prop("use_remove_disconnected", isdarkhard=True)
        b0.prop("threshold", isdarkhard=True)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.mode]

            if ui_anim_data.library_state == 1: return

            if md.mode == "VOXEL":
                props["voxel_size"].light()
                props["adaptivity"].light()
                props["octree_depth"].dark()
                props["scale"].dark()
                props["sharpness"].dark()
                props["use_remove_disconnected"].dark()
                props["threshold"].dark()
            else:
                props["voxel_size"].dark()
                props["sharpness"].dark()
                props["adaptivity"].dark()
                props["octree_depth"].light()
                props["scale"].light()
                props["use_remove_disconnected"].light()
                props["threshold"].light()

                if md.mode == "SHARP":
                    props["sharpness"].light()
                else:
                    props["sharpness"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SCREW(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("angle")
        b0.prop("screw_offset")
        b0.prop("iterations")
        b0.sep(3)
        b0.prop_flag("axis")
        b0.prop("object", options={"ID":"OBJECT"})
        b0.prop("use_object_screw_offset")
        b0.sep(3)
        b0.prop("steps", text="Steps Viewport")
        b0.join_prop("render_steps", text="Render")
        b0.sep(3)
        b0.prop("merge_threshold", text="")
        b0.join_bool("use_merge_vertices", text="Merge")
        b0.sep(3)
        b0.prop_flag(["use_stretch_u", "use_stretch_v"], text="Stretch UVs", options={"NAMES": "UV"})

        b1 = ui.new_block(title="Normals")
        b1.prop("use_smooth_shade")
        b1.prop("use_normal_calculate")
        b1.prop("use_normal_flip")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, (True  if md.object else False), md.use_object_screw_offset, md.use_merge_vertices]: return
            ui_state[:] = [ui_anim_data.library_state, (True  if md.object else False), md.use_object_screw_offset, md.use_merge_vertices]

            if ui_anim_data.library_state == 1: return

            if md.object:
                props["use_object_screw_offset"].light()

                if md.use_object_screw_offset:
                    props["screw_offset"].dark()
                else:
                    props["screw_offset"].light()
            else:
                props["use_object_screw_offset"].dark()
                props["screw_offset"].light()

            if md.use_merge_vertices:
                props["merge_threshold"].light()
            else:
                props["merge_threshold"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SHRINKWRAP(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("wrap_method")
        props["wrap_method"].set_align("FULL")
        b0.sep(2)
        b0.prop("wrap_mode")
        b0.prop("target", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b0.prop("auxiliary_target", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b0.prop("offset")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.sep(2)
        b0.prop("project_limit", text="Limit")
        b0.prop("subsurf_levels")
        b0.sep(2)
        b0.prop_flag(["use_project_x", "use_project_y", "use_project_z"], text="Axis", options={"NAMES": "XYZ"})
        b0.prop_flag(["use_negative_direction", "use_positive_direction"], text="Direction", options={"NAMES": ("Negative", "Positive")})
        b0.sep(2)
        b0.prop_flag("cull_face")
        b0.prop("use_invert_cull")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.wrap_method, md.use_negative_direction, md.cull_face]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.wrap_method, md.use_negative_direction, md.cull_face]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.wrap_method == "PROJECT":
                props["project_limit"].light()
                props["subsurf_levels"].light()
                props["use_project_x"].light()
                props["use_negative_direction"].light()
                props["cull_face"].light()
                props["auxiliary_target"].light()

                props["wrap_mode"].light()

                if md.use_negative_direction and md.cull_face in {"FRONT", "BACK"}:
                    props["use_invert_cull"].light()
                else:
                    props["use_invert_cull"].dark()
            else:
                props["project_limit"].dark()
                props["subsurf_levels"].dark()
                props["use_project_x"].dark()
                props["use_negative_direction"].dark()
                props["cull_face"].dark()
                props["auxiliary_target"].dark()

                if md.wrap_method == "NEAREST_VERTEX":
                    props["wrap_mode"].dark()
                else:
                    props["wrap_mode"].light()

                props["use_invert_cull"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SIMPLE_DEFORM(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("deform_method")
        props["deform_method"].r_button_width = self.r_button_width_200
        b0.sep(2)
        b0.prop("angle")
        b0.prop("factor")
        b0.sep(0)
        b0.prop("origin", options={"ID":"OBJECT"})
        b0.sep(0)
        b0.prop_flag("deform_axis")

        b1 = ui.new_block(title="Restrictions")
        b1.prop("limits")
        b1.sep(0)
        b1.prop_flag(["lock_x", "lock_y", "lock_z"], text="Lock", options={"NAMES": "XYZ"})
        b1.sep(0)
        b1.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.deform_method, md.deform_axis]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.deform_method, md.deform_axis]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.deform_method in {"TAPER", "STRETCH"}:
                props["factor"].light()
                props["angle"].dark()
            else:
                props["factor"].dark()
                props["angle"].light()

            if md.deform_method == "BEND":
                props["lock_x"].dark()
            else:
                deform_axis = md.deform_axis
                if deform_axis == "X":
                    props["lock_x"].dark(0)
                    props["lock_x"].light(1)
                    props["lock_x"].light(2)
                elif deform_axis == "Y":
                    props["lock_x"].light(0)
                    props["lock_x"].dark(1)
                    props["lock_x"].light(2)
                elif deform_axis == "Z":
                    props["lock_x"].light(0)
                    props["lock_x"].light(1)
                    props["lock_x"].dark(2)
                else:
                    props["lock_x"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SKIN(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("branch_smoothing")
        b0.prop_flag(["use_x_symmetry", "use_y_symmetry", "use_z_symmetry"], text="Symmetry", options={"NAMES": "XYZ"})
        b0.prop("use_smooth_shade")
        b0.sep(3)
        o_skin_create_add = b0.function([RNA_SKIN_create_armature, RNA_SKIN_add_skin_data], [self.bufn_SKIN_create_armature, self.bufn_SKIN_add_skin_data], isdarkhard=True)
        o_loose_mark_clear = b0.function([RNA_SKIN_mark_loose, RNA_SKIN_clear_loose], [self.bufn_SKIN_mark_loose, self.bufn_SKIN_clear_loose], isdarkhard=True)
        b0.sep(2)
        o_mark_root = b0.function(RNA_SKIN_mark_root, self.bufn_SKIN_mark_root, isdarkhard=True)
        o_equalize_radii = b0.function(RNA_SKIN_equalize_radii, self.bufn_SKIN_equalize_radii, isdarkhard=True)

        ui_state = []

        def fn_darklight(md):
            ob = self.w.active_object
            has_skin_data = True  if ob.data.skin_vertices else False

            if ui_state == [ui_anim_data.library_state, has_skin_data, ob.mode]: return
            ui_state[:] = [ui_anim_data.library_state, has_skin_data, ob.mode]

            if ui_anim_data.library_state == 1:
                o_skin_create_add.dark()
                o_loose_mark_clear.dark()
                o_mark_root.dark()
                o_equalize_radii.dark()
                return

            if ob.mode == "EDIT":
                o_loose_mark_clear.light()
                o_mark_root.light()
                o_equalize_radii.light()

                o_skin_create_add.dark(0)

                if has_skin_data:
                    o_skin_create_add.dark(1)
                else:
                    o_skin_create_add.light(1)
            else:
                o_loose_mark_clear.dark()
                o_mark_root.dark()
                o_equalize_radii.dark()

                if has_skin_data:
                    o_skin_create_add.light(0)
                    o_skin_create_add.dark(1)
                else:
                    o_skin_create_add.dark(0)
                    o_skin_create_add.light(1)

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SMOOTH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag(["use_x", "use_y", "use_z"], text="Axis", options={"NAMES": "XYZ"})
        b0.prop("factor")
        b0.prop("iterations")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SOFT_BODY(self):

        # <<< 1copy (0defsoftbody,, $$)
        def r_settings():
            return self.w.active_modifier.settings
        def r_point_cache():
            return self.w.active_modifier.point_cache
        def r_effector_weights():
            return self.w.active_modifier.settings.effector_weights

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        uianim = ui.set_pp(r_settings, bpytypes.SoftBodySettings, self.rr_dph(".settings"))
        ps = uianim.props

        b0 = ui.new_block()

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})

        search_data = self.search_data
        search_data.init_with(button_search)

        o_collision_collection = b0.r_prop("collision_collection", options={"ID":"COLLECTION"})
        b0.items.append(ButtonOverlay(o_collision_collection.w, button_search, o_collision_collection))
        b0.prop("speed", text="Simulation Speed", isdarkhard=True)

        b_object = ui.new_block(title="Object")
        b_object.prop("friction", isdarkhard=True)
        b_object.prop("mass", isdarkhard=True)
        b_object.prop_search("vertex_group_mass", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Control Point", isdarkhard=True)

        uianim_cache, fn_darklight_cache, blocklis_caches, media_caches, extra_buttons = ui_point_cache(
            "SOFTBODY", ui, r_point_cache, self.rr_dph(".point_cache"), self.r_object)

        b_goal = ui.new_block(title=ui.r_prop("use_goal", text="Goal", options={"HEAD"}))
        b_goal.prop_search("vertex_group_goal", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Vertex Group", isdarkhard=True)
        ps["vertex_group_goal"].set_callback = update_scene_and_ref
        b_goal.sep(1)
        b_settings = b_goal.new_block(title="Settings")
        b_settings.prop("goal_spring", text="Stiffness")
        b_settings.prop("goal_friction", text="Damping")
        b_strengths = b_goal.new_block(title="Strengths")
        b_strengths.prop("goal_default", "Default")
        b_strengths.sep(1)
        b_strengths.prop("goal_min", text="Min")
        b_strengths.join_prop("goal_max", text="Max")

        b_edges = ui.new_block(ui.r_prop("use_edges", text="Edges", options={"HEAD"}))
        b_edges.prop_search("vertex_group_spring", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Springs")
        b_edges.sep(1)
        b_edges.prop("pull")
        b_edges.prop("push")
        b_edges.sep(1)
        b_edges.prop("damping")
        b_edges.prop("plastic")
        b_edges.prop("bend")
        b_edges.sep(1)
        b_edges.prop("spring_length", text="Length")
        b_edges.sep(1)
        b_edges.prop("use_edge_collision", text=("Collision", "Edge"))
        b_edges.prop("use_face_collision", text="Face")
        b_edges.sep(1)
        b_aerodynamics = b_edges.new_block(title="Aerodynamics")
        b_aerodynamics.prop_flag("aerodynamics_type", text="Type")
        b_aerodynamics.prop("aero", text="Factor")
        b_stiffness = b_edges.new_block(title=b_edges.r_prop("use_stiff_quads", options={"HEAD"}))
        b_stiffness.prop("shear")
        ps["shear"].set_callback = update_scene_and_ref

        b_collision = ui.new_block(ui.r_prop("use_self_collision", options={"HEAD"}))
        b_collision.prop("collision_type", text="Calculation Type")
        b_collision.sep(1)
        b_collision.prop("ball_size", text="Ball Size")
        b_collision.prop("ball_stiff", text="Stiffness")
        b_collision.prop("ball_damp", text="Dampening")

        b_solver = ui.new_block(title="Solver")
        b_solver.prop("step_min", text="Step Size Min")
        b_solver.join_prop("step_max", text="Max")
        b_solver.prop("use_auto_step", text="Auto-Step")
        b_solver.prop("error_threshold")
        b_solver.sep(1)
        b_diagnostics = b_solver.new_block(title="Diagnostics")
        b_diagnostics.prop("use_diagnose", options={"FLIP"})
        ps["use_diagnose"].set_callback = update_scene_and_ref
        b_diagnostics.prop("use_estimate_matrix")
        ps["use_estimate_matrix"].set_callback = update_scene_and_ref
        b_helpers = b_solver.new_block(title="Helpers")
        b_helpers.prop("choke")
        b_helpers.prop("fuzzy")

        uianim_effector_weights, fn_darklight_effector_weights = ui_effector_weights(
            "SOFTBODY", ui, r_effector_weights, self.rr_dph(".settings.effector_weights"))

        ui_state = []

        def fn_darklight(sb):
            if ui_state == [uianim.library_state, self.w.active_modifier.point_cache.is_baked, sb.use_goal, sb.use_self_collision, sb.use_edges, sb.use_stiff_quads]: return
            ui_state[:] = [uianim.library_state, self.w.active_modifier.point_cache.is_baked, sb.use_goal, sb.use_self_collision, sb.use_edges, sb.use_stiff_quads]

            if uianim.library_state == 1: return

            if self.w.active_modifier.point_cache.is_baked:
                if ps["speed"].isdark is False:
                    ps["speed"].dark()
                    b_object.w.dark()
                    b_goal.w.dark()
                    b_collision.w.dark()
                    b_solver.w.dark()
                    b_edges.w.dark()
                return

            if ps["speed"].isdark is True:
                ps["speed"].light()
                b_object.w.light()
                b_goal.w.light()
                b_collision.w.light()
                b_solver.w.light()
                b_edges.w.light()

            if sb.use_goal:
                b_goal.w.light(use_head=False)
            else:
                b_goal.w.dark(use_head=False)

            if sb.use_self_collision:
                b_collision.w.light(use_head=False)
            else:
                b_collision.w.dark(use_head=False)

            if sb.use_edges:
                b_edges.w.light(use_head=False)

                if sb.use_stiff_quads:
                    ps["shear"].light()
                else:
                    ps["shear"].dark()
            else:
                b_edges.w.dark(use_head=False)

        def upd_data_callback():
            uianim.update_with(fn_darklight)
            uianim_cache.update_with(fn_darklight_cache)
            uianim_effector_weights.update_with(fn_darklight_effector_weights)

            blocklis_caches.upd_data()
            media_caches.upd_data()

        button_search.fn = self.r_bufn_search(upd_data_callback, [
                uianim,
                uianim_cache,
                uianim_effector_weights,
            ],
            extra_buttons = extra_buttons,
            search_data = search_data)

        self.upd_data_callback = upd_data_callback
        # >>>
        #|
    def init_tab_SOLIDIFY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        o_solidify_mode = b0.r_prop_flag("solidify_mode")

        b0.items.append(ButtonOverlay(o_solidify_mode.w, button_search, o_solidify_mode))

        b0.prop("nonmanifold_thickness_mode")
        b0.prop("nonmanifold_boundary_mode", text="Boundary")
        b0.prop("thickness")
        b0.prop("offset")
        b0.prop("nonmanifold_merge_threshold")
        b0.prop("use_even_offset")
        b0.sep(2)
        b0.prop("use_rim", text=("Rim", "Fill"))
        b0.prop("use_rim_only")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("thickness_vertex_group")
        b0.prop("use_flat_faces")

        b_normals = ui.new_block(title="Normals")
        b_normals.prop("use_flip_normals", text="Flip")
        b_normals.prop("use_quality_normals", text="High Quality")

        b_materials = ui.new_block(title="Materials")
        b_materials.prop("material_offset")
        b_materials.prop("material_offset_rim", "Rim")

        b_edge_data = ui.new_block(title="Edge Data")
        b_edge_data.prop("edge_crease_inner", text="Crease Inner")
        b_edge_data.join_prop("edge_crease_outer", text="Outer")
        b_edge_data.join_prop("edge_crease_rim", text="Rim")
        b_edge_data.sep(1)
        b_edge_data.prop("bevel_convex")

        b_clamp = ui.new_block(title="Thickness Clamp")
        b_clamp.prop("thickness_clamp")
        b_clamp.prop("use_thickness_angle_clamp")

        b_output = ui.new_block(title="Output Vertex Groups")
        b_output.prop_search("shell_vertex_group", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Shell")
        b_output.prop_search("rim_vertex_group", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Rim")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.thickness_clamp, md.solidify_mode, md.use_rim]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.thickness_clamp, md.solidify_mode, md.use_rim]

            if ui_anim_data.library_state == 1: return

            if md.thickness_clamp > 0.0:
                props["use_thickness_angle_clamp"].light()
            else:
                props["use_thickness_angle_clamp"].dark()

            if md.vertex_group:
                props["invert_vertex_group"].light()
                props["thickness_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()
                props["thickness_vertex_group"].dark()

            if md.solidify_mode == 'NON_MANIFOLD':
                if md.vertex_group:
                    props["use_flat_faces"].light()
                else:
                    props["use_flat_faces"].dark()

                props["use_quality_normals"].dark()
                props["use_even_offset"].dark()
                props["edge_crease_inner"].dark()
                props["edge_crease_outer"].dark()
                props["edge_crease_rim"].dark()
                props["nonmanifold_thickness_mode"].light()
                props["nonmanifold_boundary_mode"].light()
            else:
                props["use_flat_faces"].dark()

                props["use_quality_normals"].light()
                props["use_even_offset"].light()
                props["edge_crease_inner"].light()
                props["edge_crease_outer"].light()
                props["edge_crease_rim"].light()
                props["nonmanifold_thickness_mode"].dark()
                props["nonmanifold_boundary_mode"].dark()

            if md.use_rim:
                props["use_rim_only"].light()
                props["material_offset_rim"].light()
            else:
                props["use_rim_only"].dark()
                props["material_offset_rim"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        button_search.fn = self.r_bufn_search(upd_data_callback, [
                ui_anim_data,
            ],
            extra_buttons = None,
            search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SUBSURF(self):

        md = self.w.active_modifier
        ob = self.w.active_object

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("subdivision_type", text="Type")
        props["subdivision_type"].r_button_width = self.r_button_width_200
        b0.sep(2)

        if (ob.cycles and bpy.context.engine == 'CYCLES' and md == ob.modifiers[-1] and bpy.context.scene.cycles.feature_set == 'EXPERIMENTAL'):
            ui_anim_cycles = b0.set_pp(lambda: self.w.active_object.cycles, ob.cycles, lambda: "cycles")
            ps_cycles = ui_anim_cycles.props
            ui_properties = Info1(self)

            b0.prop("use_adaptive_subdivision", text="Adaptive Subdivision")
            ps_cycles["use_adaptive_subdivision"].set_callback = update_scene_and_ref
            b0.prop("dicing_rate")
            ps_cycles["dicing_rate"].set_callback = update_scene_and_ref

            ui_anim_data_properties = b0.set_pp(lambda: ui_properties, ui_properties, NS)
            o_info = b0.r_prop("info", text="Final Scale")
            o_info.set_align("FULL")
            b_scene = b0.new_block(title=o_info)
            ui_anim_scene_cycles = b_scene.set_pp(lambda: bpy.context.scene.cycles, bpy.context.scene.cycles, lambda: "cycles")
            ps_scene_cycles = ui_anim_scene_cycles.props
            b_scene.prop("dicing_rate", text="Scene Dicing Rate Render")
            ps_scene_cycles["dicing_rate"].set_callback = update_scene_and_ref
            b_scene.join_prop("preview_dicing_rate", text="Viewport")
            ps_scene_cycles["preview_dicing_rate"].set_callback = update_scene_and_ref
            b_scene.sep(2)
            b_scene.prop("offscreen_dicing_scale", text="Offscreen Scale")
            ps_scene_cycles["offscreen_dicing_scale"].set_callback = update_scene_and_ref
            b_scene.prop("max_subdivisions")
            ps_scene_cycles["max_subdivisions"].set_callback = update_scene_and_ref
            b_scene.prop("dicing_camera", options={"ID":"OBJECT"})
            ps_scene_cycles["dicing_camera"].set_callback = update_scene_and_ref

            b0.sep(1)
            b0.set_pp_from(ui_anim_data)
            # <<< 1copy (0definit_tab_SUBSURF,, $$)
            b0.prop("levels", text="Levels Viewport")
            b0.join_prop("render_levels", text="Render")
            props["render_levels"].set_callback = update_scene_and_ref
            b0.prop("show_only_control_edges")

            b_advanced = ui.new_block(title="Advanced")
            b_advanced.prop("use_limit_surface", text="Limit Surface")
            b_advanced.prop("quality")
            b_advanced.prop("use_creases", text="Creases")
            b_advanced.prop("use_custom_normals", text="Custom Normals")
            b_advanced.sep(1)
            b_advanced.prop("uv_smooth")
            props["uv_smooth"].r_button_width = self.r_button_width_150
            b_advanced.prop_flag("boundary_smooth")
            props["boundary_smooth"].r_button_width = self.r_button_width_150
            # >>>

            ui_state = []
            ui_state_cycles = []

            def fn_darklight(md):
                cycles = self.w.active_object.cycles
                scene_cycles = bpy.context.scene.cycles
                if ui_state == [ui_anim_data.library_state, md.use_limit_surface, cycles.use_adaptive_subdivision, cycles.dicing_rate, scene_cycles.dicing_rate, scene_cycles.preview_dicing_rate]: return
                ui_state[:] = [ui_anim_data.library_state, md.use_limit_surface, cycles.use_adaptive_subdivision, cycles.dicing_rate, scene_cycles.dicing_rate, scene_cycles.preview_dicing_rate]

                if ui_anim_data.library_state == 1: return

                if md.use_limit_surface:
                    ps_cycles["use_adaptive_subdivision"].light()
                else:
                    ps_cycles["use_adaptive_subdivision"].dark()

                if md.use_limit_surface and cycles.use_adaptive_subdivision:
                    ui_properties.info = f"Render {max(scene_cycles.dicing_rate * cycles.dicing_rate, 0.1):.2f} px  |  Viewport {max(scene_cycles.preview_dicing_rate * cycles.dicing_rate, 0.1):.2f} px"
                    o_info.upd_data()

                    ps_cycles["dicing_rate"].light()
                    o_info.light()

                    props["use_limit_surface"].dark()
                    props["render_levels"].dark()
                    props["quality"].dark()
                    props["uv_smooth"].dark()
                    props["boundary_smooth"].dark()
                    props["use_creases"].dark()
                    props["use_custom_normals"].dark()
                else:
                    ui_properties.info = ""
                    o_info.upd_data()

                    ps_cycles["dicing_rate"].dark()
                    o_info.dark()

                    props["use_limit_surface"].light()
                    props["render_levels"].light()
                    props["uv_smooth"].light()
                    props["boundary_smooth"].light()
                    props["use_creases"].light()
                    props["use_custom_normals"].light()

                    if md.use_limit_surface:
                        props["quality"].light()
                    else:
                        props["quality"].dark()

            def upd_data_callback():
                md = self.w.active_modifier
                ob = self.w.active_object
                if (ob.cycles and bpy.context.engine == 'CYCLES' and md == ob.modifiers[-1] and bpy.context.scene.cycles.feature_set == 'EXPERIMENTAL'): pass
                else:
                    self.init_tab(self.active_tab, push=False, evtkill=False)
                    return

                ui_anim_data.update_with(fn_darklight)
                ui_anim_cycles.update_with(N1)
                ui_anim_scene_cycles.update_with(N1)
        else:
            # /* 0definit_tab_SUBSURF
            b0.prop("levels", text="Levels Viewport")
            b0.join_prop("render_levels", text="Render")
            props["render_levels"].set_callback = update_scene_and_ref
            b0.prop("show_only_control_edges")

            b_advanced = ui.new_block(title="Advanced")
            b_advanced.prop("use_limit_surface", text="Limit Surface")
            b_advanced.prop("quality")
            b_advanced.prop("use_creases", text="Creases")
            b_advanced.prop("use_custom_normals", text="Custom Normals")
            b_advanced.sep(1)
            b_advanced.prop("uv_smooth")
            props["uv_smooth"].r_button_width = self.r_button_width_150
            b_advanced.prop_flag("boundary_smooth")
            props["boundary_smooth"].r_button_width = self.r_button_width_150
            # */

            ui_state = []

            def fn_darklight(md):
                if ui_state == [ui_anim_data.library_state, md.use_limit_surface]: return
                ui_state[:] = [ui_anim_data.library_state, md.use_limit_surface]

                if ui_anim_data.library_state == 1: return

                if md.use_limit_surface:
                    props["quality"].light()
                else:
                    props["quality"].dark()

            def upd_data_callback():
                md = self.w.active_modifier
                ob = self.w.active_object
                if (ob.cycles and bpy.context.engine == 'CYCLES' and md == ob.modifiers[-1] and bpy.context.scene.cycles.feature_set == 'EXPERIMENTAL'):
                    self.init_tab(self.active_tab, push=False, evtkill=False)
                    return

                ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_SURFACE(self):

        b0 = Blocks(self)
        b0.buttons = [Title("  Settings are inside the Physics tab")]
        self.items[:] = [b0]
        #|
    def init_tab_SURFACE_DEFORM(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("target", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b0.prop("falloff")
        b0.prop("strength")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("use_sparse_bind")
        b0.sep(3)
        o_bind = b0.function(RNA_SURFACE_DEFORM_bind, self.bufn_SURFACE_DEFORM_bind, isdarkhard=True)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.is_bound, (True  if md.target else False)]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.is_bound, (True  if md.target else False)]

            if ui_anim_data.library_state == 1:
                o_bind.dark()
                return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.is_bound:
                o_bind.light()

                props["use_sparse_bind"].dark()

                props["target"].dark()
                props["falloff"].dark()
                o_bind.set_button_text("Unbind")
            else:
                if md.target:
                    o_bind.light()
                else:
                    o_bind.dark()

                if md.vertex_group:
                    props["use_sparse_bind"].light()
                else:
                    props["use_sparse_bind"].dark()

                props["target"].light()
                props["falloff"].light()
                o_bind.set_button_text("Bind")

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_TRIANGULATE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("quad_method")
        b0.prop_flag("ngon_method")
        b0.prop("min_vertices")
        if "keep_custom_normals" in ui_anim_data.rnas:
            b0.prop("keep_custom_normals")

        def upd_data_callback():
            ui_anim_data.update_with(N1)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_UV_PROJECT(self):

        def rr_projector(i):
            def r_projector():
                return self.w.active_modifier.projectors[i]
            return r_projector
        def rr_dph_projector(i):
            def r_dph_projector():
                return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].projectors[{i}]'
            return r_dph_projector

        UVProjector = bpytypes.UVProjector

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_search("uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)
        b0.sep(2)
        b0.prop("aspect_x")
        b0.join_prop("aspect_y", text="Y")
        b0.sep(2)
        b0.prop("scale_x")
        b0.join_prop("scale_y", text="Y")

        b1 = ui.new_block(ui.r_prop("projector_count", text="Projectors"))
        ui_anims = []

        ui_state = []
        ui_type_state = [0]

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, any((e.object and e.object.type == 'CAMERA')  for e in md.projectors)]: return
            ui_state[:] = [ui_anim_data.library_state, any((e.object and e.object.type == 'CAMERA')  for e in md.projectors)]

            if ui_anim_data.library_state == 1: return

            if any((e.object and e.object.type == 'CAMERA')  for e in md.projectors):
                props["aspect_x"].light()
                props["aspect_y"].light()
                props["scale_x"].light()
                props["scale_y"].light()
            else:
                props["aspect_x"].dark()
                props["aspect_y"].dark()
                props["scale_x"].dark()
                props["scale_y"].dark()

        def upd_data_callback():
            if ui_type_state[0] == len(self.w.active_modifier.projectors): pass
            else:
                ui_type_state[0] = len(self.w.active_modifier.projectors)


                ui_anims.clear()
                b1.w.items.clear()
                for r, e in enumerate(self.w.active_modifier.projectors):
                    ui_anims.append(b1.set_pp(rr_projector(r), UVProjector, rr_dph_projector(r)))
                    b1.prop("object", options={"ID":"OBJECT"})

                for ui_anim in ui_anims:
                    ui_anim.tag_update()
                self.redraw_from_headkey()
                self.upd_data()
                return

            ui_anim_data.update_with(fn_darklight)
            for ui_anim in ui_anims:
                ui_anim.update_with(N1)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_UV_WARP(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_search("uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)
        b0.prop("center")
        b0.sep(2)
        b0.prop_flag("axis_u", text="Axis U")
        b0.prop_flag("axis_v", text="V")
        b0.sep(2)
        b0.prop("object_from", options={"ID":"OBJECT"})
        b0.prop("object_to", options={"ID":"OBJECT"}, text="To")
        b0.prop_search("bone_from", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().object_from))
        b0.prop_search("bone_to", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().object_to), text="To")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        b1 = ui.new_block(title="Transform")
        b1.prop("offset")
        b1.sep(0)
        b1.prop("scale")
        b1.sep(0)
        b1.prop("rotation")

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'object_from'}$)
            if md.object_from:
                name_object_from = md.object_from.name
                state_object_from = 0  if md.object_from.type == "ARMATURE" else 1
            else:
                name_object_from = ""
                state_object_from = 2
            # >>>
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'object_to'}$)
            if md.object_to:
                name_object_to = md.object_to.name
                state_object_to = 0  if md.object_to.type == "ARMATURE" else 1
            else:
                name_object_to = ""
                state_object_to = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.vertex_group, state_object_from, state_object_to, name_object_from, name_object_to]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, state_object_from, state_object_to, name_object_from, name_object_to]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if state_object_from == 0:
                props["bone_from"].light()
            else:
                props["bone_from"].dark()

            if state_object_to == 0:
                props["bone_to"].light()
            else:
                props["bone_to"].dark()

            props["bone_from"].tag_clipping_dirty()
            props["bone_to"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_VERTEX_WEIGHT_EDIT(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_search("vertex_group", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups)
        b0.prop("default_weight")
        b0.prop("add_threshold", text="")
        b0.join_bool("use_add", text="Group Add Threshold")
        b0.prop("remove_threshold", text="")
        b0.join_bool("use_remove", text="Remove Threshold")
        b0.sep(1)
        b0.prop("normalize")

        o_falloff_type = ui.r_prop("falloff_type", text="", options={"D_icon": D_geticon_falloff})
        o_invert_falloff = ui.r_prop("invert_falloff", options={"icon_cls": GpuImg_invert})
        props["invert_falloff"].r_button_width = lambda: 0
        b1 = ui.new_block(title=ButtonOverlay(None, o_invert_falloff, o_falloff_type))
        b1.w.blf_title.text = "Falloff"
        o_edit_curve = b1.function(RNA_edit_curve, self.bufn_VERTEX_WEIGHT_EDIT_edit_curve)

        b2 = ui.new_block("Influence")
        b2.prop("mask_constant", text="Global Influence")
        b2.prop_inv_vg("invert_mask_vertex_group", "mask_vertex_group", self.r_object_vertex_groups)
        b2.sep(2)
        b2.prop("mask_texture", text="Mask", options={"RICH":"TEXTURE"})
        r_button_width = self.r_button_width_166
        props["mask_texture"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop_flag("mask_tex_mapping", text="Coord")
        props["mask_tex_mapping"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop("mask_tex_use_channel", text="Channel")
        props["mask_tex_use_channel"].r_button_width = r_button_width
        b2.sep(1)
        b2.prop("mask_tex_map_object", text="Object", options={"ID":"OBJECT"})
        b2.prop_search("mask_tex_map_bone", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().mask_tex_map_object), text="Bone")
        b2.prop_search("mask_tex_uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'mask_tex_map_object'}$)
            if md.mask_tex_map_object:
                name_mask_tex_map_object = md.mask_tex_map_object.name
                state_mask_tex_map_object = 0  if md.mask_tex_map_object.type == "ARMATURE" else 1
            else:
                name_mask_tex_map_object = ""
                state_mask_tex_map_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.use_add, md.use_remove, md.falloff_type, (True  if md.mask_vertex_group else False), (True  if md.mask_texture else False), md.mask_tex_mapping, state_mask_tex_map_object, name_mask_tex_map_object]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_add, md.use_remove, md.falloff_type, (True  if md.mask_vertex_group else False), (True  if md.mask_texture else False), md.mask_tex_mapping, state_mask_tex_map_object, name_mask_tex_map_object]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if md.use_add:
                props["add_threshold"].light()
            else:
                props["add_threshold"].dark()

            if md.use_remove:
                props["remove_threshold"].light()
            else:
                props["remove_threshold"].dark()

            if md.falloff_type == "CURVE":
                o_edit_curve.light()
            else:
                o_edit_curve.dark()

            if md.mask_vertex_group:
                if md.mask_texture:
                    props["mask_vertex_group"].dark()
                    props["invert_mask_vertex_group"].dark()
                    props["mask_texture"].dark()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()
                else:
                    props["mask_vertex_group"].light()
                    props["invert_mask_vertex_group"].light()
                    props["mask_texture"].dark()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()
            else:
                props["invert_mask_vertex_group"].dark()
                props["mask_texture"].light()

                if md.mask_texture:
                    props["mask_vertex_group"].dark()
                    props["mask_tex_use_channel"].light()
                    props["mask_tex_mapping"].light()

                    if md.mask_tex_mapping == "OBJECT":
                        props["mask_tex_map_object"].light()

                        if state_mask_tex_map_object == 0:
                            props["mask_tex_map_bone"].light()
                        else:
                            props["mask_tex_map_bone"].dark()

                        props["mask_tex_uv_layer"].dark()
                    elif md.mask_tex_mapping == "UV":
                        props["mask_tex_map_object"].dark()
                        props["mask_tex_map_bone"].dark()
                        props["mask_tex_uv_layer"].light()
                    else:
                        props["mask_tex_map_object"].dark()
                        props["mask_tex_map_bone"].dark()
                        props["mask_tex_uv_layer"].dark()
                else:
                    props["mask_vertex_group"].light()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()

            props["mask_tex_map_bone"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_VERTEX_WEIGHT_MIX(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_inv_vg("invert_vertex_group_a", "vertex_group_a", self.r_object_vertex_groups)
        b0.prop_inv_vg("invert_vertex_group_b", "vertex_group_b", self.r_object_vertex_groups, text="B")
        b0.sep(2)
        b0.prop("default_weight_a")
        b0.prop("default_weight_b", text="B")
        b0.sep(2)
        b0.prop("mix_set")
        b0.prop("mix_mode")
        b0.prop("normalize")

        b2 = ui.new_block("Influence")
        b2.prop("mask_constant", text="Global Influence")
        b2.prop_inv_vg("invert_mask_vertex_group", "mask_vertex_group", self.r_object_vertex_groups)
        b2.sep(2)
        b2.prop("mask_texture", text="Mask", options={"RICH":"TEXTURE"})
        r_button_width = self.r_button_width_166
        props["mask_texture"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop_flag("mask_tex_mapping", text="Coord")
        props["mask_tex_mapping"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop("mask_tex_use_channel", text="Channel")
        props["mask_tex_use_channel"].r_button_width = r_button_width
        b2.sep(1)
        b2.prop("mask_tex_map_object", text="Object", options={"ID":"OBJECT"})
        b2.prop_search("mask_tex_map_bone", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().mask_tex_map_object), text="Bone")
        b2.prop_search("mask_tex_uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'mask_tex_map_object'}$)
            if md.mask_tex_map_object:
                name_mask_tex_map_object = md.mask_tex_map_object.name
                state_mask_tex_map_object = 0  if md.mask_tex_map_object.type == "ARMATURE" else 1
            else:
                name_mask_tex_map_object = ""
                state_mask_tex_map_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.vertex_group_a, md.vertex_group_b, (True  if md.mask_texture else False), md.mask_tex_mapping, state_mask_tex_map_object, name_mask_tex_map_object]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group_a, md.vertex_group_b, (True  if md.mask_texture else False), md.mask_tex_mapping, state_mask_tex_map_object, name_mask_tex_map_object]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group_a:
                props["invert_vertex_group_a"].light()
            else:
                props["invert_vertex_group_a"].dark()

            if md.vertex_group_b:
                props["invert_vertex_group_b"].light()
            else:
                props["invert_vertex_group_b"].dark()

            if md.mask_vertex_group:
                if md.mask_texture:
                    props["mask_vertex_group"].dark()
                    props["invert_mask_vertex_group"].dark()
                    props["mask_texture"].dark()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()
                else:
                    props["mask_vertex_group"].light()
                    props["invert_mask_vertex_group"].light()
                    props["mask_texture"].dark()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()
            else:
                props["invert_mask_vertex_group"].dark()
                props["mask_texture"].light()

                if md.mask_texture:
                    props["mask_vertex_group"].dark()
                    props["mask_tex_use_channel"].light()
                    props["mask_tex_mapping"].light()

                    if md.mask_tex_mapping == "OBJECT":
                        props["mask_tex_map_object"].light()

                        if state_mask_tex_map_object == 0:
                            props["mask_tex_map_bone"].light()
                        else:
                            props["mask_tex_map_bone"].dark()

                        props["mask_tex_uv_layer"].dark()
                    elif md.mask_tex_mapping == "UV":
                        props["mask_tex_map_object"].dark()
                        props["mask_tex_map_bone"].dark()
                        props["mask_tex_uv_layer"].light()
                    else:
                        props["mask_tex_map_object"].dark()
                        props["mask_tex_map_bone"].dark()
                        props["mask_tex_uv_layer"].dark()
                else:
                    props["mask_vertex_group"].light()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()

            props["mask_tex_map_bone"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_VERTEX_WEIGHT_PROXIMITY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_search("vertex_group", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups)
        b0.prop("target", options={"ID":"OBJECT"})
        b0.sep(2)
        b0.prop("proximity_mode")
        b0.prop("proximity_geometry")
        b0.sep(2)
        b0.prop("min_dist")
        b0.join_prop("max_dist")
        b0.prop("normalize")

        o_falloff_type = ui.r_prop("falloff_type", text="", options={"D_icon": D_geticon_falloff})
        o_invert_falloff = ui.r_prop("invert_falloff", options={"icon_cls": GpuImg_invert})
        props["invert_falloff"].r_button_width = lambda: 0
        b1 = ui.new_block(title=ButtonOverlay(None, o_invert_falloff, o_falloff_type))
        b1.w.blf_title.text = "Falloff"
        o_edit_curve = b1.function(RNA_edit_curve, self.bufn_VERTEX_WEIGHT_EDIT_edit_curve)

        b2 = ui.new_block("Influence")
        b2.prop("mask_constant", text="Global Influence")
        b2.prop_inv_vg("invert_mask_vertex_group", "mask_vertex_group", self.r_object_vertex_groups)
        b2.sep(2)
        b2.prop("mask_texture", text="Mask", options={"RICH":"TEXTURE"})
        r_button_width = self.r_button_width_166
        props["mask_texture"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop_flag("mask_tex_mapping", text="Coord")
        props["mask_tex_mapping"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop("mask_tex_use_channel", text="Channel")
        props["mask_tex_use_channel"].r_button_width = r_button_width
        b2.sep(1)
        b2.prop("mask_tex_map_object", text="Object", options={"ID":"OBJECT"})
        b2.prop_search("mask_tex_map_bone", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().mask_tex_map_object), text="Bone")
        b2.prop_search("mask_tex_uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'mask_tex_map_object'}$)
            if md.mask_tex_map_object:
                name_mask_tex_map_object = md.mask_tex_map_object.name
                state_mask_tex_map_object = 0  if md.mask_tex_map_object.type == "ARMATURE" else 1
            else:
                name_mask_tex_map_object = ""
                state_mask_tex_map_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.proximity_mode, md.falloff_type, (True  if md.mask_vertex_group else False), (True  if md.mask_texture else False), md.mask_tex_mapping, state_mask_tex_map_object, name_mask_tex_map_object]: return
            ui_state[:] = [ui_anim_data.library_state, md.proximity_mode, md.falloff_type, (True  if md.mask_vertex_group else False), (True  if md.mask_texture else False), md.mask_tex_mapping, state_mask_tex_map_object, name_mask_tex_map_object]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if md.proximity_mode == "GEOMETRY":
                props["proximity_geometry"].light()
            else:
                props["proximity_geometry"].dark()

            if md.falloff_type == "CURVE":
                o_edit_curve.light()
            else:
                o_edit_curve.dark()

            if md.mask_vertex_group:
                if md.mask_texture:
                    props["mask_vertex_group"].dark()
                    props["invert_mask_vertex_group"].dark()
                    props["mask_texture"].dark()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()
                else:
                    props["mask_vertex_group"].light()
                    props["invert_mask_vertex_group"].light()
                    props["mask_texture"].dark()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()
            else:
                props["invert_mask_vertex_group"].dark()
                props["mask_texture"].light()

                if md.mask_texture:
                    props["mask_vertex_group"].dark()
                    props["mask_tex_use_channel"].light()
                    props["mask_tex_mapping"].light()

                    if md.mask_tex_mapping == "OBJECT":
                        props["mask_tex_map_object"].light()

                        if state_mask_tex_map_object == 0:
                            props["mask_tex_map_bone"].light()
                        else:
                            props["mask_tex_map_bone"].dark()

                        props["mask_tex_uv_layer"].dark()
                    elif md.mask_tex_mapping == "UV":
                        props["mask_tex_map_object"].dark()
                        props["mask_tex_map_bone"].dark()
                        props["mask_tex_uv_layer"].light()
                    else:
                        props["mask_tex_map_object"].dark()
                        props["mask_tex_map_bone"].dark()
                        props["mask_tex_uv_layer"].dark()
                else:
                    props["mask_vertex_group"].light()
                    props["mask_tex_use_channel"].dark()
                    props["mask_tex_mapping"].dark()
                    props["mask_tex_map_object"].dark()
                    props["mask_tex_map_bone"].dark()
                    props["mask_tex_uv_layer"].dark()

            props["mask_tex_map_bone"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_VOLUME_TO_MESH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data0 = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        b0.prop("resolution_mode")
        b0.props["resolution_mode"].r_button_width = self.r_button_width_133
        ui_anim_data = b0.set_pp(self.r_modifier)
        props = b0.props

        b0.prop_flag("resolution_mode", text="")
        props["resolution_mode"].r_button_width = self.r_button_width_200
        b0.sep(2)
        b0.prop("object", options={"ID":"OBJECT"})
        b0.prop("grid_name")
        b0.sep(2)
        b0.prop("voxel_amount")
        b0.prop("voxel_size")
        b0.prop("threshold")
        b0.prop("adaptivity")
        b0.prop("use_smooth_shade")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.resolution_mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.resolution_mode]

            if ui_anim_data.library_state == 1: return

            if md.resolution_mode == "VOXEL_AMOUNT":
                props["voxel_amount"].light()
                props["voxel_size"].dark()
            elif md.resolution_mode == "VOXEL_SIZE":
                props["voxel_amount"].dark()
                props["voxel_size"].light()
            else:
                props["voxel_amount"].dark()
                props["voxel_size"].dark()

        def upd_data_callback():
            ui_anim_data0.update_with(N1)
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_WARP(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props
        b0.prop("object_from", options={"ID":"OBJECT"})
        b0.prop("object_to", text="To", options={"ID":"OBJECT"})
        b0.prop_search("bone_from", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().object_from))
        b0.prop_search("bone_to", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().object_to))
        b0.prop("use_volume_preserve")
        b0.prop("strength")
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        b1 = ui.new_block(title=ui.r_prop("falloff_type", text="", options={"D_icon": D_geticon_falloff}))
        b1.w.blf_title.text = "Falloff"
        b1.prop("falloff_radius")
        o_edit_curve = b1.function(RNA_edit_curve, self.bufn_HOOK_edit_curve)

        b2 = ui.new_block("Texture")
        b2.prop("texture", text="", options={"RICH":"TEXTURE"})
        r_button_width = self.r_button_width_200
        props["texture"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop_flag("texture_coords", text="Coord")
        props["texture_coords"].r_button_width = r_button_width
        b2.sep(1)
        b2.prop("texture_coords_object", text="Object", options={"ID":"OBJECT"})
        b2.prop_search("texture_coords_bone", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().texture_coords_object), text="Bone")
        b2.prop_search("uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'object_from'}$)
            if md.object_from:
                name_object_from = md.object_from.name
                state_object_from = 0  if md.object_from.type == "ARMATURE" else 1
            else:
                name_object_from = ""
                state_object_from = 2
            # >>>
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'object_to'}$)
            if md.object_to:
                name_object_to = md.object_to.name
                state_object_to = 0  if md.object_to.type == "ARMATURE" else 1
            else:
                name_object_to = ""
                state_object_to = 2
            # >>>
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'texture_coords_object'}$)
            if md.texture_coords_object:
                name_texture_coords_object = md.texture_coords_object.name
                state_texture_coords_object = 0  if md.texture_coords_object.type == "ARMATURE" else 1
            else:
                name_texture_coords_object = ""
                state_texture_coords_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.vertex_group, name_object_from, name_object_to, name_texture_coords_object, state_object_from, state_object_to, state_texture_coords_object, md.falloff_type, md.texture_coords]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, name_object_from, name_object_to, name_texture_coords_object, state_object_from, state_object_to, state_texture_coords_object, md.falloff_type, md.texture_coords]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if state_object_from == 0:
                props["bone_from"].light()
            else:
                props["bone_from"].dark()

            if state_object_to == 0:
                props["bone_to"].light()
            else:
                props["bone_to"].dark()

            if md.falloff_type == "CURVE":
                o_edit_curve.light()
                props["falloff_radius"].light()
            else:
                o_edit_curve.dark()

                if md.falloff_type == "NONE":
                    props["falloff_radius"].dark()
                else:
                    props["falloff_radius"].light()

            if md.texture_coords == "OBJECT":
                props["texture_coords_object"].light()
                props["uv_layer"].dark()

                if state_texture_coords_object == 0:
                    props["texture_coords_bone"].light()
                else:
                    props["texture_coords_bone"].dark()
            else:
                props["texture_coords_object"].dark()

                if md.texture_coords == "UV":
                    props["uv_layer"].light()
                else:
                    props["uv_layer"].dark()

                props["texture_coords_bone"].dark()

            props["bone_from"].tag_clipping_dirty()
            props["bone_to"].tag_clipping_dirty()
            props["texture_coords_bone"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_WAVE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag(["use_x", "use_y"], text="Motion", options={"NAMES": "XY"})
        b0.prop("use_cyclic")
        b0.sep(1)
        b0.prop_flag(["use_normal_x", "use_normal_y", "use_normal_z"], text="", options={"NAMES": "XYZ"})
        b0.join_bool("use_normal", text="Along Normals")
        b0.sep(1)
        b0.prop("falloff_radius")
        b0.prop("height")
        b0.prop("width")
        b0.prop("narrowness")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        b_start = ui.new_block(title="Start Position")
        b_start.prop("start_position_object", text="Object", options={"ID":"OBJECT"})
        b_start.sep(1)
        b_start.prop("start_position_x")
        b_start.join_prop("start_position_y", text=" Y")

        b_time = ui.new_block(title="Time")
        b_time.prop("time_offset", text="Offset")
        b_time.prop("lifetime", text="Life")
        b_time.prop("damping_time", text="Damping")
        b_time.prop("speed")

        b2 = ui.new_block("Texture")
        b2.prop("texture", text="", options={"RICH":"TEXTURE"})
        r_button_width = self.r_button_width_200
        props["texture"].r_button_width = r_button_width
        b2.sep(0)
        b2.prop_flag("texture_coords", text="Coord")
        props["texture_coords"].r_button_width = r_button_width
        b2.sep(1)
        b2.prop("texture_coords_object", text="Object", options={"ID":"OBJECT"})
        b2.prop_search("texture_coords_bone", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().texture_coords_object), text="Bone")
        b2.prop_search("uv_layer", GpuImg_GROUP_UVS, self.r_object_uvs)

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'texture_coords_object'}$)
            if md.texture_coords_object:
                name_texture_coords_object = md.texture_coords_object.name
                state_texture_coords_object = 0  if md.texture_coords_object.type == "ARMATURE" else 1
            else:
                name_texture_coords_object = ""
                state_texture_coords_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.use_normal, state_texture_coords_object, name_texture_coords_object, md.texture_coords]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.use_normal, state_texture_coords_object, name_texture_coords_object, md.texture_coords]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_normal:
                props["use_x"].light()
            else:
                props["use_x"].dark()

            if md.texture_coords == "OBJECT":
                props["texture_coords_object"].light()
                props["uv_layer"].dark()

                if state_texture_coords_object == 0:
                    props["texture_coords_bone"].light()
                else:
                    props["texture_coords_bone"].dark()
            else:
                props["texture_coords_object"].dark()

                if md.texture_coords == "UV":
                    props["uv_layer"].light()
                else:
                    props["uv_layer"].dark()

                props["texture_coords_bone"].dark()

            props["texture_coords_bone"].tag_clipping_dirty()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_WEIGHTED_NORMAL(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode", text="Mode", options={"ROW_LENGTH": 2})
        props["mode"].r_button_width = self.r_button_width_200
        b0.sep(3)
        b0.prop("weight")
        b0.prop("thresh")
        b0.sep(2)
        b0.prop("keep_sharp")
        b0.prop("use_face_influence")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_WELD(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        b0.sep(2)
        b0.prop("merge_threshold")
        b0.prop("loose_edges")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.mode]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.mode == "CONNECTED":
                props["loose_edges"].light()
            else:
                props["loose_edges"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_WIREFRAME(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("thickness")
        b0.prop("offset")
        b0.sep(2)
        b0.prop("use_boundary")
        b0.prop("use_replace", text="Replace Original")
        b0.sep(2)
        b0.prop("use_even_offset", text=("Thickness", "Even"))
        b0.prop("use_relative_offset", text="Relative")
        b0.sep(2)
        b0.prop("crease_weight", text="")
        b0.join_bool("use_crease", text="Crease Edges")
        b0.prop("material_offset")
        b0.sep(2)
        b0.prop_inv_vg("invert_vertex_group", "vertex_group", self.r_object_vertex_groups)
        b0.prop("thickness_vertex_group", text="Vertex Group Factor")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group, md.use_crease]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group, md.use_crease]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group:
                props["invert_vertex_group"].light()
                props["thickness_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()
                props["thickness_vertex_group"].dark()

            if md.use_crease:
                props["crease_weight"].light()
            else:
                props["crease_weight"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|

    def init_tab_MESH_TO_VOLUME(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT"})
        b0.prop("density")
        b0.prop("interior_band_width")
        b0.sep(2)
        b0.prop_flag("resolution_mode", options={"ROW_LENGTH": 1})
        b0.sep(2)
        b0.prop("voxel_amount")
        b0.prop("voxel_size")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.resolution_mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.resolution_mode]

            if ui_anim_data.library_state == 1: return

            if md.resolution_mode == "VOXEL_SIZE":
                props["voxel_size"].light()
                props["voxel_amount"].dark()
            else:
                props["voxel_size"].dark()
                props["voxel_amount"].light()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_VOLUME_DISPLACE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("texture", text="Texture", options={"RICH":"TEXTURE"})
        props["texture"].r_button_width = self.r_button_width_150
        b0.sep(0)
        b0.prop_flag("texture_map_mode", text="Mapping")
        props["texture_map_mode"].r_button_width = self.r_button_width_150
        b0.sep(2)
        b0.prop("texture_map_object", options={"ID":"OBJECT"})
        b0.sep(0)
        b0.prop("strength")
        b0.sep(0)
        b0.prop("texture_sample_radius", text="Sample Radius")
        b0.sep(0)
        b0.prop("texture_mid_level", text="Mid Level")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.texture_map_mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.texture_map_mode]

            if ui_anim_data.library_state == 1: return

            if md.texture_map_mode == "OBJECT":
                props["texture_map_object"].light()
            else:
                props["texture_map_object"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|

    def init_tab_GREASE_PENCIL_TEXTURE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        props["mode"].r_button_width = self.r_button_width_200
        b0.sep(2)
        b0.prop_flag("fit_method", text="Stroke Fit Method")
        props["fit_method"].r_button_width = self.r_button_width_150
        b0.prop("uv_offset")
        b0.prop("alignment_rotation")
        b0.prop("uv_scale", text="Scale")
        b0.sep(2)
        b0.prop("fill_rotation")
        b0.prop("fill_offset", text="Offset")
        b0.prop("fill_scale", text="Scale")

        # /* 0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # */

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.mode == "STROKE":
                props["fill_rotation"].dark()
                props["fill_offset"].dark()
                props["fill_scale"].dark()

                props["fit_method"].light()
                props["uv_offset"].light()
                props["alignment_rotation"].light()
                props["uv_scale"].light()
            elif md.mode == "FILL":
                props["fill_rotation"].light()
                props["fill_offset"].light()
                props["fill_scale"].light()

                props["fit_method"].dark()
                props["uv_offset"].dark()
                props["alignment_rotation"].dark()
                props["uv_scale"].dark()
            else:
                props["fill_rotation"].light()
                props["fill_offset"].light()
                props["fill_scale"].light()

                props["fit_method"].light()
                props["uv_offset"].light()
                props["alignment_rotation"].light()
                props["uv_scale"].light()

            # /* 0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # */

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_TIME(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode", options={"ROW_LENGTH": 3})
        props["mode"].r_button_width = self.r_button_width_200
        b0.sep(2)
        b0.prop("offset")
        b0.prop("frame_scale", text="Scale")
        b0.prop("use_keep_loop")

        b1 = ui.new_block(title=ui.r_prop("use_custom_frame_range", options={"HEAD"}))
        b1.prop("frame_start")
        b1.join_prop("frame_end", text="End")

        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3

        ui_state = []

        if self.w.active_modifier.mode == "CHAIN":
            modifier_type = "GREASE_PENCIL_TIME"
            # /* 0areas_gp_segment_fns
            def r_segments():
                if hasattr(self.w.active_modifier, "segments"):
                    return self.w.active_modifier.segments
                return None
            def r_segment():
                active_modifier = self.w.active_modifier
                i = active_modifier.segment_active_index
                if i < len(active_modifier.segments):
                    return active_modifier.segments[i]
                return None
            def r_dph_segment():
                active_modifier = self.w.active_modifier
                i = active_modifier.segment_active_index
                if i < len(active_modifier.segments):
                    return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].segments["{escape_identifier(active_modifier.segments[i].name)}"]'
                return ''
            def bufn_add_segments():
                modifier = self.w.active_modifier
                with bpy.context.temp_override(object=self.r_object()):
                    if modifier_type == "GREASE_PENCIL_TIME":
                        bpy.ops.object.grease_pencil_time_modifier_segment_add(modifier=modifier.name)
                    elif modifier_type == "GREASE_PENCIL_DASH":
                        bpy.ops.object.grease_pencil_dash_modifier_segment_add(modifier=modifier.name)
                    else:
                        return
            def bufn_remove_segments():
                modifier = self.w.active_modifier
                with bpy.context.temp_override(object=self.r_object()):
                    if modifier.type == "GREASE_PENCIL_TIME":
                        bpy.ops.object.grease_pencil_time_modifier_segment_remove(modifier=modifier.name)
                    elif modifier.type == "GREASE_PENCIL_DASH":
                        bpy.ops.object.grease_pencil_dash_modifier_segment_remove(modifier=modifier.name)
                    else:
                        return

            b_segments = ui.new_block(title="Segments")
            blocklis_segments = BlocklistAZ(b_segments.w,
                r_pp = r_segments,
                r_object = self.r_object,
                r_datapath_head = self.rr_dph(".segments"),
                remove_active_item = bufn_remove_segments,
                add_item = bufn_add_segments)
            blocklis_segments.r_active_index = lambda: self.w.active_modifier.segment_active_index
            blocklis_segments.set_active_index = lambda x: setattr(self.w.active_modifier, "segment_active_index", x)
            blocklis_segments_media = BlockMediaAZ(b_segments.w, blocklis_segments)
            b_segments.items += [blocklis_segments, blocklis_segments_media]
            uianim_segment = b_segments.set_pp(r_segment, bpytypes.GreasePencilTimeModifierSegment, r_dph_segment)
            ps_segment = uianim_segment.props
            # */

            b_segments.sep(1)
            b_segments.prop_flag("segment_mode")
            ps_segment["segment_mode"].r_button_width = self.r_button_width_200
            b_segments.sep(2)
            b_segments.prop("segment_start")
            b_segments.join_prop("segment_end", text="End")
            b_segments.join_prop("segment_repeat", text="Repeat")

            self.items[:] = [b0.w, b_segments.w, b1.w, b_influence.w]

            def fn_darklight(md):
                if ui_state == [ui_anim_data.library_state, md.use_layer_pass_filter]: return
                ui_state[:] = [ui_anim_data.library_state, md.use_layer_pass_filter]

                if ui_anim_data.library_state == 1: return

                b1.w.dark()

                if md.use_layer_pass_filter:
                    props["invert_layer_pass_filter"].light()
                    props["layer_pass_filter"].light()
                else:
                    props["invert_layer_pass_filter"].dark()
                    props["layer_pass_filter"].dark()

            def upd_data_callback():
                if self.w.active_modifier.mode == "CHAIN": pass
                else:
                    self.init_tab(self.active_tab, push=False, evtkill=False)
                    return

                ui_anim_data.update_with(fn_darklight)
                uianim_segment.update_with(N1)
                blocklis_segments.upd_data()
                blocklis_segments_media.upd_data()
        else:
            def fn_darklight(md):
                if ui_state == [ui_anim_data.library_state, md.mode, md.use_custom_frame_range, md.use_layer_pass_filter]: return
                ui_state[:] = [ui_anim_data.library_state, md.mode, md.use_custom_frame_range, md.use_layer_pass_filter]

                if ui_anim_data.library_state == 1: return

                if md.mode == "FIX":
                    props["frame_scale"].dark()
                    props["use_keep_loop"].dark()
                    props["use_custom_frame_range"].dark()
                    props["frame_start"].dark()
                    props["frame_end"].dark()
                else:
                    props["frame_scale"].light()
                    props["use_keep_loop"].light()
                    props["use_custom_frame_range"].light()

                    if md.use_custom_frame_range:
                        props["frame_start"].light()
                        props["frame_end"].light()
                    else:
                        props["frame_start"].dark()
                        props["frame_end"].dark()

                if md.use_layer_pass_filter:
                    props["invert_layer_pass_filter"].light()
                    props["layer_pass_filter"].light()
                else:
                    props["invert_layer_pass_filter"].dark()
                    props["layer_pass_filter"].dark()

            def upd_data_callback():
                if self.w.active_modifier.mode == "CHAIN":
                    self.init_tab(self.active_tab, push=False, evtkill=False)
                    return

                ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_inv_vg("use_invert_output", "target_vertex_group", self.r_object_vertex_groups)
        b0.prop("object", options={"ID":"OBJECT"})
        b0.sep(2)
        b0.prop("distance_start")
        b0.join_prop("distance_end")
        b0.sep(2)
        b0.prop("minimum_weight")
        b0.prop("use_multiply")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.target_vertex_group, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.target_vertex_group, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.target_vertex_group:
                props["use_invert_output"].light()
            else:
                props["use_invert_output"].dark()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_VERTEX_WEIGHT_ANGLE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_inv_vg("use_invert_output", "target_vertex_group", self.r_object_vertex_groups)
        b0.prop("angle")
        b0.prop_flag("axis")
        b0.prop_flag("space")
        props["space"].blf_value[0].text = "Local"
        props["space"].blf_value[1].text = "World"
        b0.prop("minimum_weight")
        b0.prop("use_multiply")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.target_vertex_group, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.target_vertex_group, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.target_vertex_group:
                props["use_invert_output"].light()
            else:
                props["use_invert_output"].dark()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_ARRAY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("count")
        b0.prop("replace_material", text="Material Override")

        b1 = ui.new_block(title=ui.r_prop("use_relative_offset", text="Relative Offset", options={"HEAD"}))
        b1.prop("relative_offset", text="Factor")

        b2 = ui.new_block(title=ui.r_prop("use_constant_offset", text="Constant Offset", options={"HEAD"}))
        b2.prop("constant_offset", text="Distance")

        b3 = ui.new_block(title=ui.r_prop("use_object_offset", text="Object Offset", options={"HEAD"}))
        b3.prop("offset_object", text="Object", options={"ID":"OBJECT"})

        b4 = ui.new_block(title="Randomize")
        b4.prop("random_offset", text="Offset")
        b4.prop("random_rotation", text="Rotation")
        b4.prop("random_scale")
        b4.prop("use_uniform_random_scale")
        b4.prop("seed")

        # /* 0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # */

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_relative_offset, md.use_constant_offset, md.use_object_offset, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_relative_offset, md.use_constant_offset, md.use_object_offset, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.use_relative_offset:
                props["relative_offset"].light()
            else:
                props["relative_offset"].dark()

            if md.use_constant_offset:
                props["constant_offset"].light()
            else:
                props["constant_offset"].dark()

            if md.use_object_offset:
                props["offset_object"].light()
            else:
                props["offset_object"].dark()

            # /* 0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # */

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_BUILD(self):

        def set_callback_time_mode():
            active_modifier = self.w.active_modifier
            if active_modifier.mode == "CONCURRENT" and active_modifier.time_mode == "DRAWSPEED":
                active_modifier.time_mode = "FRAMES"
                report("Concurrent unsupport Natual Drawing Speed")

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        props["mode"].r_button_width = self.r_button_width_166
        b0.prop_flag("transition")
        props["transition"].r_button_width = self.r_button_width_166
        b0.sep(2)
        b0.prop("time_mode")
        props["time_mode"].r_button_width = self.r_button_width_166
        props["time_mode"].set_callback = set_callback_time_mode
        b0.prop_flag("concurrent_time_alignment")
        props["concurrent_time_alignment"].blf_value[0].text = "Start"
        props["concurrent_time_alignment"].blf_value[1].text = "End"
        b0.prop("length", text="Frames")
        b0.prop("start_delay")
        b0.prop("speed_factor")
        b0.prop("speed_maxgap")
        b0.prop("percentage_factor")
        b0.sep(2)
        b0.prop("object", options={"ID":"OBJECT"})

        b1 = ui.new_block(title=ui.r_prop("use_restrict_frame_range", text="Effective Range", options={"HEAD"}))
        b1.prop("frame_start", text="Start")
        b1.join_prop("frame_end", text="End")

        b2 = ui.new_block(title=ui.r_prop("use_fading", text="Fading", options={"HEAD"}))
        b2.prop("fade_factor", text="Factor")
        b2.join_prop("fade_thickness_strength", text="Thickness")
        b2.join_prop("fade_opacity_strength", text="Opacity")
        b2.prop_search("target_vertex_group", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Weight Output")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.mode, md.time_mode, md.use_restrict_frame_range, md.use_fading, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.mode, md.time_mode, md.use_restrict_frame_range, md.use_fading, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.mode == "SEQUENTIAL":
                use_delay = True
                props["transition"].light()
                props["concurrent_time_alignment"].dark()
            elif md.mode == "CONCURRENT":
                use_delay = True
                props["transition"].light()
                props["concurrent_time_alignment"].light()
            else:
                use_delay = False
                props["transition"].dark()
                props["concurrent_time_alignment"].dark()

            if md.time_mode == "DRAWSPEED":
                props["speed_factor"].light()
                props["speed_maxgap"].light()
                props["length"].dark()
                props["start_delay"].dark()
                props["percentage_factor"].dark()
            elif md.time_mode == "FRAMES":
                props["speed_factor"].dark()
                props["speed_maxgap"].dark()
                props["length"].light()
                if use_delay is True:
                    props["start_delay"].light()
                else:
                    props["start_delay"].dark()
                props["percentage_factor"].dark()
            else:
                props["speed_factor"].dark()
                props["speed_maxgap"].dark()
                props["length"].dark()
                props["start_delay"].dark()
                props["percentage_factor"].light()

            if md.use_restrict_frame_range:
                props["frame_start"].light()
                props["frame_end"].light()
            else:
                props["frame_start"].dark()
                props["frame_end"].dark()

            if md.use_fading:
                b2.w.light(use_head=False)
            else:
                b2.w.dark(use_head=False)

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_DASH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("dash_offset")

        modifier_type = "GREASE_PENCIL_DASH"
        # <<< 1copy (0areas_gp_segment_fns,, ${'GreasePencilTimeModifierSegment':'GreasePencilDashModifierSegment'}$)
        def r_segments():
            if hasattr(self.w.active_modifier, "segments"):
                return self.w.active_modifier.segments
            return None
        def r_segment():
            active_modifier = self.w.active_modifier
            i = active_modifier.segment_active_index
            if i < len(active_modifier.segments):
                return active_modifier.segments[i]
            return None
        def r_dph_segment():
            active_modifier = self.w.active_modifier
            i = active_modifier.segment_active_index
            if i < len(active_modifier.segments):
                return f'modifiers["{escape_identifier(self.w.active_modifier_name)}"].segments["{escape_identifier(active_modifier.segments[i].name)}"]'
            return ''
        def bufn_add_segments():
            modifier = self.w.active_modifier
            with bpy.context.temp_override(object=self.r_object()):
                if modifier_type == "GREASE_PENCIL_TIME":
                    bpy.ops.object.grease_pencil_time_modifier_segment_add(modifier=modifier.name)
                elif modifier_type == "GREASE_PENCIL_DASH":
                    bpy.ops.object.grease_pencil_dash_modifier_segment_add(modifier=modifier.name)
                else:
                    return
        def bufn_remove_segments():
            modifier = self.w.active_modifier
            with bpy.context.temp_override(object=self.r_object()):
                if modifier.type == "GREASE_PENCIL_TIME":
                    bpy.ops.object.grease_pencil_time_modifier_segment_remove(modifier=modifier.name)
                elif modifier.type == "GREASE_PENCIL_DASH":
                    bpy.ops.object.grease_pencil_dash_modifier_segment_remove(modifier=modifier.name)
                else:
                    return

        b_segments = ui.new_block(title="Segments")
        blocklis_segments = BlocklistAZ(b_segments.w,
            r_pp = r_segments,
            r_object = self.r_object,
            r_datapath_head = self.rr_dph(".segments"),
            remove_active_item = bufn_remove_segments,
            add_item = bufn_add_segments)
        blocklis_segments.r_active_index = lambda: self.w.active_modifier.segment_active_index
        blocklis_segments.set_active_index = lambda x: setattr(self.w.active_modifier, "segment_active_index", x)
        blocklis_segments_media = BlockMediaAZ(b_segments.w, blocklis_segments)
        b_segments.items += [blocklis_segments, blocklis_segments_media]
        uianim_segment = b_segments.set_pp(r_segment, bpytypes.GreasePencilDashModifierSegment, r_dph_segment)
        ps_segment = uianim_segment.props
        # >>>
        b_segments.sep(1)
        b_segments.prop("dash")
        b_segments.join_prop("gap")
        b_segments.sep(1)
        b_segments.prop("radius")
        b_segments.join_prop("opacity")
        b_segments.sep(1)
        b_segments.prop("material_index")
        b_segments.prop("use_cyclic")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)
            uianim_segment.update_with(N1)
            blocklis_segments.upd_data()
            blocklis_segments_media.upd_data()

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_ENVELOPE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        props["mode"].r_button_width = self.r_button_width_150
        b0.sep(2)
        b0.prop("spread")
        b0.prop("thickness")
        b0.prop("strength")
        b0.prop("mat_nr")
        b0.prop("skip")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.mode == "DEFORM":
                props["strength"].dark()
                props["mat_nr"].dark()
                props["skip"].dark()
            else:
                props["strength"].light()
                props["mat_nr"].light()
                props["skip"].light()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_LENGTH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        b0.sep(1)
        b0.prop("start_factor")
        b0.join_prop("end_factor", text="End")
        b0.sep(1)
        b0.prop("start_length", text="Start Length")
        b0.join_prop("end_length", text="End")
        b0.sep(1)
        b0.prop("overshoot_factor")

        b1 = ui.new_block(title=ui.r_prop("use_random", text="Randomize", options={"HEAD"}))
        b1.prop("step")
        b1.prop("random_start_factor", text="Offset Start")
        b1.prop("random_end_factor", text="End")
        b1.prop("random_offset", text="Noise Offset")
        b1.prop("seed")

        b2 = ui.new_block(title=ui.r_prop("use_curvature", text="Curvature", options={"HEAD"}))
        b2.prop("point_density")
        b2.prop("segment_influence")
        b2.prop("max_angle")
        b2.prop("invert_curvature", text="Invert")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_random, md.use_curvature, md.mode, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_random, md.use_curvature, md.mode, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.use_random:
                b1.w.light(use_head=False)
            else:
                b1.w.dark(use_head=False)

            if md.use_curvature:
                b2.w.light(use_head=False)
            else:
                b2.w.dark(use_head=False)

            if md.mode == "RELATIVE":
                props["start_factor"].light()
                props["end_factor"].light()
                props["start_length"].dark()
                props["end_length"].dark()
            else:
                props["start_factor"].dark()
                props["end_factor"].dark()
                props["start_length"].light()
                props["end_length"].light()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_MIRROR(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag(["use_axis_x", "use_axis_y", "use_axis_z"], text="Axis", options={"NAMES": "XYZ"})
        b0.prop("object", options={"ID":"OBJECT"})

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_MULTIPLY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("duplicates")
        b0.prop("distance")
        b0.prop("offset")

        b1 = ui.new_block(title=ui.r_prop("use_fade", text="Fade", options={"HEAD"}))
        b1.prop("fading_center")
        b1.join_prop("fading_thickness")
        b1.join_prop("fading_opacity")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_fade, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_fade, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.use_fade:
                b1.w.light(use_head=False)
            else:
                b1.w.dark(use_head=False)

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_OUTLINE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("thickness")
        b0.prop("use_keep_shape")
        b0.prop("subdivision")
        b0.prop("sample_length")
        b0.sep(2)
        b0.prop("outline_material", options={"ID":"MATERIAL"})
        b0.prop("object", options={"ID":"OBJECT"})
        label0 = b0.label([""])

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, (True  if bpy.context.scene.camera else False), md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, (True  if bpy.context.scene.camera else False), md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if bpy.context.scene.camera:
                label0.blf_label[0].text = ""
            else:
                label0.blf_label[0].text = "⚠ Outline requires an active camera"

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_SIMPLIFY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("mode")
        props["mode"].r_button_width = self.r_button_width_200
        b0.sep(2)
        b0.prop("step")
        b0.prop("factor")
        b0.prop("length")
        b0.prop("sharp_threshold")
        b0.prop("distance")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.mode]: return
            ui_state[:] = [ui_anim_data.library_state, md.mode]

            if ui_anim_data.library_state == 1: return

            if md.mode == "FIXED":
                props["step"].light()
                props["factor"].dark()
                props["length"].dark()
                props["sharp_threshold"].dark()
                props["distance"].dark()
            elif md.mode == "ADAPTIVE":
                props["step"].dark()
                props["factor"].light()
                props["length"].dark()
                props["sharp_threshold"].dark()
                props["distance"].dark()
            elif md.mode == "SAMPLE":
                props["step"].dark()
                props["factor"].dark()
                props["length"].light()
                props["sharp_threshold"].light()
                props["distance"].dark()
            else:
                props["step"].dark()
                props["factor"].dark()
                props["length"].dark()
                props["sharp_threshold"].dark()
                props["distance"].light()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_SUBDIV(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("subdivision_type", text="Type")
        props["subdivision_type"].r_button_width = self.r_button_width_133
        b0.sep(1)
        b0.prop("level", text="Subdivisions")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_LINEART(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props
        button_search = b0.r_function(RNA_search, None, isdarkhard=True,
            options={"icon_cls": GpuImg_search, "icon_cls_dark": GpuImgNull})
        search_data = self.search_data
        search_data.init_with(button_search)

        o_use_cache = b0.r_prop("use_cache", isdarkhard=True)
        b0.items.append(ButtonOverlay(o_use_cache.w, button_search, o_use_cache))
        b0.sep(1)
        b0.prop_flag("source_type")
        props["source_type"].r_button_width = self.r_button_width_150
        b0.prop_inv("use_invert_collection", "source_collection", options={"ID":"COLLECTION"})
        b0.prop("source_object", options={"ID":"OBJECT"})
        b0.prop_search("target_layer", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        b0.prop("target_material", options={"ID":"MATERIAL"})
        b0.sep(1)
        b0.prop("thickness", text="Line Thickness")
        b0.prop("opacity")

        b1 = ui.new_block(title="Edge Types")
        b1.prop("shadow_region_filtering", text="Illumination Filtering")
        props["shadow_region_filtering"].r_button_width = self.r_button_width_133
        b1.sep(1)
        b1.prop("silhouette_filtering", text="")
        b1.join_bool("use_contour", text="Create")
        b1.prop("use_invert_silhouette", text="Invert", options={"icon_cls": GpuImg_invert})
        b1.sep(1)
        b1.prop("crease_threshold", text="")
        b1.join_bool("use_crease", text="Crease Threshold")
        b1.sep(1)
        r_button_width_join_bool = self.r_button_width_join_bool
        b1.prop("use_intersection", text="Intersections")
        props["use_intersection"].r_button_width = r_button_width_join_bool
        b1.prop("use_material", text="Material Borders")
        props["use_material"].r_button_width = r_button_width_join_bool
        b1.prop("use_edge_mark", text="Edge Marks")
        props["use_edge_mark"].r_button_width = r_button_width_join_bool
        b1.prop("use_loose", text="Loose")
        props["use_loose"].r_button_width = r_button_width_join_bool
        b1.prop("use_light_contour", text="Light Contour")
        props["use_light_contour"].r_button_width = r_button_width_join_bool
        b1.prop("use_shadow", text="Cast Shadow")
        props["use_shadow"].r_button_width = r_button_width_join_bool
        label1 = b1.label(["Options"])
        b1.prop("use_overlap_edge_type_support", text="Allow Overlapping Types")
        props["use_overlap_edge_type_support"].r_button_width = r_button_width_join_bool

        b2 = ui.new_block(title=ui.r_label([""], align="R1"))
        b2.w.blf_title.text = "Light Reference"
        b2.w.button0.blf_label[0].color = COL_block_fg_info
        b2.prop("light_contour_object", options={"ID":"OBJECT"})
        b2.sep(1)
        b2.prop("shadow_camera_size")
        props["shadow_camera_size"].set_callback = update_scene_and_ref
        b2.sep(1)
        b2.prop("shadow_camera_near", text="Near")
        b2.join_prop("shadow_camera_far", text="Far")

        b3 = ui.new_block(title=ui.r_label([""], align="R1"))
        b3.w.blf_title.text = "Geometry Processing"
        b3.w.button0.blf_label[0].color = COL_block_fg_info
        b3.prop("source_camera", text="", options={"ID":"OBJECT"})
        b3.join_bool("use_custom_camera", text="Custom Camera")
        b3.sep(1)
        b3.prop("use_edge_overlap", text="Overlap Edges As Contour")
        props["use_edge_overlap"].r_button_width = r_button_width_join_bool
        b3.prop("use_object_instances")
        props["use_object_instances"].r_button_width = r_button_width_join_bool
        b3.prop("use_clip_plane_boundaries")
        props["use_clip_plane_boundaries"].r_button_width = r_button_width_join_bool
        b3.prop("use_crease_on_smooth")
        props["use_crease_on_smooth"].r_button_width = r_button_width_join_bool
        b3.prop("use_crease_on_sharp")
        props["use_crease_on_sharp"].r_button_width = r_button_width_join_bool
        b3.prop("use_back_face_culling", text="Force Backface Culling")
        props["use_back_face_culling"].r_button_width = r_button_width_join_bool

        b4 = ui.new_block(title="Occlusion")
        uianim_object = b4.set_pp_id_data(self.r_object)
        b4.prop("show_in_front", text=("Object", "Show in Front"))
        uianim_object.props["show_in_front"].set_callback = update_scene_and_ref
        b4.set_pp_from(ui_anim_data)
        b4.prop("use_multiple_levels", text="Range")
        b4.prop("level_start")
        b4.join_prop("level_end", text="End")
        b4.sep(1)
        b4_0 = b4.new_block(title=b4.r_prop("use_material_mask", options={"HEAD"}))
        b4_0.prop("use_material_mask_bits", text="Material Mask", isdarkhard=True, options={"NAMES": "01234567", "ROW_LENGTH": 4})
        b4_0.prop("use_material_mask_match", text="Exact Match", isdarkhard=True)

        b5 = ui.new_block(title="Intersection")
        b5.prop("use_intersection_mask", text="Collection Masks", options={"NAMES": "01234567", "ROW_LENGTH": 4})
        b5.prop("use_intersection_match", text="Exact Match")

        o_use_face_mark = ui.r_prop("use_face_mark", text="Face Mark Filtering", options={"HEAD"})
        b6 = ui.new_block(title=ButtonOverlay(None, o_use_face_mark, ui.r_label([""], align="R1")))
        b6.w.button0.button1.blf_label[0].color = COL_block_fg_info
        b6.prop("use_face_mark_invert", text="Invert")
        b6.prop("use_face_mark_boundaries")
        b6.prop("use_face_mark_keep_contour")

        b7 = ui.new_block(title=ui.r_label([""], align="R1"))
        b7.w.blf_title.text = "Chaining"
        b7.w.button0.blf_label[0].color = COL_block_fg_info
        b7.prop("use_fuzzy_intersections", text=("Chain", None))
        props["use_fuzzy_intersections"].r_button_width = r_button_width_join_bool
        b7.prop("use_fuzzy_all")
        props["use_fuzzy_all"].r_button_width = r_button_width_join_bool
        b7.prop("use_loose_edge_chain", text="Loose Edges")
        props["use_loose_edge_chain"].r_button_width = r_button_width_join_bool
        b7.prop("use_loose_as_contour", text="Loose Edges As Contour")
        props["use_loose_as_contour"].r_button_width = r_button_width_join_bool
        b7.prop("use_detail_preserve")
        props["use_detail_preserve"].r_button_width = r_button_width_join_bool
        b7.prop("use_geometry_space_chain", text="Geometry Space")
        props["use_geometry_space_chain"].r_button_width = r_button_width_join_bool
        b7.sep(1)
        b7.prop("chaining_image_threshold")
        props["chaining_image_threshold"].r_button_width = r_button_width_join_bool
        b7.prop("smooth_tolerance")
        props["smooth_tolerance"].r_button_width = r_button_width_join_bool
        b7.prop("split_angle")
        props["split_angle"].r_button_width = r_button_width_join_bool

        b8 = ui.new_block(title=ui.r_label([""], align="R1"))
        b8.w.blf_title.text = "Vertex Weight Transfer"
        b8.w.button0.blf_label[0].color = COL_block_fg_info
        b8.prop_inv_vg("invert_source_vertex_group", "source_vertex_group", self.r_object_vertex_groups, text="Filter Source")
        props["source_vertex_group"].r_button_width = r_button_width_join_bool
        b8.prop("use_output_vertex_group_match_by_name")
        props["use_output_vertex_group_match_by_name"].r_button_width = r_button_width_join_bool
        b8.prop_search("vertex_group", GpuImg_GROUP_VERTEX, self.r_object_vertex_groups, text="Target")
        props["vertex_group"].r_button_width = r_button_width_join_bool

        b9 = ui.new_block(title="Composition")
        b9.prop("overscan")
        props["overscan"].r_button_width = r_button_width_join_bool
        b9.prop("use_image_boundary_trimming")
        props["use_image_boundary_trimming"].r_button_width = r_button_width_join_bool
        props["use_image_boundary_trimming"].set_callback = update_scene_and_ref
        b9.prop("stroke_depth_offset", text="Depth Offset")
        props["stroke_depth_offset"].r_button_width = r_button_width_join_bool
        b9.prop("use_offset_towards_custom_camera", text="Towards Custom Camera")
        props["use_offset_towards_custom_camera"].r_button_width = r_button_width_join_bool

        b10 = ui.new_block(title="Bake")
        o_bake_clear = b10.function([RNA_LINEART_BAKE, RNA_LINEART_CLEAR], [self.bufn_LINEART_bake, self.bufn_LINEART_clear], isdarkhard=True)
        o_bake_clear_all = b10.function([RNA_LINEART_BAKE_ALL, RNA_LINEART_CLEAR_ALL], [self.bufn_LINEART_bake_all, self.bufn_LINEART_clear_all], isdarkhard=True)
        o_continue = b10.function(RNA_LINEART_CONTINUE, self.bufn_LINEART_continue, isdarkhard=True)
        o_continue.r_button_width = self.r_button_width_201

        darkhards = {e: e.isdarkhard  for e in props.values()}

        ui_state = []

        def fn_darklight(md):
            is_first_lineart_in_stack = (next(e  for e in self.w.active_object.modifiers  if e.type == "LINEART") == md)

            if ui_state == [ui_anim_data.library_state, is_first_lineart_in_stack, md.is_baked, md.use_cache, md.source_type, (True  if md.light_contour_object else False), md.use_contour, md.use_custom_camera, md.use_face_mark, self.w.active_object.show_in_front, md.use_multiple_levels, md.level_end, md.use_material_mask, md.level_start, md.use_intersection]: return
            ui_state[:] = [ui_anim_data.library_state, is_first_lineart_in_stack, md.is_baked, md.use_cache, md.source_type, (True  if md.light_contour_object else False), md.use_contour, md.use_custom_camera, md.use_face_mark, self.w.active_object.show_in_front, md.use_multiple_levels, md.level_end, md.use_material_mask, md.level_start, md.use_intersection]

            if ui_anim_data.library_state == 1: return

            if md.is_baked:
                if props["opacity"].isdark is False:
                    o_use_cache.dark()
                    props["source_type"].dark()
                    props["use_invert_collection"].dark()
                    props["source_collection"].dark()
                    props["source_object"].dark()
                    props["target_layer"].dark()
                    props["target_material"].dark()
                    props["thickness"].dark()
                    props["opacity"].dark()
                    o_use_face_mark.dark()

                    b1.w.dark(use_head=False)
                    b2.w.dark(use_head=False)
                    b3.w.dark(use_head=False)
                    b4.w.dark(use_head=False)
                    uianim_object.props["show_in_front"].light()
                    b5.w.dark(use_head=False)
                    b6.w.dark(use_head=False)
                    b7.w.dark(use_head=False)
                    b8.w.dark(use_head=False)

                    for e in props.values():
                        e.isdarkhard = True

                o_continue.light()
                o_bake_clear.dark(0)
                o_bake_clear_all.dark(0)

                if is_first_lineart_in_stack is True:
                    use_cache = False
                else:
                    use_cache = md.use_cache

                if use_cache:
                    if not label1.blf_label[0].text.endswith(")"):
                        label1.blf_label[0].text = "Options  (Type overlapping cached)"
                        s = "Cached"  if is_first_lineart_in_stack else "Cached from first Line Art"

                        b2.w.button0.set_text_with(s)
                        b3.w.button0.set_text(s)
                        b6.w.button0.button1.set_text(s)
                        b7.w.button0.set_text(s)
                        b8.w.button0.set_text(s)
                else:
                    if not label1.blf_label[0].text.endswith("s"):
                        label1.blf_label[0].text = "Options"
                        b2.w.button0.set_text_with("")
                        b3.w.button0.set_text("")
                        b6.w.button0.button1.set_text("")
                        b7.w.button0.set_text("")
                        b8.w.button0.set_text("")

                if self.w.active_object.show_in_front:
                    props["stroke_depth_offset"].dark()
                    props["use_offset_towards_custom_camera"].dark()
                else:
                    props["stroke_depth_offset"].light()
                    props["use_offset_towards_custom_camera"].light()
                return

            if props["opacity"].isdark is True:
                o_use_cache.light()
                props["source_type"].light()
                props["use_invert_collection"].light()
                props["source_collection"].light()
                props["source_object"].light()
                props["target_layer"].light()
                props["target_material"].light()
                props["thickness"].light()
                props["opacity"].light()
                o_use_face_mark.light()

                b1.w.light(use_head=False)
                b2.w.light(use_head=False)
                b3.w.light(use_head=False)
                b4.w.light(use_head=False)
                b5.w.light(use_head=False)
                b6.w.light(use_head=False)
                b7.w.light(use_head=False)
                b8.w.light(use_head=False)

                for e, v in darkhards.items():
                    e.isdarkhard = v

            o_continue.dark()
            o_bake_clear.light(0)
            o_bake_clear_all.light(0)

            if is_first_lineart_in_stack is True:
                o_use_cache.dark()

                use_cache = False
            else:
                o_use_cache.light()

                use_cache = md.use_cache

            if md.source_type == "OBJECT":
                props["source_object"].light()
                props["source_collection"].dark()
                props["use_invert_collection"].dark()
            elif md.source_type == "COLLECTION":
                props["source_object"].dark()
                props["source_collection"].light()
                props["use_invert_collection"].light()
            else:
                props["source_object"].dark()
                props["source_collection"].dark()
                props["use_invert_collection"].dark()

            if md.light_contour_object:
                props["shadow_region_filtering"].light()
                props["use_light_contour"].light()
                props["use_shadow"].light()
                props["shadow_camera_size"].light()
                props["shadow_camera_near"].light()
                props["shadow_camera_far"].light()
            else:
                props["shadow_region_filtering"].dark()
                props["use_light_contour"].dark()
                props["use_shadow"].dark()
                props["shadow_camera_size"].dark()
                props["shadow_camera_near"].dark()
                props["shadow_camera_far"].dark()

            if md.use_contour:
                props["silhouette_filtering"].light()
            else:
                props["silhouette_filtering"].dark()

            if use_cache:
                if props["crease_threshold"].isdark is False:
                    props["crease_threshold"].dark()
                    props["use_overlap_edge_type_support"].dark()
                    props["light_contour_object"].dark()
                    b3.w.dark(use_head=False)
                    b6.w.dark(use_head=False)
                    o_use_face_mark.dark()
                    b7.w.dark(use_head=False)
                    b8.w.dark(use_head=False)

                if not label1.blf_label[0].text.endswith(")"):
                    label1.blf_label[0].text = "Options  (Type overlapping cached)"
                    s = "Cached"  if is_first_lineart_in_stack else "Cached from first Line Art"

                    b2.w.button0.set_text_with(s)
                    b3.w.button0.set_text(s)
                    b6.w.button0.button1.set_text(s)
                    b7.w.button0.set_text(s)
                    b8.w.button0.set_text(s)

                props["shadow_camera_size"].dark()
                props["shadow_camera_near"].dark()
                props["shadow_camera_far"].dark()
                props["source_camera"].dark()
            else:
                if props["crease_threshold"].isdark is True:
                    props["crease_threshold"].light()
                    props["use_overlap_edge_type_support"].light()
                    props["light_contour_object"].light()
                    b3.w.light(use_head=False)
                    b6.w.light(use_head=False)
                    o_use_face_mark.light()
                    b7.w.light(use_head=False)
                    b8.w.light(use_head=False)

                if not label1.blf_label[0].text.endswith("s"):
                    label1.blf_label[0].text = "Options"
                    b2.w.button0.set_text_with("")
                    b3.w.button0.set_text("")
                    b6.w.button0.button1.set_text("")
                    b7.w.button0.set_text("")
                    b8.w.button0.set_text("")

                if md.use_custom_camera:
                    props["source_camera"].light()
                else:
                    props["source_camera"].dark()

                if md.use_face_mark:
                    props["use_face_mark_invert"].light()
                    props["use_face_mark_boundaries"].light()
                    props["use_face_mark_keep_contour"].light()
                else:
                    props["use_face_mark_invert"].dark()
                    props["use_face_mark_boundaries"].dark()
                    props["use_face_mark_keep_contour"].dark()

            if self.w.active_object.show_in_front:
                props["use_multiple_levels"].light()
                props["level_start"].light()
                props["stroke_depth_offset"].dark()
                props["use_offset_towards_custom_camera"].dark()

                if md.use_multiple_levels:
                    props["level_end"].light()

                    if md.level_end == 0:
                        props["use_material_mask"].dark()
                        props["use_material_mask_bits"].dark()
                        props["use_material_mask_match"].dark()
                    else:
                        props["use_material_mask"].light()
                        if md.use_material_mask:
                            props["use_material_mask_bits"].light()
                            props["use_material_mask_match"].light()
                        else:
                            props["use_material_mask_bits"].dark()
                            props["use_material_mask_match"].dark()
                else:
                    props["level_end"].dark()

                    if md.level_start == 0:
                        props["use_material_mask"].dark()
                        props["use_material_mask_bits"].dark()
                        props["use_material_mask_match"].dark()
                    else:
                        props["use_material_mask"].light()

                        if md.use_material_mask:
                            props["use_material_mask_bits"].light()
                            props["use_material_mask_match"].light()
                        else:
                            props["use_material_mask_bits"].dark()
                            props["use_material_mask_match"].dark()
            else:
                props["use_multiple_levels"].dark()
                props["level_start"].dark()
                props["level_end"].dark()
                b4_0.w.dark(use_head=False)
                props["stroke_depth_offset"].light()
                props["use_offset_towards_custom_camera"].light()

            if md.use_intersection:
                b5.w.light(use_head=False)
            else:
                b5.w.dark(use_head=False)

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)
            uianim_object.update_with(N1)

        button_search.fn = self.r_bufn_search(upd_data_callback, [
                ui_anim_data,
                uianim_object,
            ],
            extra_buttons = [o_bake_clear, o_bake_clear_all, o_continue],
            search_data = search_data)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_ARMATURE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT", "TYPES":{"ARMATURE"}})
        b0.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        b0.sep(2)
        b0.prop("use_vertex_groups", text=("Bind To", "Vertex Groups"))
        b0.prop("use_bone_envelopes")

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group_name]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group_name]

            if ui_anim_data.library_state == 1: return

            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_HOOK(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT"})
        b0.prop_search("subtarget", GpuImg_BONE_DATA, self.rr_bones(lambda: self.r_modifier().object), text="Bone")
        b0.prop("strength")

        b1 = ui.new_block(title=ui.r_prop("falloff_type", text="", options={"D_icon": D_geticon_falloff}))
        b1.w.blf_title.text = "Falloff"
        b1.prop("falloff_radius")
        b1.prop("use_falloff_uniform")
        o_edit_curve = b1.function(RNA_edit_curve, self.bufn_GREASE_PENCIL_HOOK_edit_curve)

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            # <<< 1copy (0defstate_bone_name,, ${'__obj_attr__':'object'}$)
            if md.object:
                name_object = md.object.name
                state_object = 0  if md.object.type == "ARMATURE" else 1
            else:
                name_object = ""
                state_object = 2
            # >>>

            if ui_state == [ui_anim_data.library_state, state_object, name_object, md.falloff_type, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, state_object, name_object, md.falloff_type, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if state_object == 0:
                props["subtarget"].light()
            else:
                props["subtarget"].dark()

            if md.falloff_type == "CURVE":
                o_edit_curve.light()
                props["falloff_radius"].light()
            else:
                o_edit_curve.dark()

                if md.falloff_type == "NONE":
                    props["falloff_radius"].dark()
                else:
                    props["falloff_radius"].light()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_LATTICE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("object", options={"ID":"OBJECT", "TYPES":{"LATTICE"}})
        b0.prop("strength")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_NOISE(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("factor", text="Position")
        b0.prop("factor_strength", text="Strength")
        b0.prop("factor_thickness", text="Thickness")
        b0.prop("factor_uvs", text="UV")
        b0.prop("noise_scale")
        b0.prop("noise_offset")
        b0.prop("seed")

        b1 = ui.new_block(ui.r_prop("use_random", text="Randomize", options={"HEAD"}))
        b1.prop_flag("random_mode")
        props["random_mode"].set_callback = update_scene_and_ref
        b1.prop("step")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>
        b_influence.sep(2)
        b_influence.prop("use_custom_curve", text="Custom Curve")
        o_edit_curve = b_influence.function(RNA_edit_curve, self.bufn_GREASE_PENCIL_HOOK_edit_curve)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_random, md.random_mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_random, md.random_mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if md.use_random:
                props["random_mode"].light()

                if md.random_mode == "STEP":
                    props["step"].light()
                else:
                    props["step"].dark()
            else:
                props["random_mode"].dark()
                props["step"].dark()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

            if md.use_custom_curve:
                o_edit_curve.light()
            else:
                o_edit_curve.dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_OFFSET(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("location")
        b0.sep(0)
        b0.prop("rotation")
        b0.sep(0)
        b0.prop("scale")

        b1 = ui.new_block(title="Advanced")
        b1.prop_flag("offset_mode")
        props["offset_mode"].r_button_width = self.r_button_width_200
        b1.sep(0)
        b1.prop("stroke_location", text="Location")
        b1.sep(0)
        b1.prop("stroke_rotation", text="Rotation")
        b1.sep(0)
        b1.prop("stroke_scale", text="Scale")
        b1.prop("use_uniform_random_scale")
        b1.prop("seed")
        b1.prop("stroke_step")
        b1.prop("stroke_start_offset")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.offset_mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.offset_mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.offset_mode == "RANDOM":
                props["use_uniform_random_scale"].light()
                props["seed"].light()
                props["stroke_step"].dark()
                props["stroke_start_offset"].dark()
            else:
                props["use_uniform_random_scale"].dark()
                props["seed"].dark()
                props["stroke_step"].light()
                props["stroke_start_offset"].light()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_SHRINKWRAP(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("wrap_method")
        props["wrap_method"].set_align("FULL")
        b0.sep(2)
        b0.prop("wrap_mode")
        b0.prop("target", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b0.prop("auxiliary_target", options={"ID":"OBJECT", "TYPES":{"MESH"}})
        b0.prop("offset")
        b0.prop("smooth_factor")
        b0.prop("smooth_step")
        b0.prop("project_limit")
        b0.prop("subsurf_levels")
        b0.prop_flag(["use_project_x", "use_project_y", "use_project_z"], text="Axis", options={"NAMES": "XYZ"})
        b0.prop("use_negative_direction")
        b0.prop("use_positive_direction")
        b0.prop_flag("cull_face")
        b0.prop("use_invert_cull")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.wrap_method, md.use_negative_direction, md.cull_face, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.wrap_method, md.use_negative_direction, md.cull_face, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.wrap_method == "NEAREST_SURFACEPOINT":
                props["wrap_mode"].light()
                props["project_limit"].dark()
                props["subsurf_levels"].dark()
                props["use_project_x"].dark()
                props["use_negative_direction"].dark()
                props["use_positive_direction"].dark()
                props["cull_face"].dark()
                props["auxiliary_target"].dark()
                props["use_invert_cull"].dark()
            elif md.wrap_method == "PROJECT":
                props["wrap_mode"].light()
                props["project_limit"].light()
                props["subsurf_levels"].light()
                props["use_project_x"].light()
                props["use_negative_direction"].light()
                props["use_positive_direction"].light()
                props["cull_face"].light()
                props["auxiliary_target"].light()
                if md.use_negative_direction and md.cull_face in {"FRONT", "BACK"}:
                    props["use_invert_cull"].light()
                else:
                    props["use_invert_cull"].dark()
            elif md.wrap_method == "NEAREST_VERTEX":
                props["wrap_mode"].dark()
                props["project_limit"].dark()
                props["subsurf_levels"].dark()
                props["use_project_x"].dark()
                props["use_negative_direction"].dark()
                props["use_positive_direction"].dark()
                props["cull_face"].dark()
                props["auxiliary_target"].dark()
                props["use_invert_cull"].dark()
            else:
                props["wrap_mode"].light()
                props["project_limit"].dark()
                props["subsurf_levels"].dark()
                props["use_project_x"].dark()
                props["use_negative_direction"].dark()
                props["use_positive_direction"].dark()
                props["cull_face"].dark()
                props["auxiliary_target"].dark()
                props["use_invert_cull"].dark()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_SMOOTH(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag(["use_edit_position", "use_edit_strength", "use_edit_thickness", "use_edit_uv"], text="", options={"NAMES": ("Position", "Strength", "Thickness", "UV")})
        props["use_edit_position"].r_button_width = self.r_button_width_200
        b0.sep(2)
        b0.prop("factor")
        b0.prop("step")
        b0.sep(1)
        b0.prop("use_keep_shape")
        b0.prop("use_smooth_ends")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_edit_position, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_edit_position, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter]

            if ui_anim_data.library_state == 1: return

            if md.use_edit_position:
                props["use_keep_shape"].light()
                props["use_smooth_ends"].light()
            else:
                props["use_keep_shape"].dark()
                props["use_smooth_ends"].dark()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_THICKNESS(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop("use_uniform_thickness")
        b0.prop("thickness")
        b0.sep(1)
        b0.prop("use_weight_factor")
        b0.prop("thickness_factor")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>
        b_influence.sep(2)
        b_influence.prop("use_custom_curve", text="Custom Curve")
        o_edit_curve = b_influence.function(RNA_edit_curve, self.bufn_GREASE_PENCIL_HOOK_edit_curve)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_uniform_thickness, md.use_weight_factor, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_uniform_thickness, md.use_weight_factor, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if md.use_uniform_thickness:
                props["thickness"].light()
                props["thickness_factor"].dark()
                props["use_weight_factor"].dark()
            else:
                props["thickness"].dark()
                props["use_weight_factor"].light()
                if md.use_weight_factor:
                    props["thickness_factor"].dark()
                else:
                    props["thickness_factor"].light()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

            if md.use_custom_curve:
                o_edit_curve.light()
            else:
                o_edit_curve.dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_COLOR(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("color_mode")
        props["color_mode"].r_button_width = self.r_button_width_200
        b0.sep(1)
        b0.prop("hue")
        b0.prop("saturation")
        b0.prop("value")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        # >>>
        b_influence.sep(2)
        b_influence.prop("use_custom_curve", text="Custom Curve")
        o_edit_curve = b_influence.function(RNA_edit_curve, self.bufn_GREASE_PENCIL_HOOK_edit_curve)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence2_callback,, $$)
            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

            if md.use_custom_curve:
                o_edit_curve.light()
            else:
                o_edit_curve.dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_TINT(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("color_mode")
        props["color_mode"].r_button_width = self.r_button_width_200
        b0.sep(1)
        b0.prop("factor")
        b0.prop("use_weight_as_factor")
        b0.prop_flag("tint_mode")
        b0.prop("object", options={"ID":"OBJECT"})
        b0.prop("radius")
        b0.prop("color")
        o_color_ramp = b0.function(RNA_edit_color_ramp, self.bufn_GREASE_PENCIL_TINT_color_ramp)

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>
        b_influence.sep(2)
        b_influence.prop("use_custom_curve", text="Custom Curve")
        o_edit_curve = b_influence.function(RNA_edit_curve, self.bufn_GREASE_PENCIL_HOOK_edit_curve)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.use_weight_as_factor, md.tint_mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]: return
            ui_state[:] = [ui_anim_data.library_state, md.use_weight_as_factor, md.tint_mode, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]

            if ui_anim_data.library_state == 1:
                o_color_ramp.set_ui_state_link()
                o_edit_curve.set_ui_state_link()
                return

            o_color_ramp.set_ui_state_default()
            o_edit_curve.set_ui_state_default()

            if md.use_weight_as_factor:
                props["factor"].dark()
            else:
                props["factor"].light()

            if md.tint_mode == "UNIFORM":
                props["object"].dark()
                props["radius"].dark()
                props["color"].light()
                o_color_ramp.dark()
            else:
                props["object"].light()
                props["radius"].light()
                props["color"].dark()
                o_color_ramp.light()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

            if md.use_custom_curve:
                o_edit_curve.light()
            else:
                o_edit_curve.dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_GREASE_PENCIL_OPACITY(self):

        ui = Ui(self)
        ui.set_fold_state(P_ModifierEditor.is_fold)
        ui_anim_data = ui.set_pp(self.r_modifier)

        b0 = ui.new_block()
        props = b0.props

        b0.prop_flag("color_mode", options={"ROW_LENGTH": 3})
        props["color_mode"].r_button_width = self.r_button_width_200
        b0.sep(1)
        b0.prop("use_uniform_opacity")
        b0.prop("use_weight_as_factor")
        b0.prop("color_factor")
        b0.prop("hardness_factor")

        # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3,, $$)
        b_influence = ui.new_block(title="Influence")
        b_influence.prop_inv_search("invert_layer_filter", "layer_filter", GpuImg_OUTLINER_DATA_GP_LAYER, self.r_object_layers)
        props["layer_filter"].r_button_width = self.r_button_width_166

        o_invert_layer_pass_filter = b_influence.r_prop("invert_layer_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_layer_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_layer_pass_filter = b_influence.r_prop("layer_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_layer_pass_filter, o_invert_layer_pass_filter))
        b_influence.join_bool("use_layer_pass_filter", text="Layer Pass")
        props["use_layer_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)

        b_influence.prop_inv("invert_material_filter", "material_filter", options={"ID":"MATERIAL"})
        props["material_filter"].r_button_width = self.r_button_width_166

        o_invert_material_pass_filter = b_influence.r_prop("invert_material_pass_filter", options={"icon_cls": GpuImg_invert})
        o_invert_material_pass_filter.r_button_width = lambda: SIZE_border[3] - D_SIZE['font_main_title_offset']
        o_material_pass_filter = b_influence.r_prop("material_pass_filter", text="")
        b_influence.w.items.append(ButtonOverlay(b_influence.w, o_material_pass_filter, o_invert_material_pass_filter))
        b_influence.join_bool("use_material_pass_filter", text="Material Pass")
        props["use_material_pass_filter"].r_button_width = self.r_button_width_comb_3
        b_influence.sep(2)
        b_influence.prop_inv_vg("invert_vertex_group", "vertex_group_name", self.r_object_vertex_groups)
        # >>>
        b_influence.sep(2)
        b_influence.prop("use_custom_curve", text="Custom Curve")
        o_edit_curve = b_influence.function(RNA_edit_curve, self.bufn_GREASE_PENCIL_HOOK_edit_curve)

        ui_state = []

        def fn_darklight(md):
            if ui_state == [ui_anim_data.library_state, md.color_mode, md.use_uniform_opacity, md.use_weight_as_factor, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]: return
            ui_state[:] = [ui_anim_data.library_state, md.color_mode, md.use_uniform_opacity, md.use_weight_as_factor, md.vertex_group_name, md.use_layer_pass_filter, md.use_material_pass_filter, md.use_custom_curve]

            if ui_anim_data.library_state == 1:
                o_edit_curve.set_ui_state_link()
                return

            o_edit_curve.set_ui_state_default()

            if md.color_mode == "HARDNESS":
                props["hardness_factor"].light()
                props["use_uniform_opacity"].dark()
                props["use_weight_as_factor"].dark()
                props["color_factor"].dark()
            else:
                props["hardness_factor"].dark()
                props["use_uniform_opacity"].light()
                props["use_weight_as_factor"].light()

                if md.use_uniform_opacity:
                    props["use_weight_as_factor"].dark()
                    props["color_factor"].light()
                else:
                    props["use_weight_as_factor"].light()

                    if md.use_weight_as_factor:
                        props["color_factor"].dark()
                    else:
                        props["color_factor"].light()

            # <<< 1copy (0areas_init_tab_GREASE_PENCIL_TEXTURE_influence3_callback,, $$)
            if md.vertex_group_name:
                props["invert_vertex_group"].light()
            else:
                props["invert_vertex_group"].dark()

            if md.use_layer_pass_filter:
                props["invert_layer_pass_filter"].light()
                props["layer_pass_filter"].light()
            else:
                props["invert_layer_pass_filter"].dark()
                props["layer_pass_filter"].dark()

            if md.use_material_pass_filter:
                props["invert_material_pass_filter"].light()
                props["material_pass_filter"].light()
            else:
                props["invert_material_pass_filter"].dark()
                props["material_pass_filter"].dark()
            # >>>

            if md.use_custom_curve:
                o_edit_curve.light()
            else:
                o_edit_curve.dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|

    def catch_bufn(self, fn, evtkill=True, push_message=""):
        if evtkill: kill_evt_except()
        try:
            if r_library_editable(self.r_object()) is False: return

            with bpy.context.temp_override(object=self.w.active_object): fn()
            if push_message:
                ed_undo_push(message=push_message)
        except Exception as ex:
            DropDownOk(None, MOUSE, input_text=f'Failed.\n{ex}')
        #|
    def bufn_BEVEL_edit_profile(self):

        kill_evt_except()
        try:
            if r_library_editable(self.r_object()) is False: return

            OpBevelProfile.md = self.w.active_modifier
            bpy.ops.wm.vmd_bevel_profile("INVOKE_DEFAULT")
        except Exception as ex:
            DropDownOk(None, MOUSE, input_text=f'Unexpected error, please report to the author.\n{ex}')
        #|
    def bufn_HOOK_edit_curve(self):

        kill_evt_except()
        try:
            if r_library_editable(self.r_object()) is False: return

            OpFalloffCurve.md = self.w.active_modifier
            OpFalloffCurve.attr = "falloff_curve"
            bpy.ops.wm.vmd_falloff_curve("INVOKE_DEFAULT")
        except Exception as ex:
            DropDownOk(None, MOUSE, input_text=f'Unexpected error, please report to the author.\n{ex}')
        #|
    def bufn_VERTEX_WEIGHT_EDIT_edit_curve(self):

        kill_evt_except()
        try:
            if r_library_editable(self.r_object()) is False: return

            OpFalloffCurve.md = self.w.active_modifier
            OpFalloffCurve.attr = "map_curve"
            bpy.ops.wm.vmd_falloff_curve("INVOKE_DEFAULT")
        except Exception as ex:
            DropDownOk(None, MOUSE, input_text=f'Unexpected error, please report to the author.\n{ex}')
        #|
    def bufn_CORRECTIVE_SMOOTH_bind(self):

        self.catch_bufn(
            lambda: bpy.ops.object.correctivesmooth_bind(modifier=self.w.active_modifier.name),
            push_message = "MD Bind")
        #|
    def bufn_LAPLACIANDEFORM_bind(self):

        self.catch_bufn(
            lambda: bpy.ops.object.laplaciandeform_bind(modifier=self.w.active_modifier.name),
            push_message = "MD Bind")
        #|
    def bufn_MESH_DEFORM_bind(self):

        self.catch_bufn(
            lambda: bpy.ops.object.meshdeform_bind(modifier=self.w.active_modifier.name),
            push_message = "MD Bind")
        #|
    def bufn_SURFACE_DEFORM_bind(self):

        self.catch_bufn(
            lambda: bpy.ops.object.surfacedeform_bind(modifier=self.w.active_modifier.name),
            push_message = "MD Bind")
        #|
    def bufn_DATA_TRANSFER_gen(self):

        self.catch_bufn(
            lambda: bpy.ops.object.datalayout_transfer(modifier=self.w.active_modifier.name),
            push_message = "MD Generate Data Layers")
        #|
    def bufn_EXPLODE_refresh(self, evtkill=True):

        self.catch_bufn(
            lambda: bpy.ops.object.explode_refresh(modifier=self.w.active_modifier.name),
            evtkill=evtkill)

        upd_link_data()
        #|
    def bufn_MULTIRES_subdivide(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_subdivide(modifier=self.w.active_modifier.name, mode='CATMULL_CLARK'),
            push_message = "MD Subdivide")
        #|
    def bufn_MULTIRES_simple(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_subdivide(modifier=self.w.active_modifier.name, mode='SIMPLE'),
            push_message = "MD Simple")
        #|
    def bufn_MULTIRES_linear(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_subdivide(modifier=self.w.active_modifier.name, mode='LINEAR'),
            push_message = "MD Linear")
        #|
    def bufn_MULTIRES_unsubdivide(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_unsubdivide(modifier=self.w.active_modifier.name),
            push_message = "MD Unsubdivide")
        #|
    def bufn_MULTIRES_delete_higher(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_higher_levels_delete(modifier=self.w.active_modifier.name),
            push_message = "MD Delete Higher")
        #|
    def bufn_MULTIRES_reshape(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_reshape(modifier=self.w.active_modifier.name),
            push_message = "MD Reshape")
        #|
    def bufn_MULTIRES_apply_base(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_base_apply(modifier=self.w.active_modifier.name),
            push_message = "MD Apply Base")
        #|
    def bufn_MULTIRES_rebuild(self):

        self.catch_bufn(
            lambda: bpy.ops.object.multires_rebuild_subdiv(modifier=self.w.active_modifier.name),
            push_message = "MD Rebuild Subdivisions")
        #|
    def bufn_MULTIRES_save_external(self):

        def fn():
            if self.w.active_modifier.is_external:
                bpy.ops.object.multires_external_pack()
            else:
                bpy.ops.object.multires_external_save("INVOKE_DEFAULT", modifier=self.w.active_modifier.name)
        self.catch_bufn(fn)
        #|
    def bufn_OCEAN_bake(self):

        self.catch_bufn(
            lambda: bpy.ops.object.ocean_bake(modifier=self.w.active_modifier.name, free=True if self.w.active_modifier.is_cached else False),
            push_message = "MD Ocean Bake")
        #|
    def bufn_SKIN_create_armature(self):

        self.catch_bufn(
            lambda: bpy.ops.object.skin_armature_create(modifier=self.w.active_modifier.name),
            push_message = "MD Create Armature")
        #|
    def bufn_SKIN_add_skin_data(self):

        self.catch_bufn(
            lambda: bpy.ops.mesh.customdata_skin_add(),
            push_message = "MD Add Skin Data")
        #|
    def bufn_SKIN_mark_loose(self):

        self.catch_bufn(
            lambda: bpy.ops.object.skin_loose_mark_clear(action='MARK'),
            push_message = "MD Mark Loose")
        #|
    def bufn_SKIN_clear_loose(self):

        self.catch_bufn(
            lambda: bpy.ops.object.skin_loose_mark_clear(action='CLEAR'),
            push_message = "MD Clear Loose")
        #|
    def bufn_SKIN_mark_root(self):

        self.catch_bufn(
            lambda: bpy.ops.object.skin_root_mark(),
            push_message = "MD Mark Root")
        #|
    def bufn_SKIN_equalize_radii(self):

        self.catch_bufn(
            lambda: bpy.ops.object.skin_radii_equalize(),
            push_message = "MD Equalize Radii")
        #|
    def bufn_LINEART_bake(self):
        def bufn():
            bpy.ops.object.lineart_bake_strokes()
            update_scene()

        self.catch_bufn(bufn, push_message = "MD Line Art Bake")
        #|
    def bufn_LINEART_bake_all(self):
        def bufn():
            bpy.ops.object.lineart_bake_strokes(bake_all=True)
            update_scene()

        self.catch_bufn(bufn, push_message = "MD Line Art bake all")
        #|
    def bufn_LINEART_clear(self):
        def bufn():
            bpy.ops.object.lineart_clear()
            update_scene()

        self.catch_bufn(bufn, push_message = "MD Line Art clear bake")
        #|
    def bufn_LINEART_clear_all(self):
        def bufn():
            bpy.ops.object.lineart_clear(clear_all=True)
            update_scene()

        self.catch_bufn(bufn, push_message = "MD Line Art clear all bake")
        #|
    def bufn_LINEART_continue(self):
        modifier = self.w.active_modifier
        if hasattr(modifier, "type") and modifier.type == "LINEART" and modifier.is_baked:
            modifier.is_baked = False
            update_scene_push("MD Line Art Continue")
        #|
    def bufn_GREASE_PENCIL_HOOK_edit_curve(self):
        kill_evt_except()
        try:
            if r_library_editable(self.r_object()) is False: return

            OpFalloffCurve.md = self.w.active_modifier
            OpFalloffCurve.attr = "custom_curve"
            bpy.ops.wm.vmd_falloff_curve("INVOKE_DEFAULT")
        except Exception as ex:
            DropDownOk(None, MOUSE, input_text=f'Unexpected error, please report to the author.\n{ex}')
        #|
    def bufn_GREASE_PENCIL_TINT_color_ramp(self):
        kill_evt_except()
        OpColorRamp.md = self.w.active_modifier
        OpColorRamp.attr = "color_ramp"
        bpy.ops.wm.vmd_color_ramp("INVOKE_DEFAULT")
        #|

    def r_fcurve_use_xyz(self):
        if self.object_fcurves:
            escapename = escape_identifier(self.w.active_modifier_name)
            return [
                self.object_fcurves.find(f'modifiers["{escapename}"].use_x'),
                self.object_fcurves.find(f'modifiers["{escapename}"].use_y'),
                self.object_fcurves.find(f'modifiers["{escapename}"].use_z')
            ]
        return [None] * 3
        #|
    def r_driver_use_xyz(self):
        if self.object_drivers:
            escapename = escape_identifier(self.w.active_modifier_name)
            return [
                self.object_drivers.find(f'modifiers["{escapename}"].use_x'),
                self.object_drivers.find(f'modifiers["{escapename}"].use_y'),
                self.object_drivers.find(f'modifiers["{escapename}"].use_z')
            ]
        return [None] * 3
        #|
    def r_fcurve_use_axis_xyz(self):
        if self.object_fcurves:
            escapename = escape_identifier(self.w.active_modifier_name)
            return [
                self.object_fcurves.find(f'modifiers["{escapename}"].use_axis_x'),
                self.object_fcurves.find(f'modifiers["{escapename}"].use_axis_y'),
                self.object_fcurves.find(f'modifiers["{escapename}"].use_axis_z')
            ]
        return [None] * 3
        #|
    def r_driver_use_axis_xyz(self):
        if self.object_drivers:
            escapename = escape_identifier(self.w.active_modifier_name)
            return [
                self.object_drivers.find(f'modifiers["{escapename}"].use_axis_x'),
                self.object_drivers.find(f'modifiers["{escapename}"].use_axis_y'),
                self.object_drivers.find(f'modifiers["{escapename}"].use_axis_z')
            ]
        return [None] * 3
        #|

    def r_bufn_search(self, old_upd_callback, ui_animdatas, extra_buttons=None, search_data=None):
        def bufn_search(button=None, use_old_data=False):
            button.is_trigger_enable = True

            def bufn_delete():
                search_data.end_search()

                self.upd_data_callback = old_upd_callback
                self.items[:] = old_items
                self.headkey = old_headkey

                for ui_animdata in ui_animdatas:
                    ui_animdata.tag_update()

                    for e in ui_animdata.props.values():
                        if hasattr(e, "tag_clipping_dirty"): e.tag_clipping_dirty()

                self.redraw_from_headkey(fix_pan=True)
                self.upd_data()
                Admin.REDRAW()

            def text_search_set_callback():
                if pp.text_search: pass
                else:
                    bufn_delete()
                    return True

                filter_function = r_filter_function(text_search.is_match_case, text_search.is_match_whole_word, text_search.is_match_end)
                use_identifier = pp.use_identifier
                use_name = pp.use_name
                use_description = pp.use_description
                # pp_use_value = pp.use_value

                def r_result(s,
                            filter_fn = None,
                            search_name = None,
                            search_id = None,
                            search_description = None):

                    if filter_fn is None:
                        filter_fn = filter_function
                    if search_name is None:
                        search_name = use_name
                    if search_id is None:
                        search_id = use_identifier
                    if search_description is None:
                        search_description = use_description
                    out = set()

                    for ui_animdata in ui_animdatas:
                        for k, e in ui_animdata.props.items():
                            if hasattr(e, "rna"):
                                rna = e.rna
                            else: continue

                            if hasattr(rna, "__len__"):
                                for rna in rna:
                                    # <<< 1copy (0defr_bufn_search_text_search,, ${'continue': 'break'}$)
                                    if search_name:
                                        if hasattr(e, "blf_title"):
                                            if hasattr(e.blf_title, "unclip_text"):
                                                name = e.blf_title.unclip_text
                                                if name: pass
                                                else:
                                                    name = rna.name
                                            else: # LIst
                                                name = rna.name
                                        else:
                                            name = rna.name

                                        if filter_fn(name, s):
                                            out.add(rna)
                                            break

                                    if search_description:
                                        if filter_fn(rna.description, s):
                                            out.add(rna)
                                            break

                                    if search_id:
                                        if filter_fn((k[0]  if isinstance(k, tuple) else k), s):
                                            out.add(rna)
                                            break
                                    # >>>
                            else:
                                # /* 0defr_bufn_search_text_search
                                if search_name:
                                    if hasattr(e, "blf_title"):
                                        if hasattr(e.blf_title, "unclip_text"):
                                            name = e.blf_title.unclip_text
                                            if name: pass
                                            else:
                                                name = rna.name
                                        else: # LIst
                                            name = rna.name
                                    else:
                                        name = rna.name

                                    if filter_fn(name, s):
                                        out.add(rna)
                                        continue

                                if search_description:
                                    if filter_fn(rna.description, s):
                                        out.add(rna)
                                        continue

                                if search_id:
                                    if filter_fn((k[0]  if isinstance(k, tuple) else k), s):
                                        out.add(rna)
                                        continue
                                # */

                    if extra_buttons is not None:
                        for e in extra_buttons:
                            if hasattr(e, "rna"):
                                rna = e.rna
                            else: continue

                            if hasattr(rna, "__len__"):
                                for rna in rna:
                                    # <<< 1copy (0defr_bufn_search_text_search,, ${'continue': 'break'}$)
                                    if search_name:
                                        if hasattr(e, "blf_title"):
                                            if hasattr(e.blf_title, "unclip_text"):
                                                name = e.blf_title.unclip_text
                                                if name: pass
                                                else:
                                                    name = rna.name
                                            else: # LIst
                                                name = rna.name
                                        else:
                                            name = rna.name

                                        if filter_fn(name, s):
                                            out.add(rna)
                                            break

                                    if search_description:
                                        if filter_fn(rna.description, s):
                                            out.add(rna)
                                            break

                                    if search_id:
                                        if filter_fn((k[0]  if isinstance(k, tuple) else k), s):
                                            out.add(rna)
                                            break
                                    # >>>
                            else:
                                # <<< 1copy (0defr_bufn_search_text_search,, $$)
                                if search_name:
                                    if hasattr(e, "blf_title"):
                                        if hasattr(e.blf_title, "unclip_text"):
                                            name = e.blf_title.unclip_text
                                            if name: pass
                                            else:
                                                name = rna.name
                                        else: # LIst
                                            name = rna.name
                                    else:
                                        name = rna.name

                                    if filter_fn(name, s):
                                        out.add(rna)
                                        continue

                                if search_description:
                                    if filter_fn(rna.description, s):
                                        out.add(rna)
                                        continue

                                if search_id:
                                    if filter_fn((k[0]  if isinstance(k, tuple) else k), s):
                                        out.add(rna)
                                        continue
                                # >>>
                    return out
                    #|


                text = pp.text_search
                search_data.old_props = pp
                search_data.old_search_text = text_search

                if text.startswith(";") and not text.startswith(";;"):
                    exp = text[1 : ].strip()

                    success, results = r_filtexp_result(exp, r_result, filter_function)
                    if not success:
                        DropDownOk(None, MOUSE, input_text=f'Eval Failed\n{results}')
                        return True
                else:
                    if text.startswith(";;"):
                        text = text[1 : ]
                    results = r_result(text, filter_function)

                block0 = b0.w
                b0buttons = block0.items
                b0buttons.clear()

                if results:
                    owner_data = search_data.owner_data

                    for ui_animdata in ui_animdatas:
                        for e in ui_animdata.props.values():
                            if hasattr(e, "rna"):
                                rna = e.rna
                            else: continue

                            if hasattr(rna, "__len__"):
                                for rna in rna:
                                    if rna in results:
                                        b0buttons.append(e)
                                        owner_data[e] = e.w
                                        e.w = block0
                                        if hasattr(e, "tag_clipping_dirty"): e.tag_clipping_dirty()
                                        break
                            else:
                                if rna in results:
                                    b0buttons.append(e)
                                    owner_data[e] = e.w
                                    e.w = block0
                                    if hasattr(e, "tag_clipping_dirty"): e.tag_clipping_dirty()

                    if extra_buttons is not None:
                        for e in extra_buttons:
                            if hasattr(e, "rna"):
                                rna = e.rna
                            else: continue

                            if hasattr(rna, "__len__"):
                                for rna in rna:
                                    if rna in results:
                                        b0buttons.append(e)
                                        owner_data[e] = e.w
                                        e.w = block0
                                        if hasattr(e, "tag_clipping_dirty"): e.tag_clipping_dirty()
                                        break
                            else:
                                if rna in results:
                                    b0buttons.append(e)
                                    owner_data[e] = e.w
                                    e.w = block0
                                    if hasattr(e, "tag_clipping_dirty"): e.tag_clipping_dirty()

                for ui_animdata in ui_animdatas:
                    ui_animdata.tag_update()
                self.redraw_from_headkey(fix_pan=True)
                self.upd_data()
                Admin.REDRAW()
                return True

            if use_old_data is True:
                old_items = search_data.raw_items
                old_headkey = search_data.raw_headkey
                pp = search_data.old_props
            else:
                old_items = self.items[:]
                old_headkey = self.headkey
                search_data.raw_items = old_items
                search_data.raw_headkey = old_headkey

                pp = UiSearch(self)
                pp.text_search = "?"
                pp.use_identifier = P_ModifierEditor.search_prop_use_identifier
                pp.use_name = P_ModifierEditor.search_prop_use_name
                pp.use_description = P_ModifierEditor.search_prop_use_description

            ui = Ui(self)
            ui.set_fold_state(False)
            ui_anim_data = ui.set_pp(lambda: pp, UiSearch, NS)

            b0 = ui.new_block()
            b0.w.r_offset_L = lambda: D_SIZE['font_main_title_offset']
            props = b0.props
            button_search = b0.r_function(RNA_search, bufn_delete, isdarkhard=True,
                options={"icon_cls": GpuImg_delete, "icon_cls_dark": GpuImgNull})
            button_search.r_button_width = lambda: - D_SIZE['font_main_title_offset']

            text_search = b0.r_prop("text_search", text="")
            text_search.set_align("FULL")
            text_search.r_button_width = Ui.r_button_width_FULL_1t
            b0.items.append(ButtonOverlay(text_search.w, button_search, text_search))
            b0.sep(1)

            b0_0 = b0.new_block(title="Search From")
            b0_0.prop("use_identifier", text=("Include", "Identifier"))
            b0_0.prop("use_name")
            b0_0.prop("use_description")
            # b0_0.prop("use_value")
            for e in props.values():
                e.set_callback = text_search_set_callback

            b0 = ui.new_block(title='Results', heavy=True)

            def upd_data_callback():
                ui_anim_data.update_with(N1)
                old_upd_callback()

            self.upd_data_callback = upd_data_callback
            self.init_items_tab()
            upd_data_callback()

            if use_old_data is True:
                old_text_search = search_data.old_search_text
                text_search.is_match_case = old_text_search.is_match_case
                text_search.is_match_whole_word = old_text_search.is_match_whole_word
                text_search.is_match_end = old_text_search.is_match_end
                text_search_set_callback()
            else:
                pp.text_search = ""
                ddw = text_search.to_dropdown()
                def cancel_callback():
                    if pp.text_search: pass
                    else: bufn_delete()

                ddw.data["cancel_callback"] = cancel_callback

            search_data.state = True

        return bufn_search
        #|
    @ oneRecursive
    def reinit_tab_with(self, search_data):
        search_data.tag_reinit = True
        search_data.get_head_item_pos(self)

        self.init_tab(self.active_tab, push=False, evtkill=False)

        if search_data.state is False: return


        button_search = search_data.button_search
        button_search.fn(button=button_search, use_old_data=True)
        self.guess_pan_in_search()
        #|
    @ oneRecursive
    def redraw_from_headkey_with(self, search_data):
        search_data.tag_reinit = True
        search_data.get_head_item_pos(self)

        self.redraw_from_headkey()
        self.upd_data()

        if search_data.state is False: return


        button_search = search_data.button_search
        button_search.fn(button=button_search, use_old_data=True)
        self.guess_pan_in_search()
        #|

    def r_search_button(self):
        if self.items:
            b0 = self.items[0]
            if hasattr(b0, "buttons"):
                o = b0.buttons[0]  if b0.buttons else None
            elif hasattr(b0, "items"):
                o = b0.items[0]  if b0.items else None
            else:
                o = None

            if o is None: return
            if hasattr(o, "button0"):
                o = o.button0

            if hasattr(o, "fn"):
                if hasattr(o, "rna") and o.rna is RNA_search: return o
        return None
        #|
    def evt_search(self, input_text=None):

        kill_evt_except()

        search_button = self.r_search_button()
        if search_button is None: return

        if search_button.fn.__defaults__ is None:
            search_button.fn()
        else:
            if input_text is None:
                search_button.fn(button=search_button)
            else:
                search_button.fn(button=search_button, input_text=input_text)
        #|
    def guess_pan_in_search(self):
        if self.endkey == -1 or not self.items:
            return
        else:
            old_headkey = self.search_data.old_headkey
            if old_headkey >= len(self.items): return

            b0 = self.items[old_headkey]
            if hasattr(b0, "box_block"):
                new_x, new_y = b0.box_block.L, b0.box_block.T
            else:
                return

        old_x, old_y = self.search_data.head_item_pos
        pan_override = self.r_pan_override()
        pan_override(old_x - new_x, old_y - new_y)
        #|

    def init_items_tab(self):

        self.init_draw_range()
        self.get_cv_height()
        self.r_upd_scroll()()
        self.upd_data()
        #|
    def upd_data(self):
        block.FRAME_CURRENT = bpy.context.scene.frame_current
        ob = self.w.active_object
        object_fcurves = None
        object_drivers = None

        if hasattr(ob, "animation_data"):
            animation_data = ob.animation_data
            if hasattr(animation_data, "action"):
                if hasattr(animation_data.action, "fcurves"):
                    object_fcurves = animation_data.action.fcurves
            if hasattr(animation_data, "drivers"):
                object_drivers = animation_data.drivers

        self.object_fcurves = object_fcurves
        self.object_drivers = object_drivers

        if self.active_tab == self.w.active_tab:
            if hasattr(self, "upd_data_callback"): self.upd_data_callback()
        else:

            self.init_tab(self.w.active_tab)

            if hasattr(self, "upd_data_callback"): self.upd_data_callback()
        #|
    #|
    #|

def ui_effector_weights(weight_type, ui, r_effector_weights, r_dph, title="Field Weights"):
    b0 = ui.new_block(title=title)
    uianim_effector_weights = b0.set_pp(r_effector_weights, EffectorWeights, r_dph)
    b0_prop = b0.prop
    b0_prop("collection", options={"ID":"COLLECTION"})
    b0_prop("gravity")
    b0_prop("all")
    b0_prop("force")
    b0_prop("vortex")
    b0_prop("magnetic")
    b0_prop("harmonic")
    b0_prop("charge")
    b0_prop("lennardjones", text="Lennard - Jones")
    b0_prop("wind")
    b0_prop("curve_guide")
    b0_prop("texture")
    if weight_type != "FLUID":
        b0_prop("smokeflow")
    b0_prop("turbulence")
    b0_prop("drag")
    b0_prop("boid")
    return uianim_effector_weights, N1
    #|


class UiSearch:
    __slots__ = (
        'w',
        'text_search',
        'use_identifier',
        'use_name',
        'use_description',
        'use_value')

    id_data = OB_FAKE
    bl_rna = BlRna(
        Dictlist((
            RnaString("text_search",
                name = "Text",
                subtype = "SEARCH"),
            RnaBool("use_identifier",
                name = "Identifier",
                default = True),
            RnaBool("use_name",
                name = "Name",
                default = True),
            RnaBool("use_description",
                name = "Description",
                default = True),
            RnaBool("use_value",
                name = "Value",
                default = False),
        ))
    )

    def __init__(self, w):
        self.w = w

        self.text_search = ""
        self.use_identifier = True
        self.use_name = True
        self.use_description = True
        self.use_value = False
        #|
    #|
    #|
RNAS_UiSearch = UiSearch.bl_rna.properties
RNAS_UiSearch["use_identifier"].data = RnaDataDefaultValue(("ModifierEditor", "search_prop_use_identifier"))
RNAS_UiSearch["use_name"].data = RnaDataDefaultValue(("ModifierEditor", "search_prop_use_name"))
RNAS_UiSearch["use_description"].data = RnaDataDefaultValue(("ModifierEditor", "search_prop_use_description"))

class Info1:
    __slots__ = 'w', 'info'

    id_data = OB_FAKE
    bl_rna = BlRna(
        Dictlist((
            RnaString("info",
                name = "Info",
                is_readonly = True),
        ))
    )

    def __init__(self, w):
        self.w = w

        self.info = ""
        #|
    #|
    #|


RNA_edit_profile = RnaButton("edit_profile",
    name = "Edit Profile",
    button_text = "Edit Profile",
    description = "Edit Profile",
    size = -5)
RNA_edit_curve = RnaButton("edit_curve",
    name = "Edit Curve",
    button_text = "Edit Curve",
    description = "Edit Curve",
    size = -5)
RNA_CORRECTIVE_SMOOTH_bind = RnaButton("CORRECTIVE_SMOOTH_bind",
    name = "Bind",
    button_text = "Bind",
    description = "Bind base pose in Corrective Smooth modifier",
    size = 5)
RNA_DATA_TRANSFER_gen = RnaButton("DATA_TRANSFER_gen",
    name = "Generate Data Layers",
    button_text = "Generate Data Layers",
    description = "Transfer layout of data layer(s) from active to selected meshes")
RNA_EXPLODE_refresh = RnaButton("EXPLODE_refresh",
    name = "Refresh",
    button_text = "Refresh",
    description = "Refresh data in the Explode modifier",
    size = 5)
RNA_LAPLACIANDEFORM_bind = RnaButton("LAPLACIANDEFORM_bind",
    name = "Bind",
    button_text = "Bind",
    description = "Bind mesh to system in laplacian deform modifier",
    size = 5)
RNA_MESH_DEFORM_bind = RnaButton("MESH_DEFORM_bind",
    name = "Bind",
    button_text = "Bind",
    description = "Bind mesh to cage in mesh deform modifier",
    size = 5)
RNA_SURFACE_DEFORM_bind = RnaButton("SURFACE_DEFORM_bind",
    name = "Bind",
    button_text = "Bind",
    description = "Bind mesh to target in surface deform modifier",
    size = 5)
RNA_MULTIRES_subdivide = RnaButton("MULTIRES_subdivide",
    name = "Subdivide",
    button_text = "Subdivide",
    description = "Add a new level of subdivision")
RNA_MULTIRES_simple = RnaButton("MULTIRES_simple",
    name = "Simple",
    button_text = "Simple",
    description = "Add a new level of subdivision")
RNA_MULTIRES_linear = RnaButton("MULTIRES_linear",
    name = "Linear",
    button_text = "Linear",
    description = "Add a new level of subdivision")
RNA_MULTIRES_unsubdivide = RnaButton("MULTIRES_unsubdivide",
    name = "Unsubdivide",
    button_text = "Unsubdivide",
    description = "Rebuild a lower subdivision level of the current base mesh")
RNA_MULTIRES_delete_higher = RnaButton("MULTIRES_delete_higher",
    name = "Delete Higher",
    button_text = "Delete Higher",
    description = "Deletes the higher resolution mesh, potential loss of detail")
RNA_MULTIRES_reshape = RnaButton("MULTIRES_reshape",
    name = "Reshape",
    button_text = "Reshape",
    description = "Copy Vertex coordinates from other object")
RNA_MULTIRES_apply_base = RnaButton("MULTIRES_apply_base",
    name = "Apply Base",
    button_text = "Apply Base",
    description = "Modify the base mesh to conform to the displaced mesh")
RNA_MULTIRES_rebuild = RnaButton("MULTIRES_rebuild",
    name = "Rebuild Subdivisions",
    button_text = "Rebuild Subdivisions",
    description = "Rebuilds all possible subdivisions levels to generate a lower resolution base mesh")
RNA_MULTIRES_save_external = RnaButton("MULTIRES_save_external",
    name = "Save External File",
    button_text = "Save External File",
    description = "Save displacements to an external file")
RNA_OCEAN_bake = RnaButton("OCEAN_bake",
    name = "Bake Ocean",
    button_text = "Bake Ocean",
    description = "Bake an image sequence of ocean data")
RNA_SKIN_create_armature = RnaButton("SKIN_create_armature",
    name = "Create Armature",
    button_text = "Create Armature",
    description = "Create an armature that parallels the skin layout")
RNA_SKIN_add_skin_data = RnaButton("SKIN_add_skin_data",
    name = "Add Skin Data",
    button_text = "Add Skin Data",
    description = "Add a vertex skin layer")
RNA_SKIN_mark_loose = RnaButton("SKIN_mark_loose",
    name = "Mark Loose",
    button_text = "Mark Loose",
    description = "Mark selected vertices as loose")
RNA_SKIN_clear_loose = RnaButton("SKIN_clear_loose",
    name = "Clear Loose",
    button_text = "Clear Loose",
    description = "Clear selected vertices as loose")
RNA_SKIN_mark_root = RnaButton("SKIN_mark_root",
    name = "Mark Root",
    button_text = "Mark Root",
    description = "Mark selected vertices as roots")
RNA_SKIN_equalize_radii = RnaButton("SKIN_equalize_radii",
    name = "Equalize Radii",
    button_text = "Equalize Radii",
    description = "Make skin radii of selected vertices equal on each axis")
RNA_LINEART_BAKE = RnaButton("LINEART_BAKE",
    name = "Bake Line Art",
    button_text = "Bake Line Art",
    description = "Bake Line Art for current Grease Pencil object")
RNA_LINEART_BAKE_ALL = RnaButton("LINEART_BAKE_ALL",
    name = "Bake All",
    button_text = "Bake All",
    description = "Bake Line Art for current Grease Pencil object")
RNA_LINEART_CLEAR = RnaButton("LINEART_CLEAR",
    name = "Clear Baked Line Art",
    button_text = "Clear Baked Line Art",
    description = "Clear all strokes in current Grease Pencil object")
RNA_LINEART_CLEAR_ALL = RnaButton("LINEART_CLEAR_ALL",
    name = "Clear All",
    button_text = "Clear All",
    description = "Clear all strokes in current Grease Pencil object")
RNA_LINEART_CONTINUE = RnaButton("LINEART_CONTINUE",
    name = "Continue Without Clearing",
    button_text = "Continue Without Clearing",
    description = "Modify properties without clearing data")
RNA_edit_color_ramp = RnaButton("edit_color_ramp",
    name = "Edit Color Ramp",
    button_text = "Edit Color Ramp",
    description = "",
    size = 10)
RNA_add_canvas = RnaButton("add_canvas",
    name = "Add Canvas",
    button_text = "Add Canvas",
    description = "Add canvas on Dynamic Paint modifier",
    size = -6)
RNA_remove_canvas = RnaButton("remove_canvas",
    name = "Remove Canvas",
    button_text = "Remove Canvas",
    description = "Remove canvas on Dynamic Paint modifier",
    size = -6)
RNA_add_brush = RnaButton("add_brush",
    name = "Add Brush",
    button_text = "Add Brush",
    description = "Add Brush on Dynamic Paint modifier",
    size = -6)
RNA_remove_brush = RnaButton("remove_brush",
    name = "Remove Brush",
    button_text = "Remove Brush",
    description = "Remove Brush on Dynamic Paint modifier",
    size = -6)
RNA_dpaint_bake_image_sequence = RnaButton("dpaint_bake_image_sequence",
    name = "Bake Image Sequence",
    button_text = "Bake Image Sequence",
    description = "Bake dynamic paint image sequence surface")
RNA_dpaint_brush_color_ramp = RnaButton("dpaint_brush_color_ramp",
    name = "Edit Color Ramp",
    button_text = "Edit Color Ramp",
    description = "",
    size = -6)
RNA_fluid_color_ramp = RnaButton("fluid_color_ramp",
    name = "Edit Color Ramp",
    button_text = "Edit Color Ramp",
    description = "")
RNA_fluid_bake_all = RnaButton("fluid_bake_all",
    name = "Bake All",
    button_text = "Bake All",
    description = "Bake entire fluid simulation")
RNA_fluid_free_all = RnaButton("fluid_free_all",
    name = "Free All",
    button_text = "Free All",
    description = "Free entire fluid simulation")
RNA_fluid_bake_data = RnaButton("fluid_bake_data",
    name = "Bake Data",
    button_text = "Bake Data",
    description = "Bake fluid data")
RNA_fluid_free_data = RnaButton("fluid_free_data",
    name = "Free Data",
    button_text = "Free Data",
    description = "Free fluid data")
RNA_fluid_bake_noise = RnaButton("fluid_bake_noise",
    name = "Bake Noise",
    button_text = "Bake Noise",
    description = "Bake fluid noise")
RNA_fluid_free_noise = RnaButton("fluid_free_noise",
    name = "Free Noise",
    button_text = "Free Noise",
    description = "Free fluid noise")
RNA_fluid_bake_guides = RnaButton("fluid_bake_guides",
    name = "Bake Guides",
    button_text = "Bake Guides",
    description = "Bake fluid guiding")
RNA_fluid_free_guides = RnaButton("fluid_free_guides",
    name = "Free Guides",
    button_text = "Free Guides",
    description = "Free fluid guiding")
RNA_fluid_bake_mesh = RnaButton("fluid_bake_mesh",
    name = "Bake Mesh",
    button_text = "Bake Mesh",
    description = "Bake fluid mesh")
RNA_fluid_free_mesh = RnaButton("fluid_free_mesh",
    name = "Free Mesh",
    button_text = "Free Mesh",
    description = "Free fluid mesh")
RNA_fluid_bake_particles = RnaButton("fluid_bake_particles",
    name = "Bake Particles",
    button_text = "Bake Particles",
    description = "Bake fluid particles")
RNA_fluid_free_particles = RnaButton("fluid_free_particles",
    name = "Free Particles",
    button_text = "Free Particles",
    description = "Free fluid particles")
RNA_particle_edited_clear = RnaButton("particle_edited_clear",
    name = "Edited Clear",
    button_text = "Delete Edit",
    description = "Undo all edition performed on the particle system")
RNA_particle_connect_hair = RnaButton("particle_connect_hair",
    name = "Connect Hair",
    button_text = "Connect Hair",
    description = "Connect hair to the emitter mesh")
RNA_particle_connect_all = RnaButton("particle_connect_all",
    name = "Connect All",
    button_text = "Connect All",
    description = "Connect all hair to the emitter mesh")
RNA_particle_disconnect_hair = RnaButton("particle_disconnect_hair",
    name = "Disconnect Hair",
    button_text = "Disconnect Hair",
    description = "Disconnect hair to the emitter mesh")
RNA_particle_disconnect_all = RnaButton("particle_disconnect_all",
    name = "Disconnect All",
    button_text = "Disconnect All",
    description = "Disconnect all hair to the emitter mesh")

RNA_surface_type = r_rna_enum_from_bl_rna(
    DynamicPaintSurface_bl_rnas["surface_type"], (
        ("PAINT", "Paint", ""),
        ("DISPLACE", "Displace", ""),
        ("WEIGHT", "Weight", ""),
        ("WAVE", "Waves", "")),
    "PAINT",
    values = (0, 1, 2, 3))
RNA_surface_type_3 = r_rna_enum_from_bl_rna(
    DynamicPaintSurface_bl_rnas["surface_type"], (
        ("PAINT", "Paint", ""),
        ("DISPLACE", "Displace", ""),
        ("WAVE", "Waves", "")),
    "PAINT",
    values = (0, 1, 3))
RNA_cache_data_format = r_rna_enum_from_bl_rna(
    FluidDomainSettings_bl_rnas["cache_data_format"], (
        ("UNI", "Uni Cache", "Uni file format (.uni)"),
        ("OPENVDB", "OpenVDB", "OpenVDB file format (.vdb)"),
        ("RAW", "Raw", "Raw file format (.raw)")),
    "OPENVDB",
    values = (1, 2, 4))
RNA_cache_mesh_format = r_rna_enum_from_bl_rna(
    FluidDomainSettings_bl_rnas["cache_mesh_format"], (
        ("BOBJECT", "Binary Object", "Binary object file format (.bobj.gz)"),
        ("OBJECT", "Object", "Object file format (.obj)")),
    "BOBJECT",
    values = (8, 16))
RNA_openvdb_data_depth = r_rna_enum_from_bl_rna(
    FluidDomainSettings_bl_rnas["openvdb_data_depth"], (
        ("32", "Full", "Full float (Use 32 bit for all data)"),
        ("16", "Half", "Half float (Use 16 bit for all data)"),
        ("8", "Mini", "Mini float (Use 8 bit where possible, otherwise use 16 bit)")),
    "16",
    values = (1, 0, 2))
RNA_color_ramp_field_gas = r_rna_enum_from_bl_rna(
    FluidDomainSettings_bl_rnas["color_ramp_field"], (
        ("FLAGS", "Flags", "Flag grid of the fluid domain"),
        ("PRESSURE", "Pressure", "Pressure field of the fluid domain"),
        ("VELOCITY_X", "X Velocity", "X component of the velocity field"),
        ("VELOCITY_Y", "Y Velocity", "Y component of the velocity field"),
        ("VELOCITY_Z", "Z Velocity", "Z component of the velocity field"),
        ("FORCE_X", "X Force", "X component of the force field"),
        ("FORCE_Y", "Y Force", "Y component of the force field"),
        ("FORCE_Z", "Z Force", "Z component of the force field"),
        ("COLOR_R", "Red", "Red component of the color field"),
        ("COLOR_G", "Green", "Green component of the color field"),
        ("COLOR_B", "Blue", "Blue component of the color field"),
        ("DENSITY", "Density", "Quantity of soot in the fluid"),
        ("FLAME", "Flame", "Flame field"),
        ("FUEL", "Fuel", "Fuel field"),
        ("HEAT", "Heat", "Temperature of the fluid")),
    "DENSITY",
    values = (18, 19, 5, 6, 7, 11, 12, 13, 8, 9, 10, 0, 4, 2, 1))
RNA_color_ramp_field_liquid = r_rna_enum_from_bl_rna(
    FluidDomainSettings_bl_rnas["color_ramp_field"], (
        ("FLAGS", "Flags", "Flag grid of the fluid domain"),
        ("VELOCITY_X", "X Velocity", "X component of the velocity field"),
        ("VELOCITY_Y", "Y Velocity", "Y component of the velocity field"),
        ("VELOCITY_Z", "Z Velocity", "Z component of the velocity field"),
        ("FORCE_X", "X Force", "X component of the force field"),
        ("FORCE_Y", "Y Force", "Y component of the force field"),
        ("FORCE_Z", "Z Force", "Z component of the force field"),
        ("PHI", "Fluid Level Set", "Level set representation of the fluid"),
        ("PHI_IN", "Inflow Level Set", "Level set representation of the inflow"),
        ("PHI_OUT", "Outflow Level Set", "Level set representation of the outflow"),
        ("PHI_OBSTACLE", "Obstacle Level Set", "Level set representation of the obstacles")),
    "PHI",
    values = (18, 5, 6, 7, 11, 12, 13, 14, 15, 16, 17))
RNA_flow_source = r_rna_enum_from_bl_rna(
    FluidFlowSettings_bl_rnas["flow_source"], (
        ("MESH", "Mesh", "Emit fluid from mesh surface or volume"),
        ("PARTICLES", "Particle System", "Emit smoke from particles")),
    "MESH",
    values = (1, 0))

RNA_search = RnaButton("search",
    name = "Search",
    button_text = "",
    description = "Search properties")


def late_import():
    #|
    # <<< 1mp (VMD
    block = VMD.block
    # >>>

    # <<< 1mp (VMD.api
    api = VMD.api
    attr_NodesModifier_bake_directory = api.attr_NodesModifier_bake_directory
    # >>>

    # <<< 1mp (VMD.block
    block = VMD.block
    Blocks = block.Blocks
    BlockUtil = block.BlockUtil
    Title = block.Title
    ButtonSep = block.ButtonSep
    ButtonSplit = block.ButtonSplit
    ButtonGroupY = block.ButtonGroupY
    ButtonGroupTitle = block.ButtonGroupTitle
    ButtonOverlay = block.ButtonOverlay
    poll_hard_disable = block.poll_hard_disable
    wrapButtonFn = block.wrapButtonFn
    Ui = block.Ui
    D_cprop = block.D_cprop
    is_gn_rna_dirty = block.is_gn_rna_dirty
    is_gn_rna_dirty_no_layout = block.is_gn_rna_dirty_no_layout
    rr_items_gn_attributes = block.rr_items_gn_attributes
    geticon_obj_attr = block.geticon_obj_attr
    getinfo_obj_attr = block.getinfo_obj_attr
    # >>>

    # <<< 1mp (VMD.blocklist
    blocklist = VMD.blocklist
    BlockMediaAZ = blocklist.BlockMediaAZ
    BlocklistAZ = blocklist.BlocklistAZ
    BlocklistAZEnabled = blocklist.BlocklistAZEnabled
    ui_point_cache = blocklist.ui_point_cache
    # >>>

    # <<< 1mp (VMD.dd
    dd = VMD.dd
    DropDownOk = dd.DropDownOk
    # >>>

    # <<< 1mp (VMD.handle
    handle = VMD.handle
    upd_link_data = handle.upd_link_data
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    TRIGGER = keysys.TRIGGER
    EVT_TYPE = keysys.EVT_TYPE
    r_end_trigger = keysys.r_end_trigger
    MOUSE = keysys.MOUSE
    kill_evt_except = keysys.kill_evt_except
    # >>>

    # <<< 1mp (VMD.m
    m = VMD.m
    P = m.P
    Admin = m.Admin
    jumpout_head = m.jumpout_head
    # >>>

    # <<< 1mp (VMD.rna
    rna = VMD.rna
    RNA_refresh = rna.RNA_refresh
    # >>>

    # <<< 1mp (VMD.win
    win = VMD.win
    Head = win.Head
    # >>>

    # <<< 1mp (VMD.util.com
    com = VMD.util.com
    N = com.N
    NS = com.NS
    N1 = com.N1
    r_filter_function = com.r_filter_function
    # >>>

    # <<< 1mp (VMD.util.const
    const = VMD.util.const
    RANGE_2 = const.RANGE_2
    RANGE_3 = const.RANGE_3
    RANGE_4 = const.RANGE_4
    TUP_XYZ = const.TUP_XYZ
    STR_09 = const.STR_09
    # >>>

    # <<< 1mp (VMD.util.filtexp
    filtexp = VMD.util.filtexp
    r_filtexp_result = filtexp.r_filtexp_result
    # >>>

    utilbl = VMD.utilbl
    # <<< 1mp (utilbl
    blg = utilbl.blg
    # >>>

    # <<< 1mp (utilbl.blg
    blg = utilbl.blg
    r_button_h = blg.r_button_h
    report = blg.report
    FONT0 = blg.FONT0
    D_SIZE = blg.D_SIZE
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_widget = blg.SIZE_widget
    SIZE_block = blg.SIZE_block
    SIZE_button = blg.SIZE_button
    COL_box_val_fg_error = blg.COL_box_val_fg_error
    COL_block_fg_info = blg.COL_block_fg_info
    GpuImg_GROUP_VCOL = blg.GpuImg_GROUP_VCOL
    GpuImg_GROUP_VERTEX = blg.GpuImg_GROUP_VERTEX
    GpuImg_BONE_DATA = blg.GpuImg_BONE_DATA
    GpuImg_GROUP_UVS = blg.GpuImg_GROUP_UVS
    GpuImg_GROUP_VCOL = blg.GpuImg_GROUP_VCOL
    GpuImg_PHYSICS = blg.GpuImg_PHYSICS
    GpuImg_SPHERECURVE = blg.GpuImg_SPHERECURVE
    GpuImg_NOCURVE = blg.GpuImg_NOCURVE
    GpuImg_ID_PALETTE = blg.GpuImg_ID_PALETTE
    GpuImg_ID_MESH = blg.GpuImg_ID_MESH
    GpuImg_ID_PARTICLE = blg.GpuImg_ID_PARTICLE
    GpuImg_OUTLINER_DATA_GP_LAYER = blg.GpuImg_OUTLINER_DATA_GP_LAYER
    GpuImg_TRASH = blg.GpuImg_TRASH
    GpuImg_search = blg.GpuImg_search
    GpuImg_delete = blg.GpuImg_delete
    GpuImg_distance = blg.GpuImg_distance
    GpuImg_invert = blg.GpuImg_invert
    GpuImg_MATCUBE = blg.GpuImg_MATCUBE
    GpuImg_META_CUBE = blg.GpuImg_META_CUBE
    GpuImg_EMPTY_AXIS = blg.GpuImg_EMPTY_AXIS
    GpuImg_FILE_REFRESH = blg.GpuImg_FILE_REFRESH
    GpuImg_cache_layer = blg.GpuImg_cache_layer
    GpuImg_objectpath = blg.GpuImg_objectpath
    GpuImg_SPREADSHEET = blg.GpuImg_SPREADSHEET
    GpuImgNull = blg.GpuImgNull
    geticon_dynamic_paint_canvas = blg.geticon_dynamic_paint_canvas
    D_geticon_dynamic_paint_surface_format = blg.D_geticon_dynamic_paint_surface_format
    D_geticon_dynamic_paint_surface_type = blg.D_geticon_dynamic_paint_surface_type
    D_geticon_init_color_type = blg.D_geticon_init_color_type
    D_geticon_falloff = blg.D_geticon_falloff
    update_icons_dynamic_paint_canvas = blg.update_icons_dynamic_paint_canvas
    # >>>

    # <<< 1mp (utilbl.general
    general = utilbl.general
    update_scene = general.update_scene
    update_scene_push = general.update_scene_push
    r_library_editable = general.r_library_editable
    r_ID_dp = general.r_ID_dp
    rr_enum_items_uv = general.rr_enum_items_uv
    rr_enum_items_vgroup = general.rr_enum_items_vgroup
    rr_enum_items_vertex_color = general.rr_enum_items_vertex_color
    # >>>

    # <<< 1mp (utilbl.ops
    ops = utilbl.ops
    OpBevelProfile = ops.OpBevelProfile
    OpFalloffCurve = ops.OpFalloffCurve
    OpColorRamp = ops.OpColorRamp
    OpScanFile = ops.OpScanFile
    # >>>

    P_ModifierEditor = P.ModifierEditor

    globals().update(locals())
    #|
