import bpy, _bpy, gpu, mathutils, bmesh, math

gpu_matrix_push_pop = gpu.matrix.push_pop
gpu_matrix_multiply_matrix = gpu.matrix.multiply_matrix
gpu_matrix_scale_uniform = gpu.matrix.scale_uniform


# <<< 1mp (mathutils
Vector = mathutils.Vector
# >>>

# <<< 1mp (mathutils.geometry
geometry = mathutils.geometry
normal = geometry.normal
intersect_line_plane = geometry.intersect_line_plane
area_tri = geometry.area_tri
# >>>

# <<< 1mp (bmesh
from_edit_mesh = bmesh.from_edit_mesh
# >>>

# <<< 1mp (math
pi = math.pi
tau = math.tau
sqrt = math.sqrt
degrees = math.degrees
# >>>

from .  import VMD

# <<< 1mp (VMD.blprop
blprop = VMD.blprop
BLPROP_mesh = blprop.BLPROP_mesh
# >>>

# <<< 1mp (VMD.util.deco
deco = VMD.util.deco
assign = deco.assign
# >>>

# <<< 1mp (VMD.util.const
const = VMD.util.const
VEC_00M1 = const.VEC_00M1
VEC_001 = const.VEC_001
VEC_010 = const.VEC_010
# >>>

# <<< 1mp (VMD.userops
userops = VMD.userops
OpsReport = userops.OpsReport
OpsReportModal = userops.OpsReportModal
PollEditMesh = userops.PollEditMesh
GrabCursor = userops.GrabCursor
ModalSlowdownSpeedup = userops.ModalSlowdownSpeedup
modalKeymap = userops.modalKeymap
Bmesh = userops.Bmesh
# >>>

# <<< 1mp (VMD
m = VMD.m
# >>>

CONTEXT = _bpy.context
SpaceView3D = bpy.types.SpaceView3D
T = [None]


def r_bm_data(context):
    bms = {}
    bm_dic = {}
    total_vert_sel = 0
    total_edge_sel = 0
    total_face_sel = 0

    for ob in context.objects_in_mode:
        ob_data = ob.data
        total_vert_sel += ob_data.total_vert_sel
        total_edge_sel += ob_data.total_edge_sel
        total_face_sel += ob_data.total_face_sel

        bm = from_edit_mesh(ob_data)
        verts_sel = [e  for e in bm.verts if e.select]
        edges_sel = [e  for e in bm.edges if e.select]
        faces_sel = [e  for e in bm.faces if e.select]
        bms[ob] = Bmesh(bm, verts_sel, edges_sel, faces_sel)
        bm_dic.update({e: ob  for e in verts_sel})
        bm_dic.update({e: ob  for e in edges_sel})
        bm_dic.update({e: ob  for e in faces_sel})

    verts = []
    edges = []
    faces = []
    for b in bms.values():
        verts += b.verts_sel
        edges += b.edges_sel
        faces += b.faces_sel

    return {
        "bms": bms,
        "bm_dic": bm_dic,
        "total_vert_sel": total_vert_sel,
        "total_edge_sel": total_edge_sel,
        "total_face_sel": total_face_sel,
        "verts": verts,
        "edges": edges,
        "faces": faces,
    }
    #|

def set_face_or_vert3_normal(bm_data, ftd, new_normal,
                    local_space, method_set_normal, lock_active_vertex):

    if ftd["keep_normals_message"] == "" and method_set_normal == "KEEP_NORMALS_OF_OTHER_FACES":
        if local_space:
            old_origin = ftd["old_act_local"]  if lock_active_vertex else ftd["old_origin_local"]
            old_line0 = ftd["old_line0_local"]
            old_line1 = ftd["old_line1_keep_normal_local"]
        else:
            old_origin = ftd["old_act_global"]  if lock_active_vertex else ftd["old_origin_global"]
            old_line0 = ftd["old_line0_global"]
            old_line1 = ftd["old_line1_keep_normal_global"]
    else:
        if local_space:
            old_origin = ftd["old_act_local"]  if lock_active_vertex else ftd["old_origin_local"]
            old_line0 = ftd["old_line0_local"]
            old_line1 = ftd["old_line1_local"]
        else:
            old_origin = ftd["old_act_global"]  if lock_active_vertex else ftd["old_origin_global"]
            old_line0 = ftd["old_line0_global"]
            old_line1 = ftd["old_line1_global"]

    if ftd["method"] == "FACE":
        success, message = set_face_normal(
            bm_data,
            bm_data["faces"][0],
            old_origin,
            old_line0,
            old_line1,
            new_normal,
            local_space,
            keep_shape=(method_set_normal == "KEEP_SHAPE"))
    else:
        success, message = set_verts_normal(
            bm_data,
            bm_data["verts"],
            old_origin,
            old_line0,
            old_line1,
            new_normal,
            local_space,
            keep_shape=(method_set_normal == "KEEP_SHAPE"))

    if method_set_normal == "KEEP_NORMALS_OF_OTHER_FACES" and not message:
        if ftd["keep_normals_message"] != "":
            message = f'Keep Normals skipped: {ftd["keep_normals_message"]}'
    return success, message
    #|
def set_face_normal(bm_data, plane, old_origin, old_line0, old_line1, new_normal, local_space, keep_shape=False):
    ob = bm_data["bm_dic"][plane]
    new_pos = []

    if keep_shape is True:
        v = old_line0[0]
        old_vec = (v - old_origin).normalized()
        intersect = intersect_line_plane(v, v + new_normal, old_origin, new_normal)
        vec = (intersect - old_origin).normalized()

        if local_space:
            q = r_qdiff(normal(loop.vert.co  for loop in plane.loops), new_normal, old_vec, vec)

            for vert, line0 in zip(plane.verts, old_line0):
                vert.co[:] = old_origin + (q @ (line0 - old_origin))
        else:
            mat = ob.matrix_world
            q = r_qdiff(normal(mat @ loop.vert.co  for loop in plane.loops), new_normal, old_vec, vec)
            imat = mat.inverted_safe()
            for vert, line0 in zip(plane.verts, old_line0):
                vert.co[:] = imat @ (old_origin + (q @ (line0 - old_origin)))

    else:
        for line0, line1 in zip(old_line0, old_line1):
            pos = intersect_line_plane(line0, line1, old_origin, new_normal)
            if pos is None:
                return True, "The linked face of the selected face has the same normal as the selected face, abort."
            new_pos.append(pos)


        if local_space:
            for vert, pos in zip(plane.verts, new_pos): vert.co[:] = pos
        else:
            imat = ob.matrix_world.inverted_safe()
            for vert, pos in zip(plane.verts, new_pos): vert.co[:] = imat @ pos

    bm_data["bms"][ob].bm.normal_update()
    ob.data.update()
    return True, ""
    #|
