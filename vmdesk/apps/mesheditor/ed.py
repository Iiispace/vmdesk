











import bpy, _bpy, bmesh, gpu
from mathutils.geometry import normal
from numpy.linalg import matrix_rank

gpu_matrix_push_pop = gpu.matrix.push_pop
gpu_matrix_multiply_matrix = gpu.matrix.multiply_matrix
gpu_matrix_scale_uniform = gpu.matrix.scale_uniform

# <<< 1mp (bmesh
from_edit_mesh = bmesh.from_edit_mesh
# >>>

from .  import VMD

# <<< 1mp (VMD.util.const
const = VMD.util.const
VEC_001 = const.VEC_001
VEC_010 = const.VEC_010
# >>>

# <<< 1mp (VMD.area
area = VMD.area
AreaBlock = area.AreaBlock
AreaBlockTab = area.AreaBlockTab
AreaBlockHead = area.AreaBlockHead
# >>>

# <<< 1mp (VMD.win
win = VMD.win
Window = win.Window
StructGlobalUndo = win.StructGlobalUndo
# >>>

# <<< 1mp (VMD
m = VMD.m
# >>>

CONTEXT = _bpy.context


class MeshEditor(Window, StructGlobalUndo):
    __slots__ = (
        'area_head',
        'area_tab',
        'local_space',
        'active_tab')

    name = 'Mesh Editor'

    @staticmethod
    def r_size_default():
        PP = P.MeshEditor
        border_outer = SIZE_border[0]
        d0 = SIZE_dd_border[0]
        border_outer_2 = border_outer + border_outer

        return (
            border_outer_2 + round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac),
            border_outer_2 + AreaBlock.calc_height_by_block_len(1) + SIZE_dd_border[1] + round(2.57857 * D_SIZE['widget_width'] * PP.area_heightfac)
        )
        #| (374, 400)
    @staticmethod
    def r_size_default_area_tab():
        PP = P.MeshEditor
        border_outer = SIZE_border[0]
        d0 = SIZE_dd_border[0]

        return (
            round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac),
            round(2.57857 * D_SIZE['widget_width'] * PP.area_heightfac)
        )
        #|
    @staticmethod
    def r_size_default_area_head():
        PP = P.MeshEditor
        border_outer = SIZE_border[0]
        d0 = SIZE_dd_border[0]

        return (
            round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac),
            AreaBlock.calc_height_by_block_len(1)
        )
        #|

    def init(self, boxes, blfs):
        BlendDataTemp.init()

        self.local_space = "GLOBAL"

        # /* 0ed_MeshEditor_init
        PP = self.P_editor
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        LL = self.box_win.L + border_outer
        TT = self.box_win.title_B - border_outer

        RR = LL + round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac)
        B0 = TT - AreaBlock.calc_height_by_block_len(1)
        T0 = B0 - d1
        BB = T0 - round(2.79 * D_SIZE['widget_width'] * PP.area_heightfac)
        # */

        area_head = AreaBlockHead(self, LL, RR, B0, TT, r_size_default=self.r_size_default_area_head)
        area_head.attributes = PpMeshEditor(area_head)
        ui = Ui(area_head)
        ui_anim_data = ui.set_pp(lambda: self, PpMeshEditor, NS)
        b0 = ui.new_block()
        b0.w.no_background()
        b0.w.use_anim_slot = False
        b0.prop_flag("local_space", text="")
        b0.props["local_space"].r_button_width = lambda: D_SIZE['widget_width'] + min(SIZE_widget[2], SIZE_widget[0])
        area_head.init_draw_range()

        area_tab = AreaBlockTabMeshEditor(self, LL, RR, BB, T0, r_size_default=self.r_size_default_area_tab)
        area_tab.active_tab = ("",)
        area_tab.attributes = PpMeshTab(area_tab)
        self.areas = [area_head, area_tab]
        self.area_head = area_head
        self.area_tab = area_tab

        self.upd_data()
        BlendDataTemp.kill()
        #|

    def upd_size_areas(self):
        # <<< 1copy (0ed_MeshEditor_init,, $$)
        PP = self.P_editor
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        LL = self.box_win.L + border_outer
        TT = self.box_win.title_B - border_outer

        RR = LL + round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac)
        B0 = TT - AreaBlock.calc_height_by_block_len(1)
        T0 = B0 - d1
        BB = T0 - round(2.79 * D_SIZE['widget_width'] * PP.area_heightfac)
        # >>>
        self.area_head.upd_size(LL, RR, B0, TT)
        self.area_tab.upd_size(LL, RR, BB, T0)
        #|

    def upd_data(self):
        ob = CONTEXT.object
        if hasattr(ob, "mode") and ob.mode == "EDIT":
            if self.area_tab.active_tab != ("MAIN",):
                self.area_tab.init_tab(("MAIN",))
        else:
            if self.area_tab.active_tab != ("NONE",):
                self.area_tab.init_tab(("NONE",))

        self.area_head.upd_data()
        self.area_tab.upd_data()
        #|
    #|
    #|

