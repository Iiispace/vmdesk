import bpy

DriverTarget = bpy.types.DriverTarget
TriangulateModifier = bpy.types.TriangulateModifier

escape_identifier = bpy.utils.escape_identifier

data_ = bpy.app.translations.pgettext_data

ed_undo_push = bpy.ops.ed.undo_push
md_rnas_MESH = []
md_rnas_CURVE = []
md_rnas_SURFACE = []
md_rnas_VOLUME = []
md_rnas_LATTICE = []
md_rnas_FONT = []
md_rnas_GREASEPENCIL = []

md_identifiers_MESH = (
    "DATA_TRANSFER",
    "MESH_CACHE",
    "MESH_SEQUENCE_CACHE",
    "NORMAL_EDIT",
    "WEIGHTED_NORMAL",
    "UV_PROJECT",
    "UV_WARP",
    "VERTEX_WEIGHT_EDIT",
    "VERTEX_WEIGHT_MIX",
    "VERTEX_WEIGHT_PROXIMITY",
    "ARRAY",
    "BEVEL",
    "BOOLEAN",
    "BUILD",
    "DECIMATE",
    "EDGE_SPLIT",
    "NODES",
    "MASK",
    "MIRROR",
    "MULTIRES",
    "REMESH",
    "SCREW",
    "SKIN",
    "SOLIDIFY",
    "SUBSURF",
    "TRIANGULATE",
    "VOLUME_TO_MESH",
    "WELD",
    "WIREFRAME",
    "ARMATURE",
    "CAST",
    "CURVE",
    "DISPLACE",
    "HOOK",
    "LAPLACIANDEFORM",
    "LATTICE",
    "MESH_DEFORM",
    "SHRINKWRAP",
    "SIMPLE_DEFORM",
    "SMOOTH",
    "CORRECTIVE_SMOOTH",
    "LAPLACIANSMOOTH",
    "SURFACE_DEFORM",
    "WARP",
    "WAVE",
    "CLOTH",
    "COLLISION",
    "DYNAMIC_PAINT",
    "EXPLODE",
    "FLUID",
    "OCEAN",
    "PARTICLE_INSTANCE",
    "PARTICLE_SYSTEM",
    "SOFT_BODY")
md_identifiers_CURVE = (
    "MESH_CACHE",
    "MESH_SEQUENCE_CACHE",
    "ARRAY",
    "BEVEL",
    "BUILD",
    "DECIMATE",
    "EDGE_SPLIT",
    "NODES",
    "MIRROR",
    "REMESH",
    "SCREW",
    "SOLIDIFY",
    "SUBSURF",
    "TRIANGULATE",
    "WELD",
    "ARMATURE",
    "CAST",
    "CURVE",
    "HOOK",
    "LATTICE",
    "MESH_DEFORM",
    "SHRINKWRAP",
    "SIMPLE_DEFORM",
    "SMOOTH",
    "WARP",
    "WAVE",
    "SOFT_BODY")
md_identifiers_SURFACE = (
    "MESH_CACHE",
    "MESH_SEQUENCE_CACHE",
    "ARRAY",
    "BEVEL",
    "BUILD",
    "DECIMATE",
    "EDGE_SPLIT",
    "MIRROR",
    "REMESH",
    "SCREW",
    "SOLIDIFY",
    "SUBSURF",
    "TRIANGULATE",
    "WELD",
    "ARMATURE",
    "CAST",
    "CURVE",
    "HOOK",
    "LATTICE",
    "MESH_DEFORM",
    "SHRINKWRAP",
    "SIMPLE_DEFORM",
    "SMOOTH",
    "WARP",
    "WAVE",
    "SOFT_BODY")
md_identifiers_VOLUME = (
    "NODES",
    "MESH_TO_VOLUME",
    "VOLUME_DISPLACE")
md_identifiers_LATTICE = (
    "MESH_CACHE",
    "ARMATURE",
    "CAST",
    "CURVE",
    "HOOK",
    "LATTICE",
    "MESH_DEFORM",
    "SHRINKWRAP",
    "SIMPLE_DEFORM",
    "WARP",
    "WAVE",
    "SOFT_BODY")
md_identifiers_FONT = md_identifiers_CURVE
md_identifiers_GREASEPENCIL = (
    "GREASE_PENCIL_TEXTURE",
    "GREASE_PENCIL_TIME",
    "GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY",
    "GREASE_PENCIL_VERTEX_WEIGHT_ANGLE",
    "GREASE_PENCIL_ARRAY",
    "GREASE_PENCIL_BUILD",
    "GREASE_PENCIL_DASH",
    "GREASE_PENCIL_ENVELOPE",
    "GREASE_PENCIL_LENGTH",
    "GREASE_PENCIL_MIRROR",
    "GREASE_PENCIL_MULTIPLY",
    "GREASE_PENCIL_OUTLINE",
    "GREASE_PENCIL_SIMPLIFY",
    "GREASE_PENCIL_SUBDIV",
    "LINEART",
    "GREASE_PENCIL_ARMATURE",
    "GREASE_PENCIL_HOOK",
    "GREASE_PENCIL_LATTICE",
    "GREASE_PENCIL_NOISE",
    "GREASE_PENCIL_OFFSET",
    "GREASE_PENCIL_SHRINKWRAP",
    "GREASE_PENCIL_SMOOTH",
    "GREASE_PENCIL_THICKNESS",
    "GREASE_PENCIL_COLOR",
    "GREASE_PENCIL_TINT",
    "GREASE_PENCIL_OPACITY")

# Copy from Source
def add_empty_geometry_node_group(name=None):
    if name is None: name = data_("Geometry Nodes")
    group = bpy.data.node_groups.new(name, 'GeometryNodeTree')

    group.interface.new_socket(data_("Geometry"), in_out='INPUT', socket_type='NodeSocketGeometry')
    input_node = group.nodes.new('NodeGroupInput')
    input_node.select = False
    input_node.location.x = -200 - input_node.width

    group.interface.new_socket(data_("Geometry"), in_out='OUTPUT', socket_type='NodeSocketGeometry')
    output_node = group.nodes.new('NodeGroupOutput')
    output_node.is_active_output = True
    output_node.select = False
    output_node.location.x = 200

    group.links.new(group.nodes[data_("Group Input")].outputs[0], group.nodes[data_("Group Output")].inputs[0])
    group.is_modifier = True
    return group


def is_dead(obj):
    try:
        obj.name
        return False
    except: return True
    #|
def r_object_library_message(ob):
    if hasattr(ob, 'library') and ob.library:
        return "This operation cannot be performed \nfrom a linked data-block"
    if hasattr(ob, 'override_library') and ob.override_library and ob.override_library.is_system_override:
        return "This operation cannot be performed \nfrom a system override data-block"
    return ""
    #|

def r_md_identifier_by_name(s):
    for identifier, e in bpy.types.Modifier.bl_rna.properties['type'].enum_items.items():
        if identifier == "SURFACE": continue
        if e.name == s: return identifier
    return ""
    #|

def dr_fcurve_add(tar, tar_dp, index):
    try:    return tar.driver_add(tar_dp, index)
    except:
        try: return tar.driver_add(tar_dp)
        except: return None
    #|
def kf_fcurve_add(tar_fcs, tar_dp, index, action_group):
    try:    return tar_fcs.new(tar_dp, index, action_group)
    except: pass
    try:    return tar_fcs.new(tar_dp, index=index)
    except:
        try: return tar_fcs.new(tar_dp)
        except: return None
    #|

def tr_drivers(oj):
    try:    return oj.animation_data.drivers
    except: return None
    #|
def tr_driver(oj, data_path, index=0):
    try:    return oj.animation_data.drivers.find(data_path, index=index)
    except: return None
    #|
def tr_action_fcurves(oj):
    try:    return oj.animation_data.action.fcurves
    except: return None
    #|
def tr_dr_add(oj, dp):
    try:    return oj.driver_add(dp)
    except: return None
    #|
def tr_dr_add_index(oj, dp, index):
    try:    return oj.driver_add(dp, index=index)
    except: return None
    #|

def is_dp_exist(obj, path):
    try:
        obj.path_resolve(path)
        return True
    except: return False
    #|

def copy_fc_attrs(fc_from, fc_to):
    fc_to.auto_smoothing    = fc_from.auto_smoothing
    fc_to.color             = fc_from.color
    fc_to.color_mode        = fc_from.color_mode
    fc_to.extrapolation     = fc_from.extrapolation
    fc_to.hide              = fc_from.hide
    fc_to.is_valid          = fc_from.is_valid
    fc_to.lock              = fc_from.lock
    fc_to.mute              = fc_from.mute
    #|
