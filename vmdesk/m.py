











import bpy, _bpy, blf

blfSize = blf.size
blfColor = blf.color
blfPos = blf.position
blfDraw = blf.draw
blfDimen = blf.dimensions
blfEnable = blf.enable
blfDisable = blf.disable
blfSHADOW = blf.SHADOW
blfShadow = blf.shadow
blfShadowOffset = blf.shadow_offset

bpytypes = bpy.types

# <<< 1mp (bpytypes
Operator = bpytypes.Operator
SpaceView3D = bpytypes.SpaceView3D
Object = bpytypes.Object
TOPBAR_HT_upper_bar = bpytypes.TOPBAR_HT_upper_bar
# >>>

from gpu.state import blend_set

depsgraph_update_post = bpy.app.handlers.depsgraph_update_post
frame_change_post = bpy.app.handlers.frame_change_post

units_to_value = bpy.utils.units.to_value
units_to_string = bpy.utils.units.to_string

from math import floor
from collections import OrderedDict
from pathlib import Path
from weakref import WeakValueDictionary
from os.path import join as os_path_join
from os import sep as os_sep

from .  import util, userops

# <<< 1mp (util.deco
deco = util.deco
successResult = deco.successResult
catchStr = deco.catchStr
# >>>

Dictlist = util.types.Dictlist

OPERATORS = list(userops.classes)
D_EDITOR = Dictlist([])

def font_shadow_default():
    blfEnable(FONT0, blfSHADOW)
    blfShadow(FONT0, 3, 0.0, 0.0, 0.0, 1.0)
    blfShadowOffset(FONT0, 0, 0)
    #|
def font_shadow_custom():
    blfEnable(FONT0, blfSHADOW)
    blfShadow(FONT0, font_shadow_custom.blurlevel, font_shadow_custom.r, font_shadow_custom.g, font_shadow_custom.b, font_shadow_custom.a)
    blfShadowOffset(FONT0, font_shadow_custom.offset_x, font_shadow_custom.offset_y)
    #|
font_shadow_custom.blurlevel = 3
font_shadow_custom.r = 0.0
font_shadow_custom.g = 0.0
font_shadow_custom.b = 0.0
font_shadow_custom.a = 1.0
font_shadow_custom.offset_x = 0
font_shadow_custom.offset_y = 0

TEXT_RENDER = font_shadow_default
def make_TEXT_RENDER():
    global TEXT_RENDER
    if P.font_shadow_method == "NONE":
        TEXT_RENDER = N
        blfDisable(FONT0, blfSHADOW)
    elif P.font_shadow_method == "DEFAULT":
        TEXT_RENDER = font_shadow_default
    else:
        e = font_shadow_custom
        TEXT_RENDER = e
        rgba = P.color.font_shadow
        e.r = rgba[0]
        e.g = rgba[1]
        e.b = rgba[2]
        e.a = rgba[3]

        hardness = P.font_shadow_hardness
        if hardness == 0:
            e.blurlevel = 5
        elif hardness == 1:
            e.blurlevel = 3
        elif hardness == 2:
            e.blurlevel = 0
        else:
            e.blurlevel = 6

        e.offset_x, e.offset_y = P.font_shadow_offset
    #|

bpy_ops_object_mode_set = bpy.ops.object.mode_set




def blenddata_update_post(dummy):
    TAG_UPDATE[0] = True

    try: Admin.REDRAW()
    except: pass
    #|

class BlendDataTemp:
    __slots__ = ()

    active_object = None
    active_object_name = ""
    objects = None

    @classmethod
    def kill(cls):
        cls.objects = None
        #|
    @classmethod
    def init(cls):
        active_object = bpy.context.object
        cls.active_object = active_object
        cls.active_object_name = active_object.name  if hasattr(active_object, "name") else ""
        cls.objects = None
        #|
    @classmethod
    def r_upd_objects(cls):
        if cls.objects == None:
            objects = tuple(
                # <<< 1copy (bl_objects,, $$)
                bpy.context.view_layer.objects
                # >>>
            )
            cls.objects = objects
            return objects
        return cls.objects
        #|

    @staticmethod
    def r_all_objects():
        return tuple(
            # <<< 1copy (bl_objects,, $$)
            bpy.context.view_layer.objects
            # >>>
        )
    #|
    #|

def disable_auto_upd():
    # <<< 1copy (disable_auto_upd,, $$)
    TAG_UPDATE[2] = False
    # >>>
def enable_auto_upd():
    # <<< 1copy (enable_auto_upd,, $$)
    TAG_UPDATE[2] = True
    # >>>

def update_data():
    TAG_UPDATE[0] = False
    # /* 0m_update_data
    TAG_UPDATE[1] = True

    BlendDataTemp.init()
    for e in W_MODAL: e.upd_data()
    BlendDataTemp.kill()
    TAG_UPDATE[1] = False

    if TAG_RENAME[0] is True:
        TAG_RENAME[0] = False
    # */
def update_data_true():
    TAG_UPDATE[0] = False
    # <<< 1copy (0m_update_data,, $$)
    TAG_UPDATE[1] = True

    BlendDataTemp.init()
    for e in W_MODAL: e.upd_data()
    BlendDataTemp.kill()
    TAG_UPDATE[1] = False

    if TAG_RENAME[0] is True:
        TAG_RENAME[0] = False
    # >>>
    return True
    #|
def i_draw_callback_px():
    if bpy.context.area == CONTEXT_AREA:
        if TAG_UPDATE[0]:
            # /* 0m_draw_update_data
            TAG_UPDATE[0] = False
            if TAG_UPDATE[2]:
                # <<< 1copy (0m_update_data,, $$)
                TAG_UPDATE[1] = True

                BlendDataTemp.init()
                for e in W_MODAL: e.upd_data()
                BlendDataTemp.kill()
                TAG_UPDATE[1] = False

                if TAG_RENAME[0] is True:
                    TAG_RENAME[0] = False
                # >>>
            # */

        TEXT_RENDER()
        for e in W_DRAW: e.u_draw()

        ADMIN.u_draw()
    #|
U_DRAW_CALLBACK_PX = i_draw_callback_px
def draw_callback_px():
    try: ADMIN.u_draw
    except:
        kill_admin()
        return

    U_DRAW_CALLBACK_PX()
    #|
def draw_callback_view():
    for e in DRAW_VIEW_STACK:
        e()
    #|
DRAW_VIEW_STACK = []
def draw_view_append(fn_draw):
    global DRAW_VIEW_HANDLE
    if DRAW_VIEW_HANDLE is None:
        DRAW_VIEW_STACK.clear()
        DRAW_VIEW_HANDLE = SpaceView3D.draw_handler_add(draw_callback_view, (), 'WINDOW', 'POST_VIEW')

    DRAW_VIEW_STACK.append(fn_draw)
    #|
def draw_view_remove(fn_draw):
    DRAW_VIEW_STACK.remove(fn_draw)
    if not DRAW_VIEW_STACK:
        global DRAW_VIEW_HANDLE
        SpaceView3D.draw_handler_remove(DRAW_VIEW_HANDLE, 'WINDOW')
        DRAW_VIEW_HANDLE = None

    #|

def remove_timer():
    bpy.context.window_manager.event_timer_remove(Admin.TIMER)
    Admin.TIMER = None

    #|

def tag_obj_rename(): TAG_RENAME[0] = True

ACTIVE_MODIFIER = [None]
def topbar_header_draw_callback(self, context):
    ob = context.object
    if hasattr(ob, "modifiers") and hasattr(ob.modifiers, "active"):
        if ob.modifiers.active != ACTIVE_MODIFIER[0]:
            ACTIVE_MODIFIER[0] = ob.modifiers.active
            TAG_UPDATE[0] = True

    #|

def reg_update_post_and_subscribe():
    if blenddata_update_post not in depsgraph_update_post:   depsgraph_update_post.append(blenddata_update_post)
    if blenddata_update_post not in frame_change_post:       frame_change_post.append(blenddata_update_post)
    TOPBAR_HT_upper_bar.remove(topbar_header_draw_callback)
    TOPBAR_HT_upper_bar.append(topbar_header_draw_callback)

    subscribe_rna(
        key=(Object, "name"),
        owner=tag_obj_rename,
        args=(),
        notify=tag_obj_rename)
    #|
def unreg_update_post_and_unsubscribe():
    if blenddata_update_post in depsgraph_update_post:   depsgraph_update_post.remove(blenddata_update_post)
    if blenddata_update_post in frame_change_post:       frame_change_post.remove(blenddata_update_post)
    TOPBAR_HT_upper_bar.remove(topbar_header_draw_callback)

    clear_by_owner(tag_obj_rename)
    #|

# Need change ret
def kill_admin(sleep=True):
    if Admin.TIMER is not None: remove_timer()
    area.unreg_all_timer()
    block.unreg_all_timer()

    unreg_update_post_and_unsubscribe()

    bpy.context.window.cursor_modal_restore()

    try: Admin.REDRAW()
    except: pass

    global DRAW_HANDLE, DRAW_VIEW_HANDLE, ADMIN

    SpaceView3D.draw_handler_remove(DRAW_HANDLE, 'WINDOW')
    DRAW_HANDLE = None
    if DRAW_VIEW_HANDLE is not None:
        try:
            SpaceView3D.draw_handler_remove(DRAW_VIEW_HANDLE, 'WINDOW')
        except: pass
        DRAW_VIEW_HANDLE = None
    DRAW_VIEW_STACK.clear()

    prefs_callback_disable()

    # <<< 1copy (0m_Admin,, $$, $lambda line: line  if line.find('=') == -1 else line.replace(
    #     line.strip(), f'Admin.{line.strip()}')$)
    # ---------------------------------------------------------------------------------------------------------
    Admin.IS_RUNNING = False

    Admin.CONTEXT = None
    Admin.EVT = None
    Admin.REDRAW = None
    Admin.TIMER = None
    Admin.TAG_CURSOR = ''
    Admin.IS_INSIDE = False
    Admin.TB_ENABLE = True
    Admin.CURSOR_TYPE = None
    Admin.ENDPUSH = True
    Admin.IS_HUD = False
    Admin.IS_BUG_REPORT_RUNNING = False
    # ---------------------------------------------------------------------------------------------------------
    # >>>

    W_HEAD.clear()
    W_FOCUS[0] = None
    TAG_UPDATE[:] = [False, False, True]
    ADMIN = None

    if Admin.FIN_AFTER_CALLBACK is not None:
        def time_function():
            Admin.FIN_AFTER_CALLBACK()
            Admin.FIN_AFTER_CALLBACK = None

        bpy.app.timers.register(time_function)

    if sleep is False:
        W_PROCESS.clear()
        W_MODAL.clear()
        W_DRAW.clear()
        TASKS.clear()
        D_TASKS_IND.clear()


    return {'CANCELLED'}
    #|

def call_admin(context):
    if Admin.IS_RUNNING: return True
    if context.area.type != 'VIEW_3D': return False
    if context.region.type != 'WINDOW': return False

    bpy.ops.wm.vmd_admin('INVOKE_DEFAULT')

    if W_MODAL: update_data()
    upd_size()
    return True
    #|

def push_modal_safe():
    if ADMIN == None: return
    ADMIN.push_modal()
    #|
def force_pass_through(callback=None):
    ADMIN.push_modal()
    ADMIN.u_modal = ADMIN.i_modal_force_pass_through

    force_pass_through.callback = N  if callback is None else callback
    #|

def upd_size():
    #| call from Npanel
    prefs_callback_disable()

    upd_font_size()

    ADMIN.upd_size()

    for e in W_PROCESS: e.upd_size()

    prefs_callback_enable()
    #|

