import bpy, bmesh, mathutils, math

Vector = mathutils.Vector
normal = mathutils.geometry.normal

# <<< 1mp (math
sin = math.sin
cos = math.cos
asin = math.asin
pi = math.pi
# >>>

from ..  import util

r_compose = util.algebra.r_compose

# <<< 1mp (util.const
const = util.const
TUP_111 = const.TUP_111
VEC_00M1 = const.VEC_00M1
VEC_010 = const.VEC_010
ROT_00M1_111U = const.ROT_00M1_111U
ROT_00M1_111U_inv = const.ROT_00M1_111U_inv
# >>>

VECTOR_0a10 = Vector((0, 1, 0))
VECTOR_00m1 = Vector((0, 0, -1))
ROT_DIF_VECTOR_00m1_111 = VECTOR_00m1.rotation_difference(Vector((1, 1, 1)).normalized())
ROT_DIF_VECTOR_00m1_111_invert = ROT_DIF_VECTOR_00m1_111.inverted()


def add_light(loc, v0, v1, wi, nor, ty="AREA", shape="RECTANGLE"):
    vec_x = v1 - v0
    wi_y = vec_x.length
    vec_x.normalize()

    rot = VEC_00M1.rotation_difference(nor)
    rot2 = (rot @ VEC_010).rotation_difference(vec_x)

    if nor.to_tuple(4) != (rot2 @ rot @ VEC_00M1).to_tuple(4):
        nor = ROT_00M1_111U @ nor
        vec_x = ROT_00M1_111U @ vec_x
        rot = VEC_00M1.rotation_difference(nor)
        rot2 = (rot @ VEC_010).rotation_difference(vec_x)
        rot2 = ROT_00M1_111U_inv @ rot2

    bpy.ops.object.light_add(type=ty, align='WORLD')
    light = bpy.context.object
    light.matrix_world = r_compose(loc, rot2 @ rot, TUP_111)
    light.data.shape = shape
    light.data.size = wi
    light.data.size_y = wi_y
    return light

def r_bmface_copy(bmface):
    bmtemp = bmesh.new()
    verts = bmtemp.verts

    for loop in bmface.loops:
        verts.new(loop.vert.co)

    face = bmtemp.faces.new(verts)
    return bmtemp, face
    #|
def r_bmface_new(vertsco):
    bmtemp = bmesh.new()
    verts = bmtemp.verts

    for v in vertsco:
        verts.new(v)

    face = bmtemp.faces.new(verts)
    return bmtemp, face
    #|

def r_far_vert2(bm_verts, center_co):
    furthest_v = None
    far_v = None
    furthest = -1.0
    far = -1.0

    for v in bm_verts:
        length = (v.co - center_co).length
        if length > far:
            if length > furthest:
                far_v = furthest_v
                far = furthest
                furthest_v = v
                furthest = length
            else:
                far_v = v
                far = length

    return far_v, furthest_v
    #|

def r_median(verts):
    return sum(verts, Vector()) / len(verts)
    #|
def r_average_direction(verts):
    center = r_median(verts)
    vec = Vector()

    for v in verts:
        vec = (center - v + vec) * 0.5

    return vec
    #|
def r_outer_2vert_by_direction(verts, direction):
    direction = direction.normalized()
    rot = VEC_00M1.rotation_difference(direction)

    z_co = [(rot @ v)[2]  for v in verts]
    range0 = range(len(z_co))
    return min(range0, key=z_co.__getitem__), max(range0, key=z_co.__getitem__)
    #|
def r_outer_2vert_by_single_line(bm_verts, bm_edges):
    v0 = None
    for v in bm_verts:
        if len([e  for e in v.link_edges  if e in bm_edges]) >= 2: continue
        if v0 is None: v0 = v
        else:
            v1 = v
            break

    return v0, v1
    #|
def r_next_vert_by_edge(edge, bm_vert):
    if edge.verts[0] is bm_vert: return edge.verts[1]
    return edge.verts[0]
    #|