def copy_driver_var(v_from, v_to):
    v_to.type   = v_from.type
    v_to.name   = v_from.name
    tar_to      = v_to.targets[0]
    tar_from    = v_from.targets[0]

    try: tar_to.id_type = tar_from.id_type
    except: return False

    tar_to.id               = tar_from.id
    tar_to.data_path        = tar_from.data_path
    tar_to.rotation_mode    = tar_from.rotation_mode
    tar_to.transform_type   = tar_from.transform_type
    tar_to.transform_space  = tar_from.transform_space
    tar_to.bone_target      = tar_from.bone_target

    if len(v_from.targets) == 2:
        tar_to      = v_to.targets[1]
        tar_from    = v_from.targets[1]

        try: tar_to.id_type = tar_from.id_type
        except: return False

        tar_to.id               = tar_from.id
        tar_to.data_path        = tar_from.data_path
        tar_to.rotation_mode    = tar_from.rotation_mode
        tar_to.transform_type   = tar_from.transform_type
        tar_to.transform_space  = tar_from.transform_space
        tar_to.bone_target      = tar_from.bone_target
    return True
    #|

def copy_dr(fc_from, tar, tar_dp):
    fc = dr_fcurve_add(tar, tar_dp, fc_from.array_index)
    if fc == None: return None
    if type(fc) == list: fc = fc[fc_from.array_index]

    fc.data_path = tar_dp
    copy_fc_attrs(fc_from, fc)

    dr_to   = fc.driver
    dr_from = fc_from.driver
    dr_to.type          = dr_from.type
    dr_to.expression    = dr_from.expression
    dr_to.is_valid      = dr_from.is_valid
    dr_to.use_self      = dr_from.use_self

    variables = dr_to.variables
    for v in dr_from.variables:
        var = variables.new()
        copy_driver_var(v, var)
    return fc
    #|
def copy_kf(fc_from, tar, tar_dp): # fc_from != None
    is_empty = False
    if tar.animation_data:
        if tar.animation_data.action is None:           is_empty = True
        elif tar.animation_data.action.fcurves is None: is_empty = True
    else: is_empty = True

    if is_empty:
        if tar.keyframe_insert(data_path = tar_dp) == False: return
        fcs     = tar.animation_data.action.fcurves
        for fc in fcs: fcs.remove(fc)
    else:
        fcs     = tar.animation_data.action.fcurves

    fc = kf_fcurve_add(fcs, tar_dp, fc_from.array_index, fc_from.group)
    if fc == None: return None
    fc.data_path = tar_dp
    copy_fc_attrs(fc_from, fc)

    kps = fc.keyframe_points
    for kp in fc_from.keyframe_points:
        kp_new = kps.insert(*kp.co, keyframe_type = kp.type)
        kp_new.amplitude            = kp.amplitude
        kp_new.back                 = kp.back
        kp_new.easing               = kp.easing
        kp_new.handle_left_type     = kp.handle_left_type
        kp_new.handle_left[0]       = kp.handle_left[0]
        kp_new.handle_left[1]       = kp.handle_left[1]
        kp_new.handle_right_type    = kp.handle_right_type
        kp_new.handle_right[0]      = kp.handle_right[0]
        kp_new.handle_right[1]      = kp.handle_right[1]
        kp_new.interpolation        = kp.interpolation
        kp_new.period               = kp.period
        kp_new.select_control_point = kp.select_control_point
        kp_new.select_left_handle   = kp.select_left_handle
        kp_new.select_right_handle  = kp.select_right_handle
    return fc
    #|

def copy_md_keyframe(oj, oj_tar, tar_md, dpDot, dpDot_tar):
    try: fcurves = oj.animation_data.action.fcurves
    except: return

    if fcurves:
        for attr in dir(tar_md):
            fc = fcurves.find(dpDot + attr)
            if fc is not None: copy_kf(fc, oj_tar, dpDot_tar + attr)
    #|
def copy_md_driver(oj, oj_tar, tar_md, dpDot, dpDot_tar):
    try: drivers = oj.animation_data.drivers
    except: return

    if drivers:
        for attr in dir(tar_md):
            dr = drivers.find(dpDot + attr)
            if dr is not None:  copy_dr(dr, oj_tar, dpDot_tar + attr)
    #|


def link_modifier(obj_from, obj_to, md_from, new_md_to):
    # REFDRIVERS = m.REFDRIVERS
    attrs = getattr(ModAttr, new_md_to.type, None)

    ex_attrs = getattr(ModExAttr, new_md_to.type, ())
    if ex_attrs:
        if obj_to.type in S_spline_modifier_types:
            ex_attrs = [e for e in ex_attrs  if e != "show_on_cage"]
            if new_md_to.type in S_md_apply_on_spline: ex_attrs.append("use_apply_on_spline")
        else:
            ex_attrs = [e for e in ex_attrs]

    if attrs is None:
        attr0 = ex_attrs
        attr1 = ()
    else:
        attr0 = [e for e in attrs] + ex_attrs
        # attr1 = getattr(ModRefAttr, new_md_to.type)
        attr1 = ()

    for attr in attr0:
        fc              = tr_dr_add(new_md_to, attr)
        if fc is None:  continue
        if isinstance(fc, list):
            for ind, fc in enumerate(fc):
                dr = fc.driver
                dr.type = "SCRIPTED"
                if dr.variables:
                    v = dr.variables[0]
                    v.type = "SINGLE_PROP"
                else:
                    v = dr.variables.new()
                tar             = v.targets[0]
                tar.id          = obj_from
                tar.data_path   = f'modifiers["{escape_identifier(md_from.name)}"].{attr}'
                dr.expression   = f"var[{ind}]"
        else:
            dr = fc.driver
            dr.type = "SCRIPTED"
            if dr.variables:
                v = dr.variables[0]
                v.type = "SINGLE_PROP"
            else:
                v = dr.variables.new()
            tar             = v.targets[0]
            tar.id          = obj_from
            tar.data_path   = f'modifiers["{escape_identifier(md_from.name)}"].{attr}'
            dr.expression   = "var"

    s0 = f"modifiers[\\\"{escape_identifier(new_md_to.name)}\\\"]."
    # for attr in attr1:
    #     path = s0 + attr
    #     obj_to[f'modifiers["{new_md_to.name}"].{attr}'] = True
    #     fc = obj_to.driver_add(f'["{path}"]')
    #     dr = fc.driver
    #     dr.type = "SCRIPTED"
    #     if dr.variables:
    #         v = dr.variables[0]
    #         v.type = "SINGLE_PROP"
    #     else:
    #         v = dr.variables.new()
    #     tar             = v.targets[0]
    #     tar.id          = obj_from
    #     v.name          = md_from.name
    #     tar.data_path   = f'modifiers["{escape_identifier(md_from.name)}"].{attr}'

    #     REFDRIVERS[fc] = obj_to, id(dr)
    #|
def deeplink_modifier(obj_from, obj_to, md_from, new_md_to):
    # REFDRIVERS = m.REFDRIVERS
    attrs = getattr(ModAttr, new_md_to.type, None)

    ex_attrs = getattr(ModExAttr, new_md_to.type, ())
    if ex_attrs:
        if obj_to.type in S_spline_modifier_types:
            ex_attrs = [e for e in ex_attrs  if e != "show_on_cage"]
            if new_md_to.type in S_md_apply_on_spline: ex_attrs.append("use_apply_on_spline")
        else:
            ex_attrs = [e for e in ex_attrs]

    if attrs is None:
        attr0 = ex_attrs
        attr1 = ()
    else:
        attr0 = [e for e in attrs] + ex_attrs
        # attr1 = getattr(ModRefAttr, new_md_to.type)
        attr1 = ()

    for attr in attr0:
        fc              = tr_dr_add(new_md_to, attr)
        if fc is None:  continue
        if isinstance(fc, list):
            for ind, fc in enumerate(fc):
                dr = fc.driver
                dr.type = "SCRIPTED"
                if dr.variables:
                    v = dr.variables[0]
                    v.type = "SINGLE_PROP"
                else:
                    v = dr.variables.new()
                tar             = v.targets[0]

                obj             = obj_from
                path_link       = f'modifiers["{escape_identifier(md_from.name)}"].{attr}'

                whilelim = 0
                while whilelim < 999:
                    whilelim += 1
                    fc_next     = tr_driver(obj, path_link, ind)
                    if fc_next is not None:
                        if fc_next.driver.type == 'SCRIPTED':
                            vs  = fc_next.driver.variables
                            if len(vs) == 1:
                                v0      = vs[0]
                                if fc_next.driver.expression == f'{v0.name}[{ind}]':
                                    tar0        = v0.targets[0]
                                    if tar0.id_type == 'OBJECT':
                                        if is_dp_exist(tar0.id, tar0.data_path):
                                            obj         = tar0.id
                                            path_link   = tar0.data_path
                                            continue

                    break

                tar.id          = obj
                tar.data_path   = path_link
                dr.expression   = f"var[{ind}]"
        else:
            dr = fc.driver
            dr.type = "SCRIPTED"
            if dr.variables:
                v = dr.variables[0]
                v.type = "SINGLE_PROP"
            else:
                v = dr.variables.new()
            tar             = v.targets[0]

            obj             = obj_from
            path_link       = f'modifiers["{escape_identifier(md_from.name)}"].{attr}'

            whilelim = 0
            while whilelim < 999:
                whilelim += 1
                fc_next     = tr_driver(obj, path_link)
                if fc_next is not None:
                    if fc_next.driver.type == 'SCRIPTED':
                        vs  = fc_next.driver.variables
                        if len(vs) == 1:
                            v0      = vs[0]
                            if fc_next.driver.expression == v0.name:
                                tar0        = v0.targets[0]
                                if tar0.id_type == 'OBJECT':
                                    if is_dp_exist(tar0.id, tar0.data_path):
                                        obj         = tar0.id
                                        path_link   = tar0.data_path
                                        continue

                break

            tar.id          = obj
            tar.data_path   = path_link
            dr.expression   = "var"

    s0 = f"modifiers[\\\"{escape_identifier(new_md_to.name)}\\\"]."
    # for attr in attr1:
    #     path = s0 + attr
    #     obj_to[f'modifiers["{new_md_to.name}"].{attr}'] = True
    #     fc = obj_to.driver_add(f'["{path}"]')
    #     dr = fc.driver
    #     dr.type = "SCRIPTED"
    #     if dr.variables:
    #         v = dr.variables[0]
    #         v.type = "SINGLE_PROP"
    #     else:
    #         v = dr.variables.new()
    #     tar             = v.targets[0]

    #     obj             = obj_from
    #     md_name         = md_from.name

    #     whilelim = 0
    #     while whilelim < 999:
    #         whilelim += 1
    #         fc_next     = tr_driver(obj, f'["modifiers[\\\"{escape_identifier(md_name)}\\\"].{attr}"]')
    #         print(f"    link_data  deeplink_modifier:  fc_next={fc_next}")
    #         if fc_next is not None:
    #             if fc_next.driver.type == 'SCRIPTED':
    #                 vs  = fc_next.driver.variables
    #                 if len(vs) == 1:
    #                     v0      = vs[0]
    #                     tar0    = v0.targets[0]
    #                     if tar0.id_type == 'OBJECT':
    #                         obj     = tar0.id
    #                         md_name = v0.name
    #                         continue
    #         break

    #     tar.id          = obj
    #     v.name          = md_name
    #     tar.data_path     = f'modifiers["{escape_identifier(md_name)}"].{attr}'

    #     REFDRIVERS[fc] = obj_to, id(dr)
    #|