def upd_win_active(): #| call from Npanel
    if not W_MODAL: return

    if not W_HEAD:
        def end_modal_release():
            if hasattr(W_MODAL[-1], "resize_upd_end"):
                W_MODAL[-1].resize_upd_end()

        UpdWinActiveHead(end_modal=end_modal_release) # update P_temp when release

    prefs.U_UPD_WIN_ACTIVE = N
    # <<< 1copy (disable_auto_upd,, $$)
    TAG_UPDATE[2] = False
    # >>>

    self = W_MODAL[-1]
    x, y = P_temp.pos
    dx = x - self.box_win.L
    dy = y - self.box_win.T
    if dx or dy:
        self.dxy(dx, dy)
    else: # ref: win.i_modal_resize_click_R
        sizeX, sizeY = P_temp.size

        dx = sizeX - self.box_win.R + self.box_win.L
        if dx:
            _lim_R = REGION_DATA.R
            if self.scissor.w + dx < 4 * SIZE_title[0]: dx = 4 * SIZE_title[0] - self.scissor.w
            else:
                if self.box_win.R + dx > _lim_R: dx = _lim_R - self.box_win.R
            self.scissor.w += dx
            self.box_win.R += dx
            self.box_rim.R += dx
            # <<< 1dict (2win_boxes,, $
            # e = self.boxes[|box_shadow|]$)
            e = self.boxes[0]
            # >>>
            e.R += dx
            self.box_title_button.dx(dx)
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            # <<< 1dict (2win_blfs,, $
            # blf_title = self.blfs[|blf_title|]$)
            blf_title = self.blfs[0]
            # >>>
            blf_title.text = r_blf_clipping_end(blf_title.unclip_text, blf_title.x,
                self.box_title_button.L - D_SIZE['font_title_dx'])

            self.dxy(0, 0)
            self.resize_upd()
        else:
            dy = self.box_win.title_B - self.box_win.B - sizeY
            if dy:
                _lim_B = REGION_DATA.B + SIZE_tb[0]
                if self.scissor.h - dy < 0: dy = self.scissor.h
                else:
                    if self.box_win.B + dy < _lim_B: dy = _lim_B - self.box_win.B
                self.scissor.y += dy
                self.scissor.h -= dy
                self.box_win.B += dy
                self.box_rim.B += dy
                # <<< 1dict (2win_boxes,, $
                # e = self.boxes[|box_shadow|]$)
                e = self.boxes[0]
                # >>>
                e.B += dy

                self.dxy(0, 0)
                self.resize_upd()
            else:
                posX, posY = P_temp.canvas
                e = self.areas[0].box_area
                dx = posX - e.L + self.box_win.L + SIZE_border[0]
                if dx:
                    for e in self.areas: e.dxy(dx, 0)
                else:
                    dy = posY - e.T + self.box_win.title_B - SIZE_border[0]
                    for e in self.areas: e.dxy(0, dy)

    # <<< 1copy (enable_auto_upd,, $$)
    TAG_UPDATE[2] = True
    # >>>
    prefs.U_UPD_WIN_ACTIVE = upd_win_active
    #|

def upd_pref():
    TAG_UPDATE[0] = True

    #|

def prefs_callback_enable():
    prefs.U_UPD_SIZE = upd_size
    prefs.U_UPD_WIN_ACTIVE = upd_win_active
    prefs.U_UPD_PREF = upd_pref
    #|
def prefs_callback_disable():
    prefs.U_UPD_SIZE = N
    prefs.U_UPD_WIN_ACTIVE = N
    prefs.U_UPD_PREF = N
    #|

def upd_temp_pref(self):
    prefs.U_UPD_WIN_ACTIVE = N
    box_win = self.box_win
    P_temp.pos = box_win.L, box_win.T
    P_temp.size = box_win.R - box_win.L, box_win.title_B - box_win.B
    e = self.areas[0].box_area
    P_temp.canvas = e.L - box_win.L - SIZE_border[0], e.T - box_win.title_B + SIZE_border[0]
    prefs.U_UPD_WIN_ACTIVE = upd_win_active
    #|
def bring_to_front(self):

    #|
    upd_temp_pref(self)

    if W_MODAL:
        W_MODAL[-1].box_win.color = COL_win_title_inactive

    W_MODAL.remove(self)
    W_DRAW.remove(self)
    W_MODAL.append(self)
    W_DRAW.append(self)

    self.box_win.color = COL_win_title

    # <<< 1dict (2m_ADMIN_boxes,, $
    # ADMIN.boxes[|box_tb_active|].LRBT_upd(*TASKS[D_TASKS_IND[self.__class__.__name__]].box_icon.r_LRBT())$)
    ADMIN.boxes[2].LRBT_upd(*TASKS[D_TASKS_IND[self.__class__.__name__]].box_icon.r_LRBT())
    # >>>
    Admin.REDRAW()
    #|
def bring_draw_to_top_safe(self):
    if self in W_DRAW:
        W_DRAW.remove(self)
        W_DRAW.append(self)
        return True
    return False
    #|

def r_mouseloop(loop_type="PAN", cursor_icon=None, cursor_icon_end=None):
    if cursor_icon is None:
        Admin.TAG_CURSOR = P.cursor_pan
    else:
        Admin.TAG_CURSOR = cursor_icon

    if cursor_icon_end is None: Admin.CURSOR_TYPE

    context_window = bpy.context.window
    _CURSOR_WARP = CURSOR_WARP
    _MOUSE = MOUSE
    _MOUSE_WINDOW = MOUSE_WINDOW

    _loop_mouse_info_L = 3
    _loop_mouse_info_R = context_window.width - 6
    _loop_mouse_info_B = 3
    _loop_mouse_info_T = context_window.height - 6
    _loop_mouse_info_L2 = _loop_mouse_info_L + 5
    _loop_mouse_info_R2 = _loop_mouse_info_R - 5
    _loop_mouse_info_B2 = _loop_mouse_info_B + 5
    _loop_mouse_info_T2 = _loop_mouse_info_T - 5
    _loop_mouse_info_dx_lim = (_loop_mouse_info_R - _loop_mouse_info_L) // 2
    _loop_mouse_info_dy_lim = (_loop_mouse_info_T - _loop_mouse_info_B) // 2

    _pan_xy = _MOUSE_WINDOW[:]
    _pan_xy_org = _MOUSE_WINDOW[:]

    def mouseloop_end(override_pos=None):
        if override_pos is None:
            _CURSOR_WARP(*_pan_xy_org)
            _MOUSE[:] = _pan_xy_org
        else:
            x, y = override_pos
            if x == None: x = _pan_xy_org[0]
            if y == None: y = _pan_xy_org[1]
            _CURSOR_WARP(x, y)
            _MOUSE[:] = x, y
        Admin.TAG_CURSOR = 'DEFAULT'

    def mouseloop():
        if _MOUSE_WINDOW[0] <= _loop_mouse_info_L:
            if _MOUSE_WINDOW[1] <= _loop_mouse_info_B:
                _CURSOR_WARP(_loop_mouse_info_R2, _loop_mouse_info_T2)
                _pan_xy[0] = _loop_mouse_info_R2
                _pan_xy[1] = _loop_mouse_info_T2
            elif _MOUSE_WINDOW[1] >= _loop_mouse_info_T:
                _CURSOR_WARP(_loop_mouse_info_R2, _loop_mouse_info_B2)
                _pan_xy[0] = _loop_mouse_info_R2
                _pan_xy[1] = _loop_mouse_info_B2
            else:
                _CURSOR_WARP(_loop_mouse_info_R2, _MOUSE_WINDOW[1])
                _pan_xy[0] = _loop_mouse_info_R2
                _pan_xy[1] = _MOUSE_WINDOW[1]
        elif _MOUSE_WINDOW[0] >= _loop_mouse_info_R:
            if _MOUSE_WINDOW[1] <= _loop_mouse_info_B:
                _CURSOR_WARP(_loop_mouse_info_L2, _loop_mouse_info_T2)
                _pan_xy[0] = _loop_mouse_info_L2
                _pan_xy[1] = _loop_mouse_info_T2
            elif _MOUSE_WINDOW[1] >= _loop_mouse_info_T:
                _CURSOR_WARP(_loop_mouse_info_L2, _loop_mouse_info_B2)
                _pan_xy[0] = _loop_mouse_info_L2
                _pan_xy[1] = _loop_mouse_info_B2
            else:
                _CURSOR_WARP(_loop_mouse_info_L2, _MOUSE_WINDOW[1])
                _pan_xy[0] = _loop_mouse_info_L2
                _pan_xy[1] = _MOUSE_WINDOW[1]
        elif _MOUSE_WINDOW[1] <= _loop_mouse_info_B:
            _CURSOR_WARP(_MOUSE_WINDOW[0], _loop_mouse_info_T2)
            _pan_xy[0] = _MOUSE_WINDOW[0]
            _pan_xy[1] = _loop_mouse_info_T2
        elif _MOUSE_WINDOW[1] >= _loop_mouse_info_T:
            _CURSOR_WARP(_MOUSE_WINDOW[0], _loop_mouse_info_B2)
            _pan_xy[0] = _MOUSE_WINDOW[0]
            _pan_xy[1] = _loop_mouse_info_B2
        else:
            _pan_xy[0] = _MOUSE_WINDOW[0]
            _pan_xy[1] = _MOUSE_WINDOW[1]

    if loop_type == "NONE" or not P.pan_invert:
        def r_dxy_mouse():
            dx = _MOUSE_WINDOW[0] - _pan_xy[0]
            dy = _MOUSE_WINDOW[1] - _pan_xy[1]

            if abs(dx) > _loop_mouse_info_dx_lim: dx = 0
            if abs(dy) > _loop_mouse_info_dy_lim: dy = 0
            return dx, dy
    else:
        def r_dxy_mouse():
            dx = _pan_xy[0] - _MOUSE_WINDOW[0]
            dy = _pan_xy[1] - _MOUSE_WINDOW[1]

            if abs(dx) > _loop_mouse_info_dx_lim: dx = 0
            if abs(dy) > _loop_mouse_info_dy_lim: dy = 0
            return dx, dy

    return mouseloop_end, mouseloop, r_dxy_mouse
    #|
def r_mouse_from_region(x, y):
    EVT = Admin.EVT
    return x + EVT.mouse_x - EVT.mouse_region_x, y + EVT.mouse_y - EVT.mouse_region_y
    #|
def r_mouse_from_window(x, y):
    EVT = Admin.EVT
    return x + EVT.mouse_region_x - EVT.mouse_x, y + EVT.mouse_region_y - EVT.mouse_y
    #|
def r_hud_region(area):
    for region in area.regions:
        if region.type == 'HUD':
            if region.width > 1 and region.height > 1 and region.x > 0 and region.y > 0:
                return region

    return None
    #|
def jumpout_head():
    if W_HEAD:
        W_HEAD[-1].fin()
    #|

def save_pref():

    bpy.ops.wm.save_userpref()
    report("Preferences saved")
    #|


def active_object_set(e):
    try:
        bpy.context.view_layer.objects.active = e
        return True
    except: return False
    #|
def object_select(e, action="SELECT", active=True):
    try:
        if active:
            bpy.context.view_layer.objects.active = e
        if action == "SELECT":
            bpy.ops.object.select_all(action='DESELECT')
            e.select_set(True)
        elif action == "EXTEND":
            e.select_set(True)
        return True
    except: return False
    #|
def object_mode_set(s):
    try:
        bpy_ops_object_mode_set(mode=s)
        return True
    except: return False
    #|

