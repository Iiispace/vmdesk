from ..  import VMD
from .  import areas, ed

def reload():
    from importlib import reload

    reload(areas)
    reload(ed)

def late_import():
    areas.late_import()
    ed.late_import()