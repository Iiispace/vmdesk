import bpy
from bpy.utils import escape_identifier, unescape_identifier
from bpy.types import CollectionProperty, BlendData
from os.path import join as os_path_join

from .. util.deco import catchNone


def format_exception(ex):
    ss = str(ex).split('poll()', 1)
    return ss if len(ss) == 1 else ss[1].lstrip()
    #|

def r_obj_path_by_full_path(path):
    try:
        # names = {e.identifier for e in BlendData.bl_rna.properties  if isinstance(e, CollectionProperty)}

        ind_data = path.find("data.")

        ind_obj_start = ind_data + 5
        ind_obj_end = path.find("[", ind_obj_start)
        bpy_colls = getattr(bpy.data, path[ind_obj_start : ind_obj_end])

        ind_name_start = ind_obj_end + 1
        ind_name_end = path.find("]", ind_name_start)
        tar_obj = bpy_colls[unescape_identifier(path[ind_name_start + 1 : ind_name_end - 1])]
        dr_path = path[ind_name_end + 2 :]  if path[ind_name_end + 1] == "." else path[ind_name_end + 1 :]
        return tar_obj, dr_path
    except: return None, None
    #|
def r_ID_dp(obj):
    try:
        s = repr(obj)
        if s.startswith("bpy.data."): pass
        else: return ""
        i = s.find("[")

        if hasattr(obj, "library") and obj.library:
            return f'{s[ : i]}["{escape_identifier(obj.name)}", "{escape_identifier(obj.library.filepath)}"]'
        else:
            return f'{s[ : i]}["{escape_identifier(obj.name)}"]'
    except:
        return ""
    #|
def r_id_type(obj):
    try:
        s = repr(obj)
        if s.startswith("bpy.data."): pass
        else: return None
        i = s.find("[")

        return D_blendData_id[s[9 : i]]
    except: return None
    #|

def r_add_to_keying_set(ob, dp, index=None, undo_push=True):
    try:
        keying_sets = bpy.context.scene.keying_sets
        act_ks = keying_sets.active
        if act_ks is None:
            act_ks = keying_sets.new(idname='Button Keying Set', name='Button Keying Set')
            # act_ks.use_insertkey_xyz_to_rgb = True # removed:4.1
            # act_ks.use_insertkey_override_xyz_to_rgb = True # removed:4.1

        kspath = act_ks.paths.add(ob, dp)
        if not kspath: return False, "Failed to add keying set, path may already exist"

        if index is not None:
            if index == "all":
                kspath.use_entire_array = True
            else:
                kspath.use_entire_array = False
                kspath.array_index = index
        keying_sets.active = keying_sets.active
        if undo_push:
            ed_undo_push(message="Add to Keying Set")
        blg.report(f'Property added to Keying Set: "{act_ks.bl_idname}" | {dp}')
        return True, ""
    except Exception as ex:
        return False, str(ex)
    #|
def r_remove_from_keying_set(ob, dp, index=None, undo_push=True):
    try:
        keying_sets = bpy.context.scene.keying_sets
        act_ks = keying_sets.active
        if act_ks is None:
            return False, "Keying Set not find"

        paths = act_ks.paths
        tag = False
        if index is None:
            for p in paths:
                if p.id != ob: continue
                if p.data_path != dp: continue
                paths.remove(p)
                tag = True
        elif index == "all":
            for p in paths:
                if p.id != ob: continue
                if p.data_path != dp: continue
                if p.use_entire_array:
                    paths.remove(p)
                    tag = True
        else:
            for p in paths:
                if p.id != ob: continue
                if p.data_path != dp: continue
                if p.use_entire_array: continue
                if p.array_index == index:
                    paths.remove(p)
                    tag = True

        if tag:
            keying_sets.active = keying_sets.active
            if undo_push:
                ed_undo_push(message="Remove from Keying Set")
            blg.report(f'Property removed from Keying Set: "{act_ks.bl_idname}" | {dp}')
            return True, ""
        else:
            return False, "Keying Set not find"
    except Exception as ex:
        return False, str(ex)
    #|

