











from bpy.utils import escape_identifier
from . util.deco import catch, catchBug



def timer_beam():

    try: box_beam = SELF.box_beam
    except:

        return None

    box_beam.color = COL_box_cursor_beam_off  if box_beam.color == COL_box_cursor_beam else COL_box_cursor_beam

    Admin.REDRAW()
    return P_cursor_beam_time
    #|
def timer_selection():
    try:
        SELF.selection_timer_end()
        return None
    except: return None
    #|
def timer_undo_push():
    SELF.local_history.push()
    return None
def unreg_all_timer():
    if timer_isreg(timer_beam): timer_unreg(timer_beam)
    if timer_isreg(timer_selection): timer_unreg(timer_selection)
    if timer_isreg(timer_undo_push): timer_unreg(timer_undo_push)
    #|

def preview_datablock(datablock):
    if datablock:
        try: datablock.name_full
        except: return
    else: return

    if isinstance(datablock, Image):
        return DDPreviewImage(None, datablock,
            showname = P.preview_showname,
            scale = P.preview_scale)
    else:
        try:
            if OpsIDPreview.ID is None:
                OpsIDPreview.ID = datablock
                OpsIDPreview.show_name = P.preview_showname
                bpy.ops.wm.vmd_id_preview("INVOKE_DEFAULT", preview_scale=P.preview_scale)
        except: pass
    #|

#_c4#_c4#_c4#_c4
def C_filt_evt_head(self, override, poll_library=True, evtkill=True):
    if evtkill:
        kill_evt_except()

    ob = self.w.active_object
    if not ob: return None, None, None
    if override is None:
        # <<< 1copy (0AreaFilterYModifier_if_ind_safe,, $$)
        filt = self.filt
        blfs = filt.blfs
        if not blfs: return

        T = blfs[filt.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
        i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + filt.headkey

        if 0 <= i < len(filt.match_items):
        # >>>
            region_index = self.r_region_index(MOUSE[0], i)
        else: return None, None, None
    else:
        i, region_index = override

    if region_index in {"show_on_cage", "show_in_editmode", "show_viewport", "show_render"}:
        pass
    else:
        region_index = "name"

    if hasattr(self, "poll") and self.poll(self) == False:
        return None, None, None

    if poll_library:
        if hasattr(ob, "is_editable") and not ob.is_editable:
            if region_index == "show_viewport":
                return i, region_index, ob

            report(r_library_or_override_message(ob))
            return None, None, ob

    return i, region_index, ob
    #|
def C_filt_evt_head_no_override(self, ob, override, poll_library=True, evtkill=True):
    if evtkill:
        kill_evt_except()

    if not ob: return None, None, None
    if override is None:
        # <<< 1copy (0AreaFilterYModifier_if_ind_safe,, $$)
        filt = self.filt
        blfs = filt.blfs
        if not blfs: return

        T = blfs[filt.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
        i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + filt.headkey

        if 0 <= i < len(filt.match_items):
        # >>>
            region_index = self.r_region_index(MOUSE[0], i)
        else: return None, None, None
    else:
        i, region_index = override

    if hasattr(self, "poll") and self.poll(self) == False:
        return None, None, None

    if poll_library:
        s = r_unsupport_override_message(ob)
        if s:
            report(s)
            return None, None, ob

    return i, region_index, ob
    #|

#_c4#_c4#_c4#_c4

class StructAreaModal:
    __slots__ = ()

    def r_focus_element(self): return None
    def modal_focus_element_front(self, _e_): return False
    def modal_focus_element_back(self, _e_):
        if hasattr(self.w, "evt_search"):
            if TRIGGER['area_search']():
                self.w.evt_search()
                return
        if hasattr(self.w, "evt_undo"):
            if TRIGGER['redo']():
                self.w.evt_redo()
                return True
            if TRIGGER['undo']():
                self.w.evt_undo()
                return True
        return False
        #|
    def inside_evt(self): pass
    def outside_evt(self): pass
    def force_out(self): return False
    def modal(self):
        if self.box_area.inbox(MOUSE):
            w = self.w
            if hasattr(w, "win_inbox"): pass
            else:
                w = self.wind
            _win_inbox = w.win_inbox
            _is_inbox_other_win = w.is_inbox_other_win
            _basis_win_evt = w.basis_win_evt
            _box_area = self.box_area
            _r_focus_element = self.r_focus_element
            _modal_focus_element_front = self.modal_focus_element_front
            _modal_focus_element_back = self.modal_focus_element_back
            _outside_evt = self.outside_evt
            _force_out = self.force_out
            _evtkill = [True]
            _REDRAW = Admin.REDRAW

            def modal_local():
                evt = Admin.EVT
                # <<< 1copy (0m_check_hud,, ${
                #     'CONTEXT_AREA': 'm.CONTEXT_AREA',
                #     'return "FORCE_PASS_THROUGH"': '_w_.fin() ;return "FORCE_PASS_THROUGH"'
                # }$)
                if Admin.IS_HUD is True:
                    hud_region = r_hud_region(m.CONTEXT_AREA)
                    if hud_region is None: Admin.IS_HUD = False
                    else:
                        hud_L = hud_region.x
                        hud_B = hud_region.y
                        if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                            if Admin.IS_INSIDE is False: _w_.fin() ;return "FORCE_PASS_THROUGH"
                            # <<< 1copy (0m_outside_evt,, $$)

                            Admin.IS_INSIDE = False
                            bpy.context.window.cursor_modal_restore()
                            if W_FOCUS[0] != None:
                                if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                                W_FOCUS[0] = None
                            kill_evt()
                            # >>>

                            _w_.fin() ;return "FORCE_PASS_THROUGH"
                # >>>

                if _win_inbox(MOUSE) == False or _is_inbox_other_win() or _force_out():
                    _w_.fin()
                    return
                basis_evt_fn = _basis_win_evt()
                if basis_evt_fn != None:
                    _evtkill[0] = False
                    _w_.fin()
                    basis_evt_fn()
                    return
                if _box_area.inbox(MOUSE) == False:
                    _w_.fin()
                    return

                _e_ = _r_focus_element()

                if _e_ == None:
                    if self.focus_element != None:
                        _REDRAW()
                        if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
                        self.focus_element = None

                    if _modal_focus_element_front(_e_): return
                    _modal_focus_element_back(_e_)
                else:
                    if _e_ != self.focus_element:

                        if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()

                        self.focus_element = _e_
                        if hasattr(_e_, "inside_evt"): _e_.inside_evt()
                        _REDRAW()

                    if _modal_focus_element_front(_e_): return
                    if _e_.modal(): return
                    _modal_focus_element_back(_e_)
                #|
            def end_modal_local():
                _REDRAW()
                if hasattr(self.focus_element, "outside_evt"):
                    self.focus_element.outside_evt()
                    self.focus_element = None
                if _evtkill[0]: kill_evt_except()

                _outside_evt()
                #|

            self.focus_element = None
            self.inside_evt()

            evt = Admin.EVT
            # <<< 1copy (0m_check_hud,, ${
            #     'CONTEXT_AREA': 'm.CONTEXT_AREA'
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(m.CONTEXT_AREA)
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

            _w_ = Head(self, modal_local, end_modal_local)
            modal_local()
        #|
    @staticmethod
    def to_localmodal(self,
                    _box_area_inbox,
                    _r_focus_element,
                    _modal_focus_element_front,
                    _modal_focus_element_back,
                    _outside_evt,
                    _force_out,
                    w = None):


        if w is None:
            w = self.w
            if hasattr(w, "win_inbox"): pass
            else:
                w = self.wind

        _win_inbox = w.win_inbox
        _is_inbox_other_win = w.is_inbox_other_win
        _basis_win_evt = w.basis_win_evt
        _evtkill = [True]
        _REDRAW = Admin.REDRAW

        def modal_local():
            evt = Admin.EVT
            # <<< 1copy (0m_check_hud,, ${
            #     'CONTEXT_AREA': 'm.CONTEXT_AREA',
            #     'return "FORCE_PASS_THROUGH"': '_w_.fin() ;return "FORCE_PASS_THROUGH"'
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(m.CONTEXT_AREA)
                if hud_region is None: Admin.IS_HUD = False
                else:
                    hud_L = hud_region.x
                    hud_B = hud_region.y
                    if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                        if Admin.IS_INSIDE is False: _w_.fin() ;return "FORCE_PASS_THROUGH"
                        # <<< 1copy (0m_outside_evt,, $$)

                        Admin.IS_INSIDE = False
                        bpy.context.window.cursor_modal_restore()
                        if W_FOCUS[0] != None:
                            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                            W_FOCUS[0] = None
                        kill_evt()
                        # >>>

                        _w_.fin() ;return "FORCE_PASS_THROUGH"
            # >>>

            if _win_inbox(MOUSE) == False or _is_inbox_other_win() or _force_out():
                _w_.fin()
                return
            basis_evt_fn = _basis_win_evt()
            if basis_evt_fn != None:
                _evtkill[0] = False
                _w_.fin()
                basis_evt_fn()
                return
            if _box_area_inbox(MOUSE) == False:
                _w_.fin()
                return

            _e_ = _r_focus_element()
            _dic_["focus_element"] = _e_

            if _e_ == None:
                if self.focus_element != None:
                    _REDRAW()
                    if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
                    self.focus_element = None

                if _modal_focus_element_front(_dic_): return
                _modal_focus_element_back(_dic_)
            else:
                if _e_ != self.focus_element:

                    if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()

                    self.focus_element = _e_
                    if hasattr(_e_, "inside_evt"): _e_.inside_evt()
                    _REDRAW()

                if _modal_focus_element_front(_dic_): return
                if _e_.modal(): return
                _modal_focus_element_back(_dic_)
            #|
        def end_modal_local():
            _REDRAW()
            if hasattr(self.focus_element, "outside_evt"):
                self.focus_element.outside_evt()
                self.focus_element = None
            if _evtkill[0]: kill_evt_except()

            _outside_evt()
            #|

        self.focus_element = None

        evt = Admin.EVT
        # <<< 1copy (0m_check_hud,, ${
        #     'CONTEXT_AREA': 'm.CONTEXT_AREA'
        # }$)
        if Admin.IS_HUD is True:
            hud_region = r_hud_region(m.CONTEXT_AREA)
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

        _w_ = Head(self, modal_local, end_modal_local)
        _dic_ = {"w_head": _w_, "focus_element": None}
        modal_local()
        #|
    #|
    #|
class ScrollEvents:
    __slots__ = ()

    def scroll_region_events(self):
        if TRIGGER['dd_scroll_left_area']():
            self.evt_scrollX(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_right_area']():
            self.evt_scrollX(-P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_down_area']():
            self.evt_scrollY(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_up_area']():
            self.evt_scrollY(-P.scroll_distance)
            return True
        return False
        #|
    def scroll_area_events(self, usein_scroll_modal=True):
        if TRIGGER['dd_scroll_left_area']():
            self.evt_scrollX(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_right_area']():
            self.evt_scrollX(-P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_down_area']():
            self.evt_scrollY(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_up_area']():
            self.evt_scrollY(-P.scroll_distance)
            return True
        if usein_scroll_modal:
            if TRIGGER['dd_scroll']():
                self.to_modal_scrollbar()
                return True
        return False
        #|
    def scroll_events(self):
        if TRIGGER['dd_scroll_left_most']():
            self.evt_scrollX(self.box_area.r_w())
            return True
        if TRIGGER['dd_scroll_right_most']():
            self.evt_scrollX(-self.box_area.r_w())
            return True
        if TRIGGER['dd_scroll_down_most']():
            self.evt_scrollY(16777215)
            return True
        if TRIGGER['dd_scroll_up_most']():
            self.evt_scrollY(-16777215)
            return True
        if TRIGGER['dd_scroll_left']():
            self.evt_scrollX(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_right']():
            self.evt_scrollX(-P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_down']():
            self.evt_scrollY(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_up']():
            self.evt_scrollY(-P.scroll_distance)
            return True
        return False
        #|
    #|
    #|
class SearchDataArea:
    __slots__ = (
        'state',
        'old_search_text',
        'old_props',
        'button_search',
        'tag_reinit',
        'head_item_pos',
        'old_headkey',
        'raw_items',
        'raw_headkey',
        'owner_data')

    def __init__(self):
        self.state = False
        self.old_search_text = None
        self.old_props = None
        self.button_search = None
        self.tag_reinit = False
        self.head_item_pos = [0, 0]
        self.old_headkey = 0
        self.owner_data = {}
        #|

    def init_with(self, button_search):
        self.button_search = button_search

        if self.tag_reinit is True:
            self.tag_reinit = False
            self.owner_restore()
        else:
            self.state = False
            self.old_search_text = None
            self.old_props = None
            self.owner_data.clear()
        #|

    def owner_restore(self):
        for e, owner in self.owner_data.items():
            e.w = owner

        self.owner_data.clear()
        #|
    def end_search(self):
        self.state = False
        self.old_search_text = None
        self.old_props = None
        self.owner_restore()
        #|

    def get_head_item_pos(self, area):

        self.old_headkey = area.headkey
        if area.endkey == -1 or not area.items:
            self.head_item_pos[:] = area.box_region.inner[0], head_T
        else:
            b0 = area.items[area.headkey]
            if hasattr(b0, "box_block"):
                self.head_item_pos[:] = b0.box_block.L, b0.box_block.T
            else:
                self.head_item_pos[:] = area.box_region.inner[0], head_T
        #|
    #|
    #|


class AreaFilterY(StructAreaModal):
    __slots__ = (
        'w',
        'u_draw',
        'boxes',
        'is_flip_y',
        'is_dropdown',
        'box_area',
        'box_text',
        'box_icon_search',
        'box_filter',
        'box_selection',
        'box_beam',
        'box_match_end_bg',
        'box_match_whole_word_bg',
        'box_match_case_bg',
        'box_match_case',
        'box_match_whole_word',
        'box_match_end',
        'box_match_hover',
        'blf_text',
        'beam_index',
        'filt',
        'scissor_text_box',
        'scissor_filt',
        'local_history',
        'dd_parent',
        'focus_element',
        'readonly',
        'r_size_default')

    @staticmethod
    def calc_best_height(row_count):
        # d0 = SIZE_dd_border[0]
        # d1 = SIZE_dd_border[1]
        # widget_rim = SIZE_border[3]
        # filter_inner = SIZE_filter[2]
        # TT = 0
        # TT -= d0
        # B = TT - D_SIZE['widget_full_h']
        # T = B - d1 - widget_rim # box_filter_innerT
        # T0 = T - filter_inner
        # B0 = T0 - D_SIZE['widget_full_h'] * row_count - filter_inner
        # BB = B0 - widget_rim
        # h = - BB
        return SIZE_dd_border[0] + D_SIZE['widget_full_h'] + SIZE_dd_border[1] + D_SIZE[
            'widget_full_h'] * row_count + (SIZE_filter[2] + SIZE_border[3]) * 2
        #|
    @staticmethod
    def calc_height(inner_height):
        return SIZE_dd_border[0] + D_SIZE['widget_full_h'] + SIZE_dd_border[1] + inner_height + (
            SIZE_filter[2] + SIZE_border[3]) * 2
        #|

    def __init__(self, w, LL, RR, BB, TT, get_items,
                get_icon = None,
                get_info = None,
                is_flip_y = False,
                input_text = "",
                is_dropdown = False,
                filter_cls = None,
                r_size_default = None):
        #|
        self.w = w
        self.u_draw = self.i_draw
        self.is_flip_y = is_flip_y
        self.is_dropdown = is_dropdown
        if r_size_default is None: pass
        else:
            self.r_size_default = r_size_default

        box_area = GpuBox_area()
        box_text = GpuRim(COL_box_text, COL_box_text_rim)
        box_match_case = GpuImg_filter_match_case()
        box_match_whole_word = GpuImg_filter_match_whole_word()
        box_match_end = GpuImg_filter_match_end_left()
        box_match_end_bg = GpuImg_filter_match_active()
        box_match_whole_word_bg = GpuImg_filter_match_active()
        box_match_case_bg = GpuImg_filter_match_active()
        box_match_hover = GpuImg_filter_match_hover()
        box_icon_search = GpuImg_delete()  if input_text else GpuImg_search()
        box_filter = GpuRim(COL_box_filter, COL_box_filter_rim)
        box_selection = GpuBox(COL_box_text_selection)
        box_beam = GpuBox(COL_box_cursor_beam)
        blf_text = BlfClip("", input_text)
        blf_text.color = COL_box_text_fg
        box_match_hover.upd()

        self.boxes = [
            box_area,
            box_text,
            box_icon_search,
            box_filter,
            box_selection,
            box_beam,
            box_match_end_bg,
            box_match_whole_word_bg,
            box_match_case_bg,
            box_match_hover,
            box_match_end,
            box_match_whole_word,
            box_match_case
        ]
        self.box_area = box_area
        self.box_text = box_text
        self.box_icon_search = box_icon_search
        self.box_filter = box_filter
        self.box_selection = box_selection
        self.box_beam = box_beam
        self.box_match_end_bg = box_match_end_bg
        self.box_match_whole_word_bg = box_match_whole_word_bg
        self.box_match_case_bg = box_match_case_bg
        self.box_match_hover = box_match_hover
        self.box_match_end = box_match_end
        self.box_match_whole_word = box_match_whole_word
        self.box_match_case = box_match_case
        self.blf_text = blf_text
        self.scissor_text_box = Scissor()
        self.scissor_filt = Scissor()

        self.beam_index = [len(input_text)] * 2
        self.init_filt_and_size(LL, RR, BB, TT, get_items, get_icon, get_info, input_text, filter_cls)
        #|
    def init_filt_and_size(self, LL, RR, BB, TT, get_items, get_icon, get_info, input_text, filter_cls):
        self.filt = (FilterY  if filter_cls is None else filter_cls)(self, get_items, get_icon, get_info)

        # <<< 1copy (0area_AreaFilterY_upd_size,, $$)
        box_area = self.box_area
        old_L = box_area.L
        old_T = box_area.T
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]
        scissor_win = self.w.scissor

        LL += d0
        RR -= d0
        TT -= d0
        BB += d0

        box_text = self.box_text
        blf_text = self.blf_text

        if self.is_flip_y:
            T = BB + D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, BB, T, widget_rim)
            T += d1
            self.box_filter.LRBT_upd(LL, RR, T, TT, widget_rim)
        else:
            B = TT - D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, B, TT, widget_rim)
            B -= d1
            self.box_filter.LRBT_upd(LL, RR, BB, B, widget_rim)

        if hasattr(self, "r_parent_scissor"):
            self.upd_scissor_filt()
        else:
            self.upd_scissor_filt(scissor_win)

        L, R, B, T = box_text.inner
        L0 = box_text.L + widget_rim * 3
        L1 = L0 + SIZE_widget[0]

        self.box_icon_search.LRBT_upd(L0, L1, B, T)
        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L1 + D_SIZE['font_main_dx']
        blf_text.y = B + D_SIZE['font_main_dy']

        filt = self.filt
        xy = filt.upd_size()
        box_scroll_bg = filt.box_scroll_bg

        self.upd_clip_text_and_match_button(blf_text)
        self.upd_scissor_text_box(scissor_win)

        if xy != None and filt.blfs:
            e0 = filt.blfs[0]
            filt.r_pan_override()(xy[0] - old_L - e0.x + box_area.L, xy[1] - old_T - e0.y + box_area.T)

        # >>>
        self.filt.filter_text(input_text)
        #|

    def upd_size(self, LL, RR, BB, TT):
        # /* 0area_AreaFilterY_upd_size
        box_area = self.box_area
        old_L = box_area.L
        old_T = box_area.T
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]
        scissor_win = self.w.scissor

        LL += d0
        RR -= d0
        TT -= d0
        BB += d0

        box_text = self.box_text
        blf_text = self.blf_text

        if self.is_flip_y:
            T = BB + D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, BB, T, widget_rim)
            T += d1
            self.box_filter.LRBT_upd(LL, RR, T, TT, widget_rim)
        else:
            B = TT - D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, B, TT, widget_rim)
            B -= d1
            self.box_filter.LRBT_upd(LL, RR, BB, B, widget_rim)

        if hasattr(self, "r_parent_scissor"):
            self.upd_scissor_filt()
        else:
            self.upd_scissor_filt(scissor_win)

        L, R, B, T = box_text.inner
        L0 = box_text.L + widget_rim * 3
        L1 = L0 + SIZE_widget[0]

        self.box_icon_search.LRBT_upd(L0, L1, B, T)
        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L1 + D_SIZE['font_main_dx']
        blf_text.y = B + D_SIZE['font_main_dy']

        filt = self.filt
        xy = filt.upd_size()
        box_scroll_bg = filt.box_scroll_bg

        self.upd_clip_text_and_match_button(blf_text)
        self.upd_scissor_text_box(scissor_win)

        if xy != None and filt.blfs:
            e0 = filt.blfs[0]
            filt.r_pan_override()(xy[0] - old_L - e0.x + box_area.L, xy[1] - old_T - e0.y + box_area.T)

        # */
        #|
    def upd_scissor_text_box(self, scissor_win):
        self.scissor_text_box.intersect_with(scissor_win, self.box_icon_search.R + D_SIZE['font_main_dy'],
            self.box_match_case.L - D_SIZE['font_main_dy'], self.box_text.B, self.box_text.T)
        #|
    def upd_scissor_filt(self, scissor_win):
        e = self.box_filter.inner
        self.scissor_filt.intersect_with(scissor_win,
            e[0], e[1] - min(SIZE_widget[2], SIZE_widget[0]), e[2], e[3])
        #|

    def r_focus_element_match_button(self):
        if self.box_text.inbox(MOUSE):
            return self.r_box_match_index()
        self.box_match_hover.LRBT_upd(0, 0, 0, 0)
        return None
        #|
    def r_box_match_index(self): # ret 0/1/2 and update hover
        hover = self.box_match_hover
        B = self.box_match_case.B
        T = self.box_match_case.T

        if MOUSE[0] >= self.box_match_whole_word.R:
            R = self.box_text.R - SIZE_border[3]
            L = self.box_match_whole_word.R
            ind = 2
        elif MOUSE[0] >= self.box_match_whole_word.L:
            R = self.box_match_whole_word.R
            L = self.box_match_whole_word.L
            ind = 1
        else:
            R = self.box_match_case.R
            L = self.box_match_case.L
            ind = 0

        if hover.L == L and hover.R == R and hover.B == B and hover.T == T: pass
        else:
            hover.LRBT_upd(L, R, B, T)
            Admin.REDRAW()
        return ind
        #|

    def upd_clip_text_and_match_button(self, blf_text):
        if blf_text.unclip_text:
            self.get_box_match()
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_main'}$)
            blfSize(FONT0, D_SIZE['font_main'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            blf_text.text = r_blf_clipping_end(
                blf_text.unclip_text, blf_text.x, self.box_match_case.L - D_SIZE['font_main_dx'])
        else:
            R = self.box_text.R - SIZE_border[3]

            self.box_match_end.LRBT_upd(R, R, R, R)
            self.box_match_end_bg.LRBT_upd(R, R, R, R)

            self.box_match_whole_word.LRBT_upd(R, R, R, R)
            self.box_match_whole_word_bg.LRBT_upd(R, R, R, R)

            self.box_match_case.LRBT_upd(R, R, R, R)
            self.box_match_case_bg.LRBT_upd(R, R, R, R)
        #|
    def get_box_match(self):
        filt = self.filt
        h = SIZE_widget[0]

        L, R, B, T = self.box_text.inner
        L = R - h

        e = self.box_match_end_bg

        if filt.match_end == 1:
            if isinstance(self.box_match_end, GpuImg_filter_match_end_right):
                self.box_match_end.__class__ = GpuImg_filter_match_end_left
            e.LRBT_upd(L, R, B, T)
        elif filt.match_end == 2:
            if isinstance(self.box_match_end, GpuImg_filter_match_end_left):
                self.box_match_end.__class__ = GpuImg_filter_match_end_right
            e.LRBT_upd(L, R, B, T)
        else:
            if isinstance(self.box_match_end, GpuImg_filter_match_end_right):
                self.box_match_end.__class__ = GpuImg_filter_match_end_left
            e.LRBT_upd(0, 0, 0, 0)
        self.box_match_end.LRBT_upd(L, R, B, T)

        e = self.box_match_whole_word_bg
        R -= h
        L -= h

        self.box_match_whole_word.LRBT_upd(L, R, B, T)
        if filt.match_whole_word:
            e.LRBT_upd(L, R, B, T)
        else:
            e.LRBT_upd(0, 0, 0, 0)

        e = self.box_match_case_bg
        R -= h
        L -= h

        self.box_match_case.LRBT_upd(L, R, B, T)
        if filt.match_case:
            e.LRBT_upd(L, R, B, T)
        else:
            e.LRBT_upd(0, 0, 0, 0)

        if hasattr(self, "r_parent_scissor"):
            self.upd_scissor_text_box()
        else:
            self.upd_scissor_text_box(self.w.scissor)
        #|

    def in_box_match_button(self, mou):
        return self.box_match_case.L <= mou[0] < self.box_text.R and self.box_text.in_BT(mou)
        #|
    def in_box_search(self, mou):
        return mou[0] < self.box_icon_search.R and self.box_text.inbox(mou)
        #|
    def in_box_text_button(self, mou):
        if self.box_text.inbox(mou):
            if self.blf_text.unclip_text:
                if mou[0] >= self.box_match_case.L: return False
                if self.in_box_search(mou): return False
            return True
        return False
        #|
    def in_box_scroll(self, mou):
        if self.filt.box_scroll_bg.in_BT(mou) and self.filt.box_scroll_bg.L <= mou[0] < self.box_area.R:
            return True
        return False
        #|
    def in_box_filt(self, mou):
        if self.box_text.inbox(mou) or self.filt.box_scroll_bg.inbox(mou): return False
        return self.box_area.inbox(mou)
        #|

    def outside_evt(self):

        Admin.REDRAW()
        self.filt.box_hover.LRBT_upd(0, 0, 0, 0)
        self.box_match_hover.LRBT_upd(0, 0, 0, 0)
        self.box_text.color = COL_box_text
        #|
    def outside_evt_filt(self):
        self.filt.box_hover.LRBT_upd(0, 0, 0, 0)
        #|
    def inside_evt_filt(self): pass
    def selection_timer_end(self):
        Admin.REDRAW()
        self.box_selection.color = COL_box_text_selection
        #|

    def modal(self):

        if hasattr(self, "r_parent_scissor"):
            self.upd_scissor_filt()
        else:
            self.upd_scissor_filt(self.w.scissor)
        self.filt.r_upd_scroll()()
        Admin.REDRAW()

        if self.box_text.inbox(MOUSE):
            if self.blf_text.unclip_text:
                if MOUSE[0] >= self.box_match_case.L:
                    self.to_localmodal(self,
                        self.in_box_match_button,
                        self.r_focus_element_match_button,
                        self.localmodal_match_button,
                        NF1,
                        lambda: self.box_match_hover.LRBT_upd(0, 0, 0, 0),
                        NF)
                    return

                if self.in_box_search(MOUSE):
                    box_icon_search = self.box_icon_search
                    self.box_match_hover.LRBT_upd(*box_icon_search.r_LRBT())
                    Admin.REDRAW()
                    self.to_localmodal(self,
                        self.in_box_search,
                        NT,
                        self.localmodal_search_button,
                        NF1,
                        lambda: self.box_match_hover.LRBT_upd(0, 0, 0, 0),
                        lambda: isinstance(box_icon_search, GpuImg_search))
                    return

            self.to_localmodal(self,
                self.in_box_text_button,
                NT,
                self.localmodal_text_button,
                NF1,
                lambda: setattr(self.box_text, "color", COL_box_text),
                NF)
            return

        if self.in_box_scroll(MOUSE):
            self.to_localmodal(self,
                self.in_box_scroll,
                NT,
                self.localmodal_scroll_button,
                NF1,
                N,
                NF)
            return

        self.inside_evt_filt()

        self.to_localmodal(self,
            self.in_box_filt,
            NT,
            self.localmodal_filt,
            NF1,
            self.outside_evt_filt,
            NF)
        #|

    def dxy(self, dx, dy):
        for e in self.boxes: e.dxy_upd(dx, dy)

        self.blf_text.x += dx
        self.blf_text.y += dy

        self.filt.dxy(dx, dy)

        scissor_win = self.w.scissor
        self.upd_scissor_filt(scissor_win)
        self.upd_scissor_text_box(scissor_win)
        #|

    def upd_filter_hover(self):
        # /* 0area_AreaFilterY_upd_filter_hover
        filt = self.filt
        hover = filt.box_hover
        blfs = filt.blfs
        if blfs:
            T = blfs[filt.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
            i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + filt.headkey

            if filt.headkey <= i <= filt.endkey:
                T += (filt.headkey - i) * D_SIZE['widget_full_h']
                B = T - D_SIZE['widget_full_h']
                if hover.T == T and hover.B == B: pass
                else:
                    hover.LRBT_upd(self.scissor_filt.x, filt.box_scroll_bg.L, B, T)
                    Admin.REDRAW()
                if self.filt_region_event(B, T, i, filt) == True: return True
            else:
                if hover.L == 0 and hover.R == 0: pass
                else:
                    hover.LRBT_upd(0, 0, 0, 0)
                    Admin.REDRAW()
                if self.filt_region_event(0, 0, None, filt) == True: return True
            return i
        return None
        # */

    def localmodal_match_button(self, dic):
        if TRIGGER['click']():
            ind = dic["focus_element"]
            tx = self.blf_text.unclip_text
            if ind == 0: self.evt_toggle_match_case(tx)
            elif ind == 1: self.evt_toggle_match_whole_word(tx)
            else: self.evt_toggle_match_end(tx)
            return True
        return True
        #|
    def localmodal_search_button(self, dic):
        if TRIGGER['dd_del_all']() or TRIGGER['click'](): self.evt_area_del_text()
        return True
        #|
    def localmodal_text_button(self, dic):
        if TRIGGER['rm']():
            dic["w_head"].fin()
            self.to_modal_rm()
            return True

        if TRIGGER['dd_cut']():
            self.evt_area_cut()
            return True
        if TRIGGER['dd_paste']():
            self.evt_area_paste()
            return True
        if TRIGGER['dd_copy']():
            self.evt_area_copy()
            return True
        if TRIGGER['dd_del_all']():
            self.evt_area_del_text()
            return True

        if TRIGGER['click']():
            dic["w_head"].fin()
            self.to_modal_dd()
            return True
        return True
        #|
    def localmodal_scroll_button(self, dic):
        # /* 0area_AreaFilterY_i_modal_scroll
        # <<< 1copy (0area_AreaFilterY_filter_evt,, $$)
        if TRIGGER['dd_scroll_left_most']():
            self.filt.evt_scrollX(self.filt.r_blfs_width())
            return True
        if TRIGGER['dd_scroll_right_most']():
            self.filt.evt_scrollX(-self.filt.r_blfs_width())
            return True
        if TRIGGER['dd_scroll_down_most']():
            self.filt.evt_scrollY(len(self.filt.items) * D_SIZE['widget_full_h'])
            return True
        if TRIGGER['dd_scroll_up_most']():
            self.filt.evt_scrollY(-len(self.filt.items) * D_SIZE['widget_full_h'])
            return True
        if TRIGGER['dd_scroll_left']():
            self.filt.evt_scrollX(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_right']():
            self.filt.evt_scrollX(-P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_down']():
            self.filt.evt_scrollY(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_up']():
            self.filt.evt_scrollY(-P.scroll_distance)
            return True
        if TRIGGER['dd_beam_down']():
            self.evt_beam_down()
            return True
        if TRIGGER['dd_beam_up']():
            self.evt_beam_up()
            return True
        # >>>

        if TRIGGER['dd_scroll_left_area']():
            self.filt.evt_scrollX(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_right_area']():
            self.filt.evt_scrollX(-P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_down_area']():
            self.filt.evt_scrollY(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_up_area']():
            self.filt.evt_scrollY(-P.scroll_distance)
            return True
        if TRIGGER['dd_scroll']():
            self.to_modal_scrollbar()
            return True
        if TRIGGER['pan']():
            self.filt.to_modal_pan()
            return True
        # */
        return True
        #|
    def localmodal_filt(self, dic):
        i = self.upd_filter_hover()

        if hasattr(self, "localmodal_filt_submodal"):
            if self.localmodal_filt_submodal(): return True

        # /* 0area_AreaFilterY_filter_evt
        if TRIGGER['dd_scroll_left_most']():
            self.filt.evt_scrollX(self.filt.r_blfs_width())
            return True
        if TRIGGER['dd_scroll_right_most']():
            self.filt.evt_scrollX(-self.filt.r_blfs_width())
            return True
        if TRIGGER['dd_scroll_down_most']():
            self.filt.evt_scrollY(len(self.filt.items) * D_SIZE['widget_full_h'])
            return True
        if TRIGGER['dd_scroll_up_most']():
            self.filt.evt_scrollY(-len(self.filt.items) * D_SIZE['widget_full_h'])
            return True
        if TRIGGER['dd_scroll_left']():
            self.filt.evt_scrollX(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_right']():
            self.filt.evt_scrollX(-P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_down']():
            self.filt.evt_scrollY(P.scroll_distance)
            return True
        if TRIGGER['dd_scroll_up']():
            self.filt.evt_scrollY(-P.scroll_distance)
            return True
        if TRIGGER['dd_beam_down']():
            self.evt_beam_down()
            return True
        if TRIGGER['dd_beam_up']():
            self.evt_beam_up()
            return True
        # */
        if TRIGGER['area_save_as_shapekey']():
            if hasattr(self, "evt_save_as_shapekey"):
                self.evt_save_as_shapekey()
            return True
        if TRIGGER['area_apply_as_shapekey']():
            if hasattr(self, "evt_apply_as_shapekey"):
                self.evt_apply_as_shapekey()
            return True
        if TRIGGER['area_apply']():
            self.evt_apply()
            return True
        if TRIGGER['area_del']():
            self.evt_del()
            return True
        if TRIGGER['area_add']():
            self.evt_add()
            return True
        if TRIGGER['area_active_down_most_shift']():
            self.evt_active_down_most_shift()
            return True
        if TRIGGER['area_active_up_most_shift']():
            self.evt_active_up_most_shift()
            return True
        if TRIGGER['area_active_down_shift']():
            self.evt_active_down_shift()
            return True
        if TRIGGER['area_active_up_shift']():
            self.evt_active_up_shift()
            return True
        if TRIGGER['area_active_down_most']():
            self.evt_active_down_most()
            return True
        if TRIGGER['area_active_up_most']():
            self.evt_active_up_most()
            return True
        if TRIGGER['area_active_down']():
            self.evt_active_down()
            return True
        if TRIGGER['area_active_up']():
            self.evt_active_up()
            return True

        if TRIGGER['pan']():
            self.filt.to_modal_pan()
            return True
        if hasattr(self, "to_modal_filt_selectbox"):
            if TRIGGER['area_selectbox_subtract']():
                self.to_modal_filt_selectbox(select_operation="subtract")
                return True
            if TRIGGER['area_selectbox_extend']():
                self.to_modal_filt_selectbox(select_operation="extend")
                return True
            if TRIGGER['area_selectbox_new']():
                self.to_modal_filt_selectbox(select_operation="")
                return True
            if TRIGGER['area_select_extend']():
                if self.filt.blfs:
                    self.evt_area_select(i, extend=True)
                    return True
        if TRIGGER['area_select']():
            if self.filt.blfs:
                self.evt_area_select(i, extend=False)
                return True
        return True
        #|

    def filt_region_event(self, B, T, i, filt): return None

    def to_modal_scrollbar(self): self.filt.to_modal_scrollbar()

    def to_modal_rm(self):


        DropDownRMKeymap(self, MOUSE, [
            ("dd_cut", self.evt_area_cut),
            ("dd_paste", self.evt_area_paste),
            ("dd_copy", self.evt_area_copy),
            ("dd_del_all", self.evt_area_del_text),
        ])
        #|
    def to_modal_dd_rm(self):

        self.kill_push_timer()

        DropDownRMKeymap(self, MOUSE, [
            # <<< 1ifmatchindex (0area_AreaFilterY_text_evt, 12,
            # $lambda ls, r: (f'("{ls[r][ls[r].find("[") + 2 : ls[r].find("]") - 1
            #     ]}", self.{ls[r+1][ls[r+1].find("self.") + 5 : ls[r+1].find("()")]}),\n', True)$,
            # $$,
            # ${'TRIGGER'}$)
            ("redo", self.evt_redo),
            ("undo", self.evt_undo),
            ("dd_match_end", self.evt_toggle_match_end),
            ("dd_match_case", self.evt_toggle_match_case),
            ("dd_match_whole_word", self.evt_toggle_match_whole_word),
            ("dd_select_all", self.evt_select_all),
            ("dd_select_word", self.evt_select_word),
            ("dd_cut", self.evt_cut),
            ("dd_paste", self.evt_paste),
            ("dd_copy", self.evt_copy),
            ("dd_del_all", self.evt_del_all),
            ("dd_del", self.evt_del_line),
            ("dd_del_word", self.evt_del_word),
            ("dd_del_chr", self.evt_del_chr),
            ("dd_beam_line_begin_shift", self.evt_beam_line_begin_shift),
            ("dd_beam_line_end_shift", self.evt_beam_line_end_shift),
            ("dd_beam_left_word_shift", self.evt_beam_left_word_shift),
            ("dd_beam_right_word_shift", self.evt_beam_right_word_shift),
            ("dd_beam_left_shift", self.evt_beam_left_shift),
            ("dd_beam_right_shift", self.evt_beam_right_shift),
            ("dd_beam_down_shift", self.evt_beam_down_shift),
            ("dd_beam_up_shift", self.evt_beam_up_shift),
            ("dd_beam_line_begin", self.evt_beam_line_begin),
            ("dd_beam_line_end", self.evt_beam_line_end),
            ("dd_beam_left_word", self.evt_beam_left_word),
            ("dd_beam_right_word", self.evt_beam_right_word),
            ("dd_beam_left", self.evt_beam_left),
            ("dd_beam_right", self.evt_beam_right),
            ("dd_beam_down", self.evt_beam_down),
            ("dd_beam_up", self.evt_beam_up),
            ("dd_beam_end_shift", self.evt_beam_end_shift),
            ("dd_beam_start_shift", self.evt_beam_start_shift),
            ("dd_beam_end", self.evt_beam_end),
            ("dd_beam_start", self.evt_beam_start),
            ("pan", self.to_modal_pan_text),
            ("dd_selection_shift", self.to_modal_selection_shift),
            ("dd_selection", self.to_modal_selection),
            ("dd_linebreak", self.evt_linebreak),
            ("dd_untab", self.evt_untab),
            ("dd_tab", self.evt_tab),
            # >>>
        ])
        #|
    def to_modal_dd_rm_filt(self):

        kill_evt_except()
        filt = self.filt

        if not hasattr(filt, "rm_items"): return
        if not filt.rm_items: return

        DropDownRMKeymap(self, MOUSE, filt.rm_items)
        if hasattr(self.w, "data"):
            self.w.data["init_index"] = filt.r_mouse_index_safe()
        #|
    def fin_callfront_set_parent(self):
        global SELF
        SELF = self
        # <<< 1copy (timer_reg_first_safe,, ${'_timer_':'timer_beam', '_start_':'P_cursor_beam_time'}$)
        if not timer_isreg(timer_beam): timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        # >>>
        #|

    def to_modal_dd(self, select_all=None):

        #|
        global SELF, P_cursor_beam_time
        _REDRAW = Admin.REDRAW
        _REDRAW()
        blf_text = self.blf_text
        box_text = self.box_text
        box_text.color = COL_box_text_active
        hover = self.box_match_hover
        filt = self.filt
        filt_box_hover = filt.box_hover
        filt_box_hover_LRBT_upd = filt_box_hover.LRBT_upd
        wind = self.wind  if hasattr(self, "wind") else self.w

        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _TRIGGER_dd_esc = TRIGGER['dd_esc']
        _TRIGGER_dd_confirm = TRIGGER['dd_confirm']
        _TRIGGER_click = TRIGGER['click']
        _TRIGGER_rm = TRIGGER['rm']
        _TRIGGER_pan = TRIGGER['pan']
        _is_dropdown = self.is_dropdown
        _box_win = wind.box_win
        _box_win_inbox = _box_win.inbox
        _box_text_inbox = box_text.inbox
        _box_match_case = self.box_match_case
        _r_box_match_index = self.r_box_match_index
        _text_evt = self.text_evt
        _upd_filter_hover = self.upd_filter_hover

        dd_basis_evt = getattr(wind, "dd_basis_evt", None)
        i_modal_dd_filt_submodal = self.i_modal_dd_filt_submodal  if hasattr(self, "i_modal_dd_filt_submodal") else None

        def modal_dd():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or _TRIGGER_dd_esc():
                _temp[0] = w_head.data
                w_head.fin()
                return

            is_inside_area = self.box_area.inbox(MOUSE)
            if is_inside_area is False:
                Admin.TAG_CURSOR = 'DEFAULT'

                if filt_box_hover.L != filt_box_hover.R:
                    filt_box_hover_LRBT_upd(0, 0, 0, 0)
                    _REDRAW()

            if dd_basis_evt is None: pass
            else:
                basis_evt_fn = dd_basis_evt()
                if basis_evt_fn != None:
                    basis_evt_fn()
                    return

            if _TRIGGER_dd_confirm():
                _temp[0] = None
                w_head.fin()
                return

            if _is_dropdown:
                if _box_win_inbox(MOUSE) and MOUSE[1] > _box_win.title_B:
                    if TRIGGER['title_move']():
                        wind.to_modal_move()
                        return


            if _box_text_inbox(MOUSE):
                if filt_box_hover.L != filt_box_hover.R:
                    filt_box_hover_LRBT_upd(0, 0, 0, 0)
                    _REDRAW()

                if MOUSE[0] >= _box_match_case.L:
                    Admin.TAG_CURSOR = 'DEFAULT'

                    ind = _r_box_match_index()
                    if _TRIGGER_click():
                        if ind == 0:
                            self.evt_toggle_match_case()
                        elif ind == 1:
                            self.evt_toggle_match_whole_word()
                        else:
                            self.evt_toggle_match_end()
                        return
                else:
                    Admin.TAG_CURSOR = 'TEXT'
                    if hover.L != hover.R:
                        hover.LRBT_upd(0, 0, 0, 0)
                        _REDRAW()

                    if _TRIGGER_rm():
                        self.to_modal_dd_rm()
                        return
            else:
                Admin.TAG_CURSOR = 'DEFAULT'
                if hover.L != hover.R:
                    hover.LRBT_upd(0, 0, 0, 0)
                    _REDRAW()

            if self.box_filter.inbox(MOUSE):
                if filt.box_scroll_bg.inbox(MOUSE):
                    if filt_box_hover.L != filt_box_hover.R:
                        filt_box_hover_LRBT_upd(0, 0, 0, 0)
                        _REDRAW()

                    # <<< 1copy (0area_AreaFilterY_i_modal_scroll,, $$)
                    # <<< 1copy (0area_AreaFilterY_filter_evt,, $$)
                    if TRIGGER['dd_scroll_left_most']():
                        self.filt.evt_scrollX(self.filt.r_blfs_width())
                        return True
                    if TRIGGER['dd_scroll_right_most']():
                        self.filt.evt_scrollX(-self.filt.r_blfs_width())
                        return True
                    if TRIGGER['dd_scroll_down_most']():
                        self.filt.evt_scrollY(len(self.filt.items) * D_SIZE['widget_full_h'])
                        return True
                    if TRIGGER['dd_scroll_up_most']():
                        self.filt.evt_scrollY(-len(self.filt.items) * D_SIZE['widget_full_h'])
                        return True
                    if TRIGGER['dd_scroll_left']():
                        self.filt.evt_scrollX(P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_right']():
                        self.filt.evt_scrollX(-P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_down']():
                        self.filt.evt_scrollY(P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_up']():
                        self.filt.evt_scrollY(-P.scroll_distance)
                        return True
                    if TRIGGER['dd_beam_down']():
                        self.evt_beam_down()
                        return True
                    if TRIGGER['dd_beam_up']():
                        self.evt_beam_up()
                        return True
                    # >>>

                    if TRIGGER['dd_scroll_left_area']():
                        self.filt.evt_scrollX(P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_right_area']():
                        self.filt.evt_scrollX(-P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_down_area']():
                        self.filt.evt_scrollY(P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_up_area']():
                        self.filt.evt_scrollY(-P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll']():
                        self.to_modal_scrollbar()
                        return True
                    if TRIGGER['pan']():
                        self.filt.to_modal_pan()
                        return True
                    # >>>
                else:
                    i = _upd_filter_hover()

                    if i_modal_dd_filt_submodal is None: pass
                    else:
                        if i_modal_dd_filt_submodal(i): return

                    if _TRIGGER_rm():
                        self.to_modal_dd_rm_filt()
                        return True
                    # <<< 1copy (0area_AreaFilterY_filter_evt,, $$)
                    if TRIGGER['dd_scroll_left_most']():
                        self.filt.evt_scrollX(self.filt.r_blfs_width())
                        return True
                    if TRIGGER['dd_scroll_right_most']():
                        self.filt.evt_scrollX(-self.filt.r_blfs_width())
                        return True
                    if TRIGGER['dd_scroll_down_most']():
                        self.filt.evt_scrollY(len(self.filt.items) * D_SIZE['widget_full_h'])
                        return True
                    if TRIGGER['dd_scroll_up_most']():
                        self.filt.evt_scrollY(-len(self.filt.items) * D_SIZE['widget_full_h'])
                        return True
                    if TRIGGER['dd_scroll_left']():
                        self.filt.evt_scrollX(P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_right']():
                        self.filt.evt_scrollX(-P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_down']():
                        self.filt.evt_scrollY(P.scroll_distance)
                        return True
                    if TRIGGER['dd_scroll_up']():
                        self.filt.evt_scrollY(-P.scroll_distance)
                        return True
                    if TRIGGER['dd_beam_down']():
                        self.evt_beam_down()
                        return True
                    if TRIGGER['dd_beam_up']():
                        self.evt_beam_up()
                        return True
                    # >>>

                    if _TRIGGER_pan():
                        filt.to_modal_pan()
                        return
                    if _TRIGGER_click():
                        if i is None: pass
                        elif 0 <= i < len(filt.match_items):
                            if i != filt.active_index: filt.set_active_index(i)
                            blf_text.color = COL_box_text_fg_ignore
                            _temp[0] = None
                            w_head.fin()
                            return

            if is_inside_area is False:
                if TRIGGER['dd_confirm_area']():
                    _temp[0] = None
                    w_head.fin()
                    return

            if TRIGGER['area_active_down_most']():
                self.evt_active_down_most()
                return
            if TRIGGER['area_active_up_most']():
                self.evt_active_up_most()
                return
            if TRIGGER['area_active_down']():
                self.evt_active_down()
                return
            if TRIGGER['area_active_up']():
                self.evt_active_up()
                return

            _text_evt()
            #|

        w_head = Head(self, modal_dd, self.end_modal_dd)
        w_head.data = {
            'text': blf_text.unclip_text,
            'active_index': filt.active_index}

        P_cursor_beam_time = P.cursor_beam_time
        # <<< 1copy (0area_to_modal_dd_callfrom_dd_check,, $$)
        if timer_isreg(timer_beam):

            self.dd_parent = SELF
            if hasattr(SELF, "kill_push_timer"): SELF.kill_push_timer()
        else:
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
            self.dd_parent = None
        # >>>
        SELF = self
        Admin.TAG_CURSOR = 'TEXT'  if _box_text_inbox(MOUSE) else 'DEFAULT'

        box_icon_search = self.box_icon_search
        if isinstance(box_icon_search, GpuImg_delete):
            box_icon_search.__class__ = GpuImg_search
            box_icon_search.upd()

        blf_text.text = blf_text.unclip_text
        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + floor(blfDimen(FONT0, blf_text.text)[0])
        self.box_beam.L = L
        self.box_beam.R = L + SIZE_widget[1]
        self.box_beam.upd()
        self.get_box_match()
        filt.set_active_index(None)

        if select_all is None: select_all = P.use_select_all
        if select_all: self.evt_select_all()
        self.local_history = LocalHistory(self, P.undo_steps_local, self.r_push_item)
        return w_head
        #|
    def end_modal_dd(self):
        # <<< 1copy (0area_SELF_to_top_level,, $$)
        if self.dd_parent == None:
            if timer_isreg(timer_beam):
                timer_unreg(timer_beam)

            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

        else:
            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

            self.dd_parent.fin_callfront_set_parent()
        # >>>

        Admin.TAG_CURSOR = 'DEFAULT'
        Admin.REDRAW()
        kill_evt_except()

        blf_text = self.blf_text
        filt = self.filt
        selected_item = None
        best_item = None

        if _temp[0] == None:
            if blf_text.color is COL_box_text_fg:
                use_text_output = True
                if filt.match_items: best_item = filt.match_items[0]
            else:
                use_text_output = False
                blf_text.color = COL_box_text_fg
                i = filt.active_index

                if i != None and 0 <= i < len(filt.match_items):
                    selected_item = filt.match_items[i]
                    best_item = selected_item
                    blf_text.text = selected_item.name

            filt.filter_text(blf_text.text, callback=True)
        else:

            use_text_output = None
            data = _temp[0]
            blf_text.text = data["text"]
            filt.filter_text(blf_text.text)
            filt.set_active_index(data["active_index"], callback=False)

        if blf_text.text:
            box_icon_search = self.box_icon_search
            if isinstance(box_icon_search, GpuImg_search):
                box_icon_search.__class__ = GpuImg_delete
                box_icon_search.upd()

        self.box_text.color = COL_box_text
        self.box_beam.L = self.box_beam.R = 0
        self.box_beam.upd()
        self.box_selection.L = self.box_selection.R = 0
        self.box_selection.upd()
        blf_text.unclip_text = blf_text.text
        blf_text.x = self.box_icon_search.R + D_SIZE['font_main_dx']
        self.upd_clip_text_and_match_button(blf_text)
        filt.box_hover.LRBT_upd(0, 0, 0, 0)
        if hasattr(self, "box_match_hover"):
            self.box_match_hover.LRBT_upd(0, 0, 0, 0)

        self.local_history.kill()

        if hasattr(self.w, 'callback_end_modal_dd'):
            self.w.callback_end_modal_dd({
                'use_text_output': use_text_output,
                'selected_item': selected_item,
                'best_item': best_item
            })

        self.upd_data()
        #|

    def to_modal_selection(self, shift=False):

        #|
        _blfSize = blfSize
        _FONT0 = FONT0
        _font_main = D_SIZE['font_main']
        _blfSize(_FONT0, _font_main)
        _blf_text = self.blf_text
        _beam_index = self.beam_index
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _r_blf_ind = r_blf_ind
        _set_highlight = self.set_highlight
        _check_cursor_pos = self.check_cursor_pos

        if shift is False:
            end_trigger = r_end_trigger('dd_selection')
            self.evt_beam_move_x(_r_blf_ind(_blf_text.text, _blf_text.x, MOUSE[0]) - _beam_index[1], evtkill=False)
        else:
            end_trigger = r_end_trigger('dd_selection_shift')
            self.evt_beam_shift_x(_r_blf_ind(_blf_text.text, _blf_text.x, MOUSE[0]) - _beam_index[1], evtkill=False)

        def modal_selection():
            _REDRAW()

            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            _blfSize(_FONT0, _font_main)
            _set_highlight(_beam_index[0], _r_blf_ind(_blf_text.text, _blf_text.x, MOUSE[0]))
            _check_cursor_pos()
            #|

        w_head = Head(self, modal_selection)
        _REDRAW()
        #|
    def to_modal_selection_shift(self):

        self.to_modal_selection(shift=True)
        #|

    def to_modal_pan_text(self):

        blf_text = self.blf_text
        if blf_text.text: pass
        else: return

        blfSize(FONT0, D_SIZE['font_main'])
        _lim_L = self.r_text_limL()
        _lim_R = self.r_text_limR(_lim_L, SIZE_widget[1])

        end_trigger = r_end_trigger('pan')
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop()
        _TRIGGER_esc = TRIGGER['esc']
        _EVT_TYPE = EVT_TYPE
        _REDRAW = Admin.REDRAW
        _box_beam_dx_upd = self.box_beam.dx_upd
        _box_selection_dx_upd = self.box_selection.dx_upd

        def end_modal_pan_text():
            mouseloop_end()
            kill_evt_except()

        def modal_pan_text():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dx, dy = r_dxy_mouse()

            # /* 0area_AreaFilterY_pan_text
            new_x = blf_text.x + dx
            if new_x < _lim_R:
                dx += _lim_R - new_x

            if new_x > _lim_L:
                dx += _lim_L - new_x

            blf_text.x += dx
            _box_beam_dx_upd(dx)
            _box_selection_dx_upd(dx)
            # */
            mouseloop()

        w_head = Head(self, modal_pan_text, end_modal_pan_text)
        _REDRAW()
        #|
    def r_pan_text_override(self):
        blf_text = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        _lim_L = self.r_text_limL()
        _lim_R = self.r_text_limR(_lim_L, SIZE_widget[1])

        _box_beam_dx_upd = self.box_beam.dx_upd
        _box_selection_dx_upd = self.box_selection.dx_upd

        def pan_text_override(dx):
            # <<< 1copy (0area_AreaFilterY_pan_text,, $$)
            new_x = blf_text.x + dx
            if new_x < _lim_R:
                dx += _lim_R - new_x

            if new_x > _lim_L:
                dx += _lim_L - new_x

            blf_text.x += dx
            _box_beam_dx_upd(dx)
            _box_selection_dx_upd(dx)
            # >>>
            return dx
        return pan_text_override
        #|
    def resize_upd_end(self, override=None):

        filt = self.filt

        if filt.blfs:
            restore_canvas = True
            icon_head = filt.icons[filt.headkey]
            L0 = self.box_filter.inner[0] + SIZE_filter[1] + SIZE_border[3]
            T0 = self.box_filter.inner[3] - SIZE_filter[2] - SIZE_border[3] - D_SIZE['font_main_dT'] - D_SIZE['font_main_dy'] + SIZE_widget[0]
            dx0 = icon_head.L - L0
            dy0 = icon_head.T - T0 + filt.headkey * D_SIZE['widget_full_h']
        else:
            restore_canvas = False

        if override is None:
            if hasattr(self.w, "areas") and P.adaptive_win_resize and hasattr(self, "r_size_default") and hasattr(self.w, "r_area_posRB_adaptive"):
                posR, posB = self.w.r_area_posRB_adaptive(self)

                if posR == self.box_area.R and posB == self.box_area.B: pass
                else:
                    e = self.box_area
                    sizeXmin, sizeYmin = self.r_size_default()

                    if posR != e.R:
                        posR = max(posR, e.L + sizeXmin)
                    if posB != e.B:
                        posB = min(posB, e.T - sizeYmin)

                    self.upd_size(
                        e.L,
                        posR,
                        posB,
                        e.T)
            else:
                e = self.box_area
                self.upd_size(
                    e.L,
                    e.R,
                    e.B,
                    e.T)
        else:
            self.upd_size(*override)

        if restore_canvas is True:
            pan_override = filt.r_pan_override()
            pan_override(16777215, -16777215)
            pan_override(dx0, dy0)
        #|

    def text_evt(self):
        # /* 0area_AreaFilterY_text_evt
        if TRIGGER['redo']():
            self.evt_redo()
            return True
        if TRIGGER['undo']():
            self.evt_undo()
            return True
        if TRIGGER['dd_match_end']():
            self.evt_toggle_match_end()
            return True
        if TRIGGER['dd_match_case']():
            self.evt_toggle_match_case()
            return True
        if TRIGGER['dd_match_whole_word']():
            self.evt_toggle_match_whole_word()
            return True
        if TRIGGER['dd_select_all']():
            self.evt_select_all()
            return True
        if TRIGGER['dd_select_word']():
            self.evt_select_word()
            return True
        if TRIGGER['dd_cut']():
            self.evt_cut()
            return True
        if TRIGGER['dd_paste']():
            self.evt_paste()
            return True
        if TRIGGER['dd_copy']():
            self.evt_copy()
            return True
        if TRIGGER['dd_del_all']():
            self.evt_del_all()
            return True
        if TRIGGER['dd_del']():
            self.evt_del_line()
            return True
        if TRIGGER['dd_del_word']():
            self.evt_del_word()
            return True
        if TRIGGER['dd_del_chr']():
            self.evt_del_chr()
            return True
        if TRIGGER['dd_beam_line_begin_shift']():
            self.evt_beam_line_begin_shift()
            return True
        if TRIGGER['dd_beam_line_end_shift']():
            self.evt_beam_line_end_shift()
            return True
        if TRIGGER['dd_beam_left_word_shift']():
            self.evt_beam_left_word_shift()
            return True
        if TRIGGER['dd_beam_right_word_shift']():
            self.evt_beam_right_word_shift()
            return True
        if TRIGGER['dd_beam_left_shift']():
            self.evt_beam_left_shift()
            return True
        if TRIGGER['dd_beam_right_shift']():
            self.evt_beam_right_shift()
            return True
        if TRIGGER['dd_beam_down_shift']():
            self.evt_beam_down_shift()
            return True
        if TRIGGER['dd_beam_up_shift']():
            self.evt_beam_up_shift()
            return True
        if TRIGGER['dd_beam_line_begin']():
            self.evt_beam_line_begin()
            return True
        if TRIGGER['dd_beam_line_end']():
            self.evt_beam_line_end()
            return True
        if TRIGGER['dd_beam_left_word']():
            self.evt_beam_left_word()
            return True
        if TRIGGER['dd_beam_right_word']():
            self.evt_beam_right_word()
            return True
        if TRIGGER['dd_beam_left']():
            self.evt_beam_left()
            return True
        if TRIGGER['dd_beam_right']():
            self.evt_beam_right()
            return True
        if TRIGGER['dd_beam_down']():
            self.evt_beam_down()
            return True
        if TRIGGER['dd_beam_up']():
            self.evt_beam_up()
            return True
        if TRIGGER['dd_beam_end_shift']():
            self.evt_beam_end_shift()
            return True
        if TRIGGER['dd_beam_start_shift']():
            self.evt_beam_start_shift()
            return True
        if TRIGGER['dd_beam_end']():
            self.evt_beam_end()
            return True
        if TRIGGER['dd_beam_start']():
            self.evt_beam_start()
            return True
        if TRIGGER['pan']():
            self.to_modal_pan_text()
            return True
        if TRIGGER['dd_selection_shift']():
            self.to_modal_selection_shift()
            return True
        if TRIGGER['dd_selection']():
            self.to_modal_selection()
            return True
        if TRIGGER['dd_linebreak']():
            self.evt_linebreak()
            return True
        if TRIGGER['dd_untab']():
            self.evt_untab()
            return True
        if TRIGGER['dd_tab']():
            self.evt_tab()
            return True
        # */

        if EVT_TYPE[1] == 'PRESS':
            Admin.REDRAW()
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
            self.box_beam.color = COL_box_cursor_beam

            tx = Admin.EVT.unicode
            if tx:
                self.beam_input(tx)
                return True
        return False
        #|

    def evt_cancel(self):

        w_head = self.w.child_head
        _temp[0] = w_head.data
        w_head.fin()
        #|

    def evt_redo(self):

        kill_evt_except()
        his = self.local_history
        if timer_isreg(timer_undo_push):
            timer_unreg(timer_undo_push)
            his.push()
            report('Currently in last step')
            return

        if his.index + 1 >= len(his.array):
            report('Currently in last step')
            return

        his.index += 1
        self.to_history_index(his.index)
        #|
    def evt_undo(self):

        kill_evt_except()
        his = self.local_history
        if timer_isreg(timer_undo_push):
            timer_unreg(timer_undo_push)
            his.push()

        if his.index == 0:
            report('Currently in first step')
            return

        his.index -= 1
        self.to_history_index(his.index)
        #|
    def evt_select_all(self, override=None):

        #|
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)

        # /* 0defarea_AreaFilterY_evt_select_all
        Admin.REDRAW()
        i0, i1 = self.beam_index
        if override == None:
            ibeam = i1
            if i0 > i1: i0, i1 = i1, i0
            if i0 == 0 and i1 == len(self.blf_text.text):
                self.set_highlight(ibeam, ibeam)
            else:
                self.set_highlight(0, len(self.blf_text.text))
        else:
            if override:
                self.set_highlight(0, len(self.blf_text.text))
            else:
                self.set_highlight(i1, i1)

        self.check_cursor_pos()
        self.upd_highlight()
        kill_evt_except()
        # */
    def evt_select_word(self):

        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)

        # /* 0defarea_AreaFilterY_evt_select_word
        Admin.REDRAW()
        s = self.blf_text.text
        if not s: return
        self.set_highlight(*r_word_select_index(s, self.beam_index[1]))

        self.check_cursor_pos()
        self.upd_highlight()
        kill_evt_except()
        # */
    def evt_cut(self):

        i0, i1 = self.beam_index
        if i0 == i1:
            bpy.context.window_manager.clipboard = self.blf_text.text
            self.evt_del_all()
        else:
            if i0 > i1:
                i0, i1 = i1, i0
            bpy.context.window_manager.clipboard = self.blf_text.text[i0 : i1]
            self.evt_del_chr()
        #|
    def evt_paste(self):

        #|
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam
        self.beam_input(bpy.context.window_manager.clipboard)
        kill_evt_except()
        #|
    def evt_copy(self):

        #|
        i0, i1 = self.beam_index
        if i0 == i1: return
        if i0 > i1:
            i0, i1 = i1, i0

        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam
        self.box_selection.color = COL_box_text_selection_off
        # <<< 1copy (timer_reg_first_safe,, ${'_timer_':'timer_selection', '_start_':'0.1'}$)
        if not timer_isreg(timer_selection): timer_reg(timer_selection, first_interval=0.1)
        # >>>

        bpy.context.window_manager.clipboard = self.blf_text.text[i0 : i1]
        kill_evt_except()
        #|
    def evt_del_all(self, undo_push=True):

        if hasattr(self, "readonly") and self.readonly is True: return
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)

        self.blf_text.text = ""
        self.set_highlight(0, 0)
        self.check_limR()
        self.check_limL()
        self.check_cursor_pos()
        kill_evt_except()
        self.filt.filter_text(self.blf_text.text)
        if undo_push:
            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()
            timer_reg(timer_undo_push, first_interval=1.0)
        #|
    def evt_del_line(self):

        i0, i1 = self.beam_index
        self.evt_del_all()  if i0 == i1 else self.evt_del_chr()
        #|
    def evt_del_word(self):

        if hasattr(self, "readonly") and self.readonly is True: return
        i0, i1 = self.beam_index
        if i0 != i1:
            self.evt_del_chr()
            return
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        kill_evt_except()

        tx = self.blf_text
        s = tx.text[: i1]

        if not s: return
        i = r_prev_word_index(s)
        if i == i1: i -= 1
        if i < 0: i = 0

        tx.text = s[: i] + tx.text[i1 :]
        self.set_highlight(i, i)
        self.check_limR()
        self.check_limL()
        self.check_cursor_pos()
        self.filt.filter_text(self.blf_text.text)
        if timer_isreg(timer_undo_push): timer_unreg(timer_undo_push)
        timer_reg(timer_undo_push, first_interval=1.0)
        #|
    def evt_del_chr(self):

        if hasattr(self, "readonly") and self.readonly is True: return
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text

        if tx.text == "": return

        if i0 == i1:
            i0 -= 1
            if i0 < 0: i0 = 0
            tx.text = tx.text[ : i0] + tx.text[i1 : ]
            self.set_highlight(i0, i0)
        elif i0 < i1:
            tx.text = tx.text[ : i0] + tx.text[i1 : ]
            self.set_highlight(i0, i0)
        else:
            tx.text = tx.text[ : i1] + tx.text[i0 : ]
            self.set_highlight(i1, i1)
        self.check_limR()
        self.check_limL()
        self.check_cursor_pos()
        self.filt.filter_text(self.blf_text.text)
        if timer_isreg(timer_undo_push): timer_unreg(timer_undo_push)
        timer_reg(timer_undo_push, first_interval=1.0)
        #|
    def evt_beam_line_begin_shift(self): self.evt_beam_up_shift()
    def evt_beam_line_end_shift(self): self.evt_beam_down_shift()
    def evt_beam_left_word_shift(self):

        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)

        # /* 0defarea_AreaFilterY_evt_beam_left_word_shift
        Admin.REDRAW()
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text[: i1]

        if not s: return
        i = r_prev_word_index(s)
        if i == i1: i -= 1
        if i < 0: i = 0

        self.set_highlight(i0, i)
        self.check_cursor_pos()
        self.upd_highlight()
        # */
    def evt_beam_right_word_shift(self):

        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)

        # /* 0defarea_AreaFilterY_evt_beam_right_word_shift
        Admin.REDRAW()
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text

        if not s: return
        i = r_next_word_index(s, i1)
        if i == i1:
            i += 1
            if i > len(s): i = len(s)

        self.set_highlight(i0, i)
        self.check_cursor_pos()
        self.upd_highlight()
        # */
    def evt_beam_shift_x(self, dx, evtkill=True):

        #|
        if evtkill is True: kill_evt_except()
        blf_text = self.blf_text
        box_beam = self.box_beam
        beam_index = self.beam_index
        i1 = min(max(0, beam_index[1] + dx), len(blf_text.text))
        beam_index[1] = i1

        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + round(blfDimen(FONT0, blf_text.text[: i1])[0])
        box_beam.L = L
        box_beam.R = L + SIZE_widget[1]
        box_beam.upd()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        box_beam.color = COL_box_cursor_beam
        self.check_cursor_pos()
        self.upd_highlight()
        Admin.REDRAW()
        #|
    def evt_beam_left_shift(self):

        self.evt_beam_shift_x(-1)
        #|
    def evt_beam_right_shift(self):

        self.evt_beam_shift_x(1)
        #|
    def evt_beam_down_shift(self):

        self.evt_beam_shift_x(len(self.blf_text.text))
        #|
    def evt_beam_up_shift(self):

        self.evt_beam_shift_x(- len(self.blf_text.text))
        #|
    def evt_beam_line_begin(self): self.evt_beam_start()
    def evt_beam_line_end(self): self.evt_beam_end()
    def evt_beam_left_word(self):

        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text[: i1]

        if not s: return
        i = r_prev_word_index(s)
        if i == i1: i -= 1
        if i < 0: i = 0

        self.set_highlight(i, i)
        self.check_cursor_pos()
        #|
    def evt_beam_right_word(self):

        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text

        if not s: return
        i = r_next_word_index(s, i1)
        if i == i1:
            i += 1
            if i > len(s): i = len(s)

        self.set_highlight(i, i)
        self.check_cursor_pos()
        #|
    def evt_beam_move_x(self, dx, evtkill=True):

        if evtkill is True: kill_evt_except()
        blf_text = self.blf_text
        box_beam = self.box_beam
        box_selection = self.box_selection
        beam_index = self.beam_index
        i1 = min(max(0, beam_index[1] + dx), len(blf_text.text))
        beam_index[0] = i1
        beam_index[1] = i1

        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + round(blfDimen(FONT0, blf_text.text[: i1])[0])
        box_beam.L = L
        box_beam.R = L + SIZE_widget[1]
        box_beam.upd()
        box_selection.L = box_selection.R = L
        box_selection.upd()
        Admin.REDRAW()

        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        box_beam.color = COL_box_cursor_beam
        self.check_cursor_pos()
        #|
    def evt_beam_left(self):

        self.evt_beam_move_x(- 1)
        kill_evt_except()
        #|
    def evt_beam_right(self):

        self.evt_beam_move_x(1)
        kill_evt_except()
        #|
    def evt_beam_down(self):

        #|
        if timer_isreg(timer_beam) and self == SELF:
            if self.blf_text.color != COL_box_text_fg_ignore:
                self.blf_text.color = COL_box_text_fg_ignore
                self.set_highlight(self.beam_index[1], self.beam_index[1])

        ind = self.filt.active_index
        self.filt.set_active_index(0  if ind == None else ind + 1, callback=True)

        if P.filter_autopan_active:
            if ind != self.filt.active_index and self.filt.box_active.B < self.scissor_filt.y:
                self.filt.r_pan_override()(0, D_SIZE['widget_full_h'])
        #|
    def evt_beam_up(self):

        #|
        if timer_isreg(timer_beam) and self == SELF:
            if self.blf_text.color != COL_box_text_fg_ignore:
                self.blf_text.color = COL_box_text_fg_ignore
                self.set_highlight(self.beam_index[1], self.beam_index[1])

        ind = self.filt.active_index
        self.filt.set_active_index(0  if ind == None else ind - 1, callback=True)

        if P.filter_autopan_active:
            if ind != self.filt.active_index and self.filt.box_active.T >= self.scissor_filt.y + self.scissor_filt.h:
                self.filt.r_pan_override()(0, - D_SIZE['widget_full_h'])
        #|
    def evt_beam_end_shift(self): self.evt_beam_down_shift()
    def evt_beam_start_shift(self): self.evt_beam_up_shift()
    def evt_beam_end(self):

        self.evt_beam_move_x(len(self.blf_text.text))
        kill_evt_except()
        #|
    def evt_beam_start(self):

        self.evt_beam_move_x(- len(self.blf_text.text))
        kill_evt_except()
        #|
    def evt_toggle_match_case(self, override=None, override_value=None):

        #|
        filt = self.filt
        filt.global_index = "?"
        if override_value == None:
            filt.match_case = not filt.match_case
        else:
            filt.match_case = override_value
        filt.filter_function = r_filter_function(filt.match_case, filt.match_whole_word, filt.match_end)
        filt.filter_text(self.blf_text.text  if override == None else override)

        self.get_box_match()
        kill_evt_except()
        Admin.REDRAW()
        if self.is_dropdown is False and hasattr(self, "r_active_index"):
            i = self.r_active_index()
            filt.upd_active_index(None  if i in {None, -1} else i)
        #|
    def evt_toggle_match_whole_word(self, override=None, override_value=None):

        #|
        filt = self.filt
        filt.global_index = "?"
        if override_value == None:
            filt.match_whole_word = not filt.match_whole_word
        else:
            filt.match_whole_word = override_value
        filt.filter_function = r_filter_function(filt.match_case, filt.match_whole_word, filt.match_end)
        filt.filter_text(self.blf_text.text  if override == None else override)

        self.get_box_match()
        kill_evt_except()
        Admin.REDRAW()
        if self.is_dropdown is False and hasattr(self, "r_active_index"):
            i = self.r_active_index()
            filt.upd_active_index(None  if i in {None, -1} else i)
        #|
    def evt_toggle_match_end(self, override=None, override_value=None):

        #|
        filt = self.filt
        filt.global_index = "?"
        if override_value == None:
            filt.match_end += 1
            if filt.match_end == 3:
                filt.match_end = 0
        else:
            filt.match_end = override_value
        filt.filter_function = r_filter_function(filt.match_case, filt.match_whole_word, filt.match_end)
        filt.filter_text(self.blf_text.text  if override == None else override)

        self.get_box_match()
        kill_evt_except()
        Admin.REDRAW()
        if self.is_dropdown is False and hasattr(self, "r_active_index"):
            i = self.r_active_index()
            filt.upd_active_index(None  if i in {None, -1} else i)
        #|
    def evt_linebreak(self): pass
    def evt_untab(self): pass
    def evt_tab(self):

        filt = self.filt
        if hasattr(filt, "active_index"):
            if filt.active_index == None:
                if filt.match_items:
                    Admin.REDRAW()
                    self.evt_select_all(True)
                    self.beam_input(filt.match_items[0].name)
                return
            Admin.REDRAW()
            self.evt_select_all(True)
            self.beam_input(filt.match_items[filt.active_index].name)
        #|

    def evt_area_del_text(self):

        Admin.REDRAW()
        kill_evt_except()
        box_icon_search = self.box_icon_search
        blf_text = self.blf_text
        blf_text.text = ""
        blf_text.unclip_text = ""

        box_icon_search.__class__ = GpuImg_search
        box_icon_search.upd()
        self.filt.filter_text("", callback=True)
        self.upd_clip_text_and_match_button(blf_text)
        self.filt.global_index = "?"
        self.upd_data()
        #|
    def evt_area_copy(self):

        kill_evt_except()
        bpy.context.window_manager.clipboard = self.blf_text.unclip_text
        #|
    def evt_area_paste(self, override=None):

        kill_evt_except()
        tx = bpy.context.window_manager.clipboard  if override == None else override
        if tx:
            Admin.REDRAW()
            box_icon_search = self.box_icon_search
            blf_text = self.blf_text
            blf_text.unclip_text = blf_text.text = tx
            box_icon_search = self.box_icon_search
            if isinstance(box_icon_search, GpuImg_search):
                box_icon_search.__class__ = GpuImg_delete
                box_icon_search.upd()

            self.filt.filter_text(tx)
            self.upd_clip_text_and_match_button(blf_text)
        #|
    def evt_area_cut(self):
        self.evt_area_copy()
        self.evt_area_del_text()
        #|
    def evt_apply(self): pass
    def evt_del(self): pass
    def evt_add(self): pass
    def evt_active_down_most_shift(self): pass
    def evt_active_up_most_shift(self): pass
    def evt_active_down_shift(self): pass
    def evt_active_up_shift(self): pass
    def evt_active_down_most(self):
        ind = self.filt.active_index
        self.filt.set_active_index(len(self.filt.items), callback=True)

        if P.filter_autopan_active and self.filt.active_index != None:
            if ind != self.filt.active_index and self.filt.box_active.B < self.scissor_filt.y:
                self.filt.r_pan_override()(0, D_SIZE['widget_full_h'] * len(self.filt.match_items))
        #|
    def evt_active_up_most(self):
        ind = self.filt.active_index
        self.filt.set_active_index(0, callback=True)

        if P.filter_autopan_active and self.filt.active_index != None:
            if ind != self.filt.active_index and self.filt.box_active.T >= self.scissor_filt.y + self.scissor_filt.h:
                self.filt.r_pan_override()(0, - D_SIZE['widget_full_h'] * len(self.filt.match_items))
        #|
    def evt_active_down(self): self.evt_beam_down()
    def evt_active_up(self): self.evt_beam_up()
    def evt_area_select(self, i, extend=False):

        filt = self.filt
        if filt.blfs and 0 <= i < len(filt.match_items):
            old_act = None
            if hasattr(filt, "selnames"):
                if extend:
                    old_act = filt.active_index
                else:
                    filt.selnames.clear()
                    filt.box_selections.clear()

            if old_act is not None:
                filt.selnames[old_act] = filt.match_items[old_act].name

            filt.set_active_index(i, callback=True)
        #|

    def beam_input_unpush(self, s):
        # <<< 1copy (0area_AreaFilterY_beam_input,, $$)
        ll = len(s)
        tx = self.blf_text
        tx.color = COL_box_text_fg
        i0, i1 = self.beam_index

        if i0 == i1:
            tx.text = tx.text[ : i0] + s + tx.text[i1 : ]
            i1 += ll
            self.set_highlight(i1, i1)
        elif i0 < i1:
            tx.text = tx.text[ : i0] + s + tx.text[i1 : ]
            i0 += ll
            self.set_highlight(i0, i0)
        else:
            tx.text = tx.text[ : i1] + s + tx.text[i0 : ]
            i1 += ll
            self.set_highlight(i1, i1)

        self.check_cursor_pos()
        self.filt.filter_text(self.blf_text.text, None)
        # >>>
        #|
    def beam_input(self, s):
        # /* 0area_AreaFilterY_beam_input
        ll = len(s)
        tx = self.blf_text
        tx.color = COL_box_text_fg
        i0, i1 = self.beam_index

        if i0 == i1:
            tx.text = tx.text[ : i0] + s + tx.text[i1 : ]
            i1 += ll
            self.set_highlight(i1, i1)
        elif i0 < i1:
            tx.text = tx.text[ : i0] + s + tx.text[i1 : ]
            i0 += ll
            self.set_highlight(i0, i0)
        else:
            tx.text = tx.text[ : i1] + s + tx.text[i0 : ]
            i1 += ll
            self.set_highlight(i1, i1)

        self.check_cursor_pos()
        self.filt.filter_text(self.blf_text.text, None)
        # */
        if timer_isreg(timer_undo_push): timer_unreg(timer_undo_push)
        timer_reg(timer_undo_push, first_interval=1.0)
        #|
    def beam_input_replace(self, s):
        self.blf_text.text = ""
        self.beam_index[:] = 0, 0
        self.check_limR()
        self.beam_input(s)
        #|

    def r_push_item(self):
        return (
            self.blf_text.text,
            (self.beam_index[0], self.beam_index[1]),
            self.blf_text.x)
        #|
    def to_history_index(self, index):
        Admin.REDRAW()
        self.evt_del_all(False)
        e = self.local_history.array[index]
        self.beam_input_unpush(e[0])
        self.blf_text.x = e[2]
        self.set_highlight(*e[1])
        #|
    def kill_push_timer(self):
        if timer_isreg(timer_undo_push):
            timer_unreg(timer_undo_push)
            self.local_history.push()
        #|

    def set_highlight(self, i0, i1):
        blfSize(FONT0, D_SIZE['font_main'])
        box_selection = self.box_selection
        box_beam = self.box_beam
        x = self.blf_text.x

        self.beam_index[:] = i0, i1

        L = x + floor(blfDimen(FONT0, self.blf_text.text[: i0])[0])
        R = x + floor(blfDimen(FONT0, self.blf_text.text[: i1])[0])

        box_selection.L = L
        box_selection.R = R
        box_selection.upd()
        box_beam.L = R
        box_beam.R = R + SIZE_widget[1]
        box_beam.upd()
        #|
    def upd_highlight(self):
        blfSize(FONT0, D_SIZE['font_main'])
        box_selection = self.box_selection
        box_beam = self.box_beam
        x = self.blf_text.x

        i0, i1 = self.beam_index

        L = x + floor(blfDimen(FONT0, self.blf_text.text[: i0])[0])
        R = x + floor(blfDimen(FONT0, self.blf_text.text[: i1])[0])

        box_selection.L = L
        box_selection.R = R
        box_selection.upd()
        box_beam.L = R
        box_beam.R = R + SIZE_widget[1]
        box_beam.upd()
        #|

    def r_text_limL(self):
        return self.box_icon_search.R + D_SIZE['font_main_dx']
        #|
    def r_text_limR(self, tx_limL, beam_width): # set size require
        return min(self.box_match_case.L - D_SIZE['font_main_dx'] - beam_width
            - floor(blfDimen(FONT0, self.blf_text.text)[0]), tx_limL)
        #|
    def check_limL(self):
        # /* 0defarea_AreaFilterY_check_limL
        tx_limL = self.r_text_limL()

        if self.blf_text.x > tx_limL:
            self.blf_text.x = tx_limL
            self.upd_highlight()
        # */
    def check_limR(self):
        # /* 0defarea_AreaFilterY_check_limR
        blfSize(FONT0, D_SIZE['font_main'])
        tx_limL = self.r_text_limL()
        tx_limR = self.r_text_limR(tx_limL, 0)

        if self.blf_text.x < tx_limR:
            self.blf_text.x = tx_limR
            self.upd_highlight()
        # */
    def check_cursor_pos(self):
        if self.box_beam.R > self.scissor_text_box.x + self.scissor_text_box.w:
            self.r_pan_text_override()(
                self.scissor_text_box.x + self.scissor_text_box.w - self.box_beam.R)
        elif self.box_beam.L < self.scissor_text_box.x + SIZE_widget[0]:
            self.r_pan_text_override()(
                self.scissor_text_box.x + SIZE_widget[0] - self.box_beam.L)
        #|

    def i_draw(self):
        # ref_AreaFilterY_i_draw
        blend_set('ALPHA')
        boxes = self.boxes
        boxes[0].bind_draw()
        boxes[1].bind_draw()
        boxes[2].bind_draw()
        boxes[3].bind_draw()
        boxes[6].bind_draw()
        boxes[7].bind_draw()
        boxes[8].bind_draw()
        boxes[9].bind_draw()
        boxes[10].bind_draw()
        boxes[11].bind_draw()
        boxes[12].bind_draw()

        filt = self.filt
        filt.box_scroll_bg.bind_draw()
        filt.box_scroll.bind_draw()

        self.scissor_text_box.use()
        boxes[4].bind_draw()
        boxes[5].bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        self.scissor_filt.use()
        blend_set('ALPHA')
        filt.box_active.bind_draw()
        filt.box_hover.bind_draw()
        blfs = filt.blfs
        for e in filt.icons.values(): e.bind_draw()
        for e in blfs.values():
            blfColor(FONT0, *e.color)
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)
        blfColor(FONT0, *COL_box_filter_fg_info)
        for k, e in filt.blfs_info.items():
            blfPos(FONT0, e.x, blfs[k].y, 0)
            blfDraw(FONT0, e.text)
        self.w.scissor.use()
        #|

    def upd_data(self):
        filt = self.filt
        new_items = filt.get_items()

        if TAG_RENAME[0] is True:

            pass
        elif new_items != filt.items_unsort: pass
        else:
            its = filt.match_items
            if all(e.text == its[r].name  for r, e in filt.blfs.items()) is True:
                geticon = filt.get_icon
                if geticon == None: return

                if all(type(e) == type(geticon(its[k]))  for k, e in filt.icons.items()): return

            else:

                pass


        if hasattr(filt, "selnames"):
            old_selnames = filt.selnames.copy()

        filt.global_index = "?"
        filt.items_unsort = new_items
        filt.init_items()

        if filt.blfs:
            y = filt.blfs[filt.headkey].y + filt.headkey * D_SIZE['widget_full_h']
            filt.filter_text(self.blf_text.unclip_text)
            if filt.blfs:
                self.filt.r_pan_override()(0, y - filt.blfs[filt.headkey].y - filt.headkey * D_SIZE['widget_full_h'])
        else:
            filt.filter_text(self.blf_text.unclip_text)

        if hasattr(filt, "selnames"):
            selnames = filt.selnames
            le = len(new_items)
            for r, name in old_selnames.items():
                if r < le: selnames[r] = new_items[r].name
        #|
    #|
    #|
class FilterY:
    __slots__ = (
        'w',
        'get_items',
        'get_icon',
        'get_info',
        'items_unsort',
        'items',
        'match_items',
        'icons',
        'blfs',
        'blfs_info',
        'filter_function',
        'match_case',
        'match_whole_word',
        'match_end',
        'match_invert',
        'sort_order',
        'headkey',
        'endkey',
        'box_scroll_bg',
        'box_scroll',
        'box_active',
        'box_hover',
        'active_index',
        'set_active_index_callback',
        'names',
        'rm_items',
        'global_index',
        'is_filter_text_set_index')

    ISRUNNING_set_active_index = False

    def __init__(self, w, get_items, get_icon, get_info, is_filter_text_set_index=True):
        #|
        self.w = w
        self.get_items = get_items
        self.get_icon = get_icon
        self.get_info = get_info

        self.match_end = P.filter_match_end
        self.match_case = P.filter_match_case
        self.match_whole_word = P.filter_match_whole_word
        self.match_invert = False
        self.sort_order = set()
        self.global_index = "?"
        self.is_filter_text_set_index = is_filter_text_set_index

        self.items_unsort = get_items()
        self.init_items()
        self.match_items = []
        self.active_index = None
        self.set_active_index_callback = NKW

        self.icons = {}
        self.blfs = {}
        self.blfs_info = {}
        self.box_scroll_bg = GpuBox(COL_box_scrollbar_bg)
        self.box_scroll = GpuBox(COL_box_scrollbar)
        self.box_active = GpuBox_box_filter_active_bg()
        self.box_active.upd()
        self.box_hover = GpuBox_box_filter_hover_bg()

        self.headkey = 0
        self.endkey = -1

        self.filter_function = r_filter_function(self.match_case, self.match_whole_word, self.match_end)
        self.rm_items = []
        #|

    def init_items(self): # NEed ITems_unsort
        self.items = self.items_unsort
        self.names = {e.name: r  for r, e in enumerate(self.items)}
        #|

    def upd_size(self):
        # ref_FilterY_upd_size
        match_items = self.match_items
        box_filter = self.w.box_filter
        widget_rim = SIZE_border[3]
        icons = self.icons
        blfs = self.blfs
        blfs_info = self.blfs_info
        icons.clear()
        blfs.clear()
        blfs_info.clear()
        len_match_items = len(match_items)

        R = box_filter.R - widget_rim
        scroll_width = min(SIZE_widget[2], SIZE_widget[0])
        self.box_scroll_bg.LRBT_upd(R - scroll_width, R, box_filter.B + widget_rim, box_filter.T - widget_rim)
        self.box_hover.LRBT_upd(0, 0, 0, 0)

        old_act = self.active_index
        # if blfs:
        #     e0 = blfs[self.headkey]
        #     xy = e0.x, e0.y + self.headkey * D_SIZE['widget_full_h']
        # else:
        #     xy = None
        # <<< 1copy (0area_filter_get_blfs,, $$)
        self.headkey = 0
        full_h = D_SIZE['widget_full_h']
        T = box_filter.T - widget_rim
        x = box_filter.L + widget_rim + SIZE_filter[1] + widget_rim + D_SIZE['font_main_dy']
        y = T - SIZE_filter[2] - widget_rim - D_SIZE['font_main_dT']
        range_end = min(len_match_items, ceil((T - box_filter.B - widget_rim) / full_h) + 1)
        self.endkey = range_end - 1
        get_info = self.get_info

        if self.get_icon is None:
            if get_info is None:
                for r in range(range_end):
                    e = BlfColor(match_items[r].name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    y -= full_h
            else:
                blfSize(FONT0, D_SIZE['font_main'])
                xx = x + full_h
                for r in range(range_end):
                    o = match_items[r]
                    e = BlfColor(o.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    blfs_info[r] = Blf(get_info(o), xx + round(blfDimen(FONT0, e.text)[0]))
                    y -= full_h
        else:
            h = SIZE_widget[0]
            x += h
            R = x - D_SIZE['font_main_dy']
            L = R - h
            B = y - D_SIZE['font_main_dy']
            T = B + h
            geticon = self.get_icon

            if get_info is None:
                for r in range(range_end):
                    it = match_items[r]
                    e = BlfColor(it.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    ee = geticon(it)
                    if isinstance(ee, GpuImgSlot2): e.x += ee.max_index * h
                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h
            else:
                blfSize(FONT0, D_SIZE['font_main'])
                xx = x + full_h
                for r in range(range_end):
                    it = match_items[r]
                    e = BlfColor(it.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    e_info = Blf(get_info(it), xx + round(blfDimen(FONT0, e.text)[0]))
                    blfs_info[r] = e_info
                    ee = geticon(it)
                    if isinstance(ee, GpuImgSlot2):
                        x_offset = ee.max_index * h
                        e.x += x_offset
                        e_info.x += x_offset

                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h

        self.r_upd_scroll()()
        # >>>
        self.set_active_index(old_act)
        return None
        #|

    def dxy(self, dx, dy):
        # ref_FilterY_dxy
        self.box_scroll_bg.dxy_upd(dx, dy)
        self.box_scroll.dxy_upd(dx, dy)

        for e in self.icons.values(): e.dxy_upd(dx, dy)
        for e in self.blfs.values():
            e.x += dx
            e.y += dy
        for e in self.blfs_info.values():
            e.x += dx

        self.box_active.dxy_upd(dx, dy)
        self.box_hover.dxy_upd(dx, dy)
        #|

    def r_blfs_width(self):
        if self.blfs:
            blfSize(FONT0, D_SIZE['font_main'])
            blfs_info = self.blfs_info
            if blfs_info:
                blfs = self.blfs
                return floor(max(blfDimen(FONT0, e.text)[0] + blfDimen(FONT0, blfs_info[k].text)[0]  for k, e in blfs.items())) + D_SIZE['widget_full_h'] * 2
            return floor(max(blfDimen(FONT0, e.text)[0]  for e in self.blfs.values())) + D_SIZE['widget_full_h']
        return 0
        #|
    def to_modal_pan(self):
        # ref_FilterY_to_modal_pan

        #|
        if self.blfs: pass
        else: return

        end_trigger = r_end_trigger('pan')
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop()
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        # <<< 1copy (0defpanGet,, $$)
        _blfSize = blfSize
        _blfDimen = blfDimen
        _FONT0 = FONT0
        _fontsize_main = D_SIZE['font_main']
        sci = self.w.scissor_filt
        widget_rim = SIZE_border[3]
        blf_offset_x = D_SIZE['font_main_dy'] + SIZE_filter[1] + widget_rim
        sci_B = sci.y
        sci_T = sci.y + sci.h

        _r_blfs_width = self.r_blfs_width
        _blfs_width = [_r_blfs_width()]
        _full_h = D_SIZE['widget_full_h']
        _h = SIZE_widget[0]
        _oo = self.match_items
        _li = self.blfs
        _li_info = self.blfs_info
        _max_endkey = len(_oo) - 1
        _T_add = sci_T - widget_rim - D_SIZE['font_main_dT']
        _B_add = sci_B + widget_rim + D_SIZE['font_main_dy']
        _lim_L = sci.x + blf_offset_x
        _lim_R = sci.x + sci.w - blf_offset_x
        _lim_B = sci_B + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim
        _lim_T = sci_T - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT']
        _len = len(_li)

        if self.get_icon is None:
            _geticon = None
            _li_icon = {}
        else:
            _geticon = self.get_icon
            _li_icon = self.icons
            _icon_dB = - D_SIZE['font_main_dy']
            _icon_dT = D_SIZE['font_main_dT']
            _icon_dR = - D_SIZE['font_main_dy']
            _icon_dL = _icon_dR - _h
            _lim_L += _h

        _getinfo = self.get_info

        _upd_scroll = self.r_upd_scroll()
        _box_active_dy_upd = self.box_active.dy_upd
        _Blf = Blf
        _BlfColor = BlfColor
        _COL_box_filter_fg = COL_box_filter_fg
        # >>>

        if _geticon is None:
            if _getinfo is None:
                def modal_pan():
                    _REDRAW()
                    if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                        w_head.fin()
                        return
                    dx, dy = r_dxy_mouse()

                    # <<< 1copy (0defpanModalNoIconNoInfo,, $$)
                    bo0 = _li[self.headkey]
                    x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        _li[headkey] = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        T += _full_h
                                        del _li[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        _li[endkey] = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        B -= _full_h
                                        del _li[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    mouseloop()
            else:
                def modal_pan():
                    _REDRAW()
                    if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                        w_head.fin()
                        return
                    dx, dy = r_dxy_mouse()

                    # <<< 1copy (0defpanModalNoIcon,, $$)
                    bo0 = _li[self.headkey]
                    x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                xx = x + _full_h
                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        _li_info[headkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_info[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                xx = x + _full_h
                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        _li_info[endkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_info[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy
                    for e in _li_info.values():
                        e.x += dx

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    mouseloop()
        else:
            if _getinfo is None:
                def modal_pan():
                    _REDRAW()
                    if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                        w_head.fin()
                        return
                    dx, dy = r_dxy_mouse()

                    # <<< 1copy (0defpanModalNoInfo,, $$)
                    bo0 = _li[self.headkey]
                    bo0_icon = _li_icon[self.headkey]
                    if hasattr(bo0_icon, "max_index"):
                        x_offset = - bo0_icon.max_index * _h
                    else:
                        x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                x += x_offset
                                L = x + _icon_dL
                                R = x + _icon_dR

                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                bo1_icon = _li_icon[endkey]
                                if hasattr(bo1_icon, "max_index"): x -= bo1_icon.max_index * _h
                                L = x + _icon_dL
                                R = x + _icon_dR

                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy
                    for e in _li_icon.values(): e.dxy_upd(dx, dy)

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    mouseloop()
            else:
                def modal_pan():
                    _REDRAW()
                    if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                        w_head.fin()
                        return
                    dx, dy = r_dxy_mouse()

                    # <<< 1copy (0defpanModal,, $$)
                    bo0 = _li[self.headkey]
                    bo0_icon = _li_icon[self.headkey]
                    if hasattr(bo0_icon, "max_index"):
                        x_offset = - bo0_icon.max_index * _h
                    else:
                        x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                x += x_offset
                                L = x + _icon_dL
                                R = x + _icon_dR

                                xx = x + _full_h
                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        _li_info[headkey] = e_info
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"):
                                            x_offset = ee.max_index * _h
                                            e.x += x_offset
                                            e_info.x += x_offset

                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        del _li_info[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                bo1_icon = _li_icon[endkey]
                                if hasattr(bo1_icon, "max_index"): x -= bo1_icon.max_index * _h
                                L = x + _icon_dL
                                R = x + _icon_dR

                                xx = x + _full_h
                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        _li_info[endkey] = e_info
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"):
                                            x_offset = ee.max_index * _h
                                            e.x += x_offset
                                            e_info.x += x_offset

                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        del _li_info[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy
                    for e in _li_info.values():
                        e.x += dx
                    for e in _li_icon.values(): e.dxy_upd(dx, dy)

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    mouseloop()

        def end_modal_pan():
            _REDRAW()
            mouseloop_end()
            kill_evt_except()

        self.box_hover.LRBT_upd(0, 0, 0, 0)
        w_head = Head(self, modal_pan, end_modal_pan)
        _REDRAW()
        #|
    def r_pan_override(self):
        # <<< 1copy (0defpanGet,, $$)
        _blfSize = blfSize
        _blfDimen = blfDimen
        _FONT0 = FONT0
        _fontsize_main = D_SIZE['font_main']
        sci = self.w.scissor_filt
        widget_rim = SIZE_border[3]
        blf_offset_x = D_SIZE['font_main_dy'] + SIZE_filter[1] + widget_rim
        sci_B = sci.y
        sci_T = sci.y + sci.h

        _r_blfs_width = self.r_blfs_width
        _blfs_width = [_r_blfs_width()]
        _full_h = D_SIZE['widget_full_h']
        _h = SIZE_widget[0]
        _oo = self.match_items
        _li = self.blfs
        _li_info = self.blfs_info
        _max_endkey = len(_oo) - 1
        _T_add = sci_T - widget_rim - D_SIZE['font_main_dT']
        _B_add = sci_B + widget_rim + D_SIZE['font_main_dy']
        _lim_L = sci.x + blf_offset_x
        _lim_R = sci.x + sci.w - blf_offset_x
        _lim_B = sci_B + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim
        _lim_T = sci_T - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT']
        _len = len(_li)

        if self.get_icon is None:
            _geticon = None
            _li_icon = {}
        else:
            _geticon = self.get_icon
            _li_icon = self.icons
            _icon_dB = - D_SIZE['font_main_dy']
            _icon_dT = D_SIZE['font_main_dT']
            _icon_dR = - D_SIZE['font_main_dy']
            _icon_dL = _icon_dR - _h
            _lim_L += _h

        _getinfo = self.get_info

        _upd_scroll = self.r_upd_scroll()
        _box_active_dy_upd = self.box_active.dy_upd
        _Blf = Blf
        _BlfColor = BlfColor
        _COL_box_filter_fg = COL_box_filter_fg
        # >>>

        if _geticon is None:
            if _getinfo is None:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanModalNoIconNoInfo,, $$)
                    bo0 = _li[self.headkey]
                    x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        _li[headkey] = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        T += _full_h
                                        del _li[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        _li[endkey] = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        B -= _full_h
                                        del _li[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy
            else:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanModalNoIcon,, $$)
                    bo0 = _li[self.headkey]
                    x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                xx = x + _full_h
                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        _li_info[headkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_info[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                xx = x + _full_h
                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        _li_info[endkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_info[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy
                    for e in _li_info.values():
                        e.x += dx

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy
        else:
            if _getinfo is None:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanModalNoInfo,, $$)
                    bo0 = _li[self.headkey]
                    bo0_icon = _li_icon[self.headkey]
                    if hasattr(bo0_icon, "max_index"):
                        x_offset = - bo0_icon.max_index * _h
                    else:
                        x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                x += x_offset
                                L = x + _icon_dL
                                R = x + _icon_dR

                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                bo1_icon = _li_icon[endkey]
                                if hasattr(bo1_icon, "max_index"): x -= bo1_icon.max_index * _h
                                L = x + _icon_dL
                                R = x + _icon_dR

                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy
                    for e in _li_icon.values(): e.dxy_upd(dx, dy)

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy
            else:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanModal,, $$)
                    bo0 = _li[self.headkey]
                    bo0_icon = _li_icon[self.headkey]
                    if hasattr(bo0_icon, "max_index"):
                        x_offset = - bo0_icon.max_index * _h
                    else:
                        x_offset = 0

                    if dx < 0:
                        R = bo0.x + _blfs_width[0] + dx
                        if R < _lim_R:
                            dx -= R - _lim_R
                            L = bo0.x + dx + x_offset
                            if L > _lim_L: dx -= L - _lim_L
                    else:
                        L = bo0.x + dx + x_offset
                        if L > _lim_L: dx -= L - _lim_L

                    if dy < 0:
                        headkey = self.headkey
                        T = bo0.y + dy
                        if headkey == 0:
                            if T < _lim_T: dy -= T - _lim_T
                        else:
                            if T < _T_add:

                                endkey = self.endkey
                                x = bo0.x
                                _blfSize(_FONT0, _fontsize_main)

                                x += x_offset
                                L = x + _icon_dL
                                R = x + _icon_dR

                                xx = x + _full_h
                                while headkey != 0:
                                    if T < _T_add:

                                        y = _li[headkey].y + _full_h
                                        headkey -= 1
                                        o = _oo[headkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        _li_info[headkey] = e_info
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"):
                                            x_offset = ee.max_index * _h
                                            e.x += x_offset
                                            e_info.x += x_offset

                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        del _li_info[endkey]
                                        endkey -= 1
                                    else: break

                                if headkey == 0:
                                    T = _li[0].y + dy
                                    if T < _lim_T: dy -= T - _lim_T

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()


                    else:
                        endkey = self.endkey
                        bo1 = _li[endkey]
                        B = bo1.y + dy
                        if endkey == _max_endkey:
                            if B > _lim_B:
                                dy -= B - _lim_B
                                if self.headkey == 0:
                                    TT = bo0.y + dy
                                    if TT < _lim_T: dy += _lim_T - TT
                        else:
                            if B > _B_add:

                                headkey = self.headkey
                                x = bo1.x
                                _blfSize(_FONT0, _fontsize_main)

                                bo1_icon = _li_icon[endkey]
                                if hasattr(bo1_icon, "max_index"): x -= bo1_icon.max_index * _h
                                L = x + _icon_dL
                                R = x + _icon_dR

                                xx = x + _full_h
                                while endkey != _max_endkey:
                                    if B > _B_add:

                                        y = _li[endkey].y - _full_h
                                        endkey += 1
                                        o = _oo[endkey]
                                        e = _BlfColor(o.name, x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        _li_info[endkey] = e_info
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"):
                                            x_offset = ee.max_index * _h
                                            e.x += x_offset
                                            e_info.x += x_offset

                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        del _li_info[headkey]
                                        headkey += 1
                                    else: break

                                if endkey == _max_endkey:
                                    B = _li[endkey].y + dy
                                    if B > _lim_B: dy -= B - _lim_B

                                self.headkey = headkey
                                self.endkey = endkey
                                _blfs_width[0] = _r_blfs_width()



                    for e in _li.values():
                        e.x += dx
                        e.y += dy
                    for e in _li_info.values():
                        e.x += dx
                    for e in _li_icon.values(): e.dxy_upd(dx, dy)

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy

        return pan_override
        #|
    def to_modal_scrollbar(self):

        #|
        if self.blfs: pass
        else: return

        end_trigger = r_end_trigger('dd_scroll')
        _REDRAW = Admin.REDRAW
        _mou = MOUSE[:]
        _scrollbar = self.box_scroll
        _li = self.blfs
        _full_h = D_SIZE['widget_full_h']
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _pan_override = self.r_pan_override()

        # <<< 1copy (0area_FilterY_fn_cvY_fac,, ${
        #     'fn_cvY_fac = rf_linear_01': 'fn_cvY_fac, _fn_cvY_fac_inv = rf_linear_01_inv'
        # }$)
        box_scroll = self.box_scroll
        L, R, B, T = self.box_scroll_bg.r_LRBT()

        self.upd_scissor_filt()
        sci = self.w.scissor_filt
        sci_h = sci.h
        B = sci.y
        T = B + sci_h
        len_items = len(self.match_items)

        h = D_SIZE['widget_full_h']
        widget_rim = SIZE_border[3]
        cv_h = len_items * h
        bar_h_min = h // 2
        bar_h = T - B
        button_h = min(max(floor(bar_h * sci_h / cv_h), bar_h_min), bar_h)
        barY_dif = bar_h - button_h

        fn_cvY_fac, _fn_cvY_fac_inv = rf_linear_01_inv(
            T - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT'],
            B + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim + h * (len_items - 1))
        # >>>

        _fn_scroll_fac = rf_linear_01(
            sci.y + sci.h,
            sci.y + button_h)

        if _scrollbar.inbox(MOUSE) == False:
            # <<< 1copy (0area_FilterY_i_modal_scrollbar,, ${
            #     'MOUSE[1] - _mou[1]': 'MOUSE[1] + button_h // 2 - _scrollbar.T'
            # }$)
            _pan_override(0, round(_fn_cvY_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.T + MOUSE[1] + button_h // 2 - _scrollbar.T)), 1.0)) - _li[self.headkey].y - _full_h * self.headkey))
            # >>>

        def modal_scrollbar():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            # dy = MOUSE[1] - _mou[1]
            # fac = min(max(0.0, _fn_scroll_fac(_scrollbar.T + dy)), 1.0)
            # T = _fn_cvY_fac_inv(fac)
            # dy = T - _li[self.headkey].y - _h * self.headkey
            # _pan_override(0, round(dy))
            # /* 0area_FilterY_i_modal_scrollbar
            _pan_override(0, round(_fn_cvY_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.T + MOUSE[1] - _mou[1])), 1.0)) - _li[self.headkey].y - _full_h * self.headkey))
            # */

            _mou[:] = MOUSE

        def end_modal_scrollbar():
            _REDRAW()
            kill_evt_except()

        w_head = Head(self, modal_scrollbar, end_modal_scrollbar)
        _REDRAW()
        #|

    def filter_text(self, s, active_index=0, callback=False):
        # ref_FilterY_filter_text
        if s:
            fx = self.filter_function
            self.match_items = [e for e in self.items if fx(e.name, s)]
        else:
            self.match_items = self.items
        match_items = self.match_items
        # print('-------------------------')
        # for e in self.match_items: print(e.name)
        # print('-------------------------')

        box_filter = self.w.box_filter
        widget_rim = SIZE_border[3]
        icons = self.icons
        blfs = self.blfs
        blfs_info = self.blfs_info
        icons.clear()
        blfs.clear()
        blfs_info.clear()
        len_match_items = len(match_items)

        # /* 0area_filter_get_blfs
        self.headkey = 0
        full_h = D_SIZE['widget_full_h']
        T = box_filter.T - widget_rim
        x = box_filter.L + widget_rim + SIZE_filter[1] + widget_rim + D_SIZE['font_main_dy']
        y = T - SIZE_filter[2] - widget_rim - D_SIZE['font_main_dT']
        range_end = min(len_match_items, ceil((T - box_filter.B - widget_rim) / full_h) + 1)
        self.endkey = range_end - 1
        get_info = self.get_info

        if self.get_icon is None:
            if get_info is None:
                for r in range(range_end):
                    e = BlfColor(match_items[r].name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    y -= full_h
            else:
                blfSize(FONT0, D_SIZE['font_main'])
                xx = x + full_h
                for r in range(range_end):
                    o = match_items[r]
                    e = BlfColor(o.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    blfs_info[r] = Blf(get_info(o), xx + round(blfDimen(FONT0, e.text)[0]))
                    y -= full_h
        else:
            h = SIZE_widget[0]
            x += h
            R = x - D_SIZE['font_main_dy']
            L = R - h
            B = y - D_SIZE['font_main_dy']
            T = B + h
            geticon = self.get_icon

            if get_info is None:
                for r in range(range_end):
                    it = match_items[r]
                    e = BlfColor(it.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    ee = geticon(it)
                    if isinstance(ee, GpuImgSlot2): e.x += ee.max_index * h
                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h
            else:
                blfSize(FONT0, D_SIZE['font_main'])
                xx = x + full_h
                for r in range(range_end):
                    it = match_items[r]
                    e = BlfColor(it.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    e_info = Blf(get_info(it), xx + round(blfDimen(FONT0, e.text)[0]))
                    blfs_info[r] = e_info
                    ee = geticon(it)
                    if isinstance(ee, GpuImgSlot2):
                        x_offset = ee.max_index * h
                        e.x += x_offset
                        e_info.x += x_offset

                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h

        self.r_upd_scroll()()
        # */
        if self.is_filter_text_set_index is True:
            self.set_active_index(active_index, callback)
        #|

    def set_active_index(self, ind, callback=False):

        FilterY.ISRUNNING_set_active_index = True
        blfs = self.blfs
        box_active = self.box_active
        self.global_index = "?"

        if ind == None or not blfs:
            self.active_index = None
            active_element = None
            if box_active.L != box_active.R:
                box_active.LRBT_upd(0, 0, 0, 0)
                Admin.REDRAW()
        else:
            ind = min(max(0, ind), len(self.match_items) - 1)
            self.active_index = ind
            active_element = self.match_items[ind]
            if hasattr(self, "selnames"):
                if ind in self.selnames: del self.selnames[ind]
                if ind in self.box_selections: del self.box_selections[ind]

            y = blfs[self.headkey].y + (self.headkey - ind) * D_SIZE['widget_full_h']
            L = self.w.scissor_filt.x
            R = self.box_scroll_bg.L
            B = y - D_SIZE['font_main_dy']
            T = y + D_SIZE['font_main_dT']
            if box_active.L == L and box_active.R == R and box_active.B == B and box_active.T == T: pass
            else:
                box_active.LRBT_upd(L, R, B, T)
                Admin.REDRAW()

        if callback: self.set_active_index_callback(
            # index=None  if self.active_index == None else self.active_index + self.headkey,
            object=active_element)
        FilterY.ISRUNNING_set_active_index = False
        #|
    def upd_active_index(self, global_index):
        if global_index == self.global_index: return

        self.set_active_index(self.r_local_index(global_index))
        self.global_index = global_index
        #|

    def upd_scissor_filt(self):
        self.w.upd_scissor_filt(self.w.w.scissor)
        #|
    def r_upd_scroll(self): # need box_scroll_bg
        if self.blfs:
            # /* 0area_FilterY_fn_cvY_fac
            box_scroll = self.box_scroll
            L, R, B, T = self.box_scroll_bg.r_LRBT()

            self.upd_scissor_filt()
            sci = self.w.scissor_filt
            sci_h = sci.h
            B = sci.y
            T = B + sci_h
            len_items = len(self.match_items)

            h = D_SIZE['widget_full_h']
            widget_rim = SIZE_border[3]
            cv_h = len_items * h
            bar_h_min = h // 2
            bar_h = T - B
            button_h = min(max(floor(bar_h * sci_h / cv_h), bar_h_min), bar_h)
            barY_dif = bar_h - button_h

            fn_cvY_fac = rf_linear_01(
                T - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT'],
                B + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim + h * (len_items - 1))
            # */

            blfs = self.blfs

            def upd_scroll():
                T0 = T - max(round(fn_cvY_fac(blfs[self.headkey].y + self.headkey * h) * barY_dif), 0)
                box_scroll.LRBT_upd(L, R, T0 - button_h, T0)

            return upd_scroll
        else:
            box_scroll_LRBT_upd = self.box_scroll.LRBT_upd
            box_scroll_bg_r_LRBT = self.box_scroll_bg.r_LRBT

            def upd_scroll():
                box_scroll_LRBT_upd(*box_scroll_bg_r_LRBT())

            return upd_scroll
        #|

    def evt_scrollX(self, dx):

        if not self.blfs: return
        self.r_pan_override()(dx, 0)
        Admin.REDRAW()
        #|
    def evt_scrollY(self, dy):

        if not self.blfs: return
        self.r_pan_override()(0, dy)
        Admin.REDRAW()
        #|

    def r_local_index(self, global_index):
        if global_index in {None, -1}: return None
        if self.match_items == self.items: return global_index
        if global_index >= len(self.items): return None
        ob = self.items[global_index]
        for r, e in enumerate(self.match_items):
            if e == ob: return r
        return None
        #|
    def r_mouse_index_safe(self):
        hover = self.box_hover
        blfs = self.blfs
        if blfs:
            T = blfs[self.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
            i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + self.headkey
            if 0 <= i < len(self.match_items): return i
        return None
        #|
    #|
    #|

class AreaValBox(AreaFilterY):
    __slots__ = 'box_icon_py', 'use_py_exp', 'active_element', 'calc'

    def __init__(self, w, LL, RR, BB, TT, input_text=""):
        #|
        self.w = w
        self.u_draw = self.i_draw
        self.is_dropdown = True
        self.use_py_exp = P.use_py_exp
        self.active_element = None

        box_area = GpuBox_area()
        box_text = GpuRim(COL_box_text, COL_box_text_rim)
        box_selection = GpuBox(COL_box_text_selection)
        box_beam = GpuBox(COL_box_cursor_beam)
        box_match_hover = GpuImg_filter_match_hover()
        box_icon_py = GpuImg_py_exp_on()  if self.use_py_exp else GpuImg_py_exp_off()
        blf_text = BlfClip("", input_text)
        blf_text.color = COL_box_text_fg

        self.boxes = [
            box_area,
            box_text,
            box_selection,
            box_beam,
            box_match_hover,
            box_icon_py
        ]
        self.box_area = box_area
        self.box_text = box_text
        self.box_selection = box_selection
        self.box_beam = box_beam
        self.box_match_hover = box_match_hover
        self.box_icon_py = box_icon_py
        self.blf_text = blf_text
        self.scissor_text_box = Scissor()

        self.beam_index = [len(input_text)] * 2
        self.filt = CalcFilt(self)

        rna = w.data["rna"]
        if isinstance(rna.hard_min  if hasattr(rna, "hard_min") else rna.min_value, int):
            self.calc = Calc(input_text)
        else:
            self.calc = Calc(input_text, UnitSystem.unit_system, UnitSystem.unit_length,
                (rna.unit  if hasattr(rna, "unit") else D_gn_subtype_unit[rna.subtype])
            )

        self.upd_size(LL, RR, BB, TT)
        #|

    def upd_size(self, LL, RR, BB, TT):
        self.box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        widget_rim = SIZE_border[3]
        font_main_dy = D_SIZE['font_main_dy']

        LL += d0
        RR -= d0
        TT -= d0
        BB += d0

        box_text = self.box_text
        blf_text = self.blf_text

        B = TT - D_SIZE['widget_full_h']
        box_text.LRBT_upd(LL, RR, B, TT, widget_rim)

        L, R, B, T = box_text.inner
        L0 = R - SIZE_widget[0]

        if self.use_py_exp == True:
            if isinstance(self.box_icon_py, GpuImg_py_exp_off): self.box_icon_py.__class__ = GpuImg_py_exp_on
        else:
            if isinstance(self.box_icon_py, GpuImg_py_exp_on): self.box_icon_py.__class__ = GpuImg_py_exp_off
        self.box_icon_py.LRBT_upd(L0, R, B, T)
        self.box_match_hover.LRBT_upd(0, 0, 0, 0)
        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L + D_SIZE['font_main_dx']
        blf_text.y = B + font_main_dy

        self.scissor_text_box.intersect_with(self.w.scissor, L, L0 - font_main_dy, box_text.B, box_text.T)
        #|

    def modal(self): pass
    def to_modal_dd(self, select_all=None):

        #|
        global SELF, P_cursor_beam_time
        blf_text = self.blf_text
        self.box_text.color = COL_box_text_active

        _REDRAW = Admin.REDRAW
        _REDRAW()
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _TRIGGER_dd_esc = TRIGGER['dd_esc']
        _TRIGGER_dd_confirm = TRIGGER['dd_confirm']
        _box_win = self.w.box_win
        _box_win_inbox = _box_win.inbox
        _box_text_inbox = self.box_text.inbox
        _box_icon_py = self.box_icon_py
        _box_match_hover = self.box_match_hover
        _text_evt = self.text_evt

        def modal_dd():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or _TRIGGER_dd_esc():
                _temp[0] = w_head.data
                w_head.fin()
                return

            if _TRIGGER_dd_confirm():
                _temp[0] = None
                w_head.fin()
                return

            if _box_win_inbox(MOUSE):
                if _box_text_inbox(MOUSE):
                    if MOUSE[0] >= _box_icon_py.L:
                        Admin.TAG_CURSOR = 'DEFAULT'

                        if _box_match_hover.L == _box_icon_py.L and _box_match_hover.R == _box_icon_py.R: pass
                        else:
                            _REDRAW()
                            _box_match_hover.LRBT_upd(_box_icon_py.L, _box_icon_py.R, _box_icon_py.B, _box_icon_py.T)

                        if TRIGGER['click']():
                            self.evt_toggle_exp()
                            return
                    else:
                        Admin.TAG_CURSOR = 'TEXT'
                        if _box_match_hover.L == _box_match_hover.R: pass
                        else:
                            _REDRAW()
                            _box_match_hover.LRBT_upd(0, 0, 0, 0)

                    if self.active_element != self:

                        if self.active_element is not None: self.active_element.outside_evt()
                        self.active_element = self

                    if TRIGGER['rm']():
                        self.to_modal_dd_rm()
                        return
                elif self.w.area_display.box_area.inbox(MOUSE):
                    block0 = self.w.area_display.item
                    if self.active_element != block0:

                        Admin.TAG_CURSOR = 'DEFAULT'
                        if self.active_element is not None: self.active_element.outside_evt()
                        block0.box_block.color = COL_block_calc_display_fo
                        _REDRAW()
                        self.active_element = block0

                    if block0.modal(): return
                elif self.w.area_button.box_area.inbox(MOUSE):
                    block0 = self.w.area_button.item
                    if self.active_element != block0:

                        Admin.TAG_CURSOR = 'DEFAULT'
                        if self.active_element is not None: self.active_element.outside_evt()
                        self.active_element = block0

                    if block0.modal(): return
                elif self.w.area_tab.box_area.inbox(MOUSE):
                    block0 = self.w.area_tab
                    if self.active_element != block0:

                        Admin.TAG_CURSOR = 'DEFAULT'
                        if self.active_element is not None: self.active_element.outside_evt()
                        self.active_element = block0
                    #|
                    if block0.box_text.inbox(MOUSE):
                        if block0.box_text.color != COL_box_text_active:
                            block0.box_text.color = COL_box_text_active
                            _REDRAW()
                        hover = block0.box_match_hover

                        if block0.blf_text.unclip_text:
                            if MOUSE[0] >= block0.box_match_case.L:
                                ind = block0.r_box_match_index()

                                if TRIGGER['click']():
                                    tx = block0.blf_text.unclip_text
                                    if ind == 0:
                                        block0.evt_toggle_match_case(tx)
                                        self.set_active_index_callback()
                                    elif ind == 1:
                                        block0.evt_toggle_match_whole_word(tx)
                                        self.set_active_index_callback()
                                    else:
                                        block0.evt_toggle_match_end(tx)
                                        self.set_active_index_callback()
                                    return
                            else:
                                box_icon_search = block0.box_icon_search
                                if MOUSE[0] < box_icon_search.R:
                                    if hover.L == box_icon_search.L and hover.R == box_icon_search.R and hover.B == box_icon_search.B and hover.T == box_icon_search.T: pass
                                    else:
                                        hover.LRBT_upd(box_icon_search.L, box_icon_search.R, box_icon_search.B, box_icon_search.T)
                                        _REDRAW()

                                    if TRIGGER['click']():
                                        block0.evt_area_del_text()
                                        self.set_active_index_callback()
                                        return
                                else:
                                    if hover.L == 0 and hover.R == 0: pass
                                    else:
                                        hover.LRBT_upd(0, 0, 0, 0)
                                        _REDRAW()

                                    if TRIGGER['rm']():
                                        self.to_tab_rm(block0)
                                        return
                                    if TRIGGER['click']():
                                        self.to_tab_dd(block0)
                                        return
                        else:
                            if hover.L == 0 and hover.R == 0: pass
                            else:
                                hover.LRBT_upd(0, 0, 0, 0)
                                _REDRAW()

                            if TRIGGER['rm']():
                                self.to_tab_rm(block0)
                                return
                            if TRIGGER['click']():
                                self.to_tab_dd(block0)
                                return
                    elif block0.filt.box_scroll_bg.inbox(MOUSE):
                        if block0.box_text.color != COL_box_text:
                            block0.box_text.color = COL_box_text
                            _REDRAW()

                        hover = block0.box_match_hover
                        if hover.L == 0 and hover.R == 0: pass
                        else:
                            hover.LRBT_upd(0, 0, 0, 0)
                            _REDRAW()

                        hover = block0.filt.box_hover
                        if hover.L == 0 and hover.R == 0: pass
                        else:
                            hover.LRBT_upd(0, 0, 0, 0)
                            _REDRAW()

                        # <<< 1copy (0area_AreaFilterY_i_modal_scroll,, ${'self.':'block0.'}$)
                        # <<< 1copy (0area_AreaFilterY_filter_evt,, $$)
                        if TRIGGER['dd_scroll_left_most']():
                            block0.filt.evt_scrollX(block0.filt.r_blfs_width())
                            return True
                        if TRIGGER['dd_scroll_right_most']():
                            block0.filt.evt_scrollX(-block0.filt.r_blfs_width())
                            return True
                        if TRIGGER['dd_scroll_down_most']():
                            block0.filt.evt_scrollY(len(block0.filt.items) * D_SIZE['widget_full_h'])
                            return True
                        if TRIGGER['dd_scroll_up_most']():
                            block0.filt.evt_scrollY(-len(block0.filt.items) * D_SIZE['widget_full_h'])
                            return True
                        if TRIGGER['dd_scroll_left']():
                            block0.filt.evt_scrollX(P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_right']():
                            block0.filt.evt_scrollX(-P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_down']():
                            block0.filt.evt_scrollY(P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_up']():
                            block0.filt.evt_scrollY(-P.scroll_distance)
                            return True
                        if TRIGGER['dd_beam_down']():
                            block0.evt_beam_down()
                            return True
                        if TRIGGER['dd_beam_up']():
                            block0.evt_beam_up()
                            return True
                        # >>>

                        if TRIGGER['dd_scroll_left_area']():
                            block0.filt.evt_scrollX(P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_right_area']():
                            block0.filt.evt_scrollX(-P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_down_area']():
                            block0.filt.evt_scrollY(P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_up_area']():
                            block0.filt.evt_scrollY(-P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll']():
                            block0.to_modal_scrollbar()
                            return True
                        if TRIGGER['pan']():
                            block0.filt.to_modal_pan()
                            return True
                        # >>>
                    else:
                        if block0.box_text.color != COL_box_text:
                            block0.box_text.color = COL_box_text
                            _REDRAW()

                        hover = block0.box_match_hover
                        if hover.L == 0 and hover.R == 0: pass
                        else:
                            hover.LRBT_upd(0, 0, 0, 0)
                            _REDRAW()

                        i = block0.upd_filter_hover()
                        # <<< 1copy (0area_AreaFilterY_filter_evt,, ${'self.':'block0.'}$)
                        if TRIGGER['dd_scroll_left_most']():
                            block0.filt.evt_scrollX(block0.filt.r_blfs_width())
                            return True
                        if TRIGGER['dd_scroll_right_most']():
                            block0.filt.evt_scrollX(-block0.filt.r_blfs_width())
                            return True
                        if TRIGGER['dd_scroll_down_most']():
                            block0.filt.evt_scrollY(len(block0.filt.items) * D_SIZE['widget_full_h'])
                            return True
                        if TRIGGER['dd_scroll_up_most']():
                            block0.filt.evt_scrollY(-len(block0.filt.items) * D_SIZE['widget_full_h'])
                            return True
                        if TRIGGER['dd_scroll_left']():
                            block0.filt.evt_scrollX(P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_right']():
                            block0.filt.evt_scrollX(-P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_down']():
                            block0.filt.evt_scrollY(P.scroll_distance)
                            return True
                        if TRIGGER['dd_scroll_up']():
                            block0.filt.evt_scrollY(-P.scroll_distance)
                            return True
                        if TRIGGER['dd_beam_down']():
                            block0.evt_beam_down()
                            return True
                        if TRIGGER['dd_beam_up']():
                            block0.evt_beam_up()
                            return True
                        # >>>

                        if TRIGGER['pan']():
                            block0.filt.to_modal_pan()
                            return
                        if TRIGGER['click']():
                            if i is None: pass
                            elif 0 <= i < len(block0.filt.match_items) and i != block0.filt.active_index:
                                block0.filt.set_active_index(i)
                                self.set_active_index_callback()
                            return
                    #|
                elif MOUSE[1] > _box_win.title_B:
                    if self.active_element != None:

                        Admin.TAG_CURSOR = 'DEFAULT'
                        if self.active_element is not None: self.active_element.outside_evt()
                        self.active_element = None

                    if TRIGGER['title_move']():
                        self.w.to_modal_move()
                        return
            else:
                if self.active_element != None:
                    Admin.TAG_CURSOR = 'DEFAULT'

                    if self.active_element is not None: self.active_element.outside_evt()
                    self.active_element = None

                if TRIGGER['dd_confirm_area']():
                    _temp[0] = None
                    w_head.fin()
                    return

            block0 = self.w.area_tab
            # <<< 1copy (0area_AreaFilterY_filter_evt,, ${'self.':'block0.'}$)
            if TRIGGER['dd_scroll_left_most']():
                block0.filt.evt_scrollX(block0.filt.r_blfs_width())
                return True
            if TRIGGER['dd_scroll_right_most']():
                block0.filt.evt_scrollX(-block0.filt.r_blfs_width())
                return True
            if TRIGGER['dd_scroll_down_most']():
                block0.filt.evt_scrollY(len(block0.filt.items) * D_SIZE['widget_full_h'])
                return True
            if TRIGGER['dd_scroll_up_most']():
                block0.filt.evt_scrollY(-len(block0.filt.items) * D_SIZE['widget_full_h'])
                return True
            if TRIGGER['dd_scroll_left']():
                block0.filt.evt_scrollX(P.scroll_distance)
                return True
            if TRIGGER['dd_scroll_right']():
                block0.filt.evt_scrollX(-P.scroll_distance)
                return True
            if TRIGGER['dd_scroll_down']():
                block0.filt.evt_scrollY(P.scroll_distance)
                return True
            if TRIGGER['dd_scroll_up']():
                block0.filt.evt_scrollY(-P.scroll_distance)
                return True
            if TRIGGER['dd_beam_down']():
                block0.evt_beam_down()
                return True
            if TRIGGER['dd_beam_up']():
                block0.evt_beam_up()
                return True
            # >>>

            if TRIGGER['area_active_down_most']():
                block0.evt_active_down_most()
                return
            if TRIGGER['area_active_up_most']():
                block0.evt_active_up_most()
                return
            if TRIGGER['area_active_down']():
                block0.evt_active_down()
                return
            if TRIGGER['area_active_up']():
                block0.evt_active_up()
                return

            _text_evt()
            #|

        w_head = Head(self, modal_dd, self.end_modal_dd)
        w_head.data = {
            'text': blf_text.text,
            'unclip_text': blf_text.unclip_text}

        P_cursor_beam_time = P.cursor_beam_time
        # <<< 1copy (0area_to_modal_dd_callfrom_dd_check,, $$)
        if timer_isreg(timer_beam):

            self.dd_parent = SELF
            if hasattr(SELF, "kill_push_timer"): SELF.kill_push_timer()
        else:
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
            self.dd_parent = None
        # >>>
        SELF = self

        if self.box_text.inbox(MOUSE): Admin.TAG_CURSOR = 'TEXT'

        blf_text.text = blf_text.unclip_text
        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + floor(blfDimen(FONT0, blf_text.text)[0])
        self.box_beam.L = L
        self.box_beam.R = L + SIZE_widget[1]
        self.box_beam.upd()

        if select_all is None: select_all = P.use_select_all
        if select_all: self.evt_select_all()
        self.local_history = LocalHistory(self, P.undo_steps_local, self.r_push_item)
        return w_head
        #|
    def end_modal_dd(self):
        # <<< 1copy (0area_SELF_to_top_level,, $$)
        if self.dd_parent == None:
            if timer_isreg(timer_beam):
                timer_unreg(timer_beam)

            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

        else:
            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

            self.dd_parent.fin_callfront_set_parent()
        # >>>

        Admin.TAG_CURSOR = 'DEFAULT'
        Admin.REDRAW()
        kill_evt_except()
        self.local_history.kill()

        blf_text = self.blf_text

        if _temp[0] == None:
            use_text_output = True
        else:

            use_text_output = None

        if hasattr(self.w, 'callback_end_modal_dd'):
            self.w.callback_end_modal_dd({'use_text_output': use_text_output})
        #|

    def outside_evt(self):
        e = self.box_match_hover
        if e.L == e.R: pass
        else:
            Admin.REDRAW()
            e.LRBT_upd(0, 0, 0, 0)
        #|

    def to_tab_dd(self, block0):

        DropDownValTab(self, block0)
        #|
    def to_tab_rm(self, block0):

        def fn_paste():
            block0.evt_area_paste()
            block0.blf_text.text = ""
            self.set_active_index_callback()
        def fn_clear():
            block0.evt_area_del_text()
            self.set_active_index_callback()
        def fn_cut():
            block0.evt_area_cut()
            self.set_active_index_callback()

        DropDownRM(block0, MOUSE, [
            NameValue("Copy", block0.evt_area_copy),
            NameValue("Paste", fn_paste),
            NameValue("Cut", fn_cut),
            NameValue("Clear", fn_clear),
        ], None)
        #|

    def set_active_index_callback(self, **kw):

        filt = self.w.area_tab.filt
        if filt.active_index == None: return
        e = filt.match_items[filt.active_index]
        self.w.area_button.item.update_buttons(e.name)
        #|

    def r_text_limL(self):
        return self.box_text.L + D_SIZE['font_main_dx']
        #|
    def r_text_limR(self, tx_limL, beam_width):
        return min(self.box_icon_py.L - D_SIZE['font_main_dx'] - beam_width
            - floor(blfDimen(FONT0, self.blf_text.text)[0]), tx_limL)
        #|

    def evt_toggle_match_end(self): self.evt_toggle_exp()
    def evt_toggle_match_case(self): self.evt_toggle_exp()
    def evt_toggle_match_whole_word(self): self.evt_toggle_exp()
    def evt_beam_down(self):
        filt = self.w.area_tab.filt
        ind = filt.active_index
        filt.set_active_index(0  if ind == None else ind + 1)
        #|
    def evt_beam_up(self):
        filt = self.w.area_tab.filt
        ind = filt.active_index
        filt.set_active_index(0  if ind == None else ind - 1)
        #|
    def evt_toggle_exp(self):

        if self.use_py_exp == True:
            self.box_icon_py.__class__ = GpuImg_py_exp_off
            self.box_icon_py.upd()
            self.use_py_exp = False
        else:
            e = self.box_match_hover
            if e.L == e.R: pass
            else:
                Admin.REDRAW()
                e.LRBT_upd(0, 0, 0, 0)

            self.box_icon_py.__class__ = GpuImg_py_exp_on
            self.box_icon_py.upd()
            self.use_py_exp = True

        kill_evt_except()
        Admin.REDRAW()
        #|

    def get_clamped_int(self, z, hard_min, hard_max):
        if isinstance(z, complex): z = abs(z)
        z = min(max(hard_min, z), hard_max)
        return int(round_dec(z, 0))
        #|
    def get_clamped_float(self, z, hard_min, hard_max):
        if isinstance(z, complex): z = abs(z)
        return float(min(max(hard_min, z), hard_max))
        #|
    def calc_text(self, use_py_exp=None):

        s = self.blf_text.text.strip()
        if not s: return

        if use_py_exp == None: use_py_exp = self.use_py_exp

        Admin.REDRAW()
        s0 = s[0]
        w = self.w
        data = w.data
        rna = data["rna"]
        if hasattr(rna, "hard_min"):
            hard_min = rna.hard_min
            hard_max = rna.hard_max
        else:
            hard_min = rna.min_value
            hard_max = rna.max_value
        area_display = w.area_display
        display_text = area_display.item.blf_title
        display_info = area_display.item.blf_info

        data["last_input"] = s

        if s0 == "#":
            display_info[0].text = ""
            display_info[1].text = ""
            if hasattr(rna, "min_value") or (hasattr(rna, "is_animatable") and rna.is_animatable):
                display_text.text = "Confirm to add driver"
                return s
            else:
                display_text.text = "This property cannot be animated"
            return display_text.text
        elif s0 == ";":
            s = s[1 : ]
            use_py_exp = True

        def error_message(tx):
            display_text.text = tx
            display_info[0].text = ""
            display_info[1].text = ""
            return tx
            #|
        def upd_display_info(z):
            if isinstance(hard_min, int):
                v_py = self.get_clamped_int(z, hard_min, hard_max)
                display_info[0].text = f'Clamped :  {value_to_display(v_py)}'
                display_info[1].text = ""
                return v_py
            else:
                if w.same_as_py_value:
                    v_py = self.get_clamped_float(z, hard_min, hard_max)
                    display_info[0].text = f'Clamped :  {value_to_display(v_py)}'
                    display_info[1].text = ""
                    return v_py

                unit_factor = r_unit_factor((rna.unit  if hasattr(rna, "unit") else D_gn_subtype_unit[rna.subtype]), data["text_format"])
                v_py = self.get_clamped_float(z * unit_factor, hard_min, hard_max)
                display_info[0].text = f'Clamped :  {value_to_display(v_py / unit_factor)}'
                display_info[1].text = f'Python : {value_to_display(v_py)}'
                return v_py

            return "None"
            #|

        calc = self.calc

        if use_py_exp:
            unit = rna.unit  if hasattr(rna, "unit") else D_gn_subtype_unit[rna.subtype]
            if unit == "ROTATION" and w.data["text_format"].__name__.find("deg") == -1:
                v = units_to_value("NONE", "ROTATION", s, str_ref_unit="radians")
            else:
                v = calc_py_exp(tran_unit(s, calc.unit_system, calc.unit_length, unit))

            if v == None: return error_message("Evaluate fail")
            elif is_value(v):
                self.calc.ans_flo = v
                display_text.text = complex_to_display(v)
                return upd_display_info(v)
            else: return error_message(str(v))
        else:
            calc.calc(s)
            v = calc.ans_flo
            if isinstance(calc.ans_tx, str):
                display_text.text = calc.ans_tx
                display_info[0].text = ""
                display_info[1].text = ""
                return calc.ans_tx
            if v == None: return error_message("Evaluate fail")
            elif is_value(v):
                display_text.text = complex_to_display(v)
                return upd_display_info(v)
            else: return error_message(str(v))
        #|

    def dxy(self, dx, dy):
        for e in self.boxes: e.dxy_upd(dx, dy)

        self.blf_text.x += dx
        self.blf_text.y += dy

        box_text = self.box_text
        self.scissor_text_box.intersect_with(self.w.scissor, box_text.inner[0],
            self.box_icon_py.L - D_SIZE['font_main_dy'], box_text.B, box_text.T)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        boxes = self.boxes
        boxes[0].bind_draw()
        boxes[1].bind_draw()
        self.box_match_hover.bind_draw()
        self.box_icon_py.bind_draw()

        self.scissor_text_box.use()
        self.box_selection.bind_draw()
        self.box_beam.bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        blend_set('ALPHA')
        self.w.scissor.use()
        #|

    def upd_data(self): pass
    #|
    #|
class CalcFilt:
    __slots__ = (
        'w')

    def __init__(self, w):
        self.w = w
        #|

    def filter_text(self, s, active_index=0): pass
    #|
    #|

class AreaFilterYDropDownRMKeymap(AreaFilterY):
    __slots__ = ()

    def i_modal_dd_filt_submodal(self, i):
        if TRIGGER['rm']():
            self.fn_filt_rm(i)
            return True
        if TRIGGER['rm_km_change']():
            if i != None and i < len(self.filt.match_items):
                if self.filt.match_items[i].identifier in BL_RNA_PROP_keymaps:
                    self.evt_km_change(self.filt.match_items[i].identifier)
                    return True
        if TRIGGER['rm_km_toggle']():
            self.evt_km_toggle()
            return True
        return False
        #|

    def evt_km_change(self, identifier):

        m.D_EDITOR["SettingEditor"].open_search(identifier)
        #|
    def evt_km_toggle(self):

        kill_evt_except()
        Admin.REDRAW()
        filt = self.filt
        filt.get_info = rm_get_info_km  if filt.get_info == None else None
        filt.filter_text(self.blf_text.text, filt.active_index)
        #|
    def fn_filt_rm(self, i):
        self.kill_push_timer()

        items = []
        if i != None and i < len(self.filt.match_items):
            if self.filt.match_items[i].identifier in BL_RNA_PROP_keymaps:
                items.append(("rm_km_change", lambda: self.evt_km_change(self.filt.match_items[i].identifier)))

        items.append(("rm_km_toggle", self.evt_km_toggle))
        DropDownRMKeymap(self, MOUSE, items, override_icon={"rm_km_change": GpuImg_settings_keymap_addon_key})
        #|
    #|
    #|
class AreaFilterYDropDownEnumPointer(AreaFilterY):
    __slots__ = ()

    def i_modal_dd_filt_submodal(self, i):
        if TRIGGER['dd_preview']():
            self.w.data["init_index"] = i
            self.evt_filt_preview()
            return True
        return False
        #|

    def evt_filt_preview(self):

        kill_evt_except()
        w = self.w
        if "init_index" in w.data:
            i = w.data["init_index"]
            if i is None: return

            try: datablock = self.filt.match_items[i]
            except: return

            preview_datablock(datablock)
        #|
    #|
    #|

class AreaString(AreaFilterY):
    __slots__ = ()

    def __init__(self, w, LL, RR, BB, TT, input_text=""):
        super().__init__(w, LL, RR, BB, TT, lambda: [], is_dropdown=True, input_text=input_text)
        #|

    def upd_size(self, LL, RR, BB, TT):
        box_area = self.box_area
        # old_L = box_area.L
        # old_T = box_area.T
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        # d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]
        scissor_win = self.w.scissor

        LL += d0
        RR -= d0
        TT -= d0
        BB += d0

        box_text = self.box_text
        blf_text = self.blf_text

        B = TT - D_SIZE['widget_full_h']
        box_text.LRBT_upd(LL, RR, B, TT, widget_rim)

        L, R, B, T = box_text.inner

        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L + D_SIZE['font_main_dx']
        blf_text.y = B + D_SIZE['font_main_dy']

        self.filt = CalcFilt(self)

        self.scissor_text_box.intersect_with(scissor_win, L, R, box_text.B, box_text.T)
        #|

    def upd_scissor_text_box(self, scissor_win):
        self.scissor_text_box.intersect_with(scissor_win, self.box_text.inner[0],
            self.box_text.inner[1], self.box_text.B, self.box_text.T)
        #|

    def to_modal_dd(self, select_all=None):

        #|
        global SELF, P_cursor_beam_time
        Admin.REDRAW()
        blf_text = self.blf_text
        box_text = self.box_text
        box_text.color = COL_box_text_active

        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _TRIGGER_dd_esc = TRIGGER['dd_esc']
        _TRIGGER_dd_confirm = TRIGGER['dd_confirm']
        _TRIGGER_dd_confirm_area = TRIGGER['dd_confirm_area']
        _box_text_inbox = box_text.inbox
        _box_area_inbox = self.box_area.inbox
        _text_evt = self.text_evt

        def modal_dd():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or _TRIGGER_dd_esc():
                _temp[0] = w_head.data
                w_head.fin()
                return

            if _TRIGGER_dd_confirm():
                _temp[0] = None
                w_head.fin()
                return

            if _box_text_inbox(MOUSE):
                if TRIGGER['rm']():
                    self.to_modal_dd_rm()
                    return

            if _box_area_inbox(MOUSE) == False:
                if _TRIGGER_dd_confirm_area():
                    _temp[0] = None
                    w_head.fin()
                    return

            _text_evt()
            #|

        w_head = Head(self, modal_dd, self.end_modal_dd)
        w_head.data = {'text': blf_text.unclip_text}

        P_cursor_beam_time = P.cursor_beam_time
        # <<< 1copy (0area_to_modal_dd_callfrom_dd_check,, $$)
        if timer_isreg(timer_beam):

            self.dd_parent = SELF
            if hasattr(SELF, "kill_push_timer"): SELF.kill_push_timer()
        else:
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
            self.dd_parent = None
        # >>>
        SELF = self
        Admin.TAG_CURSOR = 'TEXT'

        blf_text.x = box_text.inner[0] + D_SIZE['font_main_dx']
        blf_text.text = blf_text.unclip_text
        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + floor(blfDimen(FONT0, blf_text.text)[0])
        self.box_beam.L = L
        self.box_beam.R = L + SIZE_widget[1]
        self.box_beam.upd()

        if select_all is None: select_all = P.use_select_all
        if select_all: self.evt_select_all()
        self.local_history = LocalHistory(self, P.undo_steps_local, self.r_push_item)
        return w_head
        #|
    def end_modal_dd(self):
        # <<< 1copy (0area_SELF_to_top_level,, $$)
        if self.dd_parent == None:
            if timer_isreg(timer_beam):
                timer_unreg(timer_beam)

            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

        else:
            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

            self.dd_parent.fin_callfront_set_parent()
        # >>>

        Admin.TAG_CURSOR = 'DEFAULT'
        Admin.REDRAW()
        kill_evt_except()

        blf_text = self.blf_text

        if _temp[0] == None:
            use_text_output = True
        else:

            use_text_output = None
            data = _temp[0]
            blf_text.text = data["text"]

        self.box_text.color = COL_box_text
        self.box_beam.L = self.box_beam.R = 0
        self.box_beam.upd()
        self.box_selection.L = self.box_selection.R = 0
        self.box_selection.upd()
        blf_text.unclip_text = blf_text.text
        self.local_history.kill()

        if hasattr(self.w, 'callback_end_modal_dd'):
            self.w.callback_end_modal_dd({
                'use_text_output': use_text_output,
            })
        #|

    def to_modal_dd_rm(self):

        self.kill_push_timer()

        DropDownRMKeymap(self, MOUSE, [
            # <<< 1ifmatchindex (0area_AreaFilterY_text_evt, 12,
            # $lambda ls, r: (f'("{ls[r][ls[r].find("[") + 2 : ls[r].find("]") - 1
            #     ]}", self.{ls[r+1][ls[r+1].find("self.") + 5 : ls[r+1].find("()")]}),\n', True
            #     )  if ls[r][ls[r].find("[") + 2 : ls[r].find("]") - 1].find("dd_match_") == -1 else ('', False)$,
            # $$,
            # ${'TRIGGER'}$)
            ("redo", self.evt_redo),
            ("undo", self.evt_undo),
            ("dd_select_all", self.evt_select_all),
            ("dd_select_word", self.evt_select_word),
            ("dd_cut", self.evt_cut),
            ("dd_paste", self.evt_paste),
            ("dd_copy", self.evt_copy),
            ("dd_del_all", self.evt_del_all),
            ("dd_del", self.evt_del_line),
            ("dd_del_word", self.evt_del_word),
            ("dd_del_chr", self.evt_del_chr),
            ("dd_beam_line_begin_shift", self.evt_beam_line_begin_shift),
            ("dd_beam_line_end_shift", self.evt_beam_line_end_shift),
            ("dd_beam_left_word_shift", self.evt_beam_left_word_shift),
            ("dd_beam_right_word_shift", self.evt_beam_right_word_shift),
            ("dd_beam_left_shift", self.evt_beam_left_shift),
            ("dd_beam_right_shift", self.evt_beam_right_shift),
            ("dd_beam_down_shift", self.evt_beam_down_shift),
            ("dd_beam_up_shift", self.evt_beam_up_shift),
            ("dd_beam_line_begin", self.evt_beam_line_begin),
            ("dd_beam_line_end", self.evt_beam_line_end),
            ("dd_beam_left_word", self.evt_beam_left_word),
            ("dd_beam_right_word", self.evt_beam_right_word),
            ("dd_beam_left", self.evt_beam_left),
            ("dd_beam_right", self.evt_beam_right),
            ("dd_beam_down", self.evt_beam_down),
            ("dd_beam_up", self.evt_beam_up),
            ("dd_beam_end_shift", self.evt_beam_end_shift),
            ("dd_beam_start_shift", self.evt_beam_start_shift),
            ("dd_beam_end", self.evt_beam_end),
            ("dd_beam_start", self.evt_beam_start),
            ("pan", self.to_modal_pan_text),
            ("dd_selection_shift", self.to_modal_selection_shift),
            ("dd_selection", self.to_modal_selection),
            ("dd_linebreak", self.evt_linebreak),
            ("dd_untab", self.evt_untab),
            ("dd_tab", self.evt_tab),
            # >>>
        ])
        #|
    def fin_callfront_set_parent(self):
        super().fin_callfront_set_parent()
        Admin.TAG_CURSOR = 'TEXT'

    def evt_toggle_match_end(self): pass
    def evt_toggle_match_case(self): pass
    def evt_toggle_match_whole_word(self): pass
    def evt_beam_down(self): self.evt_beam_end()
    def evt_beam_up(self): self.evt_beam_start()
    def evt_tab(self): pass

    def outside_evt(self): pass
    def resize_upd_end(self): pass

    def dxy(self, dx, dy):
        for e in self.boxes: e.dxy_upd(dx, dy)

        self.blf_text.x += dx
        self.blf_text.y += dy

        box_text = self.box_text
        L, R, B, T = box_text.inner
        self.scissor_text_box.intersect_with(self.w.scissor, L, R, box_text.B, box_text.T)
        #|

    def r_text_limL(self): return self.box_text.inner[0] + D_SIZE['font_main_dx']
    def r_text_limR(self, tx_limL, beam_width):
        return min(self.box_text.inner[1] - D_SIZE['font_main_dx'] - beam_width
            - floor(blfDimen(FONT0, self.blf_text.text)[0]), tx_limL)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        self.box_text.bind_draw()

        self.scissor_text_box.use()
        self.box_selection.bind_draw()
        self.box_beam.bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        self.w.scissor.use()
        #|

    def upd_data(self): pass
    #|
    #|
class AreaStringPre:
    __slots__ = (
        'w',
        'timer_beam_off_reg',
        'timer_selection_off_reg',
        'blf_text',
        'text_color',
        'r_button_width',
        'box_button',
        'box_selection',
        'box_beam',
        'beam_index',
        'init_bat',
        'draw_box',
        'dxy',
        'inside')

    def __init__(self, w, input_text=""):
        self.timer_beam_off_reg = None
        self.timer_selection_off_reg = None

        self.w = w
        self.blf_text = Blf(input_text)
        self.blf_text.color = COL_box_text_fg
        self.text_color = COL_box_text_fg

        self.box_button = GpuBox()
        self.box_selection = GpuBox(COL_box_text_selection)
        self.box_beam = GpuBox(COL_box_cursor_beam)
        self.beam_index = [0, 0]

        self.init_bat = self.init_bat_L
        self.inside = self.box_button.inbox
        self.dxy = self.i_dxy
        #|

    def init_bat_L(self, LL, RR, TT):
        self.draw_box = N
        self.dxy = self.i_dxy
        self.beam_index[:] = 0, 0

        if hasattr(self, "r_button_width"):
            RR -= self.r_button_width()

        self.blf_text.x = LL + D_SIZE['font_main_title_offset']

        self.blf_text.y = TT - SIZE_border[3] - D_SIZE['font_main_dT']
        B = TT - D_SIZE['widget_full_h']
        self.box_button.LRBT(LL, RR, B, TT)
        return B
        #|

    def r_height(self, width):
        return D_SIZE['widget_full_h']
        #|

    def dark(self):
        self.blf_text.color = COL_block_fg_ignore
        #|
    def light(self):
        self.blf_text.color = self.text_color
        #|

    def inside_evt(self): pass
    def outside_evt(self): pass
    def set_text(self, text):
        self.blf_text.text = text
        self.draw_box = N
        self.dxy = self.i_dxy
        self.beam_index[:] = 0, 0
        #|

    def modal(self):
        if TRIGGER['rm']():
            self.to_modal_rm()
            return True

        # /* 0defAreaStringPre_modal
        if TRIGGER['dd_select_all']():
            self.evt_select_all()
            return True
        if TRIGGER['dd_select_word']():
            self.evt_select_word()
            return True
        if TRIGGER['dd_cut']():
            self.evt_cut()
            return True
        if TRIGGER['dd_copy']():
            self.evt_copy()
            return True
        if TRIGGER['dd_beam_line_begin_shift']():
            self.evt_beam_line_begin_shift()
            return True
        if TRIGGER['dd_beam_line_end_shift']():
            self.evt_beam_line_end_shift()
            return True
        if TRIGGER['dd_beam_left_word_shift']():
            self.evt_beam_left_word_shift()
            return True
        if TRIGGER['dd_beam_right_word_shift']():
            self.evt_beam_right_word_shift()
            return True
        if TRIGGER['dd_beam_left_shift']():
            self.evt_beam_left_shift()
            return True
        if TRIGGER['dd_beam_right_shift']():
            self.evt_beam_right_shift()
            return True
        if TRIGGER['dd_beam_down_shift']():
            self.evt_beam_down_shift()
            return True
        if TRIGGER['dd_beam_up_shift']():
            self.evt_beam_up_shift()
            return True
        if TRIGGER['dd_beam_line_begin']():
            self.evt_beam_line_begin()
            return True
        if TRIGGER['dd_beam_line_end']():
            self.evt_beam_line_end()
            return True
        if TRIGGER['dd_beam_left_word']():
            self.evt_beam_left_word()
            return True
        if TRIGGER['dd_beam_right_word']():
            self.evt_beam_right_word()
            return True
        if TRIGGER['dd_beam_left']():
            self.evt_beam_left()
            return True
        if TRIGGER['dd_beam_right']():
            self.evt_beam_right()
            return True
        if TRIGGER['dd_beam_down']():
            self.evt_beam_down()
            return True
        if TRIGGER['dd_beam_up']():
            self.evt_beam_up()
            return True
        if TRIGGER['dd_beam_end_shift']():
            self.evt_beam_end_shift()
            return True
        if TRIGGER['dd_beam_start_shift']():
            self.evt_beam_start_shift()
            return True
        if TRIGGER['dd_beam_end']():
            self.evt_beam_end()
            return True
        if TRIGGER['dd_beam_start']():
            self.evt_beam_start()
            return True
        if TRIGGER['dd_selection_shift']():
            self.to_modal_selection_shift()
            return True
        if TRIGGER['dd_selection']():
            self.to_modal_selection()
            return True
        # */

    def to_modal_rm(self):


        DropDownRMKeymap(self, MOUSE, [
            # <<< 1ifmatchindex (0defAreaStringPre_modal, 12,
            # $lambda ls, r: (f'("{ls[r][ls[r].find("[") + 2 : ls[r].find("]") - 1
            #     ]}", self.{ls[r+1][ls[r+1].find("self.") + 5 : ls[r+1].find("()")]}),\n', True
            #     )  if ls[r][ls[r].find("[") + 2 : ls[r].find("]") - 1].find("dd_match_") == -1 else ('', False)$,
            # $$,
            # ${'TRIGGER'}$)
            ("dd_select_all", self.evt_select_all),
            ("dd_select_word", self.evt_select_word),
            ("dd_cut", self.evt_cut),
            ("dd_copy", self.evt_copy),
            ("dd_beam_line_begin_shift", self.evt_beam_line_begin_shift),
            ("dd_beam_line_end_shift", self.evt_beam_line_end_shift),
            ("dd_beam_left_word_shift", self.evt_beam_left_word_shift),
            ("dd_beam_right_word_shift", self.evt_beam_right_word_shift),
            ("dd_beam_left_shift", self.evt_beam_left_shift),
            ("dd_beam_right_shift", self.evt_beam_right_shift),
            ("dd_beam_down_shift", self.evt_beam_down_shift),
            ("dd_beam_up_shift", self.evt_beam_up_shift),
            ("dd_beam_line_begin", self.evt_beam_line_begin),
            ("dd_beam_line_end", self.evt_beam_line_end),
            ("dd_beam_left_word", self.evt_beam_left_word),
            ("dd_beam_right_word", self.evt_beam_right_word),
            ("dd_beam_left", self.evt_beam_left),
            ("dd_beam_right", self.evt_beam_right),
            ("dd_beam_down", self.evt_beam_down),
            ("dd_beam_up", self.evt_beam_up),
            ("dd_beam_end_shift", self.evt_beam_end_shift),
            ("dd_beam_start_shift", self.evt_beam_start_shift),
            ("dd_beam_end", self.evt_beam_end),
            ("dd_beam_start", self.evt_beam_start),
            ("dd_selection_shift", self.to_modal_selection_shift),
            ("dd_selection", self.to_modal_selection),
            # >>>
        ])
        #|

    def to_modal_selection(self, shift=False):

        #|
        _blfSize = blfSize
        _FONT0 = FONT0
        _font_main = D_SIZE['font_main']
        _blfSize(_FONT0, _font_main)
        _blf_text = self.blf_text
        _beam_index = self.beam_index
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _r_blf_ind = r_blf_ind
        _set_highlight = self.set_highlight

        if shift is False:
            end_trigger = r_end_trigger('dd_selection')
            self.evt_beam_move_x(_r_blf_ind(_blf_text.text, _blf_text.x, MOUSE[0]) - _beam_index[1], evtkill=False)
        else:
            end_trigger = r_end_trigger('dd_selection_shift')
            self.evt_beam_shift_x(_r_blf_ind(_blf_text.text, _blf_text.x, MOUSE[0]) - _beam_index[1], evtkill=False)

        def modal_selection():
            _REDRAW()

            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            _blfSize(_FONT0, _font_main)
            _set_highlight(_beam_index[0], _r_blf_ind(_blf_text.text, _blf_text.x, MOUSE[0]))
            #|

        w_head = Head(self, modal_selection)
        _REDRAW()
        #|
    def to_modal_selection_shift(self):

        self.to_modal_selection(shift=True)
        #|

    def evt_select_all(self, override=None):
        self.reg_timer_beam_off()
        # <<< 1copy (0defarea_AreaFilterY_evt_select_all,, $$)
        Admin.REDRAW()
        i0, i1 = self.beam_index
        if override == None:
            ibeam = i1
            if i0 > i1: i0, i1 = i1, i0
            if i0 == 0 and i1 == len(self.blf_text.text):
                self.set_highlight(ibeam, ibeam)
            else:
                self.set_highlight(0, len(self.blf_text.text))
        else:
            if override:
                self.set_highlight(0, len(self.blf_text.text))
            else:
                self.set_highlight(i1, i1)

        self.check_cursor_pos()
        self.upd_highlight()
        kill_evt_except()
        # >>>

        #|
    def evt_select_word(self):
        self.reg_timer_beam_off()
        # <<< 1copy (0defarea_AreaFilterY_evt_select_word,, $$)
        Admin.REDRAW()
        s = self.blf_text.text
        if not s: return
        self.set_highlight(*r_word_select_index(s, self.beam_index[1]))

        self.check_cursor_pos()
        self.upd_highlight()
        kill_evt_except()
        # >>>
        #|
    def evt_cut(self): self.evt_copy()
    def evt_copy(self):
        i0, i1 = self.beam_index
        if i0 == i1: return
        if i0 > i1:
            i0, i1 = i1, i0

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.reg_timer_selection_off()

        bpy.context.window_manager.clipboard = self.blf_text.text[i0 : i1]
        kill_evt_except()
        #|
    def evt_beam_line_begin_shift(self): self.evt_beam_up_shift()
    def evt_beam_line_end_shift(self): self.evt_beam_down_shift()
    def evt_beam_left_word_shift(self):
        self.reg_timer_beam_off()
        # <<< 1copy (0defarea_AreaFilterY_evt_beam_left_word_shift,, $$)
        Admin.REDRAW()
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text[: i1]

        if not s: return
        i = r_prev_word_index(s)
        if i == i1: i -= 1
        if i < 0: i = 0

        self.set_highlight(i0, i)
        self.check_cursor_pos()
        self.upd_highlight()
        # >>>
        #|
    def evt_beam_right_word_shift(self):
        self.reg_timer_beam_off()
        # <<< 1copy (0defarea_AreaFilterY_evt_beam_right_word_shift,, $$)
        Admin.REDRAW()
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text

        if not s: return
        i = r_next_word_index(s, i1)
        if i == i1:
            i += 1
            if i > len(s): i = len(s)

        self.set_highlight(i0, i)
        self.check_cursor_pos()
        self.upd_highlight()
        # >>>
        #|
    def evt_beam_shift_x(self, dx, evtkill=True):

        #|
        if evtkill is True: kill_evt_except()
        blf_text = self.blf_text
        box_beam = self.box_beam
        beam_index = self.beam_index
        i1 = min(max(0, beam_index[1] + dx), len(blf_text.text))
        beam_index[1] = i1

        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + round(blfDimen(FONT0, blf_text.text[: i1])[0])
        box_beam.L = L
        box_beam.R = L + SIZE_widget[1]
        box_beam.B = self.box_button.B + SIZE_border[3]
        box_beam.T = self.box_button.T - SIZE_border[3]
        box_beam.upd()
        self.reg_timer_beam_off()

        self.upd_highlight()
        Admin.REDRAW()
        #|
    def evt_beam_left_shift(self):

        self.evt_beam_shift_x(-1)
        #|
    def evt_beam_right_shift(self):

        self.evt_beam_shift_x(1)
        #|
    def evt_beam_down_shift(self):

        self.evt_beam_shift_x(len(self.blf_text.text))
        #|
    def evt_beam_up_shift(self):

        self.evt_beam_shift_x(- len(self.blf_text.text))
        #|
    def evt_beam_line_begin(self): self.evt_beam_start()
    def evt_beam_line_end(self): self.evt_beam_end()
    def evt_beam_left_word(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text[: i1]

        if not s: return
        i = r_prev_word_index(s)
        if i == i1: i -= 1
        if i < 0: i = 0

        self.set_highlight(i, i)
        self.check_cursor_pos()
        #|
    def evt_beam_right_word(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()
        kill_evt_except()

        i0, i1 = self.beam_index
        tx = self.blf_text
        s = tx.text

        if not s: return
        i = r_next_word_index(s, i1)
        if i == i1:
            i += 1
            if i > len(s): i = len(s)

        self.set_highlight(i, i)
        self.check_cursor_pos()
        #|
    def evt_beam_move_x(self, dx, evtkill=True):

        if evtkill is True: kill_evt_except()
        blf_text = self.blf_text
        box_beam = self.box_beam
        box_selection = self.box_selection
        beam_index = self.beam_index
        i1 = min(max(0, beam_index[1] + dx), len(blf_text.text))
        beam_index[0] = i1
        beam_index[1] = i1

        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + round(blfDimen(FONT0, blf_text.text[: i1])[0])
        box_beam.L = L
        box_beam.R = L + SIZE_widget[1]
        box_beam.B = self.box_button.B + SIZE_border[3]
        box_beam.T = self.box_button.T - SIZE_border[3]
        box_beam.upd()
        box_selection.L = box_selection.R = L
        box_selection.upd()
        Admin.REDRAW()

        self.reg_timer_beam_off()
        self.draw_box = self.i_draw_box
        self.dxy = self.i_dxy_selection
        #|
    def evt_beam_left(self):

        self.evt_beam_move_x(- 1)
        kill_evt_except()
        #|
    def evt_beam_right(self):

        self.evt_beam_move_x(1)
        kill_evt_except()
        #|
    def evt_beam_down(self): self.evt_beam_end()
    def evt_beam_up(self): self.evt_beam_start()
    def evt_beam_end_shift(self): self.evt_beam_down_shift()
    def evt_beam_start_shift(self): self.evt_beam_up_shift()
    def evt_beam_end(self):

        self.evt_beam_move_x(len(self.blf_text.text))
        kill_evt_except()
        #|
    def evt_beam_start(self):

        self.evt_beam_move_x(- len(self.blf_text.text))
        kill_evt_except()
        #|

    def set_highlight(self, i0, i1):
        blfSize(FONT0, D_SIZE['font_main'])
        x = self.blf_text.x

        self.beam_index[:] = i0, i1

        L = x + floor(blfDimen(FONT0, self.blf_text.text[: i0])[0])
        R = x + floor(blfDimen(FONT0, self.blf_text.text[: i1])[0])
        B = self.box_button.B + SIZE_border[3]
        T = self.box_button.T - SIZE_border[3]

        self.box_selection.LRBT_upd(L, R, B, T)
        self.box_beam.LRBT_upd(R, R + SIZE_widget[1], B, T)

        self.draw_box = self.i_draw_box
        self.dxy = self.i_dxy_selection
        #|
    def upd_highlight(self):
        blfSize(FONT0, D_SIZE['font_main'])
        x = self.blf_text.x

        i0, i1 = self.beam_index

        L = x + floor(blfDimen(FONT0, self.blf_text.text[: i0])[0])
        R = x + floor(blfDimen(FONT0, self.blf_text.text[: i1])[0])
        B = self.box_button.B + SIZE_border[3]
        T = self.box_button.T - SIZE_border[3]

        self.box_selection.LRBT_upd(L, R, B, T)
        self.box_beam.LRBT_upd(R, R + SIZE_widget[1], B, T)

        self.draw_box = self.i_draw_box
        self.dxy = self.i_dxy_selection
        #|

    def i_dxy(self, dx, dy):
        self.box_button.dxy(dx, dy)
        self.blf_text.x += dx
        self.blf_text.y += dy
        #|
    def i_dxy_selection(self, dx, dy):
        self.box_button.dxy(dx, dy)
        self.box_selection.dxy_upd(dx, dy)
        self.box_beam.dxy_upd(dx, dy)

        self.blf_text.x += dx
        self.blf_text.y += dy
        #|

    def r_text_limL(self): return self.box_button.L + SIZE_border[3] + D_SIZE['font_main_dx']
    def r_text_limR(self, tx_limL, beam_width):
        return min(self.box_button.R - SIZE_border[3] - D_SIZE['font_main_dx'] - beam_width
            - floor(blfDimen(FONT0, self.blf_text.text)[0]), tx_limL)
        #|
    def check_limL(self):
        # <<< 1copy (0defarea_AreaFilterY_check_limL,, $$)
        tx_limL = self.r_text_limL()

        if self.blf_text.x > tx_limL:
            self.blf_text.x = tx_limL
            self.upd_highlight()
        # >>>
        #|
    def check_limR(self):
        # <<< 1copy (0defarea_AreaFilterY_check_limR,, $$)
        blfSize(FONT0, D_SIZE['font_main'])
        tx_limL = self.r_text_limL()
        tx_limR = self.r_text_limR(tx_limL, 0)

        if self.blf_text.x < tx_limR:
            self.blf_text.x = tx_limR
            self.upd_highlight()
        # >>>
        #|
    def check_cursor_pos(self): pass

    def timer_beam_off(self):

        self.box_beam.color = FLO_0000
        Admin.REDRAW()
        self.timer_beam_off_reg = None
        if self.beam_index[0] == self.beam_index[1]:
            self.draw_box = N
            self.dxy = self.i_dxy
        #|
    def reg_timer_beam_off(self):
        if self.timer_beam_off_reg is not None:
            timer_unreg(self.timer_beam_off_reg)

        self.box_beam.color = COL_box_cursor_beam
        self.timer_beam_off_reg = self.timer_beam_off
        timer_reg(self.timer_beam_off_reg, first_interval=P.cursor_beam_time)
        #|
    def timer_selection_off(self):

        self.box_selection.color = COL_box_text_selection
        Admin.REDRAW()
        self.timer_selection_off_reg = None
        if self.beam_index[0] == self.beam_index[1]:
            self.draw_box = N
            self.dxy = self.i_dxy
        #|
    def reg_timer_selection_off(self):
        if self.timer_selection_off_reg is not None:
            timer_unreg(self.timer_selection_off_reg)

        self.box_selection.color = COL_box_text_selection_off
        self.timer_selection_off_reg = self.timer_selection_off
        timer_reg(self.timer_selection_off_reg, first_interval=0.1)
        #|

    def i_draw_box(self):
        self.box_selection.bind_draw()
        self.box_beam.bind_draw()
        #|
    def draw_blf(self):
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)
        #|

    def upd_data(self): pass
    #|
    #|
class AreaStringXY(AreaString, ScrollEvents):
    __slots__ = (
        'row_count',
        'font_id',
        'font_color',
        'tex',
        'text',
        'headkey',
        'line_x',
        'box_selection1',
        'box_selection2',
        'font_main_dx',
        'font_main_dy',
        'font_main_dT',
        'scroll_width',
        'box_scrollX_bg',
        'box_scrollY_bg',
        'box_scrollX',
        'box_scrollY')

    def __init__(self, w, input_text="", font_id=None):
        self.tex = Text(input_text)
        if font_id is None: font_id = FONT0
        self.w = w
        self.u_draw = self.i_draw
        self.is_dropdown = True
        self.font_id = font_id
        self.font_color = COL_box_text_fg
        self.text = input_text
        self.headkey = 0
        self.line_x = 0
        self.scroll_width = min(SIZE_widget[2], SIZE_widget[0])
        self.readonly = False

        box_area = GpuBox_area()
        box_text = GpuRim(COL_box_text, COL_box_text_rim)
        box_selection = GpuBox(COL_box_text_selection)
        box_selection1 = GpuBox(COL_box_text_selection)
        box_selection2 = GpuBox(COL_box_text_selection)
        box_beam = GpuBox(COL_box_cursor_beam)
        box_scrollX_bg = GpuBox(COL_box_block_scrollbar_bg)
        box_scrollY_bg = GpuBox(COL_box_block_scrollbar_bg)
        box_scrollX = GpuBox(COL_box_block_scrollbar)
        box_scrollY = GpuBox(COL_box_block_scrollbar)

        self.boxes = [
            box_area,
            box_text,
            box_selection,
            box_selection1,
            box_selection2,
            box_beam,
            box_scrollX_bg,
            box_scrollY_bg,
            box_scrollX,
            box_scrollY
        ]
        self.box_area = box_area
        self.box_text = box_text
        self.box_selection = box_selection
        self.box_selection1 = box_selection1
        self.box_selection2 = box_selection2
        self.box_beam = box_beam
        self.box_scrollX_bg = box_scrollX_bg
        self.box_scrollY_bg = box_scrollY_bg
        self.box_scrollX = box_scrollX
        self.box_scrollY = box_scrollY
        self.blf_text = []
        self.scissor_text_box = Scissor()

        self.filt = CalcFilt(self)
        #|

    def upd_size(self, LL, RR, BB, TT, use_resize_upd_end=True):
        box_area = self.box_area
        # old_L = box_area.L
        # old_T = box_area.T
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        # d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]

        LL += d0
        RR -= d0
        TT -= d0
        BB += d0

        box_text = self.box_text
        if self.blf_text:
            dx0 = self.line_x - box_text.inner[0]
            dy0 = self.blf_text[0].y - box_text.inner[3] + self.headkey * SIZE_widget[0]

            box_text.LRBT_upd(LL, RR, BB, TT, widget_rim)

            L, R, B, T = box_text.inner

            self.box_selection.upd()
            self.box_selection1.upd()
            self.box_selection2.upd()
            self.box_beam.upd()
            self.box_scrollX.upd()
            self.box_scrollY.upd()

            self.font_main_dx, self.font_main_dy, self.font_main_dT = r_widget_font_dx_dy_dT(self.font_id, SIZE_widget[0])
            self.init_blf_lines_pos_text()

            R0 = R - self.scroll_width
            B0 = B + self.scroll_width
            self.scissor_text_box.intersect_with(self.w.scissor, L, R0, B0, T)
            self.box_scrollX_bg.LRBT_upd(L, R0, B, B0)
            self.box_scrollY_bg.LRBT_upd(R0, R, B, T)

            self.r_pan_text_override()(dx0, dy0)
        else:
            box_text.LRBT_upd(LL, RR, BB, TT, widget_rim)

            L, R, B, T = box_text.inner

            self.box_selection.upd()
            self.box_selection1.upd()
            self.box_selection2.upd()
            self.box_beam.upd()
            self.box_scrollX.upd()
            self.box_scrollY.upd()

            self.font_main_dx, self.font_main_dy, self.font_main_dT = r_widget_font_dx_dy_dT(self.font_id, SIZE_widget[0])
            self.init_blf_lines_pos_text()

            R0 = R - self.scroll_width
            B0 = B + self.scroll_width
            self.scissor_text_box.intersect_with(self.w.scissor, L, R0, B0, T)
            self.box_scrollX_bg.LRBT_upd(L, R0, B, B0)
            self.box_scrollY_bg.LRBT_upd(R0, R, B, T)

        if use_resize_upd_end is True:
            self.resize_upd_end()
        #|
    def init_blf_lines_pos_text(self):
        inner = self.box_text.inner
        row_count = ceil((inner[3] - inner[2]) / SIZE_widget[0])
        self.row_count = row_count

        lines = self.tex.lines
        ll = len(lines)
        self.headkey = 0
        blf_text = self.blf_text
        h = SIZE_widget[0]
        y = inner[3] - self.font_main_dT
        self.line_x = inner[0] + self.font_main_dx

        if row_count >= ll:
            blf_text[:] = [Blf(line)  for line in lines]
            blf_text += [Blf()  for r in range(row_count - ll + 1)]
            for e in blf_text:
                e.y = y
                y -= h
        else:
            blf_text.clear()
            for r in range(row_count + 1):
                blf_text.append(Blf(lines[r], 0, y))
                y -= h
        #|

    def selection_timer_end(self):
        Admin.REDRAW()
        self.box_selection.color = COL_box_text_selection
        self.box_selection1.color = COL_box_text_selection
        self.box_selection2.color = COL_box_text_selection
        #|

    def from_string(self, s):
        self.tex.from_string(s)
        self.init_blf_lines_pos_text()
        self.set_highlight(0, 0, 0, 0)

        self.resize_upd_end()
        #|

    def modal(self): pass
    def to_modal_dd(self, select_all=None, modal_type=""):

        #|
        global SELF, P_cursor_beam_time
        Admin.REDRAW()
        self.box_text.color = COL_box_text_active

        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _TRIGGER_dd_esc = TRIGGER['dd_esc']
        _TRIGGER_dd_scroll = TRIGGER['dd_scroll']
        _TRIGGER_rm = TRIGGER['rm']
        _TRIGGER_dd_confirm_area = TRIGGER['dd_confirm_area']
        _TRIGGER_dd_confirm = TRIGGER['dd_confirm']
        _self_box_text_inbox = self.box_text.inbox
        _self_box_area_inbox = self.box_area.inbox
        _self_box_scrollY_bg = self.box_scrollY_bg
        _self_box_scrollX_bg = self.box_scrollX_bg
        _text_evt = self.text_evt

        def modal_dd():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or _TRIGGER_dd_esc():
                _temp[0] = w_head.data
                w_head.fin()
                return

            if self.scroll_events(): return
            if self.scroll_region_events(): return

            Admin.TAG_CURSOR = 'TEXT'

            if _self_box_text_inbox(MOUSE):
                if MOUSE[0] >= _self_box_scrollY_bg.L:
                    Admin.TAG_CURSOR = 'DEFAULT'
                    if _TRIGGER_dd_scroll():
                        self.to_modal_scrollY()
                        return
                elif MOUSE[1] < _self_box_scrollX_bg.T:
                    Admin.TAG_CURSOR = 'DEFAULT'
                    if _TRIGGER_dd_scroll():
                        self.to_modal_scrollX()
                        return
                else:
                    Admin.TAG_CURSOR = 'TEXT'
                if _TRIGGER_rm():
                    self.to_modal_dd_rm()
                    return

            if _self_box_area_inbox(MOUSE) == False:
                if _TRIGGER_dd_confirm_area():
                    _temp[0] = None
                    w_head.fin()
                    return

            if _text_evt(): return

            if _TRIGGER_dd_confirm():
                _temp[0] = None
                w_head.fin()
                return
            #|

        w_head = Head(self, getattr(self, modal_type, modal_dd), self.end_modal_dd)
        w_head.data = {}

        P_cursor_beam_time = P.cursor_beam_time
        # <<< 1copy (0area_to_modal_dd_callfrom_dd_check,, $$)
        if timer_isreg(timer_beam):

            self.dd_parent = SELF
            if hasattr(SELF, "kill_push_timer"): SELF.kill_push_timer()
        else:
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
            self.dd_parent = None
        # >>>
        SELF = self
        if _self_box_text_inbox(MOUSE): Admin.TAG_CURSOR = 'TEXT'

        self.init_blf_lines_pos_text()

        _, _, y, x = self.tex.beam

        if select_all is None: select_all = P.use_select_all
        if select_all: self.set_highlight(0, 0, y, x)
        else: self.set_highlight(y, x, y, x)
        tx_limL = self.r_text_limL()
        tx_limT = self.r_text_limT()
        self.r_upd_scroll(tx_limL, self.r_text_limR(tx_limL, SIZE_widget[1]), self.r_text_limB(tx_limT), tx_limT)()
        self.local_history = LocalHistory(self, P.undo_steps_local, self.r_push_item)
        return w_head
        #|
    def end_modal_dd(self):
        # <<< 1copy (0area_SELF_to_top_level,, $$)
        if self.dd_parent == None:
            if timer_isreg(timer_beam):
                timer_unreg(timer_beam)

            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

        else:
            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()

            self.dd_parent.fin_callfront_set_parent()
        # >>>

        Admin.TAG_CURSOR = 'DEFAULT'
        Admin.REDRAW()
        kill_evt_except()
        self.text = self.tex.as_string()
        self.tex.free()
        # del self.tex
        self.local_history.kill()

        if _temp[0] == None:
            use_text_output = True
        else:
            use_text_output = None

        if hasattr(self.w, 'callback_end_modal_dd'):
            self.w.callback_end_modal_dd({
                'use_text_output': use_text_output,
            })
        #|
    def i_modal_dd_editor_protect(self):
        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']():
            self.w.fin_from_area()
            return

        if self.box_area.inbox(MOUSE):
            Admin.TAG_CURSOR = 'TEXT'
        else:
            Admin.TAG_CURSOR = 'DEFAULT'

        basis_evt_fn = self.w.basis_win_evt_protect()
        if basis_evt_fn != None:
            basis_evt_fn()
            return
        if self.scroll_events(): return
        if self.scroll_region_events(): return

        if self.box_text.inbox(MOUSE):
            if MOUSE[0] >= self.box_scrollY_bg.L:
                Admin.TAG_CURSOR = 'DEFAULT'
                if TRIGGER['dd_scroll']():
                    self.to_modal_scrollY()
                    return
            elif MOUSE[1] < self.box_scrollX_bg.T:
                Admin.TAG_CURSOR = 'DEFAULT'
                if TRIGGER['dd_scroll']():
                    self.to_modal_scrollX()
                    return
            else:
                Admin.TAG_CURSOR = 'TEXT'
            if TRIGGER['rm']():
                self.to_modal_dd_rm()
                return

        if self.text_evt(): return
        if EVT_TYPE[0] == 'RET' and EVT_TYPE[1] == 'PRESS':
            self.evt_linebreak()
            return
        #|

    def r_line_index_by_mouse(self, y):
        h = SIZE_widget[0]
        T = self.blf_text[0].y + self.font_main_dT + self.headkey * h
        y -= T
        return -y // h
        #|
    def to_modal_selection(self, shift=False):

        #|
        tex = self.tex
        lines = tex.lines
        beam = tex.beam
        font_id = self.font_id

        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _r_line_index_by_mouse = self.r_line_index_by_mouse
        _blfSize = blfSize
        _D_SIZE_font_main = D_SIZE['font_main']
        _r_blf_index = r_blf_index
        _set_highlight = self.set_highlight
        _auto_pan_text = self.auto_pan_text

        # /* 0AreaStringXY_area_to_modal_selection
        y = min(max(0, _r_line_index_by_mouse(MOUSE[1])), len(lines) - 1)
        if MOUSE[0] < self.line_x: x = 0
        else:
            _blfSize(font_id, _D_SIZE_font_main)
            x = _r_blf_index(lines[y], self.line_x, MOUSE[0], font_id)
        # */

        if shift is False:
            end_trigger = r_end_trigger('dd_selection')
            _set_highlight(y, x, y, x)
        else:
            end_trigger = r_end_trigger('dd_selection')
            _set_highlight(beam[0], beam[1], y, x)
        _auto_pan_text()

        def modal_selection():
            _REDRAW()

            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            # <<< 1copy (0AreaStringXY_area_to_modal_selection,, $$)
            y = min(max(0, _r_line_index_by_mouse(MOUSE[1])), len(lines) - 1)
            if MOUSE[0] < self.line_x: x = 0
            else:
                _blfSize(font_id, _D_SIZE_font_main)
                x = _r_blf_index(lines[y], self.line_x, MOUSE[0], font_id)
            # >>>

            _set_highlight(beam[0], beam[1], y, x)
            _auto_pan_text()
            #|

        if self.is_dropdown is True:
            w_head = Head(self, modal_selection)
        else:
            self.box_beam.color = COL_box_cursor_beam
            w_head = Head(self, modal_selection, self.reg_timer_beam_off)
        _REDRAW()
        return w_head
        #|
    def to_modal_selection_shift(self):

        return self.to_modal_selection(shift=True)
        #|
    def to_modal_scrollX(self, end_fn=None):

        end_trigger = r_end_trigger('dd_scroll')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        _mou = MOUSE[:]
        _scrollbar = self.box_scrollX
        _pan_text_override = self.r_pan_text_override()

        tx_limL = self.r_text_limL()
        tx_limT = self.r_text_limT()
        tx_limR = self.r_text_limR(tx_limL, SIZE_widget[1])
        tx_limB = self.r_text_limB(tx_limT)
        # <<< 1copy (0area_AreaStringXY_fn_cvXY_fac,, ${
        #     'fn_cvX_fac = rf_linear_01': 'fn_cvX_fac, _fn_cvX_fac_inv = rf_linear_01_inv'}$)
        _h = SIZE_widget[0]

        box_scrollX = self.box_scrollX
        box_scrollY = self.box_scrollY
        blf_text = self.blf_text
        sci = self.scissor_text_box

        L0, R0, B0, T0 = self.box_scrollX_bg.r_LRBT()
        L1, R1, B1, T1 = self.box_scrollY_bg.r_LRBT()

        bar_min = D_SIZE['widget_full_h'] // 2

        cv_w = max(1, tx_limL - tx_limR + sci.w)
        width_bgX = R0 - L0
        width_barX = min(max(floor(width_bgX * sci.w / cv_w), bar_min), width_bgX)
        barX_dif = width_bgX - width_barX

        cv_h = max(1, _h * len(self.tex.lines))
        width_bgY = T1 - B1
        width_barY = min(max(floor(width_bgY * sci.h / cv_h), bar_min), width_bgY)
        barY_dif = width_bgY - width_barY

        fn_cvX_fac, _fn_cvX_fac_inv = rf_linear_01_inv(tx_limL, tx_limR)
        fn_cvY_fac = rf_linear_01(tx_limT, tx_limB)
        # >>>

        _fn_scroll_fac = rf_linear_01(
            L0,
            R0 - width_barX)

        if _scrollbar.inbox(MOUSE) == False:
            # <<< 1copy (0area_AreaStringXY_i_modal_scrollbarX,, ${
            #     'MOUSE[0] - _mou[0]': 'MOUSE[0] - width_barX // 2 - _scrollbar.L'
            # }$)
            _pan_text_override(round(_fn_cvX_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.L + MOUSE[0] - width_barX // 2 - _scrollbar.L)), 1.0)) - self.line_x), 0)
            # >>>

        def modal_scrollX():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            # dx = MOUSE[0] - _mou[0]
            # fac = min(max(0.0, _fn_scroll_fac(_scrollbar.L + dx)), 1.0)
            # L = _fn_cvX_fac_inv(fac)
            # dx = L - self.line_x
            # _pan_text_override(round(dx), 0)
            # /* 0area_AreaStringXY_i_modal_scrollbarX
            _pan_text_override(round(_fn_cvX_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.L + MOUSE[0] - _mou[0])), 1.0)) - self.line_x), 0)
            # */

            _mou[:] = MOUSE

        def end_modal_scrollX():
            _REDRAW()
            kill_evt_except()

        w_head = Head(self, modal_scrollX, end_modal_scrollX)
        _REDRAW()
        #|
    def to_modal_scrollY(self, end_fn=None):

        end_trigger = r_end_trigger('dd_scroll')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        _mou = MOUSE[:]
        _scrollbar = self.box_scrollY
        _pan_text_override = self.r_pan_text_override()

        tx_limL = self.r_text_limL()
        tx_limT = self.r_text_limT()
        tx_limR = self.r_text_limR(tx_limL, SIZE_widget[1])
        tx_limB = self.r_text_limB(tx_limT)
        # <<< 1copy (0area_AreaStringXY_fn_cvXY_fac,, ${
        #     'fn_cvY_fac = rf_linear_01': 'fn_cvY_fac, _fn_cvY_fac_inv = rf_linear_01_inv'}$)
        _h = SIZE_widget[0]

        box_scrollX = self.box_scrollX
        box_scrollY = self.box_scrollY
        blf_text = self.blf_text
        sci = self.scissor_text_box

        L0, R0, B0, T0 = self.box_scrollX_bg.r_LRBT()
        L1, R1, B1, T1 = self.box_scrollY_bg.r_LRBT()

        bar_min = D_SIZE['widget_full_h'] // 2

        cv_w = max(1, tx_limL - tx_limR + sci.w)
        width_bgX = R0 - L0
        width_barX = min(max(floor(width_bgX * sci.w / cv_w), bar_min), width_bgX)
        barX_dif = width_bgX - width_barX

        cv_h = max(1, _h * len(self.tex.lines))
        width_bgY = T1 - B1
        width_barY = min(max(floor(width_bgY * sci.h / cv_h), bar_min), width_bgY)
        barY_dif = width_bgY - width_barY

        fn_cvX_fac = rf_linear_01(tx_limL, tx_limR)
        fn_cvY_fac, _fn_cvY_fac_inv = rf_linear_01_inv(tx_limT, tx_limB)
        # >>>

        _fn_scroll_fac = rf_linear_01(
            sci.y + sci.h,
            sci.y + width_barY - T0 + B0)

        if _scrollbar.inbox(MOUSE) == False:
            # <<< 1copy (0area_AreaStringXY_i_modal_scrollbarY,, ${
            #     'MOUSE[1] - _mou[1]': 'MOUSE[1] + width_barY // 2 - _scrollbar.T'
            # }$)
            _pan_text_override(0, round(_fn_cvY_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.T + MOUSE[1] + width_barY // 2 - _scrollbar.T)), 1.0)) - blf_text[0].y - self.headkey * _h))
            # >>>

        blf_text = self.blf_text

        def modal_scrollY():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            # dy = MOUSE[1] - _mou[1]
            # fac = min(max(0.0, _fn_scroll_fac(_scrollbar.T + dy)), 1.0)
            # T = _fn_cvY_fac_inv(fac)
            # dy = T - blf_text[0].y - self.headkey * _h
            # _pan_text_override(0, round(dy))
            # /* 0area_AreaStringXY_i_modal_scrollbarY
            _pan_text_override(0, round(_fn_cvY_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.T + MOUSE[1] - _mou[1])), 1.0)) - blf_text[0].y - self.headkey * _h))
            # */

            _mou[:] = MOUSE

        def end_modal_scrollY():
            _REDRAW()
            kill_evt_except()

        w_head = Head(self, modal_scrollY, end_modal_scrollY)
        _REDRAW()
        #|

    def to_modal_pan_text(self, override=None):


        end_trigger = r_end_trigger('pan')
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop()
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        # /* 0area0_get_pan_text_data
        blfSize(self.font_id, D_SIZE['font_main'])
        # L, R, B, T = self.box_text.inner
        # self.scissor_text_box.intersect_with(self.w.scissor, L, R - self.scroll_width, B + self.scroll_width, T)
        _h = SIZE_widget[0]
        _lines = self.tex.lines
        _max_len = len(_lines)
        _max_head = _max_len - self.row_count
        lim_L = self.r_text_limL()
        lim_T = self.r_text_limT()
        _BEAM_WIDTH = SIZE_widget[1]
        _lim = [
            lim_L,
            self.r_text_limR(lim_L, _BEAM_WIDTH),
            self.r_text_limB(lim_T),
            lim_T
        ]
        _lim_add_T = self.box_text.inner[3] - self.font_main_dT
        _lim_add_B = max(_lim_add_T,
            self.box_text.inner[2] + self.font_main_dy + _h * self.row_count)

        if len(self.blf_text) == self.row_count + 1:
            _allow_pan_y = _max_len * _h > (self.row_count - 1) * _h - self.box_scrollX_bg.r_h()
        else:
            _allow_pan_y = True

        _r_upd_scroll = self.r_upd_scroll
        _upd_scroll = [_r_upd_scroll(*_lim)]
        # */

        if _allow_pan_y:
            blf_text = self.blf_text
            _r_text_limR = self.r_text_limR
            _set_highlight = self.set_highlight

            def modal_pan_text():
                _REDRAW()
                if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                    w_head.fin()
                    return

                dx, dy = r_dxy_mouse()

                # /* 0area_AreaStringXY_pan_text
                new_y = blf_text[0].y + self.headkey * _h + dy
                if new_y < _lim[3]:
                    dy += _lim[3] - new_y
                elif new_y > _lim[2]:
                    dy += _lim[2] - new_y

                new_y = blf_text[0].y + dy
                if dy < 0:
                    if new_y < _lim_add_T:
                        n = max((new_y - _lim_add_T) // _h, - self.headkey)
                        if n < 0:
                            self.headkey += n

                            dy -= n * _h
                            r = self.headkey
                            for e in blf_text:
                                e.text = _lines[r]  if r < _max_len else ""
                                r += 1
                            blfSize(self.font_id, D_SIZE['font_main'])
                            _lim[1] = _r_text_limR(_lim[0], _BEAM_WIDTH)
                            _upd_scroll[0] = _r_upd_scroll(*_lim)
                else:
                    if new_y > _lim_add_B:
                        n = max((_lim_add_B - new_y) // _h, self.headkey - _max_head)
                        if n < 0:
                            self.headkey -= n

                            dy += n * _h
                            r = self.headkey
                            for e in blf_text:
                                e.text = _lines[r]  if r < _max_len else ""
                                r += 1
                            blfSize(self.font_id, D_SIZE['font_main'])
                            _lim[1] = _r_text_limR(_lim[0], _BEAM_WIDTH)
                            _upd_scroll[0] = _r_upd_scroll(*_lim)

                new_x = self.line_x + dx
                if new_x < _lim[1]:
                    dx += _lim[1] - new_x
                elif new_x > _lim[0]:
                    dx += _lim[0] - new_x

                self.line_x += dx
                for e in blf_text: e.y += dy

                _set_highlight(*self.tex.beam)
                _upd_scroll[0]()
                # */
                mouseloop()
        else:
            _pan_text_override = self.r_pan_text_override()

            def modal_pan_text():
                _REDRAW()
                if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                    w_head.fin()
                    return

                _pan_text_override(*r_dxy_mouse())
                mouseloop()

        def end_modal_pan_text():
            mouseloop_end()
            kill_evt_except()

        if override is None:
            w_head = Head(self, modal_pan_text, end_modal_pan_text)
        else:
            end_fn = override["end_fn"]
            def end_modal_pan_text_from_block():
                end_modal_pan_text()
                if end_fn is None: pass
                else: end_fn(w=self)

                self.evt_cancel()

            w_head = Head(self, modal_pan_text, end_modal_pan_text_from_block)

        _REDRAW()
        #|
    def to_modal_pan_text_from_block(self, end_fn=None):

        self.to_modal_pan_text(override={"end_fn": end_fn})
        #|
    def r_pan_text_override(self):
        # <<< 1copy (0area0_get_pan_text_data,, $$)
        blfSize(self.font_id, D_SIZE['font_main'])
        # L, R, B, T = self.box_text.inner
        # self.scissor_text_box.intersect_with(self.w.scissor, L, R - self.scroll_width, B + self.scroll_width, T)
        _h = SIZE_widget[0]
        _lines = self.tex.lines
        _max_len = len(_lines)
        _max_head = _max_len - self.row_count
        lim_L = self.r_text_limL()
        lim_T = self.r_text_limT()
        _BEAM_WIDTH = SIZE_widget[1]
        _lim = [
            lim_L,
            self.r_text_limR(lim_L, _BEAM_WIDTH),
            self.r_text_limB(lim_T),
            lim_T
        ]
        _lim_add_T = self.box_text.inner[3] - self.font_main_dT
        _lim_add_B = max(_lim_add_T,
            self.box_text.inner[2] + self.font_main_dy + _h * self.row_count)

        if len(self.blf_text) == self.row_count + 1:
            _allow_pan_y = _max_len * _h > (self.row_count - 1) * _h - self.box_scrollX_bg.r_h()
        else:
            _allow_pan_y = True

        _r_upd_scroll = self.r_upd_scroll
        _upd_scroll = [_r_upd_scroll(*_lim)]
        # >>>

        blf_text = self.blf_text
        _r_text_limR = self.r_text_limR
        _set_highlight = self.set_highlight

        if _allow_pan_y:
            def pan_text_override(dx, dy):
                # <<< 1copy (0area_AreaStringXY_pan_text,, $$)
                new_y = blf_text[0].y + self.headkey * _h + dy
                if new_y < _lim[3]:
                    dy += _lim[3] - new_y
                elif new_y > _lim[2]:
                    dy += _lim[2] - new_y

                new_y = blf_text[0].y + dy
                if dy < 0:
                    if new_y < _lim_add_T:
                        n = max((new_y - _lim_add_T) // _h, - self.headkey)
                        if n < 0:
                            self.headkey += n

                            dy -= n * _h
                            r = self.headkey
                            for e in blf_text:
                                e.text = _lines[r]  if r < _max_len else ""
                                r += 1
                            blfSize(self.font_id, D_SIZE['font_main'])
                            _lim[1] = _r_text_limR(_lim[0], _BEAM_WIDTH)
                            _upd_scroll[0] = _r_upd_scroll(*_lim)
                else:
                    if new_y > _lim_add_B:
                        n = max((_lim_add_B - new_y) // _h, self.headkey - _max_head)
                        if n < 0:
                            self.headkey -= n

                            dy += n * _h
                            r = self.headkey
                            for e in blf_text:
                                e.text = _lines[r]  if r < _max_len else ""
                                r += 1
                            blfSize(self.font_id, D_SIZE['font_main'])
                            _lim[1] = _r_text_limR(_lim[0], _BEAM_WIDTH)
                            _upd_scroll[0] = _r_upd_scroll(*_lim)

                new_x = self.line_x + dx
                if new_x < _lim[1]:
                    dx += _lim[1] - new_x
                elif new_x > _lim[0]:
                    dx += _lim[0] - new_x

                self.line_x += dx
                for e in blf_text: e.y += dy

                _set_highlight(*self.tex.beam)
                _upd_scroll[0]()
                # >>>
                return dx, dy
        else:
            def pan_text_override(dx, dy):
                dy = -65535
                # <<< 1copy (0area_AreaStringXY_pan_text,, $$)
                new_y = blf_text[0].y + self.headkey * _h + dy
                if new_y < _lim[3]:
                    dy += _lim[3] - new_y
                elif new_y > _lim[2]:
                    dy += _lim[2] - new_y

                new_y = blf_text[0].y + dy
                if dy < 0:
                    if new_y < _lim_add_T:
                        n = max((new_y - _lim_add_T) // _h, - self.headkey)
                        if n < 0:
                            self.headkey += n

                            dy -= n * _h
                            r = self.headkey
                            for e in blf_text:
                                e.text = _lines[r]  if r < _max_len else ""
                                r += 1
                            blfSize(self.font_id, D_SIZE['font_main'])
                            _lim[1] = _r_text_limR(_lim[0], _BEAM_WIDTH)
                            _upd_scroll[0] = _r_upd_scroll(*_lim)
                else:
                    if new_y > _lim_add_B:
                        n = max((_lim_add_B - new_y) // _h, self.headkey - _max_head)
                        if n < 0:
                            self.headkey -= n

                            dy += n * _h
                            r = self.headkey
                            for e in blf_text:
                                e.text = _lines[r]  if r < _max_len else ""
                                r += 1
                            blfSize(self.font_id, D_SIZE['font_main'])
                            _lim[1] = _r_text_limR(_lim[0], _BEAM_WIDTH)
                            _upd_scroll[0] = _r_upd_scroll(*_lim)

                new_x = self.line_x + dx
                if new_x < _lim[1]:
                    dx += _lim[1] - new_x
                elif new_x > _lim[0]:
                    dx += _lim[0] - new_x

                self.line_x += dx
                for e in blf_text: e.y += dy

                _set_highlight(*self.tex.beam)
                _upd_scroll[0]()
                # >>>
                return dx, dy

        return pan_text_override
        #|
    def auto_pan_text(self):
        L, R, B, T = self.box_beam.r_LRBT()
        sci = self.scissor_text_box
        dx = 0
        dy = 0
        if R > sci.x + sci.w:
            dx = sci.x + sci.w - R
        elif L < sci.x:
            dx = sci.x - L
        if B < sci.y:
            dy = sci.y - B
        elif T > sci.y + sci.h:
            dy = sci.y + sci.h - T
        if dx or dy:

            self.r_pan_text_override()(dx, dy)
        else:
            tx_limL = self.r_text_limL()
            tx_limT = self.r_text_limT()
            self.r_upd_scroll(tx_limL, self.r_text_limR(tx_limL, SIZE_widget[1]), self.r_text_limB(tx_limT), tx_limT)()
        #|

    def resize_upd_end(self):
        blfSize(self.font_id, D_SIZE['font_main'])
        tx_limL = self.r_text_limL()
        tx_limT = self.r_text_limT()
        self.r_upd_scroll(tx_limL, self.r_text_limR(tx_limL, SIZE_widget[1]), self.r_text_limB(tx_limT), tx_limT)()
        #|

    def evt_select_all(self, override=None, evtkill=True):

        #|
        if evtkill: kill_evt_except()
        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        y0, x0, y1, x1 = self.tex.beam

        if override == None:
            y = y1
            x = x1

            if y0 > y1:
                y0, y1 = y1, y0
                x0, x1 = x1, x0
            elif y0 == y1 and x0 > x1:
                x0, x1 = x1, x0

            max_index = len(self.tex.lines) - 1
            if y0 == 0 and x0 == 0 and y1 == max_index and x1 == len(self.tex.lines[max_index]):
                self.set_highlight(y, x, y, x)
            else:
                self.set_highlight(0, 0, max_index, len(self.tex.lines[max_index]))
        else:
            if override:
                max_index = len(self.tex.lines) - 1
                self.set_highlight(0, 0, max_index, len(self.tex.lines[max_index]))
            else:
                self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        #|
    def evt_select_word(self):

        kill_evt_except()
        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        y = self.tex.beam[2]
        x = self.tex.beam[3]
        s = self.tex.lines[y]
        if not s: return
        x0, x1 = r_word_select_index(s, x)
        self.set_highlight(y, x0, y, x1)
        self.auto_pan_text()
        #|
    def evt_cut(self):

        y0, x0, y1, x1 = self.tex.beam

        if y0 == y1 and x0 == x1:
            self.set_highlight(y0, 0, y0, len(self.tex.lines[y0]))

        self.evt_copy()
        self.evt_del_chr()
        #|
    def evt_copy(self):

        #|
        y0, x0, y1, x1 = self.tex.beam

        if y0 == y1 and x0 == x1:

            return

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
            self.box_selection.color = COL_box_text_selection_off
            self.box_selection1.color = COL_box_text_selection_off
            self.box_selection2.color = COL_box_text_selection_off
            if not timer_isreg(timer_selection):
                timer_reg(timer_selection, first_interval=0.1)
        else:
            self.reg_timer_beam_off()
            self.reg_timer_selection_off()
        self.box_beam.color = COL_box_cursor_beam

        bpy.context.window_manager.clipboard = self.tex.region_as_string()
        kill_evt_except()
        #|
    def evt_del_all(self, undo_push=True, evtkill=True):

        if self.readonly is True: return

        self.tex.clear()
        self.headkey = 0
        self.init_blf_lines_pos_text()
        self.set_highlight(0, 0, 0, 0)
        self.auto_pan_text()
        if undo_push:
            if timer_isreg(timer_undo_push):
                timer_unreg(timer_undo_push)
                self.local_history.push()
            timer_reg(timer_undo_push, first_interval=1.0)
        #|
    def evt_del_line(self):

        if self.readonly is True: return

        y0, x0, y1, x1 = self.tex.beam

        if y0 == y1 and x0 == x1:
            self.tex.select_set_safe(y0, 0, y0, len(self.tex.lines[y0]))

        self.evt_del_chr()
        #|
    def evt_del_word(self):

        if self.readonly is True: return

        y0, x0, y1, x1 = self.tex.beam

        if y0 == y1 and x0 == x1: pass
        else:
            self.evt_del_chr()
            return

        if x0 != x1:
            self.evt_del_chr()
            return

        kill_evt_except()
        lines = self.tex.lines

        if y1 == 0 and x1 == 0: return

        s = lines[y1][: x1]
        if not s:
            self.evt_del_chr()
            return
        i = r_prev_word_index(s)
        if i == x1: i -= 1

        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam

        self.set_highlight(y1, max(0, i), y1, x1)

        self.beam_input("")
        self.set_highlight(*self.tex.beam)
        self.auto_pan_text()
        #|
    def evt_del_chr(self):

        if self.readonly is True: return
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam
        kill_evt_except()

        y0, x0, y1, x1 = self.tex.beam
        lines = self.tex.lines

        if y0 == y1 and x0 == x1:
            if y0 == 0 and x0 == 0: return

            self.evt_beam_left_shift()
            self.beam_input("")
        else:
            self.beam_input("")

        self.auto_pan_text()
        #|
    def evt_beam_line_begin_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam

        line = self.tex.lines[y1]
        x = len(line) - len(line.lstrip())

        x1 = 0  if x1 == x else x

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        #|
    def evt_beam_line_end_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        ll = len(self.tex.lines[y1])
        if x1 >= ll: return
        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        self.set_highlight(y0, x0, y1, ll)
        self.auto_pan_text()
        #|
    def evt_beam_left_word_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        lines = self.tex.lines

        if y1 == 0 and x1 == 0: return

        s = lines[y1][: x1]
        if not s:
            self.evt_beam_left_shift()
            return
        i = r_prev_word_index(s)
        if i == x1:
            i -= 1
            if i < 0: i = 0

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        self.set_highlight(y0, x0, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_right_word_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        lines = self.tex.lines

        s = lines[y1]
        len_s = len(s)
        if x1 == len_s:
            self.evt_beam_right_shift()
            return
        i = r_next_word_index(s, x1)
        if i == x1:
            i += 1
            if i > len_s: i = len_s

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        self.set_highlight(y0, x0, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_left_shift(self):
        # /* 0area_AreaStringXY_evt_beam_left_shift

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        y0, x0, y1, x1 = self.tex.beam
        x1 -= 1
        if x1 < 0:
            if y1 != 0:
                y1 -= 1
                x1 = len(self.tex.lines[y1])
            else:
                x1 = 0

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # */
    def evt_beam_right_shift(self):
        # /* 0area_AreaStringXY_evt_beam_right_shift

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        lines = self.tex.lines
        y0, x0, y1, x1 = self.tex.beam
        x1 += 1
        if x1 > len(lines[y1]):
            if y1 == len(lines) - 1:
                x1 = len(lines[y1])
            else:
                y1 += 1
                x1 = 0

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # */
    def evt_beam_down_shift(self):
        # /* 0area_AreaStringXY_evt_beam_down_shift

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 += 1

        if y1 >= len(tex.lines):
            y1 = len(tex.lines) - 1
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # */
    def evt_beam_up_shift(self):
        # /* 0area_AreaStringXY_evt_beam_up_shift

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 -= 1

        if y1 < 0:
            y1 = 0
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # */
    def evt_beam_line_begin(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam

        line = self.tex.lines[y1]
        x = len(line) - len(line.lstrip())

        x1 = 0  if x1 == x else x

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        #|
    def evt_beam_line_end(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        ll = len(self.tex.lines[y1])
        if x1 >= ll: return
        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        self.set_highlight(y1, ll, y1, ll)
        self.auto_pan_text()
        #|
    def evt_beam_left_word(self):

        kill_evt_except()

        y0, x0, y1, x1 = self.tex.beam
        if y1 == 0 and x1 == 0: return

        s = self.tex.lines[y1][: x1]
        if not s:
            self.evt_beam_left()
            return
        i = r_prev_word_index(s)
        if i == x1:
            i -= 1
            if i < 0: i = 0

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        self.set_highlight(y1, i, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_right_word(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam

        s = self.tex.lines[y1]
        len_s = len(s)
        if x1 == len_s:
            self.evt_beam_right()
            return
        i = r_next_word_index(s, x1)
        if i == x1:
            i += 1
            if i > len_s: i = len_s

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        self.set_highlight(y1, i, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_left(self):
        # <<< 1copy (0area_AreaStringXY_evt_beam_left_shift,, ${'(y0, x0, y1, x1)':'(y1, x1, y1, x1)'}$)

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        y0, x0, y1, x1 = self.tex.beam
        x1 -= 1
        if x1 < 0:
            if y1 != 0:
                y1 -= 1
                x1 = len(self.tex.lines[y1])
            else:
                x1 = 0

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # >>>
        #|
    def evt_beam_right(self):
        # <<< 1copy (0area_AreaStringXY_evt_beam_right_shift,, ${'(y0, x0, y1, x1)':'(y1, x1, y1, x1)'}$)

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        lines = self.tex.lines
        y0, x0, y1, x1 = self.tex.beam
        x1 += 1
        if x1 > len(lines[y1]):
            if y1 == len(lines) - 1:
                x1 = len(lines[y1])
            else:
                y1 += 1
                x1 = 0

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # >>>
        #|
    def evt_beam_down(self):
        # <<< 1copy (0area_AreaStringXY_evt_beam_down_shift,, ${'(y0, x0, y1, x1)':'(y1, x1, y1, x1)'}$)

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 += 1

        if y1 >= len(tex.lines):
            y1 = len(tex.lines) - 1
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # >>>
        #|
    def evt_beam_up(self):
        # <<< 1copy (0area_AreaStringXY_evt_beam_up_shift,, ${'(y0, x0, y1, x1)':'(y1, x1, y1, x1)'}$)

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam

        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 -= 1

        if y1 < 0:
            y1 = 0
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        # >>>
        #|
    def evt_beam_end_shift(self):

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        tex = self.tex
        y = len(tex.lines) - 1
        x = len(tex.lines[y])
        self.set_highlight(tex.beam[0], tex.beam[1], y, x)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_start_shift(self):

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        beam = self.tex.beam
        self.set_highlight(beam[0], beam[1], 0, 0)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_end(self):

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        tex = self.tex
        y = len(tex.lines) - 1
        x = len(tex.lines[y])
        self.set_highlight(y, x, y, x)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_start(self):

        Admin.REDRAW()
        if self.is_dropdown is True:
            timer_unreg(timer_beam)
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        else:
            self.reg_timer_beam_off()
        self.box_beam.color = COL_box_cursor_beam
        self.set_highlight(0, 0, 0, 0)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_linebreak(self):
        # <<< 1copy (0area_textXY_evt_head,, $$)

        if self.readonly is True: return
        self.kill_push_timer()
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam
        kill_evt_except()
        # >>>

        y0, x0, y1, x1 = self.tex.beam
        if y0 == y1 and x0 == x1: pass
        else:
            self.evt_del_chr()
            y0, x0, y1, x1 = self.tex.beam

        y1 += 1

        self.beam_input("\n")
        self.set_highlight(y1, 0, y1, 0)
        self.auto_pan_text()
        #|
    def evt_untab(self):
        # <<< 1copy (0area_textXY_evt_head,, $$)

        if self.readonly is True: return
        self.kill_push_timer()
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam
        kill_evt_except()
        # >>>

        tex = self.tex
        y0, x0, y1, x1 = tex.beam
        indentation = tex.indentation
        len_indentation = len(indentation)

        if y0 == y1 and x0 == x1:
            line = tex.lines[y1]
            dif = len(line) - len(line.lstrip())

            if dif >= x1:
                select_len = x1 % len_indentation
                if select_len == 0: select_len = len_indentation

                tex.select_set_safe(y0, x0, y0, x0 - select_len)
            else:
                if x1 == 0: return
                if line[x1 - 1] != indentation[ : 1]: return

                i = r_prev_word_index(line[ : x1], nonword_chrs=indentation[ : 1])
                select_len = x1 - i
                if select_len > 0:
                    guess_index = x0 - min(select_len, len_indentation)
                    r = guess_index % len_indentation
                    if r == 0: pass
                    else:
                        guess_index += len_indentation - r
                        if guess_index > x0: guess_index = x0

                    tex.select_set_safe(y0, x0, y0, guess_index)
                else: return

            self.beam_input("")
            self.auto_pan_text()
            return

        lines = tex.lines
        len_line_y0 = len(lines[y0])
        len_line_y1 = len(lines[y1])

        for r in (range(y0, y1 + 1)  if y1 > y0 else range(y1, y0 + 1)):
            line = lines[r]
            x = len(line) - len(line.lstrip())

            dif = x % len_indentation
            if dif == 0: dif = len_indentation

            tex.select_set_safe(r, x, r, x - dif)
            tex.write("")

        self.update_blf_text()

        x0 += len(lines[y0]) - len_line_y0
        x1 += len(lines[y1]) - len_line_y1

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        #|
    def evt_tab(self):
        # <<< 1copy (0area_textXY_evt_head,, $$)

        if self.readonly is True: return
        self.kill_push_timer()
        Admin.REDRAW()
        timer_unreg(timer_beam)
        timer_reg(timer_beam, first_interval=P_cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam
        kill_evt_except()
        # >>>

        tex = self.tex
        y0, x0, y1, x1 = tex.beam
        indentation = tex.indentation
        len_indentation = len(indentation)

        if y0 == y1 and x0 == x1:
            line = tex.lines[y1]
            dif = len(line) - len(line.lstrip())

            if dif >= x1 and len_indentation > 1:
                self.beam_input((len_indentation - x1 % len_indentation) * indentation[ : 1])
            else:
                r = x1 % len_indentation
                if r == 0:
                    self.beam_input(indentation)
                else:
                    self.beam_input(indentation[ : 1] * (len_indentation - r))

            self.auto_pan_text()
            return

        lines = tex.lines
        len_line_y0 = len(lines[y0])
        len_line_y1 = len(lines[y1])

        for r in (range(y0, y1 + 1)  if y1 > y0 else range(y1, y0 + 1)):
            line = lines[r]
            x = len(line) - len(line.lstrip())
            tex.select_set_safe(r, x, r, x)
            tex.write((len_indentation - x % len_indentation) * indentation[ : 1])

        self.update_blf_text()

        x0 += len(lines[y0]) - len_line_y0
        x1 += len(lines[y1]) - len_line_y1

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        #|

    def evt_scrollX(self, dx):

        kill_evt_except()
        self.r_pan_text_override()(dx, 0)
        Admin.REDRAW()
        #|
    def evt_scrollY(self, dy):

        kill_evt_except()
        self.r_pan_text_override()(0, dy)
        Admin.REDRAW()
        #|

    def beam_input_unpush(self, s):
        # <<< 1copy (0area_AreaStringXY_beam_input,, $$)
        if self.readonly is True: return

        ind = self.tex.write(s)
        if ind is None:
            self.update_blf_text()
        else:
            blf_index = ind - self.headkey
            if blf_index < len(self.blf_text):
                self.blf_text[blf_index].text = self.tex.lines[ind]

        self.set_highlight(*self.tex.beam)
        self.auto_pan_text()
        # >>>
        #|
    def beam_input(self, s):
        # /* 0area_AreaStringXY_beam_input
        if self.readonly is True: return

        ind = self.tex.write(s)
        if ind is None:
            self.update_blf_text()
        else:
            blf_index = ind - self.headkey
            if blf_index < len(self.blf_text):
                self.blf_text[blf_index].text = self.tex.lines[ind]

        self.set_highlight(*self.tex.beam)
        self.auto_pan_text()
        # */
        if timer_isreg(timer_undo_push): timer_unreg(timer_undo_push)
        timer_reg(timer_undo_push, first_interval=1.0)
        #|
    def update_blf_text(self):
        lines = self.tex.lines
        max_len = len(lines)
        r = self.headkey
        for e in self.blf_text:
            e.text = lines[r]  if r < max_len else ""
            r += 1
        #|

    def to_history_index(self, index):

        Admin.REDRAW()
        self.evt_del_all(False)
        e = self.local_history.array[index]
        self.beam_input_unpush(e[0])
        self.set_highlight(*e[1])
        self.r_pan_text_override()(e[2][0] - self.line_x,
            (e[2][2] - self.headkey) * SIZE_widget[0] + e[2][1] - self.blf_text[0].y)
        #|
    def r_push_item(self):
        return (
            self.tex.as_string(),
            tuple(self.tex.beam),
            (self.line_x, self.blf_text[0].y, self.headkey))
        #|

    def set_highlight(self, line_start, char_start, line_end, char_end):
        lines = self.tex.lines
        if char_start > len(lines[line_start]): char_start = len(lines[line_start])
        if char_end > len(lines[line_end]): char_end = len(lines[line_end])
        self.tex.select_set_safe(line_start, char_start, line_end, char_end)
        y0, x0, y1, x1 = self.tex.beam

        font_id = self.font_id
        h = SIZE_widget[0]
        LL, RR, BB, TT = self.box_text.inner
        L = self.line_x
        blfSize(font_id, D_SIZE['font_main'])

        if line_start == line_end:
            self.box_selection1.LRBT_upd(0, 0, 0, 0)
            self.box_selection2.LRBT_upd(0, 0, 0, 0)
            body = lines[line_start]
            T = self.blf_text[0].y + self.font_main_dT + (self.headkey - line_start) * h
            self.box_selection.LRBT_upd(
                L + floor(blfDimen(font_id, body[: char_start])[0]),
                L + floor(blfDimen(font_id, body[: char_end])[0]),
                T - h, T)

            e = self.box_selection
            self.box_beam.LRBT_upd(e.R, e.R + SIZE_widget[1], e.B, e.T)
        else:
            if line_end < line_start:
                is_flip = True
                line_start, line_end = line_end, line_start
                char_start, char_end = char_end, char_start
            else:
                is_flip = False

            body = lines[line_start]
            T0 = self.blf_text[0].y + self.font_main_dT
            T = T0 + (self.headkey - line_start) * h
            B = T - h
            self.box_selection.LRBT_upd(
                L + floor(blfDimen(font_id, body[: char_start])[0]),
                RR, B, T)

            body = lines[line_end]
            T = T0 + (self.headkey - line_end) * h
            self.box_selection2.LRBT_upd(
                LL,
                L + floor(blfDimen(font_id, body[: char_end])[0]),
                T - h, T)

            if line_end - line_start == 1:
                self.box_selection1.LRBT_upd(0, 0, 0, 0)
            else:
                self.box_selection1.LRBT_upd(LL, RR, B, T)

            if is_flip:
                e = self.box_selection
                self.box_beam.LRBT_upd(e.L, e.L + SIZE_widget[1], e.B, e.T)
            else:
                e = self.box_selection2
                self.box_beam.LRBT_upd(e.R, e.R + SIZE_widget[1], e.B, e.T)
        #|
    def r_text_limL(self):
        return self.scissor_text_box.x + self.font_main_dx
        #|
    def r_text_limR(self, tx_limL, beam_width): # set size require
        font_id = self.font_id
        return min(tx_limL,
            self.scissor_text_box.x + self.scissor_text_box.w - self.font_main_dx - beam_width
            - floor(max(blfDimen(font_id, e.text)[0]  for e in self.blf_text))
        )
        #|
    def r_text_limT(self):
        return self.scissor_text_box.y + self.scissor_text_box.h - self.font_main_dT
        #|
    def r_text_limB(self, tx_limT):
        return max(tx_limT,
            self.scissor_text_box.y + self.font_main_dy + SIZE_widget[0] * max(
            self.row_count, len(self.tex.lines) - 1)
        )
        #|
    def r_upd_scroll(self, tx_limL, tx_limR, tx_limB, tx_limT):
        # /* 0area_AreaStringXY_fn_cvXY_fac
        _h = SIZE_widget[0]

        box_scrollX = self.box_scrollX
        box_scrollY = self.box_scrollY
        blf_text = self.blf_text
        sci = self.scissor_text_box

        L0, R0, B0, T0 = self.box_scrollX_bg.r_LRBT()
        L1, R1, B1, T1 = self.box_scrollY_bg.r_LRBT()

        bar_min = D_SIZE['widget_full_h'] // 2

        cv_w = max(1, tx_limL - tx_limR + sci.w)
        width_bgX = R0 - L0
        width_barX = min(max(floor(width_bgX * sci.w / cv_w), bar_min), width_bgX)
        barX_dif = width_bgX - width_barX

        cv_h = max(1, _h * len(self.tex.lines))
        width_bgY = T1 - B1
        width_barY = min(max(floor(width_bgY * sci.h / cv_h), bar_min), width_bgY)
        barY_dif = width_bgY - width_barY

        fn_cvX_fac = rf_linear_01(tx_limL, tx_limR)
        fn_cvY_fac = rf_linear_01(tx_limT, tx_limB)
        # */

        def upd_scroll():
            L = L0 + max(round(fn_cvX_fac(self.line_x) * barX_dif), 0)
            box_scrollX.LRBT_upd(L, L + width_barX, B0, T0)

            T = T1 - max(round(fn_cvY_fac(blf_text[0].y + _h * self.headkey) * barY_dif), 0)
            box_scrollY.LRBT_upd(L1, R1, T - width_barY, T)

        return upd_scroll
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)
        self.box_text.dxy_upd(dx, dy)
        self.box_scrollX_bg.dxy_upd(dx, dy)
        self.box_scrollY_bg.dxy_upd(dx, dy)
        self.box_scrollX.dxy_upd(dx, dy)
        self.box_scrollY.dxy_upd(dx, dy)

        self.line_x += dx
        for e in self.blf_text: e.y += dy
        L, R, B, T = self.box_text.inner
        self.scissor_text_box.intersect_with(self.w.scissor, L, R - self.scroll_width, B + self.scroll_width, T)

        self.set_highlight(*self.tex.beam)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        self.box_text.bind_draw()
        self.box_scrollX_bg.bind_draw()
        self.box_scrollY_bg.bind_draw()
        self.box_scrollX.bind_draw()
        self.box_scrollY.bind_draw()

        self.scissor_text_box.use()
        self.box_selection.bind_draw()
        self.box_selection1.bind_draw()
        self.box_selection2.bind_draw()
        self.box_beam.bind_draw()

        font_id = self.font_id
        blfSize(font_id, D_SIZE['font_main'])
        blfColor(font_id, *self.font_color)
        x = self.line_x
        for e in self.blf_text:
            blfPos(font_id, x, e.y, 0)
            blfDraw(font_id, e.text)

        self.w.scissor.use()
        #|

    def reg_timer_selection_off(self): pass
    def upd_data(self): pass
    #|
    #|
class AreaStringXYPre(AreaStringXY):
    __slots__ = 'timer_beam_off_reg', 'timer_selection_off_reg', 'r_height', 'box_block'

    def __init__(self, w, input_text="", font_id=None):
        self.timer_beam_off_reg = None
        self.timer_selection_off_reg = None

        super().__init__(w, input_text=input_text, font_id=font_id)

        self.box_text.color = COL_box_text_read
        self.box_text.color_rim = COL_box_text_read_rim
        self.is_dropdown = False
        self.readonly = True
        self.box_beam.color = FLO_0000
        # self.focus_element = -1
        #|

    def init_from_block(self, area):
        self.r_height = lambda x: area.box_region.inner[3] - area.box_region.inner[2]
        self.box_block = self.box_area
        #|

    def init_bat(self, LL, RR, TT):
        BB = TT - self.r_height(None)
        self.row_count = ceil((TT - BB - (SIZE_dd_border[0] + SIZE_border[3]) * 2) / SIZE_widget[0])
        self.upd_size(LL, RR, BB, TT)
        return BB
        #|

    def modal(self):
        if self.box_text.inbox(MOUSE):
            if self.scroll_events(): return True
            if self.scroll_region_events(): return True

            if self.box_scrollY_bg.L <= MOUSE[0]:
                if TRIGGER['dd_scroll']():
                    self.to_modal_scrollY()
                    return True
            elif MOUSE[1] < self.box_scrollX_bg.T:
                if TRIGGER['dd_scroll']():
                    self.to_modal_scrollX()
                    return True

            if TRIGGER['rm']():
                self.to_modal_rm()
                return True

            if self.text_evt(): return True
        #|

    def evt_redo(self): pass
    def evt_undo(self): pass

    def resize_upd_end(self):
        if hasattr(self.w, "areas") and P.adaptive_win_resize and hasattr(self.w, "r_area_posRB_adaptive"):
            posR, posB = self.w.r_area_posRB_adaptive(self)

            if posR == self.box_area.R and posB == self.box_area.B: pass
            else:
                e = self.box_area
                if posB != e.B:
                    posB = min(posB, e.T - SIZE_widget[0] * 2)

                if self.blf_text:
                    dx0 = self.line_x - self.font_main_dx - self.box_text.inner[0]
                    dy0 = self.blf_text[0].y + self.font_main_dT - self.box_text.inner[3] + self.headkey * SIZE_widget[0]

                    self.upd_size(
                        e.L,
                        posR,
                        posB,
                        e.T,
                        use_resize_upd_end = False)
                    self.init_blf_lines_pos_text()

                    self.r_pan_text_override()(dx0, dy0)
                else:
                    self.upd_size(
                        e.L,
                        posR,
                        posB,
                        e.T,
                        use_resize_upd_end = False)
                    self.init_blf_lines_pos_text()

        super().resize_upd_end()
        #|

    def text_evt(self):
        # <<< 1copy (0area_AreaFilterY_text_evt,, $$)
        if TRIGGER['redo']():
            self.evt_redo()
            return True
        if TRIGGER['undo']():
            self.evt_undo()
            return True
        if TRIGGER['dd_match_end']():
            self.evt_toggle_match_end()
            return True
        if TRIGGER['dd_match_case']():
            self.evt_toggle_match_case()
            return True
        if TRIGGER['dd_match_whole_word']():
            self.evt_toggle_match_whole_word()
            return True
        if TRIGGER['dd_select_all']():
            self.evt_select_all()
            return True
        if TRIGGER['dd_select_word']():
            self.evt_select_word()
            return True
        if TRIGGER['dd_cut']():
            self.evt_cut()
            return True
        if TRIGGER['dd_paste']():
            self.evt_paste()
            return True
        if TRIGGER['dd_copy']():
            self.evt_copy()
            return True
        if TRIGGER['dd_del_all']():
            self.evt_del_all()
            return True
        if TRIGGER['dd_del']():
            self.evt_del_line()
            return True
        if TRIGGER['dd_del_word']():
            self.evt_del_word()
            return True
        if TRIGGER['dd_del_chr']():
            self.evt_del_chr()
            return True
        if TRIGGER['dd_beam_line_begin_shift']():
            self.evt_beam_line_begin_shift()
            return True
        if TRIGGER['dd_beam_line_end_shift']():
            self.evt_beam_line_end_shift()
            return True
        if TRIGGER['dd_beam_left_word_shift']():
            self.evt_beam_left_word_shift()
            return True
        if TRIGGER['dd_beam_right_word_shift']():
            self.evt_beam_right_word_shift()
            return True
        if TRIGGER['dd_beam_left_shift']():
            self.evt_beam_left_shift()
            return True
        if TRIGGER['dd_beam_right_shift']():
            self.evt_beam_right_shift()
            return True
        if TRIGGER['dd_beam_down_shift']():
            self.evt_beam_down_shift()
            return True
        if TRIGGER['dd_beam_up_shift']():
            self.evt_beam_up_shift()
            return True
        if TRIGGER['dd_beam_line_begin']():
            self.evt_beam_line_begin()
            return True
        if TRIGGER['dd_beam_line_end']():
            self.evt_beam_line_end()
            return True
        if TRIGGER['dd_beam_left_word']():
            self.evt_beam_left_word()
            return True
        if TRIGGER['dd_beam_right_word']():
            self.evt_beam_right_word()
            return True
        if TRIGGER['dd_beam_left']():
            self.evt_beam_left()
            return True
        if TRIGGER['dd_beam_right']():
            self.evt_beam_right()
            return True
        if TRIGGER['dd_beam_down']():
            self.evt_beam_down()
            return True
        if TRIGGER['dd_beam_up']():
            self.evt_beam_up()
            return True
        if TRIGGER['dd_beam_end_shift']():
            self.evt_beam_end_shift()
            return True
        if TRIGGER['dd_beam_start_shift']():
            self.evt_beam_start_shift()
            return True
        if TRIGGER['dd_beam_end']():
            self.evt_beam_end()
            return True
        if TRIGGER['dd_beam_start']():
            self.evt_beam_start()
            return True
        if TRIGGER['pan']():
            self.to_modal_pan_text()
            return True
        if TRIGGER['dd_selection_shift']():
            self.to_modal_selection_shift()
            return True
        if TRIGGER['dd_selection']():
            self.to_modal_selection()
            return True
        if TRIGGER['dd_linebreak']():
            self.evt_linebreak()
            return True
        if TRIGGER['dd_untab']():
            self.evt_untab()
            return True
        if TRIGGER['dd_tab']():
            self.evt_tab()
            return True
        # >>>
        #|
    def to_modal_rm(self):
        items = [
            ("dd_scroll_left_most", lambda: self.evt_scrollX(self.box_area.r_w())),
            ("dd_scroll_right_most", lambda: self.evt_scrollX(-self.box_area.r_w())),
            ("dd_scroll_down_most", lambda: self.evt_scrollY(16777215)),
            ("dd_scroll_up_most", lambda: self.evt_scrollY(-16777215)),
            ("dd_scroll_left", lambda: self.evt_scrollX(P.scroll_distance)),
            ("dd_scroll_right", lambda: self.evt_scrollX(-P.scroll_distance)),
            ("dd_scroll_down", lambda: self.evt_scrollY(P.scroll_distance)),
            ("dd_scroll_up", lambda: self.evt_scrollY(-P.scroll_distance)),

            ("dd_scroll_left_area", lambda: self.evt_scrollX(P.scroll_distance)),
            ("dd_scroll_right_area", lambda: self.evt_scrollX(-P.scroll_distance)),
            ("dd_scroll_down_area", lambda: self.evt_scrollY(P.scroll_distance)),
            ("dd_scroll_up_area", lambda: self.evt_scrollY(-P.scroll_distance)),

            ("dd_copy", self.evt_area_copy),
        ]
        DropDownRMKeymap(self, MOUSE, items)
        #|

    def timer_beam_off(self):

        self.box_beam.color = FLO_0000
        Admin.REDRAW()
        self.timer_beam_off_reg = None
        #|
    def reg_timer_beam_off(self):
        if self.timer_beam_off_reg is not None:
            timer_unreg(self.timer_beam_off_reg)

        self.timer_beam_off_reg = self.timer_beam_off
        timer_reg(self.timer_beam_off_reg, first_interval=P.cursor_beam_time)
        #|
    def timer_selection_off(self):

        self.box_selection.color = COL_box_text_selection
        self.box_selection1.color = COL_box_text_selection
        self.box_selection2.color = COL_box_text_selection
        Admin.REDRAW()
        self.timer_selection_off_reg = None
        #|
    def reg_timer_selection_off(self):
        if self.timer_selection_off_reg is not None:
            timer_unreg(self.timer_selection_off_reg)

        self.box_selection.color = COL_box_text_selection_off
        self.box_selection1.color = COL_box_text_selection_off
        self.box_selection2.color = COL_box_text_selection_off
        self.timer_selection_off_reg = self.timer_selection_off
        timer_reg(self.timer_selection_off_reg, first_interval=0.1)
        #|

    def draw_blf(self): pass
    def draw_box(self):
        self.box_area.bind_draw()
        self.box_text.bind_draw()
        self.box_scrollX_bg.bind_draw()
        self.box_scrollY_bg.bind_draw()
        self.box_scrollX.bind_draw()
        self.box_scrollY.bind_draw()

        self.scissor_text_box.use()
        self.box_selection.bind_draw()
        self.box_selection1.bind_draw()
        self.box_selection2.bind_draw()
        self.box_beam.bind_draw()

        font_id = self.font_id
        blfSize(font_id, D_SIZE['font_main'])
        blfColor(font_id, *self.font_color)
        x = self.line_x
        for e in self.blf_text:
            blfPos(font_id, x, e.y, 0)
            blfDraw(font_id, e.text)

        self.w.scissor.use()
        blend_set('ALPHA')
        #|
    #|
    #|
class AreaStringXYButton:
    __slots__ = (
        'w',
        'area',
        'font_id',
        'tex',
        'font_color',
        'line_x',
        'box_button',
        'box_selection',
        'box_selection1',
        'box_selection2',
        'box_beam',
        'blf_text',
        'dxy',
        'draw_box',
        'timer_beam_off_reg',
        'timer_selection_off_reg',
        'box_block',
        'column_len',
        'inside',
        'font_main_dx',
        'font_main_dy',
        'font_main_dT')

    #| self.w.scissor
    #| self.w.r_pan_override
    def __init__(self, w, area, input_text, wrap_width, font_id):
        self.timer_beam_off_reg = None
        self.timer_selection_off_reg = None

        blfSize(font_id, D_SIZE['font_main'])
        lines = sum([rl_blf_wrap(s, wrap_width)  for s in input_text.split('\n')], [])
        if lines: pass
        else: lines = ['']
        self.column_len = len(lines)

        #
        self.tex = Text()
        self.tex.lines = lines
        self.w = w
        self.area = area
        self.font_id = font_id
        self.font_color = COL_block_fg
        self.line_x = 0

        self.box_button = GpuRim(COL_box_text_read, COL_box_text_read_rim)
        self.box_selection = GpuBox(COL_box_text_selection)
        self.box_selection1 = GpuBox(COL_box_text_selection)
        self.box_selection2 = GpuBox(COL_box_text_selection)
        self.box_beam = GpuBox(FLO_0000)
        self.blf_text = [Blf(s)  for s in lines]

        self.dxy = self.i_dxy

        self.draw_box = self.i_draw_box
        self.inside = self.box_button.inbox
        #|

    def init_bat(self, LL, RR, TT):
        widget_rim = SIZE_border[3]
        h = SIZE_widget[0]
        B = TT - D_SIZE['widget_full_h'] - (self.column_len - 1) * h
        # self.box_button.LRBT_upd(LL, RR, B, TT, widget_rim)
        self.box_button.LRBT(LL, RR, B, TT, widget_rim)

        self.line_x = LL + D_SIZE['font_main_title_offset']
        self.font_main_dx, self.font_main_dy, self.font_main_dT = r_widget_font_dx_dy_dT(self.font_id, SIZE_widget[0])

        y = self.box_button.inner[3] - widget_rim - self.font_main_dT
        for e in self.blf_text:
            e.y = y
            y -= h

        self.set_highlight(*self.tex.beam)
        return B
        #|

    def r_height(self, width): return D_SIZE['widget_full_h'] + (self.column_len - 1) * SIZE_widget[0]

    def dark(self): pass
    def light(self): pass

    def inside_evt(self): pass
    def outside_evt(self): pass

    def modal(self):
        if TRIGGER['rm']():
            self.to_modal_rm()
            return True
        if TRIGGER['redo']():
            if hasattr(self, w, 'evt_redo'):
                self.evt_redo()
                return True
        if TRIGGER['undo']():
            if hasattr(self, w, 'evt_undo'):
                self.evt_undo()
                return True
        if TRIGGER['dd_select_all']():
            self.evt_select_all()
            return True
        if TRIGGER['dd_select_word']():
            self.evt_select_word()
            return True
        if TRIGGER['dd_cut']():
            self.evt_copy()
            return True
        if TRIGGER['dd_copy']():
            self.evt_copy()
            return True
        if TRIGGER['dd_beam_line_begin_shift']():
            self.evt_beam_line_begin_shift()
            return True
        if TRIGGER['dd_beam_line_end_shift']():
            self.evt_beam_line_end_shift()
            return True
        if TRIGGER['dd_beam_left_word_shift']():
            self.evt_beam_left_word_shift()
            return True
        if TRIGGER['dd_beam_right_word_shift']():
            self.evt_beam_right_word_shift()
            return True
        if TRIGGER['dd_beam_left_shift']():
            self.evt_beam_left_shift()
            return True
        if TRIGGER['dd_beam_right_shift']():
            self.evt_beam_right_shift()
            return True
        if TRIGGER['dd_beam_down_shift']():
            self.evt_beam_down_shift()
            return True
        if TRIGGER['dd_beam_up_shift']():
            self.evt_beam_up_shift()
            return True
        if TRIGGER['dd_beam_line_begin']():
            self.evt_beam_line_begin()
            return True
        if TRIGGER['dd_beam_line_end']():
            self.evt_beam_line_end()
            return True
        if TRIGGER['dd_beam_left_word']():
            self.evt_beam_left_word()
            return True
        if TRIGGER['dd_beam_right_word']():
            self.evt_beam_right_word()
            return True
        if TRIGGER['dd_beam_left']():
            self.evt_beam_left()
            return True
        if TRIGGER['dd_beam_right']():
            self.evt_beam_right()
            return True
        if TRIGGER['dd_beam_down']():
            self.evt_beam_down()
            return True
        if TRIGGER['dd_beam_up']():
            self.evt_beam_up()
            return True
        if TRIGGER['dd_beam_end_shift']():
            self.evt_beam_end_shift()
            return True
        if TRIGGER['dd_beam_start_shift']():
            self.evt_beam_start_shift()
            return True
        if TRIGGER['dd_beam_end']():
            self.evt_beam_end()
            return True
        if TRIGGER['dd_beam_start']():
            self.evt_beam_start()
            return True
        if TRIGGER['pan']():
            self.area.to_modal_pan()
            return True
        if TRIGGER['dd_selection_shift']():
            self.to_modal_selection(shift=True)
            return True
        if TRIGGER['dd_selection']():
            self.to_modal_selection()
            return True
        return False

    def evt_select_all(self, override=None, evtkill=True):

        if evtkill: kill_evt_except()
        Admin.REDRAW()
        self.reg_timer_beam_off()
        y0, x0, y1, x1 = self.tex.beam

        if override == None:
            y = y1
            x = x1

            if y0 > y1:
                y0, y1 = y1, y0
                x0, x1 = x1, x0
            elif y0 == y1 and x0 > x1:
                x0, x1 = x1, x0

            max_index = len(self.tex.lines) - 1
            if y0 == 0 and x0 == 0 and y1 == max_index and x1 == len(self.tex.lines[max_index]):
                self.set_highlight(y, x, y, x)
            else:
                self.set_highlight(0, 0, max_index, len(self.tex.lines[max_index]))
        else:
            if override:
                max_index = len(self.tex.lines) - 1
                self.set_highlight(0, 0, max_index, len(self.tex.lines[max_index]))
            else:
                self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        #|
    def evt_select_word(self):

        kill_evt_except()
        Admin.REDRAW()
        self.reg_timer_beam_off()

        y = self.tex.beam[2]
        x = self.tex.beam[3]
        s = self.tex.lines[y]
        if not s: return
        x0, x1 = r_word_select_index(s, x)
        self.set_highlight(y, x0, y, x1)
        self.auto_pan_text()
        #|
    def evt_copy(self):

        #|
        y0, x0, y1, x1 = self.tex.beam

        if y0 == y1 and x0 == x1:

            return

        Admin.REDRAW()
        self.reg_timer_selection_off()

        bpy.context.window_manager.clipboard = self.tex.region_as_string()
        kill_evt_except()
        #|
    def evt_beam_line_begin_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam

        line = self.tex.lines[y1]
        x = len(line) - len(line.lstrip())

        x1 = 0  if x1 == x else x

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        #|
    def evt_beam_line_end_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        ll = len(self.tex.lines[y1])
        if x1 >= ll: return
        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y0, x0, y1, ll)
        self.auto_pan_text()
        #|
    def evt_beam_left_word_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        lines = self.tex.lines

        if y1 == 0 and x1 == 0: return

        s = lines[y1][: x1]
        if not s:
            self.evt_beam_left_shift()
            return
        i = r_prev_word_index(s)
        if i == x1:
            i -= 1
            if i < 0: i = 0

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y0, x0, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_right_word_shift(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        lines = self.tex.lines

        s = lines[y1]
        len_s = len(s)
        if x1 == len_s:
            self.evt_beam_right_shift()
            return
        i = r_next_word_index(s, x1)
        if i == x1:
            i += 1
            if i > len_s: i = len_s

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y0, x0, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_left_shift(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()

        y0, x0, y1, x1 = self.tex.beam
        x1 -= 1
        if x1 < 0:
            if y1 != 0:
                y1 -= 1
                x1 = len(self.tex.lines[y1])
            else:
                x1 = 0

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_right_shift(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()

        lines = self.tex.lines
        y0, x0, y1, x1 = self.tex.beam
        x1 += 1
        if x1 > len(lines[y1]):
            if y1 == len(lines) - 1:
                x1 = len(lines[y1])
            else:
                y1 += 1
                x1 = 0

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_down_shift(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()

        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 += 1

        if y1 >= len(tex.lines):
            y1 = len(tex.lines) - 1
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_up_shift(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()

        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 -= 1

        if y1 < 0:
            y1 = 0
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y0, x0, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_line_begin(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam

        line = self.tex.lines[y1]
        x = len(line) - len(line.lstrip())

        x1 = 0  if x1 == x else x

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        #|
    def evt_beam_line_end(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam
        ll = len(self.tex.lines[y1])
        if x1 >= ll: return
        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y1, ll, y1, ll)
        self.auto_pan_text()
        #|
    def evt_beam_left_word(self):

        kill_evt_except()

        y0, x0, y1, x1 = self.tex.beam
        if y1 == 0 and x1 == 0: return

        s = self.tex.lines[y1][: x1]
        if not s:
            self.evt_beam_left()
            return
        i = r_prev_word_index(s)
        if i == x1:
            i -= 1
            if i < 0: i = 0

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y1, i, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_right_word(self):

        kill_evt_except()
        y0, x0, y1, x1 = self.tex.beam

        s = self.tex.lines[y1]
        len_s = len(s)
        if x1 == len_s:
            self.evt_beam_right()
            return
        i = r_next_word_index(s, x1)
        if i == x1:
            i += 1
            if i > len_s: i = len_s

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(y1, i, y1, i)
        self.auto_pan_text()
        #|
    def evt_beam_left(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()

        y0, x0, y1, x1 = self.tex.beam
        x1 -= 1
        if x1 < 0:
            if y1 != 0:
                y1 -= 1
                x1 = len(self.tex.lines[y1])
            else:
                x1 = 0

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_right(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()

        lines = self.tex.lines
        y0, x0, y1, x1 = self.tex.beam
        x1 += 1
        if x1 > len(lines[y1]):
            if y1 == len(lines) - 1:
                x1 = len(lines[y1])
            else:
                y1 += 1
                x1 = 0

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_down(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()
        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 += 1

        if y1 >= len(tex.lines):
            y1 = len(tex.lines) - 1
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_up(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()

        tex = self.tex
        y0, x0, y1, x1 = self.tex.beam
        y1 -= 1

        if y1 < 0:
            y1 = 0
        else:
            blfSize(self.font_id, D_SIZE['font_main'])
            x1 = r_blf_index(tex.lines[y1], self.line_x, self.box_beam.L, self.font_id)

        if x1 > len(tex.lines[y1]):
            x1 = len(tex.lines[y1])

        self.set_highlight(y1, x1, y1, x1)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_end_shift(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()
        tex = self.tex
        y = len(tex.lines) - 1
        x = len(tex.lines[y])
        self.set_highlight(tex.beam[0], tex.beam[1], y, x)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_start_shift(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()
        beam = self.tex.beam
        self.set_highlight(beam[0], beam[1], 0, 0)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_end(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()
        tex = self.tex
        y = len(tex.lines) - 1
        x = len(tex.lines[y])
        self.set_highlight(y, x, y, x)
        self.auto_pan_text()
        kill_evt_except()
        #|
    def evt_beam_start(self):

        Admin.REDRAW()
        self.reg_timer_beam_off()
        self.set_highlight(0, 0, 0, 0)
        self.auto_pan_text()
        kill_evt_except()
        #|

    def r_line_index_by_mouse(self, y):
        h = SIZE_widget[0]
        T = self.blf_text[0].y + self.font_main_dT
        y -= T
        return -y // h
        #|
    def to_modal_selection(self, shift=False):

        #|
        tex = self.tex
        lines = tex.lines
        beam = tex.beam
        font_id = self.font_id

        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _r_line_index_by_mouse = self.r_line_index_by_mouse
        _blfSize = blfSize
        _D_SIZE_font_main = D_SIZE['font_main']
        _r_blf_index = r_blf_index
        _set_highlight = self.set_highlight

        w = self.area
        box_beam = self.box_beam

        sci = w.scissor
        _lim_L = sci.x
        _lim_R = _lim_L + sci.w
        _lim_B = sci.y
        _lim_T = _lim_B + sci.h

        pan_override = w.r_pan_override()

        # <<< 1copy (0AreaStringXY_area_to_modal_selection,, $$)
        y = min(max(0, _r_line_index_by_mouse(MOUSE[1])), len(lines) - 1)
        if MOUSE[0] < self.line_x: x = 0
        else:
            _blfSize(font_id, _D_SIZE_font_main)
            x = _r_blf_index(lines[y], self.line_x, MOUSE[0], font_id)
        # >>>

        if shift is False:
            end_trigger = r_end_trigger('dd_selection')
            _set_highlight(y, x, y, x)
        else:
            end_trigger = r_end_trigger('dd_selection')
            _set_highlight(beam[0], beam[1], y, x)

        if box_beam.L < _lim_L:
            dx = _lim_L - box_beam.L
        elif box_beam.R > _lim_R:
            dx = _lim_R - box_beam.R
        else:
            dx = 0

        if box_beam.T > _lim_T:
            dy = _lim_T - box_beam.T
        elif box_beam.B < _lim_B:
            dy = _lim_B - box_beam.B
        else:
            dy = 0

        if dx or dy:
            pan_override(dx, dy)

        def modal_selection():
            _REDRAW()

            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            # <<< 1copy (0AreaStringXY_area_to_modal_selection,, $$)
            y = min(max(0, _r_line_index_by_mouse(MOUSE[1])), len(lines) - 1)
            if MOUSE[0] < self.line_x: x = 0
            else:
                _blfSize(font_id, _D_SIZE_font_main)
                x = _r_blf_index(lines[y], self.line_x, MOUSE[0], font_id)
            # >>>

            _set_highlight(beam[0], beam[1], y, x)

            if box_beam.L < _lim_L:
                dx = _lim_L - box_beam.L
            elif box_beam.R > _lim_R:
                dx = _lim_R - box_beam.R
            else:
                dx = 0

            if box_beam.T > _lim_T:
                dy = _lim_T - box_beam.T
            elif box_beam.B < _lim_B:
                dy = _lim_B - box_beam.B
            else:
                dy = 0

            if dx or dy:
                pan_override(dx, dy)

            if self.draw_box == self.i_draw_box_beam: pass
            else:
                self.draw_box = self.i_draw_box_beam
                self.dxy = self.i_dxy_beam
            #|

        self.box_beam.color = COL_box_cursor_beam
        w_head = Head(self, modal_selection, self.reg_timer_beam_off)
        self.reg_timer_beam_off()
        _REDRAW()
        return w_head
        #|
    def to_modal_rm(self):
        items = [
            ("dd_select_all", self.evt_select_all),
            ("dd_select_word", self.evt_select_word),
            ("dd_copy", self.evt_copy),
            ("dd_beam_line_begin_shift", self.evt_beam_line_begin_shift),
            ("dd_beam_line_end_shift", self.evt_beam_line_end_shift),
            ("dd_beam_left_word_shift", self.evt_beam_left_word_shift),
            ("dd_beam_right_word_shift", self.evt_beam_right_word_shift),
            ("dd_beam_left_shift", self.evt_beam_left_shift),
            ("dd_beam_right_shift", self.evt_beam_right_shift),
            ("dd_beam_down_shift", self.evt_beam_down_shift),
            ("dd_beam_up_shift", self.evt_beam_up_shift),
            ("dd_beam_line_begin", self.evt_beam_line_begin),
            ("dd_beam_line_end", self.evt_beam_line_end),
            ("dd_beam_left_word", self.evt_beam_left_word),
            ("dd_beam_right_word", self.evt_beam_right_word),
            ("dd_beam_left", self.evt_beam_left),
            ("dd_beam_right", self.evt_beam_right),
            ("dd_beam_down", self.evt_beam_down),
            ("dd_beam_up", self.evt_beam_up),
            ("dd_beam_end_shift", self.evt_beam_end_shift),
            ("dd_beam_start_shift", self.evt_beam_start_shift),
            ("dd_beam_end", self.evt_beam_end),
            ("dd_beam_start", self.evt_beam_start),
            ("pan", self.area.to_modal_pan),
        ]

        DropDownRMKeymap(self, MOUSE, items)
        #|

    def i_dxy(self, dx, dy):
        self.box_button.dxy_upd(dx, dy)

        self.line_x += dx

        for e in self.blf_text:
            e.y += dy
        #|
    def i_dxy_beam(self, dx, dy):
        self.box_button.dxy_upd(dx, dy)

        self.box_beam.dxy_upd(dx, dy)
        self.box_selection.dxy_upd(dx, dy)
        self.box_selection1.dxy_upd(dx, dy)
        self.box_selection2.dxy_upd(dx, dy)

        self.line_x += dx

        for e in self.blf_text:
            e.y += dy
        #|

    def i_draw_box(self): pass
    def i_draw_box_beam(self):
        if hasattr(self.box_selection, 'batdraw'):
            self.box_selection.bind_draw()
            self.box_selection1.bind_draw()
            self.box_selection2.bind_draw()
        if hasattr(self.box_beam, 'batdraw'):
            self.box_beam.bind_draw()
        #|
    def draw_blf(self):
        font_id = self.font_id
        blfSize(font_id, D_SIZE['font_main'])
        blfColor(font_id, *self.font_color)

        line_x = self.line_x

        for e in self.blf_text:
            blfPos(font_id, line_x, e.y, 0)
            blfDraw(font_id, e.text)
        #|

    def set_highlight(self, line_start, char_start, line_end, char_end):
        lines = self.tex.lines
        if char_start > len(lines[line_start]): char_start = len(lines[line_start])
        if char_end > len(lines[line_end]): char_end = len(lines[line_end])
        self.tex.select_set_safe(line_start, char_start, line_end, char_end)
        y0, x0, y1, x1 = self.tex.beam

        font_id = self.font_id
        h = SIZE_widget[0]
        LL, RR, BB, TT = self.box_button.inner
        L = self.line_x
        blfSize(font_id, D_SIZE['font_main'])

        if line_start == line_end:
            self.box_selection1.LRBT_upd(0, 0, 0, 0)
            self.box_selection2.LRBT_upd(0, 0, 0, 0)
            body = lines[line_start]
            T = self.blf_text[0].y + self.font_main_dT - line_start * h
            self.box_selection.LRBT_upd(
                L + floor(blfDimen(font_id, body[: char_start])[0]),
                L + floor(blfDimen(font_id, body[: char_end])[0]),
                T - h, T)

            e = self.box_selection
            self.box_beam.LRBT_upd(e.R, e.R + SIZE_widget[1], e.B, e.T)
        else:
            if line_end < line_start:
                is_flip = True
                line_start, line_end = line_end, line_start
                char_start, char_end = char_end, char_start
            else:
                is_flip = False

            body = lines[line_start]
            T0 = self.blf_text[0].y + self.font_main_dT
            T = T0 - line_start * h
            B = T - h
            self.box_selection.LRBT_upd(
                L + floor(blfDimen(font_id, body[: char_start])[0]),
                RR, B, T)

            body = lines[line_end]
            T = T0 - line_end * h
            self.box_selection2.LRBT_upd(
                LL,
                L + floor(blfDimen(font_id, body[: char_end])[0]),
                T - h, T)

            if line_end - line_start == 1:
                self.box_selection1.LRBT_upd(0, 0, 0, 0)
            else:
                self.box_selection1.LRBT_upd(LL, RR, B, T)

            if is_flip:
                e = self.box_selection
                self.box_beam.LRBT_upd(e.L, e.L + SIZE_widget[1], e.B, e.T)
            else:
                e = self.box_selection2
                self.box_beam.LRBT_upd(e.R, e.R + SIZE_widget[1], e.B, e.T)
        #|
    def auto_pan_text(self): # set_highlightRequire
        w = self.area
        e = self.box_beam
        L = e.L
        R = e.R
        B = e.B
        T = e.T

        sci = w.scissor
        _lim_L = sci.x
        _lim_R = _lim_L + sci.w
        _lim_B = sci.y
        _lim_T = _lim_B + sci.h

        if L < _lim_L:
            dx = _lim_L - L
        elif R > _lim_R:
            dx = _lim_R - R
        else:
            dx = 0

        if T > _lim_T:
            dy = _lim_T - T
        elif B < _lim_B:
            dy = _lim_B - B
        else:
            dy = 0

        if dx or dy:
            w.r_pan_override()(dx, dy)
        #|

    def timer_beam_off(self):

        self.box_beam.color = FLO_0000
        Admin.REDRAW()
        self.timer_beam_off_reg = None
        y0, x0, y1, x1 = self.tex.beam
        if y0 == y1 and x0 == x1:
            self.draw_box = self.i_draw_box
            self.dxy = self.i_dxy
        #|
    def reg_timer_beam_off(self):
        if self.timer_beam_off_reg is not None:
            timer_unreg(self.timer_beam_off_reg)

        self.timer_beam_off_reg = self.timer_beam_off
        timer_reg(self.timer_beam_off_reg, first_interval=P.cursor_beam_time)
        self.box_beam.color = COL_box_cursor_beam
        self.draw_box = self.i_draw_box_beam
        self.dxy = self.i_dxy_beam
        #|
    def timer_selection_off(self):

        self.box_selection.color = COL_box_text_selection
        self.box_selection1.color = COL_box_text_selection
        self.box_selection2.color = COL_box_text_selection
        Admin.REDRAW()
        self.timer_selection_off_reg = None
        y0, x0, y1, x1 = self.tex.beam
        if y0 == y1 and x0 == x1:
            self.draw_box = self.i_draw_box
            self.dxy = self.i_dxy
        #|
    def reg_timer_selection_off(self):
        if self.timer_selection_off_reg is not None:
            timer_unreg(self.timer_selection_off_reg)

        self.box_selection.color = COL_box_text_selection_off
        self.box_selection1.color = COL_box_text_selection_off
        self.box_selection2.color = COL_box_text_selection_off
        self.timer_selection_off_reg = self.timer_selection_off
        timer_reg(self.timer_selection_off_reg, first_interval=0.1)
        #|

    def upd_data(self): pass

    def set_ui_state_overridden(self): pass
    #|
    #|
class AreaStringMatch(AreaString):
    __slots__ = ()

    def upd_clip_text_and_match_button(self, blf_text):
        self.get_box_match()
        # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_main'}$)
        blfSize(FONT0, D_SIZE['font_main'])
        blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
        # >>>
        blf_text.text = r_blf_clipping_end(
            blf_text.unclip_text, blf_text.x, self.box_match_case.L - D_SIZE['font_main_dx'])
        #|
    def upd_scissor_text_box(self, scissor_win):
        self.scissor_text_box.intersect_with(scissor_win, self.box_text.inner[0],
            self.box_match_case.L - D_SIZE['font_main_dy'], self.box_text.B, self.box_text.T)
        #|

    def to_modal_dd(self, select_all=None, is_match_case=None, is_match_whole_word=None, is_match_end=None):

        #|
        global SELF, P_cursor_beam_time
        _REDRAW = Admin.REDRAW
        _REDRAW()
        blf_text = self.blf_text
        box_text = self.box_text
        box_text.color = COL_box_text_active

        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _TRIGGER_dd_esc = TRIGGER['dd_esc']
        _TRIGGER_dd_confirm = TRIGGER['dd_confirm']
        _TRIGGER_dd_confirm_area = TRIGGER['dd_confirm_area']
        _box_text_inbox = box_text.inbox
        _box_area_inbox = self.box_area.inbox
        _text_evt = self.text_evt

        _box_match_case = self.box_match_case
        _box_match_whole_word = self.box_match_whole_word
        _box_match_end = self.box_match_end

        _focus_element = [-1]
        self.box_match_hover.set_draw_state(False)

        def modal_dd():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or _TRIGGER_dd_esc():
                _temp[0] = w_head.data
                w_head.fin()
                return

            if _TRIGGER_dd_confirm():
                _temp[0] = None
                w_head.fin()
                return

            if _box_text_inbox(MOUSE):
                if _box_match_end.L <= MOUSE[0]:
                    if _focus_element[0] != 6:
                        _focus_element[0] = 6

                        Admin.TAG_CURSOR = 'DEFAULT'
                        self.box_match_hover.set_draw_state(True)
                        self.box_match_hover.LRBT_upd(*_box_match_end.r_LRBT())
                        _REDRAW()

                    if TRIGGER['click']():
                        self.evt_toggle_match_end()
                        return
                elif _box_match_whole_word.L <= MOUSE[0]:
                    if _focus_element[0] != 5:
                        _focus_element[0] = 5

                        Admin.TAG_CURSOR = 'DEFAULT'
                        self.box_match_hover.set_draw_state(True)
                        self.box_match_hover.LRBT_upd(*_box_match_whole_word.r_LRBT())
                        _REDRAW()

                    if TRIGGER['click']():
                        self.evt_toggle_match_whole_word()
                        return
                elif _box_match_case.L <= MOUSE[0]:
                    if _focus_element[0] != 4:
                        _focus_element[0] = 4

                        Admin.TAG_CURSOR = 'DEFAULT'
                        self.box_match_hover.set_draw_state(True)
                        self.box_match_hover.LRBT_upd(*_box_match_case.r_LRBT())
                        _REDRAW()

                    if TRIGGER['click']():
                        self.evt_toggle_match_case()
                        return
                else:
                    if _focus_element[0] != -1:
                        _focus_element[0] = -1

                        Admin.TAG_CURSOR = 'TEXT'
                        self.box_match_hover.set_draw_state(False)
                        _REDRAW()

                    if TRIGGER['rm']():
                        self.to_modal_dd_rm()
                        return
            else:
                if _focus_element[0] != -1:
                    _focus_element[0] = -1

                    Admin.TAG_CURSOR = 'TEXT'
                    self.box_match_hover.set_draw_state(False)
                    _REDRAW()

            if _box_area_inbox(MOUSE) == False:
                if _TRIGGER_dd_confirm_area():
                    _temp[0] = None
                    w_head.fin()
                    return

            _text_evt()
            #|

        w_head = Head(self, modal_dd, self.end_modal_dd)
        w_head.data = {'text': blf_text.unclip_text}

        P_cursor_beam_time = P.cursor_beam_time
        # <<< 1copy (0area_to_modal_dd_callfrom_dd_check,, $$)
        if timer_isreg(timer_beam):

            self.dd_parent = SELF
            if hasattr(SELF, "kill_push_timer"): SELF.kill_push_timer()
        else:
            timer_reg(timer_beam, first_interval=P_cursor_beam_time)
            self.dd_parent = None
        # >>>
        SELF = self
        Admin.TAG_CURSOR = 'TEXT'

        blf_text.x = box_text.inner[0] + D_SIZE['font_main_dx']
        blf_text.text = blf_text.unclip_text
        blfSize(FONT0, D_SIZE['font_main'])
        L = blf_text.x + floor(blfDimen(FONT0, blf_text.text)[0])
        self.box_beam.L = L
        self.box_beam.R = L + SIZE_widget[1]
        self.box_beam.upd()

        if select_all is None: select_all = P.use_select_all
        if select_all: self.evt_select_all()
        self.local_history = LocalHistory(self, P.undo_steps_local, self.r_push_item)

        if is_match_case is not None:
            self.filt.match_case = is_match_case
        if is_match_whole_word is not None:
            self.filt.match_whole_word = is_match_whole_word
        if is_match_end is not None:
            self.filt.match_end = is_match_end
        self.get_box_match()
        return w_head
        #|

    def evt_toggle_match_case(self, v=None):

        kill_evt_except()
        Admin.REDRAW()
        filt = self.filt
        if v == None: v = not filt.match_case
        filt.match_case = v
        self.get_box_match()
        #|
    def evt_toggle_match_whole_word(self, v=None):

        kill_evt_except()
        Admin.REDRAW()
        filt = self.filt
        if v == None: v = not filt.match_whole_word
        filt.match_whole_word = v
        self.get_box_match()
        #|
    def evt_toggle_match_end(self, v=None):

        kill_evt_except()
        Admin.REDRAW()
        filt = self.filt
        if v == None:
            v = filt.match_end + 1
            if v == 3: v = 0
        filt.match_end = v
        self.get_box_match()
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        self.box_text.bind_draw()
        self.box_match_end_bg.bind_draw()
        self.box_match_whole_word_bg.bind_draw()
        self.box_match_case_bg.bind_draw()
        self.box_match_end.bind_draw()
        self.box_match_whole_word.bind_draw()
        self.box_match_case.bind_draw()
        self.box_match_hover.bind_draw()

        self.scissor_text_box.use()
        self.box_selection.bind_draw()
        self.box_beam.bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        self.w.scissor.use()
        #|
    #|
    #|


class AreaBlock(ScrollEvents, StructAreaModal):
    __slots__ = (
        'w',
        'u_draw',
        'items',
        'box_area',
        'box_region',
        'box_scroll_bg',
        'box_scroll',
        'scissor',
        'headkey',
        'endkey',
        'draw_range',
        'active_tab',
        'cv_height',
        'head_T',
        'focus_element',
        'r_size_default',
        'attributes',
        'width_input')

    # //* 0area_AreaBlock_upd_scissor
    # *//

    @staticmethod
    def calc_height_by_len(column_len):
        return column_len * D_SIZE['widget_full_h'] + (column_len - 1) * SIZE_button[1] + (SIZE_dd_border[0] + SIZE_border[3]) * 2
        #|
    @staticmethod
    def calc_height_by_block_len(column_len):
        return SIZE_block[4] + SIZE_block[3] + column_len * D_SIZE['widget_full_h'] + (column_len - 1) * SIZE_button[1] + (SIZE_dd_border[0] + SIZE_border[3]) * 2
        #|

    def __init__(self, w, LL, RR, BB, TT, r_size_default=None):
        self.w = w
        self.u_draw = self.i_draw

        self.scissor = Scissor()
        self.box_area = GpuBox_area()
        self.box_region = GpuRimArea()
        self.box_scroll_bg = GpuBox(COL_box_block_scrollbar_bg)
        self.box_scroll = GpuBox(COL_box_block_scrollbar)

        self.items = []
        self.headkey = 0
        self.endkey = -1
        self.draw_range = range(0)

        if r_size_default is None:
            self.r_size_default = lambda: (D_SIZE['widget_width'] * 2, ) * 2
        else:
            self.r_size_default = r_size_default

        # <<< 1copy (0area_AreaBlock_init_size,, $$)
        box_area = self.box_area
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        d1 = SIZE_border[3]
        L0 = LL + d0
        T0 = TT - d0

        self.box_region.LRBT_upd(L0, RR - d0, BB + d0, T0, d1)
        # <<< 1copy (0area_AreaBlock_upd_scissor,, $$)
        e_ = self.box_region.inner
        scroll_width = min(SIZE_widget[2], SIZE_widget[0])
        self.scissor.intersect_with(self.w.scissor, e_[0], e_[1] - scroll_width, e_[2], e_[3])
        # >>>

        L, R, B, T = e_
        self.head_T = T
        L = R - scroll_width
        self.box_scroll_bg.LRBT_upd(L, R, B, T)
        self.box_scroll.LRBT_upd(L, R, B, T)
        self.width_input = self.r_width_input(None)
        if hasattr(self, 'upd_size_callback'):
            self.upd_size_callback()
        # >>>
        #|

    def upd_size(self, LL, RR, BB, TT, use_resize_upd_end=True):
        # /* 0area_AreaBlock_init_size
        box_area = self.box_area
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        d1 = SIZE_border[3]
        L0 = LL + d0
        T0 = TT - d0

        self.box_region.LRBT_upd(L0, RR - d0, BB + d0, T0, d1)
        # <<< 1copy (0area_AreaBlock_upd_scissor,, $$)
        e_ = self.box_region.inner
        scroll_width = min(SIZE_widget[2], SIZE_widget[0])
        self.scissor.intersect_with(self.w.scissor, e_[0], e_[1] - scroll_width, e_[2], e_[3])
        # >>>

        L, R, B, T = e_
        self.head_T = T
        L = R - scroll_width
        self.box_scroll_bg.LRBT_upd(L, R, B, T)
        self.box_scroll.LRBT_upd(L, R, B, T)
        self.width_input = self.r_width_input(None)
        if hasattr(self, 'upd_size_callback'):
            self.upd_size_callback()
        # */

        if use_resize_upd_end is True:
            self.resize_upd_end()
        #|

    def init_draw_range(self):
        block_gap = SIZE_block[0]
        LL, RR, BB, TT = self.box_region.inner
        self.head_T = TT
        RR -= min(SIZE_widget[2], SIZE_widget[0])
        r = -1

        for r, item in enumerate(self.items):
            TT = item.init_bat(LL, RR, TT) - block_gap
            if TT < BB: break

        self.headkey = 0
        self.endkey = r
        self.draw_range = range(r + 1)
        #|
    def init_items_tab(self):
        self.init_draw_range()
        self.get_cv_height()
        self.r_upd_scroll()()
        #|

    def r_width_input(self, button):
        e = self.box_region.inner
        return e[1] - e[0] - min(SIZE_widget[2], SIZE_widget[0])
        #|

    def inside_evt(self):

        self.redraw_scrollbar()
        #|
    def r_focus_element(self):
        items = self.items
        e = None
        y = MOUSE[1]

        for r in self.draw_range:
            box_block = items[r].box_block
            if box_block.B <= y < box_block.T:
                e = items[r]
                break
        return e
        #|
    def modal_focus_element_front(self, _e_):
        if self.scroll_events(): return True

        if self.box_scroll_bg.inbox(MOUSE):
            if self.scroll_area_events(): return True
        return False
        #|
    def modal_focus_element_back(self, _e_):
        if TRIGGER['rm']():
            self.to_modal_rm()
            return True
        if TRIGGER['pan']():
            self.to_modal_pan()
            return True
        if TRIGGER['fold_all_toggle']():
            self.evt_fold_all_toggle()
            return True
        if hasattr(self.w, "evt_search"):
            if TRIGGER['area_search']():
                self.w.evt_search()
                return True
        if hasattr(self.w, "evt_undo"):
            if TRIGGER['redo']():
                self.w.evt_redo()
                return True
            if TRIGGER['undo']():
                self.w.evt_undo()
                return True
        if hasattr(self, "evt_search"):
            if TRIGGER['area_search']():
                self.evt_search()
                return True
        if self.scroll_area_events(False): return True
        return False
        #|

    def to_modal_pan(self): # self.endkey != -1

        #|
        if self.headkey >= len(self.items): return

        end_trigger = r_end_trigger('pan')
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop()
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        # /* 0area_AreaBlock_pan_get
        sci = self.scissor
        L, R, B, T = self.box_region.inner
        he = T - B

        _li = self.items
        _max_endkey = len(_li) - 1
        _gap = SIZE_block[0]
        _lim_L = sci.x
        _lim_R = _lim_L + sci.w
        _lim_B = sci.y
        _lim_T = _lim_B + sci.h
        _T_add = _lim_B + he
        _B_add = _lim_T - he

        _upd_scroll = self.r_upd_scroll()
        # */

        if self.focus_element is not None:
            self.focus_element.box_block.color = COL_block

        def end_modal_pan():
            mouseloop_end()
            kill_evt_except()
            self.upd_data()

        def modal_pan():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dx, dy = r_dxy_mouse()

            # /* 0area_AreaBlock_modal_pan
            bo0 = _li[self.headkey].box_block

            if dx < 0:
                R = bo0.R + dx
                if R < _lim_R:
                    dx -= R - _lim_R
                    L = bo0.L + dx
                    if L > _lim_L: dx -= L - _lim_L
            else:
                L = bo0.L + dx
                if L > _lim_L: dx -= L - _lim_L

            if dy < 0:
                headkey = self.headkey
                if headkey == 0:
                    T = bo0.T + dy
                    if T < _lim_T: dy -= T - _lim_T
                else:
                    B = bo0.T + _gap
                    L = bo0.L
                    R = bo0.R
                    width = R - L
                    while B + dy <= _lim_T:
                        if headkey == 0: break

                        headkey -= 1
                        e = _li[headkey]
                        T1 = B + e.r_height(width)
                        e.init_bat(L, R, T1)
                        B = T1 + _gap

                    if headkey == 0:
                        T = _li[0].box_block.T + dy
                        if T < _lim_T: dy -= T - _lim_T

                    r = self.endkey
                    T = _li[r].box_block.T

                    while T + dy < _B_add:

                        r -= 1
                        if r == 0: break
                        T = _li[r].box_block.T
                    self.endkey = r

                    self.headkey = headkey
                    self.draw_range = range(headkey, r + 1)

            else:
                endkey = self.endkey
                bo1 = _li[endkey].box_block

                T = bo1.B - _gap
                L = bo1.L
                R = bo1.R
                while T + dy >= _lim_B:
                    if endkey == _max_endkey: break

                    endkey += 1
                    T = _li[endkey].init_bat(L, R, T) - _gap

                r = self.headkey
                B = _li[r].box_block.B

                if endkey == _max_endkey:
                    new_y = _li[endkey].box_block.B + dy
                    if new_y > _lim_B:
                        dy = max(0, dy - new_y + _lim_B)

                if r == endkey: pass
                else:
                    while B + dy > _T_add:

                        r += 1
                        if r == endkey: break
                        B = _li[r].box_block.B

                self.headkey = r

                self.endkey = endkey
                self.draw_range = range(r, endkey + 1)


            for r in self.draw_range: _li[r].dxy(dx, dy)

            self.head_T += dy
            _upd_scroll()
            # */
            mouseloop()

        w_head = Head(self, modal_pan, end_modal_pan)
        _REDRAW()
        #|
    def r_pan_override(self):
        if self.headkey >= len(self.items):
            return lambda dx, dy: (0, 0)

        # <<< 1copy (0area_AreaBlock_pan_get,, $$)
        sci = self.scissor
        L, R, B, T = self.box_region.inner
        he = T - B

        _li = self.items
        _max_endkey = len(_li) - 1
        _gap = SIZE_block[0]
        _lim_L = sci.x
        _lim_R = _lim_L + sci.w
        _lim_B = sci.y
        _lim_T = _lim_B + sci.h
        _T_add = _lim_B + he
        _B_add = _lim_T - he

        _upd_scroll = self.r_upd_scroll()
        # >>>

        def pan_override(dx, dy):
            # <<< 1copy (0area_AreaBlock_modal_pan,, $$)
            bo0 = _li[self.headkey].box_block

            if dx < 0:
                R = bo0.R + dx
                if R < _lim_R:
                    dx -= R - _lim_R
                    L = bo0.L + dx
                    if L > _lim_L: dx -= L - _lim_L
            else:
                L = bo0.L + dx
                if L > _lim_L: dx -= L - _lim_L

            if dy < 0:
                headkey = self.headkey
                if headkey == 0:
                    T = bo0.T + dy
                    if T < _lim_T: dy -= T - _lim_T
                else:
                    B = bo0.T + _gap
                    L = bo0.L
                    R = bo0.R
                    width = R - L
                    while B + dy <= _lim_T:
                        if headkey == 0: break

                        headkey -= 1
                        e = _li[headkey]
                        T1 = B + e.r_height(width)
                        e.init_bat(L, R, T1)
                        B = T1 + _gap

                    if headkey == 0:
                        T = _li[0].box_block.T + dy
                        if T < _lim_T: dy -= T - _lim_T

                    r = self.endkey
                    T = _li[r].box_block.T

                    while T + dy < _B_add:

                        r -= 1
                        if r == 0: break
                        T = _li[r].box_block.T
                    self.endkey = r

                    self.headkey = headkey
                    self.draw_range = range(headkey, r + 1)

            else:
                endkey = self.endkey
                bo1 = _li[endkey].box_block

                T = bo1.B - _gap
                L = bo1.L
                R = bo1.R
                while T + dy >= _lim_B:
                    if endkey == _max_endkey: break

                    endkey += 1
                    T = _li[endkey].init_bat(L, R, T) - _gap

                r = self.headkey
                B = _li[r].box_block.B

                if endkey == _max_endkey:
                    new_y = _li[endkey].box_block.B + dy
                    if new_y > _lim_B:
                        dy = max(0, dy - new_y + _lim_B)

                if r == endkey: pass
                else:
                    while B + dy > _T_add:

                        r += 1
                        if r == endkey: break
                        B = _li[r].box_block.B

                self.headkey = r

                self.endkey = endkey
                self.draw_range = range(r, endkey + 1)


            for r in self.draw_range: _li[r].dxy(dx, dy)

            self.head_T += dy
            _upd_scroll()
            # >>>
            return dx, dy
        return pan_override
        #|

    def evt_scrollX(self, dx):

        kill_evt_except()
        if self.endkey == -1: return
        self.r_pan_override()(dx, 0)
        Admin.REDRAW()
        #|
    def evt_scrollY(self, dy):

        kill_evt_except()
        if self.endkey == -1: return
        self.r_pan_override()(0, dy)
        Admin.REDRAW()
        #|
    def to_modal_scrollbar(self):

        if self.endkey == -1: return

        end_trigger = r_end_trigger('dd_scroll')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        _mou = MOUSE[:]
        _scrollbar = self.box_scroll
        _pan_override = self.r_pan_override()

        # <<< 1copy (0area_AreaBlock_fn_cvY_fac,, ${
        #     'fn_cvY_fac = rf_linear_01': 'fn_cvY_fac, _fn_cvY_fac_inv = rf_linear_01_inv'}$)
        box_scroll = self.box_scroll
        L, R, B, T = self.box_scroll_bg.r_LRBT()

        sci = self.scissor
        sci_h = sci.h
        B = sci.y
        T = B + sci_h
        items = self.items
        len_items = len(items)

        bar_h_min = D_SIZE['widget_full_h'] // 2
        cv_h = self.cv_height
        bar_h = T - B
        button_h = min(max(floor(bar_h * sci_h / cv_h), bar_h_min), bar_h)
        barY_dif = bar_h - button_h

        fn_cvY_fac, _fn_cvY_fac_inv = rf_linear_01_inv(T, B + cv_h)
        # >>>

        _fn_scroll_fac = rf_linear_01(
            sci.y + sci.h,
            sci.y + button_h)

        if _scrollbar.inbox(MOUSE) == False:
            # <<< 1copy (0area_AreaBlock_i_modal_scrollbar,, ${
            #     'MOUSE[1] - _mou[1]': 'MOUSE[1] + button_h // 2 - _scrollbar.T'
            # }$)
            _pan_override(0, round(_fn_cvY_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.T + MOUSE[1] + button_h // 2 - _scrollbar.T)), 1.0)) - self.head_T))
            # >>>

        def modal_scrollbar():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            # dy = MOUSE[1] - _mou[1]
            # fac = min(max(0.0, _fn_scroll_fac(_scrollbar.T + dy)), 1.0)
            # T = _fn_cvY_fac_inv(fac)
            # dy = T - self.head_T
            # _pan_override(0, round(dy))

            # /* 0area_AreaBlock_i_modal_scrollbar
            _pan_override(0, round(_fn_cvY_fac_inv(min(max(0.0, _fn_scroll_fac(_scrollbar.T + MOUSE[1] - _mou[1])), 1.0)) - self.head_T))
            # */

            _mou[:] = MOUSE

        def end_modal_scrollbar():
            _REDRAW()
            kill_evt_except()

        w_head = Head(self, modal_scrollbar, end_modal_scrollbar)
        _REDRAW()
        #|

    def to_modal_rm(self):

        items = [
            ("pan", self.to_modal_pan),
            ("Unfold All", self.evt_unfold_all),
            ("Fold All", self.evt_fold_all),
            ("fold_all_toggle", self.evt_fold_all_toggle),
        ]

        if hasattr(self.w, "evt_undo"):
            items.append(("redo", self.w.evt_redo))
            items.append(("undo", self.w.evt_undo))
        if hasattr(self, "evt_search"):
            items.append(("area_search", self.evt_search))
        DropDownRMKeymap(self, MOUSE, items)
        #|

    def evt_unfold_all(self, recursive=False):

        kill_evt_except()
        if len(self.draw_range) == 0: return

        for e in self.items:
            if hasattr(e, "init_unfold"): e.init_unfold(recursive=recursive)

        Admin.REDRAW()
        self.redraw_from_headkey()
        if hasattr(self, "upd_data_callback"): self.upd_data_callback()
        #|
    def evt_fold_all(self, recursive=False):

        kill_evt_except()

        if len(self.draw_range) == 0: return

        items = self.items
        for e in items:
            if hasattr(e, "init_fold"): e.init_fold(recursive=recursive)

        Admin.REDRAW()
        self.redraw_from_headkey()

        if self.endkey == len(self.items) - 1:
            sci = self.scissor
            B = items[self.endkey].box_block.B
            if B > sci.y:
                self.r_pan_override()(0, sci.y - B)

        if hasattr(self, "upd_data_callback"): self.upd_data_callback()
        #|
    def evt_fold_all_toggle(self):
        if all(e.is_fold  for e in self.items if hasattr(e, "is_fold")):
            self.evt_unfold_all()
        else: self.evt_fold_all()
        #|

    def get_cv_height(self):

        if self.items:
            item0 = self.items[self.headkey]
            width = item0.box_block.R - item0.box_block.L
            self.cv_height = sum(e.r_height(width)  for e in self.items) + SIZE_block[0] * (len(self.items) - 1)
        else:
            self.cv_height = 0
        #|
    def r_upd_scroll(self): # need box_scroll_bg, self.cv_height
        if self.endkey == -1:
            box_scroll_LRBT_upd = self.box_scroll.LRBT_upd
            box_scroll_bg_r_LRBT = self.box_scroll_bg.r_LRBT

            def upd_scroll():
                box_scroll_LRBT_upd(*box_scroll_bg_r_LRBT())

            return upd_scroll

        # /* 0area_AreaBlock_fn_cvY_fac
        box_scroll = self.box_scroll
        L, R, B, T = self.box_scroll_bg.r_LRBT()

        sci = self.scissor
        sci_h = sci.h
        B = sci.y
        T = B + sci_h
        items = self.items
        len_items = len(items)

        bar_h_min = D_SIZE['widget_full_h'] // 2
        cv_h = self.cv_height
        bar_h = T - B
        button_h = min(max(floor(bar_h * sci_h / cv_h), bar_h_min), bar_h)
        barY_dif = bar_h - button_h

        fn_cvY_fac = rf_linear_01(T, B + cv_h)
        # */

        box_scroll_LRBT_upd = box_scroll.LRBT_upd

        def upd_scroll():
            T0 = T - max(round(fn_cvY_fac(self.head_T) * barY_dif), 0)
            box_scroll_LRBT_upd(L, R, T0 - button_h, T0)

        return upd_scroll
        #|
    def redraw_scrollbar(self):
        Admin.REDRAW()
        self.get_cv_height()
        self.r_upd_scroll()()
        #|
    def redraw_from_headkey(self, fix_pan=False):
        items = self.items
        if items:
            r = self.headkey
            if r >= len(items):
                r = 0
                self.headkey = 0

            e0 = items[r]
            L, R, B, T = e0.box_block.r_LRBT()
            if T < self.box_region.inner[3]:
                r = 0
                self.headkey = 0
                e0 = items[r]
                L, R, B, T = e0.box_block.r_LRBT()

            R = L + self.box_region.inner[1] - self.box_region.inner[0] - min(SIZE_widget[2], SIZE_widget[0])
            head_T = T

            _li = self.items
            _max_endkey = len(_li) - 1
            _gap = SIZE_block[0]
            _lim_B = self.scissor.y

            T = items[r].init_bat(L, R, T) - _gap
            while T >= _lim_B:
                if r == _max_endkey: break
                r += 1
                T = items[r].init_bat(L, R, T) - _gap

            self.endkey = r
            self.draw_range = range(self.headkey, r + 1)

            if self.headkey == 0:
                self.head_T = head_T
            else:
                width = R - L
                self.head_T = head_T + sum(items[i].r_height(width)  for i in range(self.headkey)) + _gap * self.headkey

            self.redraw_scrollbar()

        if len(self.draw_range) == 0: return

        if items[self.endkey].box_block.B - SIZE_widget[0] > self.box_region.inner[3]:
            self.init_draw_range()
            return

        if fix_pan is False: return

        e0 = self.items[self.headkey].box_block
        sci = self.scissor
        L = sci.x
        R = L + sci.w
        B = sci.y
        T = B + sci.h

        if e0.L > L: dx = 1
        elif e0.R < R: dx = -1
        else: dx = 0

        if e0.T < T: dy = -1
        else:
            e0 = self.items[self.endkey].box_block
            if e0.B > B: dy = 1
            else: dy = 0

        if dx or dy:
            self.r_pan_override()(dx, dy)
        #|
    def resize_upd_end(self, override=None):
        if override is None:
            if hasattr(self.w, "areas") and P.adaptive_win_resize and hasattr(self.w, "r_area_posRB_adaptive"):
                posR, posB = self.w.r_area_posRB_adaptive(self)

                if posR == self.box_area.R and posB == self.box_area.B: pass
                else:
                    e = self.box_area
                    sizeXmin, sizeYmin = self.r_size_default()

                    if posR != e.R:
                        posR = max(posR, e.L + sizeXmin)
                    if posB != e.B:
                        posB = min(posB, e.T - sizeYmin)

                    self.upd_size(
                        e.L,
                        posR,
                        posB,
                        e.T,
                        use_resize_upd_end = False)
        else:
            self.upd_size(*override,
                use_resize_upd_end = False)

        self.redraw_from_headkey(True)
        self.upd_data()
        #|

    def dxy(self, dx, dy):
        self.head_T += dy
        self.box_area.dxy_upd(dx, dy)
        self.box_region.dxy_upd(dx, dy)
        self.box_scroll_bg.dxy_upd(dx, dy)
        self.box_scroll.dxy_upd(dx, dy)
        # <<< 1copy (0area_AreaBlock_upd_scissor,, $$)
        e_ = self.box_region.inner
        scroll_width = min(SIZE_widget[2], SIZE_widget[0])
        self.scissor.intersect_with(self.w.scissor, e_[0], e_[1] - scroll_width, e_[2], e_[3])
        # >>>

        items = self.items
        for r in self.draw_range: items[r].dxy(dx, dy)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        self.box_region.bind_draw()
        self.box_scroll_bg.bind_draw()
        self.box_scroll.bind_draw()

        self.scissor.use()
        items = self.items
        for r in self.draw_range: items[r].draw_box()

        blfSize(FONT0, D_SIZE['font_main'])
        for r in self.draw_range: items[r].draw_blf()
        self.w.scissor.use()
        #|

    def upd_data(self):
        for e in self.items: e.upd_data()
        #|
    #|
    #|
class AreaBlockTab(AreaBlock):
    __slots__ = ()

    def init_tab(self, tab, push=True, evtkill=True):
        if hasattr(self, "upd_data_callback"): self.upd_data_callback = N
        if evtkill: kill_evt_except()
        self.items.clear()

        if tab == None:
            self.active_tab = None
            self.init_items_tab()
            return

        self.w.active_tab = tab
        self.active_tab = tab

        try:
            getattr(self, f"init_tab_{'_'.join(tab)}", self.init_tab_except)()
        except:
            self.items.clear()
            from . m import call_bug_report_dialog
            call_bug_report_dialog()

        self.init_items_tab()

        if push: self.tabhistory_push()
        #|
    def init_tab_except(self): pass

    def tabhistory_push(self): pass

    def upd_data(self):
        if self.active_tab == self.w.active_tab:
            for e in self.items: e.upd_data()
        else:

            self.init_tab(self.w.active_tab)

            for e in self.items: e.upd_data()
        #|
    #|
    #|
class AreaBlockSimple(StructAreaModal):
    __slots__ = (
        'w',
        'u_draw',
        'items',
        'box_area',
        'box_region',
        'focus_element',
        'r_size_default',
        'attributes')

    def __init__(self, w, LL, RR, BB, TT, r_size_default=None):
        self.w = w
        self.u_draw = self.i_draw

        self.box_area = GpuBox_area()
        self.box_region = GpuRimArea()

        if r_size_default is None: pass
        else:
            self.r_size_default = r_size_default

        self.items = []
        self.upd_size(LL, RR, BB, TT)
        #|

    def r_width_input(self, button):
        e = self.box_region.inner
        return e[1] - e[0] - min(SIZE_widget[2], SIZE_widget[0])
        #|

    def upd_size(self, LL, RR, BB, TT):
        self.box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        widget_rim = SIZE_border[3]

        self.box_region.LRBT_upd(LL + d0, RR - d0, BB + d0, TT - d0, widget_rim)

        block_gap = SIZE_block[0]
        LL, RR, BB, TT = self.box_region.inner

        for item in self.items:
            TT = item.init_bat(LL, RR, TT) - block_gap
        #|

    def init_draw_range(self):
        block_gap = SIZE_block[0]
        LL, RR, BB, TT = self.box_region.inner

        for item in self.items:
            TT = item.init_bat(LL, RR, TT) - block_gap
        #|

    def r_focus_element(self):
        e = None
        y = MOUSE[1]

        for item in self.items:
            box_block = item.box_block
            if box_block.B <= y < box_block.T:
                e = item
                break
        return e
        #|

    def redraw_scrollbar(self): pass
    def redraw_from_headkey(self): pass
    def resize_upd_end(self, override=None):
        if override is None:
            if hasattr(self.w, "areas") and P.adaptive_win_resize and hasattr(self, "r_size_default") and hasattr(self.w, "r_area_posRB_adaptive"):
                posR, posB = self.w.r_area_posRB_adaptive(self)

                if posR == self.box_area.R and posB == self.box_area.B: pass
                else:
                    e = self.box_area
                    sizeXmin, sizeYmin = self.r_size_default()

                    if posR != e.R:
                        posR = max(posR, e.L + sizeXmin)
                    if posB != e.B:
                        posB = min(posB, e.T - sizeYmin)

                    self.upd_size(
                        e.L,
                        posR,
                        posB,
                        e.T)
        else:
            self.upd_size(*override)
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)
        self.box_region.dxy_upd(dx, dy)

        for e in self.items: e.dxy(dx, dy)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        self.box_region.bind_draw()

        for e in self.items: e.draw_box()

        blfSize(FONT0, D_SIZE['font_main'])
        for e in self.items: e.draw_blf()
        #|

    def upd_data(self):
        for e in self.items: e.upd_data()
        #|
    #|
    #|
class AreaBlockHead(AreaBlockSimple):
    __slots__ = ()

    def __init__(self, w, LL, RR, BB, TT, r_size_default=None):
        self.w = w
        self.u_draw = self.i_draw

        self.box_area = GpuBox_area()
        self.box_region = GpuRim(COL_box_area_header_bg, COL_box_area_header_bg)

        if r_size_default is None: pass
        else:
            self.r_size_default = r_size_default

        self.items = []
        self.upd_size(LL, RR, BB, TT)
        #|
    #|
    #|
class AreaBlockFiltHead(AreaBlockSimple):
    __slots__ = ()

    def __init__(self, w, LL, RR, BB, TT, items, r_size_default=None):
        self.w = w
        self.u_draw = self.i_draw

        self.box_area = GpuBox_area()
        self.box_region = GpuRimArea()

        if r_size_default is None: pass
        else:
            self.r_size_default = r_size_default

        self.items = items
        items[0].w = self

        self.upd_size(LL, RR, BB, TT)
        #|

    def upd_size(self, LL, RR, BB, TT):
        self.box_area.LRBT(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]

        self.box_region.LRBT(LL + d0, RR - d0, BB + d0, TT - d0, SIZE_border[3])

        LL, RR, BB, TT = self.box_region.inner
        self.items[0].init_bat(LL, RR, TT)
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy(dx, dy)
        self.box_region.dxy(dx, dy)

        self.items[0].dxy(dx, dy)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        # self.box_area.bind_draw()
        # self.box_region.bind_draw()

        self.items[0].draw_box()

        # blfSize(FONT0, D_SIZE['font_main'])
        self.items[0].draw_blf()
        #|

    def upd_data(self):
        self.items[0].upd_data()
        #|
    #|
    #|

class AreaBlock1:
    __slots__ = (
        'w',
        'u_draw',
        'item',
        'box_area')

    def __init__(self, w, LL, RR, BB, TT, item):
        self.w = w
        self.u_draw = self.i_draw

        self.box_area = GpuBox_area()

        self.item = item
        item.w = self

        self.upd_size(LL, RR, BB, TT)
        #|

    def upd_size(self, LL, RR, BB, TT):
        self.box_area.LRBT_upd(LL, RR, self.item.init_bat(LL, RR, TT), TT)
        #|

    def modal(self):
        pass
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)

        self.item.dxy(dx, dy)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()

        self.item.draw_box()

        blfSize(FONT0, D_SIZE['font_main'])
        self.item.draw_blf()
        #|

    def upd_data(self): pass
    #|
    #|

class AreaColorHue:
    __slots__ = (
        'w',
        'u_draw',
        'box_area',
        'box_button_H_bg',
        'box_button_SV_bg',
        'box_button_H',
        'box_button_SV',
        'box_button_media_H',
        'box_button_media_SV',
        'modal_drag_H_callback',
        'modal_drag_SV_callback',
        'update_button_media_enable')

    def __init__(self, w, LL, RR, BB, TT, modal_drag_H_callback, modal_drag_SV_callback):
        self.w = w
        self.u_draw = self.i_draw

        self.box_area = GpuBox()
        self.box_button_H = GpuPickerH()
        self.box_button_SV = GpuPickerSV()
        self.box_button_H_bg = GpuBox(COL_box_hue_bg)
        self.box_button_SV_bg = GpuBox(COL_box_hue_bg)
        self.box_button_media_H = GpuImg_hue_button()
        self.box_button_media_SV = GpuImg_hue_cursor()
        self.modal_drag_H_callback = modal_drag_H_callback
        self.modal_drag_SV_callback = modal_drag_SV_callback
        self.update_button_media_enable = True

        self.upd_size(LL, RR, BB, TT)
        #|

    def upd_size(self, LL, RR, BB, TT):
        self.box_area.LRBT(LL, RR, BB, TT)

        widget_rim = SIZE_border[3]
        outer = SIZE_dd_border[0] + widget_rim + SIZE_block[2]
        T = TT - outer
        B = BB + outer
        hue_height = T - B
        L = LL + outer
        R0 = L + hue_height
        self.box_button_SV.LRBT_upd(L, R0, B, T)
        self.box_button_SV_bg.LRBT_upd(L - widget_rim, R0 + widget_rim, B - widget_rim, T + widget_rim)
        L0 = R0 + SIZE_button[2] + (widget_rim + SIZE_button[1]) * 2
        R = L0 + SIZE_widget[0]
        self.box_button_H.LRBT_upd(L0, R, B, T)
        self.box_button_H_bg.LRBT_upd(L0 - widget_rim, R + widget_rim, B - widget_rim, T + widget_rim)
        self.box_button_media_H.upd()
        self.box_button_media_SV.upd()
        #|

    def modal(self):
        L, R, B, T = self.box_button_H.r_LRBT()
        R = self.box_button_media_H.R
        if L <= MOUSE[0] < R and B <= MOUSE[1] < T:
            if TRIGGER['click']():
                self.to_modal_drag_H()
                return
        elif self.box_button_SV.inbox(MOUSE):
            if TRIGGER['click']():
                self.to_modal_drag_SV()
                return
        #|

    def to_modal_drag_H(self, end_trigger="click"):
        _REDRAW = Admin.REDRAW
        _TRIGGER_esc = TRIGGER['esc']
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_valbox_drag_modal_fast = TRIGGER['valbox_drag_modal_fast']
        _TRIGGER_valbox_drag_modal_slow = TRIGGER['valbox_drag_modal_slow']
        end_trigger = r_end_trigger(end_trigger)
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop(loop_type="NONE", cursor_icon="NONE")
        _xy = [0.0, 0.0]

        _button = self.box_button_media_H
        _h_half = ceil(SIZE_widget[0] / 2)
        _max_y = self.box_button_H.T
        _min_y = self.box_button_H.B
        _max_size = _max_y - _min_y
        modal_drag_H_callback = self.modal_drag_H_callback

        self.update_button_media_enable = False

        def _end_modal():
            mouseloop_end((None, r_mouse_from_region(0, self.box_button_media_H.T - ceil(SIZE_widget[0] / 2))[1]))
            kill_evt_except()
            self.update_button_media_enable = True

        def _modal():
            # <<< 1copy (head_end_trigger_mouse_fast_slow_travel,, $$)
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return
            dx, dy = r_dxy_mouse()
            if _TRIGGER_valbox_drag_modal_fast():
                dx *= 10
                dy *= 10
            elif _TRIGGER_valbox_drag_modal_slow():
                dx *= 0.1
                dy *= 0.1

            _xy[0] += dx
            _xy[1] += dy
            travel_x, travel_y = _xy
            if travel_x >= 1.0:
                dx = floor(travel_x)
                _xy[0] -= dx
            elif travel_x <= -1.0:
                dx = ceil(travel_x)
                _xy[0] -= dx
            else: dx = 0
            if travel_y >= 1.0:
                dy = floor(travel_y)
                _xy[1] -= dy
            elif travel_y <= -1.0:
                dy = ceil(travel_y)
                _xy[1] -= dy
            else: dy = 0
            # >>>
            if dy:
                y = min(max(_min_y, _button.T - _h_half + int(dy)), _max_y)
                _button.B = y - _h_half
                _button.T = y + _h_half
                _button.upd()
                hue = (y - _min_y) / _max_size
                modal_drag_H_callback(hue)
                self.box_button_SV.hue = hue
            mouseloop()
            #|

        dy0 = MOUSE[1] - _button.T + _h_half
        y0 = min(max(_min_y, _button.T - _h_half + dy0), _max_y)
        _button.B = y0 - _h_half
        _button.T = y0 + _h_half
        _button.upd()
        hue = (y0 - _min_y) / _max_size
        modal_drag_H_callback(hue)
        self.box_button_SV.hue = hue

        w_head = Head(self, _modal, _end_modal)
        _REDRAW()
        #|
    def to_modal_drag_SV(self, end_trigger="click"):
        _REDRAW = Admin.REDRAW
        _TRIGGER_esc = TRIGGER['esc']
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_valbox_drag_modal_fast = TRIGGER['valbox_drag_modal_fast']
        _TRIGGER_valbox_drag_modal_slow = TRIGGER['valbox_drag_modal_slow']
        end_trigger = r_end_trigger(end_trigger)
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop(loop_type="NONE", cursor_icon="NONE")
        _xy = [0.0, 0.0]

        _button = self.box_button_media_SV
        _h_half = ceil(SIZE_widget[0] / 2)
        _min_x, _max_x, _min_y, _max_y = self.box_button_SV.r_LRBT()
        _max_size_x = _max_x - _min_x
        _max_size_y = _max_y - _min_y
        modal_drag_SV_callback = self.modal_drag_SV_callback

        self.update_button_media_enable = None

        def _end_modal():
            _h_half = ceil(SIZE_widget[0] / 2)
            mouseloop_end(r_mouse_from_region(
                self.box_button_media_SV.L + _h_half, self.box_button_media_SV.T - _h_half))
            kill_evt_except()
            self.update_button_media_enable = True

        def _modal():
            # <<< 1copy (head_end_trigger_mouse_fast_slow_travel,, $$)
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return
            dx, dy = r_dxy_mouse()
            if _TRIGGER_valbox_drag_modal_fast():
                dx *= 10
                dy *= 10
            elif _TRIGGER_valbox_drag_modal_slow():
                dx *= 0.1
                dy *= 0.1

            _xy[0] += dx
            _xy[1] += dy
            travel_x, travel_y = _xy
            if travel_x >= 1.0:
                dx = floor(travel_x)
                _xy[0] -= dx
            elif travel_x <= -1.0:
                dx = ceil(travel_x)
                _xy[0] -= dx
            else: dx = 0
            if travel_y >= 1.0:
                dy = floor(travel_y)
                _xy[1] -= dy
            elif travel_y <= -1.0:
                dy = ceil(travel_y)
                _xy[1] -= dy
            else: dy = 0
            # >>>
            if dx or dy:
                x = min(max(_min_x, _button.L + _h_half + int(dx)), _max_x)
                y = min(max(_min_y, _button.T - _h_half + int(dy)), _max_y)
                _button.LRBT_upd(x - _h_half, x + _h_half, y - _h_half, y + _h_half)
                modal_drag_SV_callback((x - _min_x) / _max_size_x, (y - _min_y) / _max_size_y)
            mouseloop()
            #|

        dx = MOUSE[0] - _button.L - _h_half
        dy = MOUSE[1] - _button.T + _h_half
        x = min(max(_min_x, _button.L + _h_half + dx), _max_x)
        y = min(max(_min_y, _button.T - _h_half + dy), _max_y)
        _button.LRBT_upd(x - _h_half, x + _h_half, y - _h_half, y + _h_half)
        modal_drag_SV_callback((x - _min_x) / _max_size_x, (y - _min_y) / _max_size_y)

        w_head = Head(self, _modal, _end_modal)
        _REDRAW()
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy(dx, dy)
        self.box_button_SV_bg.dxy_upd(dx, dy)
        self.box_button_SV.dxy_upd(dx, dy)
        self.box_button_H_bg.dxy_upd(dx, dy)
        self.box_button_H.dxy_upd(dx, dy)
        self.box_button_media_H.dxy_upd(dx, dy)
        self.box_button_media_SV.dxy_upd(dx, dy)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_button_SV_bg.bind_draw()
        self.box_button_SV.bind_draw()
        self.box_button_H_bg.bind_draw()
        self.box_button_H.bind_draw()
        self.box_button_media_H.bind_draw()
        self.box_button_media_SV.bind_draw()
        #|

    def update_button_media(self, hsv):
        if self.update_button_media_enable == True:
            h = SIZE_widget[0]
            h_half = ceil(h / 2)
            e = self.box_button_H

            hue = hsv[0] % 1.0
            y = round((e.T - e.B) * hue + e.B)
            self.box_button_media_H.LRBT_upd(e.R, e.R + h_half * 2, y - h_half, y + h_half)
            self.box_button_SV.hue = hue

            e = self.box_button_SV
            x = round((e.R - e.L) * min(max(0.0, hsv[1]), 1.0) + e.L)
            y = round((e.T - e.B) * min(max(0.0, hsv[2]), 1.0) + e.B)
            self.box_button_media_SV.LRBT_upd(x - h_half, x + h_half, y - h_half, y + h_half)
        elif self.update_button_media_enable == False:
            self.box_button_SV.hue = hsv[0] % 1.0
        #|

    def upd_data(self): pass
    #|
    #|


class FilterYObject(FilterY):
    __slots__ = ()

    def init_items(self): # NEed ITems_unsort
        self.items = self.items_unsort
        self.names = {(e.name, e.library.filepath)  if e.library else e.name: r  for r, e in enumerate(self.items)}
        #|
    #|
    #|
class AreaFilterYObject(AreaFilterY):
    __slots__ = ()

    def __init__(self, w, LL, RR, BB, TT, r_size_default=None): # Need BlendDataTemp.init(), BlendDataTemp.kill()

        super().__init__(w, LL, RR, BB, TT,
            BlendDataTemp.r_upd_objects,
            get_icon = geticon_Object,
            get_info = getinfo_Object,
            filter_cls = FilterYObject,
            r_size_default = r_size_default
        )
        self.filt.set_active_index_callback = self.w.set_active_object
        #|

    def upd_data(self): # Need BlendDataTemp.init(), BlendDataTemp.kill()
        super().upd_data()
        ob = self.w.active_object
        if ob:
            if ob.library:
                self.filt.upd_active_index(self.filt.names.get((ob.name, ob.library.filepath), None))
            else:
                self.filt.upd_active_index(self.filt.names.get(ob.name, None))
        else:
            self.filt.upd_active_index(None)
        #|
    #|
    #|

class FilterYModifier(FilterY):
    __slots__ = 'icons_button', 'blfs_num', 'box_hover_button', 'selnames', 'box_selections'

    def __init__(self, w, get_items, get_icon, get_info):
        self.icons_button = {}
        self.blfs_num = {}
        self.selnames = {}
        self.box_selections = {}
        self.box_hover_button = GpuImg_MD_BG_SHOW_HOVER()
        self.box_hover_button.set_draw_state(False)

        super().__init__(w, get_items, geticon_Modifier, None)
        #|

    def upd_size(self):
        # ref_FilterY_upd_size
        match_items = self.match_items
        len_match_items = len(match_items)

        # <<< 1copy (0areas_FilterYModifier_filter_clear,, $$)
        box_filter = self.w.box_filter
        widget_rim = SIZE_border[3]
        icons = self.icons
        icons_button = self.icons_button
        blfs = self.blfs
        blfs_info = self.blfs_info
        blfs_num = self.blfs_num
        icons.clear()
        icons_button.clear()
        blfs.clear()
        blfs_info.clear()
        blfs_num.clear()
        self.selnames.clear()
        self.box_selections.clear()
        # >>>

        R = box_filter.R - widget_rim
        scroll_width = min(SIZE_widget[2], SIZE_widget[0])
        self.box_scroll_bg.LRBT_upd(R - scroll_width, R, box_filter.B + widget_rim, box_filter.T - widget_rim)
        self.box_hover.LRBT_upd(0, 0, 0, 0)

        old_act = self.active_index
        # if blfs:
        #     e0 = blfs[self.headkey]
        #     xy = e0.x, e0.y + self.headkey * D_SIZE['widget_full_h']
        # else:
        #     xy = None
        # <<< 1copy (0area_FilterYModifier_filter_get_blfs,, $$)
        self.headkey = 0
        full_h = D_SIZE['widget_full_h']
        T = box_filter.T - widget_rim
        x = box_filter.L + widget_rim + SIZE_filter[1] + widget_rim + D_SIZE['font_main_dy']
        y = T - SIZE_filter[2] - widget_rim - D_SIZE['font_main_dT']
        range_end = min(len_match_items, ceil((T - box_filter.B - widget_rim) / full_h) + 1)
        self.endkey = range_end - 1
        get_info = self.get_info

        h = SIZE_widget[0]
        x += h
        R = x - D_SIZE['font_main_dy']
        L = R - h
        B = y - D_SIZE['font_main_dy']
        T = B + h
        L_icon_button = self.w.box_region.inner[0] + D_SIZE['font_main_dy']
        R_icon_button = L_icon_button + h
        geticon = self.get_icon
        ob = self.w.w.active_object

        geticon_button = self.r_region_icon_fn(ob)
        anim_data = ob.animation_data  if hasattr(ob, "animation_data") else None
        blfSize(FONT0, D_SIZE['font_label'])
        x_num = self.box_scroll_bg.L - round(D_SIZE['font_label_dx'] * 0.6 + blfDimen(FONT0, "000")[0])
        names = self.names

        if get_info is None:
            for r in range(range_end):
                it = match_items[r]
                e = BlfColor(it.name, x, y, COL_box_filter_fg)
                blfs[r] = e
                blfs_num[r] = Blf(str(names[it.name] + 1).rjust(3, " "), x_num, y)
                ee = geticon(it)
                ee.LRBT_upd(L, R, B, T)
                if hasattr(ee, "max_index"): e.x += ee.max_index * h
                icons[r] = ee
                ee = geticon_button(it, anim_data)
                ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                icons_button[r] = ee
                y -= full_h
                T -= full_h
                B -= full_h
        else:
            blfSize(FONT0, D_SIZE['font_main'])
            xx = x + full_h
            for r in range(range_end):
                it = match_items[r]
                e = BlfColor(it.name, x, y, COL_box_filter_fg)
                blfs[r] = e
                blfs_num[r] = Blf(str(names[it.name] + 1).rjust(3, " "), x_num, y)
                e_info = Blf(get_info(it), xx + round(blfDimen(FONT0, e.text)[0]))
                blfs_info[r] = e_info
                ee = geticon(it)
                ee.LRBT_upd(L, R, B, T)
                if hasattr(ee, "max_index"):
                    x_offset = ee.max_index * h
                    e.x += x_offset
                    e_info.x += x_offset

                icons[r] = ee
                ee = geticon_button(it, anim_data)
                ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                icons_button[r] = ee
                y -= full_h
                T -= full_h
                B -= full_h

        self.r_upd_scroll()()
        # >>>
        self.set_active_index(old_act)
        return None
        #|

    def dxy(self, dx, dy):
        # ref_FilterY_dxy
        self.box_scroll_bg.dxy_upd(dx, dy)
        self.box_scroll.dxy_upd(dx, dy)

        for e in self.icons.values(): e.dxy_upd(dx, dy)
        for e in self.icons_button.values(): e.dxy_upd(dx, dy)
        for e in self.blfs.values():
            e.x += dx
            e.y += dy
        for e in self.blfs_info.values():
            e.x += dx
        for e in self.blfs_num.values():
            e.x += dx
            e.y += dy

        self.box_active.dxy_upd(dx, dy)
        self.box_hover.dxy_upd(dx, dy)
        for e in self.box_selections.values(): e.dxy_upd(dx, dy)
        #|

    def r_region_icon_fn(self, ob): return r_geticon_Modifier_button(ob)

    def filter_text(self, s, active_index=0, callback=False):
        # ref_FilterY_filter_text
        if s:
            fx = self.filter_function
            match_items = [e for e in self.items if fx(e.name, s)]
            len_match_items = len(match_items)
        else:
            match_items = self.items
            len_match_items = len(match_items)
        self.match_items = match_items

        # print('-------------------------')
        # for e in self.match_items: print(e.name)
        # print('-------------------------')

        # /* 0areas_FilterYModifier_filter_clear
        box_filter = self.w.box_filter
        widget_rim = SIZE_border[3]
        icons = self.icons
        icons_button = self.icons_button
        blfs = self.blfs
        blfs_info = self.blfs_info
        blfs_num = self.blfs_num
        icons.clear()
        icons_button.clear()
        blfs.clear()
        blfs_info.clear()
        blfs_num.clear()
        self.selnames.clear()
        self.box_selections.clear()
        # */

        # /* 0area_FilterYModifier_filter_get_blfs
        self.headkey = 0
        full_h = D_SIZE['widget_full_h']
        T = box_filter.T - widget_rim
        x = box_filter.L + widget_rim + SIZE_filter[1] + widget_rim + D_SIZE['font_main_dy']
        y = T - SIZE_filter[2] - widget_rim - D_SIZE['font_main_dT']
        range_end = min(len_match_items, ceil((T - box_filter.B - widget_rim) / full_h) + 1)
        self.endkey = range_end - 1
        get_info = self.get_info

        h = SIZE_widget[0]
        x += h
        R = x - D_SIZE['font_main_dy']
        L = R - h
        B = y - D_SIZE['font_main_dy']
        T = B + h
        L_icon_button = self.w.box_region.inner[0] + D_SIZE['font_main_dy']
        R_icon_button = L_icon_button + h
        geticon = self.get_icon
        ob = self.w.w.active_object

        geticon_button = self.r_region_icon_fn(ob)
        anim_data = ob.animation_data  if hasattr(ob, "animation_data") else None
        blfSize(FONT0, D_SIZE['font_label'])
        x_num = self.box_scroll_bg.L - round(D_SIZE['font_label_dx'] * 0.6 + blfDimen(FONT0, "000")[0])
        names = self.names

        if get_info is None:
            for r in range(range_end):
                it = match_items[r]
                e = BlfColor(it.name, x, y, COL_box_filter_fg)
                blfs[r] = e
                blfs_num[r] = Blf(str(names[it.name] + 1).rjust(3, " "), x_num, y)
                ee = geticon(it)
                ee.LRBT_upd(L, R, B, T)
                if hasattr(ee, "max_index"): e.x += ee.max_index * h
                icons[r] = ee
                ee = geticon_button(it, anim_data)
                ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                icons_button[r] = ee
                y -= full_h
                T -= full_h
                B -= full_h
        else:
            blfSize(FONT0, D_SIZE['font_main'])
            xx = x + full_h
            for r in range(range_end):
                it = match_items[r]
                e = BlfColor(it.name, x, y, COL_box_filter_fg)
                blfs[r] = e
                blfs_num[r] = Blf(str(names[it.name] + 1).rjust(3, " "), x_num, y)
                e_info = Blf(get_info(it), xx + round(blfDimen(FONT0, e.text)[0]))
                blfs_info[r] = e_info
                ee = geticon(it)
                ee.LRBT_upd(L, R, B, T)
                if hasattr(ee, "max_index"):
                    x_offset = ee.max_index * h
                    e.x += x_offset
                    e_info.x += x_offset

                icons[r] = ee
                ee = geticon_button(it, anim_data)
                ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                icons_button[r] = ee
                y -= full_h
                T -= full_h
                B -= full_h

        self.r_upd_scroll()()
        # */
        self.set_active_index(active_index, callback)
        #|
    def redraw_from(self, headkey, blf_y, le):
        match_items = self.match_items
        if match_items:
            r = self.headkey
            h = SIZE_widget[0]
            full_h = D_SIZE['widget_full_h']
            icons = self.icons
            icons_button = self.icons_button
            blfs = self.blfs
            blfs_info = self.blfs_info
            blfs_num = self.blfs_num
            box_selections = self.box_selections
            selnames = self.selnames

            y = blf_y - headkey * full_h
            T = y + D_SIZE['font_main_dT']
            B = y - D_SIZE['font_main_dy']
            L_icon_button = self.w.box_region.inner[0] + D_SIZE['font_main_dy']
            R_icon_button = L_icon_button + h
            if hasattr(icons[r], "max_index"):
                x2 = blfs[r].x
                x = x2 - h
            else:
                x = blfs[r].x
                x2 = x + h

            L = icons[r].L
            R = icons[r].R
            geticon = self.get_icon
            ob = self.w.w.active_object

            geticon_button = self.r_region_icon_fn(ob)
            anim_data = ob.animation_data  if hasattr(ob, "animation_data") else None
            x_num = blfs_num[r].x
            names = self.names
            get_info = self.get_info
            icons.clear()
            icons_button.clear()
            blfs.clear()
            blfs_info.clear()
            blfs_num.clear()
            box_selections.clear()
            box_selections_L = self.w.scissor_filt.x
            box_selections_R = self.box_scroll_bg.L

            if get_info is None:
                for r in range(headkey, min(headkey + le, len(match_items))):
                    it = match_items[r]
                    ee = geticon(it)
                    if hasattr(ee, "max_index"):
                        e = BlfColor(it.name, x2, y, COL_box_filter_fg)
                    else:
                        e = BlfColor(it.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    blfs_num[r] = Blf(str(names[it.name] + 1).rjust(3, " "), x_num, y)
                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    ee = geticon_button(it, anim_data)
                    ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                    icons_button[r] = ee
                    if r in selnames:
                        e = GpuBox_box_filter_select_bg(box_selections_L, box_selections_R, B, T)
                        e.upd()
                        box_selections[r] = e
                    y -= full_h
                    T -= full_h
                    B -= full_h
            else:
                blfSize(FONT0, D_SIZE['font_main'])
                xx = x + full_h
                for r in range(headkey, min(headkey + le, len(match_items))):
                    it = match_items[r]
                    ee = geticon(it)
                    if hasattr(ee, "max_index"):
                        e = BlfColor(it.name, x2, y, COL_box_filter_fg)
                    else:
                        e = BlfColor(it.name, x, y, COL_box_filter_fg)
                    blfs[r] = e
                    blfs_num[r] = Blf(str(names[it.name] + 1).rjust(3, " "), x_num, y)
                    e_info = Blf(get_info(it), xx + round(blfDimen(FONT0, e.text)[0]))
                    blfs_info[r] = e_info
                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    ee = geticon_button(it, anim_data)
                    ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                    icons_button[r] = ee
                    if r in selnames:
                        e = GpuBox_box_filter_select_bg(box_selections_L, box_selections_R, B, T)
                        e.upd()
                        box_selections[r] = e
                    y -= full_h
                    T -= full_h
                    B -= full_h

            self.headkey = headkey
            self.endkey = headkey + len(blfs) - 1
            self.r_upd_scroll()()
            self.set_active_index(self.active_index, callback=False)
        #|

    def check_selnames(self):
        selnames = self.selnames
        match_items = self.match_items
        le = len(match_items)
        if self.active_index in selnames: del selnames[self.active_index]

        for r, e in selnames.copy().items():
            if r >= le: del selnames[r]
            if e != match_items[r].name: selnames[r] = match_items[r].name
        return selnames
        #|

    def to_modal_pan(self):
        # ref_FilterY_to_modal_pan

        #|
        if self.blfs: pass
        else: return

        end_trigger = r_end_trigger('pan')
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop()
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        # <<< 1copy (0defpanMdGet,, $$)
        _blfSize = blfSize
        _blfDimen = blfDimen
        _FONT0 = FONT0
        _fontsize_main = D_SIZE['font_main']
        sci = self.w.scissor_filt
        widget_rim = SIZE_border[3]
        blf_offset_x = D_SIZE['font_main_dy'] + SIZE_filter[1] + widget_rim
        sci_B = sci.y
        sci_T = sci.y + sci.h

        _r_blfs_width = self.r_blfs_width
        _blfs_width = [_r_blfs_width()]
        _full_h = D_SIZE['widget_full_h']
        _oo = self.match_items
        _li = self.blfs
        _li_info = self.blfs_info
        _max_endkey = len(_oo) - 1
        _T_add = sci_T - widget_rim - D_SIZE['font_main_dT']
        _B_add = sci_B + widget_rim + D_SIZE['font_main_dy']
        _lim_L = sci.x + blf_offset_x
        _lim_R = sci.x + sci.w - blf_offset_x
        _lim_B = sci_B + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim
        _lim_T = sci_T - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT']
        _len = len(_li)

        _h = SIZE_widget[0]
        _geticon = self.get_icon
        _li_icon = self.icons
        _icon_dB = - D_SIZE['font_main_dy']
        _icon_dT = D_SIZE['font_main_dT']
        _icon_dR = - D_SIZE['font_main_dy']
        _icon_dL = _icon_dR - _h
        _lim_L += _h
        _selection_L = sci.x
        _selection_R = self.box_scroll_bg.L

        _li_icon_button = self.icons_button
        _L_icons_button = self.w.box_region.inner[0] - _icon_dR
        _R_icons_button = _L_icons_button + _h
        _li_num = self.blfs_num
        _blfSize(_FONT0, D_SIZE['font_label'])
        _x_num = self.box_scroll_bg.L - round(D_SIZE['font_label_dx'] * 0.6 + _blfDimen(_FONT0, "000")[0])
        _li_selections = self.box_selections
        _li_selnames = self.selnames

        _getinfo = self.get_info
        _names = self.names

        ob = self.w.w.active_object

        _geticon_button = self.r_region_icon_fn(ob)
        _anim_data = ob.animation_data  if hasattr(ob, "animation_data") else None

        _upd_scroll = self.r_upd_scroll()
        _box_active_dy_upd = self.box_active.dy_upd
        _box_hover_button = self.box_hover_button

        _Blf = Blf
        _BlfColor = BlfColor
        _COL_box_filter_fg = COL_box_filter_fg
        _GpuBox_box_filter_select_bg = GpuBox_box_filter_select_bg
        # >>>

        def end_modal_pan():
            mouseloop_end()
            kill_evt_except()

        if _getinfo is None:
            def modal_pan():
                _REDRAW()
                if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                    w_head.fin()
                    return
                dx, dy = r_dxy_mouse()

                # <<< 1copy (0defpanMdModalNoInfo,, $$)
                bo0 = _li[self.headkey]
                bo0_icon = _li_icon[self.headkey]

                if dx < 0:
                    R = bo0.x + _blfs_width[0] + dx
                    if R < _lim_R:
                        dx -= R - _lim_R
                        if hasattr(bo0_icon, "max_index"):
                            L = bo0.x + dx - bo0_icon.max_index * _h
                        else:
                            L = bo0.x + dx
                        if L > _lim_L: dx -= L - _lim_L
                else:
                    if hasattr(bo0_icon, "max_index"):
                        L = bo0.x + dx - bo0_icon.max_index * _h
                    else:
                        L = bo0.x + dx
                    if L > _lim_L: dx -= L - _lim_L

                if dy < 0:
                    headkey = self.headkey
                    T = bo0.y + dy
                    if headkey == 0:
                        if T < _lim_T: dy -= T - _lim_T
                    else:
                        if T < _T_add:

                            endkey = self.endkey
                            x = bo0.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(bo0_icon, "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            while headkey != 0:
                                if T < _T_add:

                                    y = _li[headkey].y + _full_h
                                    headkey -= 1
                                    o = _oo[headkey]
                                    ee = _geticon(o)
                                    _li[headkey] = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li_num[headkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[headkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[headkey] = ee
                                    if headkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[headkey] = ee
                                    T += _full_h
                                    del _li[endkey]
                                    del _li_num[endkey]
                                    del _li_icon[endkey]
                                    del _li_icon_button[endkey]
                                    if endkey in _li_selections: del _li_selections[endkey]
                                    endkey -= 1
                                else: break

                            if headkey == 0:
                                T = _li[0].y + dy
                                if T < _lim_T: dy -= T - _lim_T

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()


                else:
                    endkey = self.endkey
                    bo1 = _li[endkey]
                    B = bo1.y + dy
                    if endkey == _max_endkey:
                        if B > _lim_B:
                            dy -= B - _lim_B
                            if self.headkey == 0:
                                TT = bo0.y + dy
                                if TT < _lim_T: dy += _lim_T - TT
                    else:
                        if B > _B_add:

                            headkey = self.headkey
                            x = bo1.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(_li_icon[endkey], "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            while endkey != _max_endkey:
                                if B > _B_add:

                                    y = _li[endkey].y - _full_h
                                    endkey += 1
                                    o = _oo[endkey]
                                    ee = _geticon(o)
                                    _li[endkey] = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li_num[endkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[endkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[endkey] = ee
                                    if endkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[endkey] = ee
                                    B -= _full_h
                                    del _li[headkey]
                                    del _li_num[headkey]
                                    del _li_icon[headkey]
                                    del _li_icon_button[headkey]
                                    if headkey in _li_selections: del _li_selections[headkey]
                                    headkey += 1
                                else: break

                            if endkey == _max_endkey:
                                B = _li[endkey].y + dy
                                if B > _lim_B: dy -= B - _lim_B

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()



                for e in _li.values():
                    e.x += dx
                    e.y += dy
                for e in _li_icon.values(): e.dxy_upd(dx, dy)
                for e in _li_icon_button.values(): e.dxy_upd(0, dy)
                for e in _li_num.values(): e.y += dy
                for e in _li_selections.values(): e.dy_upd(dy)

                _upd_scroll()
                _box_active_dy_upd(dy)
                _box_hover_button.dy_upd(dy)
                # >>>
                mouseloop()
        else:
            def modal_pan():
                _REDRAW()
                if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                    w_head.fin()
                    return
                dx, dy = r_dxy_mouse()

                # <<< 1copy (0defpanMdModal,, $$)
                bo0 = _li[self.headkey]
                bo0_icon = _li_icon[self.headkey]

                if dx < 0:
                    R = bo0.x + _blfs_width[0] + dx
                    if R < _lim_R:
                        dx -= R - _lim_R
                        if hasattr(bo0_icon, "max_index"):
                            L = bo0.x + dx - bo0_icon.max_index * _h
                        else:
                            L = bo0.x + dx
                        if L > _lim_L: dx -= L - _lim_L
                else:
                    if hasattr(bo0_icon, "max_index"):
                        L = bo0.x + dx - bo0_icon.max_index * _h
                    else:
                        L = bo0.x + dx
                    if L > _lim_L: dx -= L - _lim_L

                if dy < 0:
                    headkey = self.headkey
                    T = bo0.y + dy
                    if headkey == 0:
                        if T < _lim_T: dy -= T - _lim_T
                    else:
                        if T < _T_add:

                            endkey = self.endkey
                            x = bo0.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(bo0_icon, "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            xx = x + _full_h
                            while headkey != 0:
                                if T < _T_add:

                                    y = _li[headkey].y + _full_h
                                    headkey -= 1
                                    o = _oo[headkey]
                                    ee = _geticon(o)
                                    e = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li[headkey] = e
                                    _li_num[headkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                    _li_info[headkey] = e_info
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[headkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[headkey] = ee
                                    if headkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[headkey] = ee
                                    T += _full_h
                                    del _li[endkey]
                                    del _li_num[endkey]
                                    del _li_icon[endkey]
                                    del _li_icon_button[endkey]
                                    del _li_info[endkey]
                                    if endkey in _li_selections: del _li_selections[endkey]
                                    endkey -= 1
                                else: break

                            if headkey == 0:
                                T = _li[0].y + dy
                                if T < _lim_T: dy -= T - _lim_T

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()


                else:
                    endkey = self.endkey
                    bo1 = _li[endkey]
                    B = bo1.y + dy
                    if endkey == _max_endkey:
                        if B > _lim_B:
                            dy -= B - _lim_B
                            if self.headkey == 0:
                                TT = bo0.y + dy
                                if TT < _lim_T: dy += _lim_T - TT
                    else:
                        if B > _B_add:

                            headkey = self.headkey
                            x = bo1.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(_li_icon[endkey], "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            xx = x + _full_h
                            while endkey != _max_endkey:
                                if B > _B_add:

                                    y = _li[endkey].y - _full_h
                                    endkey += 1
                                    o = _oo[endkey]
                                    ee = _geticon(o)
                                    e = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li[endkey] = e
                                    _li_num[endkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                    _li_info[endkey] = e_info
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[endkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[endkey] = ee
                                    if endkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[endkey] = ee
                                    B -= _full_h
                                    del _li[headkey]
                                    del _li_num[headkey]
                                    del _li_icon[headkey]
                                    del _li_icon_button[headkey]
                                    del _li_info[headkey]
                                    if headkey in _li_selections: del _li_selections[headkey]
                                    headkey += 1
                                else: break

                            if endkey == _max_endkey:
                                B = _li[endkey].y + dy
                                if B > _lim_B: dy -= B - _lim_B

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()



                for e in _li.values():
                    e.x += dx
                    e.y += dy
                for e in _li_info.values():
                    e.x += dx
                for e in _li_icon.values(): e.dxy_upd(dx, dy)
                for e in _li_icon_button.values(): e.dxy_upd(0, dy)
                for e in _li_num.values(): e.y += dy
                for e in _li_selections.values(): e.dy_upd(dy)

                _upd_scroll()
                _box_active_dy_upd(dy)
                _box_hover_button.dy_upd(dy)
                # >>>
                mouseloop()

        self.box_hover.LRBT_upd(0, 0, 0, 0)
        w_head = Head(self, modal_pan, end_modal_pan)
        _REDRAW()
        #|
    def r_pan_override(self):
        # <<< 1copy (0defpanMdGet,, $$)
        _blfSize = blfSize
        _blfDimen = blfDimen
        _FONT0 = FONT0
        _fontsize_main = D_SIZE['font_main']
        sci = self.w.scissor_filt
        widget_rim = SIZE_border[3]
        blf_offset_x = D_SIZE['font_main_dy'] + SIZE_filter[1] + widget_rim
        sci_B = sci.y
        sci_T = sci.y + sci.h

        _r_blfs_width = self.r_blfs_width
        _blfs_width = [_r_blfs_width()]
        _full_h = D_SIZE['widget_full_h']
        _oo = self.match_items
        _li = self.blfs
        _li_info = self.blfs_info
        _max_endkey = len(_oo) - 1
        _T_add = sci_T - widget_rim - D_SIZE['font_main_dT']
        _B_add = sci_B + widget_rim + D_SIZE['font_main_dy']
        _lim_L = sci.x + blf_offset_x
        _lim_R = sci.x + sci.w - blf_offset_x
        _lim_B = sci_B + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim
        _lim_T = sci_T - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT']
        _len = len(_li)

        _h = SIZE_widget[0]
        _geticon = self.get_icon
        _li_icon = self.icons
        _icon_dB = - D_SIZE['font_main_dy']
        _icon_dT = D_SIZE['font_main_dT']
        _icon_dR = - D_SIZE['font_main_dy']
        _icon_dL = _icon_dR - _h
        _lim_L += _h
        _selection_L = sci.x
        _selection_R = self.box_scroll_bg.L

        _li_icon_button = self.icons_button
        _L_icons_button = self.w.box_region.inner[0] - _icon_dR
        _R_icons_button = _L_icons_button + _h
        _li_num = self.blfs_num
        _blfSize(_FONT0, D_SIZE['font_label'])
        _x_num = self.box_scroll_bg.L - round(D_SIZE['font_label_dx'] * 0.6 + _blfDimen(_FONT0, "000")[0])
        _li_selections = self.box_selections
        _li_selnames = self.selnames

        _getinfo = self.get_info
        _names = self.names

        ob = self.w.w.active_object

        _geticon_button = self.r_region_icon_fn(ob)
        _anim_data = ob.animation_data  if hasattr(ob, "animation_data") else None

        _upd_scroll = self.r_upd_scroll()
        _box_active_dy_upd = self.box_active.dy_upd
        _box_hover_button = self.box_hover_button

        _Blf = Blf
        _BlfColor = BlfColor
        _COL_box_filter_fg = COL_box_filter_fg
        _GpuBox_box_filter_select_bg = GpuBox_box_filter_select_bg
        # >>>

        if _getinfo is None:
            def pan_override(dx, dy):
                # <<< 1copy (0defpanMdModalNoInfo,, $$)
                bo0 = _li[self.headkey]
                bo0_icon = _li_icon[self.headkey]

                if dx < 0:
                    R = bo0.x + _blfs_width[0] + dx
                    if R < _lim_R:
                        dx -= R - _lim_R
                        if hasattr(bo0_icon, "max_index"):
                            L = bo0.x + dx - bo0_icon.max_index * _h
                        else:
                            L = bo0.x + dx
                        if L > _lim_L: dx -= L - _lim_L
                else:
                    if hasattr(bo0_icon, "max_index"):
                        L = bo0.x + dx - bo0_icon.max_index * _h
                    else:
                        L = bo0.x + dx
                    if L > _lim_L: dx -= L - _lim_L

                if dy < 0:
                    headkey = self.headkey
                    T = bo0.y + dy
                    if headkey == 0:
                        if T < _lim_T: dy -= T - _lim_T
                    else:
                        if T < _T_add:

                            endkey = self.endkey
                            x = bo0.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(bo0_icon, "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            while headkey != 0:
                                if T < _T_add:

                                    y = _li[headkey].y + _full_h
                                    headkey -= 1
                                    o = _oo[headkey]
                                    ee = _geticon(o)
                                    _li[headkey] = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li_num[headkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[headkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[headkey] = ee
                                    if headkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[headkey] = ee
                                    T += _full_h
                                    del _li[endkey]
                                    del _li_num[endkey]
                                    del _li_icon[endkey]
                                    del _li_icon_button[endkey]
                                    if endkey in _li_selections: del _li_selections[endkey]
                                    endkey -= 1
                                else: break

                            if headkey == 0:
                                T = _li[0].y + dy
                                if T < _lim_T: dy -= T - _lim_T

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()


                else:
                    endkey = self.endkey
                    bo1 = _li[endkey]
                    B = bo1.y + dy
                    if endkey == _max_endkey:
                        if B > _lim_B:
                            dy -= B - _lim_B
                            if self.headkey == 0:
                                TT = bo0.y + dy
                                if TT < _lim_T: dy += _lim_T - TT
                    else:
                        if B > _B_add:

                            headkey = self.headkey
                            x = bo1.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(_li_icon[endkey], "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            while endkey != _max_endkey:
                                if B > _B_add:

                                    y = _li[endkey].y - _full_h
                                    endkey += 1
                                    o = _oo[endkey]
                                    ee = _geticon(o)
                                    _li[endkey] = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li_num[endkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[endkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[endkey] = ee
                                    if endkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[endkey] = ee
                                    B -= _full_h
                                    del _li[headkey]
                                    del _li_num[headkey]
                                    del _li_icon[headkey]
                                    del _li_icon_button[headkey]
                                    if headkey in _li_selections: del _li_selections[headkey]
                                    headkey += 1
                                else: break

                            if endkey == _max_endkey:
                                B = _li[endkey].y + dy
                                if B > _lim_B: dy -= B - _lim_B

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()



                for e in _li.values():
                    e.x += dx
                    e.y += dy
                for e in _li_icon.values(): e.dxy_upd(dx, dy)
                for e in _li_icon_button.values(): e.dxy_upd(0, dy)
                for e in _li_num.values(): e.y += dy
                for e in _li_selections.values(): e.dy_upd(dy)

                _upd_scroll()
                _box_active_dy_upd(dy)
                _box_hover_button.dy_upd(dy)
                # >>>
                return dx, dy
        else:
            def pan_override(dx, dy):
                # <<< 1copy (0defpanMdModal,, $$)
                bo0 = _li[self.headkey]
                bo0_icon = _li_icon[self.headkey]

                if dx < 0:
                    R = bo0.x + _blfs_width[0] + dx
                    if R < _lim_R:
                        dx -= R - _lim_R
                        if hasattr(bo0_icon, "max_index"):
                            L = bo0.x + dx - bo0_icon.max_index * _h
                        else:
                            L = bo0.x + dx
                        if L > _lim_L: dx -= L - _lim_L
                else:
                    if hasattr(bo0_icon, "max_index"):
                        L = bo0.x + dx - bo0_icon.max_index * _h
                    else:
                        L = bo0.x + dx
                    if L > _lim_L: dx -= L - _lim_L

                if dy < 0:
                    headkey = self.headkey
                    T = bo0.y + dy
                    if headkey == 0:
                        if T < _lim_T: dy -= T - _lim_T
                    else:
                        if T < _T_add:

                            endkey = self.endkey
                            x = bo0.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(bo0_icon, "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            xx = x + _full_h
                            while headkey != 0:
                                if T < _T_add:

                                    y = _li[headkey].y + _full_h
                                    headkey -= 1
                                    o = _oo[headkey]
                                    ee = _geticon(o)
                                    e = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li[headkey] = e
                                    _li_num[headkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                    _li_info[headkey] = e_info
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[headkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[headkey] = ee
                                    if headkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[headkey] = ee
                                    T += _full_h
                                    del _li[endkey]
                                    del _li_num[endkey]
                                    del _li_icon[endkey]
                                    del _li_icon_button[endkey]
                                    del _li_info[endkey]
                                    if endkey in _li_selections: del _li_selections[endkey]
                                    endkey -= 1
                                else: break

                            if headkey == 0:
                                T = _li[0].y + dy
                                if T < _lim_T: dy -= T - _lim_T

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()


                else:
                    endkey = self.endkey
                    bo1 = _li[endkey]
                    B = bo1.y + dy
                    if endkey == _max_endkey:
                        if B > _lim_B:
                            dy -= B - _lim_B
                            if self.headkey == 0:
                                TT = bo0.y + dy
                                if TT < _lim_T: dy += _lim_T - TT
                    else:
                        if B > _B_add:

                            headkey = self.headkey
                            x = bo1.x
                            _blfSize(_FONT0, _fontsize_main)

                            if hasattr(_li_icon[endkey], "max_index"):
                                x2 = x
                                x -= _h
                            else:
                                x2 = x + _h

                            L = x + _icon_dL
                            R = x + _icon_dR

                            xx = x + _full_h
                            while endkey != _max_endkey:
                                if B > _B_add:

                                    y = _li[endkey].y - _full_h
                                    endkey += 1
                                    o = _oo[endkey]
                                    ee = _geticon(o)
                                    e = _BlfColor(o.name, (x2  if hasattr(ee, "max_index") else x), y, _COL_box_filter_fg)
                                    _li[endkey] = e
                                    _li_num[endkey] = _Blf(str(_names[o.name] + 1).rjust(3, " "), _x_num, y)
                                    e_info = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                    _li_info[endkey] = e_info
                                    B_icon = y + _icon_dB
                                    T_icon = y + _icon_dT
                                    ee.LRBT_upd(L, R, B_icon, T_icon)
                                    _li_icon[endkey] = ee
                                    ee = _geticon_button(o, _anim_data)
                                    ee.LRBT_upd(_L_icons_button, _R_icons_button, B_icon, T_icon)
                                    _li_icon_button[endkey] = ee
                                    if endkey in _li_selnames:
                                        ee = _GpuBox_box_filter_select_bg(_selection_L, _selection_R, B_icon, T_icon)
                                        ee.upd()
                                        _li_selections[endkey] = ee
                                    B -= _full_h
                                    del _li[headkey]
                                    del _li_num[headkey]
                                    del _li_icon[headkey]
                                    del _li_icon_button[headkey]
                                    del _li_info[headkey]
                                    if headkey in _li_selections: del _li_selections[headkey]
                                    headkey += 1
                                else: break

                            if endkey == _max_endkey:
                                B = _li[endkey].y + dy
                                if B > _lim_B: dy -= B - _lim_B

                            self.headkey = headkey
                            self.endkey = endkey
                            _blfs_width[0] = _r_blfs_width()



                for e in _li.values():
                    e.x += dx
                    e.y += dy
                for e in _li_info.values():
                    e.x += dx
                for e in _li_icon.values(): e.dxy_upd(dx, dy)
                for e in _li_icon_button.values(): e.dxy_upd(0, dy)
                for e in _li_num.values(): e.y += dy
                for e in _li_selections.values(): e.dy_upd(dy)

                _upd_scroll()
                _box_active_dy_upd(dy)
                _box_hover_button.dy_upd(dy)
                # >>>
                return dx, dy

        return pan_override
        #|
    #|
    #|
class AreaFilterYModifier(AreaFilterY):
    __slots__ = 'box_region'

    CLS_FILTER = FilterYModifier
    BL_ATTR = "modifiers"
    FILT_NUM_HOVER_OFFSET = 0
    USE_APPLY = True
    AREA_NAME = "area_mds"

    def init_filt_and_size(self, LL, RR, BB, TT, get_items, get_icon, get_info, input_text, filter_cls):
        self.box_region = GpuRim(COL_box_filter_region, COL_box_filter_region_rim)

        self.filt = self.CLS_FILTER(self, get_items, get_icon, get_info)

        # <<< 1copy (0area_AreaFilterYModifier_upd_size,, $$)
        # <<< 1copy (0area_AreaFilterY_upd_size,, ${'filt = self.filt':'''filt = self.filt
        # ; LL, RR, BB, TT = self.box_filter.inner
        # ; RR -= min(SIZE_widget[2], SIZE_widget[0])
        # ; LL = RR - self.calc_region_width()
        # ; self.box_region.LRBT_upd(LL, RR, BB, TT, SIZE_border[3])'''}$)
        box_area = self.box_area
        old_L = box_area.L
        old_T = box_area.T
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]
        scissor_win = self.w.scissor

        LL += d0
        RR -= d0
        TT -= d0
        BB += d0

        box_text = self.box_text
        blf_text = self.blf_text

        if self.is_flip_y:
            T = BB + D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, BB, T, widget_rim)
            T += d1
            self.box_filter.LRBT_upd(LL, RR, T, TT, widget_rim)
        else:
            B = TT - D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, B, TT, widget_rim)
            B -= d1
            self.box_filter.LRBT_upd(LL, RR, BB, B, widget_rim)

        if hasattr(self, "r_parent_scissor"):
            self.upd_scissor_filt()
        else:
            self.upd_scissor_filt(scissor_win)

        L, R, B, T = box_text.inner
        L0 = box_text.L + widget_rim * 3
        L1 = L0 + SIZE_widget[0]

        self.box_icon_search.LRBT_upd(L0, L1, B, T)
        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L1 + D_SIZE['font_main_dx']
        blf_text.y = B + D_SIZE['font_main_dy']

        filt = self.filt        ; LL, RR, BB, TT = self.box_filter.inner        ; RR -= min(SIZE_widget[2], SIZE_widget[0])        ; LL = RR - self.calc_region_width()        ; self.box_region.LRBT_upd(LL, RR, BB, TT, SIZE_border[3])
        xy = filt.upd_size()
        box_scroll_bg = filt.box_scroll_bg

        self.upd_clip_text_and_match_button(blf_text)
        self.upd_scissor_text_box(scissor_win)

        if xy != None and filt.blfs:
            e0 = filt.blfs[0]
            filt.r_pan_override()(xy[0] - old_L - e0.x + box_area.L, xy[1] - old_T - e0.y + box_area.T)

        # >>>
        # >>>
        self.filt.filter_text(input_text)
        self.init_callback()
        #|
    def init_callback(self):
        self.filt.set_active_index_callback = self.w.set_active_modifier
        #|
    def calc_region_width(self):
        return 5 * (SIZE_widget[0] + SIZE_border[3]) + D_SIZE['font_main_dy']
        #|

    def upd_size(self, LL, RR, BB, TT):
        # /* 0area_AreaFilterYModifier_upd_size
        # <<< 1copy (0area_AreaFilterY_upd_size,, ${'filt = self.filt':'''filt = self.filt
        # ; LL, RR, BB, TT = self.box_filter.inner
        # ; RR -= min(SIZE_widget[2], SIZE_widget[0])
        # ; LL = RR - self.calc_region_width()
        # ; self.box_region.LRBT_upd(LL, RR, BB, TT, SIZE_border[3])'''}$)
        box_area = self.box_area
        old_L = box_area.L
        old_T = box_area.T
        box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]
        scissor_win = self.w.scissor

        LL += d0
        RR -= d0
        TT -= d0
        BB += d0

        box_text = self.box_text
        blf_text = self.blf_text

        if self.is_flip_y:
            T = BB + D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, BB, T, widget_rim)
            T += d1
            self.box_filter.LRBT_upd(LL, RR, T, TT, widget_rim)
        else:
            B = TT - D_SIZE['widget_full_h']
            box_text.LRBT_upd(LL, RR, B, TT, widget_rim)
            B -= d1
            self.box_filter.LRBT_upd(LL, RR, BB, B, widget_rim)

        if hasattr(self, "r_parent_scissor"):
            self.upd_scissor_filt()
        else:
            self.upd_scissor_filt(scissor_win)

        L, R, B, T = box_text.inner
        L0 = box_text.L + widget_rim * 3
        L1 = L0 + SIZE_widget[0]

        self.box_icon_search.LRBT_upd(L0, L1, B, T)
        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L1 + D_SIZE['font_main_dx']
        blf_text.y = B + D_SIZE['font_main_dy']

        filt = self.filt        ; LL, RR, BB, TT = self.box_filter.inner        ; RR -= min(SIZE_widget[2], SIZE_widget[0])        ; LL = RR - self.calc_region_width()        ; self.box_region.LRBT_upd(LL, RR, BB, TT, SIZE_border[3])
        xy = filt.upd_size()
        box_scroll_bg = filt.box_scroll_bg

        self.upd_clip_text_and_match_button(blf_text)
        self.upd_scissor_text_box(scissor_win)

        if xy != None and filt.blfs:
            e0 = filt.blfs[0]
            filt.r_pan_override()(xy[0] - old_L - e0.x + box_area.L, xy[1] - old_T - e0.y + box_area.T)

        # >>>
        # */
    def upd_scissor_filt(self, scissor_win):
        e = self.box_filter.inner
        self.scissor_filt.intersect_with(scissor_win,
            e[0], e[1] - min(SIZE_widget[2], SIZE_widget[0]) - self.calc_region_width(),
            e[2], e[3])
        #|

    def outside_evt_filt(self):
        super().outside_evt_filt()
        self.filt.box_hover_button.set_draw_state(False)
        #|
    def inside_evt_filt(self):
        self.filt.box_hover_button.set_draw_state(True)
        self.filt.box_hover_button.LRBT_upd(0, 0, 0, 0)
        #|
    def r_region_index(self, x, i):
        if x >= self.box_region.L:
            buts = self.filt.icons_button[i]
            if x >= buts.slot7.L:
                if x >= buts.slot7.R: return "num"
                else:
                    if isinstance(buts.slot7, GpuImg_SHOW_RENDER_DISABLE): return "null"
                    else: return "show_render"
            elif x >= buts.slot3.L:
                if x >= buts.slot5.L:
                    if isinstance(buts.slot5, GpuImg_SHOW_VIEWPORT_DISABLE): return "null"
                    else: return "show_viewport"
                else:
                    if isinstance(buts.slot3, GpuImg_SHOW_IN_EDITMODE_DISABLE): return "null"
                    else: return "show_in_editmode"
            else:
                if x >= buts.slot1.L:
                    if isinstance(buts.slot1, GpuImg_SHOW_ON_CAGE_DISABLE): return "null"
                    else: return "show_on_cage"
        return "null"
        #|
    def filt_region_event(self, B, T, i, filt):
        if i is None:
            hover = filt.box_hover_button
            if hover.L == 0 and hover.R == 0: pass
            else:
                hover.LRBT_upd(0, 0, 0, 0)
                Admin.REDRAW()
            return False

        x = MOUSE[0]
        if x >= self.box_region.L:
            buts = filt.icons_button[i]
            if x >= buts.slot7.L:
                if x >= buts.slot7.R:
                    region_ind = "num"
                    R = self.box_region.inner[1]
                    L = R - D_SIZE['widget_full_h']
                else:
                    if isinstance(buts.slot7, GpuImg_SHOW_RENDER_DISABLE):
                        region_ind = "null"
                        L = 0
                        R = 0
                    else:
                        region_ind = "show_render"
                        L = buts.slot7.L - SIZE_border[3]
                        R = buts.slot7.R + SIZE_border[3]
            elif x >= buts.slot3.L:
                if x >= buts.slot5.L:
                    if isinstance(buts.slot5, GpuImg_SHOW_VIEWPORT_DISABLE):
                        region_ind = "null"
                        L = 0
                        R = 0
                    else:
                        region_ind = "show_viewport"
                        L = buts.slot5.L - SIZE_border[3]
                        R = buts.slot5.R + SIZE_border[3]
                else:
                    if isinstance(buts.slot3, GpuImg_SHOW_IN_EDITMODE_DISABLE):
                        region_ind = "null"
                        L = 0
                        R = 0
                    else:
                        region_ind = "show_in_editmode"
                        L = buts.slot3.L - SIZE_border[3]
                        R = buts.slot3.R + SIZE_border[3]
            else:
                if x >= buts.slot1.L:
                    if isinstance(buts.slot1, GpuImg_SHOW_ON_CAGE_DISABLE) or isinstance(buts.slot1, GpuImgNull):
                        region_ind = "null"
                        L = 0
                        R = 0
                    else:
                        region_ind = "show_on_cage"
                        L = buts.slot1.L - SIZE_border[3]
                        R = buts.slot1.R + SIZE_border[3]
                else:
                    region_ind = "null"
                    hover = filt.box_hover_button
                    L = 0
                    R = 0

            hover = filt.box_hover_button
            if hover.L == L and hover.R == R and hover.B == B and hover.T == T: pass
            else:
                hover.LRBT_upd(L, R, B, T)
                Admin.REDRAW()

            if region_ind == "num":
                if TRIGGER['area_sort']():
                    self.to_modal_filt_num(i)
                    return True
            elif region_ind != "null":
                if TRIGGER['ui_batch']():
                    self.evt_batch(i, region_ind)
                    return True
                if TRIGGER['click']():
                    self.to_modal_filt_button(i, region_ind)
                    return True
        else:
            hover = filt.box_hover_button
            if hover.L == 0 and hover.R == 0: pass
            else:
                hover.LRBT_upd(0, 0, 0, 0)
                Admin.REDRAW()
        return False
        #|

    def localmodal_filt_submodal(self):
        if TRIGGER['rm']():
            self.to_modal_filt_rm()
            return True
        if TRIGGER['rename']():
            self.evt_area_rename()
            return True
        if TRIGGER['ui_remove_from_keying_set']():
            self.evt_remove_from_keying_set()
            return True
        if TRIGGER['ui_add_to_keying_set']():
            self.evt_add_to_keying_set()
            return True
        if TRIGGER['ui_copy_full_data_path']():
            self.evt_copy_full_data_path()
            return True
        if TRIGGER['ui_copy_data_path']():
            self.evt_copy_data_path()
            return True
        if TRIGGER['ui_paste_full_data_path_as_driver']():
            self.evt_paste_full_data_path_as_driver()
            return True
        if TRIGGER['ui_delete_driver']():
            self.evt_delete_driver()
            return True
        if TRIGGER['ui_add_driver']():
            self.evt_add_driver(use_editor=True)
            return True
        if TRIGGER['ui_clear_keyframe']():
            self.evt_clear_keyframe()
            return True
        if TRIGGER['ui_delete_keyframe']():
            self.evt_delete_keyframe()
            return True
        if TRIGGER['ui_insert_keyframe']():
            self.evt_insert_keyframe()
            return True
        if TRIGGER['area_copy_to_selected']():
            self.evt_area_copy_to_selected()
            return True
        if TRIGGER['area_unpin_to_last_selected']():
            self.evt_unpin_to_last_selected()
            return True
        if TRIGGER['area_pin_to_last_selected']():
            self.evt_pin_to_last_selected()
            return True
        if TRIGGER['area_pin_to_last_toggle']():
            self.evt_use_pin_to_last()
            return True
        if TRIGGER['area_select_all_toggle']():
            self.evt_select_all_toggle()
            return True
        return False
        #|

    def to_modal_filt_rm(self):

        # /* 0AreaFilterYModifier_if_ind_safe
        filt = self.filt
        blfs = filt.blfs
        if not blfs: return

        T = blfs[filt.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
        i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + filt.headkey

        if 0 <= i < len(filt.match_items):
        # */
            region_index = self.r_region_index(MOUSE[0], i)
            items = [
                ("rename", lambda: self.evt_area_rename((i, T))),
                ("ui_remove_from_keying_set", lambda: self.evt_remove_from_keying_set((i, region_index))),
                ("ui_add_to_keying_set", lambda: self.evt_add_to_keying_set((i, region_index))),
                ("ui_copy_full_data_path", lambda: self.evt_copy_full_data_path((i, region_index))),
                ("ui_copy_data_path", lambda: self.evt_copy_data_path((i, region_index))),
                ("ui_paste_full_data_path_as_driver", lambda: self.evt_paste_full_data_path_as_driver((i, region_index))),
                ("ui_delete_driver", lambda: self.evt_delete_driver((i, region_index))),
                ("ui_add_driver", lambda: self.evt_add_driver((i, region_index), use_editor=True)),
                ("ui_clear_keyframe", lambda: self.evt_clear_keyframe((i, region_index))),
                ("ui_delete_keyframe", lambda: self.evt_delete_keyframe((i, region_index))),
                ("ui_insert_keyframe", lambda: self.evt_insert_keyframe((i, region_index))),
                ("area_copy_to_selected", lambda: self.evt_area_copy_to_selected((i, T))),
                ("dd_scroll_left_most", lambda: self.filt.evt_scrollX(self.filt.r_blfs_width())),
                ("dd_scroll_right_most", lambda: self.filt.evt_scrollX(-self.filt.r_blfs_width())),
                ("dd_scroll_down_most", lambda: self.filt.evt_scrollY(len(self.filt.items) * D_SIZE['widget_full_h'])),
                ("dd_scroll_up_most", lambda: self.filt.evt_scrollY(-len(self.filt.items) * D_SIZE['widget_full_h'])),
                ("dd_scroll_left", lambda: self.filt.evt_scrollX(P.scroll_distance)),
                ("dd_scroll_right", lambda: self.filt.evt_scrollX(-P.scroll_distance)),
                ("dd_scroll_down", lambda: self.filt.evt_scrollY(P.scroll_distance)),
                ("dd_scroll_up", lambda: self.filt.evt_scrollY(-P.scroll_distance)),
                ("dd_beam_down", self.evt_beam_down),
                ("dd_beam_up", self.evt_beam_up),
                ("area_apply_as_shapekey", self.evt_apply_as_shapekey),
                ("area_save_as_shapekey", self.evt_save_as_shapekey),
                ("area_apply", self.evt_apply),
                ("area_del", self.evt_del),
                ("area_add", self.evt_add),
                ("area_active_down_most_shift", self.evt_active_down_most_shift),
                ("area_active_up_most_shift", self.evt_active_up_most_shift),
                ("area_active_down_shift", self.evt_active_down_shift),
                ("area_active_up_shift", self.evt_active_up_shift),
                ("area_active_down_most", self.evt_active_down_most),
                ("area_active_up_most", self.evt_active_up_most),
                ("area_active_down", self.evt_active_down),
                ("area_active_up", self.evt_active_up),
                ("area_select_all_toggle", self.evt_select_all_toggle),
                ("pan", self.filt.to_modal_pan),
                ("area_select_extend", lambda: self.evt_area_select(i, extend=True)),
                ("area_select", lambda: self.evt_area_select(i, extend=False)),
            ]
            if HAS_MD_PIN_TO_LAST is True:
                items += [
                    ("area_unpin_to_last_selected", self.evt_unpin_to_last_selected),
                    ("area_pin_to_last_selected", self.evt_pin_to_last_selected),
                    ("area_pin_to_last_toggle", lambda: self.evt_use_pin_to_last((i, region_index))),
                ]

            override_name = {"area_copy_to_selected":"Copy to Selected"}
            DropDownRMKeymap(self, MOUSE, items,
                title = "Name"  if region_index in {"null", "num"} else region_index.replace("_", " ").title(),
                override_name = override_name)
        #|
    def to_modal_filt_button(self, filt_ind, region_ind):

        ob = self.w.active_object
        if ob == None: return
        if not hasattr(ob, "modifiers"): return
        if not hasattr(ob, "animation_data"): return
        is_spline = ob.type in S_spline_modifier_types
        filt = self.filt
        blfs = filt.blfs
        if not blfs: return
        match_items = filt.match_items
        if not match_items: return
        end_trigger = r_end_trigger('click')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        if is_spline and region_ind == "show_on_cage":
            boo = False  if match_items[filt_ind].use_apply_on_spline else True
        else:
            boo = False  if getattr(match_items[filt_ind], region_ind) else True

        is_override_library = True  if hasattr(ob, 'override_library') and ob.override_library else False
        is_only_viewport = ob.is_editable == False or (is_override_library and ob.override_library.is_system_override)
        isnot_library = not is_only_viewport

        mou = MOUSE
        pan_override = filt.r_pan_override()
        sci_win = self.w.scissor
        sci_filt = self.scissor_filt
        LL = sci_win.x
        RR = LL + sci_win.w
        BB = sci_filt.y
        TT = BB + sci_filt.h

        widget_rim = SIZE_border[3]
        font_main_dT_rim = D_SIZE['font_main_dT'] + widget_rim
        full_h = D_SIZE['widget_full_h']
        h = SIZE_widget[0]
        icons_button = filt.icons_button
        e = icons_button[filt.headkey]

        L0 = e.slot1.L
        L1 = e.slot3.L
        L2 = e.slot5.L
        L3 = e.slot7.L
        LL = max(LL, L0)
        RR = min(RR, e.slot7.R)
        le = len(match_items)
        anim_data = ob.animation_data
        push_modal = m.ADMIN.push_modal

        def localmodal():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            x, y = mou
            T = blfs[filt.headkey].y + font_main_dT_rim
            i = (T - y) // full_h + filt.headkey

            if LL <= x < RR and i in icons_button:
                if x >= L2:
                    if x >= L3:
                        if 0 <= i < le:
                            e = match_items[i]
                            if e.type in S_MD_USE_RENDER and e.show_render != boo and isnot_library:
                                _REDRAW()
                                e.show_render = boo
                                icons_button[i].update_slot(anim_data, e)
                    else:
                        if 0 <= i < le:
                            e = match_items[i]
                            if e.type in S_MD_USE_RENDER and e.show_viewport != boo:
                                _REDRAW()
                                e.show_viewport = boo
                                icons_button[i].update_slot(anim_data, e)
                else:
                    if x >= L1:
                        if 0 <= i < le:
                            e = match_items[i]
                            if is_override_library and hasattr(e, "is_override_data") and e.is_override_data: pass
                            elif e.type in S_MD_USE_EDITMODE and e.show_in_editmode != boo and isnot_library:
                                _REDRAW()
                                e.show_in_editmode = boo
                                icons_button[i].update_slot(anim_data, e)
                    else:
                        if 0 <= i < le:
                            e = match_items[i]
                            if is_override_library and hasattr(e, "is_override_data") and e.is_override_data: pass
                            else:
                                if is_spline:
                                    if e.type in S_md_apply_on_spline and e.use_apply_on_spline != boo and isnot_library:
                                        _REDRAW()
                                        e.use_apply_on_spline = boo
                                        icons_button[i].update_slot(anim_data, e)
                                else:
                                    if e.type in S_MD_BUTTON4 and e.show_on_cage != boo and isnot_library:
                                        _REDRAW()
                                        e.show_on_cage = boo
                                        icons_button[i].update_slot(anim_data, e)

            if y < BB:
                pan_override(0, ceil((BB - y) / full_h))
                _REDRAW()
                push_modal()
            elif y >= TT:
                pan_override(0, - ceil((y - TT) / full_h))
                _REDRAW()
                push_modal()
            #|

        def localmodalend():
            kill_evt_except()
            _REDRAW()
            update_data()
            ed_undo_push(message="MD Visibility")
            #|

        filt.box_hover_button.LRBT_upd(0, 0, 0, 0)
        filt.box_hover.LRBT_upd(0, 0, 0, 0)
        _REDRAW()
        w_head = Head(self, localmodal, localmodalend)
        localmodal()
        #|
    def to_modal_filt_selectbox(self, select_operation="extend"):

        ob = self.w.active_object
        if ob == None: return
        if not hasattr(ob, self.BL_ATTR): return
        filt = self.filt
        blfs = filt.blfs
        if not blfs: return
        match_items = filt.match_items
        if not match_items: return
        if select_operation == "extend":
            endtrigger = r_end_trigger('area_selectbox_extend')
        elif select_operation == "subtract":
            endtrigger = r_end_trigger('area_selectbox_subtract')
        else:
            endtrigger = r_end_trigger('area_selectbox_new')

        mou = MOUSE
        x_org, y_org = MOUSE_OVERRIDE
        widget_rim = SIZE_border[3]
        font_main_dT_rim = D_SIZE['font_main_dT'] + widget_rim
        full_h = D_SIZE['widget_full_h']
        filt_ind = (blfs[filt.headkey].y + font_main_dT_rim - y_org) // full_h + filt.headkey
        le = len(match_items)
        if not 0 <= filt_ind < le: return

        mou_old = [x_org, y_org]
        pan_override = filt.r_pan_override()
        sci_filt = self.scissor_filt
        BB = sci_filt.y
        TT = BB + sci_filt.h

        _push_modal = m.ADMIN.push_modal
        _REDRAW = Admin.REDRAW
        _TRIGGER_esc = TRIGGER['esc']
        _EVT_TYPE = EVT_TYPE
        _box_selectbox = GpuSelection(x_org, x_org, y_org, y_org, widget_rim)
        _box_selectbox_upd = _box_selectbox.upd
        _box_selectbox_upd()
        _box_selectbox_bind_draw = _box_selectbox.bind_draw

        def localdraw():
            blend_set('ALPHA')
            _box_selectbox_bind_draw()

        def localmodalend():
            kill_evt_except()
            _REDRAW()
            W_DRAW.remove(_draw_)

            headkey = filt.headkey
            endkey = filt.endkey
            i = min(max(0, (blfs[headkey].y + font_main_dT_rim - mou[1]) // full_h + headkey), le - 1)
            selnames = filt.selnames
            box_selections = filt.box_selections

            if _box_selectbox.state == 0:
                if select_operation == "extend":
                    old_act = filt.active_index
                else:
                    selnames.clear()
                    box_selections.clear()
                    selnames.clear()
                    box_selections.clear()

                if i < filt_ind:
                    for r in range(i, filt_ind + 1): selnames[r] = match_items[r].name
                else:
                    for r in range(filt_ind, i + 1): selnames[r] = match_items[r].name

                filt.set_active_index(i, callback=True)
                if select_operation == "extend" and i != old_act:
                    if old_act != None and 0 <= old_act < le:
                        selnames[old_act] = match_items[old_act].name
            else:
                if i < filt_ind:
                    for r in range(i, filt_ind + 1):
                        if r in selnames: del selnames[r]
                else:
                    for r in range(filt_ind, i + 1):
                        if r in selnames: del selnames[r]

            update_data()
            #|

        use_adaptive_selection = P.filter_adaptive_selection and select_operation == ""

        def localmodal():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc():
                _w_.fin()
                return
            if endtrigger():
                _w_.fin()
                return

            _REDRAW()
            x, y = mou

            if y < BB:
                _box_selectbox.T += pan_override(0, ceil((BB - y) / full_h))[1]
                _push_modal()
            elif y >= TT:
                _box_selectbox.T += pan_override(0, - ceil((y - TT) / full_h))[1]
                _push_modal()

            _box_selectbox.R += x - mou_old[0]
            _box_selectbox.B += y - mou_old[1]
            _box_selectbox_upd()

            mou_old[0] = x
            mou_old[1] = y

            if use_adaptive_selection is False: return
            if x < x_org:
                if _box_selectbox.state != 1: _box_selectbox.set_state(1)
            else:
                if _box_selectbox.state != 0: _box_selectbox.set_state(0)

        if select_operation == "subtract":
            _box_selectbox.set_state(1)

        _REDRAW()
        filt.box_hover_button.LRBT_upd(0, 0, 0, 0)
        filt.box_hover.LRBT_upd(0, 0, 0, 0)
        _draw_ = Udraw(localdraw)
        W_DRAW.append(_draw_)
        _w_ = Head(self, localmodal, localmodalend)
        localmodal()
        #|
    def to_modal_filt_num(self, filt_ind, override=None):

        ob = self.w.active_object
        if ob == None: return
        cls = self.__class__
        if not hasattr(ob, cls.BL_ATTR): return
        filt = self.filt
        blfs = filt.blfs
        if not blfs: return
        match_items = filt.match_items
        if not match_items: return
        if filt_ind < 0 or filt_ind > filt.endkey: return
        endtrigger = r_end_trigger('area_sort')
        AREA_NAME = cls.AREA_NAME

        mou = MOUSE
        mou_old = mou[:]
        le = len(match_items)
        imax = le - 1
        widget_rim = SIZE_border[3]
        _h = SIZE_widget[0]
        full_h = D_SIZE['widget_full_h']
        full_h2 = full_h // 2
        sci_filt = self.scissor_filt
        BB = sci_filt.y
        TT = BB + sci_filt.h
        T_add = TT - widget_rim - D_SIZE['font_main_dT'] + full_h
        B_add = BB + widget_rim + D_SIZE['font_main_dy'] - full_h - full_h2
        lim_B = BB + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim + imax * full_h
        lim_T = TT - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT']
        if lim_B < lim_T: lim_B = lim_T

        filt.icons_button.clear()
        icons = filt.icons
        blfs_num = filt.blfs_num
        geticon = filt.get_icon
        filt_headkey = filt.headkey
        if hasattr(icons[filt_headkey], "max_index"):
            blf_x2 = blfs[filt_headkey].x
            blf_x = blf_x2 - _h
        else:
            blf_x = blfs[filt_headkey].x
            blf_x2 = blf_x + _h
        num_x = blfs_num[filt_headkey].x
        blf_y = blfs[filt_headkey].y + full_h * filt_headkey
        icon_active = icons.pop(filt_ind)
        if hasattr(icon_active, "max_index"):
            icon_active_class = icon_active.slot0.__class__
        else:
            icon_active_class = icon_active.__class__
        iconL = icon_active.L
        iconR = icon_active.R
        icon_dB = - D_SIZE['font_main_dy']
        icon_dT = D_SIZE['font_main_dT']
        blf_active = blfs.pop(filt_ind)
        blf_active_color = blf_active.color
        blf_num_active = blfs_num.pop(filt_ind)
        names = filt.names
        active_index = filt.active_index
        animtime = P.animtime_filter
        _speed = full_h / animtime

        if override == None:
            selitems = filt.check_selnames().copy()
            if active_index != None and 0 <= active_index < le:
                selitems[active_index] = match_items[active_index].name
        else:
            selitems = override["selitems"]
        le_selitems = len(selitems)

        if le == 1:
            def localmodal():
                # <<< 1copy (_md_num_modal_head,, $$)
                if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']() or TRIGGER['area_sort_modal_cancel']():
                    nonlocal operation
                    operation = "Cancel"
                    _w_.fin()
                    return
                if endtrigger():
                    _w_.fin()
                    return

                Admin.REDRAW()
                mou_x, mou_y = mou
                # >>>
                upd_active_region()
                # <<< 1copy (_md_num_modal_tail,, $$)
                dx = mou_x - mou_old[0]
                dy = mou_y - mou_old[1]
                icon_active.dxy_upd(dx, dy)
                box_active.dxy_upd(dx, dy)
                blf_active.x += dx
                blf_active.y += dy
                blf_num_active.x += dx
                blf_active_region.x += dx

                mou_old[0] = mou_x
                mou_old[1] = mou_y
                # >>>

            if P.anim_filter:
                # <<< 1copy (_md_num_def_localmodal_mt_anim,, $$)
                def localmodal_mt(w):
                    _ = mtdata
                    if _["is_empty"] == True: return
                    nonlocal _t

                    mt_blfs = _["blfs"]
                    mt_blfs_num = _["blfs_num"]
                    mt_icons = _["icons"]

                    mou_y = mou[1]
                    if mou_y < _["autopan_B"]:
                        dy = ceil((_["autopan_B"] - mou_y) / full_h)
                        if _["blf_y"] + dy > _["lim_B"]: dy = _["lim_B"] - _["blf_y"]

                        # <<< 1copy (_md_num_modal_add_del_mt_anim,, $$)
                        if dy > 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (endkey + 1) * full_h
                            y_end = y + dy
                            while endkey != _["imax"]:
                                if y_end > _["B_add"]:
                                    endkey += 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'endkey', 'y_anim':'y'}$)
                                    o = _["match_items"][endkey]
                                    ee = geticon(o)
                                    mt_blfs[endkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                    mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[endkey] = ee
                                    # >>>
                                    y -= full_h
                                    y_end -= full_h
                                    del mt_blfs[headkey]
                                    del mt_blfs_num[headkey]
                                    del mt_icons[headkey]
                                    headkey += 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values():
                                e.y += dy
                                e.y_anim += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        elif dy < 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (headkey - 1) * full_h
                            y_end = y + dy
                            while headkey != 0:
                                if y_end < _["T_add"]:
                                    headkey -= 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'headkey', 'y_anim':'y'}$)
                                    o = _["match_items"][headkey]
                                    ee = geticon(o)
                                    mt_blfs[headkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                    mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[headkey] = ee
                                    # >>>
                                    y += full_h
                                    y_end += full_h
                                    del mt_blfs[endkey]
                                    del mt_blfs_num[endkey]
                                    del mt_icons[endkey]
                                    endkey -= 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values():
                                e.y += dy
                                e.y_anim += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        # >>>
                    elif mou_y > _["autopan_T"]:
                        dy = - ceil((mou_y - _["autopan_T"]) / full_h)
                        if _["blf_y"] + dy < _["lim_T"]: dy = _["lim_T"] - _["blf_y"]

                        # <<< 1copy (_md_num_modal_add_del_mt_anim,, $$)
                        if dy > 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (endkey + 1) * full_h
                            y_end = y + dy
                            while endkey != _["imax"]:
                                if y_end > _["B_add"]:
                                    endkey += 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'endkey', 'y_anim':'y'}$)
                                    o = _["match_items"][endkey]
                                    ee = geticon(o)
                                    mt_blfs[endkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                    mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[endkey] = ee
                                    # >>>
                                    y -= full_h
                                    y_end -= full_h
                                    del mt_blfs[headkey]
                                    del mt_blfs_num[headkey]
                                    del mt_icons[headkey]
                                    headkey += 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values():
                                e.y += dy
                                e.y_anim += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        elif dy < 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (headkey - 1) * full_h
                            y_end = y + dy
                            while headkey != 0:
                                if y_end < _["T_add"]:
                                    headkey -= 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'headkey', 'y_anim':'y'}$)
                                    o = _["match_items"][headkey]
                                    ee = geticon(o)
                                    mt_blfs[headkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                    mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[headkey] = ee
                                    # >>>
                                    y += full_h
                                    y_end += full_h
                                    del mt_blfs[endkey]
                                    del mt_blfs_num[endkey]
                                    del mt_icons[endkey]
                                    endkey -= 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values():
                                e.y += dy
                                e.y_anim += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        # >>>

                    endkey = _["filt"].endkey
                    headkey = _["filt"].headkey
                    i = min(max(headkey, (_["cvT"] - mou_y) // full_h), endkey + 1)
                    _["mt_ind"] = i
                    y = _["blf_y"] - headkey * full_h

                    for r in range(headkey, i):
                        # <<< 1copy (_md_num_modal_set_ind_mt_anim,, ${'_ind_':'r', '_y_':'y'}$)
                        if mt_blfs[r].y != y:
                            mt_blfs[r].y = y
                        # >>>
                        y -= full_h
                    y -= full_h
                    for r in range(i, endkey + 1):
                        # <<< 1copy (_md_num_modal_set_ind_mt_anim,, ${'_ind_':'r', '_y_':'y'}$)
                        if mt_blfs[r].y != y:
                            mt_blfs[r].y = y
                        # >>>
                        y -= full_h

                    new_t = _time()
                    dt = new_t - _t
                    _t = new_t
                    for r, e in mt_blfs.items():
                        dis = e.y - e.y_anim
                        if dis == 0.0: continue
                        elif dis < 0:
                            y = max(e.y, e.y_anim - dt * e.speed)
                            e.y_anim = y
                            mt_blfs_num[r].y = y
                            ee = mt_icons[r]
                            ee.B = y + icon_dB
                            ee.T = y + icon_dT
                            ee.upd()
                        else:
                            y = min(e.y, e.y_anim + dt * e.speed)
                            e.y_anim = y
                            mt_blfs_num[r].y = y
                            ee = mt_icons[r]
                            ee.B = y + icon_dB
                            ee.T = y + icon_dT
                            ee.upd()
                    #|
                # >>>
            else:
                # <<< 1copy (_md_num_def_localmodal_mt,, $$)
                def localmodal_mt(w):
                    _ = mtdata
                    if _["is_empty"] == True: return

                    mt_blfs = _["blfs"]
                    mt_blfs_num = _["blfs_num"]
                    mt_icons = _["icons"]

                    mou_y = mou[1]
                    if mou_y < _["autopan_B"]:
                        dy = ceil((_["autopan_B"] - mou_y) / full_h)
                        if _["blf_y"] + dy > _["lim_B"]: dy = _["lim_B"] - _["blf_y"]

                        # <<< 1copy (_md_num_modal_add_del_mt,, $$)
                        if dy > 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (endkey + 1) * full_h
                            y_end = y + dy
                            while endkey != _["imax"]:
                                if y_end > _["B_add"]:
                                    endkey += 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'endkey'}$)
                                    o = _["match_items"][endkey]
                                    ee = geticon(o)
                                    mt_blfs[endkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                    mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[endkey] = ee
                                    # >>>
                                    y -= full_h
                                    y_end -= full_h
                                    del mt_blfs[headkey]
                                    del mt_blfs_num[headkey]
                                    del mt_icons[headkey]
                                    headkey += 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values(): e.y += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        elif dy < 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (headkey - 1) * full_h
                            y_end = y + dy
                            while headkey != 0:
                                if y_end < _["T_add"]:
                                    headkey -= 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'headkey'}$)
                                    o = _["match_items"][headkey]
                                    ee = geticon(o)
                                    mt_blfs[headkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                    mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[headkey] = ee
                                    # >>>
                                    y += full_h
                                    y_end += full_h
                                    del mt_blfs[endkey]
                                    del mt_blfs_num[endkey]
                                    del mt_icons[endkey]
                                    endkey -= 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values(): e.y += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        # >>>
                    elif mou_y > _["autopan_T"]:
                        dy = - ceil((mou_y - _["autopan_T"]) / full_h)
                        if _["blf_y"] + dy < _["lim_T"]: dy = _["lim_T"] - _["blf_y"]

                        # <<< 1copy (_md_num_modal_add_del_mt,, $$)
                        if dy > 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (endkey + 1) * full_h
                            y_end = y + dy
                            while endkey != _["imax"]:
                                if y_end > _["B_add"]:
                                    endkey += 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'endkey'}$)
                                    o = _["match_items"][endkey]
                                    ee = geticon(o)
                                    mt_blfs[endkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                    mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[endkey] = ee
                                    # >>>
                                    y -= full_h
                                    y_end -= full_h
                                    del mt_blfs[headkey]
                                    del mt_blfs_num[headkey]
                                    del mt_icons[headkey]
                                    headkey += 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values(): e.y += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        elif dy < 0:
                            endkey = _["filt"].endkey
                            headkey = _["filt"].headkey
                            y = _["blf_y"] - (headkey - 1) * full_h
                            y_end = y + dy
                            while headkey != 0:
                                if y_end < _["T_add"]:
                                    headkey -= 1
                                    # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'headkey'}$)
                                    o = _["match_items"][headkey]
                                    ee = geticon(o)
                                    mt_blfs[headkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                    mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                    ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                    mt_icons[headkey] = ee
                                    # >>>
                                    y += full_h
                                    y_end += full_h
                                    del mt_blfs[endkey]
                                    del mt_blfs_num[endkey]
                                    del mt_icons[endkey]
                                    endkey -= 1
                                else: break

                            _["filt"].headkey = headkey
                            _["filt"].endkey = endkey

                            for e in mt_icons.values(): e.dy_upd(dy)
                            for e in mt_blfs.values(): e.y += dy
                            for e in mt_blfs_num.values(): e.y += dy
                            _["blf_y"] += dy
                            _["cvT"] += dy
                        # >>>

                    endkey = _["filt"].endkey
                    headkey = _["filt"].headkey
                    i = min(max(headkey, (_["cvT"] - mou_y) // full_h), endkey + 1)
                    _["mt_ind"] = i
                    y = _["blf_y"] - headkey * full_h

                    for r in range(headkey, i):
                        # <<< 1copy (_md_num_modal_set_ind_mt,, ${'_ind_':'r', '_y_':'y'}$)
                        if mt_blfs[r].y != y:
                            mt_blfs[r].y = y
                            mt_blfs_num[r].y = y
                            mt_icons[r].LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                        # >>>
                        y -= full_h
                    y -= full_h
                    for r in range(i, endkey + 1):
                        # <<< 1copy (_md_num_modal_set_ind_mt,, ${'_ind_':'r', '_y_':'y'}$)
                        if mt_blfs[r].y != y:
                            mt_blfs[r].y = y
                            mt_blfs_num[r].y = y
                            mt_icons[r].LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                        # >>>
                        y -= full_h
                    #|
                # >>>
        else:
            if override != None or filt_ind not in selitems or le_selitems == 1:
                if P.anim_filter:
                    # <<< 1copy (_md_num_modal_anim,, $$)
                    def localmodal():
                        # <<< 1copy (_md_num_modal_head,, $$)
                        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']() or TRIGGER['area_sort_modal_cancel']():
                            nonlocal operation
                            operation = "Cancel"
                            _w_.fin()
                            return
                        if endtrigger():
                            _w_.fin()
                            return

                        Admin.REDRAW()
                        mou_x, mou_y = mou
                        # >>>
                        nonlocal blf_y, cvT, _t

                        push_modal()

                        if upd_active_region() is True:
                            # <<< 1copy (_md_num_modal_tail,, $$)
                            dx = mou_x - mou_old[0]
                            dy = mou_y - mou_old[1]
                            icon_active.dxy_upd(dx, dy)
                            box_active.dxy_upd(dx, dy)
                            blf_active.x += dx
                            blf_active.y += dy
                            blf_num_active.x += dx
                            blf_active_region.x += dx

                            mou_old[0] = mou_x
                            mou_old[1] = mou_y
                            # >>>
                            return

                        if mou_y < autopan_B:
                            dy = ceil((autopan_B - mou_y) / full_h)
                            if blf_y + dy > lim_B: dy = lim_B - blf_y

                            # <<< 1copy (_md_num_modal_add_del_anim,, $$)
                            if dy > 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != imax:
                                    if y_end > B_add:
                                        endkey += 1
                                        if endkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'endkey', 'y_anim':'y'}$)
                                            o = match_items[endkey]
                                            ee = geticon(o)
                                            blfs[endkey] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y, _speed)
                                            blfs_num[endkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[endkey] = ee
                                            # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        if headkey != filt_ind:
                                            del blfs[headkey]
                                            del blfs_num[headkey]
                                            del icons[headkey]
                                        headkey += 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            elif dy < 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < T_add:
                                        headkey -= 1
                                        if headkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'headkey', 'y_anim':'y'}$)
                                            o = match_items[headkey]
                                            ee = geticon(o)
                                            blfs[headkey] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y, _speed)
                                            blfs_num[headkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[headkey] = ee
                                            # >>>
                                        y += full_h
                                        y_end += full_h
                                        if endkey != filt_ind: 
                                            del blfs[endkey]
                                            del blfs_num[endkey]
                                            del icons[endkey]
                                        endkey -= 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            # >>>
                        elif mou_y > autopan_T:
                            dy = - ceil((mou_y - autopan_T) / full_h)
                            if blf_y + dy < lim_T: dy = lim_T - blf_y

                            # <<< 1copy (_md_num_modal_add_del_anim,, $$)
                            if dy > 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != imax:
                                    if y_end > B_add:
                                        endkey += 1
                                        if endkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'endkey', 'y_anim':'y'}$)
                                            o = match_items[endkey]
                                            ee = geticon(o)
                                            blfs[endkey] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y, _speed)
                                            blfs_num[endkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[endkey] = ee
                                            # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        if headkey != filt_ind:
                                            del blfs[headkey]
                                            del blfs_num[headkey]
                                            del icons[headkey]
                                        headkey += 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            elif dy < 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < T_add:
                                        headkey -= 1
                                        if headkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'headkey', 'y_anim':'y'}$)
                                            o = match_items[headkey]
                                            ee = geticon(o)
                                            blfs[headkey] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y, _speed)
                                            blfs_num[headkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[headkey] = ee
                                            # >>>
                                        y += full_h
                                        y_end += full_h
                                        if endkey != filt_ind: 
                                            del blfs[endkey]
                                            del blfs_num[endkey]
                                            del icons[endkey]
                                        endkey -= 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            # >>>

                        endkey = filt.endkey
                        headkey = filt.headkey
                        i = min(max(headkey, (cvT - mou_y) // full_h), endkey)

                        if i >= filt_ind:
                            y = blf_y - headkey * full_h
                            for r in range(headkey, min(filt_ind, endkey + 1)):
                                # <<< 1copy (_md_num_modal_set_ind_anim,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs_i = blfs[r]
                                    blfs_i.y = y
                                    if blfs_i.speed < _speed: blfs_i.speed = _speed
                                # >>>
                                y -= full_h

                            rangehead = max(headkey, filt_ind + 1)
                            y = blf_y - rangehead * full_h + full_h
                            for r in range(rangehead, i + 1):
                                # <<< 1copy (_md_num_modal_set_ind_anim,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs_i = blfs[r]
                                    blfs_i.y = y
                                    if blfs_i.speed < _speed: blfs_i.speed = _speed
                                # >>>
                                y -= full_h

                            y = blf_y - (i + 1) * full_h
                            for r in range(i + 1, endkey + 1):
                                if r == filt_ind:
                                    y -= full_h
                                    continue
                                # <<< 1copy (_md_num_modal_set_ind_anim,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs_i = blfs[r]
                                    blfs_i.y = y
                                    if blfs_i.speed < _speed: blfs_i.speed = _speed
                                # >>>
                                y -= full_h
                        else:
                            y = blf_y - headkey * full_h
                            for r in range(headkey, i):
                                # <<< 1copy (_md_num_modal_set_ind_anim,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs_i = blfs[r]
                                    blfs_i.y = y
                                    if blfs_i.speed < _speed: blfs_i.speed = _speed
                                # >>>
                                y -= full_h

                            y = blf_y - i * full_h - full_h
                            for r in range(i, min(filt_ind, endkey + 1)):
                                # <<< 1copy (_md_num_modal_set_ind_anim,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs_i = blfs[r]
                                    blfs_i.y = y
                                    if blfs_i.speed < _speed: blfs_i.speed = _speed
                                # >>>
                                y -= full_h

                            y = blf_y - (filt_ind + 1) * full_h
                            for r in range(filt_ind + 1, endkey + 1):
                                # <<< 1copy (_md_num_modal_set_ind_anim,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs_i = blfs[r]
                                    blfs_i.y = y
                                    if blfs_i.speed < _speed: blfs_i.speed = _speed
                                # >>>
                                y -= full_h

                        new_t = _time()
                        dt = new_t - _t
                        _t = new_t
                        for r, e in blfs.items():
                            dis = e.y - e.y_anim
                            if dis == 0.0: continue
                            elif dis < 0:
                                y = max(e.y, e.y_anim - dt * e.speed)
                                e.y_anim = y
                                blfs_num[r].y = y
                                ee = icons[r]
                                ee.B = y + icon_dB
                                ee.T = y + icon_dT
                                ee.upd()
                            else:
                                y = min(e.y, e.y_anim + dt * e.speed)
                                e.y_anim = y
                                blfs_num[r].y = y
                                ee = icons[r]
                                ee.B = y + icon_dB
                                ee.T = y + icon_dT
                                ee.upd()

                        # <<< 1copy (_md_num_modal_tail,, $$)
                        dx = mou_x - mou_old[0]
                        dy = mou_y - mou_old[1]
                        icon_active.dxy_upd(dx, dy)
                        box_active.dxy_upd(dx, dy)
                        blf_active.x += dx
                        blf_active.y += dy
                        blf_num_active.x += dx
                        blf_active_region.x += dx

                        mou_old[0] = mou_x
                        mou_old[1] = mou_y
                        # >>>
                        #|
                    # >>>
                    # <<< 1copy (_md_num_def_localmodal_mt_anim,, $$)
                    def localmodal_mt(w):
                        _ = mtdata
                        if _["is_empty"] == True: return
                        nonlocal _t

                        mt_blfs = _["blfs"]
                        mt_blfs_num = _["blfs_num"]
                        mt_icons = _["icons"]

                        mou_y = mou[1]
                        if mou_y < _["autopan_B"]:
                            dy = ceil((_["autopan_B"] - mou_y) / full_h)
                            if _["blf_y"] + dy > _["lim_B"]: dy = _["lim_B"] - _["blf_y"]

                            # <<< 1copy (_md_num_modal_add_del_mt_anim,, $$)
                            if dy > 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != _["imax"]:
                                    if y_end > _["B_add"]:
                                        endkey += 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'endkey', 'y_anim':'y'}$)
                                        o = _["match_items"][endkey]
                                        ee = geticon(o)
                                        mt_blfs[endkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                        mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[endkey] = ee
                                        # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        del mt_blfs[headkey]
                                        del mt_blfs_num[headkey]
                                        del mt_icons[headkey]
                                        headkey += 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            elif dy < 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < _["T_add"]:
                                        headkey -= 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'headkey', 'y_anim':'y'}$)
                                        o = _["match_items"][headkey]
                                        ee = geticon(o)
                                        mt_blfs[headkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                        mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[headkey] = ee
                                        # >>>
                                        y += full_h
                                        y_end += full_h
                                        del mt_blfs[endkey]
                                        del mt_blfs_num[endkey]
                                        del mt_icons[endkey]
                                        endkey -= 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            # >>>
                        elif mou_y > _["autopan_T"]:
                            dy = - ceil((mou_y - _["autopan_T"]) / full_h)
                            if _["blf_y"] + dy < _["lim_T"]: dy = _["lim_T"] - _["blf_y"]

                            # <<< 1copy (_md_num_modal_add_del_mt_anim,, $$)
                            if dy > 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != _["imax"]:
                                    if y_end > _["B_add"]:
                                        endkey += 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'endkey', 'y_anim':'y'}$)
                                        o = _["match_items"][endkey]
                                        ee = geticon(o)
                                        mt_blfs[endkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                        mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[endkey] = ee
                                        # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        del mt_blfs[headkey]
                                        del mt_blfs_num[headkey]
                                        del mt_icons[headkey]
                                        headkey += 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            elif dy < 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < _["T_add"]:
                                        headkey -= 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt_anim,, ${'_ind_':'headkey', 'y_anim':'y'}$)
                                        o = _["match_items"][headkey]
                                        ee = geticon(o)
                                        mt_blfs[headkey] = BlfColorAnimY(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color, y, _speed)
                                        mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[headkey] = ee
                                        # >>>
                                        y += full_h
                                        y_end += full_h
                                        del mt_blfs[endkey]
                                        del mt_blfs_num[endkey]
                                        del mt_icons[endkey]
                                        endkey -= 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values():
                                    e.y += dy
                                    e.y_anim += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            # >>>

                        endkey = _["filt"].endkey
                        headkey = _["filt"].headkey
                        i = min(max(headkey, (_["cvT"] - mou_y) // full_h), endkey + 1)
                        _["mt_ind"] = i
                        y = _["blf_y"] - headkey * full_h

                        for r in range(headkey, i):
                            # <<< 1copy (_md_num_modal_set_ind_mt_anim,, ${'_ind_':'r', '_y_':'y'}$)
                            if mt_blfs[r].y != y:
                                mt_blfs[r].y = y
                            # >>>
                            y -= full_h
                        y -= full_h
                        for r in range(i, endkey + 1):
                            # <<< 1copy (_md_num_modal_set_ind_mt_anim,, ${'_ind_':'r', '_y_':'y'}$)
                            if mt_blfs[r].y != y:
                                mt_blfs[r].y = y
                            # >>>
                            y -= full_h

                        new_t = _time()
                        dt = new_t - _t
                        _t = new_t
                        for r, e in mt_blfs.items():
                            dis = e.y - e.y_anim
                            if dis == 0.0: continue
                            elif dis < 0:
                                y = max(e.y, e.y_anim - dt * e.speed)
                                e.y_anim = y
                                mt_blfs_num[r].y = y
                                ee = mt_icons[r]
                                ee.B = y + icon_dB
                                ee.T = y + icon_dT
                                ee.upd()
                            else:
                                y = min(e.y, e.y_anim + dt * e.speed)
                                e.y_anim = y
                                mt_blfs_num[r].y = y
                                ee = mt_icons[r]
                                ee.B = y + icon_dB
                                ee.T = y + icon_dT
                                ee.upd()
                        #|
                    # >>>

                    for r, e in blfs.items():
                        if hasattr(e, 'y_anim'): continue
                        blfs[r] = BlfColorAnimY(e.text, e.x, e.y, e.color, e.y, _speed)
                else:
                    # <<< 1copy (_md_num_modal,, $$)
                    def localmodal():
                        # <<< 1copy (_md_num_modal_head,, $$)
                        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']() or TRIGGER['area_sort_modal_cancel']():
                            nonlocal operation
                            operation = "Cancel"
                            _w_.fin()
                            return
                        if endtrigger():
                            _w_.fin()
                            return

                        Admin.REDRAW()
                        mou_x, mou_y = mou
                        # >>>
                        nonlocal blf_y, cvT

                        if upd_active_region() is True:
                            # <<< 1copy (_md_num_modal_tail,, $$)
                            dx = mou_x - mou_old[0]
                            dy = mou_y - mou_old[1]
                            icon_active.dxy_upd(dx, dy)
                            box_active.dxy_upd(dx, dy)
                            blf_active.x += dx
                            blf_active.y += dy
                            blf_num_active.x += dx
                            blf_active_region.x += dx

                            mou_old[0] = mou_x
                            mou_old[1] = mou_y
                            # >>>
                            return

                        if mou_y < autopan_B:
                            dy = ceil((autopan_B - mou_y) / full_h)
                            if blf_y + dy > lim_B: dy = lim_B - blf_y

                            # <<< 1copy (_md_num_modal_add_del,, $$)
                            if dy > 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != imax:
                                    if y_end > B_add:
                                        endkey += 1
                                        if endkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'endkey'}$)
                                            o = match_items[endkey]
                                            ee = geticon(o)
                                            blfs[endkey] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                                            blfs_num[endkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[endkey] = ee
                                            # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        if headkey != filt_ind:
                                            del blfs[headkey]
                                            del blfs_num[headkey]
                                            del icons[headkey]
                                        headkey += 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values(): e.y += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            elif dy < 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < T_add:
                                        headkey -= 1
                                        if headkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'headkey'}$)
                                            o = match_items[headkey]
                                            ee = geticon(o)
                                            blfs[headkey] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                                            blfs_num[headkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[headkey] = ee
                                            # >>>
                                        y += full_h
                                        y_end += full_h
                                        if endkey != filt_ind: 
                                            del blfs[endkey]
                                            del blfs_num[endkey]
                                            del icons[endkey]
                                        endkey -= 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values(): e.y += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            # >>>
                        elif mou_y > autopan_T:
                            dy = - ceil((mou_y - autopan_T) / full_h)
                            if blf_y + dy < lim_T: dy = lim_T - blf_y

                            # <<< 1copy (_md_num_modal_add_del,, $$)
                            if dy > 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != imax:
                                    if y_end > B_add:
                                        endkey += 1
                                        if endkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'endkey'}$)
                                            o = match_items[endkey]
                                            ee = geticon(o)
                                            blfs[endkey] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                                            blfs_num[endkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[endkey] = ee
                                            # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        if headkey != filt_ind:
                                            del blfs[headkey]
                                            del blfs_num[headkey]
                                            del icons[headkey]
                                        headkey += 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values(): e.y += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            elif dy < 0:
                                endkey = filt.endkey
                                headkey = filt.headkey
                                y = blf_y - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < T_add:
                                        headkey -= 1
                                        if headkey != filt_ind:
                                            # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'headkey'}$)
                                            o = match_items[headkey]
                                            ee = geticon(o)
                                            blfs[headkey] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                                            blfs_num[headkey] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                                            ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                            icons[headkey] = ee
                                            # >>>
                                        y += full_h
                                        y_end += full_h
                                        if endkey != filt_ind: 
                                            del blfs[endkey]
                                            del blfs_num[endkey]
                                            del icons[endkey]
                                        endkey -= 1
                                    else: break

                                filt.headkey = headkey
                                filt.endkey = endkey

                                for e in icons.values(): e.dy_upd(dy)
                                for e in blfs.values(): e.y += dy
                                for e in blfs_num.values(): e.y += dy
                                blf_y += dy
                                cvT += dy
                            # >>>

                        endkey = filt.endkey
                        headkey = filt.headkey
                        i = min(max(headkey, (cvT - mou_y) // full_h), endkey)

                        if i >= filt_ind:
                            y = blf_y - headkey * full_h
                            for r in range(headkey, min(filt_ind, endkey + 1)):
                                # <<< 1copy (_md_num_modal_set_ind,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs[r].y = y
                                    blfs_num[r].y = y
                                    icons[r].LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                # >>>
                                y -= full_h

                            rangehead = max(headkey, filt_ind + 1)
                            y = blf_y - rangehead * full_h + full_h
                            for r in range(rangehead, i + 1):
                                # <<< 1copy (_md_num_modal_set_ind,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs[r].y = y
                                    blfs_num[r].y = y
                                    icons[r].LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                # >>>
                                y -= full_h

                            y = blf_y - (i + 1) * full_h
                            for r in range(i + 1, endkey + 1):
                                if r == filt_ind:
                                    y -= full_h
                                    continue
                                # <<< 1copy (_md_num_modal_set_ind,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs[r].y = y
                                    blfs_num[r].y = y
                                    icons[r].LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                # >>>
                                y -= full_h
                        else:
                            y = blf_y - headkey * full_h
                            for r in range(headkey, i):
                                # <<< 1copy (_md_num_modal_set_ind,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs[r].y = y
                                    blfs_num[r].y = y
                                    icons[r].LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                # >>>
                                y -= full_h

                            y = blf_y - i * full_h - full_h
                            for r in range(i, min(filt_ind, endkey + 1)):
                                # <<< 1copy (_md_num_modal_set_ind,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs[r].y = y
                                    blfs_num[r].y = y
                                    icons[r].LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                # >>>
                                y -= full_h

                            y = blf_y - (filt_ind + 1) * full_h
                            for r in range(filt_ind + 1, endkey + 1):
                                # <<< 1copy (_md_num_modal_set_ind,, ${'_ind_':'r', '_y_':'y'}$)
                                if blfs[r].y != y:
                                    blfs[r].y = y
                                    blfs_num[r].y = y
                                    icons[r].LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                                # >>>
                                y -= full_h

                        # <<< 1copy (_md_num_modal_tail,, $$)
                        dx = mou_x - mou_old[0]
                        dy = mou_y - mou_old[1]
                        icon_active.dxy_upd(dx, dy)
                        box_active.dxy_upd(dx, dy)
                        blf_active.x += dx
                        blf_active.y += dy
                        blf_num_active.x += dx
                        blf_active_region.x += dx

                        mou_old[0] = mou_x
                        mou_old[1] = mou_y
                        # >>>
                        #|
                    # >>>
                    # <<< 1copy (_md_num_def_localmodal_mt,, $$)
                    def localmodal_mt(w):
                        _ = mtdata
                        if _["is_empty"] == True: return

                        mt_blfs = _["blfs"]
                        mt_blfs_num = _["blfs_num"]
                        mt_icons = _["icons"]

                        mou_y = mou[1]
                        if mou_y < _["autopan_B"]:
                            dy = ceil((_["autopan_B"] - mou_y) / full_h)
                            if _["blf_y"] + dy > _["lim_B"]: dy = _["lim_B"] - _["blf_y"]

                            # <<< 1copy (_md_num_modal_add_del_mt,, $$)
                            if dy > 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != _["imax"]:
                                    if y_end > _["B_add"]:
                                        endkey += 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'endkey'}$)
                                        o = _["match_items"][endkey]
                                        ee = geticon(o)
                                        mt_blfs[endkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                        mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[endkey] = ee
                                        # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        del mt_blfs[headkey]
                                        del mt_blfs_num[headkey]
                                        del mt_icons[headkey]
                                        headkey += 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values(): e.y += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            elif dy < 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < _["T_add"]:
                                        headkey -= 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'headkey'}$)
                                        o = _["match_items"][headkey]
                                        ee = geticon(o)
                                        mt_blfs[headkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                        mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[headkey] = ee
                                        # >>>
                                        y += full_h
                                        y_end += full_h
                                        del mt_blfs[endkey]
                                        del mt_blfs_num[endkey]
                                        del mt_icons[endkey]
                                        endkey -= 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values(): e.y += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            # >>>
                        elif mou_y > _["autopan_T"]:
                            dy = - ceil((mou_y - _["autopan_T"]) / full_h)
                            if _["blf_y"] + dy < _["lim_T"]: dy = _["lim_T"] - _["blf_y"]

                            # <<< 1copy (_md_num_modal_add_del_mt,, $$)
                            if dy > 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (endkey + 1) * full_h
                                y_end = y + dy
                                while endkey != _["imax"]:
                                    if y_end > _["B_add"]:
                                        endkey += 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'endkey'}$)
                                        o = _["match_items"][endkey]
                                        ee = geticon(o)
                                        mt_blfs[endkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                        mt_blfs_num[endkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[endkey] = ee
                                        # >>>
                                        y -= full_h
                                        y_end -= full_h
                                        del mt_blfs[headkey]
                                        del mt_blfs_num[headkey]
                                        del mt_icons[headkey]
                                        headkey += 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values(): e.y += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            elif dy < 0:
                                endkey = _["filt"].endkey
                                headkey = _["filt"].headkey
                                y = _["blf_y"] - (headkey - 1) * full_h
                                y_end = y + dy
                                while headkey != 0:
                                    if y_end < _["T_add"]:
                                        headkey -= 1
                                        # <<< 1copy (_md_num_modal_append_ind_mt,, ${'_ind_':'headkey'}$)
                                        o = _["match_items"][headkey]
                                        ee = geticon(o)
                                        mt_blfs[headkey] = BlfColor(o.name, _["blf_x2"  if hasattr(ee, "max_index") else "blf_x"], y, blf_active_color)
                                        mt_blfs_num[headkey] = Blf(str(_["names"][o.name] + 1).rjust(3, " "), _["num_x"], y)
                                        ee.LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                                        mt_icons[headkey] = ee
                                        # >>>
                                        y += full_h
                                        y_end += full_h
                                        del mt_blfs[endkey]
                                        del mt_blfs_num[endkey]
                                        del mt_icons[endkey]
                                        endkey -= 1
                                    else: break

                                _["filt"].headkey = headkey
                                _["filt"].endkey = endkey

                                for e in mt_icons.values(): e.dy_upd(dy)
                                for e in mt_blfs.values(): e.y += dy
                                for e in mt_blfs_num.values(): e.y += dy
                                _["blf_y"] += dy
                                _["cvT"] += dy
                            # >>>

                        endkey = _["filt"].endkey
                        headkey = _["filt"].headkey
                        i = min(max(headkey, (_["cvT"] - mou_y) // full_h), endkey + 1)
                        _["mt_ind"] = i
                        y = _["blf_y"] - headkey * full_h

                        for r in range(headkey, i):
                            # <<< 1copy (_md_num_modal_set_ind_mt,, ${'_ind_':'r', '_y_':'y'}$)
                            if mt_blfs[r].y != y:
                                mt_blfs[r].y = y
                                mt_blfs_num[r].y = y
                                mt_icons[r].LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                            # >>>
                            y -= full_h
                        y -= full_h
                        for r in range(i, endkey + 1):
                            # <<< 1copy (_md_num_modal_set_ind_mt,, ${'_ind_':'r', '_y_':'y'}$)
                            if mt_blfs[r].y != y:
                                mt_blfs[r].y = y
                                mt_blfs_num[r].y = y
                                mt_icons[r].LRBT_upd(_["iconL"], _["iconR"], y + icon_dB, y + icon_dT)
                            # >>>
                            y -= full_h
                        #|
                    # >>>
            else:
                new_match_items = []
                new_filt_ind = filt_ind
                match_names = {e.name: r  for r, e in enumerate(match_items)}
                visible_mds = {match_items[r].name  for r in blfs}
                blf_active.text = f'{le_selitems} items'
                if hasattr(icon_active, "max_index"):
                    icon_active.slot0.__class__ = GpuImg_MD_MULTI_SORT
                else:
                    icon_active.__class__ = GpuImg_MD_MULTI_SORT
                icon_active.upd()

                for r, e in enumerate(match_items):
                    if r == filt_ind:
                        new_filt_ind = len(new_match_items)
                        new_match_items.append(e)
                    elif r not in selitems:
                        new_match_items.append(e)

                new_match_names = {e.name: r  for r, e in enumerate(new_match_items)}
                le_new_match = len(new_match_items)
                le_old_blfs = len(blfs) + 1
                blfs.clear()
                blfs_num.clear()
                icons.clear()

                blfs[new_filt_ind] = blf_active
                blfs_num[new_filt_ind] = blf_num_active
                icons[new_filt_ind] = icon_active
                y = blf_active.y + full_h
                r = new_filt_ind
                if P.anim_filter:
                    for r in range(new_filt_ind - 1, -1, -1):
                        if y >= T_add: break
                        y_anim = blf_y - names[new_match_items[r].name] * full_h
                        _speed = abs(y_anim - y) / animtime
                        # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y_anim, _speed)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y_anim)
                        ee.LRBT_upd(iconL, iconR, y_anim + icon_dB, y_anim + icon_dT)
                        icons[r] = ee
                        # >>>
                        y += full_h
                    headkey = r  if r in blfs else r + 1
                    head_y = y
                    y = blf_active.y - full_h
                    r = new_filt_ind
                    for r in range(new_filt_ind + 1, le_new_match):
                        if y <= B_add: break
                        y_anim = blf_y - names[new_match_items[r].name] * full_h
                        _speed = abs(y_anim - y) / animtime
                        # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y_anim, _speed)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y_anim)
                        ee.LRBT_upd(iconL, iconR, y_anim + icon_dB, y_anim + icon_dT)
                        icons[r] = ee
                        # >>>
                        y -= full_h

                    le_new_blfs = len(blfs)
                    for r in range(headkey + le_new_blfs, le_new_match):
                        if le_new_blfs >= le_old_blfs: break
                        y_anim = blf_y - names[new_match_items[r].name] * full_h
                        _speed = abs(y_anim - y) / animtime
                        # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y_anim, _speed)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y_anim)
                        ee.LRBT_upd(iconL, iconR, y_anim + icon_dB, y_anim + icon_dT)
                        icons[r] = ee
                        # >>>
                        y -= full_h
                        le_new_blfs += 1

                    y = head_y
                    for r in range(headkey - 1, -1, -1):
                        if le_new_blfs >= le_old_blfs: break
                        y_anim = blf_y - names[new_match_items[r].name] * full_h
                        _speed = abs(y_anim - y) / animtime
                        # <<< 1copy (_md_num_modal_append_ind_anim,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColorAnimY(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color, y_anim, _speed)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y_anim)
                        ee.LRBT_upd(iconL, iconR, y_anim + icon_dB, y_anim + icon_dT)
                        icons[r] = ee
                        # >>>
                        y += full_h
                        le_new_blfs += 1
                        headkey -= 1
                else:
                    for r in range(new_filt_ind - 1, -1, -1):
                        if y >= T_add: break
                        # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                        ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                        icons[r] = ee
                        # >>>
                        y += full_h
                    headkey = r  if r in blfs else r + 1
                    head_y = y
                    y = blf_active.y - full_h
                    r = new_filt_ind
                    for r in range(new_filt_ind + 1, le_new_match):
                        if y <= B_add: break
                        # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                        ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                        icons[r] = ee
                        # >>>
                        y -= full_h

                    le_new_blfs = len(blfs)
                    for r in range(headkey + le_new_blfs, le_new_match):
                        if le_new_blfs >= le_old_blfs: break
                        # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                        ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                        icons[r] = ee
                        # >>>
                        y -= full_h
                        le_new_blfs += 1

                    y = head_y
                    for r in range(headkey - 1, -1, -1):
                        if le_new_blfs >= le_old_blfs: break
                        # <<< 1copy (_md_num_modal_append_ind,, ${'_ind_':'r', 'match_items':'new_match_items'}$)
                        o = new_match_items[r]
                        ee = geticon(o)
                        blfs[r] = BlfColor(o.name, (blf_x2  if hasattr(ee, "max_index") else blf_x), y, blf_active_color)
                        blfs_num[r] = Blf(str(names[o.name] + 1).rjust(3, " "), num_x, y)
                        ee.LRBT_upd(iconL, iconR, y + icon_dB, y + icon_dT)
                        icons[r] = ee
                        # >>>
                        y += full_h
                        le_new_blfs += 1
                        headkey -= 1

                filt.headkey = headkey
                filt.endkey = len(blfs) + headkey - 1
                filt.match_items = new_match_items

                self.to_modal_filt_num(new_filt_ind, override={
                    "selitems": selitems,
                })
                return

        # <<< 1copy (_md_num_modalend,, $$)
        def localmodalend():
            if mt_win[0] is not None: localmodal_mt_end(mt_win[0])

            kill_evt_except()
            Admin.REDRAW()
            W_DRAW.remove(_draw_)
            callback = None

            def localmodalend_tail():
                sci_filt.w = sci_filt_w
                filt.items_unsort = filt.get_items()
                filt.init_items()
                filt.filter_text(self.blf_text.unclip_text)
                update_data()
                if blfs:
                    filt.r_pan_override()(0, blf_y - blfs[0].y)

                mdnames = {e.name: r  for r, e in enumerate(filt.match_items)}
                for k, e in selitems.copy().items():
                    if e not in mdnames: del selitems[k]
                selnames = filt.selnames
                selnames.update({mdnames[e]: e  for e in selitems.values()})
                if filt.active_index in filt.selnames: del selnames[filt.active_index]
                box_selections = filt.box_selections
                icons = filt.icons
                L = sci_filt.x
                R = filt.box_scroll_bg.L
                for r in range(filt.headkey, filt.endkey + 1):
                    if r in selnames:
                        box_icon = icons[r]
                        e = GpuBox_box_filter_select_bg(L, R, box_icon.B, box_icon.T)
                        e.upd()
                        box_selections[r] = e

                if callback is not None: callback()
                kill_evt_except()
                self.u_draw = self.i_draw
                TAG_UPDATE[2] = True
                #|

            if bpy.context.screen.is_animation_playing:
                _text_ = "This operation cannot be performed\nwhile Timeline is playing animation"
                # <<< 1copy (_md_num_def_call_dialog,, $$)
                def call_dialog():
                    DropDownOk(None, mou, input_text=_text_)

                callback = call_dialog
                # >>>
            elif operation == "Rearrange":
                check_library_object = self.r_check_library_object()  if hasattr(self, "r_check_library_object") else ob
                # <<< 1copy (_md_num_check_library_return,, ${'_ob_':'check_library_object'}$)
                if hasattr(check_library_object, 'library') and check_library_object.library:
                    _text_ = "This operation cannot be performed \nfrom a linked data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                if hasattr(check_library_object, 'override_library') and check_library_object.override_library and check_library_object.override_library.is_system_override:
                    _text_ = "This operation cannot be performed \nfrom a system override data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                # >>>

                endkey = filt.endkey
                headkey = filt.headkey
                i = min(max(headkey, (cvT - mou[1]) // full_h), endkey)
                modifiers = getattr(ob, cls.BL_ATTR)

                if override == None:
                    if i == filt_ind: target_list = modifiers
                    else:
                        name_to_ind = {e.name: r  for r, e in enumerate(match_items)}
                        unfilt_ind_to_ind = {r: name_to_ind[e.name]
                            for r, e in enumerate(modifiers)  if e.name in name_to_ind}
                        ind_to_unfilt_ind = {e: k  for k, e in unfilt_ind_to_ind.items()}

                        filt_ind_unfilt = ind_to_unfilt_ind[filt_ind]
                        target_list = ArrayActive(modifiers, filt_ind_unfilt)
                        target_list.shiftactive(ind_to_unfilt_ind[i] - filt_ind_unfilt)
                else:
                    modifiers_ind = {e.name: r  for r, e in enumerate(modifiers)}
                    arr_sel = ArrayActive(match_items, filt_ind)
                    arr_sel.shiftactive(i - filt_ind)
                    ii = arr_sel.active_index
                    mds_sel = [modifiers[e[1]]  for e in sorted(selitems.items(), key=lambda e: e[0])]
                    s_mds_sel = set(mds_sel)
                    mds_unsel = [e  for e in modifiers  if e not in s_mds_sel]
                    mds_unsel_ind = {e.name: r  for r, e in enumerate(mds_unsel)}
                    arr0 = [arr_sel[r]  for r in range(ii)]
                    if arr0:
                        md_pre = arr0[-1]
                        r0 = mds_unsel_ind[md_pre.name] + 1
                        target_list = mds_unsel[: r0] + mds_sel + mds_unsel[r0 :]
                    else:
                        arr1 = [arr_sel[r]  for r in range(ii + 1, arr_sel.len)]
                        if arr1:
                            md_next = arr1[0]
                            r0 = mds_unsel_ind[md_next.name]
                            target_list = mds_unsel[: r0] + mds_sel + mds_unsel[r0 :]
                        elif mds_unsel:
                            r0 = modifiers_ind[mds_sel[0].name]
                            for e in reversed(mds_unsel):
                                if modifiers_ind[e.name] < r0: break
                            r0 = modifiers_ind[e.name] + 1
                            target_list = mds_unsel[: r0] + mds_sel + mds_unsel[r0 :]
                        else:
                            target_list = mds_sel

                fails = []
                target_list = [e.name  for r, e in enumerate(target_list)]
                with bpy.context.temp_override(object=ob):
                    if hasattr(self, "filt_move_to_index"):
                        modifier_move_to_index = self.filt_move_to_index
                    else:
                        modifier_move_to_index = bpy.ops.object.modifier_move_to_index

                    for r, e in enumerate(target_list):
                        if modifiers[r].name != e:
                            try: modifier_move_to_index(modifier=e, index=r)
                            except Exception as ex:
                                fails.append(f'{e}  |  {format_exception(ex)}')
                ed_undo_push(message=f"{cls.BL_ATTR} rearrange")

                if fails:
                    _text_ = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                elif any(modifiers[r].name != e  for r, e in enumerate(target_list)):
                    _text_ = "Unexpected results,\nsome items must be at the top."
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
            elif operation == "Apply to Top":
                if cls.USE_APPLY is False:
                    localmodalend_tail()
                    return

                # <<< 1copy (_md_num_check_library_return,, ${'_ob_':'ob'}$)
                if hasattr(ob, 'library') and ob.library:
                    _text_ = "This operation cannot be performed \nfrom a linked data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                if hasattr(ob, 'override_library') and ob.override_library and ob.override_library.is_system_override:
                    _text_ = "This operation cannot be performed \nfrom a system override data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                # >>>

                def apply_md():
                    modifiers = ob.modifiers
                    apply_names = {match_items[filt_ind].name}  if override == None else {modifiers[e[1]].name  for e in selitems.items()}

                    fails = []
                    with bpy.context.temp_override(object=ob):
                        modifier_apply = bpy.ops.object.modifier_apply

                        for e in modifiers[:]:
                            if e.name in apply_names:
                                if is_allow_remove_modifier(ob, e) is False:
                                    fails.append(f'{e.name}  |  Unable to apply overridden modifier')
                                    continue

                                try:
                                    modifier_apply(modifier=e.name, single_user=True)
                                except Exception as ex:
                                    fails.append(f'{e.name}  |  {format_exception(ex)}')

                    ed_undo_push(message=f"apply {len(apply_names)} item(s)")

                    if fails:
                        nonlocal callback
                        _text_ = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                        # <<< 1copy (_md_num_def_call_dialog,, $$)
                        def call_dialog():
                            DropDownOk(None, mou, input_text=_text_)

                        callback = call_dialog
                        # >>>

                if ob.data.users > 1:
                    def fn_yes():
                        apply_md()
                        localmodalend_tail()

                    DropDownYesNo(None, mou, fn_yes, localmodalend_tail,
                        input_text=f"{ob.data.users} objects are using current mesh\nIt makes current object single\nDo you want to continue?")
                    return
                else:
                    apply_md()
            elif operation == "Delete":
                # <<< 1copy (_md_num_check_library_return,, ${'_ob_':'ob'}$)
                if hasattr(ob, 'library') and ob.library:
                    _text_ = "This operation cannot be performed \nfrom a linked data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                if hasattr(ob, 'override_library') and ob.override_library and ob.override_library.is_system_override:
                    _text_ = "This operation cannot be performed \nfrom a system override data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                # >>>

                modifiers = getattr(ob, cls.BL_ATTR)
                apply_names = {match_items[filt_ind].name}  if override == None else {modifiers[e[1]].name  for e in selitems.items()}

                fails = []
                with bpy.context.temp_override(object=ob):
                    if hasattr(self, "filt_item_remove"):
                        modifier_remove = self.filt_item_remove

                        for e in reversed(modifiers):
                            if e.name in apply_names:
                                try: modifier_remove(modifier=e.name)
                                except Exception as ex:
                                    fails.append(f'{e.name}  |  {format_exception(ex)}')
                    else:
                        for e in reversed(modifiers):
                            if e.name in apply_names:
                                if is_allow_remove_modifier(ob, e) is False:
                                    fails.append(f'{e.name}  |  Unable to remove overridden modifier')
                                    continue

                                try: modifiers.remove(e)
                                except Exception as ex:
                                    fails.append(f'{e.name}  |  {format_exception(ex)}')

                if fails:
                    _text_ = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>

                ed_undo_push(message=f"{cls.BL_ATTR} delete {len(apply_names)} item(s)")

            elif operation == "Move / Copy / Link":
                mt_ind = mtdata["mt_ind"]  if "mt_ind" in mtdata else 0
                mt_ob = mt_win[0].active_object
                # <<< 1copy (_md_num_check_library_return,, ${'_ob_':'mt_ob'}$)
                if hasattr(mt_ob, 'library') and mt_ob.library:
                    _text_ = "This operation cannot be performed \nfrom a linked data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                if hasattr(mt_ob, 'override_library') and mt_ob.override_library and mt_ob.override_library.is_system_override:
                    _text_ = "This operation cannot be performed \nfrom a system override data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                # >>>

                if hasattr(mt_ob, cls.BL_ATTR):
                    attrs = AttrsMdOperationMenu()
                    modifiers = getattr(ob, cls.BL_ATTR)
                    apply_names = {match_items[filt_ind].name}  if override == None else {modifiers[e[1]].name  for e in selitems.items()}

                    def button_fn_copy(button=None):
                        ddw.fin_from_area()

                        if button.rna.identifier == "md_link": operation = "LINK"
                        elif button.rna.identifier == "md_deeplink": operation = "DEEPLINK"
                        else: operation = "COPY"

                        if mtdata["match_items"]:
                            i = getattr(mt_ob, cls.BL_ATTR).find(mtdata["match_items"][mt_ind].name)  if mt_ind < len(mtdata["match_items"]) else mt_ind
                        else: i = mt_ind

                        success, fails = self.filt_mt_copy_to_index(
                            ob, mt_ob, [e.name  for e in modifiers  if e.name in apply_names], operation, attrs, i)

                        if isinstance(fails, str): fails = [fails]

                        if button.rna.identifier == "md_move":
                            with bpy.context.temp_override(object=ob):
                                if hasattr(self, "filt_item_remove"):
                                    modifier_remove = self.filt_item_remove

                                    for e in reversed(modifiers):
                                        if e.name in apply_names:
                                            try: modifier_remove(modifier=name)
                                            except Exception as ex:
                                                fails.append(f'{name}  |  {format_exception(ex)}')
                                else:
                                    for e in reversed(modifiers):
                                        if e.name in apply_names:
                                            if is_allow_remove_modifier(ob, e) is False:
                                                fails.append(f'{e.name}  |  Unable to remove overridden modifier')
                                                continue

                                            try: modifiers.remove(e)
                                            except Exception as ex:
                                                fails.append(f'{e.name}  |  {format_exception(ex)}')

                        if hasattr(mt_ob, "name"):
                            ed_undo_push(message=f'Copy {cls.BL_ATTR} to "{mt_ob.name}"')
                        else:
                            ed_undo_push(message=f'Copy {cls.BL_ATTR} to')
                        update_data()

                        if fails:
                            le_fails = len(fails)
                            fail_text = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                            DropDownOk(None, mou, input_text=fail_text)
                        #|

                    dic = self.filt_mt_menu({
                        "ob": ob,
                        "mt_ind": mt_ind,
                        "mt_ob": mt_ob,
                        "attrs": attrs,
                        "button_fn_copy": button_fn_copy,
                    })
                    if dic is None:
                        localmodalend_tail()
                        return

                    tx = dic["info_head"]
                    tx += '\n    '.join(apply_names)

                    def endfn(data):
                        localmodalend_tail()

                    ddw = DropDownInfoUtil(None, mou, dic["buttons"], endfn=endfn, title="Operation Menu", input_text=tx)
                    return

            elif operation == "Apply to":
                mt_ind = mtdata["mt_ind"]  if "mt_ind" in mtdata else 0
                mt_ob = mt_win[0].active_object
                # <<< 1copy (_md_num_check_library_return,, ${'_ob_':'mt_ob'}$)
                if hasattr(mt_ob, 'library') and mt_ob.library:
                    _text_ = "This operation cannot be performed \nfrom a linked data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                if hasattr(mt_ob, 'override_library') and mt_ob.override_library and mt_ob.override_library.is_system_override:
                    _text_ = "This operation cannot be performed \nfrom a system override data-block"
                    # <<< 1copy (_md_num_def_call_dialog,, $$)
                    def call_dialog():
                        DropDownOk(None, mou, input_text=_text_)

                    callback = call_dialog
                    # >>>
                    localmodalend_tail()
                    return
                # >>>

                if hasattr(mt_ob, "modifiers") and mt_ob.type == ob.type:
                    def apply_md():
                        modifiers = ob.modifiers
                        apply_names = {match_items[filt_ind].name}  if override == None else {modifiers[e[1]].name  for e in selitems.items()}

                        mt_mds = mt_ob.modifiers
                        fails = []
                        copied = []
                        with bpy.context.temp_override(object=ob, selected_objects=[mt_ob]):
                            modifier_copy_to_selected = bpy.ops.object.modifier_copy_to_selected
                            for e in modifiers[:]:
                                if e.name in apply_names:
                                    if is_allow_remove_modifier(ob, e) is False:
                                        fails.append(f'{e.name}  |  Unable to move overridden modifier')
                                        continue

                                    try: modifier_copy_to_selected(modifier=e.name)
                                    except Exception as ex:
                                        fails.append(f'{e.name}  |  {format_exception(ex)}')
                                        continue

                                    new_md = mt_mds.active
                                    copied.append(new_md)

                        if copied:
                            with bpy.context.temp_override(object=ob):
                                for e in reversed(modifiers):
                                    if e.name in apply_names:
                                        if is_allow_remove_modifier(ob, e) is False:
                                            continue

                                        try: modifiers.remove(e)
                                        except Exception as ex:
                                            fails.append(f'{e.name}  |  {format_exception(ex)}')

                            with bpy.context.temp_override(object=mt_ob):
                                modifier_apply = bpy.ops.object.modifier_apply

                                for e in copied:
                                    try: modifier_apply(modifier=e.name, single_user=True)
                                    except Exception as ex:
                                        fails.append(f'{e.name}  |  {format_exception(ex)}')
                                        try: mt_mds.remove(e)
                                        except Exception as ex:
                                            fails.append(f'{e.name}  |  {format_exception(ex)}')

                            ed_undo_push(message=f"MD apply {len(apply_names)} item(s) to {mt_ob.name}")

                        if fails:
                            nonlocal callback
                            _text_ = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                            # <<< 1copy (_md_num_def_call_dialog,, $$)
                            def call_dialog():
                                DropDownOk(None, mou, input_text=_text_)

                            callback = call_dialog
                            # >>>

                    if mt_ob.data.users > 1:
                        def fn_yes():
                            apply_md()
                            localmodalend_tail()

                        DropDownYesNo(None, mou, fn_yes, localmodalend_tail,
                            input_text=f"{mt_ob.data.users} objects are using current mesh\nIt makes current object single\nDo you want to continue?")
                        return
                    else:
                        apply_md()

            localmodalend_tail()
            #|
        # >>>
        # <<< 1copy (_md_num_draw,, $$)
        def localdraw():
            blend_set('ALPHA')
            box_active.bind_draw()
            icon_active.bind_draw()
            y = blf_active.y
            blfSize(font0, blf_active_size)
            blfColor(font0, *blf_active_color)
            blfPos(font0, blf_active.x, y, 0)
            blfDraw(font0, blf_active_text)

            blfColor(font0, *blf_active_region.color)
            blfPos(font0, blf_active_region.x, y, 0)
            blfDraw(font0, operation)

            blfSize(font0, blf_num_active_size)
            blfColor(font0, *blf_num_active_color)
            blfPos(font0, blf_num_active.x, y, 0)
            blfDraw(font0, blf_num_active_text)
            #|
        # >>>
        # <<< 1copy (_md_num_def_upd_active_region,, $$)
        def upd_active_region():
            nonlocal operation, operation_override
            if TRIGGER['area_sort_modal_apply']():
                if cls.USE_APPLY is True: operation_override = "Apply to Top"
            elif TRIGGER['area_sort_modal_del'](): operation_override = "Delete"
            elif TRIGGER['area_sort_modal_sort'](): operation_override = "Rearrange"

            if box_win.inbox(mou):
                if mt_win[0] is not None:
                    localmodal_mt_end(mt_win[0])
                    mt_win[0] = None

                if operation != operation_override:
                    operation = operation_override
                    if operation == "Rearrange":
                        if hasattr(icon_active, "max_index"):
                            icon_active.slot0.__class__ = icon_active_class
                        else:
                            icon_active.__class__ = icon_active_class
                        blf_active_region.color = blf_active_color
                    elif operation == "Delete":
                        if hasattr(icon_active, "max_index"):
                            icon_active.slot0.__class__ = GpuImg_delete
                        else:
                            icon_active.__class__ = GpuImg_delete
                        blf_active_region.color = COL_box_filter_fg_del
                    else:
                        if hasattr(icon_active, "max_index"):
                            icon_active.slot0.__class__ = GpuImg_apply
                        else:
                            icon_active.__class__ = GpuImg_apply
                        blf_active_region.color = COL_box_filter_fg_apply
                    icon_active.upd()
            else:
                for w in ws:
                    if w.box_win.inbox(mou):
                        if mt_win[0] is not w:
                            if mt_win[0] is not None: localmodal_mt_end(mt_win[0])
                            mt_win[0] = w
                            localmodal_mt_init(w)

                        if operation_override == "Apply to Top":
                            if operation != "Apply to":
                                operation = "Apply to"
                                if hasattr(icon_active, "max_index"):
                                    icon_active.slot0.__class__ = GpuImg_apply
                                else:
                                    icon_active.__class__ = GpuImg_apply
                                blf_active_region.color = COL_box_filter_fg_apply
                                icon_active.upd()
                        else:
                            if operation != "Move / Copy / Link":
                                operation = "Move / Copy / Link"
                                if hasattr(icon_active, "max_index"):
                                    icon_active.slot0.__class__ = icon_active_class
                                else:
                                    icon_active.__class__ = icon_active_class
                                blf_active_region.color = blf_active_color
                                icon_active.upd()

                        localmodal_mt(w)
                        return True
                if mt_win[0] is not None:
                    localmodal_mt_end(mt_win[0])
                    mt_win[0] = None
                if operation != "Delete":
                    operation = "Delete"
                    if hasattr(icon_active, "max_index"):
                        icon_active.slot0.__class__ = GpuImg_delete
                    else:
                        icon_active.__class__ = GpuImg_delete
                    blf_active_region.color = COL_box_filter_fg_del
                    icon_active.upd()
                return True
            #|
        # >>>
        # <<< 1copy (_md_num_def_localmodal_mt_init,, $$)
        def localmodal_mt_init(w):

            _ = mtdata

            area = getattr(w, AREA_NAME)
            filt = area.filt
            blfs = filt.blfs
            match_items = filt.match_items
            sci_filt = area.scissor_filt
            if blfs:
                le = len(match_items)
                imax = le - 1
                BB = sci_filt.y
                TT = BB + sci_filt.h
                T_add = TT - widget_rim - D_SIZE['font_main_dT'] + full_h
                B_add = BB + widget_rim + D_SIZE['font_main_dy'] - full_h - full_h2
                lim_B = BB + D_SIZE['font_main_dy'] + SIZE_filter[2] + widget_rim + le * full_h
                lim_T = TT - widget_rim - SIZE_filter[2] - D_SIZE['font_main_dT']
                if lim_B < lim_T: lim_B = lim_T

                r = filt.headkey
                filt.icons_button.clear()
                icons = filt.icons
                blfs_num = filt.blfs_num
                geticon = filt.get_icon
                if hasattr(icons[r], "max_index"):
                    blf_x2 = blfs[r].x
                    blf_x = blf_x2 - _h
                else:
                    blf_x = blfs[r].x
                    blf_x2 = blf_x + _h
                num_x = blfs_num[r].x
                blf_y = blfs[r].y + full_h * r
                iconL = icons[r].L
                iconR = icons[r].R
                names = filt.names
                active_index = filt.active_index

                _["le"] = le
                _["imax"] = imax
                _["BB"] = BB
                _["TT"] = TT
                _["T_add"] = T_add
                _["B_add"] = B_add
                _["lim_B"] = lim_B
                _["lim_T"] = lim_T
                _["icons"] = icons
                _["blfs_num"] = blfs_num
                _["blf_x"] = blf_x
                _["blf_x2"] = blf_x2
                _["num_x"] = num_x
                _["blf_y"] = blf_y
                _["iconL"] = iconL
                _["iconR"] = iconR
                _["names"] = names
                _["active_index"] = active_index
                _["cvT"] = icons[r].T + widget_rim + r * full_h

                if sci_filt.h <= full_h:
                    _["autopan_B"] = BB
                    _["autopan_T"] = TT
                else:
                    _["autopan_B"] = BB + full_h2
                    _["autopan_T"] = TT - full_h2

                _["sci_filt"] = sci_filt
                _["sci_filt_w"] = sci_filt.w
                sci_filt.w += area.box_region.r_w()
                filt.box_active.LRBT_upd(0, 0, 0, 0)
                filt.box_scroll.LRBT_upd(0, 0, 0, 0)
                filt.box_selections.clear()
                _["is_empty"] = False
                if use_anim is True:
                    area.u_draw = area.i_draw_num_anim

                    for r, e in blfs.items():
                        blfs[r] = BlfColorAnimY(e.text, e.x, e.y, e.color, e.y, _speed)
            else:
                _["is_empty"] = True

            _["area"] = area
            _["filt"] = filt
            _["blfs"] = blfs
            _["match_items"] = match_items
            #|
        # >>>
        # <<< 1copy (_md_num_def_localmodal_mt_end,, $$)
        def localmodal_mt_end(w):

            _ = mtdata

            area = _["area"]
            area.u_draw = area.i_draw

            if _["is_empty"] == False:
                _["sci_filt"].w = _["sci_filt_w"]
                _["filt"].redraw_from(_["filt"].headkey, _["blf_y"], len(_["blfs"]))
            #|
        # >>>

        box_win = self.w.box_win
        offset = round(cls.FILT_NUM_HOVER_OFFSET * (self.box_filter.R - self.box_filter.L))
        L = self.box_filter.L + offset
        R = self.box_filter.R
        B = icon_active.B - widget_rim
        T = icon_active.T + widget_rim
        icon_active.dx_upd(offset)
        blf_active.x += offset
        box_active = GpuRim(COL_box_filter_num_modal, COL_box_filter_num_modal_rim,
            L, R, B, T, widget_rim)
        box_active.upd()
        font0 = FONT0
        blf_active_size = D_SIZE['font_main']
        blf_num_active_color = COL_box_filter_fg_label
        blf_num_active_text = blf_num_active.text
        blf_num_active_size = D_SIZE['font_label']
        # <<< 1copy (init_blf_clipping_end,, ${"D_SIZE['font_size']":"blf_active_size"}$)
        blfSize(FONT0, blf_active_size)
        blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
        # >>>
        x = blf_num_active.x - round(blfDimen(font0, "Move / Copy / Link")[0])
        blf_active_region = BlfColor(x=x, color=blf_active_color)
        blf_active_text = r_blf_clipping_end(blf_active.text, blf_active.x, x - D_SIZE['font_main_dx'])
        cvT = icon_active.T + widget_rim + filt_ind * full_h
        operation = "Rearrange"
        operation_override = "Rearrange"

        Admin.REDRAW()
        sci_filt_w = sci_filt.w
        sci_filt.w += self.box_region.r_w()
        if sci_filt.h <= full_h:
            autopan_B = BB
            autopan_T = TT
        else:
            autopan_B = BB + full_h2
            autopan_T = TT - full_h2
        filt.box_hover_button.LRBT_upd(0, 0, 0, 0)
        filt.box_hover.LRBT_upd(0, 0, 0, 0)
        filt.box_active.LRBT_upd(0, 0, 0, 0)
        filt.box_scroll.LRBT_upd(0, 0, 0, 0)
        filt.box_selections.clear()
        filt.blfs_info.clear()
        cls_win = self.w.__class__
        ws = [e  for e in reversed(W_MODAL)  if isinstance(e, cls_win)]
        mt_win = [None]
        mtdata = {}

        _draw_ = Udraw(localdraw)
        W_DRAW.append(_draw_)
        if P.anim_filter:
            use_anim = True
            _time = time
            _t = _time()
            push_modal = m.ADMIN.push_modal
            push_modal()
            self.u_draw = self.i_draw_num_anim
        else:
            use_anim = False
            self.u_draw = self.i_draw_num

        TAG_UPDATE[2] = False
        _w_ = Head(self, localmodal, localmodalend)
        localmodal()
        #|

    def filt_mt_menu(self, dic):
        ob = dic["ob"]
        mt_ind = dic["mt_ind"]
        mt_ob = dic["mt_ob"]
        attrs = dic["attrs"]
        button_fn_copy = dic["button_fn_copy"]

        if mt_ob.type != ob.type: return None

        tx = f'Object "{mt_ob.name}"\n    Mesh user(s) :  {mt_ob.data.users}\n\nItem(s) from object "{ob.name}" :\n    '

        button_copy = ButtonFn(None, RNA_md_copy, button_fn_copy)
        button_move = ButtonFn(None, RNA_md_move, button_fn_copy)
        if ob == mt_ob: button_move.dark()
        button_link = ButtonFn(None, RNA_md_link, button_fn_copy)
        button_deeplink = ButtonFn(None, RNA_md_deeplink, button_fn_copy)
        buttons = [
            ButtonGroupAlignLR(None, ButtonBoolTemp(None, RNA_md_use_keyframe, attrs), title_head="Include"),
            ButtonGroupAlignLR(None, ButtonBoolTemp(None, RNA_md_use_driver, attrs)),
            ButtonSep(3),
            ButtonSplit(None, button_copy, button_move, SIZE_button[1]),
            ButtonSplit(None, button_link, button_deeplink, SIZE_button[1]),
        ]
        buttons[0].button0.set(P.ModifierEditor.md_copy_use_keyframe)
        buttons[1].button0.set(P.ModifierEditor.md_copy_use_driver)
        return {"info_head": tx, "buttons": buttons}
        #|
    def filt_mt_copy_to_index(self, ob, mt_ob, apply_names, operation, attrs, i):
        return ops_mds_copy_to_object(
            ob, mt_ob, apply_names, operation, attrs.md_use_keyframe, attrs.md_use_driver, i
        )
        #|

    def check_ob_editable(self):
        w = self.w
        oj = w.active_object
        if not hasattr(oj, "modifiers"): return False
        if not oj.modifiers: return False
        s = r_library_or_override_message(oj)
        if s:
            report(s)
            return False
        return True
        #|

    @ catchBug
    def evt_area_rename(self, override=None):

        if not self.check_ob_editable(): return
        if override is None:
            # <<< 1copy (0AreaFilterYModifier_if_ind_safe,, $$)
            filt = self.filt
            blfs = filt.blfs
            if not blfs: return

            T = blfs[filt.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
            i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + filt.headkey

            if 0 <= i < len(filt.match_items):
            # >>>
                pass
            else: return
        else:
            filt = self.filt
            i, T = override

        L, R, B, _ = self.box_filter.r_LRBT()
        T += - SIZE_border[3] + (filt.headkey - i) * D_SIZE['widget_full_h']
        DropDownEnumRename(None, (L, R, T - SIZE_widget[0], T), self.w.active_object, filt.match_items[i])
        #|
    def evt_area_copy_to_selected(self, override=None):

        if bpy.context.screen.is_animation_playing:
            DropDownOk(None, MOUSE, input_text="This operation cannot be performed\nwhile Timeline is playing animation")
            return

        if override is None:
            # <<< 1copy (0AreaFilterYModifier_if_ind_safe,, $$)
            filt = self.filt
            blfs = filt.blfs
            if not blfs: return

            T = blfs[filt.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
            i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + filt.headkey

            if 0 <= i < len(filt.match_items):
            # >>>
                pass
            else: return
        else:
            filt = self.filt
            i, T = override

        match_items = filt.match_items
        selnames = filt.selnames
        act_index = filt.active_index

        selected_mds = [match_items[r]
            for r in range(len(match_items))  if r in selnames or r == act_index]
        selected_mds_and_mouse_index = [match_items[r]
            for r in range(len(match_items))  if r in selnames or r in {act_index, i}]
        md_mouse_index = [match_items[i]]
        attrs = AttrsMdCopyToSelectedOperationMenu()

        def button_fn_cancel(button=None):
            ddw.fin_from_area()
            #|
        def button_fn_run(button=None):
            if attrs.md_use_code:
                a0 = ddw.areas[0]

                success, message = eval_copy_to_selected(self.w.active_object, a0.tex.as_string())
                if success:
                    ddw.fin_from_area()
                    update_scene_push("MD Copy to Selected")
                    if message: DropDownOk(None, MOUSE, input_text=message)
                else:
                    update_scene_push("MD Copy to Selected")
                    DropDownOk(None, MOUSE, input_text=message)
            else:
                ddw.fin_from_area()

                success, message = eval_copy_to_selected(self.w.active_object, r_code_copy_to_selected(
                    attrs.md_use_code,
                    attrs.md_copy_operation,
                    attrs.md_use_keyframe,
                    attrs.md_use_driver,
                    attrs.ob_use_self,
                    self.w.active_object,
                    modifiers))

                if success:
                    update_scene_push("MD Copy to Selected")
                    if message: DropDownOk(None, MOUSE, input_text=message)
                else:
                    update_scene_push("MD Copy to Selected")
                    DropDownOk(None, MOUSE, input_text=message)
            #|
        def button_fn_get_code(v):
            if attrs.md_use_code:
                if bu_operation.is_dark() is False: buttons[2].dark()
                return

            button_fn_use_code(v)
            #|
        def button_fn_use_code(v):
            if attrs.md_use_code:
                if bu_operation.is_dark() is False: buttons[2].dark()
                return
            if bu_operation.is_dark() is True: buttons[2].light()

            if attrs.md_use_selection:
                modifiers = selected_mds_and_mouse_index  if attrs.md_use_mouse_index else selected_mds
            elif attrs.md_use_mouse_index:
                modifiers = md_mouse_index
            else:
                modifiers = []

            ddw.set_area_info(r_code_copy_to_selected(
                attrs.md_use_code,
                attrs.md_copy_operation,
                attrs.md_use_keyframe,
                attrs.md_use_driver,
                attrs.ob_use_self,
                self.w.active_object,
                modifiers
            ))
            #|

        bu_use_code = ButtonGroupAlignTitleLeft(None, ButtonBoolTemp(None, RNA_md_use_code, attrs))
        bu_operation = ButtonGroupAlignTitleLeft(None, ButtonEnumXYTemp(None, RNA_md_copy_operation, attrs, 1))
        button_run = ButtonFn(None, RNA_run, button_fn_run)
        button_cancel = ButtonFn(None, RNA_cancel, button_fn_cancel)
        bu_use_keyframe = ButtonGroupAlignLR(
            None, ButtonBoolTemp(None, RNA_md_use_keyframe, attrs), title_head="Include")
        bu_use_driver = ButtonGroupAlignLR(None, ButtonBoolTemp(None, RNA_md_use_driver, attrs))
        bu_use_mouse_index = ButtonGroupAlignLR(None, ButtonBoolTemp(None, RNA_md_use_mouse_index, attrs), title_head="Include Modifier")
        bu_use_selection = ButtonGroupAlignLR(None, ButtonBoolTemp(None, RNA_md_use_selection, attrs))
        bu_use_self = ButtonGroupAlignLR(None, ButtonBoolTemp(None, RNA_ob_use_self, attrs), title_head="Include Object")

        gap = SIZE_button[1]

        buttons = [
            bu_use_code,
            ButtonSep(3),
            ButtonSplit(None, bu_operation,
                ButtonGroupY(None, [
                    bu_use_keyframe,
                    bu_use_driver,
                    ButtonSep(3),
                    bu_use_mouse_index,
                    bu_use_selection,
                    ButtonSep(3),
                    bu_use_self], gap),
                gap, 0.5),
            ButtonSep(3),
            ButtonSplit(None, button_run, button_cancel, gap),
        ]
        PP = P.ModifierEditor
        md_copy_use_keyframe = PP.md_copy_to_selected_use_keyframe
        md_copy_use_driver = PP.md_copy_to_selected_use_driver
        md_copy_use_mouse_index = PP.md_copy_to_selected_use_mouse_index
        md_copy_use_selection = PP.md_copy_to_selected_use_selection
        md_copy_use_self = PP.md_copy_to_selected_use_self
        md_copy_operation = PP.md_copy_to_selected_operation
        md_copy_use_code = PP.md_copy_to_selected_use_code

        bu_use_code.button0.set(md_copy_use_code)
        bu_use_keyframe.button0.set(md_copy_use_keyframe)
        bu_use_driver.button0.set(md_copy_use_driver)
        bu_use_mouse_index.button0.set(md_copy_use_mouse_index)
        bu_use_selection.button0.set(md_copy_use_selection)
        bu_use_self.button0.set(md_copy_use_self)
        bu_operation.button0.set(md_copy_operation)

        if md_copy_use_selection:
            modifiers = selected_mds_and_mouse_index  if md_copy_use_mouse_index else selected_mds
        elif md_copy_use_mouse_index:
            modifiers = md_mouse_index
        else:
            modifiers = []

        ddw = DropDownInfoUtil(None, MOUSE, buttons,
            title="Copy to Selected", input_text=r_code_copy_to_selected(
                md_copy_use_code,
                md_copy_operation,
                md_copy_use_keyframe,
                md_copy_use_driver,
                md_copy_use_self,
                self.w.active_object,
                modifiers
            ), font_id=FONT1, row_count=20, width_fac=4.0)

        L = bu_use_code.button0.box_button.L
        dif = L - bu_operation.button0.box_button[0].L
        for e in bu_operation.button0.box_button:
            e.L = L
            e.upd()
        bu_operation.blf_title.x += dif

        bu_use_code.button0.set_callback = button_fn_use_code
        bu_operation.button0.set_callback = button_fn_get_code
        bu_use_keyframe.button0.set_callback = button_fn_get_code
        bu_use_driver.button0.set_callback = button_fn_get_code
        bu_use_mouse_index.button0.set_callback = button_fn_get_code
        bu_use_selection.button0.set_callback = button_fn_get_code
        bu_use_self.button0.set_callback = button_fn_get_code
        #|
    def evt_remove_from_keying_set(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        success, s = r_remove_from_keying_set(ob, f'{dp_head}{region_index}')
        if s:
            DropDownOk(None, MOUSE, input_text=s)
        #|
    def evt_add_to_keying_set(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        success, s = r_add_to_keying_set(ob, f'{dp_head}{region_index}')
        if s:
            DropDownOk(None, MOUSE, input_text=s)
        #|
    def evt_copy_full_data_path(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=False, evtkill=True)
        if i is None: return

        bpy.context.window_manager.clipboard = f'{r_ID_dp(ob)}.modifiers["{escape_identifier(self.filt.match_items[i].name)}"].{region_index}'
        report("Full Data Path is copied to the clipboard")
        #|
    def evt_copy_data_path(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=False, evtkill=True)
        if i is None: return

        bpy.context.window_manager.clipboard = f'modifiers["{escape_identifier(self.filt.match_items[i].name)}"].{region_index}'
        report("Data Path is copied to the clipboard")
        #|
    def evt_paste_full_data_path_as_driver(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        s = bpy.context.window_manager.clipboard
        if not s:
            report("Clipboard is empty")
            return

        tar_obj, dr_path = r_obj_path_by_full_path(s)
        if tar_obj is None:
            report("Invalid path")
            return

        id_type = r_id_type(tar_obj)
        if id_type is None:
            report("Invalid Object ID Type")
            return

        try:
            fc = r_md_driver_add(ob, self.filt.match_items[i].name, region_index)
            vs = fc.driver.variables
            v = vs[0] if vs else vs.new()
            tar = v.targets[0]
            tar.id_type = id_type
            tar.id = tar_obj
            tar.data_path = dr_path

            update_scene_push("MD Paste Full Path as Driver")
        except:
            report("Failure")
        #|
    def evt_delete_driver(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        if r_md_driver_remove(ob, self.filt.match_items[i].name, region_index):
            update_scene_push("Delete Driver")
        else:
            report("Driver not found")
        #|
    def evt_add_driver(self, override=None, use_editor=False):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        try:
            filt = self.filt
            if r_md_keyframe(ob, filt.match_items[i].name, region_index):
                report("Unable to add driver when keyframe already exists")
                return

            dp_head = f'modifiers["{escape_identifier(filt.match_items[i].name)}"].'
            dr = tr_driver(ob, dp_head + region_index)
            if dr:
                if use_editor:
                    open_driver_editor_from(ob, dp_head + region_index)
            else:
                if r_driver_add_safe(ob, dp_head, region_index):
                    update_scene_push("Add Driver")
                    if use_editor and P.is_open_driver_editor:
                        open_driver_editor_from(ob, dp_head + region_index)
                else:
                    report("Not allow add driver to current property")
        except Exception as ex:

            report("Failure")
        #|
    def evt_clear_keyframe(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        try:
            fcs = ob.animation_data.action.fcurves
            fcs.remove(fcs.find(f'modifiers["{escape_identifier(self.filt.match_items[i].name)}"].{region_index}'))

            update_scene_push("Clear Keyframe")
        except:
            report("Keyframe not found")
        #|
    def evt_delete_keyframe(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        try:
            ob.keyframe_delete(f'modifiers["{escape_identifier(self.filt.match_items[i].name)}"].{region_index}')

            update_scene_push("Delete Keyframe")
        except:
            report("Keyframe not found")
        #|
    def evt_insert_keyframe(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'
        if is_allow_add_driver(ob, dp_head, region_index, pp=modifier) is False:
            report(is_allow_add_driver.message)
            return

        try:
            if r_md_driver(ob, self.filt.match_items[i].name, region_index):
                report("Unable to Insert Keyframe when Driver already exists")
                return

            ob.keyframe_insert(f'modifiers["{escape_identifier(self.filt.match_items[i].name)}"].{region_index}')

            update_scene_push("Insert Keyframe")
        except:
            report("Keyframe not found")
        #|
    def evt_del(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, (0, 0), poll_library=True, evtkill=True)
        if i is None: return

        active_modifier = self.w.active_modifier
        if not active_modifier: return

        try:
            if override is None: override = P.filter_delete_behavior
            if override == "ACTIVE":
                if is_allow_remove_modifier(ob, active_modifier):
                    ob.modifiers.remove(active_modifier)
                else:
                    report("Overridden data-blocks cannot be deleted")
            else:
                modifiers = ob.modifiers
                selnames = self.filt.selnames.copy()
                selnames[modifiers.find(active_modifier.name)] = active_modifier.name
                fails = []
                for k in sorted(selnames.keys(), reverse=True):
                    name = selnames[k]
                    if name in modifiers:
                        modifier = modifiers[name]
                        if is_allow_remove_modifier(ob, modifier):
                            modifiers.remove(modifier)
                        else:
                            fails.append(modifier)

                if fails:
                    report(f'{len(fails)} overridden modifier(s) not deleted')
            update_scene_push("remove modifier(s)")
        except: pass
        #|
    @ catch
    def evt_apply(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, (0, 0), poll_library=True, evtkill=True)
        if i is None: return

        active_modifier = self.w.active_modifier
        if not active_modifier: return

        if override is None: override = P.filter_delete_behavior
        if override == "ACTIVE":
            apply_names = [active_modifier.name]
        else:
            modifiers = ob.modifiers
            selnames = self.filt.selnames.copy()
            selnames[modifiers.find(active_modifier.name)] = active_modifier.name
            apply_names = [selnames[k]  for k in sorted(selnames.keys())]

        def apply_md():
            modifiers = ob.modifiers
            fails = []
            with bpy.context.temp_override(object=ob):
                modifier_apply = bpy.ops.object.modifier_apply

                for name in apply_names:
                    if is_allow_remove_modifier(ob, modifiers) is False:
                        fails.append(f'{name}  |  Unable to apply overridden modifier')
                        continue

                    try: modifier_apply(modifier=name, single_user=True)
                    except Exception as ex:
                        fails.append(f'{name}  |  {format_exception(ex)}')

            update_scene_push("apply modifier(s)")

            if fails:
                _text_ = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                DropDownOk(None, MOUSE, input_text=_text_)

        if ob.data.users > 1:
            DropDownYesNo(None, MOUSE, apply_md, N,
                input_text=f"{ob.data.users} objects are using current mesh\nIt makes current object single\nDo you want to continue?")
            return
        else:
            apply_md()
        #|
    @ catch
    def evt_apply_as_shapekey(self, override=None):

        # /* 0area_evt_apply_as_shapekey
        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        active_modifier = self.w.active_modifier
        if not active_modifier: return

        if override is None: override = P.filter_delete_behavior
        if override == "ACTIVE":
            apply_names = [active_modifier.name]
        else:
            modifiers = ob.modifiers
            selnames = self.filt.selnames.copy()
            selnames[modifiers.find(active_modifier.name)] = active_modifier.name
            apply_names = [selnames[k]  for k in sorted(selnames.keys())]

        def apply_md():
            modifiers = ob.modifiers
            fails = []
            with bpy.context.temp_override(object=ob):
                modifier_apply = bpy.ops.object.modifier_apply_as_shapekey

                for name in apply_names:
                    if name in modifiers:
                        if modifiers[name].type not in S_md_apply_as_shapekey:
                            fails.append(f'{name}  |  Unsupported modifier type')
                            continue

                    if is_allow_remove_modifier(ob, modifiers) is False:
                        fails.append(f'{name}  |  Unable to apply overridden modifier')
                        continue

                    try: modifier_apply(keep_modifier=False, modifier=name)
                    except Exception as ex:
                        fails.append(f'{name}  |  {format_exception(ex)}')

            update_scene_push("apply modifier(s) as shape key")

            if fails:
                _text_ = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                DropDownOk(None, MOUSE, input_text=_text_)

        if ob.data.users > 1:
            DropDownYesNo(None, MOUSE, apply_md, N,
                input_text=f"{ob.data.users} objects are using current mesh\nDo you want to continue?")
            return
        else:
            apply_md()
        # */
    def evt_save_as_shapekey(self, override=None):

        # <<< 1copy (0area_evt_apply_as_shapekey,, ${
        #     'keep_modifier=False': 'keep_modifier=True',
        #     'apply modifier': 'save modifier',
        # }$)
        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        active_modifier = self.w.active_modifier
        if not active_modifier: return

        if override is None: override = P.filter_delete_behavior
        if override == "ACTIVE":
            apply_names = [active_modifier.name]
        else:
            modifiers = ob.modifiers
            selnames = self.filt.selnames.copy()
            selnames[modifiers.find(active_modifier.name)] = active_modifier.name
            apply_names = [selnames[k]  for k in sorted(selnames.keys())]

        def apply_md():
            modifiers = ob.modifiers
            fails = []
            with bpy.context.temp_override(object=ob):
                modifier_apply = bpy.ops.object.modifier_apply_as_shapekey

                for name in apply_names:
                    if name in modifiers:
                        if modifiers[name].type not in S_md_apply_as_shapekey:
                            fails.append(f'{name}  |  Unsupported modifier type')
                            continue

                    if is_allow_remove_modifier(ob, modifiers) is False:
                        fails.append(f'{name}  |  Unable to apply overridden modifier')
                        continue

                    try: modifier_apply(keep_modifier=True, modifier=name)
                    except Exception as ex:
                        fails.append(f'{name}  |  {format_exception(ex)}')

            update_scene_push("save modifier(s) as shape key")

            if fails:
                _text_ = f"{len(fails)} Failure(s) :\n    " + "\n    ".join(fails)
                DropDownOk(None, MOUSE, input_text=_text_)

        if ob.data.users > 1:
            DropDownYesNo(None, MOUSE, apply_md, N,
                input_text=f"{ob.data.users} objects are using current mesh\nDo you want to continue?")
            return
        else:
            apply_md()
        # >>>
        #|
    def evt_add(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, (0, 0), poll_library=True, evtkill=True)
        if i is None: return

        self.w.area_md.items[0].bufn_new_modifier()
        #|
    def evt_use_pin_to_last(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, override, poll_library=True, evtkill=True)
        if i is None: return

        modifier = self.filt.match_items[i]
        if is_allow_remove_modifier(ob, modifier):
            modifier.use_pin_to_last = not modifier.use_pin_to_last
            update_scene_push("MD Pin to last toggle")
        else:
            report("Unable to Pin current modifier")
        #|
    def evt_pin_to_last_selected(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, (0, 0), poll_library=True, evtkill=True)
        if i is None: return

        fails_count = 0

        for e in reversed(self.r_selected_modifiers()):
            if is_allow_remove_modifier(ob, e):
                e.use_pin_to_last = True
            else:
                fails_count += 1

        update_scene_push("MD Pin to last selected")
        if fails_count != 0:
            report(f'Unable to Pin {fails_count} modifier(s)')
        #|
    def evt_unpin_to_last_selected(self, override=None):

        i, region_index, ob = C_filt_evt_head(self, (0, 0), poll_library=True, evtkill=True)
        if i is None: return

        fails_count = 0

        for e in self.r_selected_modifiers():
            if is_allow_remove_modifier(ob, e):
                e.use_pin_to_last = False
            else:
                fails_count += 1

        update_scene_push("MD Unpin to last selected")
        if fails_count != 0:
            report(f'Unable to Pin {fails_count} modifier(s)')
        #|
    def evt_select_all_toggle(self, override=None):
        i, region_index, ob = C_filt_evt_head(self, (0, 0), poll_library=False, evtkill=True)
        if i is None: return

        filt = self.filt

        match_items = filt.match_items
        selected_modifiers = self.r_selected_modifiers()
        if len(selected_modifiers) == len(match_items):
            filt.selnames.clear()
            filt.box_selections.clear()
        else:
            selnames = filt.selnames
            for r in range(len(match_items)):
                selnames[r] = match_items[r].name

        update_data()
        Admin.REDRAW()
        #|
    def evt_batch(self, filt_ind, region_ind):

        ob = self.w.active_object
        if ob == None: return
        if not hasattr(ob, "modifiers"): return
        if not hasattr(ob, "animation_data"): return
        is_spline = ob.type in S_spline_modifier_types
        filt = self.filt
        blfs = filt.blfs
        if not blfs: return
        match_items = filt.match_items
        if not match_items: return

        if is_spline and region_ind == "show_on_cage":
            boo = False  if match_items[filt_ind].use_apply_on_spline else True
        else:
            boo = False  if getattr(match_items[filt_ind], region_ind) else True

        is_override_library = True  if hasattr(ob, 'override_library') and ob.override_library else False
        is_only_viewport = ob.is_editable == False or (is_override_library and ob.override_library.is_system_override)
        isnot_library = not is_only_viewport

        e = match_items[filt_ind]
        if region_ind == "show_on_cage":
            for e in match_items:
                if is_override_library and hasattr(e, "is_override_data") and e.is_override_data: continue
                else:
                    if is_spline:
                        if e.type in S_md_apply_on_spline and e.use_apply_on_spline != boo and isnot_library:
                            e.use_apply_on_spline = boo
                    else:
                        if e.type in S_MD_BUTTON4 and e.show_on_cage != boo and isnot_library:
                            e.show_on_cage = boo

        elif region_ind == "show_in_editmode":
            for e in match_items:
                if is_override_library and hasattr(e, "is_override_data") and e.is_override_data: continue
                elif e.type in S_MD_USE_EDITMODE and e.show_in_editmode != boo and isnot_library:
                    e.show_in_editmode = boo

        elif region_ind == "show_viewport":
            if e.type in S_MD_USE_RENDER and e.show_viewport != boo:
                for o in match_items:
                    o.show_viewport = boo

        elif region_ind == "show_render":
            if e.type in S_MD_USE_RENDER and e.show_render != boo and isnot_library:
                for o in match_items:
                    o.show_render = boo
        #|

    def r_selected_modifiers(self):
        filt = self.filt

        match_items = filt.match_items
        selnames = filt.selnames
        act_index = filt.active_index

        return [match_items[r]
            for r in range(len(match_items))  if r in selnames or r == act_index]
        #|

    def dxy(self, dx, dy):
        super().dxy(dx, dy)
        self.box_region.dxy_upd(dx, dy)
        #|

    def i_draw(self):
        # ref_AreaFilterY_i_draw
        blend_set('ALPHA')
        boxes = self.boxes
        boxes[0].bind_draw()
        boxes[1].bind_draw()
        boxes[2].bind_draw()
        boxes[3].bind_draw()
        boxes[6].bind_draw()
        boxes[7].bind_draw()
        boxes[8].bind_draw()
        boxes[9].bind_draw()
        boxes[10].bind_draw()
        boxes[11].bind_draw()
        boxes[12].bind_draw()

        filt = self.filt
        self.box_region.bind_draw()

        filt.box_scroll_bg.bind_draw()
        filt.box_scroll.bind_draw()

        scissor_filt = self.scissor_filt
        w_scissor = self.w.scissor
        scissor_set(w_scissor.x, scissor_filt.y, w_scissor.w, scissor_filt.h)
        filt.box_hover_button.bind_draw()
        for e in filt.icons_button.values(): e.bind_draw()
        blfSize(FONT0, D_SIZE['font_label'])
        blfColor(FONT0, *COL_box_filter_fg_label)
        for e in filt.blfs_num.values():
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)

        self.scissor_text_box.use()
        blend_set('ALPHA')
        boxes[4].bind_draw()
        boxes[5].bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        # w_scissor.use()
        scissor_filt.use()
        blend_set('ALPHA')
        for e in filt.box_selections.values(): e.bind_draw()
        filt.box_active.bind_draw()
        filt.box_hover.bind_draw()
        blfs = filt.blfs
        for e in filt.icons.values(): e.bind_draw()
        for e in blfs.values():
            blfColor(FONT0, *e.color)
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)
        blfColor(FONT0, *COL_box_filter_fg_info)
        for k, e in filt.blfs_info.items():
            blfPos(FONT0, e.x, blfs[k].y, 0)
            blfDraw(FONT0, e.text)
        w_scissor.use()
        #|
    def i_draw_num(self):
        # /* 0area_i_draw_num
        # ref_AreaFilterY_i_draw
        blend_set('ALPHA')
        boxes = self.boxes
        boxes[0].bind_draw()
        boxes[1].bind_draw()
        boxes[2].bind_draw()
        boxes[3].bind_draw()
        boxes[6].bind_draw()
        boxes[7].bind_draw()
        boxes[8].bind_draw()
        boxes[9].bind_draw()
        boxes[10].bind_draw()
        boxes[11].bind_draw()
        boxes[12].bind_draw()

        filt = self.filt
        self.box_region.bind_draw()

        # filt.box_scroll_bg.bind_draw()
        # filt.box_scroll.bind_draw()

        scissor_filt = self.scissor_filt
        w_scissor = self.w.scissor
        scissor_set(w_scissor.x, scissor_filt.y, w_scissor.w, scissor_filt.h)
        # filt.box_hover_button.bind_draw()
        # for e in filt.icons_button.values(): e.bind_draw()
        blfSize(FONT0, D_SIZE['font_label'])
        blfColor(FONT0, *COL_box_filter_fg_label)
        for e in filt.blfs_num.values():
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)

        self.scissor_text_box.use()
        blend_set('ALPHA')
        boxes[4].bind_draw()
        boxes[5].bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        # w_scissor.use()
        scissor_filt.use()
        blend_set('ALPHA')
        # for e in filt.box_selections.values(): e.bind_draw()
        # filt.box_active.bind_draw()
        # filt.box_hover.bind_draw()
        # blfs = filt.blfs
        for e in filt.icons.values(): e.bind_draw()
        for o in filt.blfs.values():
            blfColor(FONT0, *o.color)
            blfPos(FONT0, o.x, o.y, 0)
            blfDraw(FONT0, o.text)
        # blfColor(FONT0, *COL_box_filter_fg_info)
        # for k, e in filt.blfs_info.items():
        #     blfPos(FONT0, e.x, blfs[k].y, 0)
        #     blfDraw(FONT0, e.text)
        w_scissor.use()
        # */
    def i_draw_num_anim(self):
        # <<< 1copy (0area_i_draw_num,, ${'blfPos(FONT0, o.x, o.y, 0)':'blfPos(FONT0, o.x, o.y_anim, 0)'}$)
        # ref_AreaFilterY_i_draw
        blend_set('ALPHA')
        boxes = self.boxes
        boxes[0].bind_draw()
        boxes[1].bind_draw()
        boxes[2].bind_draw()
        boxes[3].bind_draw()
        boxes[6].bind_draw()
        boxes[7].bind_draw()
        boxes[8].bind_draw()
        boxes[9].bind_draw()
        boxes[10].bind_draw()
        boxes[11].bind_draw()
        boxes[12].bind_draw()

        filt = self.filt
        self.box_region.bind_draw()

        # filt.box_scroll_bg.bind_draw()
        # filt.box_scroll.bind_draw()

        scissor_filt = self.scissor_filt
        w_scissor = self.w.scissor
        scissor_set(w_scissor.x, scissor_filt.y, w_scissor.w, scissor_filt.h)
        # filt.box_hover_button.bind_draw()
        # for e in filt.icons_button.values(): e.bind_draw()
        blfSize(FONT0, D_SIZE['font_label'])
        blfColor(FONT0, *COL_box_filter_fg_label)
        for e in filt.blfs_num.values():
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)

        self.scissor_text_box.use()
        blend_set('ALPHA')
        boxes[4].bind_draw()
        boxes[5].bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        # w_scissor.use()
        scissor_filt.use()
        blend_set('ALPHA')
        # for e in filt.box_selections.values(): e.bind_draw()
        # filt.box_active.bind_draw()
        # filt.box_hover.bind_draw()
        # blfs = filt.blfs
        for e in filt.icons.values(): e.bind_draw()
        for o in filt.blfs.values():
            blfColor(FONT0, *o.color)
            blfPos(FONT0, o.x, o.y_anim, 0)
            blfDraw(FONT0, o.text)
        # blfColor(FONT0, *COL_box_filter_fg_info)
        # for k, e in filt.blfs_info.items():
        #     blfPos(FONT0, e.x, blfs[k].y, 0)
        #     blfDraw(FONT0, e.text)
        w_scissor.use()
        # >>>
        #|

    def upd_data(self):
        super().upd_data()
        ob = self.w.active_modifier
        filt = self.filt
        if ob:
            filt.upd_active_index(filt.names.get(ob.name, None))
        else:
            filt.upd_active_index(None)

        ob = self.w.active_object
        selnames = filt.selnames
        box_selections = filt.box_selections
        active_index = filt.active_index
        if hasattr(ob, "animation_data"): pass
        else: return

        anim_data = ob.animation_data
        match_items = filt.match_items
        for r, buttonslot in filt.icons_button.items():
            buttonslot.update_slot(anim_data, match_items[r])

            if r in selnames:
                if r == active_index:
                    del selnames[r]
                    if r in box_selections: del box_selections[r]
                elif r not in box_selections:
                    box_icon = filt.icons[r]
                    e = GpuBox_box_filter_select_bg(self.scissor_filt.x, filt.box_scroll_bg.L,
                        box_icon.B, box_icon.T)
                    e.upd()
                    box_selections[r] = e
            else:
                if r in box_selections: del box_selections[r]
        #|
    #|
    #|

class FilterYDriverVar(FilterYModifier):
    __slots__ = ()

    def __init__(self, w, get_items, get_icon, get_info):
        self.icons_button = {}
        self.blfs_num = {}
        self.selnames = {}
        self.box_selections = {}
        self.box_hover_button = GpuImg_MD_BG_SHOW_HOVER()
        self.box_hover_button.set_draw_state(False)

        FilterY.__init__(self, w, get_items, geticon_DriverVar, None)
        #|

    def r_region_icon_fn(self, ob): return geticon_fake
    #|
    #|
class AreaFilterYDriverVar(AreaFilterYModifier):
    __slots__ = ()

    CLS_FILTER = FilterYDriverVar
    BL_ATTR = "variables"
    FILT_NUM_HOVER_OFFSET = -0.8
    USE_APPLY = False
    AREA_NAME = "area_vars"

    def init_callback(self):
        self.filt.set_active_index_callback = self.w.set_active_var
        #|
    def calc_region_width(self):
        return SIZE_widget[0] + SIZE_border[3] + D_SIZE['font_main_dy']
        #|

    def r_region_index(self, x, i):
        if x >= self.box_region.L: return "num"
        return "null"
        #|
    def filt_region_event(self, B, T, i, filt):
        if i is None:
            hover = filt.box_hover_button
            if hover.L == 0 and hover.R == 0: pass
            else:
                hover.LRBT_upd(0, 0, 0, 0)
                Admin.REDRAW()
            return False

        x = MOUSE[0]
        if x >= self.box_region.L:
            R = self.box_region.inner[1]
            L = R - D_SIZE['widget_full_h']

            hover = filt.box_hover_button
            if hover.L == L and hover.R == R and hover.B == B and hover.T == T: pass
            else:
                hover.LRBT_upd(L, R, B, T)
                Admin.REDRAW()

            if TRIGGER['area_sort']():
                self.to_modal_filt_num(i)
                return True
        else:
            hover = filt.box_hover_button
            if hover.L == 0 and hover.R == 0: pass
            else:
                hover.LRBT_upd(0, 0, 0, 0)
                Admin.REDRAW()
        return False
        #|

    def r_check_library_object(self): return self.w.props.id
    def filt_move_to_index(self, modifier, index):
        variables = self.w.active_object.variables
        if modifier in variables:
            driver_var_move_to_index.variables = variables
            driver_var_move_to_index(modifier, index)
        #|
    def filt_item_remove(self, modifier):
        variables = self.w.active_object.variables
        if modifier in variables:
            variables.remove(variables[modifier])
        #|
    def filt_mt_menu(self, dic):
        ob = dic["ob"]
        mt_ind = dic["mt_ind"]
        mt_ob = dic["mt_ob"]
        attrs = dic["attrs"]
        button_fn_copy = dic["button_fn_copy"]

        tx = f'Item(s) from Data-Block :\n    '

        button_copy = ButtonFn(None, RNA_md_copy, button_fn_copy)
        button_move = ButtonFn(None, RNA_md_move, button_fn_copy)
        if ob == mt_ob: button_move.dark()
        buttons = [
            ButtonSplit(None, button_copy, button_move, SIZE_button[1]),
        ]
        return {"info_head": tx, "buttons": buttons}
        #|
    def filt_mt_copy_to_index(self, ob, mt_ob, apply_names, operation, attrs, i):
        ob_variables = ob.variables
        mt_variables = mt_ob.variables
        var_new = mt_variables.new
        new_names = []
        fails = []

        for name in apply_names:
            try:
                e = var_new()
                driver_var_name_set(mt_variables, e, name)
                copy_driver_variable(ob_variables[name], e, False)
                new_names.append(e.name)
            except Exception as ex:
                fails.append(f'► Unexpected error, please report to the author  |  {name}  |  {ex}')

        driver_var_move_to_index.variables = mt_variables
        for name in reversed(new_names):
            try:
                driver_var_move_to_index(name, i)
            except Exception as ex:
                fails.append(f'► Unexpected error, please report to the author  |  {name}  |  {ex}')

        if fails: return False, fails
        return True, fails
        #|

    def evt_del(self, override=None):

        w = self.w
        props = w.props
        fc = w.bars["driver"].button0.check(props.id)
        if not hasattr(fc, "driver"): return
        dr = fc.driver
        if not hasattr(dr, "variables"): return
        if not dr.variables: return
        variables = dr.variables
        try:
            if override is None: override = P.filter_delete_behavior
            if override == "ACTIVE":
                if w.active_var_name in variables:
                    variables.remove(variables[w.active_var_name])
            else:
                selnames = w.area_vars.filt.selnames.copy()
                if w.active_var_name in variables:
                    selnames[variables.find(w.active_var_name)] = w.active_var_name
                    for k in sorted(selnames.keys(), reverse=True):
                        name = selnames[k]
                        if name in variables:
                            variables.remove(variables[name])

            update_scene_push("Remove variable(s)")
        except: pass
        #|
    def evt_add(self, override=None):

        self.w.area_var.items[0].bufn_new_var()
        #|
    @ catchBug
    def evt_area_rename(self, override=None):

        if not hasattr(self.w.active_object, "variables"): return
        if override is None:
            # <<< 1copy (0AreaFilterYModifier_if_ind_safe,, $$)
            filt = self.filt
            blfs = filt.blfs
            if not blfs: return

            T = blfs[filt.headkey].y + D_SIZE['font_main_dT'] + SIZE_border[3]
            i = (T - MOUSE[1]) // D_SIZE['widget_full_h'] + filt.headkey

            if 0 <= i < len(filt.match_items):
            # >>>
                pass
            else: return
        else:
            filt = self.filt
            i, T = override

        active_index = filt.active_index
        @ catch
        def callback():
            filt.set_active_index(active_index, callback=True)

        L, R, B, _ = self.box_filter.r_LRBT()
        T += - SIZE_border[3] + (filt.headkey - i) * D_SIZE['widget_full_h']
        DropDownEnumRename(None, (L, R, T - SIZE_widget[0], T), self.w.props.id,
            filt.match_items[i],
            items = self.w.active_object.variables,
            write_callback = callback)
        #|
    def evt_select_all_toggle(self, override=None): pass
    def evt_batch(self, filt_ind, region_ind): pass

    def upd_data(self):
        AreaFilterY.upd_data(self)
        filt = self.filt
        ob = self.w.active_var
        if ob:
            ob_name = ob.name
            i = -1
            for i, e in enumerate(self.w.active_object.variables):
                if e.name == ob_name: break

            filt.upd_active_index(None  if i == -1 else i)
        else:
            filt.upd_active_index(None)

        ob = self.w.active_object
        selnames = filt.selnames
        box_selections = filt.box_selections
        active_index = filt.active_index

        match_items = filt.match_items
        for r, buttonslot in filt.icons_button.items():
            # buttonslot.update_slot(None, match_items[r])

            if r in selnames:
                if r == active_index:
                    del selnames[r]
                    if r in box_selections: del box_selections[r]
                elif r not in box_selections:
                    box_icon = filt.icons[r]
                    e = GpuBox_box_filter_select_bg(self.scissor_filt.x, filt.box_scroll_bg.L,
                        box_icon.B, box_icon.T)
                    e.upd()
                    box_selections[r] = e
            else:
                if r in box_selections: del box_selections[r]
        #|
    #|
    #|


class AttrsMdOperationMenu:
    __slots__ = 'md_use_keyframe', 'md_use_driver'

    def __init__(self):
        self.md_use_keyframe = False
        self.md_use_driver = False
        #|
    #|
    #|
class AttrsMdCopyToSelectedOperationMenu:
    __slots__ = (
        'md_use_code',
        'md_copy_operation',
        'md_use_keyframe',
        'md_use_driver',
        'md_use_mouse_index',
        'md_use_selection',
        'ob_use_self')

    def __init__(self):
        self.md_use_code = False
        self.md_copy_operation = "COPY"
        self.md_use_keyframe = False
        self.md_use_driver = False
        self.md_use_mouse_index = False
        self.md_use_selection = False
        self.ob_use_self = False
        #|
    #|
    #|


## _file_ ##
def late_import():
    #|
    import bpy, blf, gpu, math
    from time import time

    Image = bpy.types.Image
    units_to_value = bpy.utils.units.to_value
    timer_reg = bpy.app.timers.register
    timer_unreg = bpy.app.timers.unregister
    timer_isreg = bpy.app.timers.is_registered

    blfSize = blf.size
    blfColor = blf.color
    blfPos = blf.position
    blfDraw = blf.draw
    blfDimen = blf.dimensions

    blend_set = gpu.state.blend_set
    scissor_set = gpu.state.scissor_set

    floor = math.floor
    ceil = math.ceil

    from .  import VMD

    m = VMD.m

    # <<< 1mp (VMD.block
    block = VMD.block
    ButtonGroup = block.ButtonGroup
    ButtonGroupY = block.ButtonGroupY
    ButtonGroupAlignTitleLeft = block.ButtonGroupAlignTitleLeft
    ButtonGroupAlignLR = block.ButtonGroupAlignLR
    ButtonSplit = block.ButtonSplit
    ButtonBoolTemp = block.ButtonBoolTemp
    ButtonFn = block.ButtonFn
    ButtonSep = block.ButtonSep
    ButtonEnumXYTemp = block.ButtonEnumXYTemp
    D_gn_subtype_unit = block.D_gn_subtype_unit
    open_driver_editor_from = block.open_driver_editor_from
    # >>>

    # <<< 1mp (VMD.dd
    dd = VMD.dd
    DropDownRMKeymap = dd.DropDownRMKeymap
    DropDownRM = dd.DropDownRM
    DropDownValTab = dd.DropDownValTab
    DropDownOk = dd.DropDownOk
    DropDownYesNo = dd.DropDownYesNo
    DropDownInfoUtil = dd.DropDownInfoUtil
    DDPreviewImage = dd.DDPreviewImage
    DropDownEnumRename = dd.DropDownEnumRename
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    kill_evt = keysys.kill_evt
    kill_evt_except = keysys.kill_evt_except
    MOUSE = keysys.MOUSE
    MOUSE_OVERRIDE = keysys.MOUSE_OVERRIDE
    EVT_TYPE = keysys.EVT_TYPE
    TRIGGER = keysys.TRIGGER
    r_end_trigger = keysys.r_end_trigger
    rm_get_info_km = keysys.rm_get_info_km
    # >>>

    # <<< 1mp (m
    P = m.P
    Admin = m.Admin
    W_HEAD = m.W_HEAD
    W_DRAW = m.W_DRAW
    W_MODAL = m.W_MODAL
    W_FOCUS = m.W_FOCUS
    REGION_DATA = m.REGION_DATA
    r_mouseloop = m.r_mouseloop
    r_mouse_from_region = m.r_mouse_from_region
    TAG_RENAME = m.TAG_RENAME
    UnitSystem = m.UnitSystem
    r_unit_factor = m.r_unit_factor
    r_hud_region = m.r_hud_region
    BlendDataTemp = m.BlendDataTemp
    update_data = m.update_data
    TAG_UPDATE = m.TAG_UPDATE
    # >>>

    # <<< 1mp (VMD.rna
    rna = VMD.rna
    RNA_md_use_keyframe = rna.RNA_md_use_keyframe
    RNA_md_use_driver = rna.RNA_md_use_driver
    RNA_md_copy = rna.RNA_md_copy
    RNA_md_move = rna.RNA_md_move
    RNA_md_link = rna.RNA_md_link
    RNA_md_deeplink = rna.RNA_md_deeplink
    RNA_md_copy_operation = rna.RNA_md_copy_operation
    RNA_md_use_mouse_index = rna.RNA_md_use_mouse_index
    RNA_md_use_selection = rna.RNA_md_use_selection
    RNA_md_use_code = rna.RNA_md_use_code
    RNA_ob_use_self = rna.RNA_ob_use_self
    RNA_run = rna.RNA_run
    RNA_cancel = rna.RNA_cancel
    # >>>

    # <<< 1mp (VMD.win
    win = VMD.win
    r_full_protect_dxy = win.r_full_protect_dxy
    Head = win.Head
    # >>>

    # <<< 1mp (VMD.evals.evalcopytoselected
    evalcopytoselected = VMD.evals.evalcopytoselected
    eval_copy_to_selected = evalcopytoselected.eval_copy_to_selected
    # >>>

    util = VMD.util

    # <<< 1mp (util.algebra
    algebra = util.algebra
    rf_linear_01 = algebra.rf_linear_01
    rf_linear_01_inv = algebra.rf_linear_01_inv
    # >>>

    # <<< 1mp (util.com
    com = util.com
    N = com.N
    NT = com.NT
    NF = com.NF
    NF1 = com.NF1
    NKW = com.NKW
    r_mouse_y_index = com.r_mouse_y_index
    r_prev_word_index = com.r_prev_word_index
    r_next_word_index = com.r_next_word_index
    r_word_select_index = com.r_word_select_index
    r_filter_function = com.r_filter_function
    complex_to_display = com.complex_to_display
    value_to_display = com.value_to_display
    is_value = com.is_value
    # >>>

    # <<< 1mp (util.const
    const = util.const
    FLO_0000 = const.FLO_0000
    STR_09 = const.STR_09
    # >>>

    # <<< 1mp (util.txt
    txt = util.txt
    Text = txt.Text
    # >>>

    # <<< 1mp (util.types
    types = util.types
    NameValue = types.NameValue
    LocalHistory = types.LocalHistory
    Udraw = types.Udraw
    ArrayActive = types.ArrayActive
    # >>>

    utilbl = VMD.utilbl

    # <<< 1mp (utilbl
    blg = utilbl.blg
    # >>>

    # <<< 1mp (blg
    Blf = blg.Blf
    BlfColor = blg.BlfColor
    BlfColorAnimY = blg.BlfColorAnimY
    BlfClip = blg.BlfClip
    BlfClipColor = blg.BlfClipColor
    rl_blf_wrap = blg.rl_blf_wrap
    GpuBox = blg.GpuBox
    GpuRim = blg.GpuRim
    GpuRimArea = blg.GpuRimArea
    GpuBox_area = blg.GpuBox_area
    GpuBox_box_filter_active_bg = blg.GpuBox_box_filter_active_bg
    GpuBox_box_filter_select_bg = blg.GpuBox_box_filter_select_bg
    GpuBox_box_filter_hover_bg = blg.GpuBox_box_filter_hover_bg
    GpuPickerH = blg.GpuPickerH
    GpuPickerSV = blg.GpuPickerSV
    GpuSelection = blg.GpuSelection
    GpuImgNull = blg.GpuImgNull
    GpuImgSlot2 = blg.GpuImgSlot2
    GpuImg_search = blg.GpuImg_search
    GpuImg_delete = blg.GpuImg_delete
    GpuImg_apply = blg.GpuImg_apply
    GpuImg_filter_match_case = blg.GpuImg_filter_match_case
    GpuImg_filter_match_whole_word = blg.GpuImg_filter_match_whole_word
    GpuImg_filter_match_end_left = blg.GpuImg_filter_match_end_left
    GpuImg_filter_match_end_right = blg.GpuImg_filter_match_end_right
    GpuImg_filter_match_active = blg.GpuImg_filter_match_active
    GpuImg_filter_match_hover = blg.GpuImg_filter_match_hover
    GpuImg_py_exp_on = blg.GpuImg_py_exp_on
    GpuImg_py_exp_off = blg.GpuImg_py_exp_off
    GpuImg_hue_cursor = blg.GpuImg_hue_cursor
    GpuImg_hue_button = blg.GpuImg_hue_button
    GpuImg_SHOW_ON_CAGE_ON = blg.GpuImg_SHOW_ON_CAGE_ON
    GpuImg_SHOW_IN_EDITMODE_ON = blg.GpuImg_SHOW_IN_EDITMODE_ON
    GpuImg_SHOW_VIEWPORT_ON = blg.GpuImg_SHOW_VIEWPORT_ON
    GpuImg_SHOW_RENDER_ON = blg.GpuImg_SHOW_RENDER_ON
    GpuImg_USE_APPLY_ON_SPLINE_ON = blg.GpuImg_USE_APPLY_ON_SPLINE_ON
    GpuImg_SHOW_ON_CAGE_OFF = blg.GpuImg_SHOW_ON_CAGE_OFF
    GpuImg_SHOW_IN_EDITMODE_OFF = blg.GpuImg_SHOW_IN_EDITMODE_OFF
    GpuImg_SHOW_VIEWPORT_OFF = blg.GpuImg_SHOW_VIEWPORT_OFF
    GpuImg_SHOW_RENDER_OFF = blg.GpuImg_SHOW_RENDER_OFF
    GpuImg_USE_APPLY_ON_SPLINE_OFF = blg.GpuImg_USE_APPLY_ON_SPLINE_OFF
    GpuImg_SHOW_ON_CAGE_DISABLE = blg.GpuImg_SHOW_ON_CAGE_DISABLE
    GpuImg_SHOW_IN_EDITMODE_DISABLE = blg.GpuImg_SHOW_IN_EDITMODE_DISABLE
    GpuImg_SHOW_VIEWPORT_DISABLE = blg.GpuImg_SHOW_VIEWPORT_DISABLE
    GpuImg_SHOW_RENDER_DISABLE = blg.GpuImg_SHOW_RENDER_DISABLE
    GpuImg_MD_BG_SHOW_HOVER = blg.GpuImg_MD_BG_SHOW_HOVER
    GpuImg_MD_MULTI_SORT = blg.GpuImg_MD_MULTI_SORT
    GpuImg_MD_BG_SHOW_ON = blg.GpuImg_MD_BG_SHOW_ON
    GpuImg_MD_BG_SHOW_OFF = blg.GpuImg_MD_BG_SHOW_OFF
    GpuImg_MD_OVERRIDE_ON = blg.GpuImg_MD_OVERRIDE_ON
    GpuImg_MD_OVERRIDE_OFF = blg.GpuImg_MD_OVERRIDE_OFF
    GpuImg_settings_keymap_addon_key = blg.GpuImg_settings_keymap_addon_key
    r_blf_clipping_end = blg.r_blf_clipping_end
    r_blf_ind = blg.r_blf_ind
    r_blf_index = blg.r_blf_index
    r_widget_font_dx_dy_dT = blg.r_widget_font_dx_dy_dT
    Scissor = blg.Scissor
    report = blg.report
    geticon_Object = blg.geticon_Object
    getinfo_Object = blg.getinfo_Object
    geticon_Modifier = blg.geticon_Modifier
    geticon_DriverVar = blg.geticon_DriverVar
    geticon_fake = blg.geticon_fake
    r_geticon_Modifier_button = blg.r_geticon_Modifier_button
    GpuImgSlotDriverVar = blg.GpuImgSlotDriverVar
    r_modifier_button_BG_on = blg.r_modifier_button_BG_on
    r_modifier_button_BG_off = blg.r_modifier_button_BG_off
    S_MD_USE_RENDER = blg.S_MD_USE_RENDER
    S_MD_USE_EDITMODE = blg.S_MD_USE_EDITMODE
    S_MD_BUTTON4 = blg.S_MD_BUTTON4
    D_SIZE = blg.D_SIZE
    FONT0 = blg.FONT0
    FONT1 = blg.FONT1
    SIZE_title = blg.SIZE_title
    SIZE_border = blg.SIZE_border
    SIZE_filter = blg.SIZE_filter
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_widget = blg.SIZE_widget
    SIZE_block = blg.SIZE_block
    SIZE_button = blg.SIZE_button
    COL_box_text = blg.COL_box_text
    COL_box_text_active = blg.COL_box_text_active
    COL_box_text_rim = blg.COL_box_text_rim
    COL_box_filter = blg.COL_box_filter
    COL_box_filter_rim = blg.COL_box_filter_rim
    COL_dd_title_fg = blg.COL_dd_title_fg
    COL_box_text_fg = blg.COL_box_text_fg
    COL_box_text_fg_ignore = blg.COL_box_text_fg_ignore
    COL_box_cursor_beam = blg.COL_box_cursor_beam
    COL_box_cursor_beam_off = blg.COL_box_cursor_beam_off
    COL_box_text_selection = blg.COL_box_text_selection
    COL_box_text_selection_off = blg.COL_box_text_selection_off
    COL_box_filter_fg = blg.COL_box_filter_fg
    COL_box_filter_fg_info = blg.COL_box_filter_fg_info
    COL_box_filter_fg_label = blg.COL_box_filter_fg_label
    COL_box_filter_fg_apply = blg.COL_box_filter_fg_apply
    COL_box_filter_fg_del = blg.COL_box_filter_fg_del
    COL_box_scrollbar_bg = blg.COL_box_scrollbar_bg
    COL_box_scrollbar = blg.COL_box_scrollbar
    COL_box_block_scrollbar_bg = blg.COL_box_block_scrollbar_bg
    COL_box_block_scrollbar = blg.COL_box_block_scrollbar
    COL_box_hue_bg = blg.COL_box_hue_bg
    COL_block = blg.COL_block
    COL_block_calc_display = blg.COL_block_calc_display
    COL_block_calc_display_fo = blg.COL_block_calc_display_fo
    COL_box_filter_region = blg.COL_box_filter_region
    COL_box_filter_region_rim = blg.COL_box_filter_region_rim
    COL_box_filter_num_modal = blg.COL_box_filter_num_modal
    COL_box_filter_num_modal_rim = blg.COL_box_filter_num_modal_rim
    COL_box_area_header_bg = blg.COL_box_area_header_bg
    COL_box_text_read = blg.COL_box_text_read
    COL_box_text_read_rim = blg.COL_box_text_read_rim
    COL_block_fg = blg.COL_block_fg
    # >>>

    # <<< 1mp (utilbl.calc
    calc = utilbl.calc
    Calc = calc.Calc
    round_dec = calc.round_dec
    tran_unit = calc.tran_unit
    # >>>

    # <<< 1mp (utilbl.general
    general = utilbl.general
    format_exception = general.format_exception
    r_obj_path_by_full_path = general.r_obj_path_by_full_path
    r_add_to_keying_set = general.r_add_to_keying_set
    r_remove_from_keying_set = general.r_remove_from_keying_set
    update_scene_push = general.update_scene_push
    driver_var_move_to_index = general.driver_var_move_to_index
    driver_var_name_set = general.driver_var_name_set
    copy_driver_variable = general.copy_driver_variable
    r_library_or_override_message = general.r_library_or_override_message
    r_unsupport_override_message = general.r_unsupport_override_message
    r_ID_dp = general.r_ID_dp
    is_allow_remove_modifier = general.is_allow_remove_modifier
    is_allow_add_driver = general.is_allow_add_driver
    r_driver_add_safe = general.r_driver_add_safe
    r_id_type = general.r_id_type
    # >>>

    # <<< 1mp (utilbl.md
    md = utilbl.md
    copy_md_keyframe = md.copy_md_keyframe
    copy_md_driver = md.copy_md_driver
    link_modifier = md.link_modifier
    deeplink_modifier = md.deeplink_modifier
    r_code_copy_to_selected = md.r_code_copy_to_selected
    ops_mds_copy_to_object = md.ops_mds_copy_to_object
    r_md_driver_add = md.r_md_driver_add
    r_md_keyframe = md.r_md_keyframe
    r_md_driver = md.r_md_driver
    r_md_driver_remove = md.r_md_driver_remove
    S_md_apply_on_spline = md.S_md_apply_on_spline
    S_spline_modifier_types = md.S_spline_modifier_types
    S_md_apply_as_shapekey = md.S_md_apply_as_shapekey
    tr_driver = md.tr_driver
    # >>>

    # <<< 1mp (utilbl.ops
    ops = utilbl.ops
    OpsIDPreview = ops.OpsIDPreview
    # >>>

    # <<< 1mp (utilbl.pymath
    pymath = utilbl.pymath
    calc_py_exp = pymath.calc_py_exp
    # >>>


    ed_undo_push = bpy.ops.ed.undo_push
    BL_RNA_PROP_keymaps = P.keymaps.bl_rna.properties

    _temp = [None]
    SELF = None
    HAS_MD_PIN_TO_LAST = "use_pin_to_last" in bpy.types.Modifier.bl_rna.properties

    globals().update(locals())
    #|