def modal_object_picker_init(allow_types, r_except_objects, end_fn):
    kill_evt_except()
    context = bpy.context
    old_object = context.object
    old_selected_objects = context.selected_objects.copy()
    old_mode = old_object.mode  if hasattr(old_object, "mode") else None

    REDRAW = Admin.REDRAW
    bpy_ops_view3d_select = bpy.ops.view3d.select
    bpy_ops_object_select_all = bpy.ops.object.select_all

    object_mode_set("OBJECT")
    bpy_ops_object_select_all(action="DESELECT")
    try: context.window.cursor_modal_set(P.cursor_picker)
    except: pass
    except_objects = set()  if r_except_objects == None else r_except_objects()

    focus_object = None
    shadow_dL, shadow_dR, shadow_dB, shadow_dT = blg.SIZE_dd_shadow_offset

    widget_full_h = D_SIZE['widget_full_h']
    widget_h = SIZE_widget[0]
    widget_rim = SIZE_border[3]
    font_size = D_SIZE['font_main']
    font_dx = D_SIZE['font_main_dx']
    font_dT = D_SIZE['font_main_dT']
    font_dx2 = font_dx + font_dx
    regionR = REGION_DATA.R
    regionB = REGION_DATA.B + widget_full_h
    regionT = REGION_DATA.T

    # box_shadow = blg.GpuShadowDropDown(d=blg.SIZE_shadow_softness[1])
    box_bg = blg.GpuBox_block()
    box_button = blg.GpuRim(blg.COL_box_text, blg.COL_box_text_rim, d=widget_rim)
    GpuImg_OBJECT_DATA = blg.GpuImg_OBJECT_DATA
    box_icon_object = GpuImg_OBJECT_DATA()
    blf_name = blg.BlfColor(color=blg.COL_box_text_fg)

    def i_draw_object_picker():
        if focus_object is not None:
            blend_set('ALPHA')
            # box_shadow.bind_draw()
            box_bg.bind_draw()
            box_button.bind_draw()
            box_icon_object.bind_draw()

            e = blf_name
            blfSize(FONT0, D_SIZE['font_main'])
            blfColor(FONT0, *e.color)
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)
        #|
    def localmodal_fin(confirm=False):
        kill_evt_except()
        context.window.cursor_modal_set("DEFAULT")
        global U_DRAW_CALLBACK_PX
        U_DRAW_CALLBACK_PX = i_draw_callback_px
        ADMIN.u_modal = ADMIN.i_modal


        bpy_ops_object_select_all(action="DESELECT")
        for e in old_selected_objects: e.select_set(True)
        active_object_set(old_object)
        object_mode_set(old_mode)

        try:
            if confirm and focus_object: end_fn(focus_object)
        except Exception as ex:
            DropDownOk(None, MOUSE, input_text=f'Unexpected error, please report to the author: 01\n{ex}')
        update_data()
        #|
    def i_localmodal_object_picker(evt):
        REDRAW()
        get_evt(Admin.EVT)
        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']() or TRIGGER['dd_esc']():
            localmodal_fin()
            return {'RUNNING_MODAL'}
        if TRIGGER['click']() or TRIGGER['dd_confirm']():
            localmodal_fin(True)
            return {'RUNNING_MODAL'}

        bpy_ops_object_select_all("INVOKE_DEFAULT", action="DESELECT")
        bpy_ops_view3d_select("INVOKE_DEFAULT", deselect_all=True)
        ob = context.selected_objects[0]  if context.selected_objects else None
        if ob in except_objects: ob = None
        if ob != None and allow_types != None:
            if ob.type not in allow_types: ob = None

        nonlocal focus_object
        if ob != focus_object:
            focus_object = ob
            if ob is not None:
                # /* 0m_init_picker_draw
                blfSize(FONT0, font_size)
                x, y = MOUSE
                L = x + widget_full_h
                T = y
                B = T - widget_full_h
                R = L + widget_full_h + font_dx2 + round(blfDimen(FONT0, ob.name)[0])
                if R > regionR:
                    dx = regionR - R
                    R += dx
                    L += dx
                if T > regionT:
                    dy = regionT - T
                    T += dy
                    B += dy
                elif T < regionB:
                    dy = regionB - B - widget_full_h
                    T += dy
                    B += dy

                box_button.L = L
                box_button.R = R
                box_button.B = B
                box_button.T = T
                box_button.upd()
                L0, R0, B0, T0 = box_button.inner
                box_icon_object.LRBT_upd(L0, L0 + widget_h, B0, T0)
                blf_name.x = box_icon_object.R + font_dx
                blf_name.y = T0 - font_dT
                L -= widget_rim
                R += widget_rim
                B -= widget_rim
                T += widget_rim
                box_bg.LRBT_upd(L, R, B, T)
                # box_shadow.L = L + shadow_dL -100
                # box_shadow.R = R + shadow_dR
                # box_shadow.B = B + shadow_dB
                # box_shadow.T = T + shadow_dT + 100
                # box_shadow.upd()

                blf_name.text = ob.name
                img_cls = getattr(blg, f"GpuImg_OUTLINER_OB_{ob.type}", GpuImg_OBJECT_DATA)
                if box_icon_object.__class__ != img_cls: box_icon_object.__class__ = img_cls
                # */
        else:
            if ob is not None:
                # <<< 1copy (0m_init_picker_draw,, $$)
                blfSize(FONT0, font_size)
                x, y = MOUSE
                L = x + widget_full_h
                T = y
                B = T - widget_full_h
                R = L + widget_full_h + font_dx2 + round(blfDimen(FONT0, ob.name)[0])
                if R > regionR:
                    dx = regionR - R
                    R += dx
                    L += dx
                if T > regionT:
                    dy = regionT - T
                    T += dy
                    B += dy
                elif T < regionB:
                    dy = regionB - B - widget_full_h
                    T += dy
                    B += dy

                box_button.L = L
                box_button.R = R
                box_button.B = B
                box_button.T = T
                box_button.upd()
                L0, R0, B0, T0 = box_button.inner
                box_icon_object.LRBT_upd(L0, L0 + widget_h, B0, T0)
                blf_name.x = box_icon_object.R + font_dx
                blf_name.y = T0 - font_dT
                L -= widget_rim
                R += widget_rim
                B -= widget_rim
                T += widget_rim
                box_bg.LRBT_upd(L, R, B, T)
                # box_shadow.L = L + shadow_dL -100
                # box_shadow.R = R + shadow_dR
                # box_shadow.B = B + shadow_dB
                # box_shadow.T = T + shadow_dT + 100
                # box_shadow.upd()

                blf_name.text = ob.name
                img_cls = getattr(blg, f"GpuImg_OUTLINER_OB_{ob.type}", GpuImg_OBJECT_DATA)
                if box_icon_object.__class__ != img_cls: box_icon_object.__class__ = img_cls
                # >>>
        return {'RUNNING_MODAL'}
        #|

    REDRAW()
    global U_DRAW_CALLBACK_PX
    U_DRAW_CALLBACK_PX = i_draw_object_picker
    ADMIN.u_modal = i_localmodal_object_picker

    #|

def blockblsubwindows():
    windows = bpy.context.window_manager.windows
    if len(windows) == 1: return

    for w in windows:
        if hasattr(w.screen, "name") and w.screen.name == "temp":
            if w in Blocking.MODALS: continue
            with bpy.context.temp_override(window=w):
                vmd_blocking()
            continue

        if w.parent == None: continue

        if w in Blocking.MODALS: continue
        with bpy.context.temp_override(window=w):
            vmd_blocking()
    #|
def call_bug_report_dialog():
    if ADMIN is None:
        call_admin(bpy.context)

    Admin.IS_BUG_REPORT_RUNNING = True
    import traceback

    tracelines = traceback.format_exc().split("\n")
    for r, s in enumerate(tracelines):
        if s.lstrip().startswith('File "'):
            i0 = s.find("user_default")
            if i0 == -1: continue
            tracelines[r] = f'"{s[i0 + 12 : ]}'

    backslash_n = "\n"

    ddw = DropDownOk(None, MOUSE,
        fn_yes = ADMIN.evt_sys_off,
        title = "Bug Report",
        input_text = f"We're Sorry\nPlease report to the author:\noorcer@gmail.com\n\n{r_platform()}\n{backslash_n.join(tracelines)}",
        text_yes = "Close",
        row_count = 12,
        width_fac = 3.0)

    ddw.data['fin_callfront'] = lambda: setattr(Admin, 'IS_BUG_REPORT_RUNNING', False)
    #|


class Blocking(Operator):
    __slots__ = '__weakref__'

    bl_idname = "wm.vmd_blocking"
    bl_label = "VMD Blocking"
    bl_options = {"INTERNAL"}

    MODALS = WeakValueDictionary()

    def execute(self, context):
        context.window_manager.modal_handler_add(self)
        Blocking.MODALS[context.window] = self

        return {'RUNNING_MODAL'}
        #|

    def modal(self, context, event):
        if W_HEAD:
            areas = context.window.screen.areas
            if len(areas) == 1 and areas[0].type == "FILE_BROWSER":
                return {'PASS_THROUGH'}
            else:
                return {'RUNNING_MODAL'}


        if context.window in Blocking.MODALS:
            del Blocking.MODALS[context.window]
        return {'CANCELLED'}
        #|
    #|
    #|