def r_library_or_override_message(ob):
    if hasattr(ob, "library") and ob.library:
        return "This operation cannot be performed \nfrom a linked data-block"
    if hasattr(ob, 'override_library') and ob.override_library and ob.override_library.is_system_override:
        return "This operation cannot be performed \nfrom a system override data-block"
    return ""
    #|
def r_library_editable(ob):
    if hasattr(ob, "library") and ob.library:
        return False
    if hasattr(ob, 'override_library') and ob.override_library and ob.override_library.is_system_override:
        return False
    return True
    #|
def r_unsupport_override_message(ob):
    if hasattr(ob, 'override_library') and ob.override_library:
        return "Current data-block unsupported overridden"
    return ""
    #|
def is_allow_remove_modifier(ob, modifier):
    if ob.is_editable == False: return False
    if hasattr(modifier, "is_override_data") and modifier.is_override_data:
        if hasattr(ob, "override_library") and ob.override_library:
            return False
    return True
    #|

# Performance
#   repr            Fast
#   path_from_id    Faster
#   fstring Fn      Fastest
def dp_repr(pp, base):
    s0 = repr(pp)
    s1 = repr(base)
    if s0.startswith("bpy.context."):
        s1 = repr(P)

    s = s0.replace(s1, "")
    return s[1 : ]  if s.startswith(".") else s
    #|
def dpf_repr(pp, base):
    s0 = repr(pp)
    s1 = repr(base)
    if s1.startswith("bpy.data."): pass
    elif s0.startswith("bpy.context."):
        return s0
    else:
        raise ValueError("dpf_repr() invalid input")

    i0 = s1.find("[")
    i1 = s1.find("]")
    if hasattr(base, "library") and base.library:
        return f'{s1[ : i0]}["{escape_identifier(base.name)}", "{escape_identifier(base.library.filepath)}"]{s0.replace(s1, "")}'
    else:
        return f'{s1[ : i0]}["{escape_identifier(base.name)}"]{s0.replace(s1, "")}'
    #|
def datapath_split(dp):
    # 'modifiers["x.x"].hide'       'modifiers["x.x"]', 'hide'
    # 'location'                    '', 'location'
    # '["ab"]["x.\\"x"]'            '["ab"]', '["x.\\"x"]'

    if dp.endswith('"]'):
        i0 = dp.rfind('["', 0, -2)
        if i0 == -1: return "", dp
        return dp[ : i0], dp[i0 : ]

    i0 = dp.rfind('.')
    if i0 == -1: return "", dp
    return dp[ : i0], dp[i0 + 1 : ]
    #|
def is_array_fcurve(ob, fc):
    try:
        v = ob.path_resolve(fc.data_path)
    except:
        return False

    if isinstance(v, str): return False
    return hasattr(v, "__len__")
    #|
def r_fcurve_name(ob, fc):
    at0, at1 = datapath_split(fc.data_path)

    if at0:
        try:
            ob = ob.path_resolve(at0)
        except:
            return None

    if hasattr(ob, "bl_rna"):
        rnas = ob.bl_rna.properties
        if at1 in rnas:
            rna = rnas[at1]
            if hasattr(rna, "name"):
                return rna.name

    return None
    #|

def r_override_value(base, dp):
    if hasattr(base, "override_library"):
        if hasattr(base.override_library, "reference") and hasattr(base.override_library.reference, "path_resolve"):
            return True, base.override_library.reference.path_resolve(dp)
    return False, None
    #|
def r_dp_with(pp, base, identifier):
    if identifier[0].isalpha():
        dph = dp_repr(pp, base)
        if dph:
            return f'{dph}.{identifier}'
        return identifier
    return f'{dp_repr(pp, base)}{identifier}'
    #|
