_info = {
    "name" : "vmdesk",
    "author" : "LAW.Y.T",
    "version" : (2, 2, 0),
    "blender" : (4, 2),
    "location" : "View3d > Tool",
    "warning" : "",
    "description" : "Requirement: blender 4.2",
    "wiki_url" : "",
    "category" : "3D View",
}

if "bpy" in locals():
    from importlib import reload

    # ICon WIll NOt REload
    #######

    # 1forfile (_allfile_,, $lambda _file_, _cls_: f'{"#" if _file_[1] == "_" else "reload"}(VMD.{_file_[ 1 : -3].replace(chr(92), ".")})\n'$)

    reload(api)
    reload(blprop)
    reload(txt)
    reload(types)
    reload(num)
    reload(deco)
    reload(const)
    reload(com)
    reload(dirlib)
    reload(filtexp)
    reload(algebra)

    reload(glshader)
    reload(pymath)
    reload(ops)
    reload(calc)
    reload(general)
    reload(md)
    reload(mesh)
    reload(blg)

    reload(evalutil)
    reload(evalbatchoperation)
    reload(evalcopytoselected)
    reload(evalmdlib)

    reload(colorlist)
    reload(keysys)
    reload(prefs)
    reload(npanel)
    reload(userops)
    reload(rna)
    reload(handle)
    reload(win)
    reload(area)
    reload(block)
    reload(blocklist)
    reload(dd)
    reload(m)


    reload(apps)
    apps.reload()














    #######


import bpy
register_class = bpy.utils.register_class
unregister_class = bpy.utils.unregister_class
EnumProperty = bpy.props.EnumProperty


from .  import api, blprop
from . util import (
    txt,
    types,
    num,
    deco,
    const,
    com,
    dirlib,
    filtexp,
    algebra,
)
from . utilbl import (
    glshader,
    pymath,
    ops,
    calc,
    general,
    md,
    mesh,
    blg,
)
from . evals import (
    evalutil,
    evalbatchoperation,
    evalcopytoselected,
    evalmdlib,
)
from .  import (
    colorlist,
    keysys,
    prefs,
    npanel,
    userops,
    rna,
    handle,
    win,
    area,
    block,
    blocklist,
    dd,
    m,
)

from . handle import load_post, load_pre
from .  import evals, util, utilbl
from ..  import VMD

from .  import apps

def register():
    (print("register()"))
    #|
    handle.BL_INFO.update(_info)

    for cls in prefs.classes:
        register_class(cls)

    register_class(m.Blocking)
    register_class(m.Admin)


    handlers = bpy.app.handlers
    if load_post not in handlers.load_post: handlers.load_post.append(load_post)
    if load_pre not in handlers.load_pre: handlers.load_pre.append(load_pre)

    handle.late_import()
    handle.bl_load()

    m.late_import()
    handle.TAG_UPDATE = m.TAG_UPDATE

    keysys.late_import()
    keysys.init_keymaps(m.P)
    keysys.init_calc_exp(m.P)
    m.UnitSystem.update()

    blg.late_import()
    m.import_size()

    rna.late_import()
    general.late_import()
    userops.late_import()
    prefs.late_import()
    npanel.late_import()
    md.late_import()
    area.late_import()
    block.late_import()
    blocklist.late_import()
    dd.late_import()
    win.late_import()

    m.late_import_lv2()

    apps.late_import()

    handle.newfile_event()



    for cls in ops.classes:
        register_class(cls)

    register_class(npanel.VmdPanel)

    id_class = EnumProperty(
        name = "Class",
        description = "Editor Type",
        items = [(k, e.name, "")  for k, e in m.D_EDITOR.items()],
        options = set())

    userops.OpsEditor.__annotations__['id_class'] = id_class

    for cls in m.OPERATORS:
        register_class(cls)


















    #|

def unregister():

    #|
    from bpy.utils import unregister_class

    handle.bl_unload()

    for cls in prefs.classes:
        unregister_class(cls)

    unregister_class(m.Blocking)
    unregister_class(m.Admin)

    for cls in ops.classes:
        unregister_class(cls)

    unregister_class(npanel.VmdPanel)
    for cls in m.OPERATORS:
        unregister_class(cls)

    # ---------------------------------------------------------------------------------------------------------












    # ---------------------------------------------------------------------------------------------------------

    handlers = bpy.app.handlers
    if load_post in handlers.load_post: handlers.load_post.remove(load_post)
    if load_pre in handlers.load_pre: handlers.load_pre.remove(load_pre)

    m.P = None
    m.ADMIN = None

    # -- DoN'T RemovE ThiS, OtherwisE faileD tO deletE fonT fileS resultinG iN faileD unregisteR
    pref_view = bpy.context.preferences.view
    pref_view.use_text_antialiasing = pref_view.use_text_antialiasing
    # --
    #|