class Admin(Operator):
    __slots__ = (
        'u_modal',
        'u_modal_tb',
        'u_draw',
        'boxes')

    bl_idname = "wm.vmd_admin"
    bl_label = "VMD Admin"
    bl_options = {"INTERNAL"}

    # /* 0m_Admin
    # ---------------------------------------------------------------------------------------------------------
    IS_RUNNING = False

    CONTEXT = None
    EVT = None
    REDRAW = None
    TIMER = None
    TAG_CURSOR = ''
    IS_INSIDE = False
    TB_ENABLE = True
    CURSOR_TYPE = None
    ENDPUSH = True
    IS_HUD = False
    IS_BUG_REPORT_RUNNING = False
    # ---------------------------------------------------------------------------------------------------------
    # */

    FIN_AFTER_CALLBACK = None

    def invoke(self, context, event):

        #|
        if Admin.IS_RUNNING: return {'CANCELLED'}
        Admin.IS_RUNNING = True

        global ADMIN, CONTEXT_AREA, CONTEXT_REGION, DRAW_HANDLE, CURSOR_WARP, U_DRAW_CALLBACK_PX

        U_DRAW_CALLBACK_PX = i_draw_callback_px

        ADMIN = self
        CONTEXT_AREA = context.area
        CONTEXT_REGION = context.region
        CURSOR_WARP = context.window.cursor_warp

        Admin.CONTEXT = context
        Admin.EVT = event
        Admin.REDRAW = CONTEXT_AREA.tag_redraw
        Admin.IS_INSIDE = False
        Admin.TB_ENABLE = True

        REGION_DATA.upd(CONTEXT_AREA, CONTEXT_REGION)

        self.u_modal = self.i_modal
        self.u_modal_tb = self.to_modal_tb
        self.u_draw = self.i_draw

        h = SIZE_tb[0]
        B = REGION_DATA.B
        T = B + h
        box_tb = GpuBox_box_tb(0, context.region.width, B, T)
        box_tb.upd()
        L = REGION_DATA.L + SIZE_tb[1]
        box_tb_start = GpuImg_tb_start(L, L + h, B, T)
        box_tb_start.upd()
        box_tb_active = GpuImg_tb_active()
        box_tb_active.upd()
        box_tb_hover = GpuImg_tb_hover()
        box_tb_hover.upd()
        self.boxes = (
            # /* 2m_ADMIN_boxes $dict$
            box_tb,
            box_tb_start,
            box_tb_active,
            box_tb_hover
            # */
        )

        if TASKS:
            try:
                update_data()
            except:
                pass

        DRAW_HANDLE = SpaceView3D.draw_handler_add(draw_callback_px, (), 'WINDOW', 'POST_PIXEL')
        reg_update_post_and_subscribe()
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
        #|

    def upd_size(self):
        boxes = self.boxes
        h = SIZE_tb[0]
        B = REGION_DATA.B
        T = B + h

        # <<< 1dict (2m_ADMIN_boxes,, $
        # boxes[|box_tb|].LRBT_upd(0, CONTEXT_REGION.width, B, T)$)
        boxes[0].LRBT_upd(0, CONTEXT_REGION.width, B, T)
        # >>>
        L = REGION_DATA.L + SIZE_tb[1]
        R = L + h
        # <<< 1dict (2m_ADMIN_boxes,, $
        # boxes[|box_tb_start|].LRBT_upd(L, R, B, T)$)
        boxes[1].LRBT_upd(L, R, B, T)
        # >>>

        # <<< 1dict (2m_ADMIN_boxes,, $
        # tb_hover = boxes[|box_tb_hover|]$)
        tb_hover = boxes[3]
        # >>>
        if tb_hover.L == 0 and tb_hover.R == 0 and tb_hover.B == 0 and tb_hover.T == 0: pass
        else: tb_hover.LRBT_upd(0, 0, 0, 0)

        for e in TASKS:
            L += h
            R += h
            e.box_icon.LRBT_upd(L, R, B, T)
            e.update_multibar()

        if W_MODAL:
            self = W_MODAL[-1]
            # <<< 1dict (2m_ADMIN_boxes,, $
            # ADMIN.boxes[|box_tb_active|].LRBT_upd(*TASKS[D_TASKS_IND[self.__class__.__name__]].box_icon.r_LRBT())$)
            ADMIN.boxes[2].LRBT_upd(*TASKS[D_TASKS_IND[self.__class__.__name__]].box_icon.r_LRBT())
            # >>>
        else:
            # <<< 1dict (2m_ADMIN_boxes,, $
            # boxes[|box_tb_active|].LRBT_upd(0, 0, 0, 0)$)
            boxes[2].LRBT_upd(0, 0, 0, 0)
            # >>>
        #|

    def modal(self, context, event):
        try:
            if context.area is None:
                kill_admin()
                return {'CANCELLED'}
            if context.space_data.region_quadviews:
                self.report({'WARNING'}, "This Add-on does not support Quad View in the current version.")
                kill_admin()
                return {'CANCELLED'}

            Admin.EVT = event
            return self.u_modal(event)
        except Exception as ex:
            if Admin.IS_BUG_REPORT_RUNNING is True:
                kill_admin(sleep=False)
                return {'CANCELLED'}

            call_bug_report_dialog()
            return {'RUNNING_MODAL'}
        #|

    def i_modal(self, evt):
        # /* 0m_Admin_i_modal
        if W_HEAD:
            get_evt(evt)
            if W_HEAD[-1].modal() == "FORCE_PASS_THROUGH":
                # <<< 1copy (Admin_set_cursor,, $$)
                if Admin.TAG_CURSOR:
                    if Admin.TAG_CURSOR == 'restore':
                        bpy.context.window.cursor_modal_restore()

                        Admin.CURSOR_TYPE = None
                    else:
                        if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                            try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                            except: pass

                            Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                    Admin.TAG_CURSOR = ''
                # >>>
                return {'PASS_THROUGH'}
            # <<< 1copy (Admin_set_cursor,, $$)
            if Admin.TAG_CURSOR:
                if Admin.TAG_CURSOR == 'restore':
                    bpy.context.window.cursor_modal_restore()

                    Admin.CURSOR_TYPE = None
                else:
                    if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                        try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                        except: pass

                        Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                Admin.TAG_CURSOR = ''
            # >>>
            return {'RUNNING_MODAL'}

        if Admin.IS_INSIDE is True:
            get_evt(evt)

            x = evt.mouse_region_x
            y = evt.mouse_region_y
            rd = REGION_DATA
            if x < rd.L or x > rd.R or y < rd.B or y > rd.T:
                # <<< 1copy (0m_outside_evt,, $$)

                Admin.IS_INSIDE = False
                bpy.context.window.cursor_modal_restore()
                if W_FOCUS[0] != None:
                    if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                    W_FOCUS[0] = None
                kill_evt()
                # >>>
                return {'PASS_THROUGH'}

            # <<< 1copy (0m_check_hud,, ${
            #     'if Admin.IS_INSIDE': '#if Admin.IS_INSIDE',
            #     '"FORCE_PASS_THROUGH"': "{'PASS_THROUGH'}"
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(CONTEXT_AREA)
                if hud_region is None: Admin.IS_HUD = False
                else:
                    hud_L = hud_region.x
                    hud_B = hud_region.y
                    if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                        #if Admin.IS_INSIDE is False: return {'PASS_THROUGH'}
                        # <<< 1copy (0m_outside_evt,, $$)

                        Admin.IS_INSIDE = False
                        bpy.context.window.cursor_modal_restore()
                        if W_FOCUS[0] != None:
                            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                            W_FOCUS[0] = None
                        kill_evt()
                        # >>>

                        return {'PASS_THROUGH'}
            # >>>

            if Admin.TB_ENABLE == True:
                if y < rd.B + SIZE_tb[0]:
                    rd.upd(CONTEXT_AREA, CONTEXT_REGION)
                    if rd.L + SIZE_tb[1] < x < rd.R and rd.B < y < rd.B + SIZE_tb[0]:
                        self.u_modal_tb()
                        # <<< 1copy (Admin_set_cursor,, $$)
                        if Admin.TAG_CURSOR:
                            if Admin.TAG_CURSOR == 'restore':
                                bpy.context.window.cursor_modal_restore()

                                Admin.CURSOR_TYPE = None
                            else:
                                if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                    try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                    except: pass

                                    Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                            Admin.TAG_CURSOR = ''
                        # >>>
                        return {'RUNNING_MODAL'}

            for e in reversed(W_MODAL):
                if e.modal() is True:
                    if W_FOCUS[0] != e:
                        if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                        W_FOCUS[0] = e
                    # <<< 1copy (Admin_set_cursor,, $$)
                    if Admin.TAG_CURSOR:
                        if Admin.TAG_CURSOR == 'restore':
                            bpy.context.window.cursor_modal_restore()

                            Admin.CURSOR_TYPE = None
                        else:
                            if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                except: pass

                                Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                        Admin.TAG_CURSOR = ''
                    # >>>
                    return {'RUNNING_MODAL'}

            # <<< 1copy (0m_outside_evt,, $$)

            Admin.IS_INSIDE = False
            bpy.context.window.cursor_modal_restore()
            if W_FOCUS[0] != None:
                if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                W_FOCUS[0] = None
            kill_evt()
            # >>>
            return {'PASS_THROUGH'}
        else:
            x = evt.mouse_region_x
            y = evt.mouse_region_y
            rd = REGION_DATA
            if x < rd.L or x > rd.R or y < rd.B or y > rd.T: return {'PASS_THROUGH'}

            if Admin.TB_ENABLE == True:
                if y < rd.B + SIZE_tb[0]:
                    rd.upd(CONTEXT_AREA, CONTEXT_REGION)
                    if rd.L + SIZE_tb[1] < x < rd.R and rd.B < y < rd.B + SIZE_tb[0]:
                        self.inside_evt()
                        kill_evt()
                        get_evt(evt)
                        self.u_modal_tb()
                        # <<< 1copy (Admin_set_cursor,, $$)
                        if Admin.TAG_CURSOR:
                            if Admin.TAG_CURSOR == 'restore':
                                bpy.context.window.cursor_modal_restore()

                                Admin.CURSOR_TYPE = None
                            else:
                                if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                    try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                    except: pass

                                    Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                            Admin.TAG_CURSOR = ''
                        # >>>
                        return {'RUNNING_MODAL'}

            kill_evt()
            get_evt(evt)

            # <<< 1copy (0m_check_hud,, ${
            #     'if Admin.IS_INSIDE': '#if Admin.IS_INSIDE',
            #     '"FORCE_PASS_THROUGH"': "{'PASS_THROUGH'}",
            #     '#if Admin.IS_INSIDE is False: ': ''
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(CONTEXT_AREA)
                if hud_region is None: Admin.IS_HUD = False
                else:
                    hud_L = hud_region.x
                    hud_B = hud_region.y
                    if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                        return {'PASS_THROUGH'}
                        # <<< 1copy (0m_outside_evt,, $$)

                        Admin.IS_INSIDE = False
                        bpy.context.window.cursor_modal_restore()
                        if W_FOCUS[0] != None:
                            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                            W_FOCUS[0] = None
                        kill_evt()
                        # >>>

                        return {'PASS_THROUGH'}
            # >>>

            for e in reversed(W_MODAL):
                if e.modal() is True:
                    if W_FOCUS[0] != e:
                        if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                        W_FOCUS[0] = e
                    # <<< 1copy (Admin_set_cursor,, $$)
                    if Admin.TAG_CURSOR:
                        if Admin.TAG_CURSOR == 'restore':
                            bpy.context.window.cursor_modal_restore()

                            Admin.CURSOR_TYPE = None
                        else:
                            if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                except: pass

                                Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                        Admin.TAG_CURSOR = ''
                    # >>>
                    return {'RUNNING_MODAL'}

            return {'PASS_THROUGH'}
        # */

    def i_modal_push(self, evt):

        self.u_modal = self.i_modal

        if Admin.TIMER is not None: remove_timer()

        if Admin.ENDPUSH is True: pass
        else:
            Admin.ENDPUSH = True
            return {'RUNNING_MODAL'}

        # <<< 1copy (0m_Admin_i_modal,, $$)
        if W_HEAD:
            get_evt(evt)
            if W_HEAD[-1].modal() == "FORCE_PASS_THROUGH":
                # <<< 1copy (Admin_set_cursor,, $$)
                if Admin.TAG_CURSOR:
                    if Admin.TAG_CURSOR == 'restore':
                        bpy.context.window.cursor_modal_restore()

                        Admin.CURSOR_TYPE = None
                    else:
                        if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                            try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                            except: pass

                            Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                    Admin.TAG_CURSOR = ''
                # >>>
                return {'PASS_THROUGH'}
            # <<< 1copy (Admin_set_cursor,, $$)
            if Admin.TAG_CURSOR:
                if Admin.TAG_CURSOR == 'restore':
                    bpy.context.window.cursor_modal_restore()

                    Admin.CURSOR_TYPE = None
                else:
                    if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                        try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                        except: pass

                        Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                Admin.TAG_CURSOR = ''
            # >>>
            return {'RUNNING_MODAL'}

        if Admin.IS_INSIDE is True:
            get_evt(evt)

            x = evt.mouse_region_x
            y = evt.mouse_region_y
            rd = REGION_DATA
            if x < rd.L or x > rd.R or y < rd.B or y > rd.T:
                # <<< 1copy (0m_outside_evt,, $$)

                Admin.IS_INSIDE = False
                bpy.context.window.cursor_modal_restore()
                if W_FOCUS[0] != None:
                    if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                    W_FOCUS[0] = None
                kill_evt()
                # >>>
                return {'PASS_THROUGH'}

            # <<< 1copy (0m_check_hud,, ${
            #     'if Admin.IS_INSIDE': '#if Admin.IS_INSIDE',
            #     '"FORCE_PASS_THROUGH"': "{'PASS_THROUGH'}"
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(CONTEXT_AREA)
                if hud_region is None: Admin.IS_HUD = False
                else:
                    hud_L = hud_region.x
                    hud_B = hud_region.y
                    if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                        #if Admin.IS_INSIDE is False: return {'PASS_THROUGH'}
                        # <<< 1copy (0m_outside_evt,, $$)

                        Admin.IS_INSIDE = False
                        bpy.context.window.cursor_modal_restore()
                        if W_FOCUS[0] != None:
                            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                            W_FOCUS[0] = None
                        kill_evt()
                        # >>>

                        return {'PASS_THROUGH'}
            # >>>

            if Admin.TB_ENABLE == True:
                if y < rd.B + SIZE_tb[0]:
                    rd.upd(CONTEXT_AREA, CONTEXT_REGION)
                    if rd.L + SIZE_tb[1] < x < rd.R and rd.B < y < rd.B + SIZE_tb[0]:
                        self.u_modal_tb()
                        # <<< 1copy (Admin_set_cursor,, $$)
                        if Admin.TAG_CURSOR:
                            if Admin.TAG_CURSOR == 'restore':
                                bpy.context.window.cursor_modal_restore()

                                Admin.CURSOR_TYPE = None
                            else:
                                if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                    try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                    except: pass

                                    Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                            Admin.TAG_CURSOR = ''
                        # >>>
                        return {'RUNNING_MODAL'}

            for e in reversed(W_MODAL):
                if e.modal() is True:
                    if W_FOCUS[0] != e:
                        if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                        W_FOCUS[0] = e
                    # <<< 1copy (Admin_set_cursor,, $$)
                    if Admin.TAG_CURSOR:
                        if Admin.TAG_CURSOR == 'restore':
                            bpy.context.window.cursor_modal_restore()

                            Admin.CURSOR_TYPE = None
                        else:
                            if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                except: pass

                                Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                        Admin.TAG_CURSOR = ''
                    # >>>
                    return {'RUNNING_MODAL'}

            # <<< 1copy (0m_outside_evt,, $$)

            Admin.IS_INSIDE = False
            bpy.context.window.cursor_modal_restore()
            if W_FOCUS[0] != None:
                if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                W_FOCUS[0] = None
            kill_evt()
            # >>>
            return {'PASS_THROUGH'}
        else:
            x = evt.mouse_region_x
            y = evt.mouse_region_y
            rd = REGION_DATA
            if x < rd.L or x > rd.R or y < rd.B or y > rd.T: return {'PASS_THROUGH'}

            if Admin.TB_ENABLE == True:
                if y < rd.B + SIZE_tb[0]:
                    rd.upd(CONTEXT_AREA, CONTEXT_REGION)
                    if rd.L + SIZE_tb[1] < x < rd.R and rd.B < y < rd.B + SIZE_tb[0]:
                        self.inside_evt()
                        kill_evt()
                        get_evt(evt)
                        self.u_modal_tb()
                        # <<< 1copy (Admin_set_cursor,, $$)
                        if Admin.TAG_CURSOR:
                            if Admin.TAG_CURSOR == 'restore':
                                bpy.context.window.cursor_modal_restore()

                                Admin.CURSOR_TYPE = None
                            else:
                                if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                    try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                    except: pass

                                    Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                            Admin.TAG_CURSOR = ''
                        # >>>
                        return {'RUNNING_MODAL'}

            kill_evt()
            get_evt(evt)

            # <<< 1copy (0m_check_hud,, ${
            #     'if Admin.IS_INSIDE': '#if Admin.IS_INSIDE',
            #     '"FORCE_PASS_THROUGH"': "{'PASS_THROUGH'}",
            #     '#if Admin.IS_INSIDE is False: ': ''
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(CONTEXT_AREA)
                if hud_region is None: Admin.IS_HUD = False
                else:
                    hud_L = hud_region.x
                    hud_B = hud_region.y
                    if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                        return {'PASS_THROUGH'}
                        # <<< 1copy (0m_outside_evt,, $$)

                        Admin.IS_INSIDE = False
                        bpy.context.window.cursor_modal_restore()
                        if W_FOCUS[0] != None:
                            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                            W_FOCUS[0] = None
                        kill_evt()
                        # >>>

                        return {'PASS_THROUGH'}
            # >>>

            for e in reversed(W_MODAL):
                if e.modal() is True:
                    if W_FOCUS[0] != e:
                        if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                        W_FOCUS[0] = e
                    # <<< 1copy (Admin_set_cursor,, $$)
                    if Admin.TAG_CURSOR:
                        if Admin.TAG_CURSOR == 'restore':
                            bpy.context.window.cursor_modal_restore()

                            Admin.CURSOR_TYPE = None
                        else:
                            if Admin.CURSOR_TYPE != Admin.TAG_CURSOR:
                                try: bpy.context.window.cursor_modal_set(Admin.TAG_CURSOR)
                                except: pass

                                Admin.CURSOR_TYPE = Admin.TAG_CURSOR

                        Admin.TAG_CURSOR = ''
                    # >>>
                    return {'RUNNING_MODAL'}

            return {'PASS_THROUGH'}
        # >>>
        #|
    def i_modal_force_pass_through(self, evt):
        self.u_modal = self.i_modal_force_pass_through_callback

        return {'PASS_THROUGH'}
        #|
    def i_modal_force_pass_through_callback(self, evt):
        self.u_modal = self.i_modal

        if Admin.TIMER is not None: remove_timer()
        force_pass_through.callback()
        return {'PASS_THROUGH'}
        #|
    def i_modal_pass_always(self, evt):
        return {'PASS_THROUGH'}
        #|

    def to_modal_tb(self):

        w = TaskBarModalHead()

        # <<< 1dict (2m_ADMIN_boxes,, $
        # if MOUSE[0] < self.boxes[|box_tb_start|].R:$)
        if MOUSE[0] < self.boxes[1].R:
        # >>>
            self.evt_start()
            return
        else:
            for e in TASKS:
                if e.box_icon.in_LR(MOUSE):
                    self.evt_task(e)
                    return

        # <<< 1dict (2m_ADMIN_boxes,, $
        # self.boxes[|box_tb_hover|].LRBT_upd(0, 0, 0, 0)$)
        self.boxes[3].LRBT_upd(0, 0, 0, 0)
        # >>>
        Admin.REDRAW()
        w.modal()
        #|

    def evt_task(self, task):
        #|
        # <<< 1dict (2m_ADMIN_boxes,, $
        # hover = self.boxes[|box_tb_hover|]$)
        hover = self.boxes[3]
        # >>>
        icon = task.box_icon

        # /* 0m_evt_task_check
        global _is_allow_task_evt
        if hover.L == icon.L and hover.R == icon.R and hover.B == icon.B and hover.T == icon.T:
            if EVT_TYPE[1] == 'RELEASE':
                _is_allow_task_evt = True
        else:
            hover.LRBT_upd(*icon.r_LRBT())
            Admin.REDRAW()
            _is_allow_task_evt = True
        # */

        if _is_allow_task_evt is True:
            if TRIGGER['rm']():
                DropDownTaskRM(task, (icon.L, icon.B))
                return
            if TRIGGER['click']():
                _is_allow_task_evt = False

                if len(task.ws) == 1:
                    w = task.ws[0]
                    if w in W_MODAL:
                        if W_MODAL[-1] == w: self.evt_min(w)
                        else: bring_to_front(w)
                    else: self.evt_unmin(w)
                else:
                    # <<< 1dict (2win_blfs,, $
                    # items = [NameValue(w.blfs[|blf_title|].unclip_text, w)  for w in task.ws]$)
                    items = [NameValue(w.blfs[0].unclip_text, w)  for w in task.ws]
                    # >>>
                    DropDownTask(self, (icon.L, icon.B), items, task.ws[0].name)
                return
        #|
    def evt_start(self):
        #|
        # <<< 1dict (2m_ADMIN_boxes,, $
        # hover = self.boxes[|box_tb_hover|]$)
        hover = self.boxes[3]
        # >>>
        # <<< 1dict (2m_ADMIN_boxes,, $
        # icon = self.boxes[|box_tb_start|]$)
        icon = self.boxes[1]
        # >>>

        # <<< 1copy (0m_evt_task_check,, $$)
        global _is_allow_task_evt
        if hover.L == icon.L and hover.R == icon.R and hover.B == icon.B and hover.T == icon.T:
            if EVT_TYPE[1] == 'RELEASE':
                _is_allow_task_evt = True
        else:
            hover.LRBT_upd(*icon.r_LRBT())
            Admin.REDRAW()
            _is_allow_task_evt = True
        # >>>

        if TRIGGER['click']() and _is_allow_task_evt:
            _is_allow_task_evt = False

            DropDownStartMenu(icon.r_LRBT())
        #|
    def evt_min(self, w):

        #|
        Admin.REDRAW()
        cls_name = w.__class__.__name__
        task = TASKS[D_TASKS_IND[cls_name]]
        W_MODAL.remove(w)
        W_DRAW.remove(w)

        W_FOCUS[0] = None
        if W_MODAL:
            self = W_MODAL[-1]
            self.box_win.color = COL_win_title
            # <<< 1dict (2m_ADMIN_boxes,, $
            # ADMIN.boxes[|box_tb_active|].LRBT_upd(*TASKS[D_TASKS_IND[self.__class__.__name__]].box_icon.r_LRBT())$)
            ADMIN.boxes[2].LRBT_upd(*TASKS[D_TASKS_IND[self.__class__.__name__]].box_icon.r_LRBT())
            # >>>
        else:
            # <<< 1dict (2m_ADMIN_boxes,, $
            # ADMIN.boxes[|box_tb_active|].LRBT_upd(0, 0, 0, 0)$)
            ADMIN.boxes[2].LRBT_upd(0, 0, 0, 0)
            # >>>

        if hasattr(w, "evt_min_callback"): w.evt_min_callback()
        #|
    def evt_unmin(self, w):

        #|
        Admin.REDRAW()
        cls_name = w.__class__.__name__
        task = TASKS[D_TASKS_IND[cls_name]]
        if W_MODAL:
            W_MODAL[-1].box_win.color = COL_win_title_inactive
        W_MODAL.append(w)
        W_DRAW.append(w)
        w.box_win.color = COL_win_title

        # <<< 1dict (2m_ADMIN_boxes,, $
        # self.boxes[|box_tb_active|].LRBT_upd(*task.box_icon.r_LRBT())$)
        self.boxes[2].LRBT_upd(*task.box_icon.r_LRBT())
        # >>>

        tag_obj_rename()
        # <<< 1copy (0m_update_data,, ${'for e in W_MODAL: e.upd_data()':'w.upd_data()'}$)
        TAG_UPDATE[1] = True

        BlendDataTemp.init()
        w.upd_data()
        BlendDataTemp.kill()
        TAG_UPDATE[1] = False

        if TAG_RENAME[0] is True:
            TAG_RENAME[0] = False
        # >>>
        if hasattr(w, "evt_unmin_callback"): w.evt_unmin_callback()
        #|
    def evt_sys_off(self, sleep=False):

        def modal_fin(evt):

            kill_admin(sleep=sleep)
            return {"CANCELLED"}

        self.u_modal = modal_fin

        if Admin.TIMER is None:
            Admin.TIMER = bpy.context.window_manager.event_timer_add(0, window=bpy.context.window)
        #|

    def to_modal_fin(self):
        self.u_modal = lambda evt: kill_admin()

        if Admin.TIMER is None:
            Admin.TIMER = bpy.context.window_manager.event_timer_add(0, window=bpy.context.window)
        #|

    def push_modal(self):
        #|
        self.u_modal = self.i_modal_push

        if Admin.TIMER is None:
            Admin.TIMER = bpy.context.window_manager.event_timer_add(0, window=bpy.context.window)

        #|

    def inside_evt(self):
        context = bpy.context
        Admin.IS_INSIDE = True
        Admin.CURSOR_TYPE = None
        Admin.TAG_CURSOR = 'DEFAULT'
        REGION_DATA.upd(CONTEXT_AREA, CONTEXT_REGION)
        Admin.IS_HUD = r_hud_region(CONTEXT_AREA) is not None

        # <<< 1dict (2m_ADMIN_boxes,, $
        # e = self.boxes[|box_tb|]$)
        e = self.boxes[0]
        # >>>
        # <<< 1dict (2m_ADMIN_boxes,, $
        # if e.R == CONTEXT_REGION.width and e.B == REGION_DATA.B and self.boxes[|box_tb_start|].L == REGION_DATA.L + SIZE_tb[1]: pass$)
        if e.R == CONTEXT_REGION.width and e.B == REGION_DATA.B and self.boxes[1].L == REGION_DATA.L + SIZE_tb[1]: pass
        # >>>
        else:
            self.upd_size()
            Admin.REDRAW()


        # <<< 1copy (0m_draw_update_data,, $$)
        TAG_UPDATE[0] = False
        if TAG_UPDATE[2]:
            # <<< 1copy (0m_update_data,, $$)
            TAG_UPDATE[1] = True

            BlendDataTemp.init()
            for e in W_MODAL: e.upd_data()
            BlendDataTemp.kill()
            TAG_UPDATE[1] = False

            if TAG_RENAME[0] is True:
                TAG_RENAME[0] = False
            # >>>
        # >>>
        #|
    def outside_evt(self):
        # /* 0m_outside_evt

        Admin.IS_INSIDE = False
        bpy.context.window.cursor_modal_restore()
        if W_FOCUS[0] != None:
            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
            W_FOCUS[0] = None
        kill_evt()
        # */

    def disable_taskbar(self):
        Admin.TB_ENABLE = False
        self.u_draw = N
        #|
    def enable_taskbar(self):
        Admin.TB_ENABLE = True
        self.u_draw = self.i_draw
        #|

    def i_draw(self):
        #|
        blend_set('ALPHA')
        for e in self.boxes: e.bind_draw()
        for e in TASKS:
            e.box_icon.bind_draw()
            e.box_multibar.bind_draw()
        #|

    def reg(self, w):
        if W_MODAL:
            W_MODAL[-1].box_win.color = COL_win_title_inactive

        cls = w.__class__

        W_PROCESS.append(w)
        W_MODAL.append(w)
        W_DRAW.append(w)
        # if hasattr(cls, "WS"):
        #     if isinstance(cls.WS, set): cls.WS.add(w)

        cls_name = cls.__name__
        task = r_task_by_clsname(cls_name)
        if task == None:
            D_TASKS_IND[cls_name] = len(TASKS)
            task = Task(w, getattr(blg, f'GpuImg_{cls_name}', GpuImgNull))
            TASKS.append(task)
        else:
            task.ws.append(w)
            task.update_multibar()

        # <<< 1dict (2m_ADMIN_boxes,, $
        # self.boxes[|box_tb_active|].LRBT_upd(*task.box_icon.r_LRBT())$)
        self.boxes[2].LRBT_upd(*task.box_icon.r_LRBT())
        # >>>
        #|

    def unreg(self, w):
        cls = w.__class__

        W_PROCESS.remove(w)
        W_MODAL.remove(w)
        W_DRAW.remove(w)
        # if hasattr(cls, "WS"):
        #     if isinstance(cls.WS, set): cls.WS.remove(w)

        cls_name = cls.__name__
        ind = D_TASKS_IND[cls_name]
        task = TASKS[ind]
        task.ws.remove(w)
        if task.ws: task.update_multibar()
        else:
            del TASKS[ind]
            D_TASKS_IND.clear()
            h = SIZE_tb[0]
            # <<< 1dict (2m_ADMIN_boxes,, $
            # tb_start = ADMIN.boxes[|box_tb_start|]$)
            tb_start = ADMIN.boxes[1]
            # >>>
            L = tb_start.R
            R = L + h

            for r, e in enumerate(TASKS):
                D_TASKS_IND[e.ws[0].__class__.__name__] = r
                ee = e.box_icon
                ee.L = L
                ee.R = R
                ee.upd()
                L += h
                R += h
                e.update_multibar()

        if W_MODAL:
            act = W_MODAL[-1]
            act.box_win.color = COL_win_title
            # <<< 1dict (2m_ADMIN_boxes,, $
            # ADMIN.boxes[|box_tb_active|].LRBT_upd(*TASKS[D_TASKS_IND[act.__class__.__name__]].box_icon.r_LRBT())$)
            ADMIN.boxes[2].LRBT_upd(*TASKS[D_TASKS_IND[act.__class__.__name__]].box_icon.r_LRBT())
            # >>>
            upd_temp_pref(act)
        else:
            # <<< 1dict (2m_ADMIN_boxes,, $
            # self.boxes[|box_tb_active|].LRBT_upd(0, 0, 0, 0)$)
            self.boxes[2].LRBT_upd(0, 0, 0, 0)
            # >>>
        #|
    #|
    #|

