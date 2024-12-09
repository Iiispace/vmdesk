











def check_open_from_dd():
    for e in W_DRAW.copy():
        clsname = e.__class__.__name__
        if clsname.startswith("DropDown") or clsname.startswith("DD"):
            bring_draw_to_top_safe(e)
    #|

class StructGlobalUndo:
    __slots__ = ()

    def evt_redo(self):
        kill_evt_except()
        try:
            ed_redo()
            Admin.REDRAW()
            update_data()
        except:
            report('Currently in last step / Redo failed')
    def evt_undo(self):
        kill_evt_except()
        try:
            ed_undo()
            Admin.REDRAW()
            update_data()
        except:
            report('Currently in first step / Undo failed')
    #|
    #|


#|  require
#|      ADMIN
#|      upd_size_areas
#|  kw need
#|      id_class
#|      use_pos
#|      use_fit
#|      pos_offset
#|
class Window:
    __slots__ = (
        'w',
        'u_modal',
        'u_draw',
        'cls_ind',
        'boxes',
        'blfs',
        'box_rim',
        'box_win',
        'box_title_button',
        'box_hover',
        'scissor',
        'areas',
        'upd_size_state',
        'P_editor')

    INIT_DATA = None

    def __init__(self, **kw):

        Window.INIT_DATA = kw

        self.upd_size_state = True
        self.u_draw = self.i_draw
        self.u_modal = self.i_modal
        self.w = kw["w"]  if "w" in kw else None

        if "event" in kw:
            evt = kw["event"]
        else:
            evt = Admin.EVT
            kw["event"] = evt
        prefEditor = getattr(P, kw["id_class"], None)
        self.P_editor = prefEditor

        title_B = - SIZE_title[0]
        h3 = - title_B * 3
        rim_d = SIZE_border[2]
        editor_name = self.name
        cls_ind = r_smallest_miss({e.cls_ind  for e in W_PROCESS  if e.name == editor_name}, 1)
        self.cls_ind = cls_ind
        if cls_ind != 1:
            editor_name += f" {cls_ind}"

        if prefEditor == None:
            kw["use_pos"] = True
            kw["use_fit"] = True

        if kw["use_fit"]:
            R = h3 - title_B
            B = title_B - R
        else:
            R = max(prefEditor.size[0], h3 - title_B)
            B = title_B - prefEditor.size[1]

        box_win = GpuWin(0, R, B, 0, title_B)
        box_rim = GpuWinRim(-rim_d, R + rim_d, B - rim_d, rim_d, rim_d)
        box_title_button = GpuImg_title_button(R - h3, R, title_B, 0)
        box_hover = GpuBox(FLO_0000)
        box_shadow = GpuShadow(
            SIZE_win_shadow_offset[0],
            R + SIZE_win_shadow_offset[1],
            B + SIZE_win_shadow_offset[2],
            SIZE_win_shadow_offset[3],
            SIZE_shadow_softness[0])

        title_y = title_B + D_SIZE['font_title_dy']
        title_x = D_SIZE['font_title_dx']
        # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
        blfSize(FONT0, D_SIZE['font_title'])
        blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
        # >>>
        blf_title = BlfClip(r_blf_clipping_end(editor_name, title_x, box_title_button.L - title_x
            ), editor_name, title_x, title_y)

        boxes = [
            # /* 2win_boxes $dict$
            box_shadow,
            box_rim,
            box_win,
            box_hover,
            box_title_button
            # */
        ]
        blfs = [
            # /* 2win_blfs $dict$
            blf_title,
            # */
        ]
        self.boxes = boxes
        self.blfs = blfs
        self.box_rim = box_rim
        self.box_win = box_win
        self.box_title_button = box_title_button
        self.box_hover = box_hover

        if kw["use_pos"]:
            offset = kw["pos_offset"]
            x = evt.mouse_region_x + offset[0]
            y = evt.mouse_region_y + offset[1]
        else:
            x = prefEditor.pos[0]
            y = prefEditor.pos[1]

        #| check overlap
        if P.win_check_overlap:
            overlap_offset_x, overlap_offset_y = P.win_overlap_offset

            x = r_best_new_int_miss(
                {e.box_win.L  for e in W_MODAL  if hasattr(e, "box_win")},
                x, overlap_offset_x, REGION_DATA.L + 1, REGION_DATA.R)
            y = r_best_new_int_miss(
                {e.box_win.T  for e in W_MODAL  if hasattr(e, "box_win")},
                y, overlap_offset_y, REGION_DATA.B + 1, REGION_DATA.T)
        #|

        if "preserve_size" in kw:
            preserve_size = kw["preserve_size"]
            if x + preserve_size[0] > REGION_DATA.R:
                x = REGION_DATA.R - preserve_size[0]
            if y - preserve_size[1] < REGION_DATA.B + SIZE_tb[0]:
                y = REGION_DATA.B + SIZE_tb[0] + preserve_size[1]

        dx, dy = r_full_protect_dxy(box_rim.L + x, box_rim.R + x, box_rim.B + y, box_rim.T + y)
        x += dx
        y += dy

        for e in boxes: e.dxy_upd(x, y)
        for e in blfs:
            e.x += x
            e.y += y

        self.scissor = Scissor()
        self.scissor.LRBT(box_win.L, box_win.R, box_win.B, box_win.title_B)
        self.init(boxes, blfs)

        #| change temp prefs in N-panel
        prefs_callback_disable()
        P_temp.pos = x, y
        P_temp.size = R, title_B - B
        P_temp.canvas = 0, 0
        prefs_callback_enable()
        #|

        m.ADMIN.reg(self)

        Admin.REDRAW()
        Admin.TAG_CURSOR = 'DEFAULT'
        kill_evt()
        if kw["use_fit"]: self.evt_fit()
        self.resize_upd_end()

        check_open_from_dd()
        #|

    def upd_size(self):
        #| call from Npanel
        #| already prefs_callback_disable()
        if self.upd_size_state == True:
            box_win = self.box_win
            pos = box_win.L, box_win.T

            # <<< 1dict (2win_blfs,, $
            # blf_title = self.blfs[|blf_title|]$)
            blf_title = self.blfs[0]
            # >>>
            title_B = - SIZE_title[0]
            h3 = - title_B * 3
            rim_d = SIZE_border[2]
            R = box_win.R - box_win.L
            B = box_win.B - box_win.T

            box_win.LRBT(0, R, B, 0, title_B)
            self.scissor.LRBT(0, R, B, title_B)
            self.box_rim.LRBT(-rim_d, R + rim_d, B - rim_d, rim_d, rim_d)
            self.box_title_button.LRBT(R - h3, R, title_B, 0)
            self.box_hover.color = FLO_0000
            # <<< 1dict (2win_boxes,, $
            # self.boxes[|box_shadow|].LRBT(
            #     SIZE_win_shadow_offset[0],
            #     R + SIZE_win_shadow_offset[1],
            #     B + SIZE_win_shadow_offset[2],
            #     SIZE_win_shadow_offset[3],
            #     SIZE_shadow_softness[0])$)
            self.boxes[0].LRBT(                SIZE_win_shadow_offset[0],                R + SIZE_win_shadow_offset[1],                B + SIZE_win_shadow_offset[2],                SIZE_win_shadow_offset[3],                SIZE_shadow_softness[0])
            # >>>

            title_y = title_B + D_SIZE['font_title_dy']
            title_x = D_SIZE['font_title_dx']
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            blf_title.x = title_x
            blf_title.y = title_y
            blf_title.text = r_blf_clipping_end(blf_title.unclip_text, title_x, self.box_title_button.L - title_x)

            dx = pos[0]
            dy = pos[1]
            # <<< 1copy (0win_Window_dxy_without_areas,, $$)
            self.scissor.dxy(dx, dy)
            for e in self.boxes: e.dxy_upd(dx, dy)

            for e in self.blfs:
                e.x += dx
                e.y += dy
            # >>>
            self.upd_size_areas()
        elif self.upd_size_state == None: self.upd_size_state = False
        #|

    def fin(self, killevt=None):

        if hasattr(self, "fin_callfront"): self.fin_callfront()
        Admin.REDRAW()
        m.ADMIN.unreg(self)
        if killevt == None: kill_evt_except()
        elif killevt: kill_evt()

        if P.sys_auto_off and not W_PROCESS: m.ADMIN.to_modal_fin()
        #|

    def modal(self):
        if self.box_rim.inbox(MOUSE):
            if Admin.IS_INSIDE == False:
                m.ADMIN.inside_evt()
                if hasattr(self, "sys_inside_evt"): self.sys_inside_evt()

            # <<< 1copy (0defwin_TRIGGER_bring_to_front,, $$)
            if TRIGGER['click']():
                if W_MODAL[-1] != self:

                    bring_to_front(self)
            # >>>

            if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']():
                self.fin()
                return True

            if TRIGGER['pan_win']():
                self.to_modal_pan_win()
                return True

            inner = self.box_rim.inner
            inner = inner[0] + 2, inner[1] - 2, inner[2] + 2, inner[3] - 2
            if inner[0] < MOUSE[0] < inner[1] and inner[2] < MOUSE[1] < inner[3]: pass
            elif P.lock_win_size: pass
            else:
                self.to_modal_resize()
                return True

            if MOUSE[1] >= self.box_win.title_B:
                self.to_modal_title()
                return True
            else:
                self.u_modal()
            return True

        return False
        #|
    def i_modal(self):
        for e in self.areas:
            if e.box_area.inbox(MOUSE):
                e.modal()
                return

        if hasattr(self, "evt_search"):
            if TRIGGER['area_search']():
                self.evt_search()
                return
        if hasattr(self, "evt_undo"):
            if TRIGGER['redo']():
                self.evt_redo()
                return
            if TRIGGER['undo']():
                self.evt_undo()
                return
        #|

    def win_inbox(self, MOUSE):
        if self.box_rim.inbox(MOUSE):
            if MOUSE[1] >= self.box_win.title_B: return False
            return True
        return False
        #|

    def basis_win_evt(self): # use for head modal
        if self.box_rim.inbox(MOUSE):
            # <<< 1copy (0defwin_TRIGGER_bring_to_front,, $$)
            if TRIGGER['click']():
                if W_MODAL[-1] != self:

                    bring_to_front(self)
            # >>>

            if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc'](): return self.evt_basis_fin

            inner = self.box_rim.inner
            inner = inner[0] + 2, inner[1] - 2, inner[2] + 2, inner[3] - 2
            if inner[0] < MOUSE[0] < inner[1] and inner[2] < MOUSE[1] < inner[3]: pass
            elif P.lock_win_size: pass
            else: return self.to_modal_resize

            if TRIGGER['pan_win'](): return self.to_modal_pan_win
            if hasattr(self, "evt_undo"):
                if TRIGGER['redo'](): return self.evt_redo
                if TRIGGER['undo'](): return self.evt_undo
        return None
        #|
    def evt_basis_fin(self):

        for e in reversed(W_HEAD): e.fin()
        self.fin()
        #|
    def is_inbox_other_win(self):
        x, y = MOUSE
        rd = REGION_DATA
        if x < rd.L or x > rd.R or y < rd.B or y > rd.T: return True
        if rd.L + SIZE_tb[1] < x and y < rd.B + SIZE_tb[0]: return True

        for e in reversed(W_MODAL):
            if e == self: return False
            if e.box_rim.inbox(MOUSE): return True
        return False
        #|

    def to_modal_resize(self):

        #|
        inner = self.box_rim.inner
        inner = inner[0] + 2, inner[1] - 2, inner[2] + 2, inner[3] - 2
        if inner[0] < MOUSE[0] < inner[1]:
            Admin.TAG_CURSOR = 'MOVE_Y'
            if MOUSE[1] > (inner[3] + inner[2]) // 2:
                pass
            else:
                pass
        elif MOUSE[0] > (inner[1] + inner[0]) // 2:
            if inner[2] < MOUSE[1] < inner[3]:
                Admin.TAG_CURSOR = 'MOVE_X'
            elif MOUSE[1] > (inner[3] + inner[2]) // 2:
                Admin.TAG_CURSOR = 'SCROLL_XY'
            else:
                Admin.TAG_CURSOR = 'SCROLL_XY'
        else:
            if inner[2] < MOUSE[1] < inner[3]:
                Admin.TAG_CURSOR = 'MOVE_X'
            elif MOUSE[1] > (inner[3] + inner[2]) // 2:
                Admin.TAG_CURSOR = 'SCROLL_XY'
            else:
                Admin.TAG_CURSOR = 'SCROLL_XY'

        def end_modal_resize_pre():
            Admin.TAG_CURSOR = 'DEFAULT'

        def modal_resize_pre():
            evt = Admin.EVT
            # <<< 1copy (0m_check_hud,, ${
            #     'CONTEXT_AREA': 'm.CONTEXT_AREA',
            #     'return "FORCE_PASS_THROUGH"': 'w_head.fin() ;return "FORCE_PASS_THROUGH"'
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(m.CONTEXT_AREA)
                if hud_region is None: Admin.IS_HUD = False
                else:
                    hud_L = hud_region.x
                    hud_B = hud_region.y
                    if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                        if Admin.IS_INSIDE is False: w_head.fin() ;return "FORCE_PASS_THROUGH"
                        # <<< 1copy (0m_outside_evt,, $$)

                        Admin.IS_INSIDE = False
                        bpy.context.window.cursor_modal_restore()
                        if W_FOCUS[0] != None:
                            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                            W_FOCUS[0] = None
                        kill_evt()
                        # >>>

                        w_head.fin() ;return "FORCE_PASS_THROUGH"
            # >>>

            inner = self.box_rim.inner
            inner = inner[0] + 2, inner[1] - 2, inner[2] + 2, inner[3] - 2
            if self.box_rim.inbox(MOUSE):
                # <<< 1copy (0defwin_TRIGGER_bring_to_front,, $$)
                if TRIGGER['click']():
                    if W_MODAL[-1] != self:

                        bring_to_front(self)
                # >>>

                if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']():
                    w_head.fin()
                    self.fin()
                    return

                if inner[0] < MOUSE[0] < inner[1] and inner[2] < MOUSE[1] < inner[3]:
                    w_head.fin()
                    return

                if inner[0] < MOUSE[0] < inner[1]:
                    Admin.TAG_CURSOR = 'MOVE_Y'
                    if MOUSE[1] > (inner[3] + inner[2]) // 2:
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_T()
                            return
                    else:
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_B()
                            return
                elif MOUSE[0] > (inner[1] + inner[0]) // 2:
                    if inner[2] < MOUSE[1] < inner[3]:
                        Admin.TAG_CURSOR = 'MOVE_X'
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_R()
                            return
                    elif MOUSE[1] > (inner[3] + inner[2]) // 2:
                        Admin.TAG_CURSOR = 'SCROLL_XY'
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_TR()
                            return
                    else:
                        Admin.TAG_CURSOR = 'SCROLL_XY'
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_BR()
                            return
                else:
                    if inner[2] < MOUSE[1] < inner[3]:
                        Admin.TAG_CURSOR = 'MOVE_X'
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_L()
                            return
                    elif MOUSE[1] > (inner[3] + inner[2]) // 2:
                        Admin.TAG_CURSOR = 'SCROLL_XY'
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_TL()
                            return
                    else:
                        Admin.TAG_CURSOR = 'SCROLL_XY'
                        if TRIGGER['resize']():
                            self.to_modal_resize_click_BL()
                            return
            else:
                w_head.fin()

        w_head = Head(self, modal_resize_pre, end_modal_resize_pre)
        #|
    def end_modal_resize_click(self):
        self.resize_upd_end()

        box_win = self.box_win
        #| change temp prefs in N-panel
        prefs_callback_disable()
        P_temp.pos = box_win.L, box_win.T
        P_temp.size = box_win.R - box_win.L, box_win.title_B - box_win.B
        prefs_callback_enable()
        #|
        kill_evt_except()
        #|
    def to_modal_resize_click_B(self): # ref: m.upd_win_active

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd

        _lim_B = REGION_DATA.B + SIZE_tb[0]

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dy = MOUSE[1] - _xy[1]
            if _scissor.h - dy < 0: dy = _scissor.h
            else:
                if _box_win.B + dy < _lim_B: dy = _lim_B - _box_win.B
            _scissor.y += dy
            _scissor.h -= dy
            _box_win.B += dy
            _box_rim.B += dy
            _box_shadow.B += dy

            _dxy(0, 0)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def to_modal_resize_click_T(self):

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd

        _lim_T = REGION_DATA.T

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dy = _xy[1] - MOUSE[1]
            if _scissor.h - dy < 0: dy = _scissor.h
            else:
                if _box_win.T - dy > _lim_T: dy = _box_win.T - _lim_T
            _scissor.y += dy
            _scissor.h -= dy
            _box_win.B += dy
            _box_rim.B += dy
            _box_shadow.B += dy

            _dxy(0, -dy)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def to_modal_resize_click_R(self): # ref: m.upd_win_active

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd
        _box_title_button = self.box_title_button
        _box_title_button_dx = _box_title_button.dx
        # <<< 1dict (2win_blfs,, $
        # _blf_title = self.blfs[|blf_title|]$)
        _blf_title = self.blfs[0]
        # >>>
        _blf_title_unclip_text = _blf_title.unclip_text
        _r_blf_clipping_end = r_blf_clipping_end
        _font_title_dx = D_SIZE['font_title_dx']
        _SIZE_title0 = SIZE_title[0]

        _lim_R = REGION_DATA.R

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dx = MOUSE[0] - _xy[0]
            if _scissor.w + dx < 4 * _SIZE_title0: dx = 4 * _SIZE_title0 - _scissor.w
            else:
                if _box_win.R + dx > _lim_R: dx = _lim_R - _box_win.R
            _scissor.w += dx
            _box_win.R += dx
            _box_rim.R += dx
            _box_shadow.R += dx
            _box_title_button_dx(dx)
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            _blf_title.text = _r_blf_clipping_end(_blf_title_unclip_text, _blf_title.x,
                _box_title_button.L - _font_title_dx)

            _dxy(0, 0)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def to_modal_resize_click_L(self):

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd
        _box_title_button = self.box_title_button
        _box_title_button_dx = _box_title_button.dx
        # <<< 1dict (2win_blfs,, $
        # _blf_title = self.blfs[|blf_title|]$)
        _blf_title = self.blfs[0]
        # >>>
        _blf_title_unclip_text = _blf_title.unclip_text
        _r_blf_clipping_end = r_blf_clipping_end
        _font_title_dx = D_SIZE['font_title_dx']
        _SIZE_title0 = SIZE_title[0]

        _lim_L = REGION_DATA.L

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dx = _xy[0] - MOUSE[0]
            if _scissor.w + dx < 4 * _SIZE_title0: dx = 4 * _SIZE_title0 - _scissor.w
            else:
                if _box_win.L - dx < _lim_L: dx = _box_win.L - _lim_L
            _scissor.w += dx
            _box_win.R += dx
            _box_rim.R += dx
            _box_shadow.R += dx
            _box_title_button_dx(dx)
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            _blf_title.text = _r_blf_clipping_end(_blf_title.unclip_text, _blf_title.x,
                _box_title_button.L - _font_title_dx)

            _dxy(-dx, 0)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def to_modal_resize_click_BR(self):

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd
        _box_title_button = self.box_title_button
        _box_title_button_dx = _box_title_button.dx
        # <<< 1dict (2win_blfs,, $
        # _blf_title = self.blfs[|blf_title|]$)
        _blf_title = self.blfs[0]
        # >>>
        _blf_title_unclip_text = _blf_title.unclip_text
        _r_blf_clipping_end = r_blf_clipping_end
        _font_title_dx = D_SIZE['font_title_dx']
        _SIZE_title0 = SIZE_title[0]

        _lim_R = REGION_DATA.R
        _lim_B = REGION_DATA.B + SIZE_tb[0]

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dy = MOUSE[1] - _xy[1]
            if _scissor.h - dy < 0: dy = _scissor.h
            else:
                if _box_win.B + dy < _lim_B: dy = _lim_B - _box_win.B
            _scissor.y += dy
            _scissor.h -= dy
            _box_win.B += dy
            _box_rim.B += dy
            _box_shadow.B += dy

            dx = MOUSE[0] - _xy[0]
            if _scissor.w + dx < 4 * _SIZE_title0: dx = 4 * _SIZE_title0 - _scissor.w
            else:
                if _box_win.R + dx > _lim_R: dx = _lim_R - _box_win.R
            _scissor.w += dx
            _box_win.R += dx
            _box_rim.R += dx
            _box_shadow.R += dx
            _box_title_button_dx(dx)
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            _blf_title.text = _r_blf_clipping_end(_blf_title_unclip_text, _blf_title.x,
                _box_title_button.L - _font_title_dx)

            _dxy(0, 0)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def to_modal_resize_click_BL(self):

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd
        _box_title_button = self.box_title_button
        _box_title_button_dx = _box_title_button.dx
        # <<< 1dict (2win_blfs,, $
        # _blf_title = self.blfs[|blf_title|]$)
        _blf_title = self.blfs[0]
        # >>>
        _blf_title_unclip_text = _blf_title.unclip_text
        _r_blf_clipping_end = r_blf_clipping_end
        _font_title_dx = D_SIZE['font_title_dx']
        _SIZE_title0 = SIZE_title[0]

        _lim_L = REGION_DATA.L
        _lim_B = REGION_DATA.B + SIZE_tb[0]

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dy = MOUSE[1] - _xy[1]
            if _scissor.h - dy < 0: dy = _scissor.h
            else:
                if _box_win.B + dy < _lim_B: dy = _lim_B - _box_win.B
            _scissor.y += dy
            _scissor.h -= dy
            _box_win.B += dy
            _box_rim.B += dy
            _box_shadow.B += dy

            dx = _xy[0] - MOUSE[0]
            if _scissor.w + dx < 4 * _SIZE_title0: dx = 4 * _SIZE_title0 - _scissor.w
            else:
                if _box_win.L - dx < _lim_L: dx = _box_win.L - _lim_L
            _scissor.w += dx
            _box_win.R += dx
            _box_rim.R += dx
            _box_shadow.R += dx
            _box_title_button_dx(dx)
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            _blf_title.text = _r_blf_clipping_end(_blf_title.unclip_text, _blf_title.x,
                _box_title_button.L - _font_title_dx)

            _dxy(-dx, 0)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def to_modal_resize_click_TR(self):

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd
        _box_title_button = self.box_title_button
        _box_title_button_dx = _box_title_button.dx
        # <<< 1dict (2win_blfs,, $
        # _blf_title = self.blfs[|blf_title|]$)
        _blf_title = self.blfs[0]
        # >>>
        _blf_title_unclip_text = _blf_title.unclip_text
        _r_blf_clipping_end = r_blf_clipping_end
        _font_title_dx = D_SIZE['font_title_dx']
        _SIZE_title0 = SIZE_title[0]

        _lim_R = REGION_DATA.R
        _lim_T = REGION_DATA.T

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dy = _xy[1] - MOUSE[1]
            if _scissor.h - dy < 0: dy = _scissor.h
            else:
                if _box_win.T - dy > _lim_T: dy = _box_win.T - _lim_T
            _scissor.y += dy
            _scissor.h -= dy
            _box_win.B += dy
            _box_rim.B += dy
            _box_shadow.B += dy

            dx = MOUSE[0] - _xy[0]
            if _scissor.w + dx < 4 * _SIZE_title0: dx = 4 * _SIZE_title0 - _scissor.w
            else:
                if _box_win.R + dx > _lim_R: dx = _lim_R - _box_win.R
            _scissor.w += dx
            _box_win.R += dx
            _box_rim.R += dx
            _box_shadow.R += dx
            _box_title_button_dx(dx)
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            _blf_title.text = _r_blf_clipping_end(_blf_title_unclip_text, _blf_title.x,
                _box_title_button.L - _font_title_dx)

            _dxy(0, -dy)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def to_modal_resize_click_TL(self):

        end_trigger = r_end_trigger('resize')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _scissor = self.scissor
        _box_win = self.box_win
        _box_rim = self.box_rim
        # <<< 1dict (2win_boxes,, $
        # _box_shadow = self.boxes[|box_shadow|]$)
        _box_shadow = self.boxes[0]
        # >>>
        _dxy = self.dxy
        _resize_upd = self.resize_upd
        _box_title_button = self.box_title_button
        _box_title_button_dx = _box_title_button.dx
        # <<< 1dict (2win_blfs,, $
        # _blf_title = self.blfs[|blf_title|]$)
        _blf_title = self.blfs[0]
        # >>>
        _blf_title_unclip_text = _blf_title.unclip_text
        _r_blf_clipping_end = r_blf_clipping_end
        _font_title_dx = D_SIZE['font_title_dx']
        _SIZE_title0 = SIZE_title[0]

        _lim_L = REGION_DATA.L
        _lim_T = REGION_DATA.T

        def modal_resize_click():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dy = _xy[1] - MOUSE[1]
            if _scissor.h - dy < 0: dy = _scissor.h
            else:
                if _box_win.T - dy > _lim_T: dy = _box_win.T - _lim_T
            _scissor.y += dy
            _scissor.h -= dy
            _box_win.B += dy
            _box_rim.B += dy
            _box_shadow.B += dy

            dx = _xy[0] - MOUSE[0]
            if _scissor.w + dx < 4 * _SIZE_title0: dx = 4 * _SIZE_title0 - _scissor.w
            else:
                if _box_win.L - dx < _lim_L: dx = _box_win.L - _lim_L
            _scissor.w += dx
            _box_win.R += dx
            _box_rim.R += dx
            _box_shadow.R += dx
            _box_title_button_dx(dx)
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_title'}$)
            blfSize(FONT0, D_SIZE['font_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            _blf_title.text = _r_blf_clipping_end(_blf_title.unclip_text, _blf_title.x,
                _box_title_button.L - _font_title_dx)

            _dxy(-dx, -dy)
            _resize_upd()
            _xy[:] = MOUSE

        w_head = Head(self, modal_resize_click, self.end_modal_resize_click)
        _REDRAW()
        #|
    def resize_upd(self): pass
    def resize_upd_end(self):

        for e in self.areas:
            if hasattr(e, "resize_upd_end"):
                e.resize_upd_end()
        #|

    def to_modal_title(self):

        #|
        Admin.REDRAW()
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _TRIGGER_title_button = TRIGGER['title_button']
        _TRIGGER_title_move = TRIGGER['title_move']
        _box_title_button = self.box_title_button
        _box_hover = self.box_hover
        _is_inbox_other_win = self.is_inbox_other_win
        _box_rim_inbox = self.box_rim.inbox
        _inner = self.box_rim.inner
        _P_lock_win_size = P.lock_win_size
        _box_win = self.box_win

        x = MOUSE[0]
        B = _box_title_button.B
        T = _box_title_button.T
        h = T - B
        R = _box_title_button.R

        if x >= R - h:
            _box_hover.color = COL_win_title_hover_red
            _box_hover.LRBT_upd(R - h, R, B, T)
        elif x >= R - h - h:
            _box_hover.color = COL_win_title_hover
            _box_hover.LRBT_upd(R - h - h, R - h, B, T)
        elif x >= _box_title_button.L:
            _box_hover.color = COL_win_title_hover
            _box_hover.LRBT_upd(_box_title_button.L, _box_title_button.L + h, B, T)

        def modal_title():
            evt = Admin.EVT
            # <<< 1copy (0m_check_hud,, ${
            #     'CONTEXT_AREA': 'm.CONTEXT_AREA',
            #     'return "FORCE_PASS_THROUGH"': 'w_head.fin() ;return "FORCE_PASS_THROUGH"'
            # }$)
            if Admin.IS_HUD is True:
                hud_region = r_hud_region(m.CONTEXT_AREA)
                if hud_region is None: Admin.IS_HUD = False
                else:
                    hud_L = hud_region.x
                    hud_B = hud_region.y
                    if hud_L <= evt.mouse_x < hud_L + hud_region.width and hud_B <= evt.mouse_y < hud_B + hud_region.height:
                        if Admin.IS_INSIDE is False: w_head.fin() ;return "FORCE_PASS_THROUGH"
                        # <<< 1copy (0m_outside_evt,, $$)

                        Admin.IS_INSIDE = False
                        bpy.context.window.cursor_modal_restore()
                        if W_FOCUS[0] != None:
                            if hasattr(W_FOCUS[0], "outside_evt"): W_FOCUS[0].outside_evt()
                            W_FOCUS[0] = None
                        kill_evt()
                        # >>>

                        w_head.fin() ;return "FORCE_PASS_THROUGH"
            # >>>

            if _is_inbox_other_win():
                w_head.fin()
                return

            if _box_rim_inbox(MOUSE):
                # <<< 1copy (0defwin_TRIGGER_bring_to_front,, $$)
                if TRIGGER['click']():
                    if W_MODAL[-1] != self:

                        bring_to_front(self)
                # >>>

                if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc():
                    w_head.fin()
                    self.fin()
                    return

                if _inner[0] + 2 < MOUSE[0] < _inner[1] - 2 and _inner[2] + 2 < MOUSE[1] < _inner[3] - 2: pass
                elif _P_lock_win_size: pass
                else:
                    w_head.fin()
                    return

                if MOUSE[1] >= _box_win.title_B:
                    x = MOUSE[0]
                    B = _box_title_button.B
                    T = _box_title_button.T
                    h = T - B
                    R = _box_title_button.R

                    if x >= R - h:
                        _box_hover.color = COL_win_title_hover_red
                        if _box_hover.R != R:
                            _box_hover.LRBT_upd(R - h, R, B, T)
                            Admin.REDRAW()

                        if _TRIGGER_title_button():
                            self.to_modal_title_button(2, w_head)
                            return
                    elif x >= R - h - h:
                        _box_hover.color = COL_win_title_hover
                        if _box_hover.R != R - h:
                            _box_hover.LRBT_upd(R - h - h, R - h, B, T)
                            Admin.REDRAW()

                        if _TRIGGER_title_button():
                            self.to_modal_title_button(1, w_head)
                            return
                    elif x >= _box_title_button.L:
                        _box_hover.color = COL_win_title_hover
                        if _box_hover.L != _box_title_button.L:
                            _box_hover.LRBT_upd(_box_title_button.L, _box_title_button.L + h, B, T)
                            Admin.REDRAW()

                        if _TRIGGER_title_button():
                            self.to_modal_title_button(0, w_head)
                            return
                    else:
                        _box_hover.color = FLO_0000
                        if _box_hover.L == _box_hover.R == 0: pass
                        else:
                            _box_hover.LRBT_upd(0, 0, 0, 0)
                            Admin.REDRAW()

                        if _TRIGGER_title_move():
                            w_head.fin()
                            self.to_modal_move()
                            return
                else:
                    w_head.fin()
            else:
                w_head.fin()
            #|

        def end_modal_title():
            Admin.REDRAW()
            _box_hover.color = FLO_0000
            _box_hover.LRBT_upd(0, 0, 0, 0)

        w_head = Head(self, modal_title, end_modal_title)
        #|

    def to_modal_move(self):

        #|
        end_trigger = r_end_trigger('title_move')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _dxy = self.dxy

        def modal_move():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            _dxy(MOUSE[0] - _xy[0], MOUSE[1] - _xy[1])
            _xy[:] = MOUSE

        w_head = Head(self, modal_move, self.end_modal_move)
        #|
    def end_modal_move(self):
        self.dxy(*r_full_protect_dxy(*self.box_rim.r_LRBT()))

        #| change temp prefs in N-panel
        prefs_callback_disable()
        P_temp.pos = self.box_win.L, self.box_win.T
        prefs_callback_enable()
        #|

    def to_modal_title_button(self, button_ind, parent_head):


        end_trigger = r_end_trigger('title_move')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _button_ind = [button_ind]
        _box_hover = self.box_hover
        _box_win = self.box_win
        _box_title_button = self.box_title_button
        _box_title_button_inbox = _box_title_button.inbox
        _box_title_button_r_h = _box_title_button.r_h

        _box_hover.color = COL_win_title_hover_hold_red  if _button_ind[0] == 2 else COL_win_title_hover_hold

        def modal_title_button():
            _REDRAW()

            last_ind = _button_ind[0]

            if _box_title_button_inbox(MOUSE):
                h = _box_title_button_r_h()
                L = _box_title_button.L + h

                if MOUSE[0] >= L + h: _button_ind[0] = 2
                elif MOUSE[0] >= L: _button_ind[0] = 1
                else: _button_ind[0] = 0
            else:
                _button_ind[0] = None

            if last_ind != _button_ind[0]:
                if _button_ind[0] == None:
                    _box_hover.color = FLO_0000
                else:
                    h = _box_title_button_r_h()
                    L = _box_title_button.L + _button_ind[0] * h
                    R = L + h
                    B = _box_win.title_B
                    T = _box_win.T

                    _box_hover.LRBT_upd(L, R, B, T)
                    _box_hover.color = COL_win_title_hover_hold_red  if _button_ind[0] == 2 else COL_win_title_hover_hold

            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc():
                _button_ind[0] = None
                w_head.fin()
            if end_trigger():
                w_head.fin()
            #|

        def end_modal_title_button():
            parent_head.fin()
            ind = _button_ind[0]
            if ind == 2: self.fin()
            elif ind == 1: self.evt_fit()
            elif ind == 0: m.ADMIN.evt_min(self)
            #|

        w_head = Head(self, modal_title_button, end_modal_title_button)
        _REDRAW()
        #|

    def to_modal_pan_win(self):

        #|
        end_trigger = r_end_trigger('pan_win')
        mouseloop_end, mouseloop, r_dxy_mouse = r_mouseloop()
        _TRIGGER_esc = TRIGGER['esc']
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE

        # /* 0win_get_canvas_lim
        border_outer = SIZE_border[0]
        box_win = self.box_win
        areas = self.areas
        e = areas[0].box_area
        _lim_L = e.L
        _lim_R = e.R
        _lim_B = e.B
        _lim_T = e.T
        for a in areas:
            e = a.box_area
            if e.L < _lim_L: _lim_L = e.L
            if e.R > _lim_R: _lim_R = e.R
            if e.B < _lim_B: _lim_B = e.B
            if e.T > _lim_T: _lim_T = e.T
        # */

        _lim_R = box_win.R - border_outer - _lim_R + _lim_L
        _lim_L = box_win.L + border_outer
        _lim_B = box_win.B + border_outer + _lim_T - _lim_B
        _lim_T = box_win.title_B - border_outer
        if _lim_R > _lim_L: _lim_R = _lim_L
        if _lim_B < _lim_T: _lim_B = _lim_T

        def end_modal_pan_win():
            mouseloop_end()
            kill_evt_except()
            self.resize_upd_end()

            #| change temp prefs in N-panel
            prefs_callback_disable()
            e = self.areas[0].box_area
            P_temp.canvas = e.L - self.box_win.L - SIZE_border[0], e.T - self.box_win.title_B + SIZE_border[0]
            prefs_callback_enable()

        def modal_pan_win():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            dx, dy = r_dxy_mouse()

            e = self.areas[0].box_area
            x = e.L + dx
            y = e.T + dy

            if x > _lim_L: dx += _lim_L - x
            elif x < _lim_R: dx += _lim_R - x
            if y < _lim_T: dy += _lim_T - y
            elif y > _lim_B: dy += _lim_B - y

            for e in self.areas: e.dxy(dx, dy)

            mouseloop()

        w_head = Head(self, modal_pan_win, end_modal_pan_win)
        #|

    def i_draw(self):
        #|
        blend_set('ALPHA')
        for e in self.boxes: e.bind_draw()

        scissor_test_set(True)
        self.scissor.use()

        for e in self.areas:
            e.u_draw()

        scissor_test_set(False)

        # <<< 1dict (2win_blfs,, $
        # e = self.blfs[|blf_title|]$)
        e = self.blfs[0]
        # >>>
        blfSize(FONT0, D_SIZE['font_title'])
        blfColor(FONT0, *COL_win_title_fg)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)
        #|

    def dxy(self, dx, dy):
        # /* 0win_Window_dxy_without_areas
        self.scissor.dxy(dx, dy)
        for e in self.boxes: e.dxy_upd(dx, dy)

        for e in self.blfs:
            e.x += dx
            e.y += dy
        # */
        for e in self.areas: e.dxy(dx, dy)
        #|

    def outside_evt(self): pass

    def evt_fit(self):

        P_temp.canvas = 0, 0
        #|
        if hasattr(self, "r_size_default"):
            sizeX, sizeY = self.r_size_default()
            P_temp.size[0] = sizeX
            P_temp.size = self.box_win.r_w(), sizeY
            return

        # <<< 1copy (0win_get_canvas_lim,, $$)
        border_outer = SIZE_border[0]
        box_win = self.box_win
        areas = self.areas
        e = areas[0].box_area
        _lim_L = e.L
        _lim_R = e.R
        _lim_B = e.B
        _lim_T = e.T
        for a in areas:
            e = a.box_area
            if e.L < _lim_L: _lim_L = e.L
            if e.R > _lim_R: _lim_R = e.R
            if e.B < _lim_B: _lim_B = e.B
            if e.T > _lim_T: _lim_T = e.T
        # >>>

        border_outer2 = border_outer + border_outer
        target_size_x = _lim_R - _lim_L + border_outer2
        target_size_y = _lim_T - _lim_B + border_outer2
        P_temp.size[0] = target_size_x
        win_width = box_win.R - box_win.L
        if win_width != target_size_x: P_temp.size[0] = win_width

        P_temp.size[1] = target_size_y
        win_height = box_win.title_B - box_win.B
        if win_height != target_size_y: P_temp.size[1] = win_height
        #|

    def r_area_posRB_adaptive(self, area):
        areas = {a  for a in self.areas  if a != area}
        L, R, B, T = area.box_area.r_LRBT()

        if any(a.box_area.L >= R  for a in areas):
            posR = R
        else:
            posR = self.box_win.R - SIZE_border[0]

        if any(a.box_area.T <= B  for a in areas):
            posB = B
        else:
            posB = self.box_win.B + SIZE_border[0]
        return posR, posB
        #|
    def r_editor_name(self):
        # <<< 1dict (2win_blfs,, $
        # return self.blfs[|blf_title|].unclip_text$)
        return self.blfs[0].unclip_text
        # >>>
        #|

    def upd_data(self):
        for e in self.areas: e.upd_data()
    #|
    #|

