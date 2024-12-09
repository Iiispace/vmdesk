











import bpy, blf, gpu

blfSize = blf.size
blfColor = blf.color
blfPos = blf.position
blfDraw = blf.draw
blfDimen = blf.dimensions

blend_set = gpu.state.blend_set
scissor_set = gpu.state.scissor_set

PointCache = bpy.types.PointCache
CacheFileLayer = bpy.types.CacheFileLayer

ed_undo_push = bpy.ops.ed.undo_push


from math import ceil

from .  import util, area, block

catch = util.deco.catch
RnaButton = util.types.RnaButton


# <<< 1mp (area
AreaFilterY = area.AreaFilterY
FilterY = area.FilterY
C_filt_evt_head_no_override = area.C_filt_evt_head_no_override
# >>>

# <<< 1mp (block
ButtonFnImgHover = block.ButtonFnImgHover
ButtonEnumXYFlagPython = block.ButtonEnumXYFlagPython
paste_full_data_path_as_driver_safe = block.paste_full_data_path_as_driver_safe
open_driver_editor_from = block.open_driver_editor_from
poll_hard_disable = block.poll_hard_disable
BlockUtil = block.BlockUtil
Title = block.Title
ButtonGroupTitle = block.ButtonGroupTitle
ButtonSep = block.ButtonSep
wrapButtonFn = block.wrapButtonFn
# >>>


class BlockMediaAZ:
    __slots__ = (
        'w',
        'blocklis',
        'items',
        'focus_element',
        'evtkill',
        'box_alphabet',
        'box_invert_order')

    def __init__(self, w, blocklis):
        self.w = w
        self.blocklis = blocklis

        e = ButtonEnumXYFlagPython(self, RNA_sort_order, blocklis.filt, row_length=2)
        e.blf_value[0].text = ""
        e.blf_value[1].text = ""
        e.set_callback = self.set_callback_sort_order
        self.items = [
            e,
            ButtonFnImgHover(self, RNA_new_item, blocklis.evt_add, "GpuImg_ADD"),
            ButtonFnImgHover(self, RNA_remove_item, blocklis.evt_del, "GpuImg_REMOVE"),
        ]
        self.box_alphabet = GpuImg_SORTALPHA()
        self.box_invert_order = GpuImg_invert_y()
        #|

    def init_bat(self, LL, RR, TT):
        widget_rim = SIZE_border[3]
        h = SIZE_widget[0]
        TT -= widget_rim
        LL += SIZE_block[7] + SIZE_button[1] + widget_rim
        items = self.items

        e = items[0]
        e.init_bat(LL, LL + D_SIZE['widget_full_h'] * 2, TT)
        self.box_alphabet.LRBT_upd(*e.box_button[0].inner)
        self.box_invert_order.LRBT_upd(*e.box_button[1].inner)

        LL = RR - h
        items[2].init_bat(LL, RR, TT)
        LL -= h
        RR -= h
        BB = items[1].init_bat(LL, RR, TT)

        return BB - widget_rim
        #|

    def r_height(self, width): return D_SIZE['widget_full_h']

    def is_dark(self):
        return True  if self.items[0].is_dark() else False
        #|
    def dark(self):
        for e in self.items:
            e.dark()
        #|
    def light(self):
        for e in self.items:
            e.light()
        #|

    def inside(self, mouse):
        for e in self.items:
            if e.inside(mouse):
                self.evtkill = False  if hasattr(e, "evtkill") and e.evtkill == False else True
                return True
        return False
        #|
    def inside_evt(self):
        self.focus_element = None
        #|
    def outside_evt(self):
        for e in self.items:
            e.outside_evt()
        #|

    def modal(self):
        e = None
        for o in self.items:
            if o.inside(MOUSE):
                e = o
                break

        if e is None:
            if self.focus_element is not None:
                self.focus_element.outside_evt()
                self.focus_element = None
        else:
            if self.focus_element != e:
                if self.focus_element is not None: self.focus_element.outside_evt()
                self.focus_element = e
                e.inside_evt()

            if e.modal(): return True
        return False
        #|

    def set_callback_sort_order(self):
        # /* 0blocklist_tag_filt_and_update
        self.blocklis.filt.items_unsort = None
        self.blocklis.filt.global_index = "?"
        self.w.upd_data()
        # */

    def dxy(self, dx, dy):
        for e in self.items:
            e.dxy(dx, dy)

        self.box_alphabet.dxy_upd(dx, dy)
        self.box_invert_order.dxy_upd(dx, dy)
        #|
    def draw_box(self):
        for e in self.items:
            e.draw_box()

        self.box_alphabet.bind_draw()
        self.box_invert_order.bind_draw()
        #|
    def draw_blf(self):
        for e in self.items:
            e.draw_blf()
        #|

    def upd_data(self):
        for e in self.items:
            e.upd_data()
        #|
    #|
    #|
class FilterYAZ(FilterY):
    __slots__ = 'mapto_sorted', 'mapto_unsort'

    def init_items(self): # need items_unsort
        name_attr = self.w.name_attr
        if "ALPHABET" in self.sort_order:
            sorted_items = sorted(enumerate(self.items_unsort), key=lambda e: getattr(e[1], name_attr), reverse="INVERT" in self.sort_order)
            self.items = [e  for i, e in sorted_items]
            self.mapto_unsort = [i  for i, e in sorted_items]
            self.mapto_sorted = {i: r  for r, i in enumerate(self.mapto_unsort)}
        else:
            self.items = list(reversed(self.items_unsort))  if "INVERT" in self.sort_order else self.items_unsort

        self.names = {getattr(e, name_attr): r  for r, e in enumerate(self.items)}
        #|

    def r_local_index(self, global_index):
        if global_index in {None, -1}: return None
        if "ALPHABET" in self.sort_order:
            ob = self.items_unsort[global_index]
            for r, e in enumerate(self.match_items):
                if e == ob: return r
        else:
            if self.match_items == self.items:
                return len(self.match_items) - 1 - global_index if "INVERT" in self.sort_order else global_index

            if global_index >= len(self.items_unsort): return None

            ob = self.items_unsort[global_index]
            for r, e in enumerate(self.match_items):
                if e == ob: return r
        return None
        #|

    def set_active_index(self, ind, callback=False):
        if callback is False: pass
        else:
            s = r_library_or_override_message(self.w.r_object())
            if s:
                report(s)
                return

        super().set_active_index(ind, callback)
        #|

    def upd_scissor_filt(self):
        self.w.upd_scissor_filt()
        #|
    #|
    #|