def r_md_driver_add(oj, md_name, attr, exp="var", index=None, use_variable=True): # need catch
    # try:
    if index is None:
        dr = tr_driver(oj, f'modifiers["{escape_identifier(md_name)}"].{attr}')
        if dr is None: dr = oj.modifiers[md_name].driver_add(attr)
    else:
        dr = tr_driver(oj, f'modifiers["{escape_identifier(md_name)}"].{attr}', index)
        if dr is None: dr = oj.modifiers[md_name].driver_add(attr, index)

    driver = dr.driver
    driver.type = 'SCRIPTED'
    if use_variable:
        if not driver.variables:
            v = driver.variables.new()
    else:
        if driver.variables:
            variables_remove = driver.variables.remove
            for e in driver.variables:
                variables_remove(e)

    driver.expression = exp
    return dr
    # except: # not animatable
    #     path = f'["modifiers[\\\"{escape_identifier(md_name)}\\\"].{attr}"]'
    #     fc = tr_driver(oj, path)
    #     if fc is None:
    #         oj[f'modifiers["{md_name}"].{attr}'] = True
    #         fc = oj.driver_add(path)

    #     driver = fc.driver
    #     driver.type = 'SCRIPTED'

    #     m.REFDRIVERS[fc] = oj, id(driver)
    #     if driver.variables:
    #         variables_remove = driver.variables.remove
    #         for e in driver.variables:
    #             variables_remove(e)
    #     v = driver.variables.new()
    #     # v.name = md_name
    #     return fc
    #|
def r_md_driver_remove(oj, md_name, attr, index=None): # need refresh
    if index is None:
        success = oj.modifiers[md_name].driver_remove(attr)
    else:
        success = oj.modifiers[md_name].driver_remove(attr, index)

    # if not success:
    #     try:
    #         if not oj.animation_data:           return False
    #         if not oj.animation_data.drivers:   return False

    #         dr = oj.animation_data.drivers.find(f'["modifiers[\\\"{escape_identifier(md_name)}\\\"].{attr}"]')
    #         if dr is None: return False
    #         if dr in m.REFDRIVERS:
    #             del m.REFDRIVERS[dr]

    #         path = f'modifiers["{escape_identifier(md_name)}"].{attr}'
    #         if path in oj:
    #             # del oj[path]
    #             oj.pop(path)

    #         oj.animation_data.drivers.remove(dr)
    #         return True
    #     except:
    #         return False
    return True
    #|
def r_md_driver(oj, md_name, attr, index=None):
    drivers = tr_drivers(oj)
    if drivers:
        if index is None:
            return drivers.find(f'modifiers["{escape_identifier(md_name)}"].{attr}')
        else:
            return drivers.find(f'modifiers["{escape_identifier(md_name)}"].{attr}', index=index)
    return None
    #|
def r_md_refdriver(oj, md_name, attr):
    drivers = tr_drivers(oj)
    if drivers:
        return drivers.find(f'["modifiers[\\\"{escape_identifier(md_name)}\\\"].{attr}"]')
    return None
    #|
def r_md_keyframe_add(oj, md_name, attr, index=None): # need catch
    fc = kf_fcurve_add(tr_action_fcurves(oj), f'modifiers[{md_name}].{attr}', index, None)
    return fc
    #|
def r_md_keyframe(oj, md_name, attr, index=None):
    fcurves = tr_action_fcurves(oj)
    if fcurves:
        if index is None:
            return fcurves.find(f'modifiers["{escape_identifier(md_name)}"].{attr}')
        else:
            return fcurves.find(f'modifiers["{escape_identifier(md_name)}"].{attr}', index=index)
    return None
    #|

def r_code_copy_to_selected(
                            use_code,
                            operation,
                            use_keyframe,
                            use_driver,
                            use_self,
                            self_object,
                            modifiers):
    if use_code:
        s = '# The following Python code can be overridden\n\n'
    else:
        s = '# Enable "Override Code" to run Python Code\n\n'

    s += 'mds = (\n'

    for modifier in modifiers:
        s += f'    "{modifier.name}",\n'

    s += ')\n\nselected_objects = ( # Name, Operation, Keyframe, Driver, MDs, Index (Optional)\n'

    if use_self:
        for ob in bpy.context.selected_objects  if self_object in bpy.context.selected_objects else [
            e  for e in bpy.context.selected_objects] + [self_object]:

            if hasattr(ob, 'library') and ob.library: continue
            if hasattr(ob, 'override_library') and ob.override_library and ob.override_library.is_system_override:
                continue
            if ob.type == 'MESH':
                s += f'    ("{ob.name}", "{operation}", {use_keyframe}, {use_driver}, mds, {len(ob.modifiers)}),\n'
    else:
        for ob in bpy.context.selected_objects:
            if ob == self_object: continue
            if hasattr(ob, 'library') and ob.library: continue
            if hasattr(ob, 'override_library') and ob.override_library and ob.override_library.is_system_override:
                continue
            if ob.type == 'MESH':
                s += f'    ("{ob.name}", "{operation}", {use_keyframe}, {use_driver}, mds, {len(ob.modifiers)}),\n'

    return s + ')'
    #|

