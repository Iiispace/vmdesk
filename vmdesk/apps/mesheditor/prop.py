
from .  import VMD

# <<< 1mp (VMD.util.types
types = VMD.util.types
blRna = types.blRna
r_enum_items_create = types.r_enum_items_create
RnaDataOps = types.RnaDataOps
RnaFloat = types.RnaFloat
RnaFloatVector = types.RnaFloatVector
RnaBool = types.RnaBool
RnaString = types.RnaString
RnaButton = types.RnaButton
RnaEnum = types.RnaEnum
# >>>


class PpMeshEditor(blRna((
    RnaEnum("local_space",
        enum_items = r_enum_items_create((("LOCAL", "Local", ""), ("GLOBAL", "Global", ""))),
        name = "Space",
        description = "Transform space",
        default = "GLOBAL"),
    ))):
    __slots__ = 'w'
class PpMeshTab(blRna((
    RnaFloat("distance",
        name = "Distance",
        description = "Distance between 2 vertices",
        subtype = "DISTANCE",
        unit = "LENGTH"),
    RnaFloatVector("direction",
        name = "Direction",
        description = "Direction of 2 vertices",
        default = (0.0, 0.0, 0.0),
        subtype = "DIRECTION",
        unit = "LENGTH"),
    RnaFloatVector("u_direction",
        name = "Unit Vector",
        description = "Unit Direction of 2 vertices",
        default = (0.0, 0.0, 0.0),
        subtype = "STRING_VECTOR",
        unit = "LENGTH"),
    RnaBool("vert_invert",
        name = "Invert",
        description = "Reverse moved vertex"),
    RnaFloatVector("u_normal",
        name = "Unit Normal",
        description = "Unit normal of 3 vertices or face",
        default = (0.0, 0.0, 0.0),
        subtype = "STRING_VECTOR",
        unit = "LENGTH"),
    RnaEnum("method_set_normal",
        enum_items = r_enum_items_create((
            ("NONE", "None", ""),
            ("KEEP_NORMALS_OF_OTHER_FACES", "Keep Normals of Other Faces", "Keep normals of unselected faces if possible"),
            ("KEEP_SHAPE", "Keep Shape", ""))),
        name = "Method",
        description = "How to set face normals",
        default = "KEEP_SHAPE"),
    RnaBool("lock_active_vertex",
        name = "Lock Active Vertex",
        description = "Keep active vertex location"),
    RnaButton("vert_limit",
        name = "Vertex Limit",
        description = "Deactivate the property when the selected vertex count exceeds this value",
        button_text = "Vertex Limit"),
    RnaButton("make_collinear",
        name = "Make Collinear",
        description = "Make vertices collinear",
        button_text = "Make Collinear"),
    RnaButton("make_coplanar",
        name = "Make Coplanar",
        description = "Make vertices coplanar",
        button_text = "Make Coplanar"),
    RnaBool("lock_active_vertex_collinear",
        name = "Lock Active Vertex",
        description = "Keep active vertex location"),
    RnaFloat("area",
        name = "Area",
        description = "Faces area",
        unit = "AREA"),
    RnaFloat("angle",
        name = "Included Angle",
        description = "Unsigned angle between 2 edges. If 3 vertices selected, the angle will be based on the second selected vertex.\nWhen modifying the angle, the last selected vertex will move and maintain the length from the second vertex",
        subtype = "ANGLE",
        unit = "ROTATION"),
    ))):
    __slots__ = 'w'

RNAS_mesh = PpMeshTab.bl_rna.properties
RNAS_mesh["distance"].data = RnaDataOps("mesh.vmd_vert_distance", "Mesh")
RNAS_mesh["direction"].data = RnaDataOps("mesh.vmd_vert_direction", "Mesh")
RNAS_mesh["u_normal"].data = RnaDataOps("mesh.vmd_normal", "Mesh")
RNAS_mesh["make_collinear"].data = RnaDataOps("mesh.vmd_collinear", "Mesh")
RNAS_mesh["make_coplanar"].data = RnaDataOps("mesh.vmd_coplanar", "Mesh")
RNAS_mesh["area"].data = RnaDataOps("mesh.vmd_area", "Mesh")
RNAS_mesh["angle"].data = RnaDataOps("mesh.vmd_angle", "Mesh")