def set_verts_normal(bm_data, verts, old_origin, old_line0, old_line1, new_normal, local_space, keep_shape=False):
    bm_dic = bm_data["bm_dic"]
    new_pos = []

    if keep_shape is True:
        v = old_line0[0]
        old_vec = (v - old_origin).normalized()
        intersect = intersect_line_plane(v, v + new_normal, old_origin, new_normal)
        vec = (intersect - old_origin).normalized()

        if local_space:
            q = r_qdiff(normal(vert.co  for vert in verts), new_normal, old_vec, vec)

            for vert, line0 in zip(verts, old_line0):
                vert.co[:] = old_origin + (q @ (line0 - old_origin))
        else:
            mat = bm_dic[verts[0]].matrix_world
            q = r_qdiff(normal(mat @ vert.co  for vert in verts), new_normal, old_vec, vec)

            imat_lookup = {}
            for vert in verts:
                ob = bm_dic[vert]
                if ob in imat_lookup: continue
                imat_lookup[ob] = ob.matrix_world.inverted_safe()

            for vert, line0 in zip(verts, old_line0):
                vert.co[:] = imat_lookup[bm_dic[vert]] @ (old_origin + (q @ (line0 - old_origin)))
    else:
        for line0, line1 in zip(old_line0, old_line1):
            pos = intersect_line_plane(line0, line1, old_origin, new_normal)
            if pos is None:
                return True, "The linked face of the selected face has the same normal as the selected face, abort."
            new_pos.append(pos)


        if local_space:
            for vert, pos in zip(verts, new_pos): vert.co[:] = pos
        else:
            imat_lookup = {}
            for vert in verts:
                ob = bm_dic[vert]
                if ob in imat_lookup: continue
                imat_lookup[ob] = ob.matrix_world.inverted_safe()

            for vert, pos in zip(verts, new_pos):
                vert.co[:] = imat_lookup[bm_dic[vert]] @ pos

    for ob, bme in bm_data["bms"].items():
        bme.bm.normal_update()
        ob.data.update()
    return True, ""
    #|

def set_distance(bm_data, v0, v1, distance, u_vec_glo, u_vec, local_space=False, invert=False):
    bm_dic = bm_data["bm_dic"]
    if invert:
        v0, v1 = v1, v0
        u_vec_glo = - u_vec_glo
        u_vec = - u_vec

    if local_space:
        v0.co[:] = v1.co + u_vec * distance
    else:
        new_loc = bm_dic[v1].matrix_world @ v1.co + u_vec_glo * distance
        v0.co[:] = bm_dic[v0].matrix_world.inverted_safe() @ new_loc

    ob0 = bm_dic[v0]
    ob1 = bm_dic[v1]
    if ob0 is ob1:
        bm_data["bms"][ob0].bm.normal_update()
        ob0.data.update()
    else:
        bm_data["bms"][ob0].bm.normal_update()
        bm_data["bms"][ob1].bm.normal_update()
        ob0.data.update()
        ob1.data.update()
    #|

def set_direction(bm_data, v0, v1, vec3, local_space=False, invert=False):
    vec3 = Vector(vec3)
    bm_dic = bm_data["bm_dic"]
    if invert:
        v0, v1 = v1, v0
        vec3 = - vec3

    ob = bm_dic[v0]

    if local_space:
        v0.co[:] = v1.co + vec3
    else:
        new_loc = bm_dic[v1].matrix_world @ v1.co + vec3
        v0.co[:] = ob.matrix_world.inverted_safe() @ new_loc

    bm_data["bms"][ob].bm.normal_update()
    ob.data.update()
    #|

def is_single_line(bm_data):
    return bm_data["total_vert_sel"] == bm_data["total_edge_sel"] + 1
    #|

def r_3vert_by_2edge_connect(e0, e1):
    v0, v1 = e0.verts
    v2, v3 = e1.verts
    if v2 is v0: return v1, v0, v3
    if v2 is v1: return v0, v1, v3
    if v3 is v0: return v1, v0, v2
    return v0, v1, v2
    #|
def r_3vert_angle(bm_data): # total_vert_sel == 3
    ob = CONTEXT.object
    try: act = bm_data["bms"][ob].bm.select_history.active
    except: act = None

    if bm_data["total_edge_sel"] == 2:
        edge0, edge1 = bm_data["edges"]
        if act is edge0: edge0, edge1 = edge1, edge0

        v0, v1, v2 = r_3vert_by_2edge_connect(edge0, edge1)
    else:
        v0, v1, v2 = bm_data["verts"]
        try: v_center = bm_data["bms"][ob].bm.select_history[-2]
        except: v_center = None

        if v_center is v0: v1, v0 = v0, v1
        elif v_center is v2: v1, v2 = v2, v1

    if act is v0: v0, v2 = v2, v0
    return v0, v1, v2
    #|

def make_collinear(bm_data, lock_active_vertex=False):
    bm_dic = bm_data["bm_dic"]
    verts = bm_data["verts"]
    verts_co = [bm_dic[v].matrix_world @ v.co  for v in verts]

    if is_single_line(bm_data):
        i0, i1 = r_outer_2vert_by_single_line(verts, bm_data["edges"])
        i0 = verts.index(i0)
        i1 = verts.index(i1)
    else:
        i0, i1 = r_outer_2vert_by_direction(verts_co, r_average_direction(verts_co))

    v0 = verts[i0]
    v1 = verts[i1]
    u_vec = (verts_co[i0] - verts_co[i1]).normalized()

    rot = u_vec.rotation_difference(VEC_00M1)
    rot_inv = rot.inverted()
    pos = rot @ verts_co[i0]
    x, y = pos[0 : 2]

    inv_matrix_dic = {ob: ob.matrix_world.inverted_safe()  for ob in bm_data["bms"]}

    act = None
    if lock_active_vertex:
        try: act = bm_data["bms"][CONTEXT.object].bm.select_history.active
        except: pass
        if act not in verts: act = None

    if act is None:
        for v_co, v in zip(verts_co, verts):
            pos = rot @ v_co
            pos[0] = x
            pos[1] = y
            v.co[:] = inv_matrix_dic[bm_dic[v]] @ (rot_inv @ pos)
    else:
        old_pos = bm_dic[act].matrix_world @ act.co
        pos = rot @ old_pos
        pos[0] = x
        pos[1] = y
        pos = rot_inv @ pos
        offset = old_pos - pos

        for v_co, v in zip(verts_co, verts):
            pos = rot @ v_co
            pos[0] = x
            pos[1] = y
            pos = rot_inv @ pos
            v.co[:] = inv_matrix_dic[bm_dic[v]] @ (pos + offset)

    for bme in bm_data["bms"].values(): bme.bm.normal_update()
    for ob in inv_matrix_dic: ob.data.update()
    #|

