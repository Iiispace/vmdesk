from ..  import VMD
from .  import prop, ed

def reload():
    from importlib import reload

    reload(prop)
    reload(ed)

def late_import():
    prop.late_import()
    ed.late_import()