class Task:
    __slots__ = (
        'ws',
        'box_icon',
        'box_multibar')

    def __init__(self, w, icon):
        self.ws = [w]
        h = SIZE_tb[0]
        # <<< 1dict (2m_ADMIN_boxes,, $
        # tb_start = ADMIN.boxes[|box_tb_start|]$)
        tb_start = ADMIN.boxes[1]
        # >>>
        L = tb_start.R + len(TASKS) * h
        self.box_icon = icon(L, L + h, tb_start.B, tb_start.T)
        self.box_icon.upd()
        self.box_multibar = GpuBox_box_tb_multibar()
        self.box_multibar.upd()
        #|

    def update_multibar(self):
        if len(self.ws) == 1:
            self.box_multibar.LRBT_upd(0, 0, 0, 0)
        else:
            e = self.box_icon
            d = SIZE_tb[0] // 20
            self.box_multibar.LRBT_upd(e.L + d, e.R - d, e.B, min(e.T, e.B + SIZE_tb[2]))
        #|
    #|
    #|
def r_task_by_clsname(clsname):
    if clsname in D_TASKS_IND: return TASKS[D_TASKS_IND[clsname]]
    return None
    #|

class TaskBarModalHead:
    __slots__ = ()

    def __init__(self):
        W_HEAD.append(self)
        blockblsubwindows()
        #|

    def modal(self):
        evt = Admin.EVT
        # <<< 1copy (0m_check_hud,, $$)
        if Admin.IS_HUD is True:
            hud_region = r_hud_region(CONTEXT_AREA)
            if hud_region is None: Admin.IS_HUD = False
            else:
                hud_L = hud_region.x
                hud_B = hud_region.y
                if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                    if Admin.IS_INSIDE is False: return "FORCE_PASS_THROUGH"
                    # <<< 1copy (0m_outside_evt,, $$)

                    Admin.IS_INSIDE = False
                    bpy.context.window.cursor_modal_restore()
                    if W_FOCUS[0] != None:
                        if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                        W_FOCUS[0] = None
                    kill_evt()
                    # >>>

                    return "FORCE_PASS_THROUGH"
        # >>>

        boxes = ADMIN.boxes
        # <<< 1dict (2m_ADMIN_boxes,, $
        # tb_start = boxes[|box_tb_start|]$)
        tb_start = boxes[1]
        # >>>

        if tb_start.L < MOUSE[0] < REGION_DATA.R and tb_start.B < MOUSE[1] < tb_start.T:
            if MOUSE[0] < tb_start.R:
                ADMIN.evt_start()
                return
            else:
                for e in TASKS:
                    if e.box_icon.in_LR(MOUSE):
                        ADMIN.evt_task(e)
                        return

            # <<< 1dict (2m_ADMIN_boxes,, $
            # boxes[|box_tb_hover|].LRBT_upd(0, 0, 0, 0)$)
            boxes[3].LRBT_upd(0, 0, 0, 0)
            # >>>
            Admin.REDRAW()

            if TRIGGER['rm']():
                self.to_modal_rm()
                return
        else:
            W_HEAD.remove(self)
            # <<< 1dict (2m_ADMIN_boxes,, $
            # boxes[|box_tb_hover|].LRBT_upd(0, 0, 0, 0)$)
            boxes[3].LRBT_upd(0, 0, 0, 0)
            # >>>
            Admin.REDRAW()
            push_modal_safe()
        #|

    def to_modal_rm(self):

        items = [
            ("Move Active Window", self.evt_move_active_window),
            ("Reset Active Window Position", lambda :self.evt_move_active_window(reset_only=True)),
        ]
        DropDownRMKeymap(self, MOUSE, items, title="Taskbar")
        #|

    def evt_move_active_window(self, reset_only=False):
        if not W_MODAL:
            report("No active window found")
            return

        w = W_MODAL[-1]
        if hasattr(w, "to_modal_move"):
            if reset_only:
                if hasattr(w, "P_editor"):
                    P_temp.pos = w.P_editor.pos
                    w.end_modal_move()
                elif hasattr(w, "end_modal_move"):
                    w.end_modal_move()
            else:
                P_temp.pos = MOUSE
                w.to_modal_move()
        #|
    #|
    #|