class BlocklistAZ(AreaFilterY):
    __slots__ = (
        'pp',
        'r_pp',
        'r_object',
        'r_datapath_head',
        'dxy',
        'draw_box',
        'r_parent_scissor',
        'r_active_index',
        'set_active_index',
        'remove_active_item',
        'add_item',
        'update_icons',
        'column_len',
        'wind',
        'area',
        'active_index',
        'name_attr',
        'use_index',
        'r_unsort_index')

    CLS_FILTER = FilterYAZ

    def __init__(self, w, r_pp, r_object, r_datapath_head,
                get_icon = None,
                get_info = None,
                remove_active_item = None,
                add_item = None,
                update_icons = None,
                use_ui_active_index = False,
                name_attr = "name",
                use_index = False):

        self.w = w
        self.is_dropdown = False
        self.name_attr = name_attr
        self.use_index = use_index
        self.r_unsort_index = self.r_unsort_index_default

        self.r_pp = r_pp
        self.r_object = r_object
        self.r_datapath_head = r_datapath_head

        self.r_parent_scissor = lambda: self.area.scissor
        if use_ui_active_index:
            self.r_active_index = lambda: self.active_index
            def set_active_index(e):
                self.active_index = e

            self.set_active_index = set_active_index
            self.active_index = None
        else:
            self.r_active_index = lambda: self.pp.active_index
            self.set_active_index = lambda x: setattr(self.pp, "active_index", x)

        self.remove_active_item = remove_active_item
        self.add_item = add_item
        self.update_icons = update_icons
        if hasattr(w, "area"):
            self.wind = w.area.w
            self.area = w.area
        else:
            raise ValueError("TODO")

        self.scissor_text_box = Scissor()
        self.scissor_filt = Scissor()

        self.dxy = self.i_dxy
        self.draw_box = self.i_draw_box
        self.column_len = P.blocklist_column_len

        self.box_area = GpuBox_area()
        self.box_text = GpuRim(COL_box_text, COL_box_text_rim)
        self.box_match_case = GpuImg_filter_match_case()
        self.box_match_whole_word = GpuImg_filter_match_whole_word()
        self.box_match_end = GpuImg_filter_match_end_left()
        self.box_match_end_bg = GpuImg_filter_match_active()
        self.box_match_whole_word_bg = GpuImg_filter_match_active()
        self.box_match_case_bg = GpuImg_filter_match_active()
        self.box_match_hover = GpuImg_filter_match_hover()
        self.box_match_hover.upd()
        self.box_icon_search = GpuImg_search()
        self.box_filter = GpuRim(COL_box_filter, COL_box_filter_rim)
        self.box_selection = GpuBox(COL_box_text_selection)
        self.box_beam = GpuBox(COL_box_cursor_beam)
        blf_text = BlfClip()
        blf_text.color = COL_box_text_fg
        self.blf_text = blf_text

        self.filt = self.CLS_FILTER(self, lambda: tuple(self.r_pp()), get_icon, get_info, is_filter_text_set_index=False)
        self.filt.set_active_index_callback = self.set_active_index_callback
        self.beam_index = [0, 0]
        #|

    def init_bat(self, L, R, T):
        L += SIZE_block[7]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]
        full_h = D_SIZE['widget_full_h']

        LL = L + d0
        RR = R - d0
        TT = T - d0
        B0 = TT - full_h
        box_text = self.box_text
        box_text.LRBT_upd(LL, RR, B0, TT, widget_rim)
        B0 -= d1
        BB = B0 - widget_rim - widget_rim - SIZE_filter[2] - full_h * self.column_len
        self.box_filter.LRBT_upd(LL, RR, BB, B0, widget_rim)

        BB -= d0
        self.box_area.LRBT_upd(L, R, BB, T)

        blf_text = self.blf_text
        L, R, B, T = box_text.inner
        L0 = box_text.L + widget_rim * 3
        L1 = L0 + SIZE_widget[0]

        self.box_icon_search.LRBT_upd(L0, L1, B, T)
        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L1 + D_SIZE['font_main_dx']
        blf_text.y = B + D_SIZE['font_main_dy']

        self.filt.upd_size()
        self.filt.filter_text(blf_text.unclip_text)
        self.upd_scissor_filt()
        self.upd_clip_text_and_match_button(blf_text)
        self.upd_scissor_text_box()
        return BB
        #|

    def set_active_index_callback(self, **kw): # object
        pp = self.r_pp()
        l = list(self.filt.items_unsort)
        try:
            i = l.index(kw["object"])
        except ValueError:
            return

        self.set_active_index(i)
        update_scene_push(f"Cache index = {i}")
        #|
    def upd_scissor_text_box(self):
        self.scissor_text_box.intersect_with(self.r_parent_scissor(), self.box_icon_search.R + D_SIZE['font_main_dy'],
            self.box_match_case.L - D_SIZE['font_main_dy'], self.box_text.B, self.box_text.T)
        #|
    def upd_scissor_filt(self):
        e = self.box_filter.inner
        self.scissor_filt.intersect_with(self.r_parent_scissor(),
            e[0], e[1] - min(SIZE_widget[2], SIZE_widget[0]), e[2], e[3])
        #|

    def r_height(self, width):
        return SIZE_dd_border[0] + SIZE_dd_border[1] + SIZE_border[3] + SIZE_filter[2] + D_SIZE['widget_full_h'] * (self.column_len + 1)
        #|

    def is_dark(self): return False
    def dark(self): pass
    def light(self): pass

    def inside(self, mouse): return self.box_area.inbox(mouse)
    # def inside_evt(self): pass
    def outside_evt(self):
        Admin.TAG_CURSOR = 'DEFAULT'
        super().outside_evt()
        #|
    def outside_evt_filt(self):
        Admin.TAG_CURSOR = 'DEFAULT'
        super().outside_evt_filt()
        #|

    def localmodal_filt_submodal(self):
        if TRIGGER['rm']():
            self.to_modal_filt_rm()
            return True
        if TRIGGER['rename']():
            self.evt_area_rename()
            return True
        #|

    def localmodal_filt(self, dic):
        if P.lock_list_size is False:
            if self.box_filter.B <= MOUSE[1] <= self.box_filter.inner[2]:
                Admin.TAG_CURSOR = 'MOVE_Y'
                if TRIGGER['resize']():
                    self.to_modal_filt_resize()
                    return True
            else:
                Admin.TAG_CURSOR = 'DEFAULT'

        return super().localmodal_filt(dic)
        #|

    def to_modal_filt_resize(self):

        _end_trigger = r_end_trigger('resize')
        Admin.REDRAW()

        def end_modal_filt_resize():
            Admin.REDRAW()
            kill_evt_except()

            self.column_len = max(1, round(max(1, _box_rim.T - _box_rim.B) / SIZE_widget[0]) - 1)
            self.area.redraw_from_headkey()
            self.filt.r_upd_scroll()()
            #|
        def i_modal_filt_resize():
            Admin.REDRAW()

            if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']() or _end_trigger():
                w_head.fin()
                return

            _box_rim.B = MOUSE[1]
            _box_rim.upd()
            #|

        _box_rim = self.box_filter

        w_head = Head(self, i_modal_filt_resize, end_modal_filt_resize)
        #|
    @ catch
    def to_modal_filt_rm(self):

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

        override_name = {}
        items = [
            ("rename", lambda: self.evt_area_rename((i, T))),
            ("Sort Alphabetically Toggle", self.evt_toggle_az),
            ("Reverse Order Toggle", self.evt_toggle_order),
            ("Resize", self.to_modal_filt_resize),

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

            ("area_del", lambda: self.evt_del((self.r_active_index(), T))),
            ("Delete Current", lambda: self.evt_del((i, T))),
            ("area_add", self.evt_add),
            ("area_active_down_most", self.evt_active_down_most),
            ("area_active_up_most", self.evt_active_up_most),
            ("area_active_down", self.evt_active_down),
            ("area_active_up", self.evt_active_up),
            ("pan", self.filt.to_modal_pan),
            ("area_select", lambda: self.evt_area_select(i, extend=False)),
        ]
        override_name["area_del"] = "Delete Active"
        DropDownRMKeymap(self, MOUSE, items, title="Point Cache", override_name=override_name)
        #|
    @ catch
    def evt_area_rename(self, override=None):

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

        active_item = filt.match_items[i]
        if isinstance(active_item, CacheFileLayer):
            def end_fn(s):
                try:
                    layers = self.r_pp()
                    if any(layer.filepath == s  for layer in layers):
                        report("Layer path already exists", ty="WARNING")
                        return
                    active_item.filepath = s
                    update_scene_push("Cache layer rename")
                except Exception as ex:
                    report(str(ex), ty="WARNING")

            OpScanFile.end_fn = end_fn
            bpy.ops.wm.vmd_scan_file("INVOKE_DEFAULT", filepath="", filter_glob="*.abc")
            return

        L, R, B, _ = self.box_filter.r_LRBT()
        T += - SIZE_border[3] + (filt.headkey - i) * D_SIZE['widget_full_h']
        DropDownEnumRename(None, (L, R, T - SIZE_widget[0], T), self.r_object(), active_item, items=tuple(self.r_pp()))
        #|
    @ catch
    def evt_del(self, override=None):

        if self.remove_active_item is None: return
        s = r_library_or_override_message(self.r_object())
        if s:
            report(s)
            return
        if override is None:
            i = self.r_active_index()
        else:
            filt = self.filt
            i, T = override

        active_index = self.r_active_index()
        if active_index != i:
            self.set_active_index(i)

        self.remove_active_item()
        update_scene_push("Remove list item")
        #|
    @ catch
    def evt_add(self, override=None):

        if self.add_item is None: return
        s = r_library_or_override_message(self.r_object())
        if s:
            report(s)
            return

        self.add_item()
        update_scene_push("Add list item")
        #|

    def evt_toggle_az(self, override=None, override_value=None):

        sort_order = self.filt.sort_order
        if "ALPHABET" in sort_order:
            sort_order.remove("ALPHABET")
        else:
            sort_order.add("ALPHABET")

        # <<< 1copy (0blocklist_tag_filt_and_update,, ${'self.blocklis':'self'}$)
        self.filt.items_unsort = None
        self.filt.global_index = "?"
        self.w.upd_data()
        # >>>
        #|
    def evt_toggle_order(self, override=None, override_value=None):

        sort_order = self.filt.sort_order
        if "INVERT" in sort_order:
            sort_order.remove("INVERT")
        else:
            sort_order.add("INVERT")

        # <<< 1copy (0blocklist_tag_filt_and_update,, ${'self.blocklis':'self'}$)
        self.filt.items_unsort = None
        self.filt.global_index = "?"
        self.w.upd_data()
        # >>>
        #|

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
                filt.selnames[old_act] = getattr(filt.match_items[old_act], self.name_attr)

            filt.set_active_index(i, callback=True)
        #|

    def r_unsort_index_default(self, it):
        for index, e in enumerate(self.filt.items_unsort):
            if e == it: return index
        return -1
        #|

    def i_dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)
        self.box_text.dxy_upd(dx, dy)
        self.box_icon_search.dxy_upd(dx, dy)
        self.box_filter.dxy_upd(dx, dy)
        self.box_selection.dxy_upd(dx, dy)
        self.box_beam.dxy_upd(dx, dy)
        self.box_match_end_bg.dxy_upd(dx, dy)
        self.box_match_whole_word_bg.dxy_upd(dx, dy)
        self.box_match_case_bg.dxy_upd(dx, dy)
        self.box_match_hover.dxy_upd(dx, dy)
        self.box_match_end.dxy_upd(dx, dy)
        self.box_match_whole_word.dxy_upd(dx, dy)
        self.box_match_case.dxy_upd(dx, dy)

        self.blf_text.x += dx
        self.blf_text.y += dy

        self.filt.dxy(dx, dy)
        self.upd_scissor_filt()
        self.upd_scissor_text_box()
        #|

    def i_draw_box(self):
        self.box_area.bind_draw()
        self.box_text.bind_draw()
        self.box_icon_search.bind_draw()
        self.box_filter.bind_draw()
        self.box_match_end_bg.bind_draw()
        self.box_match_whole_word_bg.bind_draw()
        self.box_match_case_bg.bind_draw()
        self.box_match_hover.bind_draw()
        self.box_match_end.bind_draw()
        self.box_match_whole_word.bind_draw()
        self.box_match_case.bind_draw()

        filt = self.filt
        filt.box_scroll_bg.bind_draw()
        filt.box_scroll.bind_draw()

        self.scissor_text_box.use()
        self.box_selection.bind_draw()
        self.box_beam.bind_draw()
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

        self.r_parent_scissor().use()
        blend_set('ALPHA')
        #|
    def draw_blf(self): pass

    def upd_data_super(self):
        filt = self.filt
        new_items = filt.get_items()

        if TAG_RENAME[0] is True:

            pass
        elif new_items != filt.items_unsort: pass
        else:
            its = filt.match_items
            name_attr = self.name_attr
            if all(e.text == getattr(its[r], name_attr)  for r, e in filt.blfs.items()) is True:
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
            name_attr = self.name_attr
            selnames = filt.selnames
            le = len(new_items)
            for r, name in old_selnames.items():
                if r < le: selnames[r] = getattr(new_items[r], name_attr)
        #|
    def upd_data(self):
        pp = self.r_pp()
        self.pp = pp
        if pp is None: return

        self.upd_data_super()
        i = self.r_active_index()
        self.filt.upd_active_index(None  if i in {None, -1} else i)

        if self.update_icons is None: return
        self.update_icons(self.filt)
        #|
    #|
    #|

