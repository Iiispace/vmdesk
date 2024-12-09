import bpy, blf

unescape_identifier = bpy.utils.unescape_identifier

blfLoad = blf.load
blf_unload = blf.unload
bpy_types = bpy.types
abspath = bpy.path.abspath
persistent = bpy.app.handlers.persistent

from os.path import realpath, dirname
from os import sep as os_sep

from . util.deco import noRecursive


BL_INFO = {}
TAG_UPDATE = [False, False, True]
FONT_DIR = os_sep.join((dirname(realpath(__file__)), "Fonts"))
PATH_FONT0 = abspath(os_sep.join((FONT_DIR, "droidsans.ttf")))
PATH_FONT1 = abspath(os_sep.join((FONT_DIR, "bmonofont-i18n.ttf")))
FONT_IDS = [-1, -1]


def bus_unit_system():

    m.UnitSystem.update()
    #|

MSGBUS_ATTRS = (
    ((bpy_types.UnitSettings, "system"), bus_unit_system),
    ((bpy_types.UnitSettings, "length_unit"), bus_unit_system),
    ((bpy_types.UnitSettings, "scale_length"), bus_unit_system),
    ((bpy_types.UnitSettings, "system_rotation"), bus_unit_system),
    ((bpy_types.UnitSettings, "mass_unit"), bus_unit_system),
    ((bpy_types.UnitSettings, "time_unit"), bus_unit_system),
    ((bpy_types.UnitSettings, "temperature_unit"), bus_unit_system),)