def ops_mds_copy_to_object(object_from, object_to, name_mds, operation, use_keyframe, use_driver, index=None):
    lib_mess = r_object_library_message(object_to)
    if lib_mess: return False, lib_mess
    if not hasattr(object_from, "modifiers"): return False, "Source object doesn't have modifiers"
    if not hasattr(object_to, "modifiers"): return False, "Target object doesn't have modifiers"
    if hasattr(object_from, "type") and hasattr(object_to, "type"): pass
    else: return False, "Object Type Error"
    if object_from.type != object_to.type: return False, "Source and target objects are of different types"

    object_from_modifiers = object_from.modifiers
    object_to_modifiers = object_to.modifiers
    fails = []
    copied = []

    if operation == "LINK":
        def fn_use_kfdr(new_modifier, old_modifier):
            link_modifier(object_from, object_to, old_modifier, new_modifier)
    elif operation == "DEEPLINK":
        def fn_use_kfdr(new_modifier, old_modifier):
            deeplink_modifier(object_from, object_to, old_modifier, new_modifier)
    else:
        def fn_use_keyframe(new_modifier, old_modifier):
            try:
                copy_md_keyframe(
                    object_from, object_to, new_modifier,
                    f'modifiers["{escape_identifier(old_modifier.name)}"].', f'modifiers["{escape_identifier(new_modifier.name)}"].')
            except Exception as ex:
                fails.append(f'► Unexpected error, please report to the author  |  {new_modifier.name}  |  {ex}')
            #|
        def fn_use_driver(new_modifier, old_modifier):
            try:
                copy_md_driver(
                    object_from, object_to, new_modifier,
                    f'modifiers["{escape_identifier(old_modifier.name)}"].', f'modifiers["{escape_identifier(new_modifier.name)}"].')
            except Exception as ex:
                fails.append(f'► Unexpected error, please report to the author  |  {new_modifier.name}  |  {ex}')
            #|

        if use_keyframe == False and use_driver == False:
            def fn_use_kfdr(new_modifier, old_modifier): pass
        else:
            if use_keyframe:
                if use_driver:
                    def fn_use_kfdr(new_modifier, old_modifier):
                        fn_use_keyframe(new_modifier, old_modifier)
                        fn_use_driver(new_modifier, old_modifier)
                else:
                    def fn_use_kfdr(new_modifier, old_modifier):
                        fn_use_keyframe(new_modifier, old_modifier)
            else:
                def fn_use_kfdr(new_modifier, old_modifier):
                    fn_use_driver(new_modifier, old_modifier)

    if object_from == object_to:
        with bpy.context.temp_override(object=object_from):
            modifier_copy = bpy.ops.object.modifier_copy
            modifier_move_to_index = bpy.ops.object.modifier_move_to_index

            for md_name in name_mds:
                if md_name not in object_from_modifiers:
                    fails.append(f'{md_name}  |  Modifier not find')
                    continue

                try:
                    if object_from_modifiers[md_name].type == "HOOK":
                        try: modifier_copy(modifier=md_name)
                        except:
                            modifier_copy_HOOK(object_from_modifiers, object_to_modifiers, md_name)
                    else:
                        modifier_copy(modifier=md_name)
                except Exception as ex:
                    fails.append(f'{md_name}  |  {format_exception(ex)}')
                    continue
                new_md = object_from_modifiers.active
                copied.append(new_md)

                try: modifier_move_to_index(modifier=new_md.name, index=len(object_from_modifiers) - 1)
                except Exception as ex:
                    fails.append(f'{new_md.name}  |  {format_exception(ex)}')

                fn_use_kfdr(new_md, object_from_modifiers[md_name])

            if index is not None:
                for e in reversed(copied):
                    try: modifier_move_to_index(modifier=e.name, index=index)
                    except Exception as ex:
                        fails.append(f'{e.name}  |  {format_exception(ex)}')
                for e in copied:
                    i = object_to_modifiers.find(e.name)
                    if i != index:
                        fails.append(f'{e.name}  |  Unexpected order, some items must be at the top')
                    index += 1
    else:
        with bpy.context.temp_override(object=object_from, selected_objects=[object_to]):
            modifier_copy_to_selected = bpy.ops.object.modifier_copy_to_selected

            for md_name in name_mds:
                if md_name not in object_from_modifiers:
                    fails.append(f'{md_name}  |  Modifier not find')
                    continue

                try:
                    if object_from_modifiers[md_name].type == "HOOK":
                        try: modifier_copy_to_selected(modifier=md_name)
                        except:
                            modifier_copy_HOOK(object_from_modifiers, object_to_modifiers, md_name)
                    else:
                        modifier_copy_to_selected(modifier=md_name)
                except Exception as ex:
                    fails.append(f'{md_name}  |  {format_exception(ex)}')
                    continue
                new_md = object_to_modifiers.active
                copied.append(new_md)

                fn_use_kfdr(new_md, object_from_modifiers[md_name])

        if index is not None:
            with bpy.context.temp_override(object=object_to):
                modifier_move_to_index = bpy.ops.object.modifier_move_to_index

                for e in reversed(copied):
                    try: modifier_move_to_index(modifier=e.name, index=index)
                    except Exception as ex:
                        fails.append(f'{e.name}  |  {format_exception(ex)}')
                for e in copied:
                    i = object_to_modifiers.find(e.name)
                    if i != index:
                        fails.append(f'{e.name}  |  Unexpected order, some items must be at the top')
                    index += 1
    return True, fails
    #|
def ops_mds_batch_operation(target_object, md_source, same_md_type, same_md_name, attributes, current_value):
    lib_mess = r_object_library_message(target_object)
    if lib_mess: return False, lib_mess
    if not hasattr(target_object, "type"): return False, "Object Type Error"
    if target_object.type != "MESH": return False, "Object Type Error"

    rnas = md_source.bl_rna.properties
    md_type = md_source.type
    md_name = md_source.name
    mds = target_object.modifiers
    fails = []

    for attr in attributes:
        if isinstance(attr, str): index = None
        elif isinstance(attr, tuple) or isinstance(attr, list):
            if len(attr) != 2:
                fails.append(f'{attr}  |  Length must be equal to 2')
                continue
            attr, index = attr
        else:
            fails.append(f'{attr}  |  Attribute input must be str / tuple / list')
            continue

        if attr not in rnas:
            fails.append(f'{attr}  |  Invalid attribute')
            continue
        rna = rnas[attr]
        if rna.is_readonly:
            fails.append(f'{attr}  |  Read only attribute')
            continue

        if hasattr(rna, "is_array") and rna.is_array:
            for modifier in mds:
                if same_md_type and modifier.type != md_type: continue
                if same_md_name and modifier.name != md_name: continue

                md_rnas = modifier.bl_rna.properties
                if attr not in md_rnas: continue
                md_rna = md_rnas[attr]
                if md_rna.is_readonly: continue
                if not hasattr(md_rna, "is_array") or md_rna.is_array == False:
                    fails.append(f'{target_object.name} : {modifier.name} : {attr} : {index}  |  Target modifier property is not an array')
                    continue

                if index is None:
                    try:
                        setattr(modifier, attr, current_value)
                    except:
                        fails.append(f'{target_object.name} : {modifier.name} : {attr}  |  Failed to set value, skipped')
                else:
                    if not isinstance(index, int):
                        fails.append(f'{target_object.name} : {modifier.name} : {attr} : {index}  |  Index Error')
                        continue

                    if index >= md_rna.array_length:
                        fails.append(f'{target_object.name} : {modifier.name} : {attr} : {index}  |  Out of Index')
                        continue

                    try:
                        getattr(modifier, attr)[index] = current_value
                    except:
                        fails.append(f'{target_object.name} : {modifier.name} : {attr}  |  Failed to set value, skipped')
        else:
            for modifier in mds:
                if same_md_type and modifier.type != md_type: continue
                if same_md_name and modifier.name != md_name: continue

                md_rnas = modifier.bl_rna.properties
                if attr not in md_rnas: continue
                if md_rnas[attr].is_readonly: continue

                try:
                    setattr(modifier, attr, current_value)
                except:
                    fails.append(f'{target_object.name} : {modifier.name} : {attr}  |  Failed to set value, skipped')

    return True, fails
    #|

def modifier_copy_HOOK(object_from_modifiers, object_to_modifiers, md_name):
    md_from = object_from_modifiers[md_name]
    new_md = object_to_modifiers.new(md_name, "HOOK")

    new_md.show_viewport = md_from.show_viewport
    new_md.show_render = md_from.show_render
    new_md.show_in_editmode = md_from.show_in_editmode
    new_md.show_on_cage = md_from.show_on_cage
    new_md.object = md_from.object
    new_md.subtarget = md_from.subtarget
    new_md.vertex_group = md_from.vertex_group
    new_md.invert_vertex_group = md_from.invert_vertex_group
    new_md.strength = md_from.strength
    new_md.falloff_type = md_from.falloff_type
    new_md.falloff_radius = md_from.falloff_radius
    new_md.use_falloff_uniform = md_from.use_falloff_uniform
    new_md.center = md_from.center
    curve_from = md_from.falloff_curve
    curve_new = new_md.falloff_curve

    curve_new.extend = curve_from.extend
    curve_new.tone = curve_from.tone
    curve_new.use_clip = curve_from.use_clip
    curve_new.black_level = curve_from.black_level
    curve_new.white_level = curve_from.white_level

    points_new = curve_new.curves[0].points
    points_from = curve_from.curves[0].points
    for point in points_from:
        e = points_new.new(*point.location)
        e.handle_type = point.handle_type

    curve_new.clip_max_x = curve_from.clip_max_x
    curve_new.clip_max_y = curve_from.clip_max_y
    curve_new.clip_min_x = curve_from.clip_min_x
    curve_new.clip_min_y = curve_from.clip_min_y
    curve_new.update()
    #|


