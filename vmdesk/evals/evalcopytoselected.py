import bpy
from .. utilbl.md import ops_mds_copy_to_object

from . evalutil import r_exec


def eval_copy_to_selected(self_object, code):
    try:
        success, localdict = r_exec(code)
        if success is False:
            return False, localdict

        if "selected_objects" not in localdict: return False, "Variable selected_objects missing, canceled"
        if not localdict["selected_objects"]: return True, "Object list is empty, canceled"

        obj_fails = []
        bpy_data_objects = bpy.data.objects

        for object_data in localdict["selected_objects"]:
            if len(object_data) == 6:
                name, operation, use_keyframe, use_driver, modifiers, index = object_data
            else:
                name, operation, use_keyframe, use_driver, modifiers = object_data
                index = None

            if name not in bpy_data_objects:
                obj_fails.append(f'{name} not find')
                continue

            success, fails = ops_mds_copy_to_object(
                self_object, bpy_data_objects[name], modifiers, operation, use_keyframe, use_driver, index=index)

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