def r_dpf_with(pp, base, identifier):
    if identifier[0].isalpha():
        return f'{dpf_repr(pp, base)}.{identifier}'
    return f'{dpf_repr(pp, base)}{identifier}'
    #|
def is_value_overridden(pp, base, identifier, index=None):
    dp = r_dp_with(pp, base, identifier)
    success, v_ref = r_override_value(base, dp)
    if success is False: return False

    if not isinstance(v_ref, str) and hasattr(v_ref, "__len__"):
        if index is None:
            if v_ref[:] == base.path_resolve(dp)[:]: return False
        else:
            if v_ref[index] == base.path_resolve(dp)[index]: return False
    else:
        if v_ref == base.path_resolve(dp): return False
    return True
    #|

def r_driver_fc(ob, dp, index=None):
    if hasattr(ob, "animation_data"):
        if hasattr(ob.animation_data, "drivers"):
            if hasattr(ob.animation_data.drivers, "find"):
                if index is None:
                    return ob.animation_data.drivers.find(dp)
                return ob.animation_data.drivers.find(dp, index=index)
    return None
    #|
def r_action_fc(ob, dp, index=None):
    if hasattr(ob, "animation_data"):
        if hasattr(ob.animation_data, "action"):
            if hasattr(ob.animation_data.action, "fcurves"):
                if hasattr(ob.animation_data.action.fcurves, "find"):
                    if index is None:
                        return ob.animation_data.action.fcurves.find(dp)
                    return ob.animation_data.action.fcurves.find(dp, index=index)
    return None
    #|
def is_vec(v):
    if isinstance(v, str): return False
    return hasattr(v, "__len__")
    #|

def is_allow_add_driver(ob, dp_head, attr, pp=None):
    try:
        if pp is None:
            if dp_head:
                pp = ob.path_resolve(dp_head[ : -1]  if dp_head.endswith(".") else dp_head)
            else:
                pp = ob

        if not pp:
            is_allow_add_driver.message = "Path not found"
            return False

        if attr in pp.bl_rna.properties:
            rna = pp.bl_rna.properties[attr]
            if hasattr(rna, "is_readonly") and rna.is_readonly:
                is_allow_add_driver.message = "Property is readonly"
                return False

            if hasattr(rna, "is_animatable") and rna.is_animatable == False:
                is_allow_add_driver.message = "Property is not animatable"
                return False

        is_override_library = True  if hasattr(ob, 'override_library') and ob.override_library else False

        if isinstance(pp, Modifier):
            if attr == "show_viewport":
                is_allow_add_driver.message = ""
                return True

            if attr in {"show_in_editmode", "show_on_cage", "use_apply_on_spline"}:
                if is_override_library and hasattr(pp, "is_override_data") and pp.is_override_data:
                    is_allow_add_driver.message = "Override data is not animatable"
                    return False

            if ob.is_editable == False or (is_override_library and ob.override_library.is_system_override):
                is_allow_add_driver.message = "Linked data is not animatable"
                return False
        else:
            if ob.is_editable == False or (is_override_library and ob.override_library.is_system_override):
                is_allow_add_driver.message = "Linked data is not animatable"
                return False

        is_allow_add_driver.message = ""
        return True
    except Exception as ex:
        is_allow_add_driver.message = str(ex)
        return False
    #|
@ catchNone
def r_driver_add_safe(ob, dp_head, attr, exp="var", index=None, use_variable=True):
    if dp_head:
        pp = ob.path_resolve(dp_head[ : -1]  if dp_head.endswith(".") else dp_head)
    else:
        pp = ob

    if is_allow_add_driver(ob, dp_head, attr, pp=pp) is False: return None

    if index is None:
        dr = tr_driver(ob, dp_head + attr)
        if dr: return None
        dr = pp.driver_add(attr)
    else:
        dr = pp.driver_add(attr, index)
        if dr: return None

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
    #|


def update_scene():
    bpy.context.scene.update_tag()
    P.refresh = True
    Admin.REDRAW()
    update_data()
    #|