class ModArrayAttr:
    __slots__ = ()
    ARMATURE = ()
    ARRAY = ('constant_offset_displace', 'relative_offset_displace')
    BOOLEAN = ()
    BEVEL = ()
    BUILD = ()
    CAST = ()


    CORRECTIVE_SMOOTH = ()
    CURVE = ()
    DATA_TRANSFER = ()
    DECIMATE = ()
    DISPLACE = ()
    EDGE_SPLIT = ()
    EXPLODE = ()
    HOOK = ()
    LAPLACIANDEFORM = ()
    LAPLACIANSMOOTH = ()
    LATTICE = ()
    MASK = ()
    MESH_CACHE = ()
    MESH_DEFORM = ()
    MESH_SEQUENCE_CACHE = ()
    MIRROR = ('use_axis', 'use_bisect_axis', 'use_bisect_flip_axis')
    MULTIRES = ()
    NODES = ()
    NORMAL_EDIT = ('offset',)
    OCEAN = ()
    PARTICLE_INSTANCE = ()
    REMESH = ()
    SCREW = ()
    SHRINKWRAP = ()
    SIMPLE_DEFORM = ('limits',)
    SKIN = ()
    SMOOTH = ()
    SOLIDIFY = ()
    SUBSURF = ()
    SURFACE_DEFORM = ()
    TRIANGULATE = ()
    UV_PROJECT = ()
    UV_WARP = ('center', 'offset', 'scale')
    VERTEX_WEIGHT_EDIT = ()
    VERTEX_WEIGHT_MIX = ()
    VERTEX_WEIGHT_PROXIMITY = ()
    VOLUME_DISPLACE = ('texture_mid_level',)
    VOLUME_TO_MESH = ()
    WARP = ()
    WAVE = ()
    WEIGHTED_NORMAL = ()
    WELD = ()
    WIREFRAME = ()

    GREASE_PENCIL_TEXTURE = ('fill_offset',)
    GREASE_PENCIL_TIME = ()
    GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY = ()
    GREASE_PENCIL_VERTEX_WEIGHT_ANGLE = ()
    GREASE_PENCIL_ARRAY = (
        'constant_offset',
        'random_offset',
        'random_rotation',
        'random_scale',
        'relative_offset',)
    GREASE_PENCIL_BUILD = ()
    GREASE_PENCIL_DASH = ()
    GREASE_PENCIL_ENVELOPE = ()
    GREASE_PENCIL_LENGTH = ()
    GREASE_PENCIL_MIRROR = ()
    GREASE_PENCIL_MULTIPLY = ()
    GREASE_PENCIL_OUTLINE = ()
    GREASE_PENCIL_SIMPLIFY = ()
    GREASE_PENCIL_SUBDIV = ()
    LINEART = ('use_intersection_mask', 'use_material_mask_bits')
    GREASE_PENCIL_ARMATURE = ()
    GREASE_PENCIL_HOOK = ()
    GREASE_PENCIL_LATTICE = ()
    GREASE_PENCIL_NOISE = ()
    GREASE_PENCIL_OFFSET = (
        'location',
        'rotation',
        'scale',
        'stroke_location',
        'stroke_rotation',
        'stroke_scale',)
    GREASE_PENCIL_SHRINKWRAP = ()
    GREASE_PENCIL_SMOOTH = ()
    GREASE_PENCIL_THICKNESS = ()
    GREASE_PENCIL_COLOR = ()
    GREASE_PENCIL_TINT = ('color',)
    GREASE_PENCIL_OPACITY = ()
    #|
class ModRefAttr:
    __slots__ = ()
    ARMATURE = ('object', 'use_bone_envelopes', 'use_vertex_groups', 'vertex_group',)
    ARRAY = ('curve', 'end_cap', 'offset_object', 'start_cap',)
    BOOLEAN = ('object',)
    BEVEL = ('vertex_group',)
    BUILD = ()
    CAST = ('object', 'vertex_group',)


    CORRECTIVE_SMOOTH = ('vertex_group',)
    CURVE = ('object', 'vertex_group',)
    DATA_TRANSFER = ('object', 'vertex_group',)
    DECIMATE = ('vertex_group',)
    DISPLACE = ('texture', 'texture_coords_bone', 'texture_coords_object', 'uv_layer', 'vertex_group',)
    EDGE_SPLIT = ()
    EXPLODE = ('particle_uv', 'vertex_group',)
    HOOK = ('object', 'subtarget', 'vertex_group',)
    LAPLACIANDEFORM = ('vertex_group',)
    LAPLACIANSMOOTH = ('vertex_group',)
    LATTICE = ('object', 'vertex_group',)
    MASK = ('armature', 'vertex_group',)
    MESH_CACHE = ('filepath', 'vertex_group',)
    MESH_DEFORM = ('object', 'vertex_group',)
    MESH_SEQUENCE_CACHE = ('cache_file', 'object_path',)
    MESH_TO_VOLUME = ('object',)
    MIRROR = ('mirror_object',)
    MULTIRES = ('filepath',)
    NODES = ('node_group',)
    NORMAL_EDIT = ('target', 'vertex_group',)
    OCEAN = (
        'bake_foam_fade',
        'damping',
        'depth',
        'fetch_jonswap',
        'filepath',
        'foam_layer_name',
        'frame_end',
        'frame_start',
        'invert_spray',
        'random_seed',
        'repeat_x',
        'repeat_y',
        'resolution',
        'sharpen_peak_jonswap',
        'spatial_size',
        'spectrum',
        'spray_layer_name',
        'use_foam',
        'use_normals',
        'use_spray',
        'viewport_resolution',
        'wave_alignment',
        'wave_direction',
        'wave_scale_min',
        'wind_velocity',)
    PARTICLE_INSTANCE = ('index_layer_name', 'object', 'particle_system', 'value_layer_name',)
    REMESH = ()
    SCREW = ('object',)
    SHRINKWRAP = ('auxiliary_target', 'target', 'vertex_group',)
    SIMPLE_DEFORM = ('origin', 'vertex_group',)
    SKIN = ()
    SMOOTH = ('vertex_group',)
    SOLIDIFY = ('rim_vertex_group', 'shell_vertex_group', 'vertex_group',)
    SUBSURF = ()
    SURFACE_DEFORM = ('target', 'use_sparse_bind', 'vertex_group',)
    TRIANGULATE = ()
    UV_PROJECT = ('uv_layer',)
    UV_WARP = (
        'bone_from',
        'bone_to',
        'object_from',
        'object_to',
        'uv_layer',
        'vertex_group',)
    VERTEX_WEIGHT_EDIT = (
        'mask_tex_map_bone',
        'mask_tex_map_object',
        'mask_tex_uv_layer',
        'mask_texture',
        'mask_vertex_group',
        'vertex_group',)
    VERTEX_WEIGHT_MIX = (
        'mask_tex_map_bone',
        'mask_tex_map_object',
        'mask_tex_uv_layer',
        'mask_texture',
        'mask_vertex_group',
        'vertex_group_a',
        'vertex_group_b',)
    VERTEX_WEIGHT_PROXIMITY = (
        'mask_tex_map_bone',
        'mask_tex_map_object',
        'mask_tex_uv_layer',
        'mask_texture',
        'mask_vertex_group',
        'target',
        'vertex_group',)
    VOLUME_DISPLACE = ('texture', 'texture_map_object',)
    VOLUME_TO_MESH = ('grid_name', 'object',)
    WARP = (
        'bone_from',
        'bone_to',
        'object_from',
        'object_to',
        'texture',
        'texture_coords_bone',
        'texture_coords_object',
        'uv_layer',
        'vertex_group',)
    WAVE = (
        'start_position_object',
        'texture',
        'texture_coords_bone',
        'texture_coords_object',
        'uv_layer',
        'vertex_group',)
    WEIGHTED_NORMAL = ('vertex_group',)
    WELD = ('vertex_group',)
    WIREFRAME = ('vertex_group',)

    GREASE_PENCIL_TEXTURE = ('layer_filter', 'material_filter', 'vertex_group_name')
    GREASE_PENCIL_TIME = ('frame_end', 'frame_start', 'layer_filter')
    GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY = (
        'layer_filter',
        'material_filter',
        'object',
        'target_vertex_group',
        'vertex_group_name',)
    GREASE_PENCIL_VERTEX_WEIGHT_ANGLE = (
        'layer_filter',
        'material_filter',
        'target_vertex_group',
        'vertex_group_name',)
    GREASE_PENCIL_ARRAY = (
        'layer_filter',
        'material_filter',
        'offset_object',)
    GREASE_PENCIL_BUILD = (
        'layer_filter',
        'material_filter',
        'object',
        'target_vertex_group',)
    GREASE_PENCIL_DASH = ('layer_filter', 'material_filter')
    GREASE_PENCIL_ENVELOPE = (
        'layer_filter',
        'material_filter',
        'vertex_group_name',)
    GREASE_PENCIL_LENGTH = ('layer_filter', 'material_filter')
    GREASE_PENCIL_MIRROR = ('layer_filter', 'material_filter', 'object')
    GREASE_PENCIL_MULTIPLY = ('layer_filter', 'material_filter')
    GREASE_PENCIL_OUTLINE = (
        'layer_filter',
        'material_filter',
        'object',
        'outline_material',)
    GREASE_PENCIL_SIMPLIFY = ()
    GREASE_PENCIL_SUBDIV = ('layer_filter', 'material_filter')
    LINEART = (
        'light_contour_object',
        'source_camera',
        'source_collection',
        'source_object',
        'source_vertex_group',
        'target_layer',
        'target_material',
        'vertex_group',)
    GREASE_PENCIL_ARMATURE = ('object', 'vertex_group_name')
    GREASE_PENCIL_HOOK = (
        'layer_filter',
        'material_filter',
        'object',
        'subtarget',
        'vertex_group_name',)
    GREASE_PENCIL_LATTICE = (
        'layer_filter',
        'material_filter',
        'object',
        'vertex_group_name',)
    GREASE_PENCIL_NOISE = (
        'layer_filter',
        'material_filter',
        'vertex_group_name',)
    GREASE_PENCIL_OFFSET = (
        'layer_filter',
        'material_filter',
        'vertex_group_name',)
    GREASE_PENCIL_SHRINKWRAP = (
        'auxiliary_target',
        'layer_filter',
        'material_filter',
        'target',
        'vertex_group_name',)
    GREASE_PENCIL_SMOOTH = (
        'layer_filter',
        'material_filter',
        'vertex_group_name',)
    GREASE_PENCIL_THICKNESS = (
        'layer_filter',
        'material_filter',
        'vertex_group_name',)
    GREASE_PENCIL_COLOR = ('layer_filter', 'material_filter')
    GREASE_PENCIL_TINT = (
        'layer_filter',
        'material_filter',
        'object',
        'vertex_group_name',)
    GREASE_PENCIL_OPACITY = (
        'layer_filter',
        'material_filter',
        'vertex_group_name',)
    #|