class FilterYAZEnabled(FilterYAZ):
    __slots__ = 'icons_button', 'box_hover_button'

    def rr_anim_state_eye(self):
        ob = self.w.r_object()
        r_enabled_datapath = self.w.r_enabled_datapath
        if hasattr(ob, "animation_data"):
            anim_data = ob.animation_data
            if hasattr(anim_data, "action") and hasattr(anim_data.action, "fcurves") and anim_data.action.fcurves:
                if hasattr(anim_data, "drivers") and anim_data.drivers:
                    fcurves = anim_data.action.fcurves
                    drivers = anim_data.drivers

                    if self.w.use_index is False:
                        def r_anim_state(e0):
                            dp = r_enabled_datapath(e0)
                            if fcurves.find(dp): return 1
                            if drivers.find(dp): return 2
                            return 0
                    else:
                        items_lookup = {e: r  for r, e in enumerate(self.items_unsort)}
                        def r_anim_state(e0):
                            dp = r_enabled_datapath(items_lookup[e0])
                            if fcurves.find(dp): return 1
                            if drivers.find(dp): return 2
                            return 0
                else:
                    fcurves = anim_data.action.fcurves

                    if self.w.use_index is False:
                        def r_anim_state(e0):
                            dp = r_enabled_datapath(e0)
                            if fcurves.find(dp): return 1
                            return 0
                    else:
                        items_lookup = {e: r  for r, e in enumerate(self.items_unsort)}
                        def r_anim_state(e0):
                            dp = r_enabled_datapath(items_lookup[e0])
                            if fcurves.find(dp): return 1
                            return 0
            else:
                if hasattr(anim_data, "drivers") and anim_data.drivers:
                    drivers = anim_data.drivers

                    if self.w.use_index is False:
                        def r_anim_state(e0):
                            dp = r_enabled_datapath(e0)
                            if drivers.find(dp): return 2
                            return 0
                    else:
                        items_lookup = {e: r  for r, e in enumerate(self.items_unsort)}
                        def r_anim_state(e0):
                            dp = r_enabled_datapath(items_lookup[e0])
                            if drivers.find(dp): return 2
                            return 0
                else:
                    def r_anim_state(e0):
                        return 0
        else:
            def r_anim_state(e0):
                return 0

        return r_anim_state
        #|

    def upd_size(self):
        # ref_FilterY_upd_size
        name_attr = self.w.name_attr
        match_items = self.match_items
        box_filter = self.w.box_filter
        widget_rim = SIZE_border[3]
        icons = self.icons
        icons_button = self.icons_button
        blfs = self.blfs
        blfs_info = self.blfs_info
        icons.clear()
        icons_button.clear()
        blfs.clear()
        blfs_info.clear()
        len_match_items = len(match_items)

        R = box_filter.R - widget_rim
        scroll_width = min(SIZE_widget[2], SIZE_widget[0])
        self.box_scroll_bg.LRBT_upd(R - scroll_width, R, box_filter.B + widget_rim, box_filter.T - widget_rim)
        self.box_hover.LRBT_upd(0, 0, 0, 0)

        old_act = self.active_index
        # <<< 1copy (0blocklist_FilterYAZ_get_blfs,, $$)
        self.headkey = 0
        full_h = D_SIZE['widget_full_h']
        T = box_filter.T - widget_rim
        x = box_filter.L + widget_rim + SIZE_filter[1] + widget_rim + D_SIZE['font_main_dy']
        y = T - SIZE_filter[2] - widget_rim - D_SIZE['font_main_dT']
        range_end = min(len_match_items, ceil((T - box_filter.B - widget_rim) / full_h) + 1)
        self.endkey = range_end - 1
        get_info = self.get_info
        _GpuImgSlotEye = GpuImgSlotEye
        r_anim_state = self.rr_anim_state_eye()

        h = SIZE_widget[0]
        L_icon_button = self.w.box_region.inner[0] + D_SIZE['font_main_dy']
        R_icon_button = L_icon_button + h
        r_enabled = self.w.r_enabled

        if self.get_icon is None:
            B = y - D_SIZE['font_main_dy']
            T = B + h
            if get_info is None:
                for r in range(range_end):
                    o = match_items[r]
                    e = BlfColor(getattr(o, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                    ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                    icons_button[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h
            else:
                blfSize(FONT0, D_SIZE['font_main'])
                xx = x + full_h
                for r in range(range_end):
                    o = match_items[r]
                    e = BlfColor(getattr(o, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    blfs_info[r] = Blf(get_info(o), xx + round(blfDimen(FONT0, e.text)[0]))
                    ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                    ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                    icons_button[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h
        else:
            x += h
            R = x - D_SIZE['font_main_dy']
            L = R - h
            B = y - D_SIZE['font_main_dy']
            T = B + h
            geticon = self.get_icon

            if get_info is None:
                for r in range(range_end):
                    it = match_items[r]
                    e = BlfColor(getattr(it, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    ee = geticon(it)
                    if hasattr(ee, "max_index"): e.x += ee.max_index * h
                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    ee = _GpuImgSlotEye(r_enabled(it), r_anim_state(it))
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
                    e = BlfColor(getattr(it, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    e_info = Blf(get_info(it), xx + round(blfDimen(FONT0, e.text)[0]))
                    blfs_info[r] = e_info
                    ee = geticon(it)
                    if hasattr(ee, "max_index"):
                        x_offset = ee.max_index * h
                        e.x += x_offset
                        e_info.x += x_offset

                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    ee = _GpuImgSlotEye(r_enabled(it), r_anim_state(it))
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
    def filter_text(self, s, active_index=0, callback=False):
        # ref_FilterY_filter_text
        name_attr = self.w.name_attr
        if s:
            fx = self.filter_function
            self.match_items = [e for e in self.items if fx(getattr(e, name_attr), s)]
        else:
            self.match_items = self.items
        match_items = self.match_items
        # print('-------------------------')
        # for e in self.match_items: print(e.name)
        # print('-------------------------')

        box_filter = self.w.box_filter
        widget_rim = SIZE_border[3]
        icons = self.icons
        icons_button = self.icons_button
        blfs = self.blfs
        blfs_info = self.blfs_info
        icons.clear()
        icons_button.clear()
        blfs.clear()
        blfs_info.clear()
        len_match_items = len(match_items)

        # /* 0blocklist_FilterYAZ_get_blfs
        self.headkey = 0
        full_h = D_SIZE['widget_full_h']
        T = box_filter.T - widget_rim
        x = box_filter.L + widget_rim + SIZE_filter[1] + widget_rim + D_SIZE['font_main_dy']
        y = T - SIZE_filter[2] - widget_rim - D_SIZE['font_main_dT']
        range_end = min(len_match_items, ceil((T - box_filter.B - widget_rim) / full_h) + 1)
        self.endkey = range_end - 1
        get_info = self.get_info
        _GpuImgSlotEye = GpuImgSlotEye
        r_anim_state = self.rr_anim_state_eye()

        h = SIZE_widget[0]
        L_icon_button = self.w.box_region.inner[0] + D_SIZE['font_main_dy']
        R_icon_button = L_icon_button + h
        r_enabled = self.w.r_enabled

        if self.get_icon is None:
            B = y - D_SIZE['font_main_dy']
            T = B + h
            if get_info is None:
                for r in range(range_end):
                    o = match_items[r]
                    e = BlfColor(getattr(o, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                    ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                    icons_button[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h
            else:
                blfSize(FONT0, D_SIZE['font_main'])
                xx = x + full_h
                for r in range(range_end):
                    o = match_items[r]
                    e = BlfColor(getattr(o, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    blfs_info[r] = Blf(get_info(o), xx + round(blfDimen(FONT0, e.text)[0]))
                    ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                    ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                    icons_button[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h
        else:
            x += h
            R = x - D_SIZE['font_main_dy']
            L = R - h
            B = y - D_SIZE['font_main_dy']
            T = B + h
            geticon = self.get_icon

            if get_info is None:
                for r in range(range_end):
                    it = match_items[r]
                    e = BlfColor(getattr(it, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    ee = geticon(it)
                    if hasattr(ee, "max_index"): e.x += ee.max_index * h
                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    ee = _GpuImgSlotEye(r_enabled(it), r_anim_state(it))
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
                    e = BlfColor(getattr(it, name_attr), x, y, COL_box_filter_fg)
                    blfs[r] = e
                    e_info = Blf(get_info(it), xx + round(blfDimen(FONT0, e.text)[0]))
                    blfs_info[r] = e_info
                    ee = geticon(it)
                    if hasattr(ee, "max_index"):
                        x_offset = ee.max_index * h
                        e.x += x_offset
                        e_info.x += x_offset

                    ee.LRBT_upd(L, R, B, T)
                    icons[r] = ee
                    ee = _GpuImgSlotEye(r_enabled(it), r_anim_state(it))
                    ee.LRBT_upd(L_icon_button, R_icon_button, B, T)
                    icons_button[r] = ee
                    y -= full_h
                    T -= full_h
                    B -= full_h

        self.r_upd_scroll()()
        # */
        if self.is_filter_text_set_index is True:
            self.set_active_index(active_index, callback)
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

        self.box_active.dxy_upd(dx, dy)
        self.box_hover.dxy_upd(dx, dy)
        #|

    def to_modal_pan(self):

        #|
        if self.blfs: pass
        else: return

        end_trigger = r_end_trigger('pan')
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop()
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        # <<< 1copy (0defpanEyeGet,, $$)
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

        _GpuImgSlotEye = GpuImgSlotEye
        r_anim_state = self.rr_anim_state_eye()
        r_enabled = self.w.r_enabled
        L_icon_button = self.w.box_region.inner[0] + D_SIZE['font_main_dy']
        R_icon_button = L_icon_button + _h
        _li_icon_button = self.icons_button
        name_attr = self.w.name_attr
        # >>>

        if _geticon is None:
            if _getinfo is None:
                def modal_pan():
                    _REDRAW()
                    if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                        w_head.fin()
                        return
                    dx, dy = r_dxy_mouse()

                    # <<< 1copy (0defpanEyeModalNoIconNoInfo,, $$)
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
                                        _li[headkey] = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon_button[endkey]
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
                                        _li[endkey] = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon_button[headkey]
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
                    for e in _li_icon_button.values(): e.dxy_upd(0, dy)

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

                    # <<< 1copy (0defpanEyeModalNoIcon,, $$)
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        _li_info[headkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_info[endkey]
                                        del _li_icon_button[endkey]
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        _li_info[endkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_info[headkey]
                                        del _li_icon_button[headkey]
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
                    for e in _li_icon_button.values(): e.dxy_upd(0, dy)

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

                    # <<< 1copy (0defpanEyeModalNoInfo,, $$)
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[headkey] = ee
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        del _li_icon_button[endkey]
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[endkey] = ee
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        del _li_icon_button[headkey]
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

                    # <<< 1copy (0defpanEyeModal,, $$)
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
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
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        del _li_info[endkey]
                                        del _li_icon_button[endkey]
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
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
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        del _li_info[headkey]
                                        del _li_icon_button[headkey]
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

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    mouseloop()

        def end_modal_pan():
            _REDRAW()
            mouseloop_end()
            kill_evt_except()

        self.box_hover.LRBT_upd(0, 0, 0, 0)
        self.box_hover_button.LRBT_upd(0, 0, 0, 0)
        w_head = Head(self, modal_pan, end_modal_pan)
        _REDRAW()
        #|
    def r_pan_override(self):
        # <<< 1copy (0defpanEyeGet,, $$)
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

        _GpuImgSlotEye = GpuImgSlotEye
        r_anim_state = self.rr_anim_state_eye()
        r_enabled = self.w.r_enabled
        L_icon_button = self.w.box_region.inner[0] + D_SIZE['font_main_dy']
        R_icon_button = L_icon_button + _h
        _li_icon_button = self.icons_button
        name_attr = self.w.name_attr
        # >>>

        if _geticon is None:
            if _getinfo is None:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanEyeModalNoIconNoInfo,, $$)
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
                                        _li[headkey] = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon_button[endkey]
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
                                        _li[endkey] = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon_button[headkey]
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
                    for e in _li_icon_button.values(): e.dxy_upd(0, dy)

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy
            else:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanEyeModalNoIcon,, $$)
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        _li_info[headkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_info[endkey]
                                        del _li_icon_button[endkey]
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        _li_info[endkey] = _Blf(_getinfo(o), xx + round(_blfDimen(_FONT0, e.text)[0]))
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_info[headkey]
                                        del _li_icon_button[headkey]
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
                    for e in _li_icon_button.values(): e.dxy_upd(0, dy)

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy
        else:
            if _getinfo is None:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanEyeModalNoInfo,, $$)
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[headkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[headkey] = ee
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        del _li_icon_button[endkey]
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
                                        _li[endkey] = e
                                        ee = _geticon(o)
                                        if hasattr(ee, "max_index"): e.x += ee.max_index * _h
                                        ee.LRBT_upd(L, R, y + _icon_dB, y + _icon_dT)
                                        _li_icon[endkey] = ee
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        del _li_icon_button[headkey]
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

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy
            else:
                def pan_override(dx, dy):
                    # <<< 1copy (0defpanEyeModal,, $$)
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
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
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[headkey] = ee
                                        T += _full_h
                                        del _li[endkey]
                                        del _li_icon[endkey]
                                        del _li_info[endkey]
                                        del _li_icon_button[endkey]
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
                                        e = _BlfColor(getattr(o, name_attr), x, y, _COL_box_filter_fg)
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
                                        ee = _GpuImgSlotEye(r_enabled(o), r_anim_state(o))
                                        ee.LRBT_upd(L_icon_button, R_icon_button, y + _icon_dB, y + _icon_dT)
                                        _li_icon_button[endkey] = ee
                                        B -= _full_h
                                        del _li[headkey]
                                        del _li_icon[headkey]
                                        del _li_info[headkey]
                                        del _li_icon_button[headkey]
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

                    _upd_scroll()
                    _box_active_dy_upd(dy)
                    # >>>
                    return dx, dy

        return pan_override
        #|
    #|
    #|
class BlocklistAZEnabled(BlocklistAZ):
    __slots__ = 'r_enabled', 'r_enabled_datapath', 'r_datapath_head', 'box_region', 'set_enabled'

    CLS_FILTER = FilterYAZEnabled

    def __init__(self, w, r_pp, r_object, r_datapath_head,
                get_icon = None,
                get_info = None,
                remove_active_item = None,
                add_item = None,
                update_icons = None,
                r_enabled = None,
                r_enabled_datapath = None,
                set_enabled = None,
                use_ui_active_index = False,
                name_attr = "name",
                use_index = False):

        self.box_region = GpuRim(COL_box_filter_region, COL_box_filter_region_rim)

        super().__init__(w, r_pp, r_object, r_datapath_head,
            get_icon = get_icon,
            get_info = get_info,
            remove_active_item = remove_active_item,
            add_item = add_item,
            update_icons = update_icons,
            use_ui_active_index = use_ui_active_index,
            name_attr = name_attr,
            use_index = use_index)

        self.r_enabled = r_enabled
        self.r_enabled_datapath = r_enabled_datapath
        self.set_enabled = set_enabled
        filt = self.filt
        filt.icons_button = {}
        filt.box_hover_button = GpuImg_MD_BG_SHOW_HOVER()
        filt.box_hover_button.set_draw_state(False)
        #|

    def init_bat(self, L, R, T):
        L += SIZE_block[7]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_rim = SIZE_border[3]
        full_h = D_SIZE['widget_full_h']

        LL = L + d0
        RR = R - d0
        TT = T - d0
        B0 = TT - full_h
        box_text = self.box_text
        box_text.LRBT_upd(LL, RR, B0, TT, widget_rim)
        B0 -= d1
        BB = B0 - widget_rim - widget_rim - SIZE_filter[2] - full_h * self.column_len
        self.box_filter.LRBT_upd(LL, RR, BB, B0, widget_rim)

        BB -= d0
        self.box_area.LRBT_upd(L, R, BB, T)

        blf_text = self.blf_text
        L, R, B, T = box_text.inner
        L0 = box_text.L + widget_rim * 3
        L1 = L0 + SIZE_widget[0]

        self.box_icon_search.LRBT_upd(L0, L1, B, T)
        self.box_selection.LRBT_upd(0, 0, B, T)
        self.box_beam.LRBT_upd(0, 0, B, T)

        blf_text.x = L1 + D_SIZE['font_main_dx']
        blf_text.y = B + D_SIZE['font_main_dy']

        LL, RR, BB, TT = self.box_filter.inner
        RR -= min(SIZE_widget[2], SIZE_widget[0])
        LL = RR - self.calc_region_width()
        self.box_region.LRBT_upd(LL, RR, BB, TT, SIZE_border[3])

        self.filt.upd_size()
        self.filt.filter_text(blf_text.unclip_text)
        self.upd_scissor_filt()
        self.upd_clip_text_and_match_button(blf_text)
        self.upd_scissor_text_box()
        return BB
        #|
    def calc_region_width(self):
        return D_SIZE['widget_full_h'] + D_SIZE['font_main_dy'] * 2
        #|

    def upd_scissor_filt(self):
        e = self.box_filter.inner
        self.scissor_filt.intersect_with(self.r_parent_scissor(),
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
            if buts.slot0.L <= x < buts.slot0.R: return "eye"
        return "null"
        #|

    def filt_region_event(self, B, T, i, filt):
        hover = filt.box_hover_button

        if i is None:
            if hover.L == 0 and hover.R == 0: pass
            else:
                hover.LRBT_upd(0, 0, 0, 0)
                Admin.REDRAW()
            return False

        if MOUSE[0] >= self.box_region.L:
            buts = filt.icons_button[i]

            if hover.L == buts.L and hover.R == buts.R and hover.B == buts.B and hover.T == buts.T: pass
            else:
                hover.LRBT_upd(buts.L, buts.R, buts.B, buts.T)
                Admin.REDRAW()

            if TRIGGER['click']():
                self.to_modal_filt_eye(i)
                return True
        else:
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
        #|

    @ catch
    def to_modal_filt_rm(self):

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

        region_index = self.r_region_index(MOUSE[0], i)
        override_name = {}

        items = [
            ("rename", lambda: self.evt_area_rename((i, T))),
            ("Sort Alphabetically Toggle", self.evt_toggle_az),
            ("Reverse Order Toggle", self.evt_toggle_order),
            ("Resize", self.to_modal_filt_resize),

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

            ("area_del", lambda: self.evt_del((self.r_active_index(), T))),
            ("Delete Current", lambda: self.evt_del((i, T))),
            ("area_add", self.evt_add),
            ("area_active_down_most", self.evt_active_down_most),
            ("area_active_up_most", self.evt_active_up_most),
            ("area_active_down", self.evt_active_down),
            ("area_active_up", self.evt_active_up),
            ("pan", self.filt.to_modal_pan),
            ("area_select", lambda: self.evt_area_select(i, extend=False)),
        ]
        override_name["area_del"] = "Delete Active"
        DropDownRMKeymap(self, MOUSE, items, title="Point Cache", override_name=override_name)
        #|
    def to_modal_filt_eye(self, filt_ind):

        ob = self.r_object()
        if ob == None: return

        lib_message = r_library_or_override_message(ob)
        if lib_message:
            report(lib_message)
            return
        override_message = r_unsupport_override_message(ob)
        if override_message:
            report(override_message)
            return

        filt = self.filt
        blfs = filt.blfs
        if not blfs: return
        match_items = filt.match_items
        if not match_items: return
        end_trigger = r_end_trigger('click')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']

        r_enabled = self.r_enabled
        set_enabled = self.set_enabled
        r_anim_state = filt.rr_anim_state_eye()
        boo = False  if r_enabled(match_items[filt_ind]) else True

        mou = MOUSE
        pan_override = filt.r_pan_override()
        sci_win = self.r_parent_scissor()
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
        R0 = e.slot1.R
        LL = max(LL, L0)
        RR = min(RR, R0)
        le = len(match_items)
        anim_data = ob.animation_data  if hasattr(ob, "animation_data") else None
        push_modal = m.ADMIN.push_modal

        def localmodal():
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            x, y = mou
            T = blfs[filt.headkey].y + font_main_dT_rim
            i = (T - y) // full_h + filt.headkey

            if LL <= x < RR and i in icons_button:
                if 0 <= i < le:
                    e = match_items[i]
                    if r_enabled(e) == boo: pass
                    else:
                        _REDRAW()
                        set_enabled(e, boo)
                        icons_button[i].update_slot(r_enabled(e), r_anim_state(e))

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
            Admin.REDRAW()
            update_data()
            ed_undo_push(message="Item enabled toggle")
            #|

        filt.box_hover_button.LRBT_upd(0, 0, 0, 0)
        filt.box_hover.LRBT_upd(0, 0, 0, 0)
        Admin.REDRAW()
        w_head = Head(self, localmodal, localmodalend)
        localmodal()
        #|

    def evt_remove_from_keying_set(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        if region_index == "eye":
            if self.use_index is False:
                dp = self.r_enabled_datapath(self.filt.match_items[i])
            else:
                dp = self.r_enabled_datapath(self.r_unsort_index(self.filt.match_items[i]))

            success, s = r_remove_from_keying_set(ob, dp)
            if s:
                DropDownOk(None, MOUSE, input_text=s)
        #|
    def evt_add_to_keying_set(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        if region_index == "eye":
            if self.use_index is False:
                dp = self.r_enabled_datapath(self.filt.match_items[i])
            else:
                dp = self.r_enabled_datapath(self.r_unsort_index(self.filt.match_items[i]))

            success, s = r_add_to_keying_set(ob, dp)
            if s:
                DropDownOk(None, MOUSE, input_text=s)
        #|
    def evt_copy_full_data_path(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        if self.use_index is False:
            if region_index == "eye":
                dp = f'{r_ID_dp(ob)}.{self.r_enabled_datapath(self.filt.match_items[i])}'
            else:
                dp = f'{r_ID_dp(ob)}.{self.r_datapath_head(self.filt.match_items[i])}.{self.name_attr}'
        else:
            index = self.r_unsort_index(self.filt.match_items[i])
            if region_index == "eye":
                dp = f'{r_ID_dp(ob)}.{self.r_enabled_datapath(index)}'
            else:
                dp = f'{r_ID_dp(ob)}.{self.r_datapath_head(index)}.{self.name_attr}'

        bpy.context.window_manager.clipboard = dp
        report("Full Data Path is copied to the clipboard")
        #|
    def evt_copy_data_path(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        if self.use_index is False:
            if region_index == "eye":
                dp = self.r_enabled_datapath(self.filt.match_items[i])
            else:
                dp = f'{self.r_datapath_head(self.filt.match_items[i])}.{self.name_attr}'
        else:
            index = self.r_unsort_index(self.filt.match_items[i])
            if region_index == "eye":
                dp = self.r_enabled_datapath(index)
            else:
                dp = f'{self.r_datapath_head(index)}.{self.name_attr}'

        bpy.context.window_manager.clipboard = dp
        report("Data Path is copied to the clipboard")
        #|
    def evt_paste_full_data_path_as_driver(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        if region_index == "eye":
            pp = self.filt.match_items[i]
            if self.use_index is False:
                dp = self.r_enabled_datapath(pp)
            else:
                dp = self.r_enabled_datapath(self.r_unsort_index(pp))
            attr = dp[dp.rfind(".") + 1 : ]

            success, ex = paste_full_data_path_as_driver_safe(
                bpy.context.window_manager.clipboard,
                r_driver_fc(ob, dp),
                dp,
                ob,
                pp.bl_rna.properties[attr],
                pp)

            if success is False: DropDownOk(None, MOUSE, input_text=f'Failed to add Driver.\n{ex}')
        #|
    def evt_delete_driver(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        if region_index == "eye":
            pp = self.filt.match_items[i]
            if self.use_index is False:
                dp = self.r_enabled_datapath(pp)
            else:
                dp = self.r_enabled_datapath(self.r_unsort_index(pp))
            attr = dp[dp.rfind(".") + 1 : ]
            dr = r_driver_fc(ob, dp)
            if dr:
                ob.animation_data.drivers.remove(dr)
            else:
                report("Driver not found")
                return

            update_scene_push("Delete Driver")
        #|
    def evt_add_driver(self, override=None, use_editor=False):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        try:
            if region_index == "eye":
                pp = self.filt.match_items[i]
                if self.use_index is False:
                    dp = self.r_enabled_datapath(pp)
                else:
                    dp = self.r_enabled_datapath(self.r_unsort_index(pp))
                i0 = dp.rfind(".")
                attr = dp[i0 + 1 : ]
                dphead = dp[ : i0]
                fc = r_action_fc(ob, dp)
                if fc:
                    report("Unable to add driver when keyframe already exists")
                    return

                dr = r_driver_fc(ob, dp)
                if dr:
                    if use_editor:
                        open_driver_editor_from(ob, dp)
                else:
                    if r_driver_add_safe(ob, dphead, attr):
                        update_scene_push("Add Driver")
                        if use_editor and P.is_open_driver_editor:
                            open_driver_editor_from(ob, dp)
                    else:
                        report("Not allow add driver to current property")
        except Exception as ex:

            report("Failure")
        #|
    def evt_clear_keyframe(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        try:
            if region_index == "eye":
                pp = self.filt.match_items[i]
                if self.use_index is False:
                    dp = self.r_enabled_datapath(pp)
                else:
                    dp = self.r_enabled_datapath(self.r_unsort_index(pp))

                fcs = ob.animation_data.action.fcurves
                fcs.remove(fcs.find(dp))

                update_scene_push("Clear Keyframe")
        except:
            report("Keyframe not found")
        #|
    def evt_delete_keyframe(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        try:
            if region_index == "eye":
                pp = self.filt.match_items[i]
                if self.use_index is False:
                    dp = self.r_enabled_datapath(pp)
                else:
                    dp = self.r_enabled_datapath(self.r_unsort_index(pp))
                attr = dp[dp.rfind(".") + 1 : ]
                pp.keyframe_delete(attr)

                update_scene_push("Delete Keyframe")
        except:
            report("Keyframe not found")
        #|
    def evt_insert_keyframe(self, override=None):

        i, region_index, ob = C_filt_evt_head_no_override(self, self.r_object(), override, poll_library=True, evtkill=True)
        if i is None: return

        try:
            if region_index == "eye":
                pp = self.filt.match_items[i]
                if self.use_index is False:
                    dp = self.r_enabled_datapath(pp)
                else:
                    dp = self.r_enabled_datapath(self.r_unsort_index(pp))
                attr = dp[dp.rfind(".") + 1 : ]
                dr = r_driver_fc(ob, dp)
                if dr:
                    report("Unable to Insert Keyframe when Driver already exists")
                    return

                pp.keyframe_insert(attr)

                update_scene_push("Insert Keyframe")
        except:
            report("Keyframe not found")
        #|

    def i_dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)
        self.box_text.dxy_upd(dx, dy)
        self.box_icon_search.dxy_upd(dx, dy)
        self.box_filter.dxy_upd(dx, dy)
        self.box_selection.dxy_upd(dx, dy)
        self.box_beam.dxy_upd(dx, dy)
        self.box_match_end_bg.dxy_upd(dx, dy)
        self.box_match_whole_word_bg.dxy_upd(dx, dy)
        self.box_match_case_bg.dxy_upd(dx, dy)
        self.box_match_hover.dxy_upd(dx, dy)
        self.box_match_end.dxy_upd(dx, dy)
        self.box_match_whole_word.dxy_upd(dx, dy)
        self.box_match_case.dxy_upd(dx, dy)
        self.box_region.dxy_upd(dx, dy)

        self.blf_text.x += dx
        self.blf_text.y += dy

        self.filt.dxy(dx, dy)
        self.upd_scissor_filt()
        self.upd_scissor_text_box()
        #|

    def i_draw_box(self):
        self.box_area.bind_draw()
        self.box_text.bind_draw()
        self.box_icon_search.bind_draw()
        self.box_filter.bind_draw()
        self.box_match_end_bg.bind_draw()
        self.box_match_whole_word_bg.bind_draw()
        self.box_match_case_bg.bind_draw()
        self.box_match_hover.bind_draw()
        self.box_match_end.bind_draw()
        self.box_match_whole_word.bind_draw()
        self.box_match_case.bind_draw()

        filt = self.filt
        self.box_region.bind_draw()

        filt.box_scroll_bg.bind_draw()
        filt.box_scroll.bind_draw()

        scissor_filt = self.scissor_filt
        w_scissor = self.r_parent_scissor()
        scissor_set(w_scissor.x, scissor_filt.y, w_scissor.w, scissor_filt.h)
        filt.box_hover_button.bind_draw()
        for e in filt.icons_button.values(): e.bind_draw()

        self.scissor_text_box.use()
        self.box_selection.bind_draw()
        self.box_beam.bind_draw()
        e = self.blf_text
        blfSize(FONT0, D_SIZE['font_main'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)

        scissor_filt.use()
        blend_set('ALPHA')
        filt.box_active.bind_draw()
        filt.box_hover.bind_draw()
        blfs = filt.blfs
        for e in filt.icons.values(): e.bind_draw()
        for e in blfs.values():
            blfColor(FONT0, *e.color)
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)

        w_scissor.use()
        blend_set('ALPHA')
        #|

    def upd_data(self):
        pp = self.r_pp()
        self.pp = pp
        if pp is None: return

        self.upd_data_super()
        i = self.r_active_index()
        filt = self.filt
        filt.upd_active_index(None  if i in {None, -1} else i)

        if self.update_icons is None: pass
        else:
            self.update_icons(filt)

        r_enabled = self.r_enabled
        r_anim_state = filt.rr_anim_state_eye()
        match_items = filt.match_items
        for r, e in filt.icons_button.items():
            o = match_items[r]
            e.update_slot(r_enabled(o), r_anim_state(o))
        #|
    #|
    #|


def ui_point_cache(cachetype, ui, r_point_cache, r_dph, r_object):
    b0 = ui.new_block(title="Cache")
    uianim_cache = b0.set_pp(r_point_cache, PointCache, r_dph)
    props = b0.props

    def remove_active_point_cache():
        if not bpy.data.is_saved:
            report("Cache is disabled until the file is saved")
            return

        ob = r_object()
        def bufn():
            with bpy.context.temp_override(object=ob, point_cache=r_point_cache()):
                bpy.ops.ptcache.remove()

        wrapButtonFn(bufn, ob, evtkill=False)
    def add_point_cache():
        if not bpy.data.is_saved:
            report("Cache is disabled until the file is saved")
            return

        ob = r_object()
        def bufn():
            with bpy.context.temp_override(object=ob, point_cache=r_point_cache()):
                bpy.ops.ptcache.add()

        wrapButtonFn(bufn, ob, evtkill=False)
    def ptcache_bake():
        # <<< 1copy (0blocklist_ptcache_bake,, $$)
        def bufn():
            OpClothBake.init_data = {
                "object": r_object(),
                "point_cache": r_point_cache(),
                "operation": "BAKE",
            }
            bpy.ops.wm.vmd_cloth_bake()

        wrapButtonFn(bufn, update=False)
        # >>>
    def ptcache_calc():
        # <<< 1copy (0blocklist_ptcache_bake,, ${'BAKE':'CALC'}$)
        def bufn():
            OpClothBake.init_data = {
                "object": r_object(),
                "point_cache": r_point_cache(),
                "operation": "CALC",
            }
            bpy.ops.wm.vmd_cloth_bake()

        wrapButtonFn(bufn, update=False)
        # >>>
    def ptcache_bake_delete_all():
        # <<< 1copy (0blocklist_ptcache_bake,, ${'BAKE':'DEL_ALL'}$)
        def bufn():
            OpClothBake.init_data = {
                "object": r_object(),
                "point_cache": r_point_cache(),
                "operation": "DEL_ALL",
            }
            bpy.ops.wm.vmd_cloth_bake()

        wrapButtonFn(bufn, update=False)
        # >>>
    def ptcache_bake_from():
        # <<< 1copy (0blocklist_ptcache_bake,, ${'BAKE':'FROM'}$)
        def bufn():
            OpClothBake.init_data = {
                "object": r_object(),
                "point_cache": r_point_cache(),
                "operation": "FROM",
            }
            bpy.ops.wm.vmd_cloth_bake()

        wrapButtonFn(bufn, update=False)
        # >>>
    def ptcache_bake_all_dynamics():
        # <<< 1copy (0blocklist_ptcache_bake,, ${'BAKE':'BAKE_ALL'}$)
        def bufn():
            OpClothBake.init_data = {
                "object": r_object(),
                "point_cache": r_point_cache(),
                "operation": "BAKE_ALL",
            }
            bpy.ops.wm.vmd_cloth_bake()

        wrapButtonFn(bufn, update=False)
        # >>>
    def ptcache_bake_all_to_frame():
        # <<< 1copy (0blocklist_ptcache_bake,, ${'BAKE':'FRAME'}$)
        def bufn():
            OpClothBake.init_data = {
                "object": r_object(),
                "point_cache": r_point_cache(),
                "operation": "FRAME",
            }
            bpy.ops.wm.vmd_cloth_bake()

        wrapButtonFn(bufn, update=False)
        # >>>

    if cachetype == 'RIGID_BODY':
        blocklis_caches = None
        media_caches = None
    else:
        block0 = b0.w
        blocklis_caches = BlocklistAZ(block0,
            r_pp = lambda: r_point_cache().point_caches,
            r_object = r_object,
            r_datapath_head = lambda i: f'{r_dph()}.point_caches[{i}]',
            get_icon = lambda e: GpuImg_PHYSICS(),
            remove_active_item = remove_active_point_cache,
            add_item = add_point_cache,
            use_index = True)

        media_caches = BlockMediaAZ(block0, blocklis_caches)

        block0.items += [
            blocklis_caches,
            media_caches,
            ButtonSep(2),
        ]

        if cachetype in {'PSYS', 'HAIR'}:
            b0.prop("use_external")
            b0.sep(2)

    b0.prop("index", text="Index")
    b0.prop("filepath", text="Path")
    b0.prop("frame_start", text="Simulation Start")
    props["frame_start"].set_callback = update_scene
    b0.prop("frame_end")
    props["frame_end"].set_callback = update_scene

    has_frame_step = cachetype not in {'CLOTH', 'DYNAMIC_PAINT', 'RIGID_BODY'}
    if has_frame_step is True:
        b0.prop("frame_step")

    b0.sep(1)
    label0 = b0.label([""] * 2)
    label0_blf0 = label0.blf_label[0]
    label0_blf1 = label0.blf_label[1]
    b0.sep(1)

    b0.prop("use_disk_cache", isdarkhard=True)
    b0.prop("use_library_path", text="Use Library Path", isdarkhard=True)
    b0.prop("compression", text="Compression", isdarkhard=True)
    label1 = b0.label([""])
    label1_blf0 = label1.blf_label[0]
    func0 = b0.function(
        [RNA_ptcache_bake, RNA_ptcache_bake_all_dynamics],
        [ptcache_bake, ptcache_bake_all_dynamics], isdarkhard=True)
    func1 = b0.function(
        [RNA_ptcache_calc, RNA_ptcache_bake_delete_all],
        [ptcache_calc, ptcache_bake_delete_all], isdarkhard=True)
    func2 = b0.function(
        [RNA_ptcache_bake_from, RNA_ptcache_bake_all_to_frame],
        [ptcache_bake_from, ptcache_bake_all_to_frame], isdarkhard=True)

    ui_state = []
    cachetype_in_DYNAMIC_PAINT_RIGID_BODY = cachetype in {'DYNAMIC_PAINT', 'RIGID_BODY'}

    def fn_darklight_cache(cache):
        if cachetype_in_DYNAMIC_PAINT_RIGID_BODY: can_bake = True
        else:
            if cache.id_data.library and not cache.use_disk_cache:
                can_bake = False
            else:
                can_bake = True

        if ui_state == [uianim_cache.library_state, cache.use_external, bpy.data.is_saved, cache.is_baked, (cache.id_data.override_library is None), cache.use_disk_cache, can_bake]: return
        ui_state[:] = [uianim_cache.library_state, cache.use_external, bpy.data.is_saved, cache.is_baked, (cache.id_data.override_library is None), cache.use_disk_cache, can_bake]


        label0_blf0.text = cache.info
        label0_blf1.text = ""

        if uianim_cache.library_state in {1, -1}:
            func0.dark(0)
            func1.dark(0)
            func2.dark(0)

            if cache.use_external:
                label1_blf0.text = ""
            else:
                label1_blf0.text = "Linked object baking requires Disk Cache to be enabled"
                is_saved = bpy.data.is_saved

                if cachetype == 'DYNAMIC_PAINT' and not is_saved:
                    label0_blf1.text = "Cache is disabled until the file is saved"

                if cachetype_in_DYNAMIC_PAINT_RIGID_BODY: pass
                else:
                    if is_saved: pass
                    else:
                        label0_blf1.text = "Options are disabled until the file is saved"

                if cache.is_baked is True:
                    func0.set_button_text("Delete Bake", 0)
                else:
                    func0.set_button_text("Bake", 0)
            return

        if cache.use_external:
            props["index"].dark()
            props["filepath"].dark()
            props["frame_start"].dark()
            props["frame_end"].dark()
            props["use_disk_cache"].dark()
            props["use_library_path"].dark()
            props["compression"].dark()
            func0.dark()
            func1.dark()
            func2.dark()
            if has_frame_step is True:
                props["frame_step"].dark()
        else:
            func0.light()
            func1.light()
            func2.light()

            is_saved = bpy.data.is_saved
            is_liboverride = cache.id_data.override_library is not None

            if cachetype == 'DYNAMIC_PAINT' and not is_saved:
                props["index"].dark()
                props["filepath"].dark()
                props["frame_start"].dark()
                props["frame_end"].dark()
                props["use_disk_cache"].dark()
                props["use_library_path"].dark()
                props["compression"].dark()
                func0.dark()
                func1.dark()
                func2.dark()
                if has_frame_step is True:
                    props["frame_step"].dark()

                label0_blf1.text = "Cache is disabled until the file is saved"
            else:
                props["index"].dark()
                props["filepath"].dark()
                props["frame_start"].light()
                props["frame_end"].light()
                props["use_disk_cache"].light()
                props["use_library_path"].light()
                props["compression"].light()
                if has_frame_step is True:
                    props["frame_step"].light()

            enabled = cache.is_baked is False

            if cachetype in {'PSYS', 'DYNAMIC_PAINT'}:
                props["frame_start"].dark()
                props["frame_end"].dark()
            else:
                if enabled:
                    props["frame_start"].light()
                    props["frame_end"].light()
                else:
                    props["frame_start"].dark()
                    props["frame_end"].dark()

            if has_frame_step is True:
                if enabled:
                    props["frame_step"].light()
                else:
                    props["frame_step"].dark()

            if cachetype_in_DYNAMIC_PAINT_RIGID_BODY:
                label1_blf0.text = ""

                props["use_library_path"].dark()
                props["compression"].dark()
                props["use_disk_cache"].dark()
            else:
                if is_saved: pass
                else:
                    label0_blf1.text = "Options are disabled until the file is saved"

                flow_enabled = enabled and is_saved
                if flow_enabled:
                    props["use_disk_cache"].light()
                else:
                    props["use_disk_cache"].dark()

                if flow_enabled and cache.use_disk_cache:
                    props["use_library_path"].light()
                    props["compression"].light()
                else:
                    props["use_library_path"].dark()
                    props["compression"].dark()

                if not can_bake:
                    label1_blf0.text = "Linked object baking requires Disk Cache to be enabled"
                else:
                    label1_blf0.text = ""

            # 6Buttons
            if is_liboverride and not cache.use_disk_cache:
                func0.set_button_text("Bake (Disk mandatory)", 0)
                func0.dark(0)
                func1.dark(0)
                func2.dark(0)
            elif cache.is_baked is True:
                func0.set_button_text("Delete Bake", 0)
            else:
                func0.set_button_text("Bake", 0)

            if not can_bake:
                func0.dark(0)

            if not enabled:
                func1.dark(0)
                func2.dark(0)
        #|

    return uianim_cache, fn_darklight_cache, blocklis_caches, media_caches, [func0, func1, func2]
    #|

RNA_ptcache_bake = RnaButton("ptcache_bake",
    name = "Bake",
    button_text = "Bake",
    description = "Bake physics")
RNA_ptcache_calc = RnaButton("ptcache_calc",
    name = "Calculate to Frame",
    button_text = "Calculate to Frame",
    description = "Bake physics")
RNA_ptcache_bake_delete_all = RnaButton("ptcache_bake_delete_all",
    name = "Delete All Bakes",
    button_text = "Delete All Bakes",
    description = "Delete all baked caches of all objects in the current scene")
RNA_ptcache_bake_from = RnaButton("ptcache_bake_from",
    name = "Current Cache to Bake",
    button_text = "Current Cache to Bake",
    description = "Bake from cache")
RNA_ptcache_bake_all_dynamics = RnaButton("ptcache_bake_all_dynamics",
    name = "Bake All Dynamics",
    button_text = "Bake All Dynamics",
    description = "Bake all physics")
RNA_ptcache_bake_all_to_frame = RnaButton("ptcache_bake_all_to_frame",
    name = "Update All to Frame",
    button_text = "Update All to Frame",
    description = "Bake all physics")


## _file_ ##
def late_import():
    #|
    from .  import VMD

    m = VMD.m

    # <<< 1mp (m
    P = m.P
    Admin = m.Admin
    r_mouseloop = m.r_mouseloop
    update_data = m.update_data
    TAG_RENAME = m.TAG_RENAME
    # >>>

    # <<< 1mp (VMD.dd
    dd = VMD.dd
    DropDownEnumRename = dd.DropDownEnumRename
    DropDownRMKeymap = dd.DropDownRMKeymap
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    kill_evt_except = keysys.kill_evt_except
    MOUSE = keysys.MOUSE
    EVT_TYPE = keysys.EVT_TYPE
    TRIGGER = keysys.TRIGGER
    r_end_trigger = keysys.r_end_trigger
    # >>>

    # <<< 1mp (VMD.rna
    rna = VMD.rna
    RNA_remove_item = rna.RNA_remove_item
    RNA_new_item = rna.RNA_new_item
    RNA_sort_order = rna.RNA_sort_order
    # >>>

    # <<< 1mp (VMD.win
    win = VMD.win
    Head = win.Head
    # >>>

    utilbl = VMD.utilbl

    # <<< 1mp (utilbl
    blg = utilbl.blg
    # >>>

    # <<< 1mp (blg
    Blf = blg.Blf
    BlfClip = blg.BlfClip
    BlfColor = blg.BlfColor
    D_SIZE = blg.D_SIZE
    FONT0 = blg.FONT0
    Scissor = blg.Scissor
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_filter = blg.SIZE_filter
    SIZE_block = blg.SIZE_block
    SIZE_widget = blg.SIZE_widget
    SIZE_button = blg.SIZE_button
    GpuBox_area = blg.GpuBox_area
    GpuBox = blg.GpuBox
    GpuRim = blg.GpuRim
    GpuImg_filter_match_case = blg.GpuImg_filter_match_case
    GpuImg_filter_match_whole_word = blg.GpuImg_filter_match_whole_word
    GpuImg_filter_match_end_left = blg.GpuImg_filter_match_end_left
    GpuImg_filter_match_active = blg.GpuImg_filter_match_active
    GpuImg_filter_match_hover = blg.GpuImg_filter_match_hover
    GpuImg_search = blg.GpuImg_search
    GpuImg_SORTALPHA = blg.GpuImg_SORTALPHA
    GpuImg_invert_y = blg.GpuImg_invert_y
    GpuImg_MD_BG_SHOW_HOVER = blg.GpuImg_MD_BG_SHOW_HOVER
    GpuImgSlotEye = blg.GpuImgSlotEye
    GpuImg_PHYSICS = blg.GpuImg_PHYSICS
    COL_box_text = blg.COL_box_text
    COL_box_text_rim = blg.COL_box_text_rim
    COL_box_filter = blg.COL_box_filter
    COL_box_filter_rim = blg.COL_box_filter_rim
    COL_box_text_selection = blg.COL_box_text_selection
    COL_box_cursor_beam = blg.COL_box_cursor_beam
    COL_box_filter_region = blg.COL_box_filter_region
    COL_box_filter_region_rim = blg.COL_box_filter_region_rim
    COL_box_text_fg = blg.COL_box_text_fg
    COL_box_filter_fg = blg.COL_box_filter_fg
    COL_block_fg_info = blg.COL_block_fg_info
    report = blg.report
    # >>>

    # <<< 1mp (utilbl.general
    general = utilbl.general
    update_scene = general.update_scene
    update_scene_push = general.update_scene_push
    r_library_or_override_message = general.r_library_or_override_message
    r_unsupport_override_message = general.r_unsupport_override_message
    r_remove_from_keying_set = general.r_remove_from_keying_set
    r_add_to_keying_set = general.r_add_to_keying_set
    r_ID_dp = general.r_ID_dp
    r_obj_path_by_full_path = general.r_obj_path_by_full_path
    r_driver_fc = general.r_driver_fc
    r_action_fc = general.r_action_fc
    r_driver_add_safe = general.r_driver_add_safe
    # >>>

    # <<< 1mp (utilbl.ops
    ops = utilbl.ops
    OpClothBake = ops.OpClothBake
    OpScanFile = ops.OpScanFile
    # >>>

    globals().update(locals())
    #|