MSGBUS_MDLINK_ATTRS = ()
# MSGBUS_MDLINK_ATTRS = (
#     (bpy_types.BooleanModifier, 'object'),
#     (bpy_types.BevelModifier, 'vertex_group'),
#     (bpy_types.ArmatureModifier, 'object'),
#     (bpy_types.ArmatureModifier, 'vertex_group'),
#     (bpy_types.ArmatureModifier, 'use_vertex_groups'),
#     (bpy_types.ArmatureModifier, 'use_bone_envelopes'),
#     (bpy_types.ArrayModifier, 'curve'),
#     (bpy_types.ArrayModifier, 'end_cap'),
#     (bpy_types.ArrayModifier, 'offset_object'),
#     (bpy_types.ArrayModifier, 'start_cap'),
#     (bpy_types.CastModifier, 'object'),
#     (bpy_types.CastModifier, 'vertex_group'),
#     (bpy_types.CurveModifier, 'object'),
#     (bpy_types.CurveModifier, 'vertex_group'),
#     (bpy_types.CorrectiveSmoothModifier, 'vertex_group'),
#     (bpy_types.DataTransferModifier, 'object'),
#     (bpy_types.DataTransferModifier, 'vertex_group'),
#     (bpy_types.DecimateModifier, 'vertex_group'),
#     (bpy_types.DisplaceModifier, 'texture'),
#     (bpy_types.DisplaceModifier, 'texture_coords_bone'),
#     (bpy_types.DisplaceModifier, 'texture_coords_object'),
#     (bpy_types.DisplaceModifier, 'uv_layer'),
#     (bpy_types.DisplaceModifier, 'vertex_group'),
#     (bpy_types.ExplodeModifier, 'particle_uv'),
#     (bpy_types.ExplodeModifier, 'vertex_group'),
#     (bpy_types.HookModifier, 'object'),
#     (bpy_types.HookModifier, 'subtarget'),
#     (bpy_types.HookModifier, 'vertex_group'),
#     (bpy_types.LaplacianDeformModifier, 'vertex_group'),
#     (bpy_types.LaplacianSmoothModifier, 'vertex_group'),
#     (bpy_types.LatticeModifier, 'object'),
#     (bpy_types.LatticeModifier, 'vertex_group'),
#     (bpy_types.MaskModifier, 'armature'),
#     (bpy_types.MaskModifier, 'vertex_group'),
#     (bpy_types.MeshCacheModifier, 'filepath'),
#     (bpy_types.MeshCacheModifier, 'vertex_group'),
#     (bpy_types.MeshDeformModifier, 'object'),
#     (bpy_types.MeshDeformModifier, 'vertex_group'),
#     (bpy_types.MeshSequenceCacheModifier, 'cache_file'),
#     (bpy_types.MeshSequenceCacheModifier, 'object_path'),
#     (bpy_types.MirrorModifier, 'mirror_object'),
#     (bpy_types.MultiresModifier, 'filepath'),
#     (bpy_types.NormalEditModifier, 'target'),
#     (bpy_types.NormalEditModifier, 'vertex_group'),
#     (bpy_types.OceanModifier, 'bake_foam_fade'),
#     (bpy_types.OceanModifier, 'damping'),
#     (bpy_types.OceanModifier, 'depth'),
#     (bpy_types.OceanModifier, 'fetch_jonswap'),
#     (bpy_types.OceanModifier, 'filepath'),
#     (bpy_types.OceanModifier, 'foam_layer_name'),
#     (bpy_types.OceanModifier, 'frame_end'),
#     (bpy_types.OceanModifier, 'frame_start'),
#     (bpy_types.OceanModifier, 'invert_spray'),
#     (bpy_types.OceanModifier, 'random_seed'),
#     (bpy_types.OceanModifier, 'repeat_x'),
#     (bpy_types.OceanModifier, 'repeat_y'),
#     (bpy_types.OceanModifier, 'resolution'),
#     (bpy_types.OceanModifier, 'sharpen_peak_jonswap'),
#     (bpy_types.OceanModifier, 'spatial_size'),
#     (bpy_types.OceanModifier, 'spectrum'),
#     (bpy_types.OceanModifier, 'spray_layer_name'),
#     (bpy_types.OceanModifier, 'use_foam'),
#     (bpy_types.OceanModifier, 'use_normals'),
#     (bpy_types.OceanModifier, 'use_spray'),
#     (bpy_types.OceanModifier, 'viewport_resolution'),
#     (bpy_types.OceanModifier, 'wave_alignment'),
#     (bpy_types.OceanModifier, 'wave_direction'),
#     (bpy_types.OceanModifier, 'wave_scale_min'),
#     (bpy_types.OceanModifier, 'wind_velocity'),
#     (bpy_types.ParticleInstanceModifier, 'index_layer_name'),
#     (bpy_types.ParticleInstanceModifier, 'object'),
#     (bpy_types.ParticleInstanceModifier, 'particle_system'),
#     (bpy_types.ParticleInstanceModifier, 'value_layer_name'),
#     (bpy_types.ScrewModifier, 'object'),
#     (bpy_types.ShrinkwrapModifier, 'auxiliary_target'),
#     (bpy_types.ShrinkwrapModifier, 'target'),
#     (bpy_types.ShrinkwrapModifier, 'vertex_group'),
#     (bpy_types.SimpleDeformModifier, 'origin'),
#     (bpy_types.SimpleDeformModifier, 'vertex_group'),
#     (bpy_types.SmoothModifier, 'vertex_group'),
#     (bpy_types.SolidifyModifier, 'rim_vertex_group'),
#     (bpy_types.SolidifyModifier, 'shell_vertex_group'),
#     (bpy_types.SolidifyModifier, 'vertex_group'),
#     (bpy_types.SurfaceDeformModifier, 'target'),
#     (bpy_types.SurfaceDeformModifier, 'use_sparse_bind'),
#     (bpy_types.SurfaceDeformModifier, 'vertex_group'),
#     (bpy_types.UVProjectModifier, 'uv_layer'),
#     (bpy_types.UVWarpModifier, 'bone_from'),
#     (bpy_types.UVWarpModifier, 'bone_to'),
#     (bpy_types.UVWarpModifier, 'object_from'),
#     (bpy_types.UVWarpModifier, 'object_to'),
#     (bpy_types.UVWarpModifier, 'uv_layer'),
#     (bpy_types.UVWarpModifier, 'vertex_group'),
#     (bpy_types.VertexWeightEditModifier, 'mask_tex_map_bone'),
#     (bpy_types.VertexWeightEditModifier, 'mask_tex_map_object'),
#     (bpy_types.VertexWeightEditModifier, 'mask_tex_uv_layer'),
#     (bpy_types.VertexWeightEditModifier, 'mask_texture'),
#     (bpy_types.VertexWeightEditModifier, 'mask_vertex_group'),
#     (bpy_types.VertexWeightEditModifier, 'vertex_group'),
#     (bpy_types.VertexWeightMixModifier, 'mask_tex_map_bone'),
#     (bpy_types.VertexWeightMixModifier, 'mask_tex_map_object'),
#     (bpy_types.VertexWeightMixModifier, 'mask_tex_uv_layer'),
#     (bpy_types.VertexWeightMixModifier, 'mask_texture'),
#     (bpy_types.VertexWeightMixModifier, 'mask_vertex_group'),
#     (bpy_types.VertexWeightMixModifier, 'vertex_group_a'),
#     (bpy_types.VertexWeightMixModifier, 'vertex_group_b'),
#     (bpy_types.VertexWeightProximityModifier, 'mask_tex_map_bone'),
#     (bpy_types.VertexWeightProximityModifier, 'mask_tex_map_object'),
#     (bpy_types.VertexWeightProximityModifier, 'mask_tex_uv_layer'),
#     (bpy_types.VertexWeightProximityModifier, 'mask_texture'),
#     (bpy_types.VertexWeightProximityModifier, 'mask_vertex_group'),
#     (bpy_types.VertexWeightProximityModifier, 'target'),
#     (bpy_types.VertexWeightProximityModifier, 'vertex_group'),
#     (bpy_types.VolumeToMeshModifier, 'grid_name'),
#     (bpy_types.VolumeToMeshModifier, 'object'),
#     (bpy_types.WarpModifier, 'bone_from'),
#     (bpy_types.WarpModifier, 'bone_to'),
#     (bpy_types.WarpModifier, 'object_from'),
#     (bpy_types.WarpModifier, 'object_to'),
#     (bpy_types.WarpModifier, 'texture'),
#     (bpy_types.WarpModifier, 'texture_coords_bone'),
#     (bpy_types.WarpModifier, 'texture_coords_object'),
#     (bpy_types.WarpModifier, 'uv_layer'),
#     (bpy_types.WarpModifier, 'vertex_group'),
#     (bpy_types.WaveModifier, 'start_position_object'),
#     (bpy_types.WaveModifier, 'texture'),
#     (bpy_types.WaveModifier, 'texture_coords_bone'),
#     (bpy_types.WaveModifier, 'texture_coords_object'),
#     (bpy_types.WaveModifier, 'uv_layer'),
#     (bpy_types.WaveModifier, 'vertex_group'),
#     (bpy_types.WeightedNormalModifier, 'vertex_group'),
#     (bpy_types.WeldModifier, 'vertex_group'),
#     (bpy_types.WireframeModifier, 'vertex_group'),
#     (bpy_types.NodesModifier, 'node_group'),
#     (bpy_types.MeshToVolumeModifier, 'object'),
#     (bpy_types.VolumeDisplaceModifier, 'texture'),
#     (bpy_types.VolumeDisplaceModifier, 'texture_map_object'),)