class Head:
    __slots__ = (
        'w',
        'modal',
        'end_modal',
        'data')

    def __init__(self, w, i_modal, end_modal=None, disable_update=False):
        #|
        self.w = w
        self.modal = i_modal
        self.end_modal = end_modal

        W_HEAD.append(self)
        blockblsubwindows()
        if disable_update: TAG_UPDATE[2] = False
        #|

    def fin(self):

        push_modal_safe()

        W_HEAD.remove(self)
        if not W_HEAD: TAG_UPDATE[2] = True

        if self.end_modal: self.end_modal()
        #|
    #|
    #|


#| require REGION_DATA.upd()
def r_full_protect_dxy(L, R, B, T):
    #|
    if R > REGION_DATA.R:
        dx = REGION_DATA.R - R
    elif L < REGION_DATA.L:
        dx = REGION_DATA.L - L
    else:
        dx = 0

    if T > REGION_DATA.T:
        return dx, REGION_DATA.T - T
    elif B < REGION_DATA.B + SIZE_tb[0]:
        dy = REGION_DATA.B + SIZE_tb[0] - B
        if T + dy > REGION_DATA.T: return dx, REGION_DATA.T - T
        return dx, dy
    return dx, 0
    #|



#|  kw need
#|      w
#|      pos
#|      size
#|  kw optional
#|      use_titlebar
#|      title
#|      title_button
#|
class DropDown:
    __slots__ = (
        'w',
        'modal',
        'u_draw',
        'boxes',
        'blfs',
        'box_rim',
        'box_win',
        'box_title_button',
        'box_hover',
        'scissor',
        'areas',
        'is_flip_y',
        'title_buttons',
        'data',
        'focus_element',
        'is_autoclose',
        'child_head')

    INIT_DATA = None

    def __init__(self, **kw):

        # ref_DropDownVal
        DropDown.INIT_DATA = kw
        blfs = []

        self.modal = self.i_modal
        self.u_draw = self.i_draw
        self.w = kw["w"]
        self.data = {}
        self.is_autoclose = kw["is_autoclose"]  if "is_autoclose" in kw else False

        if "event" in kw:
            evt = kw["event"]
        else:
            evt = Admin.EVT
            kw["event"] = evt

        title_buttons = []
        if "use_titlebar" in kw and kw["use_titlebar"]:
            inner = SIZE_title[1] // 20
            button_h = SIZE_title[1] - inner - inner
            title_B = - SIZE_title[1]
            title_x = D_SIZE['font_dd_title_dx']
            titleR = kw["size"][0] - title_x
            if "title_button" in kw:
                for o in kw["title_button"]:
                    if o[0] == "close":
                        title_buttons.append(
                            ButtonFnImg(self, RNA_close, o[1], 'GpuImg_dropdown_close'))
                        titleR -= inner + inner + button_h
                    else:
                        title_button0, button_width = o
                        title_buttons.append(title_button0)
                        title_button0.w = self
                        titleR -= button_width + inner
            if "title" in kw:
                title = kw["title"]
                if isinstance(title, str):
                    title_y = title_B + D_SIZE['font_dd_title_dy']
                    # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_dd_title'}$)
                    blfSize(FONT0, D_SIZE['font_dd_title'])
                    blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
                    # >>>
                    blfs.append(BlfClip(r_blf_clipping_end(title, title_x, titleR
                        ), title, title_x, title_y))
        else:
            title_B = 0

        rim_d = SIZE_dd_border[2]
        R, B = kw["size"]
        B = title_B - B

        box_win = GpuDropDown(0, R, B, 0, title_B)
        box_rim = GpuDropDownRim(-rim_d, R + rim_d, B - rim_d, rim_d, rim_d)
        # box_title_button = GpuImg_title_button(R - h3, R, title_B, 0)
        box_hover = GpuBox(FLO_0000)
        box_shadow = GpuShadowDropDown(
            SIZE_dd_shadow_offset[0],
            R + SIZE_dd_shadow_offset[1],
            B + SIZE_dd_shadow_offset[2],
            SIZE_dd_shadow_offset[3],
            SIZE_shadow_softness[1])


        boxes = [
            box_shadow,
            box_rim,
            box_win,
            box_hover]

        self.boxes = boxes
        self.blfs = blfs
        self.box_rim = box_rim
        self.box_win = box_win
        self.box_hover = box_hover

        if title_buttons:
            self.title_buttons = title_buttons
            self.focus_element = None

            # ref: append_title_button
            R0 = R - inner
            L0 = R0 - button_h
            B0 = title_B + inner
            for e in title_buttons:
                boxes.append(e.box_button)
                e.init_bat(L0, R0, -inner)
                B_diff = B0 - e.box_button.B
                e.box_button.B += B_diff
                if hasattr(e, "box_img"):
                    e.box_img.B += B_diff
                    boxes.append(e.box_img)
                else:
                    e.blf_value.y += B_diff
                    blfs.append(e.blf_value)

                R0 = e.box_button.L - inner
                L0 = 0

        x, y = kw["pos"]
        if "protect_pos" in kw and kw["protect_pos"] == False: pass
        else:
            dx, dy = r_full_protect_dxy(box_rim.L + x, box_rim.R + x, box_rim.B + y, box_rim.T + y)
            x += dx
            y += dy

        for e in boxes: e.dxy_upd(x, y)
        for e in blfs:
            e.x += x
            e.y += y

        self.scissor = Scissor()
        self.scissor.LRBT(box_win.L, box_win.R, box_win.B, box_win.title_B)
        self.init(boxes, blfs)

        W_HEAD.append(self)
        W_DRAW.append(self)

        Admin.REDRAW()
        Admin.TAG_CURSOR = 'DEFAULT'
        if "killevt" in kw and kw["killevt"] == False: pass
        else: kill_evt()
        blockblsubwindows()
        #|
    def evt_close_confirm(self):

        pass
        #|
    def fin(self):

        Admin.REDRAW()
        W_HEAD.remove(self)
        W_DRAW.remove(self)

        kill_evt_except()
        Admin.ENDPUSH = False

        self.fin_callback()
        #|
    def fin_callback(self): pass
    def callback_end_modal_dd(self, dict_data):
        self.data.update(dict_data)
        self.fin()
        #|

    def win_inbox(self, MOUSE):
        if self.box_rim.inbox(MOUSE):
            if MOUSE[1] >= self.box_win.title_B: return False
            return True
        return False
        #|
    def is_inbox_other_win(self): return False
    def basis_win_evt(self):
        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']() or TRIGGER['dd_esc']():
            return self.fin

        if self.box_win.inbox(MOUSE):
            if MOUSE[1] > self.box_win.title_B:
                if TRIGGER['title_move'](): return self.to_modal_move
        else:
            if self.is_autoclose is True: return self.fin

        if self.win_inbox(MOUSE) == False:
            if hasattr(self, "evt_dd_confirm"):
                if TRIGGER['dd_confirm'](): return self.evt_dd_confirm
            if hasattr(self, "evt_click_outside"):
                if TRIGGER['click'](): return self.evt_click_outside
        return None
        #|
    def basis_win_evt_protect(self):
        if hasattr(self, "title_buttons"):
            e = None
            for o in self.title_buttons:
                if o.inside(MOUSE):
                    e = o
                    break

            if e is None:
                if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
                self.focus_element = None
            else:
                if self.focus_element != e:
                    if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
                    self.focus_element = e
                    e.inside_evt()
                    kill_evt_except()

                if e.modal(): return N

        if self.box_win.inbox(MOUSE) and MOUSE[1] > self.box_win.title_B:
            if TRIGGER['title_move'](): return self.to_modal_move

        return None
        #|

    def i_modal(self):
        basis_evt_fn = self.basis_win_evt()
        if basis_evt_fn != None:
            basis_evt_fn()
            return

        for e in self.areas:
            if e.box_area.inbox(MOUSE):
                e.modal()
                return
        #|

    def to_modal_move(self):

        #|
        end_trigger = r_end_trigger('title_move')
        _REDRAW = Admin.REDRAW
        _EVT_TYPE = EVT_TYPE
        _TRIGGER_esc = TRIGGER['esc']
        _xy = MOUSE[:]
        _dxy = self.dxy

        def modal_move():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _TRIGGER_esc() or end_trigger():
                w_head.fin()
                return

            _dxy(MOUSE[0] - _xy[0], MOUSE[1] - _xy[1])
            _xy[:] = MOUSE

        w_head = Head(self, modal_move, self.end_modal_move)
        #|
    def end_modal_move(self):
        self.dxy(*r_full_protect_dxy(*self.box_rim.r_LRBT()))
        #|

    def i_draw(self):
        #|
        blend_set('ALPHA')
        for e in self.boxes: e.bind_draw()

        scissor_test_set(True)
        self.scissor.use()

        for e in self.areas:
            e.u_draw()

        scissor_test_set(False)
        if self.blfs:
            e = self.blfs[0]
            blfSize(FONT0, D_SIZE['font_dd_title'])
            blfColor(FONT0, *COL_dd_title_fg)
            blfPos(FONT0, e.x, e.y, 0)
            blfDraw(FONT0, e.text)
            blfSize(FONT0, D_SIZE['font_main'])
            for e in self.blfs[1 :]:
                if hasattr(e, "size"):
                    blfSize(FONT0, e.size)
                    blfColor(FONT0, *e.color)
                    blfPos(FONT0, e.x, e.y, 0)
                    blfDraw(FONT0, e.text)
                    blfSize(FONT0, D_SIZE['font_main'])
                else:
                    blfColor(FONT0, *e.color)
                    blfPos(FONT0, e.x, e.y, 0)
                    blfDraw(FONT0, e.text)
        #|

    def dxy(self, dx, dy):
        self.scissor.dxy(dx, dy)
        for e in self.boxes: e.dxy_upd(dx, dy)

        for e in self.blfs:
            e.x += dx
            e.y += dy

        for e in self.areas: e.dxy(dx, dy)
        #|

    def set_title(self, s):
        e = self.blfs[0]
        e.unclip_text = s
        # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_dd_title'}$)
        blfSize(FONT0, D_SIZE['font_dd_title'])
        blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
        # >>>
        e.text = r_blf_clipping_end(s, e.x, self.title_buttons[-1].box_button.L - SIZE_title[1] // 20)
        #|
    def remove_title_buttons(self, ind0, ind1):
        title_buttons = self.title_buttons
        boxes = self.boxes
        blfs = self.blfs

        for r in range(ind0, ind1):
            e = title_buttons[r]
            boxes.remove(e.box_button)

            if hasattr(e, "box_img"):
                boxes.remove(e.box_img)
            else:
                blfs.remove(e.blf_value)

        del title_buttons[ind0 : ind1]
        #|
    def append_title_button(self, e):
        title_buttons = self.title_buttons
        boxes = self.boxes
        blfs = self.blfs
        inner = SIZE_title[1] // 20
        button_h = SIZE_title[1] - inner - inner

        R0 = title_buttons[-1].box_button.L - inner
        B0 = self.box_win.title_B + inner
        T0 = self.box_win.T - inner

        boxes.append(e.box_button)
        e.init_bat(0, R0, T0)
        B_diff = B0 - e.box_button.B
        e.box_button.B += B_diff
        if hasattr(e, "box_img"):
            e.box_img.B += B_diff
            boxes.append(e.box_img)
        else:
            e.blf_value.y += B_diff
            blfs.append(e.blf_value)

        R0 = e.box_button.L - inner
        title_buttons.append(e)
        #|
    #|
    #|


class Detail(Window):
    __slots__ = 'rna'

    name = 'Detail'

    def __init__(self, text, title="Detail", event=None):

        self.rna = RnaString("default", "Detail", "Temporary Editor Property", text, "LINES", is_readonly=True)

        x = SIZE_widget[0] // 2
        preserve_size = (21 * SIZE_widget[0], 11 * SIZE_widget[0] + SIZE_title[0])

        if event is None:
            super().__init__(id_class="", use_pos=True, use_fit=True, pos_offset=(-x, x), preserve_size=preserve_size)
        else:
            super().__init__(id_class="", use_pos=True, use_fit=True, pos_offset=(-x, x), event=event, preserve_size=preserve_size)
        #|

    def init(self, boxes, blfs):
        sizeX, sizeY = self.r_size_default()
        a0 = AreaStringXYPre(self, input_text=self.rna.default)
        self.areas = [a0]

        border_outer = SIZE_border[0]
        e = self.box_win
        LL = e.L
        TT = e.title_B
        a0.upd_size(
            LL + border_outer,
            LL + sizeX - border_outer,
            TT - sizeY + border_outer,
            TT - border_outer,
            use_resize_upd_end = False)
        #|

    def upd_size_areas(self, use_resize_upd_end=True):
        border_outer = SIZE_border[0]
        e = self.box_win
        LL = e.L
        RR = e.R
        BB = e.B
        TT = e.title_B
        self.areas[0].upd_size(
            LL + border_outer,
            RR - border_outer,
            BB + border_outer,
            TT - border_outer,
            use_resize_upd_end = use_resize_upd_end)
        #|

    @staticmethod
    def r_size_default():
        # 368, 182
        return SIZE_border[0] * 2 + 20 * SIZE_widget[0], SIZE_border[0] * 2 + (SIZE_dd_border[0] + SIZE_border[3]) * 2 + D_SIZE['widget_full_h'] + 8 * SIZE_widget[0] + min(SIZE_widget[2], SIZE_widget[0])
        #|

    @staticmethod
    def r_rna_info(rna):
        ty = rs_format_py_type(rna)
        s = f'Property Name :  {rna.name}\n\nDescription :\n{rna.description}\n\nType :  {ty}\nIdentifier :  {rna.identifier}\n'

        for at in (
            "subtype",
            "unit",
            "hard_min",
            "hard_max",
            "step",
            "is_readonly",
        ):
            if hasattr(rna, at):
                v = getattr(rna, at)
                if isinstance(v, float): v = value_to_display(v)
                s += f'{at.title().replace("_", " ")} :  {v}\n'

        if hasattr(rna, "is_array") and rna.is_array:
            s += f'Is Array :  True\n'
            s += f'Array Length :  {rna.array_length}\n'
            s += f'Default Array :  {tuple(rna.default_array)}\n'
        else:
            s += f'Is Array :  False\n'
            v = rna.default  if hasattr(rna, "default") else "None"
            s += f'Default :  {v}\n'

            if hasattr(rna, "enum_items"):
                if rna.is_enum_flag:
                    s += f'Value Type :  set\n'
                else:
                    s += f'Value Type :  str\n'

                s += 'Enum Items :\n' + Detail.r_format_enum_items(rna.enum_items)
            else:
                s += f'Value Type :  {rs_format_py_type(v)}\n'

        s += "\n"
        for at in dir(rna):
            if at in {
                "name",
                "description",
                "identifier",
                "subtype",
                "unit",
                "hard_min",
                "hard_max",
                "step",
                "is_readonly",
                "is_array",
                "array_length",
                "default_array",
                "default",
                "is_enum_flag",
                "enum_items",
            }: continue

            if hasattr(rna, at):
                v = getattr(rna, at)
                if type(v) not in {tuple, type(None), str, bool, int, float, list, dict, set}: continue

                if isinstance(v, float): v = value_to_display(v)
                s += f'{at.title().replace("_", " ")} :  {v}\n'

        if hasattr(rna, "data"):
            s += "\nData:\n"
            data = rna.data
            for at in dir(data):
                if at.startswith("_"): continue
                v = getattr(data, at)
                if isinstance(v, float): v = value_to_display(v)
                s += f'    {at.title().replace("_", " ")} :  {v}\n'
        return s
        #|
    @staticmethod
    def r_format_enum_items(enum_items, indent=0):
        s0 = " " * indent
        s = s0 + "(\n"
        le = len(s)
        s1 = '), ' + s

        for e in enum_items:
            s += s0 + f'    "{e.identifier}",\n'
            s += s0 + f'    "{e.name}",\n'
            description = e.description.replace("\\", "\\\\")
            s += s0 + f'    "{description}",\n' + s1
        return s[: - le - 2]
        #|
    #|
    #|


## _file_ ##
def late_import():
    #|
    import bpy, blf, gpu

    blfSize = blf.size
    blfColor = blf.color
    blfPos = blf.position
    blfDraw = blf.draw
    blfDimen = blf.dimensions

    blend_set = gpu.state.blend_set
    scissor_test_set = gpu.state.scissor_test_set

    from math import floor

    from .  import VMD

    m = VMD.m

    # <<< 1mp (VMD.area
    area = VMD.area
    AreaStringXYPre = area.AreaStringXYPre
    # >>>

    # <<< 1mp (VMD.block
    block = VMD.block
    BlockFull = block.BlockFull
    ButtonFnImg = block.ButtonFnImg
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    kill_evt = keysys.kill_evt
    kill_evt_except = keysys.kill_evt_except
    MOUSE = keysys.MOUSE
    EVT_TYPE = keysys.EVT_TYPE
    TRIGGER = keysys.TRIGGER
    r_end_trigger = keysys.r_end_trigger
    PRESS = keysys.PRESS
    # >>>

    # <<< 1mp (m
    P = m.P
    Admin = m.Admin
    W_PROCESS = m.W_PROCESS
    W_MODAL = m.W_MODAL
    W_HEAD = m.W_HEAD
    W_DRAW = m.W_DRAW
    W_FOCUS = m.W_FOCUS
    REGION_DATA = m.REGION_DATA
    r_mouseloop = m.r_mouseloop
    r_hud_region = m.r_hud_region
    prefs_callback_disable = m.prefs_callback_disable
    prefs_callback_enable = m.prefs_callback_enable
    TAG_UPDATE = m.TAG_UPDATE
    push_modal_safe = m.push_modal_safe
    bring_draw_to_top_safe = m.bring_draw_to_top_safe
    update_data = m.update_data
    blockblsubwindows = m.blockblsubwindows
    # >>>

    util = VMD.util

    # <<< 1mp (util.com
    com = util.com
    rs_format_py_type = com.rs_format_py_type
    N = com.N
    NS = com.NS
    value_to_display = com.value_to_display
    # >>>

    # <<< 1mp (util.const
    const = util.const
    FLO_0000 = const.FLO_0000
    # >>>

    # <<< 1mp (util.num
    num = util.num
    r_smallest_miss = num.r_smallest_miss
    r_best_new_int_miss = num.r_best_new_int_miss
    # >>>

    # <<< 1mp (util.types
    types = util.types
    RnaString = types.RnaString
    RnaButton = types.RnaButton
    # >>>

    blg = VMD.utilbl.blg

    # <<< 1mp (blg
    BlfClip = blg.BlfClip
    GpuBox = blg.GpuBox
    GpuWin = blg.GpuWin
    GpuWinRim = blg.GpuWinRim
    GpuShadow = blg.GpuShadow
    GpuDropDown = blg.GpuDropDown
    GpuDropDownRim = blg.GpuDropDownRim
    GpuShadowDropDown = blg.GpuShadowDropDown
    GpuImg_title_button = blg.GpuImg_title_button
    r_blf_clipping_end = blg.r_blf_clipping_end
    Scissor = blg.Scissor
    report = blg.report
    D_SIZE = blg.D_SIZE
    FONT0 = blg.FONT0
    SIZE_title = blg.SIZE_title
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_tb = blg.SIZE_tb
    SIZE_win_shadow_offset = blg.SIZE_win_shadow_offset
    SIZE_dd_shadow_offset = blg.SIZE_dd_shadow_offset
    SIZE_shadow_softness = blg.SIZE_shadow_softness
    SIZE_widget = blg.SIZE_widget
    COL_win_title_fg = blg.COL_win_title_fg
    COL_dd_title_fg = blg.COL_dd_title_fg
    COL_win_title_hover = blg.COL_win_title_hover
    COL_win_title_hover_red = blg.COL_win_title_hover_red
    COL_win_title_hover_hold = blg.COL_win_title_hover_hold
    COL_win_title_hover_hold_red = blg.COL_win_title_hover_hold_red
    # >>>

    ed_undo = bpy.ops.ed.undo
    ed_redo = bpy.ops.ed.redo

    _xy = [0, 0]
    _end_trigger = None

    bring_to_front = m.bring_to_front
    P_temp = P.temp

    RNA_close = RnaButton("close",
        name = "Close",
        button_text = "",
        description = "DropDown Menu close button.")

    globals().update(locals())
    #|