class ModExAttr:
    __slots__ = ()
    EX2 = ('show_viewport', 'show_render')
    EX3 = ('show_in_editmode', 'show_viewport', 'show_render')
    EX4 = ('show_on_cage', 'show_in_editmode', 'show_viewport', 'show_render')

    # /* 0md_ModExAttr_EX4
    ARMATURE = EX4
    ARRAY = EX4
    CAST = EX4
    CORRECTIVE_SMOOTH = EX4
    CURVE = EX4
    DATA_TRANSFER = EX4
    DISPLACE = EX4
    EDGE_SPLIT = EX4
    HOOK = EX4
    LAPLACIANDEFORM = EX4
    LAPLACIANSMOOTH = EX4
    LATTICE = EX4
    MASK = EX4
    MESH_DEFORM = EX4
    MIRROR = EX4
    NODES = EX4
    NORMAL_EDIT = EX4
    SHRINKWRAP = EX4
    SIMPLE_DEFORM = EX4
    SMOOTH = EX4
    SOLIDIFY = EX4
    SUBSURF = EX4
    SURFACE_DEFORM = EX4
    TRIANGULATE = EX4
    UV_PROJECT = EX4
    VERTEX_WEIGHT_EDIT = EX4
    VERTEX_WEIGHT_MIX = EX4
    VERTEX_WEIGHT_PROXIMITY = EX4
    WARP = EX4
    WAVE = EX4
    WEIGHTED_NORMAL = EX4
    WELD = EX4
    # */
    # /* 0md_ModExAttr_EX3
    BOOLEAN = EX3
    BEVEL = EX3
    MESH_CACHE = EX3
    OCEAN = EX3
    PARTICLE_INSTANCE = EX3
    REMESH = EX3
    SCREW = EX3
    SKIN = EX3
    UV_WARP = EX3
    WIREFRAME = EX3
    GREASE_PENCIL_TEXTURE = EX3
    GREASE_PENCIL_TIME = EX3
    GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY = EX3
    GREASE_PENCIL_VERTEX_WEIGHT_ANGLE = EX3
    GREASE_PENCIL_ARRAY = EX3
    GREASE_PENCIL_BUILD = EX3
    GREASE_PENCIL_DASH = EX3
    GREASE_PENCIL_ENVELOPE = EX3
    GREASE_PENCIL_LENGTH = EX3
    GREASE_PENCIL_MIRROR = EX3
    GREASE_PENCIL_MULTIPLY = EX3
    GREASE_PENCIL_OUTLINE = EX3
    GREASE_PENCIL_SIMPLIFY = EX3
    GREASE_PENCIL_SUBDIV = EX3
    LINEART = EX2
    GREASE_PENCIL_ARMATURE = EX3
    GREASE_PENCIL_HOOK = EX3
    GREASE_PENCIL_LATTICE = EX3
    GREASE_PENCIL_NOISE = EX3
    GREASE_PENCIL_OFFSET = EX3
    GREASE_PENCIL_SHRINKWRAP = EX3
    GREASE_PENCIL_SMOOTH = EX3
    GREASE_PENCIL_THICKNESS = EX3
    GREASE_PENCIL_COLOR = EX3
    GREASE_PENCIL_TINT = EX3
    GREASE_PENCIL_OPACITY = EX3
    # */
    # /* 0md_ModExAttr_EX2
    BUILD = EX2
    CLOTH = EX2
    DECIMATE = EX2
    DYNAMIC_PAINT = EX2
    EXPLODE = EX2
    FLUID = EX2
    MESH_SEQUENCE_CACHE = EX2
    MESH_TO_VOLUME = EX2
    MULTIRES = EX2
    PARTICLE_SYSTEM = EX2
    SOFT_BODY = EX2
    VOLUME_DISPLACE = EX2
    VOLUME_TO_MESH = EX2
    # */
