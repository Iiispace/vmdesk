from bpy import props

# <<< 1mp (props
StringProperty, = props.StringProperty,
EnumProperty, = props.EnumProperty,
BoolProperty, = props.BoolProperty,
IntVectorProperty, = props.IntVectorProperty,
FloatVectorProperty, = props.FloatVectorProperty,
FloatProperty = props.FloatProperty
# >>>

BLPROP_mesh = {
    "vertex_distance": FloatProperty(
        name = "Distance",
        description = "Distance between 2 vertices",
        subtype = "DISTANCE"),
    "local_space": BoolProperty(
        name = "Local Space",
        description = "Use local space",
        default = False),
    "invert_vertex": BoolProperty(
        name = "Invert",
        description = "Move another vertex",
        default = False),
    "line_direction": FloatVectorProperty(
        name = "Direction",
        description = "Direction of 2 vertices",
        subtype = "TRANSLATION"),
    "face_normal": FloatVectorProperty(
        name = "Normal",
        description = "Face normal",
        size = 3,
        subtype = "TRANSLATION"),
    "method_set_normal": EnumProperty(
        name = "Method",
        description = "How to set face normals",
        items = (
            ("NONE", "None", ""),
            ("KEEP_NORMALS_OF_OTHER_FACES", "Keep Normals of Other Faces", "Keep normals of unselected faces if possible"),
            ("KEEP_SHAPE", "Keep Shape", "")),
        default = "KEEP_NORMALS_OF_OTHER_FACES"),
    "lock_active_vertex": BoolProperty(
        name = "Lock Active Vertex",
        description = "Keep active vertex location",
        default = False),
    "included_angle": FloatProperty(
        name = "Angle",
        description = "Included angle",
        subtype = "ANGLE"),
    "tot_area": FloatProperty(
        name = "Area",
        description = "Total area",
        unit = "AREA",
        min = 0.0,
        precision=6),
}
