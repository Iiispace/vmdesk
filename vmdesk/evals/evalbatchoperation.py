import bpy, math

escape_identifier = bpy.utils.escape_identifier

from .. utilbl.md import ops_mds_batch_operation

from . evalutil import r_exec


def eval_batch_operation(self_object, md_source, code):
    try:
        success, localdict = r_exec(code)
        if success is False:
            return False, localdict

        if "selected_objects" not in localdict: return False, "Variable selected_objects missing, canceled"
        if "attributes" not in localdict: return False, "Variable attributes missing, canceled"
        if "set_value_to" not in localdict: return False, "Variable set_value_to missing, canceled"
        if not localdict["selected_objects"]: return False, "Object list is empty, canceled"
        if not localdict["attributes"]: return False, "attribute list is empty, canceled"

        obj_fails = []
        bpy_data_objects = bpy.data.objects

        for object_data in localdict["selected_objects"]:
            name, same_md_type, same_md_name = object_data

            if name not in bpy_data_objects:
                obj_fails.append(f'{name} not find')
                continue

            success, fails = ops_mds_batch_operation(bpy_data_objects[name],
                md_source, same_md_type, same_md_name, localdict["attributes"], localdict["set_value_to"])

            if fails:
                if isinstance(fails, str):
                    obj_fails.append(f"    {name}\n        {fails}")
                else:
                    obj_fails.append(f"    {name}\n        " + "\n        ".join(fails))

        if obj_fails:
            return True, f"{len(obj_fails)} Object(s) failed :\n" + "\n".join(obj_fails)
    except Exception as exx:
        return False, str(exx)

    return True, ""
    #|

def r_code_batch_operation(self_object, pp, datapath, current_value):
    if pp.Use_code:
        s = '# The following Python code can be overridden\n\n'
    else:
        s = '# Enable "Override Code" to run Python Code\n\n'

    s += f'set_value_to = {datapath}\n# {current_value}\n\n'
    s += 'selected_objects = ( # Name, Same MD Type, Same MD Name\n'

    same_md_type = pp.Only_same_type
    same_md_name = pp.Only_same_name

    if pp.Affect_self_object: s += f'    ("{escape_identifier(self_object.name)}", {same_md_type}, {same_md_name}),\n'
    if pp.Affect_selected_objects:
        for ob in bpy.context.selected_objects:
            if ob == self_object: continue
            if ob.type != "MESH": continue
            if ob.library: continue
            s += f'    ("{escape_identifier(ob.name)}", {same_md_type}, {same_md_name}),\n'

    s += ')\n\nattributes = (\n'

    for at in dir(pp):
        if at[0].isupper() or at.startswith("_"): continue

        if getattr(pp, at):
            if at[-1] in "0123456789":
                s += f'    ("{at[ : -1]}", {at[-1]}),\n'
            else:
                s += f'    "{at}",\n'

    return s + ')'
    #|