def make_coplanar(bm_data, lock_active_vertex=False):
    ftd = OpsSetNormal.r_first_time_data(bm_data)
    if ftd["method"] == "NONE": return

    set_face_or_vert3_normal(
        bm_data,
        ftd,
        ftd["old_normal_global"],
        False,
        "KEEP_NORMALS_OF_OTHER_FACES",
        lock_active_vertex)
    #|

def set_angle(bm_data, v0, v1, v2, angle, local_space=False, invert=False, lock_active_vertex=None):
    if invert: v0, v2 = v2, v0

    bm_dic = bm_data["bm_dic"]
    if local_space:
        verts = [v.co  for v in (v0, v1, v2)]
    else:
        verts = [bm_dic[v].matrix_world @ v.co  for v in (v0, v1, v2)]
    org_co_glo = verts

    u_pos = (verts[0] - verts[1]).normalized()
    length = (verts[1] - verts[2]).length
    u_nor = normal(verts)
    if u_nor == Vector(): u_nor = Vector((0.0, 0.0, 1.0))

    u_vec0, u_vec1 = r_u_pos_by_angle(u_pos, u_nor, angle)
    pos0 = length * u_vec0 + org_co_glo[1]
    pos1 = length * u_vec1 + org_co_glo[1]
    an_0 = r_angle(org_co_glo[2], org_co_glo[1], pos0)
    an_1 = r_angle(org_co_glo[2], org_co_glo[1], pos1)

    if angle % tau < pi:   new_pos = pos0 if an_0 < an_1 else pos1
    else:              new_pos = pos1 if an_0 < an_1 else pos0

    if local_space == False: new_pos = bm_dic[v2].matrix_world.inverted_safe() @ new_pos

    if lock_active_vertex is v2:
        offset = v2.co - new_pos
        new_pos += offset
        v0.co +=  offset
        v1.co += offset
    else:
        v2.co[:] = new_pos

    obs = {bm_dic[v0], bm_dic[v1], bm_dic[v2]}
    bms = bm_data["bms"]
    for ob in obs:
        bms[ob].bm.normal_update()
        ob.data.update()
    #|

def set_face_area(bm_data, ftd, tot_area, local_space=False, lock_active_vertex=False):
    bm_dic = bm_data["bm_dic"]
    verts = sum(([v for v in face.verts]  for face in bm_data["faces"]), [])

    if local_space:
        fac = sqrt(tot_area / ftd["old_area_local"])

        if lock_active_vertex:
            center = ftd["center_act_local"]
            for v, vec in zip(verts, ftd["vecs_act_local"]):
                v.co[:] = fac * vec + center
        else:
            center = ftd["center_local"]
            for v, vec in zip(verts, ftd["vecs_local"]):
                v.co[:] = fac * vec + center
    else:
        fac = sqrt(tot_area / ftd["old_area_global"])
        inv_matrix_dic = {ob: ob.matrix_world.inverted_safe()  for ob in bm_data["bms"]}

        if lock_active_vertex:
            center = ftd["center_act_global"]
            for v, vec in zip(verts, ftd["vecs_act_global"]):
                v.co[:] = inv_matrix_dic[bm_dic[v]] @ (fac * vec + center)
        else:
            center = ftd["center_global"]
            for v, vec in zip(verts, ftd["vecs_global"]):
                v.co[:] = inv_matrix_dic[bm_dic[v]] @ (fac * vec + center)

    for ob, bme in bm_data["bms"].items():
        bme.bm.normal_update()
        ob.data.update()
    #|

def restore_header(self=None):
    MODAL_DRAG_STATE[0] = -1
    CONTEXT.area.header_text_set(None)
    #|
def remove_draw_handler(cls):
    if hasattr(cls, 'DRAW_HANDLER') and cls.DRAW_HANDLER:
        SpaceView3D.draw_handler_remove(cls.DRAW_HANDLER, 'WINDOW')
        cls.DRAW_HANDLER = None
    #|
def add_draw_handler(cls, fn_draw):
    cls.DRAW_HANDLER = SpaceView3D.draw_handler_add(fn_draw, (), 'WINDOW', 'POST_VIEW')
    #|


def callback_distance(option, value):
    self = option["button"]
    if MODAL_DRAG_STATE[0] == 1:
        bm_data, v0, v1, u_vec_glo, u_vec, local_space, invert = T[0]
    else:
        bm_data = r_bm_data(CONTEXT)

        try: act = bm_data["bms"][CONTEXT.object].bm.select_history.active
        except: act = None

        v0, v1 = bm_data["verts"]
        if act is v1: v0, v1 = v1, v0

        bm_dic = bm_data["bm_dic"]

        vec_glo = (bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)
        vec = v0.co - v1.co
        u_vec_glo = vec_glo.normalized()
        u_vec = vec.normalized()
        local_space = option["r_local_space"]()
        invert = self.pp.vert_invert

        T[0] = [bm_data, v0, v1, u_vec_glo, u_vec, local_space, invert]

    set_distance(bm_data, v0, v1, value, u_vec_glo, u_vec, local_space, invert)

    if local_space:
        self.pp.distance = (v0.co - v1.co).length
    else:
        bm_dic = bm_data["bm_dic"]
        self.pp.distance = ((bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)).length

    if value < 0: self.pp.distance *= -1
    self.upd_data()
    #|
