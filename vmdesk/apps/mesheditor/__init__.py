from ..  import VMD
from .  import prop, ops, ed

def reload():
    from importlib import reload

    reload(prop)
    reload(ops)
    reload(ed)

def late_import():
    ops.late_import()
    ed.late_import()