def r_button_width_str_vec():
    return round(D_SIZE['widget_width'] * 1.6)
    #|
def r_button_width_info_L():
    return round(D_SIZE['widget_width'] + SIZE_widget[0] * 2)
    #|

class AreaBlockTabMeshEditor(AreaBlockTab):
    __slots__ = (
        'upd_data_callback',
        'bm_data')

    def init_tab_NONE(self):
        self.items[:] = [BlockFull(self, ButtonGroupTitle(None, "Requires Edit Mesh"))]

        self.upd_data_callback = N
        #|
    def init_tab_MAIN(self):
        attributes = self.attributes
        r_local_space = lambda: self.w.local_space == "LOCAL"
        option = {"r_local_space": r_local_space}

        ui = Ui(self)
        ui.set_fold_state(P.MeshEditor.is_fold)
        ui_anim_data = ui.set_pp(lambda: attributes, PpMeshTab, NS)
        rnas = ui_anim_data.rnas

        b0 = ui.new_block(title=ui.r_prop("distance", isdarkhard=True))
        b0.w.use_anim_slot = False
        b0.w.blf_title.text = "Vertices"
        props = b0.props
        allot_callback(props, "distance", callback_distance, option, drag_untag=True)
        b0.prop("direction", isdarkhard=True)
        allot_callback(props, "direction", callback_direction, option, drag_untag=True)
        b0.sep(0)
        b0.prop("vert_invert")
        props["vert_invert"].set_callback = update_data_true
        b0.sep(0)
        b0.prop("u_direction", isdarkhard=True)
        allot_callback(props, "u_direction", callback_u_direction, option)
        props["u_direction"].r_button_width = r_button_width_str_vec

        b1 = ui.new_block(title=ui.r_prop("u_normal", isdarkhard=True))
        b1.w.use_anim_slot = False
        b1.w.blf_title.text = "Face"
        allot_callback(props, "u_normal", callback_u_normal, option)
        props["u_normal"].r_button_width = r_button_width_str_vec
        b1.prop("method_set_normal")
        props["method_set_normal"].set_callback = update_data_true
        props["method_set_normal"].r_button_width = r_button_width_str_vec
        b1.prop("lock_active_vertex")
        props["lock_active_vertex"].set_callback = update_data_true

        o_vert_limit = ui.r_function(rnas["vert_limit"], wrapper_push(self.bufn_limit, rnas["vert_limit"], push_method="PUSH"))
        o_vert_limit.init_bat = o_vert_limit.init_bat_L
        o_vert_limit.r_button_width = lambda: round(D_SIZE['widget_width'] * 0.7)
        b2 = ui.new_block(title=o_vert_limit)
        b2.w.use_anim_slot = False
        o_make_collinear = b2.r_function(rnas["make_collinear"], wrapper_push(self.bufn_collinear, rnas["make_collinear"], push_method="PUSH"))
        o_info0 = b2.r_info("")
        o_info0.r_button_width = r_button_width_info_L
        b2.overlay(o_info0, o_make_collinear)
        o_make_coplanar = b2.r_function(rnas["make_coplanar"], wrapper_push(self.bufn_coplanar, rnas["make_coplanar"], push_method="PUSH"))
        o_info1 = b2.r_info("")
        o_info1.r_button_width = r_button_width_info_L
        b2.overlay(o_info1, o_make_coplanar)
        b2.sep(1)
        b2.prop("lock_active_vertex_collinear")
        props["lock_active_vertex_collinear"].set_callback = update_data_true
        b2.sep(1)
        b2.prop("area", isdarkhard=True)
        allot_callback(props, "area", callback_area, option, drag_untag=True)
        b2.prop("angle", isdarkhard=True)
        allot_callback(props, "angle", callback_angle, option, drag_untag=True)

        if P.MeshEditor.use_ui_preview:
            # /* 0AreaBlockTabMeshEditor_draw_distance
            distance_dashline_coords = [[0.0] * 3, [0.0] * 3]
            distance_dashline = GpuScreenDash(COL_preview_3d_dash, COL_preview_3d_dash2, distance_dashline_coords)

            def inside_draw_distance():
                ob = CONTEXT.object
                if hasattr(ob, "mode") and ob.mode == "EDIT":
                    if sum(o.data.total_vert_sel  for o in CONTEXT.objects_in_mode) == 2:
                        coords = []
                        for o in CONTEXT.objects_in_mode:
                            if o.data.total_vert_sel == 0: continue

                            bm = from_edit_mesh(o.data)
                            coords += [tuple(o.matrix_world @ v.co)  for v in bm.verts  if v.select]
                            # bm.free()

                        if len(coords) == 2:
                            distance_dashline_coords[:] = coords
                            distance_dashline.upd()
                            distance_dashline.bind_draw()
            # */
            allot_inout_draw_view(props["distance"], inside_draw_distance)

            # /* 0AreaBlockTabMeshEditor_draw_angle
            angle_dashline_coords = [[0.0] * 3, [0.0] * 3]
            angle_dashline = GpuScreenDash(COL_preview_3d_dash, COL_preview_3d_dash2, angle_dashline_coords)
            angle_dashline_coords2 = [[0.0] * 3, [0.0] * 3]
            angle_dashline2 = GpuScreenDash(COL_preview_3d_dash, COL_preview_3d_dash2, angle_dashline_coords2)

            def inside_draw_angle():
                ob = CONTEXT.object
                if hasattr(ob, "mode") and ob.mode == "EDIT":
                    if sum(o.data.total_vert_sel  for o in CONTEXT.objects_in_mode) == 3:
                        bm_data = r_bm_data(CONTEXT)
                        v0, v1, v2 = r_3vert_angle(bm_data)
                        bm_dic = bm_data["bm_dic"]
                        v0_glo = bm_dic[v0].matrix_world @ v0.co
                        v1_glo = bm_dic[v1].matrix_world @ v1.co
                        v2_glo = bm_dic[v2].matrix_world @ v2.co

                        vec0 = v0_glo - v1_glo
                        vec0_length = vec0.length
                        vec1_length = (v2_glo - v1_glo).length
                        if vec1_length > vec0_length:
                            arc_scale = 0.33 * vec0_length
                        else:
                            arc_scale = 0.33 * vec1_length

                        angle_dashline_coords[:] = [
                            v0_glo,
                            v1_glo,
                        ]
                        angle_dashline_coords2[:] = [
                            v1_glo,
                            v2_glo,
                        ]

                        angle_dashline.upd()
                        angle_dashline2.upd()
                        angle_dashline.bind_draw()
                        angle_dashline2.bind_draw()

                        mat_arc = r_qdiff(VEC_001, normal((v0_glo, v1_glo, v2_glo)), VEC_010, vec0.normalized()).to_matrix().to_4x4()
                        mat_arc[0][3] = v1_glo[0]
                        mat_arc[1][3] = v1_glo[1]
                        mat_arc[2][3] = v1_glo[2]
                        with gpu_matrix_push_pop():
                            gpu_matrix_multiply_matrix(mat_arc)
                            gpu_matrix_scale_uniform(arc_scale)
                            draw_angle_arc(r_angle(v0_glo, v1_glo, v2_glo), 32, COL_preview_3d_arc)
            # */
            allot_inout_draw_view(props["angle"], inside_draw_angle)

        def fn_darklight(ats):
            ob = CONTEXT.object
            if hasattr(ob, "mode") and ob.mode == "EDIT":
                bm_data = r_bm_data(CONTEXT)
                self.bm_data = bm_data

                if bm_data["total_vert_sel"] == 2:
                    if props["distance"].isdark is True:
                        props["distance"].light()
                        props["direction"].light()
                        props["u_direction"].light()
                        props["vert_invert"].light()

                    if props["u_normal"].isdark is False:
                        props["u_normal"].dark()
                        props["method_set_normal"].dark()
                        props["lock_active_vertex"].dark()
                    if o_make_collinear.isdark is False:
                        o_make_collinear.dark()
                        o_info0.set_text("")
                        o_make_coplanar.dark()
                        o_info1.set_text("")
                        props["lock_active_vertex_collinear"].dark()
                    if props["area"].isdark is False:
                        props["area"].dark()

                    try: act = bm_data["bms"][ob].bm.select_history.active
                    except: act = None

                    v0, v1 = bm_data["verts"]
                    if act is v1: v0, v1 = v1, v0
                    if attributes.vert_invert: v0, v1 = v1, v0

                    if self.w.local_space == "LOCAL":
                        vec = v0.co - v1.co
                        attributes.direction[:] = vec
                        attributes.u_direction[:] = vec.normalized()
                        attributes.distance = vec.length
                    else:
                        bm_dic = bm_data["bm_dic"]
                        vec = (bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)
                        attributes.direction[:] = vec
                        attributes.u_direction[:] = vec.normalized()
                        attributes.distance = vec.length
                else:
                    if props["distance"].isdark is False:
                        props["distance"].dark()
                        props["direction"].dark()
                        props["u_direction"].dark()
                        props["vert_invert"].dark()

                    inlimit = bm_data["total_vert_sel"] <= P.MeshEditor.vert_limit
                    local_space = self.w.local_space == "LOCAL"

                    if bm_data["total_vert_sel"] >= 3 and inlimit:
                        if props["u_normal"].isdark is True:
                            props["u_normal"].light()
                            props["lock_active_vertex"].light()
                        if o_make_collinear.isdark is True:
                            o_make_collinear.light()
                            o_make_coplanar.light()
                            props["lock_active_vertex_collinear"].light()

                        if bm_data["total_face_sel"] == 1 and bm_data["total_vert_sel"] == len(bm_data["faces"][0].verts):
                            if props["method_set_normal"].isdark is True:
                                props["method_set_normal"].light()

                            plane = bm_data["faces"][0]
                            if local_space is True:
                                attributes.u_normal[:] = normal(loop.vert.co  for loop in plane.loops)
                            else:
                                mat = bm_data["bm_dic"][plane].matrix_world
                                attributes.u_normal[:] = normal(mat @ loop.vert.co  for loop in plane.loops)
                        else:
                            if props["method_set_normal"].isdark is True:
                                props["method_set_normal"].light()

                            if local_space is True:
                                attributes.u_normal[:] = normal(v.co  for v in bm_data["verts"])
                            else:
                                bm_dic = bm_data["bm_dic"]
                                attributes.u_normal[:] = normal(bm_dic[v].matrix_world @ v.co  for v in bm_data["verts"])

                        vecs = bm_data["verts"][ : -1]
                        if local_space is True:
                            v_co = bm_data["verts"][-1].co
                            vecs = [v.co - v_co  for v in vecs]
                        else:
                            bm_dic = bm_data["bm_dic"]
                            v = bm_data["verts"][-1]
                            v_co = bm_dic[v].matrix_world @ v.co
                            vecs = [bm_dic[v].matrix_world @ v.co - v_co  for v in vecs]
                        th = bin_search_continue(lambda v: matrix_rank(vecs, v) < 2, 0, 1000)
                        o_info0.set_text(f"Collinear Threshold :  {'> 1000'  if th is None else '{:.6f}'.format(th)}")
                        th = bin_search_continue(lambda v: matrix_rank(vecs, v) < 3, 0, 1000)
                        o_info1.set_text(f"Coplanar Threshold :  {'> 1000'  if th is None else '{:.6f}'.format(th)}")

                        if bm_data["total_vert_sel"] == 3:
                            if props["angle"].isdark is True:
                                props["angle"].light()

                            v0, v1, v2 = r_3vert_angle(bm_data)
                            if local_space is True:
                                attributes.angle = r_angle(v0.co, v1.co, v2.co)
                            else:
                                bm_dic = bm_data["bm_dic"]
                                attributes.angle = r_angle(
                                    bm_dic[v0].matrix_world @ v0.co,
                                    bm_dic[v1].matrix_world @ v1.co,
                                    bm_dic[v2].matrix_world @ v2.co)
                        else:
                            if props["angle"].isdark is False:
                                props["angle"].dark()
                    else:
                        if props["u_normal"].isdark is False:
                            props["u_normal"].dark()
                            props["method_set_normal"].dark()
                            props["lock_active_vertex"].dark()
                        if o_make_collinear.isdark is False:
                            o_make_collinear.dark()
                            o_info0.set_text("")
                            o_make_coplanar.dark()
                            o_info1.set_text("")
                            props["lock_active_vertex_collinear"].dark()
                        if props["angle"].isdark is False:
                            props["angle"].dark()

                    if bm_data["total_face_sel"] >= 1 and inlimit:
                        if props["area"].isdark is True:
                            props["area"].light()

                        if local_space is True:
                            attributes.area = sum(face.calc_area()  for face in bm_data["faces"])
                        else:
                            attributes.area = r_faces_area(bm_data["faces"], bm_data["bm_dic"])
                    else:
                        if props["area"].isdark is False:
                            props["area"].dark()

        def upd_data_callback():
            ui_anim_data.update_with(fn_darklight)

        self.upd_data_callback = upd_data_callback
        #|

    def bufn_limit(self):

        m.D_EDITOR["SettingEditor"].open_search("vert_limit", true_ids={"id", "editor"})
        #|
    def bufn_collinear(self):

        make_collinear(r_bm_data(CONTEXT), self.attributes.lock_active_vertex_collinear)
        #|
    def bufn_coplanar(self):

        make_coplanar(r_bm_data(CONTEXT), self.attributes.lock_active_vertex_collinear)
        #|

    def upd_data(self):
        self.upd_data_callback()
        #|
    #|
    #|