def callback_direction(option, value):
    self = option["button"]
    if hasattr(value, "__len__"): pass
    else:
        e = self.pp.direction[:]
        e[self.focus_element[0]] = value
        value = e

    if MODAL_DRAG_STATE[0] == 1:
        bm_data, v0, v1, local_space = T[0]
    else:
        bm_data = r_bm_data(CONTEXT)

        try: act = bm_data["bms"][CONTEXT.object].bm.select_history.active
        except: act = None

        v0, v1 = bm_data["verts"]
        if act is v1: v0, v1 = v1, v0

        local_space = option["r_local_space"]()
        if self.pp.vert_invert: v0, v1 = v1, v0

        T[0] = [bm_data, v0, v1, local_space]

    set_direction(bm_data, v0, v1, value, local_space, False)

    if local_space:
        self.pp.direction[:] = v0.co - v1.co
    else:
        bm_dic = bm_data["bm_dic"]
        self.pp.direction[:] = (bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)

    self.upd_data()
    #|
def callback_u_direction(option, value):
    self = option["button"]

    bm_data = r_bm_data(CONTEXT)

    try: act = bm_data["bms"][CONTEXT.object].bm.select_history.active
    except: act = None

    v0, v1 = bm_data["verts"]
    if act is v1: v0, v1 = v1, v0

    local_space = option["r_local_space"]()
    if self.pp.vert_invert: v0, v1 = v1, v0

    if local_space:
        distance = (v0.co - v1.co).length
    else:
        bm_dic = bm_data["bm_dic"]
        distance = ((bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)).length

    set_direction(bm_data, v0, v1, Vector(value) * distance, local_space, False)

    if local_space:
        self.pp.u_direction[:] = (v0.co - v1.co).normalized()
    else:
        bm_dic = bm_data["bm_dic"]
        self.pp.u_direction[:] = ((bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)).normalized()

    self.upd_data()
    #|

def callback_u_normal(option, value):
    self = option["button"]
    if hasattr(value, "__len__"):
        self.pp.u_normal[:] = value
    else:
        self.pp.u_normal[self.focus_element[0]] = value

    bm_data = r_bm_data(CONTEXT)
    local_space = option["r_local_space"]()
    method_set_normal = self.pp.method_set_normal
    lock_active_vertex = self.pp.lock_active_vertex
    ftd = OpsSetNormal.r_first_time_data(bm_data)
    T[0] = [bm_data, local_space, method_set_normal, lock_active_vertex, ftd]

    if ftd["method"] == "NONE":
        report("Need select 1 face or 3 vertices, abort")
        return

    set_face_or_vert3_normal(
        bm_data,
        ftd,
        Vector(self.pp.u_normal),
        local_space,
        method_set_normal,
        lock_active_vertex)

    update_data()
    #|
def callback_area(option, value):
    self = option["button"]
    if MODAL_DRAG_STATE[0] == 1:
        bm_data, local_space, lock_active_vertex, ftd = T[0]
    else:
        bm_data = r_bm_data(CONTEXT)
        local_space = option["r_local_space"]()
        lock_active_vertex = self.pp.lock_active_vertex_collinear
        ftd = OpsSetArea.r_first_time_data(bm_data)
        T[0] = [bm_data, local_space, lock_active_vertex, ftd]

    if self.pp.area < 0.0: self.pp.area = 0.0

    try:
        set_face_area(
            bm_data,
            ftd,
            self.pp.area,
            local_space,
            lock_active_vertex)
    except: return

    self.upd_data()
    #|
def callback_angle(option, value):
    self = option["button"]
    if MODAL_DRAG_STATE[0] == 1:
        bm_data, local_space, lock_active_vertex, org_coord = T[0]
    else:
        bm_data = r_bm_data(CONTEXT)
        local_space = option["r_local_space"]()
        lock_active_vertex = self.pp.lock_active_vertex_collinear
        v0, v1, v2 = r_3vert_angle(bm_data)
        org_coord = v0.co.copy(), v1.co.copy(), v2.co.copy()
        T[0] = [bm_data, local_space, lock_active_vertex, org_coord]

    try: act = bm_data["bms"][CONTEXT.object].bm.select_history.active
    except: act = None
    lock_active_vertex = act  if lock_active_vertex else None
    v0, v1, v2 = r_3vert_angle(bm_data)
    v0.co[:] = org_coord[0]
    v1.co[:] = org_coord[1]
    v2.co[:] = org_coord[2]

    set_angle(bm_data, v0, v1, v2, self.pp.angle, local_space, False, lock_active_vertex)

    self.upd_data()
    #|


OPS_SLOTS = (
    'option',
    'pp',
    'mou',
    'mou_limit',
    'tag_redraw',
    'header_text_set',
    'keymaps',
    'trigger_slowdown',
    'trigger_speedup',
    'drag_speed_fast',
    'drag_speed_slow')

def c_fin(self, context, event, cancel=False):
    restore_header()
    remove_draw_handler(self.__class__)

    if cancel is True:
        bpy.ops.ed.undo()
    #|
def c_except_with(self):
    restore_header()
    remove_draw_handler(self.__class__)
    #|


@ assign(
    fin = c_fin,
    except_with = c_except_with)