class UpdWinActiveHead:
    __slots__ = 'end_modal'

    def __init__(self, end_modal=None):
        self.end_modal = end_modal
        W_HEAD.append(self)
        #|

    def modal(self):

        if self.end_modal is None: pass
        else:
            self.end_modal()

        W_HEAD.remove(self)

        upd_temp_pref(W_MODAL[-1])
        #|
    #|
    #|


def r_unit_factor(rna_unit, text_format):
    if rna_unit == "ROTATION":
        if text_format.__name__.find("deg") == -1: return 1.0
        else: return FLOAT_deg
    else:
        return UnitSystem.D_unit_factor[rna_unit]
    #|
class UnitSystem:
    __slots__ = ()

    unit_system = ""
    unit_length = ""
    unit_rotation = ""
    unit_mass = ""
    unit_time = ""
    unit_temperature = ""
    format_int = None
    format_float = None
    D_format = {}
    D_unit_factor = {
        'INT': 1.0,
        'NONE': 1.0,
        'LENGTH': 1.0,
        'AREA': 1.0,
        'VOLUME': 1.0,
        'ROTATION': 1.0,
        'TIME': 1.0,
        'TIME_ABSOLUTE': 1.0,
        'VELOCITY': 1.0,
        'ACCELERATION': 1.0,
        'MASS': 1.0,
        'CAMERA': 1.0,
        'POWER': 1.0,
        'TEMPERATURE': 1.0}
    D_unit_display = {
        'INT': '',
        'NONE': '',
        'LENGTH': '',
        'AREA': '',
        'VOLUME': '',
        'ROTATION': '°', # fixed
        'TIME': '',
        'TIME_ABSOLUTE': '',
        'VELOCITY': '',
        'ACCELERATION': '',
        'MASS': '',
        'CAMERA': '',
        'POWER': '',
        'TEMPERATURE': ''}
    D_type_format_float = {}

    @staticmethod
    def r_unit_flo(s, unit_system, unit_length, rna_unit="LENGTH"):
        unit_scale = _bpy.context.scene.unit_settings.scale_length
        if unit_scale <= 9.999999717180685e-10: unit_scale = 1.0
        if unit_scale == 1.0:
            return units_to_value(unit_system, rna_unit, s, str_ref_unit=unit_length)
        return units_to_value(unit_system, rna_unit, s, str_ref_unit=unit_length) / unit_scale
        #|

    @classmethod
    def rs_format_length(cls, f):
        return f'{cls.format_float(f / D_unit_factor["LENGTH"])} {D_unit_display["LENGTH"]}'
        #|
    @classmethod
    def rs_format_area(cls, f):
        return f'{cls.format_float(f / D_unit_factor["AREA"])} {D_unit_display["AREA"]}'
        #|
    @classmethod
    def rs_format_volume(cls, f):
        return f'{cls.format_float(f / D_unit_factor["VOLUME"])} {D_unit_display["VOLUME"]}'
        #|
    @classmethod
    def rs_format_deg(cls, f):
        return f'{cls.format_float(f / FLOAT_deg)} °'
        #|
    @classmethod
    def rs_format_mass(cls, f):
        return f'{cls.format_float(f / D_unit_factor["MASS"])} {D_unit_display["MASS"]}'
        #|
    @classmethod
    def rs_format_time(cls, f):
        return f'{cls.format_float(f / D_unit_factor["TIME_ABSOLUTE"])} {D_unit_display["TIME_ABSOLUTE"]}'
        #|
    @classmethod
    def rs_format_velocity(cls, f):
        return f'{cls.D_format["LENGTH"](f)} / s'
        #|
    @classmethod
    def rs_format_acceleration(cls, f):
        return f'{cls.D_format["LENGTH"](f)} / s²'
        #|
    @classmethod
    def rs_format_temperature(cls, f): pass
    @classmethod
    def rs_format_length_adaptive(cls, f):
        return "  " + units_to_string(cls.unit_system, "LENGTH", f, precision=20)
        #|
    @classmethod
    def rs_format_area_adaptive(cls, f):
        return "  " + units_to_string(cls.unit_system, "AREA", f, precision=20)
        #|
    @classmethod
    def rs_format_volume_adaptive(cls, f):
        return "  " + units_to_string(cls.unit_system, "VOLUME", f, precision=20)
        #|
    @classmethod
    def rs_format_mass_adaptive(cls, f):
        return "  " + units_to_string(cls.unit_system, "MASS", f, precision=20)
        #|
    @classmethod
    def rs_format_time_adaptive(cls, f):
        return "  " + units_to_string(cls.unit_system, "TIME", f, precision=20)
        #|
    @classmethod
    def rs_format_temperature_adaptive(cls, f):
        return "  " + units_to_string(cls.unit_system, "TEMPERATURE", f, precision=20)
        #|
    @classmethod
    def rs_format_percentage_int(cls, f):
        return f'{cls.format_int(f)} %'
        #|
    @classmethod
    def rs_format_percentage_float(cls, f):
        return f'{cls.format_float(f)} %'
        #|

    @classmethod
    def update(cls):
        if not _bpy.context or not _bpy.context.scene: return
        unit_system = _bpy.context.scene.unit_settings.system
        unit_length = _bpy.context.scene.unit_settings.length_unit
        unit_rotation = _bpy.context.scene.unit_settings.system_rotation
        unit_mass = _bpy.context.scene.unit_settings.mass_unit
        unit_time = _bpy.context.scene.unit_settings.time_unit
        unit_temperature = _bpy.context.scene.unit_settings.temperature_unit
        cls.unit_system = unit_system
        cls.unit_length = unit_length
        cls.unit_rotation = unit_rotation
        cls.unit_mass = unit_mass
        cls.unit_time = unit_time
        cls.unit_temperature = unit_temperature

        r_unit_flo = cls.r_unit_flo
        f1 = r_unit_flo("1", unit_system, unit_length)
        f2 = f1 * f1
        D_unit_factor["VOLUME"] = f1 * f2
        D_unit_factor["AREA"] = f2
        D_unit_factor["LENGTH"] = f1
        D_unit_factor["VELOCITY"] = f1
        D_unit_factor["ACCELERATION"] = f1
        D_unit_factor["CAMERA"] = f1
        e = cls.D_format

        if P.format_float in cls.D_type_format_float:
            format_float = cls.D_type_format_float[P.format_float]
        else:
            format_float = rs_format_float6_rstrip
        cls.format_float = format_float
        e["NONE"] = format_float
        e["TIME"] = format_float
        e["POWER"] = format_float

        if unit_system == "METRIC":
            if unit_length in D_length_unit_to_display:
                D_unit_display["LENGTH"] = D_length_unit_to_display[unit_length]
                e["LENGTH"] = cls.rs_format_length
                e["AREA"] = cls.rs_format_area
                e["VOLUME"] = cls.rs_format_volume
            else:
                D_unit_display["LENGTH"] = ""
                e["LENGTH"] = cls.rs_format_length_adaptive
                e["AREA"] = cls.rs_format_area_adaptive
                e["VOLUME"] = cls.rs_format_volume_adaptive
        elif unit_system == "IMPERIAL":
            if unit_length in D_length_unit_to_display:
                D_unit_display["LENGTH"] = D_length_unit_to_display[unit_length]
                e["LENGTH"] = cls.rs_format_length
                e["AREA"] = cls.rs_format_area
                e["VOLUME"] = cls.rs_format_volume
            else:
                D_unit_display["LENGTH"] = ""
                e["LENGTH"] = cls.rs_format_length_adaptive
                e["AREA"] = cls.rs_format_area_adaptive
                e["VOLUME"] = cls.rs_format_volume_adaptive
        else:
            D_unit_display["LENGTH"] = ""
            e["LENGTH"] = format_float
            e["AREA"] = cls.rs_format_area
            e["VOLUME"] = cls.rs_format_volume

        if P.show_length_unit == False: D_unit_display["LENGTH"] = ""
        if D_unit_display["LENGTH"]:
            if D_unit_display["LENGTH"] == '"':
                D_unit_display["AREA"] = "in²"
                D_unit_display["VOLUME"] = "in³"
            elif D_unit_display["LENGTH"] == "'":
                D_unit_display["AREA"] = "ft²"
                D_unit_display["VOLUME"] = "ft³"
            else:
                D_unit_display["AREA"] = D_unit_display["LENGTH"] + "²"
                D_unit_display["VOLUME"] = D_unit_display["LENGTH"] + "³"
        else:
            D_unit_display["AREA"] = "unit²"
            D_unit_display["VOLUME"] = "unit³"


        if unit_rotation == "DEGREES":
            D_unit_factor["ROTATION"] = FLOAT_deg
            e["ROTATION"] = cls.rs_format_deg
        else:
            D_unit_factor["ROTATION"] = 1.0
            e["ROTATION"] = format_float

        if unit_mass in D_mass_unit_to_display:
            e["MASS"] = cls.rs_format_mass
            u = D_mass_unit_to_display[unit_mass]
            D_unit_display["MASS"] = u
            if u in D_unit_replace: u = D_unit_replace[u]
        else:
            e["MASS"] = cls.rs_format_mass_adaptive
            u = ""
            D_unit_display["MASS"] = u
        D_unit_factor["MASS"] = r_unit_flo(f'1 {u}', unit_system, unit_length, "MASS")

        if unit_time in D_time_unit_to_display:
            e["TIME_ABSOLUTE"] = cls.rs_format_time
            u = D_time_unit_to_display[unit_time]
            D_unit_display["TIME_ABSOLUTE"] = u
            if u in D_unit_replace: u = D_unit_replace[u]
        else:
            e["TIME_ABSOLUTE"] = cls.rs_format_time_adaptive
            u = ""
            D_unit_display["TIME_ABSOLUTE"] = u
        D_unit_factor["TIME_ABSOLUTE"] = r_unit_flo(f'1 {u}', unit_system, unit_length, "TIME_ABSOLUTE")

        if unit_temperature in D_temperature_unit_to_display:
            e["TEMPERATURE"] = cls.rs_format_temperature_adaptive
            u = D_temperature_unit_to_display[unit_temperature]
            D_unit_display["TEMPERATURE"] = u
            if u in D_unit_replace: u = D_unit_replace[u]
        else:
            e["TEMPERATURE"] = cls.rs_format_temperature_adaptive
            u = ""
            D_unit_display["TEMPERATURE"] = u
        # D_unit_factor["TEMPERATURE"] = r_unit_flo(f'1 {u}', unit_system, unit_length, "TEMPERATURE")

        e["CAMERA"] = e["LENGTH"]
        e["VELOCITY"] = cls.rs_format_velocity
        e["ACCELERATION"] = cls.rs_format_acceleration

        #|

    #|
    #|
