from ..  import VMD
from .  import (
    dreditor,
    mdeditor,
    mesheditor,
    settingeditor,
)

def reload():
    from importlib import reload

    reload(dreditor)
    reload(mdeditor)
    reload(mesheditor)
    reload(settingeditor)

    dreditor.reload()
    mdeditor.reload()
    mesheditor.reload()
    settingeditor.reload()

def late_import():
    dreditor.late_import()
    mdeditor.late_import()
    mesheditor.late_import()
    settingeditor.late_import()