class OpsSetDistance(OpsReportModal, PollEditMesh, GrabCursor, ModalSlowdownSpeedup, modalKeymap(
    {"cancel": {"RIGHTMOUSE"}, "confirm": {"LEFTMOUSE", "RET", "NUMPAD_ENTER"}, "slowdown": {"shift"}, "speedup": {"ctrl"}, "local_space": {"S"}, "invert": {"I"}},
    # <<< 1precompile (type="modalKeymap")
    "{'cancel': ['RIGHTMOUSE'], 'confirm': ['LEFTMOUSE', 'RET', 'NUMPAD_ENTER'], 'slowdown': ['shift'], 'speedup': ['ctrl'], 'local_space': ['S'], 'invert': ['I']}"
    # >>>
    )):
    __slots__ = OPS_SLOTS

    bl_idname = "mesh.vmd_vert_distance"
    bl_label = "VMD Set Vertex Distance"
    bl_options = {"REGISTER", "UNDO", "GRAB_CURSOR", "BLOCKING"}
    bl_description = "Set distance between 2 vertices"

    distance: BLPROP_mesh["vertex_distance"]
    local_space: BLPROP_mesh["local_space"]
    invert: BLPROP_mesh["invert_vertex"]

    def i_invoke(self, context, event):
        if not self.invoke_default:
            self.execute(context)
            return {'FINISHED'}
        if self.create_option(context, push=True) is False: return {'CANCELLED'}

        self.keymap_load()
        self.get_trigger_slowdown_speedup()
        keymaps = self.keymaps
        if "local_space" not in keymaps:
            keymaps["local_space"] = set()
        if "invert" not in keymaps:
            keymaps["invert"] = set()

        area = context.area
        self.header_text_set = area.header_text_set
        self.tag_redraw = area.tag_redraw

        self.invoke_grab_cursor(context, event)
        context.window_manager.modal_handler_add(self)

        self.set_header()
        # <<< 1copy (0AreaBlockTabMeshEditor_draw_distance,, $$)
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
        # >>>

        add_draw_handler(self.__class__, inside_draw_distance)
        return {'RUNNING_MODAL'}
        #|

    def i_modal(self, context, event):
        self.tag_redraw()
        keymaps = self.keymaps
        evt_type = event.type

        if evt_type == 'MOUSEMOVE': pass
        elif evt_type == 'ESC' or evt_type in keymaps["cancel"]:
            self.fin(context, event, cancel=True)
            return {'CANCELLED'}
        elif evt_type == 'RET' or evt_type in keymaps["confirm"]:
            self.fin(context, event)
            return {'FINISHED'}
        elif evt_type in keymaps["local_space"] and event.value == "PRESS":
            self.local_space = not self.local_space
            old_distance = self.distance

            MODAL_DRAG_STATE[0] = 0
            callback_distance(self.option, 1000.0)
            MODAL_DRAG_STATE[0] = 1
            self.distance = old_distance
        elif evt_type in keymaps["invert"] and event.value == "PRESS":
            self.pp.vert_invert = not self.pp.vert_invert
            old_distance = self.distance

            MODAL_DRAG_STATE[0] = 0
            callback_distance(self.option, 1000.0)
            MODAL_DRAG_STATE[0] = 1
            self.distance = old_distance
        else: return {'RUNNING_MODAL'}

        x, y = self.mou
        dx = event.mouse_x - x
        dy = event.mouse_y - y

        offset = dx  if abs(dx) > abs(dy) else dy
        if abs(offset) > self.mou_limit:
            self.mou[:] = event.mouse_x, event.mouse_y
            return {'RUNNING_MODAL'}

        if self.trigger_slowdown(event):
            self.distance += offset * self.drag_speed_slow
        elif self.trigger_speedup(event):
            self.distance += offset * self.drag_speed_fast
        else:
            self.distance += offset * self.drag_speed
        callback_distance(self.option, self.distance)

        self.set_header()
        self.mou[:] = event.mouse_x, event.mouse_y
        return {'RUNNING_MODAL'}
        #|

    def i_execute(self, context):
        if hasattr(self, 'option'):
            self.pp.vert_invert = self.invert
        else:
            if self.create_option(context) is False: return {'CANCELLED'}

        callback_distance(self.option, self.distance)
        MODAL_DRAG_STATE[0] = -1
        return {'FINISHED'}
        #|

    def create_option(self, context, push=False):
        bm_data = r_bm_data(context)
        if bm_data["total_vert_sel"] != 2:
            self.report({"WARNING"}, "Need to select only 2 vertices")
            return False

        pp = PpMeshTab(None)
        self.pp = pp

        pp.vert_invert = self.invert

        self.option = {
            "button": self,
            "r_local_space": lambda: self.local_space
        }

        try: act_vert = bm_data["bms"][context.object].bm.select_history.active
        except: act_vert = None

        v0, v1 = bm_data["verts"]
        if act_vert is v1: v0, v1 = v1, v0

        if self.local_space:
            self.distance = (v0.co - v1.co).length
        else:
            bm_dic = bm_data["bm_dic"]
            self.distance = ((bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)).length

        if push is True:
            bpy.ops.ed.undo_push(message=f'{self.bl_label} [Start]')

        MODAL_DRAG_STATE[0] = 0
        callback_distance(self.option, self.distance)
        MODAL_DRAG_STATE[0] = 1
        return True
        #|
    def set_header(self):
        self.header_text_set(f'Distance :  {rs_format_float6(self.pp.distance)}        {"Local"  if self.local_space else "Global"} Space        {"Invert Vertex"  if self.pp.vert_invert else ""}')
        #|
    def upd_data(self):
        self.distance = self.pp.distance
        #|
    #|
    #|