def r_angle(v0, v_center, v1):
    vec1 = (v0 - v_center).normalized()
    vec2 = (v1 - v_center).normalized()
    if vec1.dot(vec2) >= 0.0:
        return 2.0 * asin((vec1 - vec2).length / 2.0)
    return pi - 2.0 * asin((vec1 + vec2).length / 2.0)
    #|
def r_u_pos_by_angle(u_pos, u_nor, angle):
    rot = VECTOR_00m1.rotation_difference(u_nor)
    rot2 = (rot @ VECTOR_0a10).rotation_difference(u_pos)
    q = rot2 @ rot

    if (q @ VECTOR_00m1).to_tuple(4) != u_nor.to_tuple(4):
        u_nor = ROT_DIF_VECTOR_00m1_111 @ u_nor
        u_pos = ROT_DIF_VECTOR_00m1_111 @ u_pos
        rot = VECTOR_00m1.rotation_difference(u_nor)
        rot2 = (rot @ VECTOR_0a10).rotation_difference(u_pos)
        rot2 = ROT_DIF_VECTOR_00m1_111_invert @ rot2
        q = rot2 @ rot

    pos0 = Vector((sin(angle), cos(angle), 0.0))
    pos1 = pos0.copy()
    pos1[0] *= -1
    return q @ pos0, q @ pos1
    #|
def r_qdiff(vec0_old, vec0, vec1_old, vec1):
    rot = vec0_old.rotation_difference(vec0)
    rot2 = (rot @ vec1_old).rotation_difference(vec1)
    q = rot2 @ rot

    if (q @ vec0_old).to_tuple(4) != vec0.to_tuple(4):
        vec0 = ROT_DIF_VECTOR_00m1_111 @ vec0
        vec1 = ROT_DIF_VECTOR_00m1_111 @ vec1
        rot = vec0_old.rotation_difference(vec0)
        rot2 = (rot @ vec1_old).rotation_difference(vec1)
        rot2 = ROT_DIF_VECTOR_00m1_111_invert @ rot2
        return rot2 @ rot
    return q
    #|
def r_vert_area(loops):
    bmtemp = bmesh.new()
    verts = bmtemp.verts

    for co in loops:
        verts.new(co)

    face_area = bmtemp.faces.new(verts).calc_area()
    bmtemp.free()
    return face_area

    # n = Vector()
    # v_prev = loops[-1]
    # for v_curr in loops:
    #     n[0] += (v_prev[1] - v_curr[1]) * (v_prev[2] + v_curr[2])
    #     n[1] += (v_prev[2] - v_curr[2]) * (v_prev[0] + v_curr[0])
    #     n[2] += (v_prev[0] - v_curr[0]) * (v_prev[1] + v_curr[1])
    #     v_prev = v_curr
    # return n.length * 0.5
    #|
def r_faces_area(bm_faces, bm_dic):
    bmtemp = bmesh.new()
    verts = bmtemp.verts
    faces = bmtemp.faces

    face_area = 0.0
    for face in bm_faces:
        bmtemp.clear()

        for loop in face.loops: verts.new(bm_dic[face].matrix_world @ loop.vert.co)
        face_area += faces.new(verts).calc_area()
    bmtemp.free()
    return face_area
    #|

def is_2edge_connect(e0, e1):
    return len({*e0.verts, *e1.verts}) == 3
    #|
def rotate(verts, origin, q):
    for v in verts:
        v[:] = q @ (v - origin)
    #|


# def r_vert_normal(loops): # non-normalize
#     n = Vector()
#     v_prev = loops[-1]
#     for v_curr in loops:
#         n[0] += (v_prev[1] - v_curr[1]) * (v_prev[2] + v_curr[2])
#         n[1] += (v_prev[2] - v_curr[2]) * (v_prev[0] + v_curr[0])
#         n[2] += (v_prev[0] - v_curr[0]) * (v_prev[1] + v_curr[1])
#         v_prev = v_curr
#     return n
#     #|