@persistent
def load_pre(dummy):

    if m.ADMIN is not None:
        try:
            m.kill_admin()
        except Exception as ex:
            pass

    #|
@persistent
def load_post(dummy):


    bl_load()
    newfile_event()
    #|

def newfile_event():

    block.PREF_HISTORY.kill()
    block.PREF_HISTORY.__init__(block, m.P.undo_steps_local)
    #|

@ noRecursive
def upd_link_data():
    pass
    # print("[[[[ update_link_data ]]]]")
    # for fc, e in REFDRIVERS.copy().items():
    #     try:
    #         obj, dr_id = e
    #         if hasattr(fc, "driver"):
    #             if fc.driver == None or dr_id != id(fc.driver):
    #                 del REFDRIVERS[fc]
    #                 continue
    #         else:
    #             del REFDRIVERS[fc]
    #             continue

    #         dp = unescape_identifier(fc.data_path[2 : -2])
    #         # pink = obj.path_resolve(dp)
    #         tar = fc.driver.variables[0].targets[0]
    #         point_to = tar.id.path_resolve(tar.data_path)

    #         if obj.path_resolve(dp) != point_to:
    #             i0 = dp.rfind(".")
    #             setattr(obj.path_resolve(dp[ : i0]), dp[i0 + 1 : ], point_to)
    #             TAG_UPDATE[0] = True
    #             print(f"[[[[REF]]]]{obj.name}")
    #     except:
    #         continue

    # if TAG_UPDATE[0]:
    #     try: update_data()
    #     except: pass
    # #|

