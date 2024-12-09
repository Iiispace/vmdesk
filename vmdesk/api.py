import bpy

from bpy.types import NodesModifier

attr_NodesModifier_bake_directory = "bake_directory" if "bake_directory" in NodesModifier.bl_rna.properties else "simulation_bake_directory"


D_blendData_id = {
    "actions":          "ACTION",
    "armatures":        "ARMATURE",
    "brushes":          "BRUSH",
    "cache_files":      "CACHEFILE",
    "cameras":          "CAMERA",
    "collections":      "COLLECTION",
    "curves":           "CURVE",
    "fonts":            "FONT",
    "grease_pencils":   "GREASEPENCIL",
    "hair_curves":      "CURVES",
    "images":           "IMAGE",
    "lattices":         "LATTICE",
    "libraries":        "LIBRARY",
    "lightprobes":      "LIGHT_PROBE",
    "lights":           "LIGHT",
    "linestyles":       "LINESTYLE",
    "masks":            "MASK",
    "materials":        "MATERIAL",
    "meshes":           "MESH",
    "metaballs":        "META",
    "movieclips":       "MOVIECLIP",
    "node_groups":      "NODETREE",
    "objects":          "OBJECT",
    "paint_curves":     "PAINTCURVE",
    "palettes":         "PALETTE",
    "particles":        "PARTICLE",
    "pointclouds":      "POINTCLOUD",
    "scenes":           "SCENE",
    "screens":          "SCREEN",
    "shape_keys":       "KEY",
    "sounds":           "SOUND",
    "speakers":         "SPEAKER",
    "texts":            "TEXT",
    "textures":         "TEXTURE",
    "volumes":          "VOLUME",
    "window_managers":  "WINDOWMANAGER",
    "workspaces":       "WORKSPACE",
    "worlds":           "WORLD"}
D_id_blendData = {k: e for e, k in D_blendData_id.items()}

D_blendData_cls = {
    "actions":          "Action",
    "armatures":        "Armature",
    "brushes":          "Brush",
    "cache_files":      "CacheFile",
    "cameras":          "Camera",
    "collections":      "Collection",
    "curves":           "Curve",
    "fonts":            "VectorFont",
    "grease_pencils":   "GreasePencil",
    "hair_curves":      "Curves",
    "images":           "Image",
    "lattices":         "Lattice",
    "libraries":        "Library",
    "lightprobes":      "LightProbe",
    "lights":           "Light",
    "linestyles":       "FreestyleLineStyle",
    "masks":            "Mask",
    "materials":        "Material",
    "meshes":           "Mesh",
    "metaballs":        "MetaBall",
    "movieclips":       "MovieClip",
    "node_groups":      "NodeTree",
    "objects":          "Object",
    "paint_curves":     "PaintCurve",
    "palettes":         "Palette",
    "particles":        "ParticleSettings",
    "pointclouds":      "PointCloud",
    "scenes":           "Scene",
    "screens":          "Screen",
    "shape_keys":       "Key",
    "sounds":           "Sound",
    "speakers":         "Speaker",
    "texts":            "Text",
    "textures":         "Texture",
    "volumes":          "Volume",
    "window_managers":  "WindowManager",
    "workspaces":       "WorkSpace",
    "worlds":           "World"}
D_cls_blendData = {k: e for e, k in D_blendData_cls.items()}
D_cls_id = {k: D_blendData_id[e] for k, e in D_cls_blendData.items()}
D_id_cls = {k: e for e, k in D_cls_id.items()}

S_ALLOW_ASSET = {
    'MATERIAL',
    'COLLECTION',
    'OBJECT',
    'BRUSH',
    'ACTION',
    'WORLD'}
S_ALLOW_PREVIEW = {
    'IMAGE',
    'MATERIAL',
    'TEXTURE',
}