D_unit_factor = UnitSystem.D_unit_factor
D_unit_display = UnitSystem.D_unit_display


class LibraryModifier:
    __slots__ = (
        'gn_paths',
        'md_paths_MESH',
        'md_paths_CURVE',
        'md_paths_SURFACE',
        'md_paths_VOLUME',
        'md_paths_LATTICE',
        'md_paths_FONT',
        'md_paths_GREASEPENCIL',
        'types_items')

    def __init__(self):
        self.gn_paths = OrderedDict()
        self.md_paths_MESH = OrderedDict()
        self.md_paths_CURVE = OrderedDict()
        self.md_paths_SURFACE = OrderedDict()
        self.md_paths_VOLUME = OrderedDict()
        self.md_paths_LATTICE = OrderedDict()
        self.md_paths_FONT = OrderedDict()
        self.md_paths_GREASEPENCIL = OrderedDict()

        self.types_items = {
            "MESH": [],
            "CURVE": [],
            "SURFACE": [],
            "VOLUME": [],
            "LATTICE": [],
            "FONT": [],
            "GREASEPENCIL": [],
        }
        #|

    @staticmethod
    @ successResult
    def glob_blends(path, recursive, markonly):
        gn_paths = LIBRARY_MODIFIER.gn_paths
        md_paths_MESH = LIBRARY_MODIFIER.md_paths_MESH
        md_paths_CURVE = LIBRARY_MODIFIER.md_paths_CURVE
        md_paths_SURFACE = LIBRARY_MODIFIER.md_paths_SURFACE
        md_paths_VOLUME = LIBRARY_MODIFIER.md_paths_VOLUME
        md_paths_LATTICE = LIBRARY_MODIFIER.md_paths_LATTICE
        md_paths_FONT = LIBRARY_MODIFIER.md_paths_FONT
        md_paths_GREASEPENCIL = LIBRARY_MODIFIER.md_paths_GREASEPENCIL

        if P.md_lib_filter:
            lib_filter_text = P.md_lib_filter
            def filter_fx(ob):
                try: return bpyeval_ob(lib_filter_text, ob)
                except: return False
        else:
            def filter_fx(ob): return True

        libs = bpy.data.libraries
        old_libs = set(libs)
        nodes = bpy.data.node_groups
        objects = bpy.data.objects
        current_file_path = bpy.data.filepath

        for blend_path in r_glob_files(path, ".blend", recursive=recursive):
            if current_file_path == blend_path: continue
            try:
                old_nodes = set(nodes)

                with libs.load(blend_path, link=True) as (data_from, data_to):
                    data_to.node_groups = data_from.node_groups

                names = []
                if markonly:
                    for node in set(nodes).difference(old_nodes):
                        if node.type == "GEOMETRY" and node.asset_data:
                            if filter_fx(node):
                                names.append(NameLibrary(node.name, FilepathVersion(blend_path, "")))
                        nodes.remove(node)
                else:
                    for node in set(nodes).difference(old_nodes):
                        if node.type == "GEOMETRY":
                            if filter_fx(node):
                                names.append(NameLibrary(node.name, FilepathVersion(blend_path, "")))
                        nodes.remove(node)

                names.sort(key=lambda x: x.name)
                gn_paths[blend_path] = names
            except:
                gn_paths[blend_path] = []

            try:
                old_objects = set(objects)

                with libs.load(blend_path, link=True) as (data_from, data_to):
                    data_to.objects = data_from.objects

                names_MESH = []
                names_CURVE = []
                names_SURFACE = []
                names_VOLUME = []
                names_LATTICE = []
                names_FONT = []
                names_GREASEPENCIL = []

                if markonly:
                    for ob in set(objects).difference(old_objects):
                        if hasattr(ob, "modifiers") and ob.modifiers and ob.asset_data:
                            # /* 0m_glob_blends_modifier
                            for modifier in ob.modifiers:
                                if filter_fx(ob):
                                    if ob.type == "MESH":
                                        names_MESH.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "CURVE":
                                        names_CURVE.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "SURFACE":
                                        names_SURFACE.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "VOLUME":
                                        names_VOLUME.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "LATTICE":
                                        names_LATTICE.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "FONT":
                                        names_FONT.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "GREASEPENCIL":
                                        names_GREASEPENCIL.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                            # */
                        objects.remove(ob)
                else:
                    for ob in set(objects).difference(old_objects):
                        if hasattr(ob, "modifiers") and ob.modifiers:
                            # <<< 1copy (0m_glob_blends_modifier,, $$)
                            for modifier in ob.modifiers:
                                if filter_fx(ob):
                                    if ob.type == "MESH":
                                        names_MESH.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "CURVE":
                                        names_CURVE.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "SURFACE":
                                        names_SURFACE.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "VOLUME":
                                        names_VOLUME.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "LATTICE":
                                        names_LATTICE.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "FONT":
                                        names_FONT.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                                    elif ob.type == "GREASEPENCIL":
                                        names_GREASEPENCIL.append(NameLibraryIdentifier(modifier.name, FilepathVersion(blend_path, ob.name), modifier.type))
                            # >>>
                        objects.remove(ob)

                names_MESH.sort(key=lambda x: x.name)
                names_CURVE.sort(key=lambda x: x.name)
                names_SURFACE.sort(key=lambda x: x.name)
                names_VOLUME.sort(key=lambda x: x.name)
                names_LATTICE.sort(key=lambda x: x.name)
                names_FONT.sort(key=lambda x: x.name)
                names_GREASEPENCIL.sort(key=lambda x: x.name)

                md_paths_MESH[blend_path] = names_MESH
                md_paths_CURVE[blend_path] = names_CURVE
                md_paths_SURFACE[blend_path] = names_SURFACE
                md_paths_VOLUME[blend_path] = names_VOLUME
                md_paths_LATTICE[blend_path] = names_LATTICE
                md_paths_FONT[blend_path] = names_FONT
                md_paths_GREASEPENCIL[blend_path] = names_GREASEPENCIL
            except:
                md_paths_MESH[blend_path] = []
                md_paths_CURVE[blend_path] = []
                md_paths_SURFACE[blend_path] = []
                md_paths_VOLUME[blend_path] = []
                md_paths_LATTICE[blend_path] = []
                md_paths_FONT[blend_path] = []
                md_paths_GREASEPENCIL[blend_path] = []

        for e in set(libs).difference(old_libs):
            libs.remove(e)
        #|

    @staticmethod
    def ui_edit_path(button0=None, box_block=None):

        if button0 is None: return
        else:
            L, R, B, T = button0.box_button.r_LRBT()

        def confirm_fn(s):
            P.md_lib_filepath = s
            save_pref()
            message = LibraryModifier.ui_refresh_path(False)
            if message: return message
            return False

        def r_default_value(): return P.bl_rna.properties["md_lib_filepath"].default

        def bufn_clear():
            a0 = ddw.areas[0]
            ss = a0.tex.as_string()
            i0 = ss.find("directories")
            if i0 == -1: return
            if i0 != 0:
                if ss[i0 - 1] not in {"\n", " "}: return
            if ss[i0 + 11] not in {" ", "="}: return

            open_index = r_py_end_bracket_index(ss, i0, open_sign="", close_sign="(")
            if open_index == -1: return
            end_index = r_py_end_bracket_index(ss, open_index)
            a0.evt_del_all(undo_push=False)
            a0.beam_input(ss[ : open_index + 1] + "# Folder, Recursive, Marked assets only\n" + ss[end_index : ])

        def bufn_append():
            a0 = ddw.areas[0]

            def end_fn(s):
                s = s.replace("\\", "/")
                s = '\n    ("' + s + '", True, True),\n'
                ss = a0.tex.as_string()
                i0 = ss.find("directories")

                is_good_format = True
                if i0 == -1: is_good_format = False
                elif i0 != 0:
                    if ss[i0 - 1] not in {"\n", " "}: is_good_format = False
                if ss[i0 + 11] not in {" ", "="}: is_good_format = False

                open_index = r_py_end_bracket_index(ss, i0, open_sign="", close_sign="(")
                if open_index == -1: is_good_format = False
                end_index = r_py_end_bracket_index(ss, open_index)

                if is_good_format is True:
                    new_text = ss[ : end_index - 1] + s + ss[end_index : ]
                else:
                    new_text = ss + s

                a0.evt_del_all(undo_push=False)
                a0.beam_input(new_text)

            OpScanFolder.end_fn = end_fn
            bpy.ops.wm.vmd_scan_folder("INVOKE_DEFAULT")

        title_buttons = (
            (RnaButton("clear_paths", name="Clear Paths", button_text="Clear", description="", size=-3), bufn_clear),
            (RnaButton("append_paths", name="Append Path", button_text="Append Path", description="", size=-5), bufn_append),
        )

        ddw = DropDownText(button0, (box_block.L, R, T), P.md_lib_filepath, confirm_fn, r_default_value,
            title_buttons=title_buttons)
        #|
    @staticmethod
    def ui_refresh_path(report_dialog=True):


        global LIBRARY_MODIFIER
        if LIBRARY_MODIFIER is None: LIBRARY_MODIFIER = LibraryModifier()

        glob_blends = LIBRARY_MODIFIER.glob_blends
        gn_paths = LIBRARY_MODIFIER.gn_paths
        md_paths_MESH = LIBRARY_MODIFIER.md_paths_MESH
        md_paths_CURVE = LIBRARY_MODIFIER.md_paths_CURVE
        md_paths_SURFACE = LIBRARY_MODIFIER.md_paths_SURFACE
        md_paths_VOLUME = LIBRARY_MODIFIER.md_paths_VOLUME
        md_paths_LATTICE = LIBRARY_MODIFIER.md_paths_LATTICE
        md_paths_FONT = LIBRARY_MODIFIER.md_paths_FONT
        md_paths_GREASEPENCIL = LIBRARY_MODIFIER.md_paths_GREASEPENCIL

        gn_paths.clear()
        md_paths_MESH.clear()
        md_paths_CURVE.clear()
        md_paths_SURFACE.clear()
        md_paths_VOLUME.clear()
        md_paths_LATTICE.clear()
        md_paths_FONT.clear()
        md_paths_GREASEPENCIL.clear()

        types_items = LIBRARY_MODIFIER.types_items
        for e in types_items.values(): e.clear()

        directories, message = eval_md_lib(P.md_lib_filepath)
        if message:
            if report_dialog: DropDownOk(None, MOUSE, input_text=message)
            return message

        if isinstance(directories, tuple) or isinstance(directories, list): pass
        else:
            if report_dialog: DropDownOk(None, MOUSE, input_text="directories must be a list or tuple")
            return message

        message = []

        for r, e in enumerate(directories):
            if isinstance(e, list) or isinstance(e, tuple): pass
            else:
                message.append(f'Item {r} must be a list or tuple')
                continue
            if len(e) != 3:
                message.append(f'Item {r} length must be equal to 3')
                continue

            path, recursive, markonly = e
            if isinstance(path, str) and isinstance(recursive, bool) and isinstance(markonly, bool): pass
            else:
                message.append(f'Item {r} context must be (string, bool, bool)')
                continue

            if os_sep == "\\":
                path.replace("/", "\\")

            success, result = glob_blends(path, recursive, markonly)
            if result: message.append(result)

        if P.md_lib_use_essentials:
            blender_version = bpy.app.version
            lib_folder = Path(bpy.app.binary_path).parent.joinpath(
                os_path_join(f"{blender_version[0]}.{blender_version[1]}", "datafiles", "assets", "geometry_nodes")
                )

            if lib_folder.exists():
                success, result = glob_blends(lib_folder, True, False)
                if result: message.append(result)

        items_gn = sum(gn_paths.values(), [])
        types_items["MESH"][:] = items_gn + sum(md_paths_MESH.values(), []) + md_rnas_MESH
        types_items["CURVE"][:] = items_gn + sum(md_paths_CURVE.values(), []) + md_rnas_CURVE
        types_items["SURFACE"][:] = sum(md_paths_SURFACE.values(), []) + md_rnas_SURFACE
        types_items["VOLUME"][:] = items_gn + sum(md_paths_VOLUME.values(), []) + md_rnas_VOLUME
        types_items["LATTICE"][:] = sum(md_paths_LATTICE.values(), []) + md_rnas_LATTICE
        types_items["FONT"][:] = items_gn + sum(md_paths_FONT.values(), []) + md_rnas_FONT
        types_items["GREASEPENCIL"][:] = items_gn + sum(md_paths_GREASEPENCIL.values(), []) + md_rnas_GREASEPENCIL

        if message:
            message = "\n".join(message)
            if report_dialog: DropDownOk(None, MOUSE, input_text=message)
            return message

        if report_dialog: report("Modifier Library updated")
        #|
    #|
    #|