def update_scene_push(push_message=""):
    bpy.context.scene.update_tag()
    P.refresh = True
    Admin.REDRAW()
    update_data()
    ed_undo_push(message=push_message)
    #|

class FakeDriverTarget:
    __slots__ = (
        'bone_target',
        'context_property',
        'data_path',
        'id',
        'id_type',
        'rotation_mode',
        'transform_space',
        'transform_type')
    #|
    #|
class FakeDriverVariable:
    __slots__ = (
        'is_name_valid',
        'name',
        'targets',
        'type')

    def __init__(self, len_target):
        self.targets = [FakeDriverTarget() for _ in range(len_target)]
        #|
    #|
    #|

def copy_driver_variable(v_from, v_to, copy_name=True):
    v_to.type   = v_from.type
    if copy_name:
        v_to.name   = v_from.name

    tar_to      = v_to.targets[0]
    tar_from    = v_from.targets[0]

    try:
        tar_to.id_type          = tar_from.id_type
    except: pass
    tar_to.id               = tar_from.id
    tar_to.data_path        = tar_from.data_path
    tar_to.rotation_mode    = tar_from.rotation_mode
    tar_to.transform_type   = tar_from.transform_type
    tar_to.transform_space  = tar_from.transform_space
    tar_to.bone_target      = tar_from.bone_target
    tar_to.context_property = tar_from.context_property

    if len(v_from.targets) == 2:
        tar_to      = v_to.targets[1]
        tar_from    = v_from.targets[1]

        try:
            tar_to.id_type          = tar_from.id_type
        except: pass
        tar_to.id               = tar_from.id
        tar_to.data_path        = tar_from.data_path
        tar_to.rotation_mode    = tar_from.rotation_mode
        tar_to.transform_type   = tar_from.transform_type
        tar_to.transform_space  = tar_from.transform_space
        tar_to.bone_target      = tar_from.bone_target
        tar_to.context_property = tar_from.context_property
    #|
def driver_var_move_to_index(var_name, index):
    variables = driver_var_move_to_index.variables
    old_index = variables.find(var_name)
    if old_index == index: return

    dic = {e: k  for k, e in variables.items()}
    temp_var = FakeDriverVariable(len(variables[old_index].targets))
    copy_driver_variable(variables[old_index], temp_var, False)

    if index > old_index:
        for r in range(old_index, index):
            dic[variables[r]] = variables[r + 1].name
            copy_driver_variable(variables[r + 1], variables[r], False)

        dic[variables[index]] = variables[old_index].name
        copy_driver_variable(temp_var, variables[index], False)
    else:
        for r in range(old_index, index, -1):
            dic[variables[r]] = variables[r - 1].name
            copy_driver_variable(variables[r - 1], variables[r], False)

        dic[variables[index]] = variables[old_index].name
        copy_driver_variable(temp_var, variables[index], False)


    name_set = {e  for e in dic.values()}
    for e in variables.values():
        i = 0
        while True:
            new_name = str(i)
            i += 1
            if new_name in name_set: continue

            e.name = new_name
            name_set.add(new_name)
            break

    for e in variables.values():
        e.name = dic[e]
    #|
def driver_var_name_set(variables, variable, name):
    if name in variables:
        i = 0
        while True:
            new_name = f"{name}_{i}"
            if len(new_name) >= 63:
                i = 0
                name = "var"
                new_name = f"{name}_{i}"
            if new_name in variables:
                i += 1
                continue

            variable.name = new_name
            break
        return False
    else:
        variable.name = name
        return True
    #|


def rr_enum_items_vgroup(r_object):
    def r_enum_items_vgroup():
        ob = r_object()
        if hasattr(ob, "vertex_groups"):
            if hasattr(ob.vertex_groups, "__contains__"):
                return ob.vertex_groups
        return {}
    return r_enum_items_vgroup
    #|