def subscribe():
    if subscribe.IS_SUBSCRIBE is True: return
    subscribe.IS_SUBSCRIBE = True
    subscribe_rna = bpy.msgbus.subscribe_rna

    # for attr in MSGBUS_MDLINK_ATTRS:
    #     subscribe_rna(
    #         key     = attr,
    #         owner   = attr,
    #         args    = (),
    #         notify  = upd_link_data)

    for attr, e in MSGBUS_ATTRS:
        subscribe_rna(
            key     = attr,
            owner   = attr,
            args    = (),
            notify  = e)

    #|
def unsubscribe():
    if subscribe.IS_SUBSCRIBE is False: return
    subscribe.IS_SUBSCRIBE = False
    # REFDRIVERS.clear()
    clear_by_owner = bpy.msgbus.clear_by_owner

    # for attr in MSGBUS_MDLINK_ATTRS:    clear_by_owner(attr)
    for attr, e in MSGBUS_ATTRS:        clear_by_owner(attr)


    #|
subscribe.IS_SUBSCRIBE = False

def bl_load():


    unsubscribe()
    # for obj in (
    #     1copy (bl_objects,, $$)
    # ):
    #     if obj.animation_data:
    #         for fc in obj.animation_data.drivers:
    #             path = fc.data_path
    #             if path[: 12] == '["modifiers[':
    #                 REFDRIVERS[fc] = obj, id(fc.driver)

    subscribe()
    upd_link_data()

    global PATH_FONT0, PATH_FONT1
    # <<< 1copy (assignP,, $$)
    P = bpy.context.preferences.addons[__package__].preferences
    # >>>
    if P.fontpath_method == "BLENDER":
        pref_view = bpy.context.preferences.view
        PATH_FONT0 = pref_view.font_path_ui
        PATH_FONT1 = pref_view.font_path_ui_mono

        font0 = blfLoad(PATH_FONT0)
        FONT_IDS[0] = 0  if font0 == -1 else font0

        font1 = blfLoad(PATH_FONT1)
        FONT_IDS[1] = 1  if font1 == -1 else font1
    elif P.fontpath_method == "CUSTOM":
        font0 = blfLoad(P.fontpath_ui)
        if font0 == -1:
            FONT_IDS[0] = blfLoad(PATH_FONT0)
        else:
            FONT_IDS[0] = font0
            PATH_FONT0 = P.fontpath_ui

        font1 = blfLoad(P.fontpath_ui_mono)
        if font1 == -1:
            FONT_IDS[1] = blfLoad(PATH_FONT1)
        else:
            FONT_IDS[1] = font1
            PATH_FONT1 = P.fontpath_ui_mono
    else:
        FONT_IDS[0] = blfLoad(PATH_FONT0)
        FONT_IDS[1] = blfLoad(PATH_FONT1)
    #|
def bl_unload():
    #|

    if m.ADMIN is not None:
        try:
            m.kill_admin()
        except Exception as ex:
            pass


    unsubscribe()
    blf_unload(PATH_FONT0)
    blf_unload(PATH_FONT1)
    #|

def late_import():
    #|
    from .  import VMD

    m = VMD.m
    block = VMD.block
    update_data = m.update_data

    globals().update(locals())
    #|