@ catchStr
def r_platform():
    import platform, gpu
    s = f'{platform.platform()}\n{gpu.platform.renderer_get()}  {gpu.platform.version_get()}\nblender {bpy.app.version_string}  commit date: {str(bpy.app.build_date, "utf-8")}  hash: {str(bpy.app.build_hash, "utf-8")}\nvmdesk {".".join(str(e)  for e in ADDON_VERSION)}'
    return s
    #|


def late_import():
    #|
    from .  import VMD

    BL_INFO = VMD.handle.BL_INFO

    # <<< 1copy (assignP,, $$)
    P = bpy.context.preferences.addons[__package__].preferences
    # >>>
    ADDON_VERSION = BL_INFO["version"]

    prefs = VMD.prefs
    util = VMD.util

    # <<< 1mp (util.com
    com = util.com
    N = com.N
    rs_format_int6 = com.rs_format_int6
    rs_format_float6 = com.rs_format_float6
    rs_format_float6_rstrip = com.rs_format_float6_rstrip
    rs_format_float_left = com.rs_format_float_left
    r_py_end_bracket_index = com.r_py_end_bracket_index
    # >>>

    # <<< 1mp (util.dirlib
    dirlib = util.dirlib
    r_glob_files = dirlib.r_glob_files
    # >>>
    # <<< 1mp (util.const
    const = util.const
    D_unit_replace = const.D_unit_replace
    D_length_unit_to_display = const.D_length_unit_to_display
    D_mass_unit_to_display = const.D_mass_unit_to_display
    D_time_unit_to_display = const.D_time_unit_to_display
    D_temperature_unit_to_display = const.D_temperature_unit_to_display
    FLOAT_deg = const.FLOAT_deg
    # >>>

    # <<< 1mp (util.types
    types = util.types
    RegionData = types.RegionData
    NameValue = types.NameValue
    NameLibrary = types.NameLibrary
    NameLibraryIdentifier = types.NameLibraryIdentifier
    FilepathVersion = types.FilepathVersion
    RnaButton = types.RnaButton
    # >>>

    blg = VMD.utilbl.blg

    subscribe_rna = bpy.msgbus.subscribe_rna
    clear_by_owner = bpy.msgbus.clear_by_owner
    P_temp = P.temp

    ADDON_FOLDER = __file__[: -4]

    W_PROCESS = []
    W_HEAD = []
    W_MODAL = []
    W_DRAW = []
    W_FOCUS = [None]
    TASKS = []
    D_TASKS_IND = {}
    DRAW_HANDLE = None
    DRAW_VIEW_HANDLE = None
    ADMIN = None
    CONTEXT_AREA = None
    CONTEXT_REGION = None
    CURSOR_WARP = None
    REGION_DATA = RegionData()
    TAG_UPDATE = [False, False, True] # tag_update, is_updating, is_enable_auto_update
    TAG_RENAME = [False]
    LIBRARY_MODIFIER = None

    _is_allow_task_evt = True

    UnitSystem.format_int = rs_format_int6
    UnitSystem.format_float = rs_format_float6
    UnitSystem.D_format.update({
        'INT': rs_format_int6,
        'NONE': rs_format_float6,
        'LENGTH': None,
        'AREA': None,
        'VOLUME': None,
        'ROTATION': None,
        'TIME': rs_format_float6,
        'TIME_ABSOLUTE': None,
        'VELOCITY': None,
        'ACCELERATION': None,
        'MASS': None,
        'CAMERA': None,
        'POWER': None,
        'TEMPERATURE': None
    })
    UnitSystem.D_type_format_float.update({
        'THOUSAND_SEPARATOR': rs_format_float6_rstrip,
        'THOUSAND_SEPARATOR_FULL': rs_format_float6,
        'NO_SEPARATOR_LEFT': rs_format_float_left
    })

    globals().update(locals())
    #|
def import_size():
    #|
    # <<< 1mp (blg
    FONT0 = blg.FONT0
    D_SIZE = blg.D_SIZE
    upd_font_size = blg.upd_font_size
    GpuBox_box_tb = blg.GpuBox_box_tb
    GpuBox_box_tb_multibar = blg.GpuBox_box_tb_multibar
    GpuImg_tb_start = blg.GpuImg_tb_start
    GpuImg_tb_active = blg.GpuImg_tb_active
    GpuImg_tb_hover = blg.GpuImg_tb_hover
    GpuImgNull = blg.GpuImgNull
    SIZE_tb = blg.SIZE_tb
    SIZE_title = blg.SIZE_title
    SIZE_border = blg.SIZE_border
    SIZE_widget = blg.SIZE_widget
    r_blf_clipping_end = blg.r_blf_clipping_end
    report = blg.report
    COL_win_title = blg.COL_win_title
    COL_win_title_inactive = blg.COL_win_title_inactive
    # >>>

    globals().update(locals())
    #|

def late_import_lv2():
    #|
    area = VMD.area
    block = VMD.block

    # <<< 1mp (VMD.dd
    dd = VMD.dd
    DropDownTask = dd.DropDownTask
    DropDownTaskRM = dd.DropDownTaskRM
    DropDownRMKeymap = dd.DropDownRMKeymap
    DropDownOk = dd.DropDownOk
    DropDownText = dd.DropDownText
    DropDownStartMenu = dd.DropDownStartMenu
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    get_evt = keysys.get_evt
    kill_evt = keysys.kill_evt
    kill_evt_except = keysys.kill_evt_except
    MOUSE = keysys.MOUSE
    TRIGGER = keysys.TRIGGER
    EVT_TYPE = keysys.EVT_TYPE
    MOUSE_WINDOW = keysys.MOUSE_WINDOW
    # >>>

    # <<< 1mp (VMD.evals.evalutil
    evalutil = VMD.evals.evalutil
    bpyeval_ob = evalutil.bpyeval_ob
    # >>>
    # <<< 1mp (VMD.evals.evalmdlib
    evalmdlib = VMD.evals.evalmdlib
    eval_md_lib = evalmdlib.eval_md_lib
    # >>>

    utilbl = VMD.utilbl

    # <<< 1mp (utilbl.md
    md = utilbl.md
    md_rnas_MESH = md.md_rnas_MESH
    md_rnas_CURVE = md.md_rnas_CURVE
    md_rnas_SURFACE = md.md_rnas_SURFACE
    md_rnas_VOLUME = md.md_rnas_VOLUME
    md_rnas_LATTICE = md.md_rnas_LATTICE
    md_rnas_FONT = md.md_rnas_FONT
    md_rnas_GREASEPENCIL = md.md_rnas_GREASEPENCIL
    # >>>

    # <<< 1mp (utilbl.ops
    ops = utilbl.ops
    OpScanFolder = ops.OpScanFolder
    # >>>

    vmd_blocking = bpy.ops.wm.vmd_blocking

    globals().update(locals())
    #|
