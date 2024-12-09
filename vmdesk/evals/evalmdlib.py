import bpy

from . evalutil import r_exec


def eval_md_lib(code):
    try:
        success, localdict = r_exec(code)
        if success is False:
            return None, localdict

        if "directories" in localdict: return localdict["directories"], ""

        return None, 'Local variable "directories" requires'
    except Exception as exx:
        return None, str(exx)

    return None, "Unknown Error"
    #|