def rr_enum_items_uv(r_object):
    def r_enum_items_uv():
        ob = r_object()
        if hasattr(ob, "data") and hasattr(ob.data, "uv_layers"):
            if hasattr(ob.data.uv_layers, "__contains__"):
                return ob.data.uv_layers
        return {}
    return r_enum_items_uv
    #|
def rr_enum_items_vertex_color(r_object):
    def r_enum_items_vertex_color():
        ob = r_object()
        if hasattr(ob, "data") and hasattr(ob.data, "vertex_colors"):
            if hasattr(ob.data.vertex_colors, "__contains__"):
                return ob.data.vertex_colors
        return {}
    return r_enum_items_vertex_color


def bpy_data_append(file_path, inner_path, name, link=False):
    if file_path == bpy.data.filepath:
        raise ValueError("Invalid file path")
        return

    bpy.ops.wm.append(
        filepath = os_path_join(file_path, inner_path, name),
        directory = os_path_join(file_path, inner_path),
        filename = name,
        link = link)
    #|


def bl_NodeSocket_compare(socket0, socket1, lookup0, lookup1):
    if socket0.bl_idname != socket1.bl_idname: return False
    if socket0.enabled != socket1.enabled: return False
    if socket0.hide != socket1.hide: return False
    if socket0.hide_value != socket1.hide_value: return False
    if socket0.type != socket1.type: return False

    if len(socket0.links) != len(socket1.links): return False
    return True
    #|
def bl_Node_compare(node0, node1, lookup0, lookup1):
    if node0.bl_idname != node1.bl_idname: return False
    if node0.hide != node1.hide: return False
    if node0.mute != node1.mute: return False

    if len(node0.inputs) != node1.inputs: return False
    if len(node0.outputs) != node1.outputs: return False

    if any(bl_NodeSocket_compare(e0, e1, lookup0, lookup1) is False
        for e0, e1 in zip(node0.inputs, node1.inputs)): return False

    if any(bl_NodeSocket_compare(e0, e1, lookup0, lookup1) is False
        for e0, e1 in zip(node0.outputs, node1.outputs)): return False
    return True
    #|
def bl_NodeLink_compare(link0, link1):
    TODO
    return True
    #|
def bl_NodeTreeInterfaceItem_compare(it0, it1):
    TODO
    return True
    #|
def bl_NodeTree_compare(tree0, tree1):
    return tree0 == tree1
    if tree0.bl_idname != tree1.bl_idname: return False

    if len(tree0.nodes) != len(tree1.nodes): return False
    if len(tree0.links) != len(tree1.links): return False
    if len(tree0.interface.items_tree) != len(tree1.interface.items_tree): return False

    lookup0 = {e: k  for k, e in tree0.nodes.items()}
    lookup1 = {e: k  for k, e in tree1.nodes.items()}

    if any(bl_Node_compare(e0, e1, lookup0, lookup1) is False
        for e0, e1 in zip(tree0.nodes, tree1.nodes)): return False

    if any(bl_NodeLink_compare(e0, e1) is False
        for e0, e1 in zip(tree0.links, tree1.links)): return False

    if any(bl_NodeTreeInterfaceItem_compare(e0, e1) is False
        for e0, e1 in zip(tree0.interface.items_tree, tree1.interface.items_tree)): return False


    return True
    #|


## _file_ ##
def late_import():
    #|
    import bpy
    Modifier = bpy.types.Modifier

    from ..  import VMD

    # <<< 1mp (VMD.api
    api = VMD.api
    D_cls_blendData = api.D_cls_blendData
    D_blendData_id = api.D_blendData_id
    D_cls_id = api.D_cls_id
    # >>>

    # <<< 1mp (VMD.m
    m = VMD.m
    P = m.P
    Admin = m.Admin
    update_data = m.update_data
    # >>>

    blg = VMD.utilbl.blg
    tr_driver = VMD.utilbl.md.tr_driver

    ed_undo_push = bpy.ops.ed.undo_push

    globals().update(locals())
    #|