m.D_EDITOR.new('MeshEditor', MeshEditor)

def late_import():
    #|
    from .  import ops, prop

    # <<< 1mp (ops
    r_bm_data = ops.r_bm_data
    r_3vert_angle = ops.r_3vert_angle
    make_collinear = ops.make_collinear
    make_coplanar = ops.make_coplanar
    callback_distance = ops.callback_distance
    callback_direction = ops.callback_direction
    callback_u_direction = ops.callback_u_direction
    callback_u_normal = ops.callback_u_normal
    callback_area = ops.callback_area
    callback_angle = ops.callback_angle
    # >>>

    # <<< 1mp (prop
    PpMeshEditor = prop.PpMeshEditor
    PpMeshTab = prop.PpMeshTab
    # >>>

    # <<< 1mp (VMD.block
    block = VMD.block
    Ui = block.Ui
    allot_callback = block.allot_callback
    allot_inout_draw_view = block.allot_inout_draw_view
    wrapper_push = block.wrapper_push
    poll_hard_disable = block.poll_hard_disable
    Title = block.Title
    BlockR = block.BlockR
    BlockFull = block.BlockFull
    ButtonGroup = block.ButtonGroup
    ButtonGroupTitle = block.ButtonGroupTitle
    EdFloat = block.EdFloat
    # >>>

    # <<< 1mp (VMD.m
    m = VMD.m
    P = m.P
    Admin = m.Admin
    BlendDataTemp = m.BlendDataTemp
    update_data_true = m.update_data_true
    # >>>

    # <<< 1mp (VMD.rna
    rna = VMD.rna
    RNA_local_space = rna.RNA_local_space
    r_props_by_rnas = rna.r_props_by_rnas
    # >>>

    # <<< 1mp (VMD.util.com
    com = VMD.util.com
    bin_search_continue = com.bin_search_continue
    N = com.N
    NS = com.NS
    # >>>

    # <<< 1mp (VMD.utilbl.blg
    blg = VMD.utilbl.blg
    GpuRim = blg.GpuRim
    GpuBox_area = blg.GpuBox_area
    GpuScreenDash = blg.GpuScreenDash
    FONT0 = blg.FONT0
    D_SIZE = blg.D_SIZE
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_widget = blg.SIZE_widget
    COL_preview_3d_dash = blg.COL_preview_3d_dash
    COL_preview_3d_dash2 = blg.COL_preview_3d_dash2
    COL_preview_3d_arc = blg.COL_preview_3d_arc
    draw_angle_arc = blg.draw_angle_arc
    # >>>

    # <<< 1mp (VMD.utilbl.mesh
    mesh = VMD.utilbl.mesh
    r_faces_area = mesh.r_faces_area
    r_angle = mesh.r_angle
    r_qdiff = mesh.r_qdiff
    # >>>

    globals().update(locals())
    #|