class OpsSetDirection(OpsReport, PollEditMesh):
    __slots__ = 'is_first_time'

    bl_idname = "mesh.vmd_vert_direction"
    bl_label = "VMD Set Vertex Direction"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Set direction of 2 vertices"

    direction: BLPROP_mesh["line_direction"]
    local_space: BLPROP_mesh["local_space"]
    invert: BLPROP_mesh["invert_vertex"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.is_first_time = True
        #|

    def i_execute(self, context):
        bm_data = r_bm_data(context)
        if bm_data["total_vert_sel"] != 2:
            self.report({"WARNING"}, "Need to select only 2 vertices")
            return {'CANCELLED'}

        try: act = bm_data["bms"][context.object].bm.select_history.active
        except: act = None

        v0, v1 = bm_data["verts"]
        if act is v1: v0, v1 = v1, v0

        if self.is_first_time is True:
            self.is_first_time = False
            is_first_time = True

            bm_dic = bm_data["bm_dic"]

            vec_glo = (bm_dic[v0].matrix_world @ v0.co) - (bm_dic[v1].matrix_world @ v1.co)
            vec = v0.co - v1.co

            self.direction = vec  if self.local_space else vec_glo
        else:
            is_first_time = False

        set_direction(bm_data, v0, v1, self.direction, self.local_space, self.invert)

        for bm in bm_data["bms"].values(): bm.bm.free()
        return {'FINISHED'}
        #|
    #|
    #|

class OpsSetNormal(OpsReport, PollEditMesh):
    __slots__ = 'first_time_data'

    bl_idname = "mesh.vmd_normal"
    bl_label = "VMD Set Normal"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Set normal"

    normal: BLPROP_mesh["face_normal"]
    local_space: BLPROP_mesh["local_space"]
    method_set_normal: BLPROP_mesh["method_set_normal"]
    lock_active_vertex: BLPROP_mesh["lock_active_vertex"]

    @staticmethod
    def r_first_time_data(bm_data):
        if bm_data["total_face_sel"] == 1 and bm_data["total_vert_sel"] == len(bm_data["faces"][0].verts):
            plane = bm_data["faces"][0]
            ob = bm_data["bm_dic"][plane]
            mat = ob.matrix_world

            old_normal_local = normal(loop.vert.co  for loop in plane.loops)
            old_normal_global = normal(mat @ loop.vert.co  for loop in plane.loops)

            bmtemp, face = r_bmface_copy(plane)
            for v in face.verts: v.co[:] = mat @ v.co
            old_origin_global = face.calc_center_median()
            old_origin_local = plane.calc_center_median()

            old_line0_global = [v.co.copy()  for v in face.verts]
            old_line0_local = [v.co.copy()  for v in plane.verts]
            old_line1_global = [v + old_normal_global  for v in old_line0_global]
            old_line1_local = [v + old_normal_local  for v in old_line0_local]
            bmtemp.free()

            act_vert = None
            try: act_vert = bm_data["bms"][ob].bm.select_history.active
            except: pass
            if act_vert not in plane.verts: act_vert = None
            if act_vert is None:
                old_act_local = old_origin_local
                old_act_global = old_origin_global
            else:
                old_act_local = act_vert.co.copy()
                old_act_global = mat @ act_vert.co

            method = "FACE"
            old_line1_keep_normal_global = []
            old_line1_keep_normal_local = []

            def r_keep_normals_message():
                plane_edges = plane.edges
                lines = {}

                for vert in plane.verts:
                    ll_faces = len(vert.link_faces)

                    if ll_faces == 1:   continue
                    if ll_faces > 3:
                        return "Some vertices in selected face have more than 3 linked faces"

                    if ll_faces == 2:
                        faces = vert.link_faces
                        face = faces[1 if faces[0] is plane else 0]
                        plane_edges = plane.edges
                        share_edge = set(plane_edges).intersection(face.edges)
                        if len(share_edge) != 1:
                            return "2 of the linked faces of the vertices in the selected face have no or more than one shared edge"

                        share_edge, = share_edge
                        v0, v1 = share_edge.verts

                        for edge in face.edges:
                            if edge == share_edge: continue
                            if v0 in edge.verts:
                                lines[v0] = edge
                            elif v1 in edge.verts:
                                lines[v1] = edge

                    elif ll_faces == 3:
                        faces = vert.link_faces
                        if faces[0] == plane:
                            face1 = faces[1]
                            face2 = faces[2]
                        elif faces[1] == plane:
                            face1 = faces[0]
                            face2 = faces[2]
                        else:
                            face1 = faces[0]
                            face2 = faces[1]

                        check_connect_plane = False
                        check_connect_other = False

                        for e in face1.edges:
                            if plane in e.link_faces:
                                check_connect_plane = True
                            elif face2 in e.link_faces:
                                check_connect_other = True
                                line = e

                        if check_connect_plane is False or check_connect_other is False:
                            return "The 3 linked faces of a vertice in the selected face are not connected, abort."

                        lines[vert] = line

                for i, vert in enumerate(plane.verts):
                    if vert in lines:
                        line = lines[vert]
                        if vert is line.verts[0]: v0, v1 = line.verts
                        else: v1, v0 = line.verts

                        old_line1_keep_normal_local.append(v1.co.copy())
                        old_line1_keep_normal_global.append(mat @ v1.co)
                    else:
                        old_line1_keep_normal_local.append(old_line1_local[i])
                        old_line1_keep_normal_global.append(old_line1_global[i])

                return ""
        else:
            if bm_data["total_vert_sel"] < 3: return {'method': "NONE"}

            verts = bm_data["verts"]
            bm_dic = bm_data["bm_dic"]

            old_normal_local = normal(v.co  for v in verts)
            old_normal_global = normal(bm_dic[v].matrix_world @ v.co  for v in verts)

            old_line0_local = [v.co.copy()  for v in verts]
            bmtemp, face = r_bmface_new(old_line0_local)
            old_origin_local = face.calc_center_median()
            old_line1_local = [v + old_normal_local  for v in old_line0_local]
            bmtemp.free()

            old_line0_global = [bm_dic[v].matrix_world @ v.co  for v in verts]
            bmtemp, face = r_bmface_new(old_line0_global)
            old_origin_global = face.calc_center_median()
            old_line1_global = [v + old_normal_global  for v in old_line0_global]
            bmtemp.free()

            act_vert = None
            try: act_vert = bm_data["bms"][bm_dic[verts[0]]].bm.select_history.active
            except: pass
            if act_vert not in verts: act_vert = None
            if act_vert is None:
                old_act_local = old_origin_local
                old_act_global = old_origin_global
            else:
                old_act_local = act_vert.co.copy()
                old_act_global = bm_dic[act_vert].matrix_world @ act_vert.co

            method = "VERT3"
            old_line1_keep_normal_global = []
            old_line1_keep_normal_local = []

            def r_keep_normals_message(): return "Available when selecting a face"

        return {
            'old_normal_local': old_normal_local,
            'old_normal_global': old_normal_global,
            'old_line0_local': old_line0_local,
            'old_line0_global': old_line0_global,
            'old_line1_local': old_line1_local,
            'old_line1_global': old_line1_global,
            'old_origin_local': old_origin_local,
            'old_origin_global': old_origin_global,
            'old_act_local': old_act_local,
            'old_act_global': old_act_global,
            'method': method,
            'keep_normals_message': r_keep_normals_message(),
            'old_line1_keep_normal_global': old_line1_keep_normal_global,
            'old_line1_keep_normal_local': old_line1_keep_normal_local,
        }
        #|

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.first_time_data = None
        #|

    def i_execute(self, context):
        bm_data = r_bm_data(context)

        def fin(success, message):
            if success:
                if message: self.report({"INFO"}, message)
                for bm in bm_data["bms"].values(): bm.bm.free()
                return {'FINISHED'}
            else:
                if message: self.report({"WARNING"}, message)
                for bm in bm_data["bms"].values(): bm.bm.free()
                return {'CANCELLED'}

        if self.first_time_data is None:
            ftd = self.r_first_time_data(bm_data)
            self.first_time_data = ftd

            if ftd["method"] == "NONE":
                success = False
                message = "Need select 1 face or 3 vertices, abort"
                return fin(success, message)
            if ftd["method"] == "VERT3": self.method_set_normal = "KEEP_SHAPE"

            self.normal[:] = ftd["old_normal_local"  if self.local_space else "old_normal_global"]
            # return fin(True, "")

        ftd = self.first_time_data
        if ftd["method"] == "NONE":
            success = False
            message = "Need select 1 face or 3 vertices, abort"
        else:
            success, message = set_face_or_vert3_normal(
                bm_data,
                ftd,
                self.normal,
                self.local_space,
                self.method_set_normal,
                self.lock_active_vertex)

        return fin(success, message)
        #|
    #|
    #|

class OpsCollinear(OpsReport, PollEditMesh):
    __slots__ = ()

    bl_idname = "mesh.vmd_collinear"
    bl_label = "VMD Collinear"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Make Collinear"

    lock_active_vertex: BLPROP_mesh["lock_active_vertex"]

    def i_execute(self, context):
        bm_data = r_bm_data(context)
        total_vert_sel = bm_data["total_vert_sel"]
        if total_vert_sel <= 2: return {'CANCELLED'}

        make_collinear(bm_data, lock_active_vertex=self.lock_active_vertex)

        for bm in bm_data["bms"].values(): bm.bm.free()
        return {'FINISHED'}
        #|
    #|
    #|

class OpsCoplanar(OpsReport, PollEditMesh):
    __slots__ = ()

    bl_idname = "mesh.vmd_coplanar"
    bl_label = "VMD Coplanar"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Make Coplanar"

    lock_active_vertex: BLPROP_mesh["lock_active_vertex"]

    def i_execute(self, context):
        bm_data = r_bm_data(context)
        total_vert_sel = bm_data["total_vert_sel"]
        if total_vert_sel <= 3: return {'CANCELLED'}

        make_coplanar(bm_data, self.lock_active_vertex)

        for bm in bm_data["bms"].values(): bm.bm.free()
        return {'FINISHED'}
        #|
    #|
    #|

@ assign(
    fin = c_fin,
    except_with = c_except_with)
class OpsSetAngle(OpsReportModal, PollEditMesh, GrabCursor, ModalSlowdownSpeedup, modalKeymap(
    {"cancel": {"RIGHTMOUSE"}, "confirm": {"LEFTMOUSE", "RET", "NUMPAD_ENTER"}, "slowdown": {"shift"}, "speedup": {"ctrl"}, "local_space": {"S"}, "lock_active": {"Q"}},
    # <<< 1precompile (type="modalKeymap")
    "{'cancel': ['RIGHTMOUSE'], 'confirm': ['LEFTMOUSE', 'RET', 'NUMPAD_ENTER'], 'slowdown': ['shift'], 'speedup': ['ctrl'], 'local_space': ['S'], 'lock_active': ['Q']}"
    # >>>
    )):
    __slots__ = OPS_SLOTS

    bl_idname = "mesh.vmd_angle"
    bl_label = "VMD Set Angle"
    bl_options = {"REGISTER", "UNDO", "GRAB_CURSOR", "BLOCKING"}
    bl_description = "Set included angle"

    angle: BLPROP_mesh["included_angle"]
    local_space: BLPROP_mesh["local_space"]
    lock_active_vertex: BLPROP_mesh["lock_active_vertex"]

    def i_invoke(self, context, event):
        if not self.invoke_default:
            self.execute(context)
            return {'FINISHED'}
        if self.create_option(context, push=True) is False: return {'CANCELLED'}

        self.keymap_load()
        self.get_trigger_slowdown_speedup()
        keymaps = self.keymaps
        if "local_space" not in keymaps:
            keymaps["local_space"] = set()
        # if "invert" not in keymaps:
        #     keymaps["invert"] = set()
        if "lock_active" not in keymaps:
            keymaps["lock_active"] = set()

        area = context.area
        self.header_text_set = area.header_text_set
        self.tag_redraw = area.tag_redraw

        self.invoke_grab_cursor(context, event)
        context.window_manager.modal_handler_add(self)

        self.set_header()
        # <<< 1copy (0AreaBlockTabMeshEditor_draw_angle,, $$)
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
        # >>>

        add_draw_handler(self.__class__, inside_draw_angle)
        return {'RUNNING_MODAL'}
        #|

    def i_modal(self, context, event):
        self.tag_redraw()
        keymaps = self.keymaps
        evt_type = event.type

        if evt_type == 'MOUSEMOVE': pass
        elif evt_type == 'ESC' or evt_type in keymaps["cancel"]:
            self.fin(context, event, cancel=True)
            return {'CANCELLED'}
        elif evt_type == 'RET' or evt_type in keymaps["confirm"]:
            self.fin(context, event)
            return {'FINISHED'}
        elif evt_type in keymaps["local_space"] and event.value == "PRESS":
            self.local_space = not self.local_space
            old_angle = self.pp.angle
            self.pp.angle = 2.0

            MODAL_DRAG_STATE[0] = 0
            callback_angle(self.option, None)
            MODAL_DRAG_STATE[0] = 1
            self.pp.angle = old_angle
        elif evt_type in keymaps["lock_active"] and event.value == "PRESS":
            self.pp.lock_active_vertex_collinear = not self.pp.lock_active_vertex_collinear
            old_angle = self.pp.angle
            self.pp.angle = 2.0

            MODAL_DRAG_STATE[0] = 0
            callback_angle(self.option, None)
            MODAL_DRAG_STATE[0] = 1
            self.pp.angle = old_angle
        else: return {'RUNNING_MODAL'}

        x, y = self.mou
        dx = event.mouse_x - x
        dy = event.mouse_y - y

        offset = dx  if abs(dx) > abs(dy) else dy
        if abs(offset) > self.mou_limit:
            self.mou[:] = event.mouse_x, event.mouse_y
            return {'RUNNING_MODAL'}

        if self.trigger_slowdown(event):
            self.pp.angle += offset * self.drag_speed_slow
        elif self.trigger_speedup(event):
            self.pp.angle += offset * self.drag_speed_fast
        else:
            self.pp.angle += offset * self.drag_speed
        callback_angle(self.option, None)

        self.set_header()
        self.mou[:] = event.mouse_x, event.mouse_y
        return {'RUNNING_MODAL'}
        #|

    def i_execute(self, context):
        if hasattr(self, 'option'):
            pp = self.pp
            pp.angle = self.angle
            pp.lock_active_vertex_collinear = self.lock_active_vertex
        else:
            if self.create_option(context) is False: return {'CANCELLED'}

        callback_angle(self.option, None)
        MODAL_DRAG_STATE[0] = -1
        return {'FINISHED'}
        #|

    def create_option(self, context, push=False):
        bm_data = r_bm_data(context)
        if bm_data["total_vert_sel"] != 3:
            self.report({"WARNING"}, "3 vertices need to be selected")
            return False

        pp = PpMeshTab(None)
        self.pp = pp

        # pp.vert_invert = self.invert
        pp.lock_active_vertex_collinear = self.lock_active_vertex

        self.option = {
            "button": self,
            "r_local_space": lambda: self.local_space
        }

        v0, v1, v2 = r_3vert_angle(bm_data)

        if self.local_space:
            self.pp.angle = r_angle(v0.co, v1.co, v2.co)
        else:
            bm_dic = bm_data["bm_dic"]
            self.pp.angle = r_angle(
                bm_dic[v0].matrix_world @ v0.co,
                bm_dic[v1].matrix_world @ v1.co,
                bm_dic[v2].matrix_world @ v2.co)

        if push is True:
            bpy.ops.ed.undo_push(message=f'{self.bl_label} [Start]')

        MODAL_DRAG_STATE[0] = 0
        callback_angle(self.option, None)
        MODAL_DRAG_STATE[0] = 1
        return True
        #|
    def set_header(self):
        self.header_text_set(f'Angle :  {rs_format_float6(self.angle)}        {rs_format_float6(degrees(self.angle))}°        {"Local"  if self.local_space else "Global"} Space        {"Lock Active"  if self.pp.lock_active_vertex_collinear else ""}')
        #|
    def upd_data(self):
        self.angle = self.pp.angle
        #|
    #|
    #|

class OpsSetArea(OpsReport, PollEditMesh):
    __slots__ = 'first_time_data'

    bl_idname = "mesh.vmd_area"
    bl_label = "VMD Set Area"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Set face area"

    tot_area: BLPROP_mesh["tot_area"]
    local_space: BLPROP_mesh["local_space"]
    lock_active_vertex: BLPROP_mesh["lock_active_vertex"]

    @staticmethod
    def r_first_time_data(bm_data):
        bm_dic = bm_data["bm_dic"]
        faces = bm_data["faces"]
        face_verts = sum(([v for v in face.verts]  for face in faces), [])
        face_verts_global_co = [bm_dic[v].matrix_world @ v.co  for v in face_verts]

        center_local = r_median([v.co  for v in face_verts])
        center_global = r_median(face_verts_global_co)

        vecs_local = [v.co - center_local  for v in face_verts]
        vecs_global = [co - center_global  for co in face_verts_global_co]

        old_area_local = sum(face.calc_area()  for face in faces)
        old_area_global = r_faces_area(faces, bm_dic)

        act_vert = None
        try: act_vert = bm_data["bms"][CONTEXT.object].bm.select_history.active
        except: pass
        if act_vert not in face_verts: act_vert = None
        if act_vert is None:
            center_act_local = center_local
            center_act_global = center_global
            vecs_act_local = vecs_local
            vecs_act_global = vecs_global
        else:
            center_act_local = act_vert.co.copy()
            center_act_global = bm_dic[act_vert].matrix_world @ act_vert.co
            vecs_act_local = [v.co - center_act_local  for v in face_verts]
            vecs_act_global = [co - center_act_global  for co in face_verts_global_co]

        return {
            'center_local': center_local,
            'center_global': center_global,
            'center_act_local': center_act_local,
            'center_act_global': center_act_global,
            'vecs_local': vecs_local,
            'vecs_global': vecs_global,
            'vecs_act_local': vecs_act_local,
            'vecs_act_global': vecs_act_global,
            'old_area_local': old_area_local,
            'old_area_global': old_area_global,
        }
        #|

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.first_time_data = None
        #|

    def i_execute(self, context):
        bm_data = r_bm_data(context)
        if bm_data["total_face_sel"] < 1:
            self.report({"WARNING"}, "Need to select at least 1 face")
            return {'CANCELLED'}

        if self.first_time_data is None:
            ftd = self.r_first_time_data(bm_data)
            self.first_time_data = ftd
            self.tot_area = ftd["old_area_local"  if self.local_space else "old_area_global"]
        else:
            try:
                set_face_area(
                    bm_data,
                    self.first_time_data,
                    self.tot_area,
                    self.local_space,
                    self.lock_active_vertex)
            except: pass

        for bm in bm_data["bms"].values(): bm.bm.free()
        return {'FINISHED'}
        #|
    #|
    #|


m.OPERATORS += [
    OpsSetDistance,
    OpsSetDirection,
    OpsSetNormal,
    OpsCollinear,
    OpsCoplanar,
    OpsSetAngle,
    OpsSetArea,
]

def late_import():
    from .  import prop
    # <<< 1mp (prop
    PpMeshTab = prop.PpMeshTab
    # >>>

    # <<< 1mp (VMD.util.com
    com = VMD.util.com
    rs_format_float6 = com.rs_format_float6
    # >>>

    # <<< 1mp (VMD.utilbl.mesh
    mesh = VMD.utilbl.mesh
    r_median = mesh.r_median
    r_average_direction = mesh.r_average_direction
    r_outer_2vert_by_direction = mesh.r_outer_2vert_by_direction
    r_outer_2vert_by_single_line = mesh.r_outer_2vert_by_single_line
    r_next_vert_by_edge = mesh.r_next_vert_by_edge
    r_angle = mesh.r_angle
    r_u_pos_by_angle = mesh.r_u_pos_by_angle
    r_vert_area = mesh.r_vert_area
    r_bmface_copy = mesh.r_bmface_copy
    r_bmface_new = mesh.r_bmface_new
    r_faces_area = mesh.r_faces_area
    r_qdiff = mesh.r_qdiff
    is_2edge_connect = mesh.is_2edge_connect
    # >>>

    # <<< 1mp (VMD.block
    block = VMD.block
    MODAL_DRAG_STATE = block.MODAL_DRAG_STATE
    # >>>

    # <<< 1mp (VMD.m
    m = VMD.m
    update_data = m.update_data
    # >>>

    # <<< 1mp (VMD.utilbl.blg
    blg = VMD.utilbl.blg
    GpuScreenDash = blg.GpuScreenDash
    COL_preview_3d_dash = blg.COL_preview_3d_dash
    COL_preview_3d_dash2 = blg.COL_preview_3d_dash2
    COL_preview_3d_arc = blg.COL_preview_3d_arc
    report = blg.report
    draw_angle_arc = blg.draw_angle_arc
    # >>>

    globals().update(locals())
    #|