class ModAttr:
    __slots__ = ()
    ARMATURE = (
        'invert_vertex_group',
        'use_deform_preserve_volume',
        'use_multi_modifier',)
    ARRAY = (
        'constant_offset_displace',
        'count',
        'fit_length',
        'fit_type',
        'merge_threshold',
        'offset_u',
        'offset_v',
        'relative_offset_displace',
        'use_constant_offset',
        'use_merge_vertices',
        'use_merge_vertices_cap',
        'use_object_offset',
        'use_relative_offset',)
    BOOLEAN = (
        'double_threshold',
        'material_mode',
        'operand_type',
        'operation',
        'solver',
        'use_hole_tolerant',
        'use_self',)
    BEVEL = (
        'affect',
        'angle_limit',
        'face_strength_mode',
        'harden_normals',
        'invert_vertex_group',
        'limit_method',
        'loop_slide',
        'mark_seam',
        'mark_sharp',
        'material',
        'miter_inner',
        'miter_outer',
        'offset_type',
        'profile',
        'profile_type',
        'segments',
        'spread',
        'use_clamp_overlap',
        'vmesh_method',
        'width',
        'width_pct',)
    BUILD = (
        'frame_duration',
        'frame_start',
        'seed',
        'use_random_order',
        'use_reverse',)
    CAST = (
        'cast_type',
        'factor',
        'invert_vertex_group',
        'radius',
        'size',
        'use_radius_as_size',
        'use_transform',
        'use_x',
        'use_y',
        'use_z',)


    CORRECTIVE_SMOOTH = (
        'factor',
        'invert_vertex_group',
        'iterations',
        'rest_source',
        'scale',
        'smooth_type',
        'use_only_smooth',
        'use_pin_boundary',)
    CURVE = (
        'deform_axis',
        'invert_vertex_group',)
    DATA_TRANSFER = (
        'data_types_edges',
        'data_types_loops',
        'data_types_polys',
        'data_types_verts',
        'edge_mapping',
        'invert_vertex_group',
        'islands_precision',
        'layers_uv_select_dst',
        'layers_uv_select_src',
        'layers_vcol_loop_select_dst',
        'layers_vcol_loop_select_src',
        'layers_vcol_vert_select_dst',
        'layers_vcol_vert_select_src',
        'layers_vgroup_select_dst',
        'layers_vgroup_select_src',
        'loop_mapping',
        'max_distance',
        'mix_factor',
        'mix_mode',
        'poly_mapping',
        'ray_radius',
        'use_edge_data',
        'use_loop_data',
        'use_max_distance',
        'use_object_transform',
        'use_poly_data',
        'use_vert_data',
        'vert_mapping',)
    DECIMATE = (
        'angle_limit',
        'decimate_type',
        'delimit',
        'invert_vertex_group',
        'iterations',
        'ratio',
        'symmetry_axis',
        'use_collapse_triangulate',
        'use_dissolve_boundaries',
        'use_symmetry',
        'vertex_group_factor',)
    DISPLACE = (
        'direction',
        'invert_vertex_group',
        'mid_level',
        'space',
        'strength',
        'texture_coords',)
    EDGE_SPLIT = (
        'split_angle',
        'use_edge_angle',
        'use_edge_sharp',)
    EXPLODE = (
        'invert_vertex_group',
        'protect',
        'show_alive',
        'show_dead',
        'show_unborn',
        'use_edge_cut',
        'use_size',)
    HOOK = (
        'center',
        'falloff_radius',
        'falloff_type',
        'invert_vertex_group',
        'strength',
        'use_falloff_uniform',)
    LAPLACIANDEFORM = (
        'invert_vertex_group',
        'iterations',)
    LAPLACIANSMOOTH = (
        'invert_vertex_group',
        'iterations',
        'lambda_border',
        'lambda_factor',
        'use_normalized',
        'use_volume_preserve',
        'use_x',
        'use_y',
        'use_z',)
    LATTICE = (
        'invert_vertex_group',
        'strength',)
    MASK = (
        'invert_vertex_group',
        'mode',
        'threshold',
        'use_smooth',)
    MESH_CACHE = (
        'cache_format',
        'deform_mode',
        'eval_factor',
        'eval_frame',
        'eval_time',
        'factor',
        'flip_axis',
        'forward_axis',
        'frame_scale',
        'frame_start',
        'interpolation',
        'invert_vertex_group',
        'play_mode',
        'time_mode',
        'up_axis',)
    MESH_DEFORM = (
        'invert_vertex_group',
        'precision',
        'use_dynamic_bind',)
    MESH_SEQUENCE_CACHE = (
        'read_data',
        'use_vertex_interpolation',
        'velocity_scale',)
    MESH_TO_VOLUME = (
        'density',
        'interior_band_width',
        'resolution_mode',
        'voxel_amount',
        'voxel_size',)
    MIRROR = (
        'bisect_threshold',
        'merge_threshold',
        'mirror_offset_u',
        'mirror_offset_v',
        'offset_u',
        'offset_v',
        'use_axis',
        'use_bisect_axis',
        'use_bisect_flip_axis',
        'use_clip',
        'use_mirror_merge',
        'use_mirror_u',
        'use_mirror_udim',
        'use_mirror_v',
        'use_mirror_vertex_groups',)
    MULTIRES = (
        'boundary_smooth',
        'levels',
        'quality',
        'render_levels',
        'sculpt_levels',
        'show_only_control_edges',
        'use_creases',
        'use_custom_normals',
        'use_sculpt_base_mesh',
        'uv_smooth',)
    NODES = ()
    NORMAL_EDIT = (
        'invert_vertex_group',
        'mix_factor',
        'mix_limit',
        'mix_mode',
        'mode',
        'no_polynors_fix',
        'offset',
        'use_direction_parallel',)
    OCEAN = (
        'choppiness',
        'foam_coverage',
        'geometry_mode',
        'size',
        'time',
        'wave_scale',)
    PARTICLE_INSTANCE = (
        'axis',
        'particle_amount',
        'particle_offset',
        'particle_system_index',
        'position',
        'random_position',
        'random_rotation',
        'rotation',
        'show_alive',
        'show_dead',
        'show_unborn',
        'space',
        'use_children',
        'use_normal',
        'use_path',
        'use_preserve_shape',
        'use_size',)
    REMESH = (
        'adaptivity',
        'mode',
        'octree_depth',
        'scale',
        'sharpness',
        'threshold',
        'use_remove_disconnected',
        'use_smooth_shade',
        'voxel_size',)
    SCREW = (
        'angle',
        'axis',
        'iterations',
        'merge_threshold',
        'render_steps',
        'screw_offset',
        'steps',
        'use_merge_vertices',
        'use_normal_calculate',
        'use_normal_flip',
        'use_object_screw_offset',
        'use_smooth_shade',
        'use_stretch_u',
        'use_stretch_v',)
    SHRINKWRAP = (
        'cull_face',
        'invert_vertex_group',
        'offset',
        'project_limit',
        'subsurf_levels',
        'use_invert_cull',
        'use_negative_direction',
        'use_positive_direction',
        'use_project_x',
        'use_project_y',
        'use_project_z',
        'wrap_method',
        'wrap_mode',)
    SIMPLE_DEFORM = (
        'angle',
        'deform_axis',
        'deform_method',
        'factor',
        'invert_vertex_group',
        'limits',
        'lock_x',
        'lock_y',
        'lock_z',)
    SKIN = (
        'branch_smoothing',
        'use_smooth_shade',
        'use_x_symmetry',
        'use_y_symmetry',
        'use_z_symmetry',)
    SMOOTH = (
        'factor',
        'invert_vertex_group',
        'iterations',
        'use_x',
        'use_y',
        'use_z',)
    SOLIDIFY = (
        'bevel_convex',
        'edge_crease_inner',
        'edge_crease_outer',
        'edge_crease_rim',
        'invert_vertex_group',
        'material_offset',
        'material_offset_rim',
        'nonmanifold_boundary_mode',
        'nonmanifold_merge_threshold',
        'nonmanifold_thickness_mode',
        'offset',
        'solidify_mode',
        'thickness',
        'thickness_clamp',
        'thickness_vertex_group',
        'use_even_offset',
        'use_flat_faces',
        'use_flip_normals',
        'use_quality_normals',
        'use_rim',
        'use_rim_only',
        'use_thickness_angle_clamp',)
    SUBSURF = (
        'boundary_smooth',
        'levels',
        'quality',
        'render_levels',
        'show_only_control_edges',
        'subdivision_type',
        'use_creases',
        'use_custom_normals',
        'use_limit_surface',
        'uv_smooth',)
    SURFACE_DEFORM = (
        'falloff',
        'invert_vertex_group',
        'strength',)
    TRIANGULATE = None
    UV_PROJECT = (
        'aspect_x',
        'aspect_y',
        'projector_count',
        'scale_x',
        'scale_y',)
    UV_WARP = (
        'axis_u',
        'axis_v',
        'center',
        'invert_vertex_group',
        'offset',
        'rotation',
        'scale',)
    VERTEX_WEIGHT_EDIT = (
        'add_threshold',
        'default_weight',
        'falloff_type',
        'invert_falloff',
        'invert_mask_vertex_group',
        'mask_constant',
        'mask_tex_mapping',
        'mask_tex_use_channel',
        'normalize',
        'remove_threshold',
        'use_add',
        'use_remove',)
    VERTEX_WEIGHT_MIX = (
        'default_weight_a',
        'default_weight_b',
        'invert_mask_vertex_group',
        'invert_vertex_group_a',
        'invert_vertex_group_b',
        'mask_constant',
        'mask_tex_mapping',
        'mask_tex_use_channel',
        'mix_mode',
        'mix_set',
        'normalize',)
    VERTEX_WEIGHT_PROXIMITY = (
        'falloff_type',
        'invert_falloff',
        'invert_mask_vertex_group',
        'mask_constant',
        'mask_tex_mapping',
        'mask_tex_use_channel',
        'max_dist',
        'min_dist',
        'normalize',
        'proximity_geometry',
        'proximity_mode',)
    VOLUME_DISPLACE = (
        'strength',
        'texture_map_mode',
        'texture_mid_level',
        'texture_sample_radius',)
    VOLUME_TO_MESH = (
        'adaptivity',
        'resolution_mode',
        'threshold',
        'use_smooth_shade',
        'voxel_amount',
        'voxel_size',)
    WARP = (
        'falloff_radius',
        'falloff_type',
        'invert_vertex_group',
        'strength',
        'texture_coords',
        'use_volume_preserve',)
    WAVE = (
        'damping_time',
        'falloff_radius',
        'height',
        'invert_vertex_group',
        'lifetime',
        'narrowness',
        'speed',
        'start_position_x',
        'start_position_y',
        'texture_coords',
        'time_offset',
        'use_cyclic',
        'use_normal',
        'use_normal_x',
        'use_normal_y',
        'use_normal_z',
        'use_x',
        'use_y',
        'width',)
    WEIGHTED_NORMAL = (
        'invert_vertex_group',
        'keep_sharp',
        'mode',
        'thresh',
        'use_face_influence',
        'weight',)
    WELD = (
        'invert_vertex_group',
        'loose_edges',
        'merge_threshold',
        'mode',)
    WIREFRAME = (
        'crease_weight',
        'invert_vertex_group',
        'material_offset',
        'offset',
        'thickness',
        'thickness_vertex_group',
        'use_boundary',
        'use_crease',
        'use_even_offset',
        'use_relative_offset',
        'use_replace',)

    GREASE_PENCIL_TEXTURE = (
        'alignment_rotation',
        'fill_offset',
        'fill_rotation',
        'fill_scale',
        'fit_method',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'mode',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'uv_offset',
        'uv_scale',)
    GREASE_PENCIL_TIME = (
        'frame_scale',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'layer_pass_filter',
        'mode',
        'offset',
        'use_custom_frame_range',
        'use_keep_loop',
        'use_layer_pass_filter',)
    GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY = (
        'distance_end',
        'distance_start',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'minimum_weight',
        'use_invert_output',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_multiply',)
    GREASE_PENCIL_VERTEX_WEIGHT_ANGLE = (
        'angle',
        'axis',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'minimum_weight',
        'space',
        'use_invert_output',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_multiply',)
    GREASE_PENCIL_ARRAY = (
        'constant_offset',
        'count',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'material_pass_filter',
        'random_offset',
        'random_rotation',
        'random_scale',
        'relative_offset',
        'replace_material',
        'seed',
        'use_constant_offset',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_object_offset',
        'use_relative_offset',
        'use_uniform_random_scale',)
    GREASE_PENCIL_BUILD = (
        'concurrent_time_alignment',
        'fade_factor',
        'fade_opacity_strength',
        'fade_thickness_strength',
        'frame_end',
        'frame_start',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'length',
        'material_pass_filter',
        'mode',
        'percentage_factor',
        'speed_factor',
        'speed_maxgap',
        'start_delay',
        'time_mode',
        'transition',
        'use_fading',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_restrict_frame_range',)
    GREASE_PENCIL_DASH = (
        'dash_offset',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'material_pass_filter',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    GREASE_PENCIL_ENVELOPE = (
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'mat_nr',
        'material_pass_filter',
        'mode',
        'skip',
        'spread',
        'strength',
        'thickness',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    GREASE_PENCIL_LENGTH = (
        'end_factor',
        'end_length',
        'invert_curvature',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'material_pass_filter',
        'max_angle',
        'mode',
        'overshoot_factor',
        'point_density',
        'random_end_factor',
        'random_offset',
        'random_start_factor',
        'seed',
        'segment_influence',
        'start_factor',
        'start_length',
        'step',
        'use_curvature',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_random',)
    GREASE_PENCIL_MIRROR = (
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'material_pass_filter',
        'use_axis_x',
        'use_axis_y',
        'use_axis_z',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    GREASE_PENCIL_MULTIPLY = (
        'distance',
        'duplicates',
        'fading_center',
        'fading_opacity',
        'fading_thickness',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'material_pass_filter',
        'offset',
        'use_fade',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    GREASE_PENCIL_OUTLINE = (
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'material_pass_filter',
        'sample_length',
        'subdivision',
        'thickness',
        'use_keep_shape',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    GREASE_PENCIL_SIMPLIFY = (
        'mode',
        'step',
        'factor',
        'length',
        'sharp_threshold',
        'distance',)
    GREASE_PENCIL_SUBDIV = (
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'level',
        'material_pass_filter',
        'subdivision_type',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    LINEART = (
        'chaining_image_threshold',
        'crease_threshold',
        'invert_source_vertex_group',
        'level_end',
        'level_start',
        'opacity',
        'overscan',
        'shadow_camera_far',
        'shadow_camera_near',
        'shadow_camera_size',
        'shadow_region_filtering',
        'silhouette_filtering',
        'smooth_tolerance',
        'source_type',
        'split_angle',
        'stroke_depth_offset',
        'thickness',
        'use_back_face_culling',
        'use_cache',
        'use_clip_plane_boundaries',
        'use_contour',
        'use_crease',
        'use_crease_on_sharp',
        'use_crease_on_smooth',
        'use_custom_camera',
        'use_detail_preserve',
        'use_edge_mark',
        'use_edge_overlap',
        'use_face_mark',
        'use_face_mark_boundaries',
        'use_face_mark_invert',
        'use_face_mark_keep_contour',
        'use_fuzzy_all',
        'use_fuzzy_intersections',
        'use_geometry_space_chain',
        'use_image_boundary_trimming',
        'use_intersection',
        'use_intersection_mask',
        'use_intersection_match',
        'use_invert_collection',
        'use_invert_silhouette',
        'use_light_contour',
        'use_loose',
        'use_loose_as_contour',
        'use_loose_edge_chain',
        'use_material',
        'use_material_mask',
        'use_material_mask_bits',
        'use_material_mask_match',
        'use_multiple_levels',
        'use_object_instances',
        'use_offset_towards_custom_camera',
        'use_output_vertex_group_match_by_name',
        'use_overlap_edge_type_support',
        'use_shadow',)
    GREASE_PENCIL_ARMATURE = (
        'invert_vertex_group',
        'use_bone_envelopes',
        # 'use_deform_preserve_volume',
        'use_vertex_groups',)
    GREASE_PENCIL_HOOK = (
        # 'center',
        'falloff_radius',
        'falloff_type',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'strength',
        # 'use_custom_curve',
        'use_falloff_uniform',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    GREASE_PENCIL_LATTICE = (
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'strength',
        'use_layer_pass_filter',
        'use_material_pass_filter',)
    GREASE_PENCIL_NOISE = (
        'factor',
        'factor_strength',
        'factor_thickness',
        'factor_uvs',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'noise_offset',
        'noise_scale',
        'random_mode',
        'seed',
        'step',
        'use_custom_curve',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_random',)
    GREASE_PENCIL_OFFSET = (
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'location',
        'material_pass_filter',
        'offset_mode',
        'rotation',
        'scale',
        'seed',
        'stroke_location',
        'stroke_rotation',
        'stroke_scale',
        'stroke_start_offset',
        'stroke_step',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_uniform_random_scale',)
    GREASE_PENCIL_SHRINKWRAP = (
        'cull_face',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'offset',
        'project_limit',
        'smooth_factor',
        'smooth_step',
        'subsurf_levels',
        'use_invert_cull',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_negative_direction',
        'use_positive_direction',
        'use_project_x',
        'use_project_y',
        'use_project_z',
        'wrap_method',
        'wrap_mode',)
    GREASE_PENCIL_SMOOTH = (
        'factor',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'step',
        # 'use_custom_curve',
        'use_edit_position',
        'use_edit_strength',
        'use_edit_thickness',
        'use_edit_uv',
        'use_keep_shape',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_smooth_ends',)
    GREASE_PENCIL_THICKNESS = (
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'thickness',
        'thickness_factor',
        'use_custom_curve',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_uniform_thickness',
        'use_weight_factor',)
    GREASE_PENCIL_COLOR = (
        'color_mode',
        'hue',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'layer_pass_filter',
        'material_pass_filter',
        'saturation',
        'use_custom_curve',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'value',)
    GREASE_PENCIL_TINT = (
        'color',
        'color_mode',
        'factor',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'radius',
        'tint_mode',
        'use_custom_curve',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_weight_as_factor',)
    GREASE_PENCIL_OPACITY = (
        'color_factor',
        'color_mode',
        'hardness_factor',
        'invert_layer_filter',
        'invert_layer_pass_filter',
        'invert_material_filter',
        'invert_material_pass_filter',
        'invert_vertex_group',
        'layer_pass_filter',
        'material_pass_filter',
        'use_custom_curve',
        'use_layer_pass_filter',
        'use_material_pass_filter',
        'use_uniform_opacity',
        'use_weight_as_factor',)
    #|

if "keep_custom_normals" in TriangulateModifier.bl_rna.properties:
    ModAttr.TRIANGULATE = (
        'keep_custom_normals',
        'min_vertices',
        'ngon_method',
        'quad_method',)
else:
    ModAttr.TRIANGULATE = (
        'min_vertices',
        'ngon_method',
        'quad_method',)

S_md_apply_as_shapekey = {
    'ARMATURE',
    'CAST',
    'CLOTH',
    'COLLISION',
    'CORRECTIVE_SMOOTH',
    'CURVE',
    'DISPLACE',
    'HOOK',
    'LAPLACIANDEFORM',
    'LAPLACIANSMOOTH',
    'LATTICE',
    'MESH_CACHE',
    'MESH_DEFORM',
    'PARTICLE_SYSTEM',
    'SHRINKWRAP',
    'SIMPLE_DEFORM',
    'SMOOTH',
    'SOFT_BODY',
    'SURFACE',
    'SURFACE_DEFORM',
    'WARP',
    'WAVE'}
S_md_apply_on_spline = {
    'ARMATURE',
    'BUILD',
    'CAST',
    'CURVE',
    'DECIMATE',
    'HOOK',
    'LATTICE',
    'MESH_CACHE',
    'MESH_DEFORM',
    'REMESH',
    'SHRINKWRAP',
    'SIMPLE_DEFORM',
    'SMOOTH',
    'SOFT_BODY',
    'WARP',
    'WAVE'}
S_md_only_one = {
    'CLOTH',
    'COLLISION',
    'FLUID',
    'SOFT_BODY'}
S_spline_modifier_types = {"CURVE", "SURFACE"}

if bpy.app.version >= (4, 3, 0):
    ModRefAttr.BEVEL += ('edge_weight', 'vertex_weight')


class ModifierFake:
    def __init__(self, name="", mdtype="",
                show_viewport = False,
                show_render = False,
                show_in_editmode = False,
                show_on_cage = False,
                use_apply_on_spline = False):

        self.rna_type = None
        self.name = name
        self.type = mdtype
        self.show_viewport = show_viewport
        self.show_render = show_render
        self.show_in_editmode = show_in_editmode
        self.show_on_cage = show_on_cage
        self.show_expanded = False
        self.is_active = False
        self.use_pin_to_last = False
        self.is_override_data = False
        self.use_apply_on_spline = use_apply_on_spline
        self.execution_time = 0.0
        self.persistent_uid = 0
        #|
    #|
    #|

## _file_ ##
def late_import():
    #|
    from ..  import VMD

    report = VMD.utilbl.blg.report
    SIZE_border = VMD.utilbl.blg.SIZE_border

    format_exception = VMD.utilbl.general.format_exception

    m = VMD.m
    dd = VMD.dd

    tag_obj_rename = m.tag_obj_rename
    update_data = m.update_data

    md_rns_items = bpy.types.Modifier.bl_rna.properties['type'].enum_items.items()
    md_rnas_MESH[:] = [e  for identifier, e in md_rns_items  if identifier in md_identifiers_MESH]
    md_rnas_CURVE[:] = [e  for identifier, e in md_rns_items  if identifier in md_identifiers_CURVE]
    md_rnas_SURFACE[:] = [e  for identifier, e in md_rns_items  if identifier in md_identifiers_SURFACE]
    md_rnas_VOLUME[:] = [e  for identifier, e in md_rns_items  if identifier in md_identifiers_VOLUME]
    md_rnas_LATTICE[:] = [e  for identifier, e in md_rns_items  if identifier in md_identifiers_LATTICE]
    md_rnas_FONT[:] = [e  for identifier, e in md_rns_items  if identifier in md_identifiers_FONT]
    md_rnas_GREASEPENCIL[:] = [e  for identifier, e in md_rns_items  if identifier in md_identifiers_GREASEPENCIL]

    globals().update(locals())
    #|
