











from types import SimpleNamespace
from pathlib import Path
from os import sep as os_sep
from math import ceil

from . util import deco

# <<< 1mp (deco
successResult = deco.successResult
noRecursive = deco.noRecursive
catch = deco.catch
# >>>

from . win import DropDown


class UpdateModal:
    __slots__ = 'upd_data'

    def __init__(self, upd_data):
        self.upd_data = upd_data
        #|
    #|
    #|

class DropDownTask(DropDown):
    __slots__ = ()

    def __init__(self, w, pos, items, title):
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0

        size = (SIZE_widget[0] * 16 + d0x2,
            d0x2 + d1 + (SIZE_filter[2] + SIZE_border[3]) * 2 + max(SIZE_filter[0], D_SIZE['widget_full_h']))

        super().__init__(w=w, pos=pos, size=size, use_titlebar=True, title=title, items=items)

        self.child_head = self.areas[0].to_modal_dd()
        #|
    def init(self, boxes, blfs):

        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        items = init['items']
        size_x, size_y = init['size']

        self.areas = [AreaFilterY(self, L, L + size_x, T - size_y, T, lambda: items, is_dropdown=True)]
        #|

    def fin_callback(self):

        #|
        data = self.data
        if data["use_text_output"] != None:

            w = None
            if P.adaptive_enum_input:
                if self.areas[0].blf_text.unclip_text.strip():
                    if data["best_item"] != None:
                        w = data["best_item"].value

            if w is None:
                filt = self.areas[0].filt
                tx = self.areas[0].blf_text.unclip_text
                if filt.active_index != None:
                    e = filt.match_items[filt.active_index]
                    if e.name == tx:
                        w = e.value

            if w is not None:
                if w in W_MODAL:
                    if W_MODAL[-1] == w: m.ADMIN.evt_min(w)
                    else: bring_to_front(w)
                else:
                    m.ADMIN.evt_unmin(w)
        #|
    #|
    #|

class DropDownRM(DropDown):
    __slots__ = ()

    def __init__(self, w, pos, items,
                get_icon = None,
                get_info = None,
                title = "Context Menu",
                size_x = None,
                size_y = None,
                input_text = "",
                area0_cls = None):
        #|
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        blfSize(FONT0, D_SIZE['font_main'])

        if size_x == None:
            items_max_x = floor(max(blfDimen(FONT0, e.name)[0]  for e in items))  if items else 0

            size_x = max(SIZE_widget[0] * 12, min(REGION_DATA.R - REGION_DATA.L,
                SIZE_widget[0] + d0x2 + D_SIZE['font_main_dx'] * 2 + items_max_x))
        if size_y == None:
            size_y = min(REGION_DATA.T - REGION_DATA.B - SIZE_tb[0] - SIZE_title[1],
                d0x2 + d1 + (SIZE_filter[2] + SIZE_border[3]) * 2 + (len(items) + 1) * D_SIZE['widget_full_h'])

        super().__init__(
            w = w,
            pos = pos,
            size = (size_x, size_y),
            use_titlebar = True,
            title = title,
            items = items,
            get_icon = get_icon,
            get_info = get_info,
            input_text = input_text,
            area0_cls = AreaFilterY  if area0_cls is None else area0_cls)

        self.child_head = self.areas[0].to_modal_dd()
        #|
    def init(self, boxes, blfs):

        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        size_x, size_y = init['size']
        items = init['items']
        area0_cls = init['area0_cls']

        self.areas = [area0_cls(self, L, L + size_x, T - size_y, T, lambda: items,
            get_icon = init['get_icon'],
            get_info = init['get_info'],
            input_text = init['input_text'],
            is_dropdown = True)]
        #|

    def fin_callback(self):

        #|
        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        if data["use_text_output"] != None:

            if data["use_text_output"]:
                if P.adaptive_enum_input:
                    if self.areas[0].blf_text.unclip_text.strip():
                        if data["best_item"] != None: data["best_item"].value()
            else:
                if data["best_item"] != None: data["best_item"].value()

        data.clear()
        #|
    #|
    #|
class DropDownRMKeymap(DropDownRM):
    __slots__ = ()

    def __init__(self, w, pos, lis_id_fn,
                title="Context Menu",
                fin_callfront=None,
                override_name=None,
                override_icon=None):

        get_info = rm_get_info_km  if P.show_rm_keymap else None
        area0_cls = AreaFilterYDropDownRMKeymap

        if override_icon is None:
            _D_icon = D_icon_rm
        else:
            _D_icon = D_icon_rm.copy()
            _D_icon.update(override_icon)

        def get_icon(e):
            if e.identifier in _D_icon:
                return _D_icon[e.identifier]()
            return GpuImgNull()

        if override_name is None: override_name = {}

        super().__init__(w, pos,
            [IdentifierNameValue(idd, ((override_name[idd]  if idd in override_name else BL_RNA_PROP_keymaps[idd].name
                )  if idd in BL_RNA_PROP_keymaps else idd
                ), fx)  for idd, fx in lis_id_fn],
            get_icon=get_icon, get_info=get_info, title=title, area0_cls=area0_cls)

        if fin_callfront is not None: self.data["fin_callfront"] = fin_callfront
        #|
    #|
    #|
class DropDownTaskRM(DropDownRMKeymap):
    __slots__ = ()

    def __init__(self, task, pos):
        items = [
            ("Close All", self.evt_close_all),
            ("New Editor", self.evt_new_editor),
        ]
        super().__init__(task, pos, items, title=split_upper(task.box_icon.__class__.__name__[7 : ]))
        #|

    @ catch
    def evt_close_all(self):
        for w in self.w.ws.copy():
            w.fin()
        #|
    @ catch
    def evt_new_editor(self):
        bpy.ops.wm.vmd_editor("INVOKE_DEFAULT", id_class=self.w.box_icon.__class__.__name__[7 : ], use_pos=False)
        #|
    #|
    #|
class DropDownString(DropDown):
    __slots__ = ()

    def __init__(self, w, LRBT, input_text):
        d0 = SIZE_dd_border[0]
        # d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        LL, RR, BB, TT = LRBT

        size = RR - LL + d0x2, TT - BB + d0x2

        super().__init__(w=w, pos=(LL - d0, TT + d0), size=size, use_titlebar=False, protect_pos=False,
            input_text=input_text)

        self.child_head = self.areas[0].to_modal_dd()
        #|
    def init(self, boxes, blfs):

        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        size_x, size_y = init['size']

        self.areas = [AreaString(self, L, L + size_x, T - size_y, T, input_text=init['input_text'])]
        #|

    def fin_callback(self):

        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        w = self.w
        is_readonly = hasattr(w, "rna") and hasattr(w.rna, "is_readonly") and w.rna.is_readonly

        if data["use_text_output"] == None or is_readonly:
            if "cancel_callback" in data:
                data["cancel_callback"]()
        else:

            try: w.set(self.areas[0].blf_text.unclip_text)
            except: report("Value Error")

        data.clear()
        #|
    #|
    #|
class DropDownStringMatch(DropDown):
    __slots__ = ()

    def __init__(self, w, LRBT, input_text, is_match_case=None, is_match_whole_word=None, is_match_end=None):
        d0 = SIZE_dd_border[0]
        # d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        LL, RR, BB, TT = LRBT

        size = RR - LL + d0x2, TT - BB + d0x2

        super().__init__(w=w, pos=(LL - d0, TT + d0), size=size, use_titlebar=False, protect_pos=False,
            input_text=input_text)

        self.child_head = self.areas[0].to_modal_dd(
            is_match_case = is_match_case,
            is_match_whole_word = is_match_whole_word,
            is_match_end = is_match_end)
        #|

    def init(self, boxes, blfs):

        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        size_x, size_y = init['size']

        self.areas = [AreaStringMatch(self, L, L + size_x, T - size_y, T, input_text=init['input_text'])]
        #|

    def fin_callback(self):

        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        w = self.w
        is_readonly = hasattr(w, "rna") and hasattr(w.rna, "is_readonly") and w.rna.is_readonly

        if data["use_text_output"] == None or is_readonly:
            if "cancel_callback" in data:
                data["cancel_callback"]()
        else:

            try: w.set(self.areas[0].blf_text.unclip_text)
            except: report("Value Error")

        data.clear()
        #|
    #|
    #|
class DropDownStringXY(DropDown):
    __slots__ = ()

    def __init__(self, w, LRBT, input_text, font_id=None, killevt=True, select_all=None):
        d0 = SIZE_dd_border[0]
        # d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        LL, RR, BB, TT = LRBT

        super().__init__(w=w,
            pos = (LL - d0, TT + d0),
            size = (RR - LL + d0x2, TT - BB + d0x2),
            use_titlebar = False,
            protect_pos = False,
            killevt = killevt,
            input_text = input_text,
            font_id = FONT0  if font_id is None else font_id)

        self.child_head = self.areas[0].to_modal_dd(select_all=select_all)
        #|
    def init(self, boxes, blfs):

        #|
        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        size_x, size_y = init['size']

        a0 = AreaStringXY(self,
            input_text = init['input_text'],
            font_id = init['font_id'])
        a0.upd_size(L, L + size_x, T - size_y, T)
        self.areas = [a0]
        #|

    def fin_callback(self):

        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        w = self.w
        is_readonly = hasattr(w, "rna") and hasattr(w.rna, "is_readonly") and w.rna.is_readonly

        if is_readonly: pass
        elif data["use_text_output"] == None:
            w.b_str = None
            w.upd_data()
        else:

            try:
                w.set(self.areas[0].text)
            except:
                report("Value Error")

        data.clear()
        #|
    #|
    #|
class DropDownText(DropDown):
    __slots__ = 'save_confirm_message', 'confirm_fn', 'r_default_value'

    def __init__(self, w, LRT, input_text, confirm_fn, r_default_value,
                row_count = 28,
                font_id = None,
                killevt = True,
                title = "Text Editor",
                save_confirm_message = "\n    It will save all preferences.\n    This process cannot be Undo/Redo.\n    Do you want to continue?",
                title_buttons = None):

        self.confirm_fn = confirm_fn
        self.r_default_value = r_default_value
        self.save_confirm_message = save_confirm_message

        d0 = SIZE_dd_border[0]
        # d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        line_h = SIZE_widget[0]
        widget_rim = SIZE_border[3]
        LL, RR, TT = LRT
        BB = TT - row_count * line_h - widget_rim - widget_rim
        inner = SIZE_title[1] // 20
        button_h = SIZE_title[1] - inner - inner - widget_rim - widget_rim
        button_font_size = floor(button_h * SIZE_foreground[2])
        button_save = ButtonFnFreeSize(None, RNA_save, self.bufn_save, button_font_size, button_h)
        button_reset = ButtonFnFreeSize(None, RNA_reset, self.bufn_reset, button_font_size, button_h)
        title_button = [
            ("close", self.fin_from_area),
            (button_save, button_save.r_override_width()),
            (button_reset, button_reset.r_override_width())]
        if title_buttons is not None:
            for e in title_buttons:
                o = ButtonFnFreeSize(None, e[0], e[1], button_font_size, button_h)
                title_button.append((o, o.r_override_width()))

        super().__init__(w=w,
            pos = (LL - d0, TT + d0),
            size = (RR - LL + d0x2, TT - BB + d0x2),
            use_titlebar = True,
            protect_pos = True,
            killevt = killevt,
            input_text = input_text,
            row_count = row_count,
            font_id = FONT1  if font_id is None else font_id,
            title = title,
            title_button = title_button
        )

        self.data['input_text'] = input_text
        self.child_head = self.areas[0].to_modal_dd(select_all=False, modal_type="i_modal_dd_editor_protect")
        #|
    def init(self, boxes, blfs):

        #|
        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        size_x, size_y = init['size']

        a0 = AreaStringXY(self,
            input_text = init['input_text'],
            font_id = init['font_id'])
        a0.upd_size(L, L + size_x, T - size_y, T)
        self.areas = [a0]
        #|

    def fin_callback(self):

        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        data.clear()
        #|
    def bufn_save(self):

        self.areas[0].kill_push_timer()

        if self.save_confirm_message:
            DropDownYesNo(self, MOUSE, self.set_state_to_confirm_and_check, input_text=self.save_confirm_message)
        else:
            self.set_state_to_confirm_and_check()
        #|
    def bufn_reset(self):

        Admin.REDRAW()
        a0 = self.areas[0]
        a0.evt_select_all()
        a0.beam_input(self.r_default_value())
        a0.kill_push_timer()
        #|
    def set_state_to_confirm_and_check(self):
        exc = self.confirm_fn(self.areas[0].tex.as_string())
        if exc:
            DropDownOk(self, MOUSE, input_text=f'{exc}', width_fac=3.0)
        else:
            self.areas[0].evt_cancel()
        #|
    def fin_from_area(self):
        if self.data['input_text'] == self.areas[0].tex.as_string(): self.areas[0].evt_cancel()
        else:
            DropDownYesNo(self, MOUSE, self.areas[0].evt_cancel,
                input_text="\n    There are unsaved changes.\n    Do you want to close?")
        #|
    #|
    #|
class DropDownEnum(DropDownRM):
    __slots__ = 'write_text', 'adaptive_input'

    def __init__(self, w, LRBT, title,
                items = None,
                input_text = "",
                fixed_width = False,
                write_text = None,
                get_icon = None,
                get_info = None):

        self.write_text = write_text
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        pos = (LRBT[0] - d0, LRBT[3] + d0 + SIZE_title[1])
        size_x = LRBT[1] - LRBT[0] + d0x2  if fixed_width else None

        if items != None:
            if items:
                if hasattr(w, "get"):
                    if hasattr(items, "find"):
                        index = items.find(w.get())
                    else:
                        index = find_index_attr(items, w.get(), "name")
                else:
                    index = -1
            else:
                items = [Name("")]
                index = -1
        elif hasattr(w, "rna") and hasattr(w.rna, "enum_items"):
            if w.rna.enum_items:
                if hasattr(w.rna.enum_items[0], "identifier"):
                    items = [IdentifierNameValue(e.identifier, e.name, None)  for e in w.rna.enum_items]
                else:
                    items = [Name(e.name)  for e in w.rna.enum_items]

                if hasattr(w.rna.enum_items, "find"):
                    index = w.rna.enum_items.find(w.get())
                else:
                    index = find_index_attr(w.rna.enum_items, w.get(), "name")
            else:
                items = [Name("")]
                index = -1
        else:
            items = [Name("")]
            index = -1

        size_y = min(LRBT[3] - REGION_DATA.B - SIZE_tb[0],
            d0x2 + d1 + (SIZE_filter[2] + SIZE_border[3]) * 2 + (len(items) + 1) * D_SIZE['widget_full_h'])

        super().__init__(w, pos, items, size_x=size_x, size_y=size_y, title=title, input_text=input_text,
            get_icon=get_icon, get_info=get_info)
        if index != -1:
            self.areas[0].filt.set_active_index(index)
        #|

    def fin_callback(self):

        #|
        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        if data["use_text_output"] != None:

            if data["use_text_output"]:
                tx = self.areas[0].blf_text.unclip_text
                adaptive_enum_input = P.adaptive_enum_input
                if hasattr(self, "adaptive_input"):
                    if self.adaptive_input is True:
                        adaptive_enum_input = True
                    elif self.adaptive_input is False:
                        adaptive_enum_input = False
                if adaptive_enum_input:
                    if tx.strip():
                        if data["best_item"] != None:
                            tx = data["best_item"].name
            else:
                if data["best_item"] == None:
                    tx = self.areas[0].blf_text.unclip_text
                else:
                    tx = data["best_item"].name

            w = self.w
            if hasattr(w, "rna") and hasattr(w.rna, "enum_items"): write_fn = self.write_enum
            else: write_fn = self.write_string

            try:
                if self.write_text == None: write_fn(tx)
                else: self.write_text(tx, data["best_item"], data["use_text_output"])
            except: report("Value Error")

        data.clear()
        #|

    def write_string(self, tx):
        self.w.set(tx)
        #|
    def write_enum(self, tx):
        rna = self.w.rna
        if tx.startswith(";") and tx.strip() == "None":
            self.w.set(None)
            return

        self.w.set(tx)
        #|
    #|
    #|
class DropDownEnumRename(DropDownEnum):
    __slots__ = ()

    def __init__(self, w, LRBT, base_ob, ob, items=None, fixed_width=True, is_report=True, write_callback=None):
        s = r_library_or_override_message(base_ob)
        if s:
            if is_report: report(s)
            return
        if not hasattr(ob, "name"): return

        L, R, B, T = LRBT
        T += SIZE_border[3]
        B -= SIZE_border[3]

        cls_name = ob.__class__.__name__
        if cls_name not in D_cls_blendData:
            cls = ob.__class__
            if hasattr(cls, "__bases__") and cls.__bases__:
                cls_name = cls.__bases__[0].__name__

        if cls_name in D_cls_blendData:
            items = getattr(bpy.data, D_cls_blendData[cls_name])
            get_icon = r_get_icon_blendData_subtype(cls_name)
            if cls_name == "Object":
                get_info = getinfo_Object
            else:
                get_info = get_info_users
        else:
            if isinstance(ob, bpy.types.Modifier):
                if not hasattr(base_ob, "modifiers"): return

                if hasattr(ob, "is_override_data") and ob.is_override_data:
                    if hasattr(base_ob, "override_library") and base_ob.override_library:
                        if is_report: report("Overridden data-blocks names are not editable")
                        return

                items = base_ob.modifiers
                get_icon = geticon_Modifier
                get_info = get_info_users
            elif isinstance(ob, bpy.types.DriverVariable):
                get_icon = geticon_DriverVar
                get_info = None
            else:

                s = r_unsupport_override_message(base_ob)
                if s:
                    if is_report: report(s)
                    return
                get_icon = None
                get_info = None

        def write_text(tx, best_item, use_text_output):
            if use_text_output or best_item == None:
                ob.name = tx
            else:
                ob.name = best_item.name

            update_scene_push("Data-Block Rename")
            if write_callback is not None: write_callback()

        self.adaptive_input = False
        super().__init__(w, (L, R, B, T), f"Rename {ob.name}", items,
            input_text = ob.name,
            fixed_width = fixed_width,
            write_text = write_text,
            get_icon = get_icon,
            get_info = get_info)
        #|
    #|
    #|
class DropDownEnumPointer(DropDownRM):
    __slots__ = 'preview_cache'

    def __init__(self, w, LRBT, title, all_objects,
                allow_types = None,
                r_except_objects = None,
                items = None,
                input_text = "",
                fixed_width = False,
                get_icon = None,
                get_info = None):

        except_objects = set()  if r_except_objects == None else r_except_objects()
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        pos = (LRBT[0] - d0, LRBT[3] + d0 + SIZE_title[1])
        size_x = LRBT[1] - LRBT[0] + d0x2  if fixed_width else None

        if allow_types == None:
            items = [ob  for ob in all_objects  if ob not in except_objects]
        else:
            items = [ob  for ob in all_objects  if ob.type in allow_types and ob not in except_objects]

        if items:
            if hasattr(items, "find"):
                index = items.find(w.get())
            else:
                index = find_index(items, w.get())
        else:
            items = [Name("")]
            index = -1
            get_icon = None

        size_y = min(LRBT[3] - REGION_DATA.B - SIZE_tb[0],
            d0x2 + d1 + (SIZE_filter[2] + SIZE_border[3]) * 2 + (len(items) + 1) * D_SIZE['widget_full_h'])

        super().__init__(w, pos, items,
            size_x = size_x,
            size_y = size_y,
            title = title,
            input_text = input_text,
            get_icon = get_icon,
            get_info = get_info_users,
            area0_cls = AreaFilterYDropDownEnumPointer)

        a0 = self.areas[0]
        if index != -1:
            a0.filt.set_active_index(index)

        a0.filt.rm_items.append(("dd_preview", a0.evt_filt_preview))
        #|

    def fin_callback(self):

        #|
        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        if data["use_text_output"] != None:

            if data["use_text_output"]:
                ob = None
                tx = self.areas[0].blf_text.unclip_text

                if P.adaptive_enum_input:
                    if tx.strip():
                        if data["best_item"] != None:
                            ob = data["best_item"]

                if ob is None:
                    objects = self.areas[0].filt.items
                    ob = objects[tx]  if tx in objects else tx
            else:
                ob = data["best_item"]

            try: self.w.set(ob)
            except: report("Value Error")

        data.clear()
        if hasattr(self, "preview_cache"): self.preview_cache.kill()
        #|
    #|
    #|
class DropDownEnumTexture(DropDownEnumPointer):
    __slots__ = ()

    def __init__(self, w, LRBT, title, all_objects,
                allow_types = None,
                r_except_objects = None,
                items = None,
                input_text = "",
                fixed_width = False):

        super().__init__(w, LRBT, title, all_objects,
            allow_types = allow_types,
            r_except_objects = r_except_objects,
            items = items,
            input_text = input_text,
            fixed_width = fixed_width,
            get_icon = None,
            get_info = get_info_users)
        #|

    #|
    #|
class DropDownEnumImage(DropDownEnumPointer):
    __slots__ = ()

    def __init__(self, w, LRBT, title, all_objects,
                allow_types = None,
                r_except_objects = None,
                items = None,
                input_text = "",
                fixed_width = False):

        if not all_objects: get_icon = None
        elif P.prop_image_dd_showicon:
            self.preview_cache = PreviewCache(self, bpy.data.images)
            get_icon = self.preview_cache.get_icon
        else:
            get_icon = None

        super().__init__(w, LRBT, title, all_objects,
            allow_types = allow_types,
            r_except_objects = r_except_objects,
            items = items,
            input_text = input_text,
            fixed_width = fixed_width,
            get_icon = get_icon,
            get_info = get_info_users)
        #|

    #|
    #|
class DropDownEnumMaterial(DropDownEnumPointer):
    __slots__ = ()

    def __init__(self, w, LRBT, title, all_objects,
                allow_types = None,
                r_except_objects = None,
                items = None,
                input_text = "",
                fixed_width = False):

        # self.preview_cache = PreviewCacheMaterial(self, bpy.data.materials)

        super().__init__(w, LRBT, title, all_objects,
            allow_types=allow_types,
            r_except_objects=r_except_objects,
            items=items,
            input_text=input_text,
            fixed_width=fixed_width,
            get_icon=None,
            get_info=get_info_users)
        #|

    #|
    #|

class DropDownValTab(DropDown):
    __slots__ = ()

    def __init__(self, w, block0, title="Calculator Tabs"):
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        box_text = block0.box_text
        blf_text = block0.blf_text
        filt = block0.filt

        size = ((box_text.R - box_text.L) * 2,
            d0x2 + d1 + (SIZE_filter[2] + SIZE_border[3]) * 2 + max(SIZE_filter[0], D_SIZE['widget_full_h']))

        super().__init__(w=w,
            pos = (box_text.L - d0, box_text.T + SIZE_title[1] + d0),
            size = size,
            use_titlebar = True,
            title = title,
            input_text = blf_text.unclip_text,
            items = filt.items)

        a = self.areas[0]
        self.child_head = a.to_modal_dd()
        a.evt_toggle_match_case(None, filt.match_case)
        a.evt_toggle_match_whole_word(None, filt.match_whole_word)
        a.evt_toggle_match_end(None, filt.match_end)
        #|
    def init(self, boxes, blfs):

        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        items = init['items']
        size_x, size_y = init['size']

        self.areas = [AreaFilterY(self, L, L + size_x, T - size_y, T, lambda: items,
            is_dropdown=True, input_text=init['input_text'])]
        #|

    def fin_callback(self):

        data = self.data

        if data["use_text_output"] != None:

            filt = self.areas[0].filt
            blf_text = self.areas[0].blf_text
            area_tab = self.w.w.area_tab
            area_tab.filt.match_end = filt.match_end
            area_tab.filt.match_whole_word = filt.match_whole_word
            area_tab.filt.match_case = filt.match_case

            area_tab.evt_area_del_text()
            area_tab.evt_area_paste(blf_text.unclip_text)
            area_tab.blf_text.text = ""

        self.w.set_active_index_callback()
        #|
    #|
    #|
class DropDownVal(DropDown):
    __slots__ = 'area_textbox', 'area_display', 'area_button', 'area_tab', 'same_as_py_value', 'text_format'

    def __init__(self, w, LRBT, tx, py_val, rna, array_range=None, tab="Int"):

        # ref_DropDown
        self.same_as_py_value = True
        self.text_format = w.text_format  if hasattr(w, "text_format") else None

        if isinstance(rna.hard_min  if hasattr(rna, "hard_min") else rna.min_value, int):
            input_text = value_to_display(py_val)
        else:
            rna_unit = rna.unit  if hasattr(rna, "unit") else D_gn_subtype_unit[rna.subtype]
            unit_factor = r_unit_factor(rna_unit, self.text_format)
            if unit_factor != 1.0:
                self.same_as_py_value = False
                py_val /= unit_factor

            input_text = value_to_display(py_val)
            if rna_unit == "ROTATION":
                tab = "Radians"  if unit_factor == 1.0 else "Degrees"
            else:
                tab = "Float"

        blfs = []

        self.u_draw = self.i_draw
        self.w = w
        self.data = {
            "rna": rna,
            "array_range": array_range,
            "text_format": self.text_format
        }
        self.scissor = Scissor()
        is_autoclose = False

        title = rna.name
        if array_range != None: title += f" [{array_range.start} : {array_range.stop}]"
        evt = Admin.EVT
        LL, RR, BB, TT = LRBT
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        rim_d = SIZE_dd_border[2]
        d0x2 = d0 + d0

        title_B = - SIZE_title[1]
        # R, B = kw["size"]
        R = d0x2 + RR - LL
        B = title_B - 999
        ex_width = SIZE_widget[0] * 5 + SIZE_border[3] * 2
        R += ex_width

        if isinstance(title, str):
            title_y = title_B + D_SIZE['font_dd_title_dy']
            title_x = D_SIZE['font_dd_title_dx']
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_dd_title'}$)
            blfSize(FONT0, D_SIZE['font_dd_title'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            blfs.append(BlfClip(r_blf_clipping_end(title, title_x, R - title_x
                ), title, title_x, title_y))

        box_win = GpuDropDown(0, R, B, 0, title_B)
        box_rim = GpuDropDownRim(-rim_d, R + rim_d, B - rim_d, rim_d, rim_d)
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

        x = LL - d0
        y = TT + d0 + SIZE_title[1]

        for e in boxes: e.dxy_upd(x, y)
        for e in blfs:
            e.x += x
            e.y += y


        LL = box_win.L
        RR = box_win.R
        TT = box_win.title_B
        B0 = TT - D_SIZE['widget_full_h'] - d0x2
        R0 = RR - ex_width

        a0 = AreaValBox(self, LL, RR, B0, TT, input_text=input_text)
        a1 = AreaBlock1(self, LL, RR, B0, B0, BlockCalcDisplay(None))
        T1 = a1.box_area.B
        a2 = AreaBlock1(self, LL, R0, T1, T1, BlockCalcButton(None))
        B = a2.box_area.B
        a3 = AreaFilterY(self, R0, RR, B, T1, lambda: ITEMS_CALC_TAB)
        a3.filt.set_active_index_callback = a0.set_active_index_callback
        self.area_textbox = a0
        self.area_display = a1
        self.area_button = a2
        self.area_tab = a3
        self.areas = [a0, a1, a2, a3]

        box_win.B = B
        box_rim.B = B - rim_d
        box_shadow.B = B + SIZE_dd_shadow_offset[2]
        self.scissor.LRBT(LL, RR, B, box_win.title_B)
        self.dxy(*r_full_protect_dxy(box_rim.L, box_rim.R, box_rim.B, box_rim.T))

        filt = a3.filt
        filt.r_upd_scroll()()

        W_HEAD.append(self)
        W_DRAW.append(self)

        Admin.REDRAW()
        Admin.TAG_CURSOR = 'DEFAULT'
        kill_evt()

        self.child_head = a0.to_modal_dd()
        e = list(filter(lambda e: e.name == tab, a3.filt.items))
        if e: a3.filt.set_active_index(e[0].value)
        blockblsubwindows()
        #|

    def modal(self): pass

    def fin_callback(self):

        #|
        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        if hasattr(self.w, "active_index"): self.w.active_index = None

        if data["use_text_output"] != None:

            out = self.area_textbox.calc_text() # py value
            if isinstance(out, str):
                if out.startswith("#"):
                    array_range = data["array_range"]
                    try:
                        if array_range == None:
                            self.w.set(out)
                        else:
                            self.w.set([out] * len(array_range), (array_range.start, array_range.stop))
                    except:
                        report("Fail to Add Driver")
                else:
                    report(out)
            else:
                rna = data["rna"]
                array_range = data["array_range"]
                try:
                    if hasattr(rna, "hard_min"):
                        hard_min = rna.hard_min
                        hard_max = rna.hard_max
                    else:
                        hard_min = rna.min_value
                        hard_max = rna.max_value
                    v = min(max(hard_min, out), hard_max)
                    if array_range == None:
                        self.w.set(v)
                    else:
                        self.w.set([v] * len(array_range), (array_range.start, array_range.stop))
                except:
                    report("Value Error")
        #|
    #|
    #|




class DropDownBuColor(DropDown):
    __slots__ = (
        'color_value',
        'hsv',
        'hex',
        'hex_str',
        'button_rgb',
        'button_hsv',
        'button_hex_str',
        'hex_format',
        'hue_size',
        'color_space',
        'update_modal')

    def __init__(self, w):
        box_button = w.box_button.copy()
        box_button.color_rim = [0.0, 0.0, 0.0, 0.0]
        color_space = w.color_space
        self.color_space = color_space

        title = f"{color_space}  |  {w.rna.name}"
        self.hex_format = getattr(com, f'rs_format_hex_{P.format_hex}', com.rs_format_hex_UPPERCASE_SEPARATOR)

        rgb = w.get()
        self.color_value = rgb
        self.hsv = list(rgb_to_hsv(max(0.0, rgb[0]), max(0.0, rgb[1]), max(0.0, rgb[2])))
        self.hex = [0.0, 0.0, 0.0]
        self.hex_str = ""
        L, R, B, T = box_button.r_LRBT()
        d0 = SIZE_dd_border[0]
        widget_rim = SIZE_border[3]
        outer = (d0 + widget_rim) * 2
        a1_width = SIZE_block[2] * 2 + D_SIZE['widget_width'] + D_SIZE['widget_full_h']
        size_y = outer + max(SIZE_block[2] * 2 + SIZE_button[3], 8 * D_SIZE['widget_full_h'])
        size_x = a1_width + size_y + SIZE_button[2] + (widget_rim + SIZE_button[1]) * 2 + SIZE_widget[0] + SIZE_widget[0] // 4
        if hasattr(w, "bufn_keyframe"): size_x += SIZE_widget[0]
        pos = (R + d0 - size_x, T + d0)

        super().__init__(w=w, pos=pos, size=(size_x, size_y), use_titlebar=True, title=title,
            box_button=box_button, a1_width=a1_width)

        self.data["is_confirm"] = False
        #|
    def init(self, boxes, blfs):

        init = DropDown.INIT_DATA
        data = self.data
        d0 = SIZE_dd_border[0]
        LL, RR, BB, TT = self.box_win.r_LRBT()
        Tt = self.box_win.title_B
        size_x, size_y = init['size']
        h = SIZE_widget[0]

        self_hex = self.hex
        self_hsv = self.hsv
        rgb = self.color_value
        hex_format = self.hex_format
        color_space = self.color_space

        def modal_drag_H_callback(fac):
            button_hsv_set(fac, 0)
            #|
        def button_rgb_update_callback():
            button_hsv.callback_enable = False
            button_hsv_set(rgb_to_hsv(max(0.0, rgb[0]), max(0.0, rgb[1]), max(0.0, rgb[2])), (0, 3))
            self_hex[:] = r_media_rgb255(rgb)

            self.hex_str = hex_format(self_hex)
            button_hex_str_blf_value.text = self.hex_str
            update_button_media(rgb_to_hsv(self_hex[0] / 255.0, self_hex[1] / 255.0, self_hex[2] / 255.0))
            button_hsv.callback_enable = True
            #|
        def button_hsv_update_callback():
            u.callback_enable = False
            u.set(hsv_to_rgb(*self_hsv), (0, 3))
            self_hex[:] = r_media_rgb255(rgb)
            self.hex_str = hex_format(self_hex)
            button_hex_str_blf_value.text = self.hex_str
            hsv = rgb_to_hsv(self_hex[0] / 255.0, self_hex[1] / 255.0, self_hex[2] / 255.0)
            if hsv[1] == 0.0:
                update_button_media((self.hsv[0], hsv[1], hsv[2]))
            else:
                update_button_media(hsv)
            u.callback_enable = True
            #|
        if color_space == "Scene Linear":
            def r_media_rgb255(rgb01):
                return (
                    scene_linear_to_hex(rgb01[0]),
                    scene_linear_to_hex(rgb01[1]),
                    scene_linear_to_hex(rgb01[2]),
                )
                #|

            def modal_drag_SV_callback(fac_x, fac_y):
                l = hsv_to_rgb(self_hsv[0], fac_x, fac_y)

                u_set(
                    [
                        L_rgb_to_scene_linear[min(max(0, round(l[0] * 255.0)), 255)],
                        L_rgb_to_scene_linear[min(max(0, round(l[1] * 255.0)), 255)],
                        L_rgb_to_scene_linear[min(max(0, round(l[2] * 255.0)), 255)]],
                    (0, 3))
                #|

            def set_callfront_hex_str(s):
                if len(s) < 6: s = "0" * (6 - len(s)) + s
                r = int(s[0 : 2], 16)
                g = int(s[2 : 4], 16)
                b = int(s[4 : 6], 16)

                u_set(
                    [L_rgb_to_scene_linear[r], L_rgb_to_scene_linear[g], L_rgb_to_scene_linear[b]],
                    (0, 3))
                return True
                #|
        elif color_space == "GPU Shader":
            def r_media_rgb255(rgb01):
                return (
                    glc_to_hex(rgb01[0]),
                    glc_to_hex(rgb01[1]),
                    glc_to_hex(rgb01[2]),
                )
                #|

            def modal_drag_SV_callback(fac_x, fac_y):
                l = hsv_to_rgb(self_hsv[0], fac_x, fac_y)

                u_set([
                    L_rgb_to_glc[min(max(0, round(l[0] * 255.0)), 255)],
                    L_rgb_to_glc[min(max(0, round(l[1] * 255.0)), 255)],
                    L_rgb_to_glc[min(max(0, round(l[2] * 255.0)), 255)]], (0, 3))
                #|

            def set_callfront_hex_str(s):
                if len(s) < 6: s = "0" * (6 - len(s)) + s
                r = int(s[0 : 2], 16)
                g = int(s[2 : 4], 16)
                b = int(s[4 : 6], 16)

                u_set([L_rgb_to_glc[r], L_rgb_to_glc[g], L_rgb_to_glc[b]], (0, 3))
                return True
                #|
        else:
            def r_media_rgb255(rgb01):
                return (
                    min(max(0, round(rgb01[0] * 255)), 255),
                    min(max(0, round(rgb01[1] * 255)), 255),
                    min(max(0, round(rgb01[2] * 255)), 255),
                )
                #|

            def modal_drag_SV_callback(fac_x, fac_y):
                u_set(hsv_to_rgb(self_hsv[0], fac_x, fac_y), (0, 3))
                #|

            def set_callfront_hex_str(s):
                if len(s) < 6: s = "0" * (6 - len(s)) + s
                r = int(s[0 : 2], 16)
                g = int(s[2 : 4], 16)
                b = int(s[4 : 6], 16)

                u_set([r / 255.0, g / 255.0, b / 255.0], (0, 3))
                return True
                #|

        self_hex[:] = r_media_rgb255(rgb)
        self.hex_str = hex_format(self_hex)

        L0 = RR - init['a1_width']
        a0 = AreaColorHue(self, LL, L0, BB, Tt, modal_drag_H_callback, modal_drag_SV_callback)
        a1 = AreaBlockSimple(self, L0, RR, BB, Tt)
        a1b0 = BlockR(a1)

        w = self.w
        rna = w.rna
        r_pp = w.r_pp

        #
        array_length = rna.array_length

        if w.ui_anim_data is None:
            ui_anim_data = None
        else:
            r_dph = w.ui_anim_data.r_dph
            r_pp_ref = w.ui_anim_data.r_pp_ref
            rnas = w.ui_anim_data.rnas
            ui_anim_data = UiAnimData(r_pp, r_pp_ref, r_dph, rnas)

        if hasattr(self.w, "identifier_escape"):
            u = (BuGnFloatVecColor  if rna.is_animatable else BuGnFloatVecColorNoAnim)(
                w.w, rna, r_pp, ui_anim_data, "", False)
            u.identifier_escape = f'["{u.identifier}"]'

            if ui_anim_data is not None:
                ui_anim_data.props[(u.identifier, )] = u
        else:
            u = (BuFloatVecColor  if rna.is_animatable else BuFloatVecColorNoAnim)(
                w.w, rna, r_pp, ui_anim_data, "", False)

            if ui_anim_data is not None:
                ui_anim_data.props[u.identifier] = u

        u.init_subtype_dimen("RGBA", "XXXX")
        u.init_bat = u.init_bat_anim_L
        u.step = 1
        self.button_rgb = u
        #

        u.update_callback = button_rgb_update_callback
        u.callback_enable = True
        u_set = u.set

        button_hsv = BuFloatVecColorNoAnim(a1b0, RNA_hsv, lambda: self, None, "", False)
        button_hsv.init_subtype_dimen(TUP_HSV, "XXX")
        button_hsv.init_bat = button_hsv.init_bat_anim_L
        button_hsv.update_callback = button_hsv_update_callback
        button_hsv.callback_enable = True
        button_hsv_set = button_hsv.set

        button_hex_str = ButtonStringColorHex(a1b0, RNA_hex_str_glc, self, subtype_override=TUP_HEX)
        button_hex_str.set_callfront = set_callfront_hex_str
        button_hex_str_set = button_hex_str.set
        button_hex_str_blf_value = button_hex_str.blf_value

        self.button_hsv = button_hsv
        self.button_hex_str = button_hex_str

        a1b0.buttons = [
            u,
            ButtonSep(),
            button_hsv,
            ButtonSep(),
            button_hex_str,
            ButtonSep(),
            ButtonFnImg(a1b0, RNA_eyedropper, self.bufn_eyedropper, 'GpuImg_eyedropper')
        ]
        self.areas = [a0, a1]
        self.hue_size = max(a1b0.r_height(0), SIZE_button[3])

        a1.items.append(a1b0)
        a1.box_area.L -= h
        a1.box_area.upd()
        a1.box_region.L -= h
        a1.box_region.upd()
        a1.init_draw_range()
        a0.box_area.R -= h
        a0.box_area.upd()

        # if SIZE_title[1] > d0 + d0:
        box_button = init['box_button']
        data['box_button'] = box_button
        data['input_color'] = tuple(self.color_value)
        box_button.B = Tt + d0
        box_button.T = TT - d0
        box_button.R = RR - d0
        box_button.L = a1b0.buttons[0].box_button.L
        box_button.upd()

        if hasattr(self.w, "identifier_escape"):
            title_button = BuGnColor(self, rna, r_pp, None, "", False, color_space)
        else:
            title_button = BuColor(self, rna, r_pp, None, "", False, color_space)
        title_button.box_button = box_button
        title_button.color_value[:] = w.color_value

        if hasattr(w, "box_grid"):
            box_grid = w.box_grid.copy()
            box_rgb = w.box_rgb.copy()
            data['box_grid'] = box_grid
            data['box_rgb'] = box_rgb

            B = box_button.inner[2]
            T = box_button.inner[3]
            cx = box_button.r_center_x()
            box_grid.B = B
            box_grid.T = T
            box_grid.L = cx
            box_grid.R = box_button.inner[1]
            box_rgb.B = B
            box_rgb.T = T
            box_rgb.L = box_button.inner[0]
            box_rgb.R = cx
            box_grid.upd()
            box_rgb.upd()

            w_boxes = [box_grid, box_button, box_rgb]
            title_button.box_grid = box_grid
            title_button.box_rgb = box_rgb
        else:
            w_boxes = [box_button]

        boxes += w_boxes

        update_button_media = a0.update_button_media
        update_button_media(rgb_to_hsv(self.hex[0] / 255.0, self.hex[1] / 255.0, self.hex[2] / 255.0))

        color_value = self.color_value

        if ui_anim_data is None:
            @ noRecursive
            def upd_data():
                u.upd_data()

                if list(color_value) == title_button.color_value: pass
                else:

                    title_button.color_value[:] = color_value
                    title_button.set_box_color(color_value)
        else:
            @ noRecursive
            def upd_data():
                block.FRAME_CURRENT = bpy.context.scene.frame_current
                ui_anim_data.update_with(N1)

                if list(color_value) == title_button.color_value: pass
                else:

                    title_button.color_value[:] = color_value
                    title_button.set_box_color(color_value)

        self.update_modal = UpdateModal(upd_data)
        W_MODAL.insert(-1, self.update_modal)
        upd_data()
        u.blf_title.text = ""
        button_hsv.blf_title.text = ""
        #|

    def evt_click_outside(self): self.evt_dd_confirm()
    def evt_dd_confirm(self):
        self.data["is_confirm"] = True
        self.fin()
        #|

    def fin_callback(self):
        kill_evt()
        if hasattr(self, "update_modal"):
            W_MODAL.remove(self.update_modal)


        data = self.data
        finalvalue = list(self.w.get())

        if "fin_callfront" in data: data["fin_callfront"]()

        if data["is_confirm"]:

            self.w.set(finalvalue, (0, len(data["input_color"])), undo_push=data["input_color"])
        else:

            self.w.set(data["input_color"], (0, len(data["input_color"])), undo_push=False)
        #|

    def bufn_eyedropper(self):

        _REDRAW = Admin.REDRAW
        _REDRAW()
        kill_evt_except()
        _end_trigger0 = TRIGGER['esc']
        _end_trigger1 = TRIGGER['dd_esc']
        trigger_confirm0 = TRIGGER['click']
        trigger_confirm1 = TRIGGER['dd_confirm']
        _EVT_TYPE = EVT_TYPE

        LL = REGION_DATA.L
        RR = REGION_DATA.R
        BB = REGION_DATA.B + SIZE_tb[0]
        TT = REGION_DATA.T
        full_h = D_SIZE['widget_full_h']
        h = SIZE_widget[0]
        wi = D_SIZE['widget_width']
        widget_rim = SIZE_border[3]
        depth = full_h // 3
        box_bg = GpuRim(COL_box_val, COL_box_val_rim, d=widget_rim)
        box_color = GpuBox([0.0, 0.0, 0.0, 1.0])
        blf_hex = BlfColor(color=COL_box_val_fg)
        hex_format = self.hex_format

        box_bg_bind_draw = box_bg.bind_draw
        box_color_bind_draw = box_color.bind_draw
        _FONT0 = FONT0
        _D_SIZE_font_main = D_SIZE['font_main']
        _D_SIZE_font_main_dx = D_SIZE['font_main_dx']
        _D_SIZE_font_main_dy = D_SIZE['font_main_dy']

        # /* 0dd_bufn_eyedropper_box
        if LL <= MOUSE[0] < RR and BB <= MOUSE[1] < TT:
            R = MOUSE[0] + full_h + wi
            if R > RR: R = MOUSE[0] - full_h
            L = R - wi
            T = BB + full_h  if MOUSE[1] < BB + full_h else MOUSE[1]
            B = T - full_h
        else:
            L = min(max(MOUSE[0] + depth, LL), RR - wi)
            R = L + wi
            T = min(max(MOUSE[1] + depth, BB + full_h), TT)
            B = T - full_h

        box_bg.L = L
        box_bg.R = R
        box_bg.B = B
        box_bg.T = T
        box_bg.upd()
        L0, R0, B0, T0 = box_bg.inner
        box_color.LRBT_upd(L0, L0 + h, B0, T0)

        r, g, b = active_framebuffer_get().read_color(*MOUSE_WINDOW, 1, 1, 3, 0, 'UBYTE').to_list()[0][0]
        r = min(max(0, r), 255)
        g = min(max(0, g), 255)
        b = min(max(0, b), 255)
        box_color.color[0 : 3] = L_rgb_to_glc[r], L_rgb_to_glc[g], L_rgb_to_glc[b]
        blf_hex.text = "# " + hex_format([r, g, b])
        if r in D_glc_null or g in D_glc_null or b in D_glc_null:
            blf_hex.color = COL_box_val_fg_error
        else:
            blf_hex.color = COL_box_val_fg
        blf_hex.x = box_color.R + _D_SIZE_font_main_dx
        blf_hex.y = B0 + _D_SIZE_font_main_dy
        # */

        def _modal():
            _REDRAW()
            if (_EVT_TYPE[0] == 'ESC' and _EVT_TYPE[1] == 'PRESS') or _end_trigger0() or _end_trigger1():
                w_head.fin()
                return

            # <<< 1copy (0dd_bufn_eyedropper_box,, $$)
            if LL <= MOUSE[0] < RR and BB <= MOUSE[1] < TT:
                R = MOUSE[0] + full_h + wi
                if R > RR: R = MOUSE[0] - full_h
                L = R - wi
                T = BB + full_h  if MOUSE[1] < BB + full_h else MOUSE[1]
                B = T - full_h
            else:
                L = min(max(MOUSE[0] + depth, LL), RR - wi)
                R = L + wi
                T = min(max(MOUSE[1] + depth, BB + full_h), TT)
                B = T - full_h

            box_bg.L = L
            box_bg.R = R
            box_bg.B = B
            box_bg.T = T
            box_bg.upd()
            L0, R0, B0, T0 = box_bg.inner
            box_color.LRBT_upd(L0, L0 + h, B0, T0)

            r, g, b = active_framebuffer_get().read_color(*MOUSE_WINDOW, 1, 1, 3, 0, 'UBYTE').to_list()[0][0]
            r = min(max(0, r), 255)
            g = min(max(0, g), 255)
            b = min(max(0, b), 255)
            box_color.color[0 : 3] = L_rgb_to_glc[r], L_rgb_to_glc[g], L_rgb_to_glc[b]
            blf_hex.text = "# " + hex_format([r, g, b])
            if r in D_glc_null or g in D_glc_null or b in D_glc_null:
                blf_hex.color = COL_box_val_fg_error
            else:
                blf_hex.color = COL_box_val_fg
            blf_hex.x = box_color.R + _D_SIZE_font_main_dx
            blf_hex.y = B0 + _D_SIZE_font_main_dy
            # >>>

            if trigger_confirm0() or trigger_confirm1():
                w_head.data["is_confirm"] = True
                w_head.fin()
                return
            #|
        def _modal_end():

            Admin.TAG_CURSOR = 'DEFAULT'
            W_DRAW.remove(u_draw)

            if w_head.data["is_confirm"]:
                try: self.button_hex_str.set(blf_hex.text)
                except: pass

            kill_evt_except()
            #|
        def _draw():
            blend_set('ALPHA')
            box_bg_bind_draw()
            box_color_bind_draw()

            blfSize(_FONT0, _D_SIZE_font_main)
            blfColor(_FONT0, *blf_hex.color)
            blfPos(_FONT0, blf_hex.x, blf_hex.y, 0)
            blfDraw(_FONT0, blf_hex.text)
            #|

        Admin.TAG_CURSOR = 'EYEDROPPER'
        w_head = Head(self, _modal, _modal_end)
        w_head.data = {"is_confirm": False}
        u_draw = Udraw(_draw)
        W_DRAW.append(u_draw)
        #|
    #|
    #|

class DropDownYesNo(DropDown):
    __slots__ = 'button_yes', 'button_no', 'fn_yes', 'fn_no'

    def __init__(self, w, pos,
                fn_yes = None,
                fn_no = None,
                title = "Confirm Dialog",
                input_text = "Are You Confirm?",
                text_yes = "Yes",
                text_no = "No",
                font_id = None,
                row_count = 6,
                width_fac = 2.0):

        self.fn_yes = fn_yes
        self.fn_no = fn_no
        RNA_yes.default = text_yes
        RNA_no.default = text_no
        width = round(width_fac * D_SIZE['widget_width'])
        LL = pos[0]
        RR = LL + width
        TT = pos[1]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        line_h = SIZE_widget[0]
        BB = TT - row_count * line_h - SIZE_border[3] * 2
        area_button_h = d1 + d1 + D_SIZE['widget_full_h'] + d0x2

        super().__init__(w=w,
            pos = (LL - d0, TT + d0),
            size = (RR - LL + d0x2, TT - BB + d0x2 + area_button_h),
            use_titlebar = True,
            protect_pos = True,
            killevt = True,
            input_text = input_text,
            row_count = row_count,
            font_id = FONT0  if font_id is None else font_id,
            title = title,
            title_button = [("close", self.fin_from_area)],
            area_button_h = area_button_h)

        self.child_head = self.areas[0].to_modal_dd(select_all=False, modal_type="i_modal_dd_editor_protect")
        #|
    def init(self, boxes, blfs):

        #|
        init = DropDown.INIT_DATA
        size_x, size_y = init['size']
        L = self.box_win.L
        R = L + size_x
        T = self.box_win.title_B
        B = T - size_y + init['area_button_h']

        a0 = AreaStringXY(self,
            input_text = init['input_text'],
            font_id = init['font_id'])
        a0.upd_size(L, R, B, T)
        self.areas = [a0]

        button_yes = ButtonFn(self, RNA_yes, self.bufn_yes)
        button_no = ButtonFn(self, RNA_no, self.fin_from_area)
        self.button_yes = button_yes
        self.button_no = button_no
        boxes.append(button_yes.box_button)
        boxes.append(button_no.box_button)
        blfs.append(button_yes.blf_value)
        blfs.append(button_no.blf_value)

        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        B -= SIZE_dd_border[0] + d1
        L += d0 + widget_rim
        R -= d0 + widget_rim
        button_width = (R - L - d0 - d1) // 2
        button_yes.init_bat(L, L + button_width, B)
        button_no.init_bat(R - button_width, R, B)
        #|

    def fin_from_area(self): self.areas[0].evt_cancel()
    def fin_callback(self):
        data = self.data

        if "fin_callfront" in data: data["fin_callfront"]()

        if "is_confirm" in data and data["is_confirm"]:

            if self.fn_yes != None: self.fn_yes()
        else:

            if self.fn_no != None: self.fn_no()

        data.clear()
        #|
    def bufn_yes(self):

        self.data["is_confirm"] = True
        self.fin_from_area()
        #|

    def basis_win_evt_protect(self):
        e = None
        if self.button_yes.inside(MOUSE): e = self.button_yes
        elif self.button_no.inside(MOUSE): e = self.button_no
        else:
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
    #|
    #|
class DropDownOk(DropDownYesNo):
    __slots__ = ()

    def __init__(self, w, pos,
                fn_yes = None,
                title = "Dialog",
                input_text = "Ok?",
                text_yes = "OK",
                font_id = None,
                row_count = 6,
                width_fac = 2.0):

        super().__init__(w, pos,
            fn_yes = fn_yes,
            title = title,
            input_text = input_text,
            text_yes = text_yes,
            text_no = "",
            font_id = font_id,
            row_count = row_count,
            width_fac = width_fac)

        self.button_no.box_button.LRBT_upd(0, 0, 0, 0, 0)
        self.button_no.blf_value.x = 0
        self.button_no.blf_value.y = 0
        #|
    #|
    #|
class DropDownInfoUtil(DropDown):
    __slots__ = 'endfn', 'buttons', 'area_items', 'active_tab'

    def __init__(self, w, pos, buttons,
                area_items = None,
                endfn = None,
                title = "Dialog",
                input_text = "",
                font_id = None,
                row_count = 6,
                width_fac = 2.0,
                block_size = 6,
                readonly = False,
                wrap_input = False):

        self.buttons = buttons
        self.area_items = area_items
        self.endfn = endfn
        width = round(width_fac * D_SIZE['widget_width'])
        LL = pos[0]
        RR = LL + width
        TT = pos[1]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        line_h = SIZE_widget[0]
        widget_rim_2 = SIZE_border[3] * 2
        BB = TT - row_count * line_h - widget_rim_2
        size_x = width + d0x2
        area_width = size_x - d0x2 - widget_rim_2
        button_gap = SIZE_button[1]
        area_button_h = d1 + d1 + d0x2 + sum(e.r_height(area_width) + button_gap  for e in buttons)
        area_block_h = 0  if area_items is None else AreaBlockTab.calc_height_by_len(block_size)
        if font_id is None:
            font_id = FONT0

        if wrap_input:
            blfSize(font_id, D_SIZE['font_main'])
            lines = []
            for line in input_text.split("\n"):
                line_strip = line.lstrip()
                indent = (len(line) - len(line_strip)) * " "
                lines += [f'{indent}{s}'  for s in rl_blf_wrap(line_strip, area_width - blfDimen(font_id, indent)[0])]

            input_text = "\n".join(lines)

        super().__init__(w=w,
            pos = (LL - d0, TT + d0),
            size = (size_x, TT - BB + d0x2 + area_button_h + area_block_h),
            use_titlebar = True,
            protect_pos = True,
            killevt = True,
            input_text = input_text,
            row_count = row_count,
            font_id = font_id,
            title = title,
            title_button = [("close", self.fin_from_area)],
            area_button_h = area_button_h,
            area_block_h = area_block_h)

        a0 = self.areas[0]
        self.child_head = a0.to_modal_dd(select_all=False, modal_type="i_modal_dd_editor_protect")
        a0.readonly = readonly
        #|
    def init(self, boxes, blfs):

        #|
        init = DropDown.INIT_DATA
        size_x, size_y = init['size']
        L = self.box_win.L
        R = L + size_x
        T = self.box_win.title_B
        B = T - size_y + init['area_button_h'] + init['area_block_h']

        a0 = AreaStringXY(self,
            input_text = init['input_text'],
            font_id = init['font_id'])
        a0.upd_size(L, R, B, T)
        self.areas = [a0]

        if self.area_items is not None:
            T = B
            B = T - init['area_block_h']
            a1 = AreaBlockTab(self, L, R, B, T)
            self.areas.append(a1)
            a1.items = self.area_items
            self.active_tab = None
            a1.active_tab = None

        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        B -= SIZE_dd_border[0] + d1
        L += d0 + widget_rim
        R -= d0 + widget_rim
        button_gap = SIZE_button[1]

        for e in self.buttons:
            B = e.init_bat(L, R, B) - button_gap
        #|

    def fin_from_area(self): self.areas[0].evt_cancel()
    def fin_callback(self):
        data = self.data

        if "fin_callfront" in data: data["fin_callfront"]()

        if self.endfn != None: self.endfn(data)

        data.clear()
        #|

    def r_area_tab(self): return self.areas[1]
    def r_area_info(self):
        return self.areas[0].tex.as_string()
        #|
    def set_area_info(self, s, beam_start=False):
        a0 = self.areas[0]
        a0.evt_del_all(undo_push=False, evtkill=False)
        a0.beam_input_unpush(s)
        if beam_start:
            a0.evt_beam_start()
        #|

    def basis_win_evt(self):
        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']():
            return self.areas[0].evt_cancel
        return None
        #|
    def basis_win_evt_protect(self):
        e = None
        for o in self.title_buttons:
            if o.inside(MOUSE):
                e = o
                break
        if e is None:
            for o in self.buttons:
                if o.inside(MOUSE):
                    e = o
                    break

            if self.area_items and e is None and self.areas[1].box_area.inbox(MOUSE):
                e = self.areas[1]

                if self.focus_element != e:
                    if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
                    self.focus_element = e
                    kill_evt_except()

                e.modal()
                return N

        if e is None:
            if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
            self.focus_element = None
        else:
            if self.focus_element != e:
                if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
                self.focus_element = e
                e.inside_evt()
                if hasattr(e, "evtkill") and e.evtkill == False: pass
                else: kill_evt_except()

            e.modal()
            return N

        if self.box_win.inbox(MOUSE) and MOUSE[1] > self.box_win.title_B:
            if TRIGGER['title_move'](): return self.to_modal_move

        if self.areas[0].box_area.inbox(MOUSE): return None
        return N
        #|

    def dxy(self, dx, dy):
        super().dxy(dx, dy)
        for e in self.buttons: e.dxy(dx, dy)
        #|
    def i_draw(self):
        super().i_draw()
        blend_set('ALPHA')
        for e in self.buttons: e.draw_box()
        for e in self.buttons: e.draw_blf()
        #|
    #|
    #|
class DropDownListUtil(DropDown):
    __slots__ = 'endfn', 'area_items', 'active_tab'

    def __init__(self, w, pos, items,
                area_items = None,
                endfn = None,
                get_icon = None,
                get_info = None,
                title = "Menu",
                size_x = None,
                size_y = None,
                input_text = "",
                block_size = 6):

        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        d0x2 = d0 + d0
        button_gap = SIZE_button[1]
        blfSize(FONT0, D_SIZE['font_main'])

        if size_x == None:
            size_x = max(SIZE_widget[0] * 12, min(REGION_DATA.R - REGION_DATA.L,
                SIZE_widget[0] + d0x2 + D_SIZE['font_main_dx'] * 2 + floor(max(
                    blfDimen(FONT0, e.name)[0]  for e in items))))
        if size_y == None:
            size_y = min(REGION_DATA.T - REGION_DATA.B - SIZE_tb[0] - SIZE_title[1],
                d0x2 + d1 + (SIZE_filter[2] + SIZE_border[3]) * 2 + (len(items) + 1) * D_SIZE['widget_full_h'])

        area_block_h = 0  if area_items is None else AreaBlockTab.calc_height_by_len(block_size)

        super().__init__(w=w, pos=pos, size=(size_x, size_y), use_titlebar=True, title=title,
            items=items, get_icon=get_icon, get_info=get_info, input_text=input_text,
            area_block_h = area_block_h)

        self.child_head = self.areas[0].to_modal_dd()
        #|
    def init(self, boxes, blfs):

        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        size_x, size_y = init['size']
        items = init['items']

        B = T - size_y + init['area_block_h']
        R = L + size_x

        self.areas = [AreaFilterY(self, L, R, B, T, lambda: items,
            get_icon = init['get_icon'],
            get_info = init['get_info'],
            input_text = init['input_text'],
            is_dropdown = True)]

        if self.area_items is not None:
            T = B
            B = T - init['area_block_h']
            a1 = AreaBlockTab(self, L, R, B, T)
            self.areas.append(a1)
            a1.items = self.area_items
            self.active_tab = None
            a1.active_tab = None
        #|

    def fin_from_area(self): self.areas[0].evt_cancel()
    def fin_callback(self):

        #|
        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        if data["use_text_output"] != None:

            if data["use_text_output"]:
                if P.adaptive_enum_input:
                    if self.areas[0].blf_text.unclip_text.strip():
                        if data["best_item"] != None: data["best_item"].value()
            else:
                if data["best_item"] != None: data["best_item"].value()

        data.clear()
        #|

    def r_area_tab(self): return self.areas[1]

    def basis_win_evt(self):
        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc']() or TRIGGER['dd_esc']():
            return self.areas[0].evt_cancel
        return None
        #|
    def dd_basis_evt(self):
        if self.areas[1].box_area.inbox(MOUSE) is False: return None
        self.areas[1].modal()
        return N
        #|
    #|
    #|

class DropDownNewModifier(DropDownListUtil):
    __slots__ = 'bpy_object', 'md_lib_method'

    def __init__(self, w, pos, bpy_object):
        self.bpy_object = bpy_object
        self.md_lib_method = P.md_lib_method
        if m.LIBRARY_MODIFIER is None: m.LibraryModifier.ui_refresh_path(report_dialog=False)

        if bpy_object.type not in m.LIBRARY_MODIFIER.types_items: return

        area_items = []
        self.area_items = area_items

        super().__init__(w, pos, m.LIBRARY_MODIFIER.types_items[bpy_object.type],
            area_items = area_items,
            get_icon = self.get_icon,
            get_info = self.get_info,
            title = "Add Modifier",
            size_x = round(D_SIZE['widget_width'] * 2.1),
            size_y = pos[1] - REGION_DATA.B - SIZE_tb[0] - SIZE_title[1],
            block_size = 1)

        area_tab = self.r_area_tab()
        button0 = ButtonEnumXYTemp(None, P.bl_rna.properties["md_lib_method"], self, row_length=3)
        area_items.append(BlockFull(area_tab, button0))
        area_tab.init_items_tab()
        #|

    def get_icon(self, e):
        if hasattr(e, "identifier"):
            if e.identifier in blg.D_geticon_Modifier: return blg.D_geticon_Modifier[e.identifier]()
            return GpuImg_OUTLINER_OB_UNKNOW
        return GpuImg_ID_NODETREE()
        #|
    def get_info(self, e):
        if hasattr(e, "library"):
            if hasattr(e.library, "version") and e.library.version:
                return f'{e.library.filepath}  |  {e.library.version}'
            return e.library.filepath
        return ""
        #|

    def fin_callback(self):

        #|
        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        if data["use_text_output"] != None:

            oj = self.bpy_object
            item = None

            if data["use_text_output"]:
                tx = None
                if P.adaptive_enum_input:
                    if self.areas[0].blf_text.unclip_text.strip():
                        if data["best_item"] != None:
                            tx = data["best_item"].name

                if tx is None:
                    tx = self.areas[0].blf_text.unclip_text
            else:
                if data["best_item"] == None:
                    tx = self.areas[0].blf_text.unclip_text
                else:
                    item = data["best_item"]
                    tx = item.name

            if item is None:
                name_to_item = {e.name: e  for e in self.areas[0].filt.items}
                if tx in name_to_item: item = name_to_item[tx]

            if item is not None:
                cls = self.__class__

                if hasattr(item, "identifier"):
                    if hasattr(item, "library"):
                        success, result = cls.new_md_copy(oj, item.library.filepath, item.library.version, item.name)
                        if success: update_scene_push(f'Add Modifier: {tx}')
                        if result: report(f"Failed. {result}")
                    else:
                        oj.modifiers.new(tx, item.identifier)
                        update_scene_push(f'Add Modifier: {tx}')

                elif hasattr(item, "library"):
                    success, result = cls.new_gn_modifier_with(oj, item.library.filepath, item.name, self.md_lib_method)
                    if success: update_scene_push(f'Add Modifier: {tx}')
                    if result: report(f"Failed. {result}")

        data.clear()
        #|

    @staticmethod
    @ successResult
    def new_gn_modifier_with(oj, file_path, node_name, md_lib_method):
        node_groups = bpy.data.node_groups

        if md_lib_method == "LINK":
            name_tuple = node_name, file_path

            if name_tuple not in node_groups:
                bpy_data_append(file_path, "NodeTree", node_name, link=True)

            node = node_groups[name_tuple]
        else:
            if node_name in node_groups:
                old_node = node_groups[node_name]
                old_node_groups = set(node_groups)
                bpy_data_append(file_path, "NodeTree", node_name, link=False)
                new_node = next(ob  for ob in node_groups  if ob not in old_node_groups)
            else:
                bpy_data_append(file_path, "NodeTree", node_name, link=False)
                new_node = node_groups[node_name]
                old_node = None

            if old_node is not None and md_lib_method == "REUSE":
                # if bl_NodeTree_compare(old_node, new_node):
                #     node = old_node
                #     node_groups.remove(new_node)
                # else:
                #     node = new_node

                node = old_node
                node_groups.remove(new_node)
            else:
                node = new_node

        md = oj.modifiers.new(node_name, "NODES")
        md.node_group = node
        #|

    @staticmethod
    def new_md_copy(oj, file_path, object_name, modifier_name):
        try:
            objects = bpy.data.objects

            if object_name in objects:
                old_objects = set(objects)
                bpy_data_append(file_path, "Object", object_name, link=False)
                new_object = next(ob  for ob in objects if ob not in old_objects)
            else:
                bpy_data_append(file_path, "Object", object_name, link=False)
                new_object = objects[object_name]

            if not hasattr(new_object, "type") or oj.type != new_object.type:
                objects.remove(new_object)
                return False, "Source object type mismatch"
            if not hasattr(new_object, "modifiers") or not new_object.modifiers:
                objects.remove(new_object)
                return False, "Source object has no modifiers"
            if modifier_name not in new_object.modifiers:
                objects.remove(new_object)
                return False, "Source object modifier not found"
            source_md = new_object.modifiers[modifier_name]

            success, fails = ops_mds_copy_to_object(
                new_object, oj, [modifier_name], "COPY", True, True)

            objects.remove(new_object)

            if success: return True, ""
            else: return False, "Cannot copy modifiers from source object"
        except Exception as ex:
            return False, str(ex)
        return True, ""
        #|
    #|
    #|
class DropDownStartMenu(DropDownListUtil):
    __slots__ = ()

    def __init__(self, icon_LRBT):
        L, R, B, T = icon_LRBT
        area_items = []
        self.area_items = area_items
        pos = (L, T + SIZE_widget[0] * 12)

        items = [IdentifierNameValue(k, e.name, None)  for k, e in m.D_EDITOR.items()]
        items.sort(key=lambda e: e.name)

        super().__init__(None, pos, items,
            area_items = area_items,
            get_icon = self.get_icon,
            get_info = self.get_info,
            title = "Start Menu",
            size_x = round(D_SIZE['widget_width'] * 2.1),
            size_y = pos[1] - REGION_DATA.B - SIZE_tb[0] - SIZE_title[1],
            block_size = 1)

        area_tab = self.r_area_tab()
        button0 = ButtonFn(None, RNA_sys_off, self.bufn_sys_off)
        button1 = ButtonFn(None, RNA_sys_sleep, self.bufn_sys_sleep)
        g0 = ButtonSplit(None, button1, button0, gap=SIZE_border[3])
        area_items.append(BlockFull(area_tab, g0))
        area_tab.init_items_tab()
        #|

    def get_icon(self, e):
        if hasattr(e, "identifier"): return getattr(blg, f'GpuImg_{e.identifier}', GpuImgNull)()
        return GpuImgNull()
        #|
    def get_info(self, e):
        return ""
        #|

    def fin_callback(self):

        #|
        data = self.data
        if "fin_callfront" in data: data["fin_callfront"]()

        if data["use_text_output"] != None:

            item = None

            if data["use_text_output"]:
                tx = None
                if P.adaptive_enum_input:
                    if self.areas[0].blf_text.unclip_text.strip():
                        if data["best_item"] != None:
                            tx = data["best_item"].name

                if tx is None:
                    tx = self.areas[0].blf_text.unclip_text
            else:
                if data["best_item"] == None:
                    tx = self.areas[0].blf_text.unclip_text
                else:
                    item = data["best_item"]
                    tx = item.name

            if item is None:
                name_to_item = {e.name: e  for e in self.areas[0].filt.items}
                if tx in name_to_item: item = name_to_item[tx]

            if item is not None:
                if hasattr(item, "identifier"):
                    bpy.ops.wm.vmd_editor('INVOKE_DEFAULT', id_class=item.identifier, use_pos=False, use_fit=False)

        data.clear()
        #|

    def bufn_sys_off(self):
        try:
            W_HEAD[-1].fin()
            self.fin_from_area()
        except: pass

        m.ADMIN.evt_sys_off()
        #|
    def bufn_sys_sleep(self):
        try:
            W_HEAD[-1].fin()
            self.fin_from_area()
        except: pass

        m.ADMIN.evt_sys_off(sleep=True)
        #|
    #|
    #|

class DropDownAddOpsShortcut(DropDown):
    __slots__ = 'rna', 'keymap_category', 'active_tab', 'key_info', 'shortcut_to_km', 'area_info'

    def __init__(self, w, pos, operator_id, keymap_category):
        try:
            at0, at1 = operator_id.split(".")
            ops = getattr(getattr(bpy.ops, at0), at1)
        except: return

        self.rna = ops.get_rna_type()
        self.keymap_category = keymap_category
        self.shortcut_to_km = r_shortcut_to_km(bpy.context.window_manager.keyconfigs.user.keymaps, keymap_category)
        if self.shortcut_to_km is None: return

        self.key_info = f"Shortcut Categroy :  {keymap_category}"

        LL, TT = pos
        size_x = round(D_SIZE['widget_width'] * 3.0)
        size_y = size_x
        d0 = SIZE_dd_border[0]
        inner = SIZE_title[1] // 20
        button_h = SIZE_title[1] - inner - inner - SIZE_border[3] * 2
        button_font_size = floor(button_h * SIZE_foreground[2])

        button_append = ButtonFnFreeSize(None, RNA_append, self.bufn_append, button_font_size, button_h)

        super().__init__(w=w,
            pos = (LL - d0, TT + d0),
            size = (size_x, size_y),
            use_titlebar = True,
            protect_pos = True,
            killevt = True,
            font_id = FONT0,
            title = "Assign Operator Shortcut",
            title_button = [("close", self.fin), (button_append, button_append.r_override_width())])

        a0 = self.areas[0]
        a0.rnas = {k: e  for k, e in self.rna.properties.items()  if e.type != "POINTER" and k != "rna_type"}
        a0.props = r_props_by_rnas(a0.rnas)

        kmi_rnas = bpy.types.KeyMapItem.bl_rna.properties
        a0.bl_kmi_rnas = {
            "idname": RNA_idname,
            "type": kmi_rnas["type"],
            "value": kmi_rnas["value"],
            "direction": kmi_rnas["direction"],
            "key_modifier": kmi_rnas["key_modifier"],
            "repeat": kmi_rnas["repeat"],
            "any": kmi_rnas["any"],
            "shift_ui": kmi_rnas["shift_ui"],
            "ctrl_ui": kmi_rnas["ctrl_ui"],
            "alt_ui": kmi_rnas["alt_ui"],
            "oskey_ui": kmi_rnas["oskey_ui"],
        }
        a0.bl_kmi_props = r_props_by_rnas(a0.bl_kmi_rnas)
        a0.bl_kmi_props.idname = operator_id
        a0.bl_kmi_props.value = "PRESS"
        a0.init_tab(("MAIN",))
        #|

    def init(self, boxes, blfs):
        init = DropDown.INIT_DATA
        L = self.box_win.L
        T = self.box_win.title_B
        size_x, size_y = init['size']
        B = T - size_y
        R = L + size_x

        T1 = B + D_SIZE['widget_full_h'] + 3 * SIZE_widget[0] + (SIZE_dd_border[0] + SIZE_border[3]) * 2
        B0 = T1 + SIZE_dd_border[1]

        a0 = AreaBlockTabAddOpsShortcut(self, L, R, B0, T)
        a1 = AreaStringXYPre(self, input_text=self.key_info)
        a1.upd_size(L, R, B, T1)
        self.areas = [a0, a1]
        self.area_info = a1

        self.active_tab = None
        a0.active_tab = None
        #|

    def basis_win_evt(self):
        if (EVT_TYPE[0] == 'ESC' and EVT_TYPE[1] == 'PRESS') or TRIGGER['esc'](): return self.fin

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

    def fin_callback(self):
        kill_evt()
        #|

    def update_repeat_info(self):
        kmi = self.areas[0].bl_kmi_props

        if kmi.any:
            km_keys = ("ANY", kmi.type)  if kmi.key_modifier == "NONE" else ("ANY", kmi.key_modifier, kmi.type)
        else:
            km_keys = []
            if kmi.shift_ui: km_keys.append("SHIFT")
            if kmi.ctrl_ui: km_keys.append("CTRL")
            if kmi.alt_ui: km_keys.append("ALT")
            if kmi.oskey_ui: km_keys.append("OSKEY")
            if kmi.key_modifier != "NONE": km_keys.append(kmi.key_modifier)
            km_keys.append(kmi.type)
            km_keys = tuple(km_keys)

        self.key_info = f"Shortcut Categroy :  {self.keymap_category}\n" + r_shortcutrepeatinfo(km_keys, self.shortcut_to_km)
        self.area_info.from_string(self.key_info)
        #|

    def bufn_append(self):
        self.fin()
        try:
            kmi = self.areas[0].bl_kmi_props
            if kmi.type == "NONE": return

            e = bpy.context.window_manager.keyconfigs.user.keymaps[self.keymap_category].keymap_items.new(
                idname = kmi.idname,
                type = kmi.type,
                value = kmi.value,
                any = kmi.any,
                shift = int(kmi.shift_ui),
                ctrl = int(kmi.ctrl_ui),
                alt = int(kmi.alt_ui),
                oskey = int(kmi.oskey_ui),
                key_modifier = kmi.key_modifier,
                direction = kmi.direction,
                repeat = kmi.repeat,
                head=False)

            props = self.areas[0].props
            properties = e.properties
            for at in self.areas[0].rnas:
                setattr(properties, at, getattr(props, at))

            report("Added successfully. Requires manual saving of preferences")
        except:
            report("Unexpected error", ty="WARNING")

        if "fin_callback" in self.data:
            self.data["fin_callback"]()
            self.data.clear()
        #|
    #|
    #|
class DropDownEditOpsShortcut(DropDownAddOpsShortcut):
    __slots__ = 'keymap_item'

    def __init__(self, w, pos, operator_id, keymap_category):
        bl_keymap = bpy.context.window_manager.keyconfigs.user.keymaps[keymap_category]
        super().__init__(w, pos, operator_id, keymap_category)

        e = self.title_buttons[-1]
        self.remove_title_buttons(1, 2)
        self.append_title_button(
            ButtonFnFreeSize(None, RNA_confirm, self.bufn_confirm, e.blf_value.size, e.height))
        self.append_title_button(
            ButtonFnFreeSize(None, RNA_remove, self.bufn_remove, e.blf_value.size, e.height))
        self.set_title("Edit Operator Shortcut")

        a0 = self.areas[0]
        bl_kmi_props = a0.bl_kmi_props
        props = a0.props
        rnas = a0.rnas
        kmi = bl_keymap.keymap_items[operator_id]
        kmi_properties = kmi.properties

        for at in a0.bl_kmi_rnas:
            try: setattr(bl_kmi_props, at, getattr(kmi, at))
            except: pass

        for at in rnas:
            try: setattr(props, at, getattr(kmi_properties, at))
            except: pass

        bu_key_modifier = a0.items[1].buttons[4].button0
        bu_key_modifier.set(bu_key_modifier.get())
        #|

    def bufn_confirm(self):
        self.fin()

        try:
            a0 = self.areas[0]
            bl_kmi_props = a0.bl_kmi_props
            props = a0.props
            rnas = a0.rnas
            bl_keymap = bpy.context.window_manager.keyconfigs.user.keymaps[self.keymap_category]
            kmi = bl_keymap.keymap_items[bl_kmi_props.idname]
            kmi_properties = kmi.properties
            kmi.map_type = "KEYBOARD"

            for at in a0.bl_kmi_rnas:
                try: setattr(kmi, at, getattr(bl_kmi_props, at))
                except: pass

            for at in rnas:
                try: setattr(kmi_properties, at, getattr(props, at))
                except: pass

            report("Edited successfully. Requires manual saving of preferences")
        except:
            report("Failed. The keymap may have been removed externally", ty="WARNING")

        if "fin_callback" in self.data:
            self.data["fin_callback"]()
            self.data.clear()
        #|
    def bufn_remove(self):
        self.fin()

        try:
            a0 = self.areas[0]
            bl_kmi_props = a0.bl_kmi_props
            bl_keymap = bpy.context.window_manager.keyconfigs.user.keymaps[self.keymap_category]
            kmi = bl_keymap.keymap_items[bl_kmi_props.idname]
            bl_keymap.keymap_items.remove(kmi)

            report("Removed. Requires manual saving of preferences")
        except:
            report("Failed. The keymap may have been removed externally", ty="WARNING")

        if "fin_callback" in self.data:
            self.data["fin_callback"]()
            self.data.clear()
        #|
    #|
    #|

class DDPreviewImage(DropDown):
    __slots__ = ()

    def __init__(self, w, img, pos=None, showname=True, scale=1.0):
        d0 = SIZE_dd_border[0]
        title_h = max(2, d0)
        size_x = round(150 * scale) + d0 + d0
        size_y = size_x
        title = img.name  if showname else ""

        if pos is None:
            pos = (
                MOUSE[0] - SIZE_title[1],
                MOUSE[1] + SIZE_title[1] + d0
            )

        super().__init__(
            w = w,
            pos = pos,
            size = (size_x, size_y),
            use_titlebar = True,
            title = title,
            is_autoclose = True)

        o = self.box_win

        if showname: pass
        else:
            rim_d = SIZE_dd_border[2]
            dT = o.title_B + title_h - o.T
            o.T += dT
            o.upd()
            self.box_rim.T += dT
            self.box_rim.upd()
            e = self.boxes[0]
            e.T += dT
            e.upd()

        e = GpuImgUtil(img)
        self.boxes.append(e)
        e.LRBT_upd(
            o.L + d0,
            o.R - d0,
            o.B + d0,
            o.title_B - d0)
        #|

    def init(self, boxes, blfs):

        self.areas = []
        #|

    def fin_callback(self):
        kill_evt()
        #|
    #|
    #|
class DDKeyframes(DropDown):
    __slots__ = (
        'keyframe_buttons',
        'r_array',
        'r_fcurve',
        'r_driver',
        'upd_button_keyframe',
        'focus_element')

    def __init__(self, w, rna, r_array, row_length, r_fcurve, r_driver, upd_button_keyframe, r_keyframe_button_fn, pos=None):
        self.r_array = r_array
        self.r_fcurve = r_fcurve
        self.r_driver = r_driver
        self.upd_button_keyframe = upd_button_keyframe
        self.focus_element = None

        d0 = SIZE_dd_border[0]
        d0x2 = d0 + d0
        h = SIZE_widget[0]
        inner = h // 4
        inner_2 = inner + inner
        full_h = D_SIZE['widget_full_h']
        widget_rim = SIZE_border[3]
        widget_rim_2 = widget_rim + widget_rim
        array = r_array()
        array_length = len(array)
        title_h = max(2, d0)
        size_x = full_h * row_length + d0x2 + inner_2
        size_y = full_h * ceil(array_length / row_length) + d0x2 + inner_2
        title = rna.name

        if pos is None:
            pos = (
                MOUSE[0] - SIZE_title[1],
                MOUSE[1] + SIZE_title[1] + d0
            )

        super().__init__(
            w = w,
            pos = pos,
            size = (size_x, size_y),
            use_titlebar = True,
            title = title)

        keyframe_button_fn_wrapper = self.keyframe_button_fn_wrapper
        keyframe_buttons = [
            ButtonFnImgHoverKeyframe(self, RNA_button_keyframe, keyframe_button_fn_wrapper(r_keyframe_button_fn(r), r))  for r in range(array_length)
        ]
        self.keyframe_buttons = keyframe_buttons
        o = self.box_win
        L = o.L + d0 + inner + widget_rim
        range_row = range(row_length)
        LRs = []
        R0 = L + h
        for _ in range_row:
            LRs.append([L, R0])
            L = R0 + widget_rim_2
            R0 += full_h

        i = 0
        T = o.title_B - d0 - inner - widget_rim
        B = T - h
        amount = array_length // row_length
        for _ in range(amount):
            for r in range_row:
                L0, R0 = LRs[r]
                keyframe_buttons[i].box_button.LRBT_upd(L0, R0, B, T)
                keyframe_buttons[i].box_hover = None
                i += 1

            T = B - widget_rim_2
            B -= full_h

        for r in range(array_length - amount * row_length):
            L0, R0 = LRs[r]
            keyframe_buttons[i].box_button.LRBT_upd(L0, R0, B, T)
            keyframe_buttons[i].box_hover = None
            i += 1
        #|

    def init(self, boxes, blfs):
        self.areas = []
        #|

    def keyframe_button_fn_wrapper(self, func, index):
        def keyframe_button_fn():
            func()
            self.upd_button_keyframe(self.keyframe_buttons[index], self.r_fcurve()[index], self.r_driver()[index], self.r_array()[index])
        return keyframe_button_fn
        #|

    def i_modal(self):
        basis_evt_fn = self.basis_win_evt()
        if basis_evt_fn != None:
            basis_evt_fn()
            return

        e = None
        for o in self.keyframe_buttons:
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

            e.modal()
        #|

    def i_draw(self):
        super().i_draw()

        blend_set('ALPHA')
        scissor_test_set(True)
        self.scissor.use()

        upd_button_keyframe = self.upd_button_keyframe
        for e, fc, dr, v in zip(self.keyframe_buttons, self.r_fcurve(), self.r_driver(), self.r_array()):
            upd_button_keyframe(e, fc, dr, v)
            e.draw_box()

        scissor_test_set(False)
        #|

    def dxy(self, dx, dy):
        super().dxy(dx, dy)

        for e in self.keyframe_buttons:
            e.dxy(dx, dy)
        #|

    def fin_callback(self):
        kill_evt()
        #|
    def evt_click_outside(self): self.evt_dd_confirm()
    def evt_dd_confirm(self):
        self.fin()
        #|
    #|
    #|
class DDKeyframeGroup(DropDown):
    __slots__ = 'update_modal'

    def __init__(self, w):
        widget_rim = SIZE_border[3]
        h = SIZE_widget[0]
        d0 = SIZE_dd_border[0]
        borders = (widget_rim + d0) * 4

        L, R, B, T = w.box_anim.r_LRBT()
        L -= D_SIZE['widget_width'] + borders + SIZE_block[1] + SIZE_block[2] + h

        if hasattr(w.rna, "__len__"):
            array_length = len(w.rna)
            h_gaps = SIZE_button[1] * (array_length - 1) + widget_rim * (array_length + 1)
        else:
            array_length = w.array_length
            h_gaps = 0

        super().__init__(
            w = w,
            pos = (L + d0 + d0 + SIZE_block[2] + widget_rim, T),
            size = (R - L, h * array_length + borders + SIZE_block[4] + SIZE_block[3] + h_gaps),
            use_titlebar = False,
            title = "")
        #|

    def init(self, boxes, blfs):
        init = DropDown.INIT_DATA
        w = self.w
        rna = w.rna
        r_pp = w.r_pp

        L, R, B, T = self.box_win.r_LRBT()
        d0 = SIZE_dd_border[0]
        T = self.box_win.title_B - d0
        B += d0
        L += d0
        R -= d0

        a0 = AreaBlockSimple(self, L, R, B, T)
        b0 = BlockR(a0)
        self.areas = [a0]

        r_dph = w.ui_anim_data.r_dph
        r_pp_ref = w.ui_anim_data.r_pp_ref
        rnas = w.ui_anim_data.rnas
        ui_anim_data = UiAnimData(r_pp, r_pp_ref, r_dph, rnas)

        if hasattr(rna, "subtype") and rna.subtype.startswith("COLOR"):
            if hasattr(w, "identifier_escape"):
                u = (BuGnFloatVecSub  if rna.is_animatable else BuGnFloatVecSubNoAnim)(
                    w.w, rna, r_pp, ui_anim_data, "", False)
                u.identifier_escape = f'["{u.identifier}"]'
                ui_anim_data.props[(u.identifier, )] = u
            else:
                u = (BuFloatVecSub  if rna.is_animatable else BuFloatVecSubNoAnim)(
                    w.w, rna, r_pp, ui_anim_data, "", False)
                ui_anim_data.props[u.identifier] = u

            u.init_subtype_dimen("RGBA", "XXXX")
            u.init_bat = u.init_bat_anim
            u.step = 1

            b0.buttons = [u]
        elif hasattr(rna, "__len__"):
            b0_buttons = []
            BuCls = BuBool  if rna[0].is_animatable else BuBoolNoAnim
            for r, rna0 in enumerate(rna):
                u = BuCls(
                    w.w, rna0, r_pp, ui_anim_data, None, False)
                ui_anim_data.props[u.identifier] = u
                u.init_bat = u.init_bat_animR
                b0_buttons.append(u)

            b0.buttons = b0_buttons
        else:
            u = (BuBoolVec  if rna.is_animatable else TODO)(
                w.w, rna, r_pp, ui_anim_data, rna.name, False)
            ui_anim_data.props[u.identifier] = u

            u.init_subtype([str(r)  for r in u.vec_range])
            u.init_bat = u.init_bat_anim
            b0.buttons = [u]

        a0.items.append(b0)
        a0.init_draw_range()

        def upd_data():
            block.FRAME_CURRENT = bpy.context.scene.frame_current
            ui_anim_data.update_with(N1)
            #|

        self.update_modal = UpdateModal(upd_data)
        W_MODAL.insert(-1, self.update_modal)
        upd_data()

        if hasattr(rna, "__len__"): pass
        else:
            if rna.type != "BOOLEAN":
                u.blf_title.text = ""
        #|

    def fin_callback(self):
        kill_evt()
        W_MODAL.remove(self.update_modal)
        #|
    def evt_click_outside(self): self.evt_dd_confirm()
    def evt_dd_confirm(self):
        self.fin()
        #|
    #|
    #|


def get_info_users(e):
    if hasattr(e, "library") and e.library and e.library.filepath:
        s = f"{e.library.filepath}  |  "
    else:
        s = ""

    if hasattr(e, "users"):
        if e.use_fake_user: return f'{s}{e.users} F'
        return f'{s}{e.users}'
    return s
    #|
def r_get_icon_blendData_subtype(cls_name):
    if cls_name == "Object":
        def get_icon(e):
            return getattr(blg, f"GpuImg_OUTLINER_OB_{e.type}", GpuImgNull)()
    else:
        return None

    return get_icon
    #|

class PreviewCache:
    __slots__ = (
        'w',
        'gpu_images',
        'bpy_data_type')

    def __init__(self, w, bpy_data_type):
        self.w = w
        self.gpu_images = {}
        self.bpy_data_type = bpy_data_type
        #|

    def kill(self):

        self.gpu_images.clear()
        #|

    def get_icon(self, e):
        if e in self.gpu_images: return self.gpu_images[e]
        else:
            gpu_image = GpuImgUtil(e)
            self.gpu_images[e] = gpu_image
            return gpu_image
        #|
    #|
    #|
class PreviewCacheMaterial(PreviewCache):
    __slots__ = (
        'temp_scene',
        'temp_world',
        'temp_mesh',
        'temp_plane',
        'temp_cam',
        'temp_camera',
        'temp_folder',
        'temp_filepath')

    def __init__(self, w, bpy_data_type):
        super().__init__(w, bpy_data_type)

        resolution = SIZE_widget[0] * 4

        temp_folder = mkdtemp()

        temp_filepath = f'{temp_folder}{os_sep}0.png'

        bpydata = bpy.data
        scene = bpydata.scenes.new("")
        scene.render.engine = "BLENDER_EEVEE"
        scene.render.image_settings.file_format = "PNG"
        scene.render.filepath = temp_filepath
        scene.eevee.taa_render_samples = 1
        scene.eevee.taa_samples = 0
        scene.eevee.use_taa_reprojection = False
        scene.render.resolution_x = resolution
        scene.render.resolution_y = resolution
        scene.frame_end = 1
        world = bpydata.worlds.new("")
        world.color = 1.0, 1.0, 1.0
        scene.world = world

        me = bpydata.meshes.new("")
        me.from_pydata([(-1.0, -1.0, 0.0), (1.0, -1.0, 0.0), (-1.0, 1.0, 0.0), (1.0, 1.0, 0.0)], [], [(0, 1, 3, 2)])
        me.uv_layers.new()
        plane = bpydata.objects.new("", me)
        cam_offset = 1
        cam_distance = 2
        cam = bpydata.cameras.new("")
        cam.type = "ORTHO"
        cam.clip_start = 0.1
        cam.clip_end = 10
        cam.ortho_scale = cam_distance
        camera = bpydata.objects.new("", cam)
        camera.location[2] = cam_offset + cam_distance
        scene.collection.objects.link(camera)
        scene.collection.objects.link(plane)
        scene.camera = camera

        self.temp_folder = temp_folder
        self.temp_filepath = temp_filepath
        self.temp_scene = scene
        self.temp_world = world
        self.temp_mesh = me
        self.temp_plane = plane
        self.temp_cam = cam
        self.temp_camera = camera
        #|

    def kill(self):
        del_folder(self.temp_folder)
        bpydata = bpy.data

        bpydata.objects.remove(self.temp_camera)
        bpydata.objects.remove(self.temp_plane)
        bpydata.cameras.remove(self.temp_cam)
        bpydata.meshes.remove(self.temp_mesh)
        bpydata.worlds.remove(self.temp_world)
        bpydata.scenes.remove(self.temp_scene)
        del self.temp_cam
        del self.temp_mesh
        del self.temp_camera
        del self.temp_plane
        del self.temp_world
        del self.temp_scene
        del self.temp_filepath
        del self.temp_folder
        super().kill()
        #|

    def get_icon(self, e):
        if e in self.gpu_images: return self.gpu_images[e]
        else:
            self.temp_plane.active_material = e
            bpy.ops.render.render(animation=False, write_still=True, scene=self.temp_scene.name)
            img = bpy_images_load(self.temp_filepath)
            img.alpha_mode = "PREMUL"
            gpu_image = GpuImgUtil(img)
            bpy_images_remove(img)
            self.gpu_images[e] = gpu_image
            return gpu_image
        #|
    #|
    #|


def call_dd_license():
    if not P: return

    is_accept = [False]
    lines = None
    txtpath = Path(f"{m.ADDON_FOLDER}{os_sep}LICENSE.txt")
    if txtpath.exists():
        with open(str(txtpath), "r") as f:
            lines = tuple(f.readlines())

    if not lines:
        DropDownOk(None, [50, 250], input_text="License file is missing, please reinstall it.")
        return

    def button_fn_cancel(button=None):
        ddw.fin_from_area()
        #|
    def button_fn_next():
        if not props.accept_license: return
        is_accept[0] = True
        ddw.fin_from_area()
        #|
    def endfn(dic):
        nonlocal lines
        del lines
        if not props.accept_license: return
        if is_accept[0] is True:
            call_dd_first_time_setting()

    gap = SIZE_button[1]
    props = SimpleNamespace()
    props.accept_license = False
    button_cancel = ButtonFn(None, RNA_cancel, button_fn_cancel)
    button_next = ButtonFn(None, RNA_next, button_fn_next)
    area_items = []
    input_text = "".join(lines)

    ddw = DropDownInfoUtil(None, [0, 0],
        [ButtonSplit(None, button_cancel, button_next, gap)],
        area_items = area_items,
        endfn = endfn,
        title = "Welcome to vmdesk",
        input_text = input_text,
        row_count=12, width_fac=3.0, block_size=3, readonly=True)

    area_tab = ddw.r_area_tab()
    layout = Layout(area_tab)
    l0 = layout.new_block()
    l0.sep(1)
    g_title = l0.title("Please read the above license agreement carefully.")
    g_accept = l0.prop(props, RNA_accept, title="I accept the terms in the License Agreement", align="T", use_push=False, set_callback=False)
    l0.sep(3)

    def set_callback_accept():
        g_accept.button0.upd_data()
        if props.accept_license:
            if button_next.is_dark() is True:
                button_next.light()
        else:
            if button_next.is_dark() is False:
                button_next.dark()


    g_accept.button0.set_callback = set_callback_accept

    area_tab.init_items_tab()
    button_next.dark()
    #|
def call_dd_first_time_setting():
    enumitems_primary_button = Dictlist((
        EnumItem("LEFTMOUSE", "Left Mouse", ""),
        EnumItem("RIGHTMOUSE", "Right Mouse", "")))
    enumitems_primary_button.default = "LEFTMOUSE"

    enumitems_filter_operation = Dictlist((
        EnumItem("PRESS_PRESS", "Click-Click", ""),
        EnumItem("DRAG_RELEASE", "Drag-Release", "")))
    enumitems_filter_operation.default = "PRESS_PRESS"

    RNA_primary_button = RnaEnum("primary_button",
        enumitems_primary_button,
        name = "Primary Mouse Button",
        default = enumitems_primary_button.default
    )
    RNA_filter_operation = RnaEnum("filter_operation",
        enumitems_filter_operation,
        name = "Filter Event Method",
        default = enumitems_filter_operation.default
    )

    def button_fn_cancel(button=None):
        ddw.fin_from_area()
        #|
    def button_fn_confirm():
        ddw.fin_from_area()
        P.is_first_use = False
        save_pref()
        #|
    def endfn(dic):
        if bpy.app.timers.is_registered(preview_anim) == True:
            bpy.app.timers.unregister(preview_anim)

    gap = SIZE_button[1]
    props = SimpleNamespace()
    props.primary_button = "LEFTMOUSE"  if KEYMAPS["click"].types0 == ['LEFTMOUSE'] else "RIGHTMOUSE"
    props.filter_operation = "PRESS_PRESS"  if KEYMAPS["area_sort"].value0 == "PRESS" else "DRAG_RELEASE"
    button_cancel = ButtonFn(None, RNA_cancel, button_fn_cancel)
    button_confirm = ButtonFn(None, RNA_confirm_full, button_fn_confirm)
    area_items = []

    input_text = "Press 'Confirm' to save preferences.\n\nPrimary Button :  This option will\n    take effect immediately.\n\nFilter Event :  How to start and end the operation.\n\nTips :  The default shortcut key for Context Menu is\n    to hold down the Right Mouse button for 0.2 seconds\n    and Release Right Mouse to cancel.\n    You can change them through the settings editor."

    def draw_ddw():
        ddw.i_draw()
        if draw_ddw.is_draw_preview is False: return

        blend_set('ALPHA')
        for e in pboxes: e.bind_draw()

        area_mds.u_draw()

        blfSize(FONT0, fontsize_title)
        blfColor(FONT0, *fontcolor_title)
        pblf_title.draw_pos()

        blend_set('ALPHA')
        filt_active_bg.bind_draw()
        filt_last_item["icon"].bind_draw()
        filt_last_item["icon_button"].bind_draw()
        o = filt_last_item["blf"]
        blfSize(FONT0, fontsize_main)
        blfColor(FONT0, *o.color)
        blfPos(FONT0, o.x, o.y, 0)
        blfDraw(FONT0, o.text)
        blfSize(FONT0, D_SIZE['font_label'])
        blfColor(FONT0, *P_color.box_filter_fg_label)
        o = filt_last_item["num"]
        blfPos(FONT0, o.x, o.y, 0)
        blfDraw(FONT0, o.text)

        blfSize(FONT0, fontsize_cursor)
        blfColor(FONT0, *color_cursor_circle)
        cursor_circle.draw_pos()
        #|
    draw_ddw.is_draw_preview = False
    def r_upd_modifiers():
        return [
            ModifierFake("Boolean", "BOOLEAN"),
            ModifierFake("Boolean 2", "BOOLEAN", show_viewport=True),
            ModifierFake("Subdivision", "SUBSURF", show_viewport=True),
        ]
    def preview_anim():

        preview_anim.anim()
        Admin.REDRAW()
        return 0.01666
    def anim_1():
        if cursor_circle.x >= filt_last_item["num"].x + widget_h3:
            preview_anim.anim = anim_2
            color_cursor_circle[2] = 0.0
            filt_active_bg.color = P_color.box_filter_num_modal
            filt_active_bg.color_rim = P_color.box_filter_num_modal_rim
            area_mds.u_draw = area_mds.i_draw_num
            return
        cursor_circle.x += 2
    def anim_2():
        dx, dy = -2, -1
        if filt_last_item["icon"].L <= pbox_rim.L:
            dx, dy = travels
            travels[0] = 0
            travels[1] = 0
            preview_anim.anim = anim_1
            is_end = True
        else:
            travels[0] -= dx
            travels[1] -= dy
            is_end = False

        filt_active_bg.dxy_upd(dx, dy)
        filt_last_item["icon"].dxy_upd(dx, dy)
        filt_last_item["icon_button"].dxy_upd(dx, dy)
        filt_last_item["blf"].x += dx
        filt_last_item["blf"].y += dy
        filt_last_item["num"].x += dx
        filt_last_item["num"].y += dy
        cursor_circle.x += dx
        cursor_circle.y += dy
        if is_end: reset_cursor_circle()
    preview_anim.anim = anim_1
    travels = [0, 0]

    ddw = DropDownInfoUtil(None, [0, 300],
        [ButtonSplit(None, button_cancel, button_confirm, gap)],
        area_items = area_items,
        endfn = endfn,
        title = "Basic settings",
        input_text = input_text,
        row_count=7, width_fac=2.2, block_size=3, readonly=True)
    ddw.u_draw = draw_ddw

    # Preview area
    widget_rim = SIZE_border[3]
    P_color = P.color
    fontsize_title = D_SIZE['font_title']
    fontsize_main = D_SIZE['font_main']
    fontsize_cursor = fontsize_main * 2
    fontcolor_title = P_color.block_fg
    preview_area_width = D_SIZE['widget_width'] * 2
    preview_area_border = D_SIZE['widget_full_h']
    widget_h3 = SIZE_widget[0] // 3
    filter_width = round(D_SIZE['widget_width'] * 1.5)

    pbox_rim = GpuRim(COL_win, COL_win_rim)
    pbox_filter = GpuRim(P_color.box_filter, P_color.box_filter_rim)
    pboxes = [
        pbox_rim,
    ]
    pblf_title = Blf("Preview Area")
    pblfs = [
    ]

    ed_fake = SimpleNamespace()
    ed_fake.active_object = None
    ed_fake.active_modifier = None
    ed_fake.scissor = ddw.scissor
    ed_fake.set_active_modifier = lambda **kw: None
    area_mds = AreaFilterYModifier(ed_fake, 0, 0, 0, 0, r_upd_modifiers)
    area_mds.scissor_text_box.__class__ = ScissorFake
    area_mds.scissor_filt.__class__ = ScissorFake
    mds_filt = area_mds.filt
    filt_last_item = {}
    cursor_circle = Blf("●")
    color_cursor_circle = [1.0] * 4
    filt_active_bg = GpuRim()

    def upd_preview_area():
        LL, RR, BB, TT = ddw.box_rim.r_LRBT()
        LL = RR + 9
        RR = LL + preview_area_width

        pbox_rim.LRBT_upd(LL, RR, BB, TT, widget_rim)
        blfSize(FONT0, fontsize_title)
        pblf_title.x = pbox_rim.r_center_x() - blfDimen(FONT0, "Preview Area")[0] // 2
        pblf_title.y = TT - widget_rim - D_SIZE['font_title_dT']

        R = RR - preview_area_border
        L = R - filter_width
        T = pblf_title.y - preview_area_border
        B = BB + preview_area_border

        area_mds.upd_size(L, R, B, T)
        travels[0] = 0
        travels[1] = 0
        reset_cursor_circle()
    def reset_cursor_circle():
        if len(mds_filt.icons) == 3:
            filt_last_item["icon"] = mds_filt.icons.pop(2)
            filt_last_item["icon_button"] = mds_filt.icons_button.pop(2)
            filt_last_item["blf"] = mds_filt.blfs.pop(2)
            filt_last_item["num"] = mds_filt.blfs_num.pop(2)

        cursor_circle.x = filt_last_item["num"].x - widget_h3
        cursor_circle.y = filt_last_item["blf"].y
        preview_anim.anim = anim_1
        color_cursor_circle[2] = 1.0
        filt_active_bg.color_rim = FLO_0000
        filt_active_bg.color = FLO_0000
        filt_active_bg.LRBT_upd(
            area_mds.box_filter.L,
            area_mds.box_filter.R,
            filt_last_item["icon"].B - widget_rim,
            filt_last_item["icon"].T + widget_rim, widget_rim)
        area_mds.u_draw = area_mds.i_draw
    #

    area_tab = ddw.r_area_tab()
    layout = Layout(area_tab)
    l0 = layout.new_block()
    l0.sep(1)
    g_primary_button = l0.prop(props, RNA_primary_button, use_push=False, set_callback=False)
    g_filter_operation = l0.prop(props, RNA_filter_operation, use_push=False, set_callback=False)
    l0.sep(3)

    def set_callback_primary_button():
        g_primary_button.button0.upd_data()
        is_swap = False
        if props.primary_button == "RIGHTMOUSE":
            if KEYMAPS["click"].types0 != ['RIGHTMOUSE']: is_swap = True
        else:
            if KEYMAPS["click"].types0 != ['LEFTMOUSE']: is_swap = True

        if is_swap is False: return
        for k, e in KEYMAPS.items():
            # /* 0dd_swap_keymap
            ks = e.types0
            ss = None
            if "LEFTMOUSE" in ks:
                ss = ",".join(["RIGHTMOUSE"  if o == "LEFTMOUSE" else o  for o in ks])
            elif "RIGHTMOUSE" in ks:
                ss = ",".join(["LEFTMOUSE"  if o == "RIGHTMOUSE" else o  for o in ks])

            if ss is not None:
                write_keytype(ss, k, 0, refresh=False)
            # */
            # <<< 1copy (0dd_swap_keymap,, ${'0':'1'}$)
            ks = e.types1
            ss = None
            if "LEFTMOUSE" in ks:
                ss = ",".join(["RIGHTMOUSE"  if o == "LEFTMOUSE" else o  for o in ks])
            elif "RIGHTMOUSE" in ks:
                ss = ",".join(["LEFTMOUSE"  if o == "RIGHTMOUSE" else o  for o in ks])

            if ss is not None:
                write_keytype(ss, k, 1, refresh=False)
            # >>>

            init_keymaps(P)
        #|
    def set_callback_filter_operation():
        g_filter_operation.button0.upd_data()
        km = KEYMAPS["area_sort"]
        if props.filter_operation == "PRESS_PRESS":
            if km.value0 != "PRESS":
                write_keyvalue("PRESS", "area_sort", 0, refresh=False)
                write_keyendvalue("PRESS", "area_sort", 0, refresh=False)
                init_keymaps(P)
        else:
            if km.value0 != "DRAG":
                write_keyvalue("DRAG", "area_sort", 0, refresh=False)
                write_keyendvalue("RELEASE", "area_sort", 0, refresh=False)
                init_keymaps(P)

    g_primary_button.button0.set_callback = set_callback_primary_button
    g_filter_operation.button0.set_callback = set_callback_filter_operation

    def inevt():
        g_filter_operation.button0.inside_evt()
        upd_preview_area()
        draw_ddw.is_draw_preview = True
        if bpy.app.timers.is_registered(preview_anim) == False:
            bpy.app.timers.register(preview_anim, first_interval=0.01666)
    def outevt():
        g_filter_operation.button0.outside_evt()
        draw_ddw.is_draw_preview = False
        if bpy.app.timers.is_registered(preview_anim) == True:
            bpy.app.timers.unregister(preview_anim)

    g_filter_operation.inside_evt = inevt
    g_filter_operation.outside_evt = outevt

    area_tab.init_items_tab()
    #|

def call_dd_index_dialog(posLT,
                        pos_offset = None,
                        index_range = range(3),
                        dark_indexes = None,
                        endfn = None,
                        title = "Dialog",
                        text = "",
                        row_count = 2,
                        width_fac = 2.0,
                        block_size = None):

    pos = [posLT[0], posLT[1]]
    if pos_offset:
        pos[0] += pos_offset[0]
        pos[1] += pos_offset[1]

    gap = SIZE_button[1]
    if block_size is None:
        block_size = len(index_range) + 1

    def button_fn_cancel(button=None):
        ddw.fin_from_area()
        #|
    def button_fn_confirm():
        ddw.data["is_confirm"] = True
        ddw.data["indexes"] = [r  for r in index_range  if getattr(props, f'use_{r}')]
        ddw.fin_from_area()
        #|

    button_cancel = ButtonFn(None, RNA_cancel, button_fn_cancel)
    button_confirm = ButtonFn(None, RNA_confirm_full, button_fn_confirm)
    area_items = []

    props = SimpleNamespace()

    ddw = DropDownInfoUtil(None, pos,
        [ButtonSplit(None, button_confirm, button_cancel, gap)],
        area_items = area_items,
        endfn = endfn,
        title = title,
        input_text = text,
        row_count = row_count,
        width_fac = width_fac,
        block_size = block_size)

    button_cancel.box_button.LRBT_upd(0, 0, 0, 0, 0)
    blf_value = button_cancel.blf_value
    blf_value.text = ""
    blf_value.x = 0
    blf_value.y = 0

    ddw.data["props"] = props
    ddw.data["is_confirm"] = False

    area_tab = ddw.r_area_tab()
    layout = Layout(area_tab)
    l0 = layout.new_block()
    l0.sep(2)
    fields = {}

    for r in index_range:
        attr = f'use_{r}'
        setattr(props, attr, False)

        fields[attr] = l0.prop(props, RnaBool(attr, str(r)), use_push=False, set_callback=True)

    l0.sep(2)
    if dark_indexes:
        for r in index_range:
            attr = f'use_{r}'

            if r in dark_indexes:
                fields[attr].dark()
            else:
                fields[attr].button0.set(True)
    else:
        fields[f'use_{index_range.start}'].button0.set(True)

    area_tab.init_items_tab()
    return ddw
    #|

## _file_ ##
def late_import():
    #|
    import bpy, blf, gpu, math, colorsys
    from tempfile import mkdtemp

    blfSize = blf.size
    blfColor = blf.color
    blfPos = blf.position
    blfDraw = blf.draw
    blfDimen = blf.dimensions

    active_framebuffer_get = gpu.state.active_framebuffer_get
    blend_set = gpu.state.blend_set
    scissor_test_set = gpu.state.scissor_test_set

    floor = math.floor
    rgb_to_hsv = colorsys.rgb_to_hsv
    hsv_to_rgb = colorsys.hsv_to_rgb


    from .  import VMD

    m = VMD.m
    block = VMD.block

    # <<< 1mp (VMD.api
    api = VMD.api
    D_cls_blendData = api.D_cls_blendData
    # >>>

    # <<< 1mp (VMD.area
    area = VMD.area
    AreaFilterY = area.AreaFilterY
    AreaFilterYModifier = area.AreaFilterYModifier
    AreaValBox = area.AreaValBox
    AreaBlock1 = area.AreaBlock1
    AreaString = area.AreaString
    AreaStringMatch = area.AreaStringMatch
    AreaStringXY = area.AreaStringXY
    AreaStringXYPre = area.AreaStringXYPre
    AreaBlockSimple = area.AreaBlockSimple
    AreaBlockTab = area.AreaBlockTab
    AreaColorHue = area.AreaColorHue
    AreaFilterYDropDownRMKeymap = area.AreaFilterYDropDownRMKeymap
    AreaFilterYDropDownEnumPointer = area.AreaFilterYDropDownEnumPointer
    # >>>

    # <<< 1mp (block
    BlockCalcDisplay = block.BlockCalcDisplay
    BlockCalcButton = block.BlockCalcButton
    BlockR = block.BlockR
    BlockFull = block.BlockFull
    ButtonSep = block.ButtonSep
    ButtonStringColorHex = block.ButtonStringColorHex
    ButtonFn = block.ButtonFn
    ButtonFnFreeSize = block.ButtonFnFreeSize
    ButtonFnImg = block.ButtonFnImg
    ButtonSplit = block.ButtonSplit
    D_gn_subtype_unit = block.D_gn_subtype_unit
    RNA_button_keyframe = block.RNA_button_keyframe
    ButtonFnImgHoverKeyframe = block.ButtonFnImgHoverKeyframe
    ButtonEnumXYTemp = block.ButtonEnumXYTemp
    ButtonFloatVectorColor = block.ButtonFloatVectorColor
    BuFloatVecColor = block.BuFloatVecColor
    BuFloatVecColorNoAnim = block.BuFloatVecColorNoAnim
    BuGnFloatVecColor = block.BuGnFloatVecColor
    BuGnFloatVecColorNoAnim = block.BuGnFloatVecColorNoAnim
    BuFloatVecSub = block.BuFloatVecSub
    BuFloatVecSubNoAnim = block.BuFloatVecSubNoAnim
    BuGnFloatVecSub = block.BuGnFloatVecSub
    BuGnFloatVecSubNoAnim = block.BuGnFloatVecSubNoAnim
    BuBoolVec = block.BuBoolVec
    BuBool = block.BuBool
    BuBoolNoAnim = block.BuBoolNoAnim
    BuColor = block.BuColor
    BuGnColor = block.BuGnColor
    UiAnimData = block.UiAnimData
    Layout = block.Layout
    # >>>

    # <<< 1mp (VMD.colorlist
    colorlist = VMD.colorlist
    L_rgb_to_glc = colorlist.L_rgb_to_glc
    glc_to_hex = colorlist.glc_to_hex
    D_glc_null = colorlist.D_glc_null
    NULL_INFO = colorlist.NULL_INFO
    scene_linear_to_hex = colorlist.scene_linear_to_hex
    L_rgb_to_scene_linear = colorlist.L_rgb_to_scene_linear
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    kill_evt = keysys.kill_evt
    kill_evt_except = keysys.kill_evt_except
    MOUSE = keysys.MOUSE
    MOUSE_WINDOW = keysys.MOUSE_WINDOW
    EVT_TYPE = keysys.EVT_TYPE
    TRIGGER = keysys.TRIGGER
    KEYMAPS = keysys.KEYMAPS
    write_keytype = keysys.write_keytype
    write_keyvalue = keysys.write_keyvalue
    write_keyendvalue = keysys.write_keyendvalue
    init_keymaps = keysys.init_keymaps
    r_end_trigger = keysys.r_end_trigger
    ITEMS_CALC_TAB = keysys.ITEMS_CALC_TAB
    rm_get_info_km = keysys.rm_get_info_km
    r_shortcut_to_km = keysys.r_shortcut_to_km
    r_shortcutrepeatinfo = keysys.r_shortcutrepeatinfo
    # >>>

    # <<< 1mp (m
    P = m.P
    Admin = m.Admin
    W_MODAL = m.W_MODAL
    W_HEAD = m.W_HEAD
    W_DRAW = m.W_DRAW
    bring_to_front = m.bring_to_front
    REGION_DATA = m.REGION_DATA
    UnitSystem = m.UnitSystem
    r_unit_factor = m.r_unit_factor
    save_pref = m.save_pref
    blockblsubwindows = m.blockblsubwindows
    # >>>

    # <<< 1mp (VMD.rna
    rna = VMD.rna
    r_props_by_rnas = rna.r_props_by_rnas
    RNA_cancel = rna.RNA_cancel
    # >>>

    # <<< 1mp (VMD.win
    win = VMD.win
    r_full_protect_dxy = win.r_full_protect_dxy
    Head = win.Head
    # >>>

    util = VMD.util
    com = util.com

    # <<< 1mp (com
    value_to_display = com.value_to_display
    is_value = com.is_value
    N = com.N
    N1 = com.N1
    bin_search = com.bin_search
    find_index = com.find_index
    find_index_attr = com.find_index_attr
    # >>>

    # <<< 1mp (util.const
    const = util.const
    FLO_0000 = const.FLO_0000
    TUP_RGBA = const.TUP_RGBA
    TUP_HSV = const.TUP_HSV
    TUP_HEX = const.TUP_HEX
    # >>>

    # <<< 1mp (util.dirlib
    dirlib = util.dirlib
    del_folder = dirlib.del_folder
    # >>>

    # <<< 1mp (util.num
    num = util.num
    split_upper = num.split_upper
    # >>>

    # <<< 1mp (util.types
    types = util.types
    Name = types.Name
    IdentifierNameValue = types.IdentifierNameValue
    RnaFloatVector = types.RnaFloatVector
    RnaBool = types.RnaBool
    RnaString = types.RnaString
    RnaButton = types.RnaButton
    RnaEnum = types.RnaEnum
    BoxGroup = types.BoxGroup
    Udraw = types.Udraw
    Dictlist = types.Dictlist
    EnumItem = types.EnumItem
    # >>>

    utilbl = VMD.utilbl

    # <<< 1mp (utilbl
    blg = utilbl.blg
    # >>>

    # <<< 1mp (blg
    Blf = blg.Blf
    BlfColor = blg.BlfColor
    BlfClip = blg.BlfClip
    GpuBox = blg.GpuBox
    GpuRim = blg.GpuRim
    GpuDropDown = blg.GpuDropDown
    GpuDropDownRim = blg.GpuDropDownRim
    GpuShadowDropDown = blg.GpuShadowDropDown
    GpuImgNull = blg.GpuImgNull
    GpuImgUtil = blg.GpuImgUtil
    GpuImg_ID_NODETREE = blg.GpuImg_ID_NODETREE
    GpuImg_OUTLINER_OB_UNKNOW = blg.GpuImg_OUTLINER_OB_UNKNOW
    GpuImg_driver_true = blg.GpuImg_driver_true
    GpuImg_keyframe_next_false_even = blg.GpuImg_keyframe_next_false_even
    GpuImg_keyframe_next_false_odd = blg.GpuImg_keyframe_next_false_odd
    GpuImg_keyframe_current_true_even = blg.GpuImg_keyframe_current_true_even
    GpuImg_keyframe_current_true_odd = blg.GpuImg_keyframe_current_true_odd
    GpuImg_keyframe_false = blg.GpuImg_keyframe_false
    r_blf_clipping_end = blg.r_blf_clipping_end
    rl_blf_wrap = blg.rl_blf_wrap
    Scissor = blg.Scissor
    ScissorFake = blg.ScissorFake
    report = blg.report
    FONT0 = blg.FONT0
    FONT1 = blg.FONT1
    D_SIZE = blg.D_SIZE
    SIZE_tb = blg.SIZE_tb
    SIZE_title = blg.SIZE_title
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_filter = blg.SIZE_filter
    SIZE_widget = blg.SIZE_widget
    SIZE_dd_shadow_offset = blg.SIZE_dd_shadow_offset
    SIZE_shadow_softness = blg.SIZE_shadow_softness
    SIZE_button = blg.SIZE_button
    SIZE_block = blg.SIZE_block
    SIZE_foreground = blg.SIZE_foreground
    COL_win = blg.COL_win
    COL_win_rim = blg.COL_win_rim
    COL_box_val = blg.COL_box_val
    COL_box_val_rim = blg.COL_box_val_rim
    COL_box_val_fo = blg.COL_box_val_fo
    COL_box_val_fg = blg.COL_box_val_fg
    COL_box_val_fg_error = blg.COL_box_val_fg_error
    COL_box_button_fg_info = blg.COL_box_button_fg_info
    geticon_Object = blg.geticon_Object
    getinfo_Object = blg.getinfo_Object
    geticon_Modifier = blg.geticon_Modifier
    geticon_DriverVar = blg.geticon_DriverVar
    D_icon_rm = blg.D_icon_rm
    # >>>

    # <<< 1mp (utilbl.general
    general = utilbl.general
    update_scene_push = general.update_scene_push
    r_library_or_override_message = general.r_library_or_override_message
    r_unsupport_override_message = general.r_unsupport_override_message
    bpy_data_append = general.bpy_data_append
    bl_NodeTree_compare = general.bl_NodeTree_compare
    # >>>

    # <<< 1mp (utilbl.md
    md = utilbl.md
    ops_mds_copy_to_object = md.ops_mds_copy_to_object
    md_rnas_MESH = md.md_rnas_MESH
    md_rnas_CURVE = md.md_rnas_CURVE
    md_rnas_SURFACE = md.md_rnas_SURFACE
    md_rnas_VOLUME = md.md_rnas_VOLUME
    md_rnas_LATTICE = md.md_rnas_LATTICE
    ModifierFake = md.ModifierFake
    # >>>


    BL_RNA_PROP_keymaps = P.keymaps.bl_rna.properties
    D_format = m.UnitSystem.D_format

    import _bpy
    bpy_images_load = _bpy.data.images.load
    bpy_images_remove = _bpy.data.images.remove

    RNA_hsv = RnaFloatVector("hsv",
        name = "HSV",
        description = "Color Panel HSV",
        default = (0.0, 0.0, 0.0),
        subtype = "COLOR")
    RNA_hsv.soft_min = 0.0
    RNA_hsv.soft_max = 1.0
    RNA_hex_str_glc = RnaString("hex_str",
        name = "Gamma Corrected Hex",
        default = "\"0\"",
        description = "Color Panel hex value.\nInvalid value in (\n" + NULL_INFO[0] + "\n)")
    RNA_eyedropper = RnaButton("eyedropper",
        name = "Eyedropper",
        button_text = "",
        description = "Sample a color from the Blender window to store in a property.",
        size = -1)
    RNA_yes = RnaButton("yes",
        name = "Yes",
        button_text = "Yes",
        description = "Button Yes.")
    RNA_no = RnaButton("no",
        name = "No",
        button_text = "No",
        description = "Button No.")
    RNA_save = RnaButton("save",
        name = "Save",
        button_text = "Save",
        description = "Button Save.",
        size = -3)
    RNA_append = RnaButton("append",
        name = "Append",
        button_text = "Append",
        description = "Button Append.",
        size = -3)
    RNA_confirm = RnaButton("confirm",
        name = "Confirm",
        button_text = "Confirm",
        description = "Button Confirm.",
        size = -3)
    RNA_confirm_full = RnaButton("confirm",
        name = "Confirm",
        button_text = "Confirm",
        description = "Button Confirm.")
    RNA_remove = RnaButton("remove",
        name = "Remove",
        button_text = "Remove",
        description = "Button Remove.",
        size = -3)
    RNA_reset = RnaButton("reset",
        name = "Reset",
        button_text = "Reset",
        description = "Button Reset.",
        size = -3)
    RNA_sys_off = RnaButton("sys_off",
        name = "System Off",
        button_text = "Off",
        description = "")
    RNA_sys_sleep = RnaButton("sys_sleep",
        name = "System Sleep",
        button_text = "Sleep",
        description = "")
    RNA_idname = RnaString("idname",
        name = "ID Name",
        default = "",
        description = "",
        is_readonly = True)
    RNA_edit_keys = RnaButton("edit_keys",
        name = "Keys",
        button_text = "Edit",
        description = "")
    RNA_key_info = RnaString("key_info",
        name = "Key Info",
        default = "",
        description = "",
        subtype = "LINES",
        is_readonly = True)
    RNA_next = RnaButton("next",
        name = "Next",
        button_text = "Next",
        description = "")
    RNA_accept = RnaBool("accept_license",
        name = "Accept License")


    class AreaBlockTabAddOpsShortcut(AreaBlockTab):
        __slots__ = (
            'upd_data_callback',
            'props',
            'rnas',
            'bl_kmi_props',
            'bl_kmi_rnas')

        def init_tab_MAIN(self):
            layout = Layout(self)
            layout.set_fold_state(False)
            props = self.props
            rnas = self.rnas
            bl_kmi_props = self.bl_kmi_props
            bl_kmi_rnas = self.bl_kmi_rnas
            set_callback = self.upd_data
            enumitems_keys = bl_kmi_rnas["type"].enum_items
            key_to_name = {
                "SHIFT": "Shift",
                "CTRL": "Ctrl",
                "ALT": "Alt",
                "OSKEY": "OS Key",
            }

            @ noRecursive
            def set_callback(option, value):
                if bl_kmi_props.type == "NONE": g_edit_keys.button0.set_button_text("Edit")
                else:
                    li = []
                    if bl_kmi_props.shift_ui: li.append("SHIFT")
                    if bl_kmi_props.ctrl_ui: li.append("CTRL")
                    if bl_kmi_props.alt_ui: li.append("ALT")
                    if bl_kmi_props.oskey_ui: li.append("OSKEY")
                    if bl_kmi_props.key_modifier != "NONE": li.append(bl_kmi_props.key_modifier)

                    li.append(bl_kmi_props.type)
                    set_edit_keys(li)
                self.upd_data()
            @ noRecursive
            def set_edit_keys(li):
                bl_kmi_props.shift_ui = False
                bl_kmi_props.ctrl_ui = False
                bl_kmi_props.alt_ui = False
                bl_kmi_props.oskey_ui = False

                li_name = []
                for k in li:
                    if k in key_to_name:
                        li_name.append(key_to_name[k])

                        if k == "SHIFT":
                            bl_kmi_props.shift_ui = True
                        elif k == "CTRL":
                            bl_kmi_props.ctrl_ui = True
                        elif k == "ALT":
                            bl_kmi_props.alt_ui = True
                        else:
                            bl_kmi_props.oskey_ui = True
                    elif k in enumitems_keys:
                        li_name.append(enumitems_keys[k].name)
                        bl_kmi_props.type = k

                g_edit_keys.button0.set_button_text("   ".join(li_name))
                self.w.update_repeat_info()
                self.upd_data()
            def bufn_edit_keys():
                g_edit_keys.button0.set_button_text("Press a key")

                def localmodal():
                    evt = Admin.EVT
                    if evt.value == "PRESS":
                        if evt.type not in {"NONE", "LEFT_CTRL", "LEFT_ALT", "LEFT_SHIFT", "RIGHT_ALT", "RIGHT_CTRL", "RIGHT_SHIFT", "OSKEY"}:
                            w_head.fin()
                            kill_evt()
                            li = []
                            if evt.shift: li.append("SHIFT")
                            if evt.ctrl: li.append("CTRL")
                            if evt.alt: li.append("ALT")
                            if evt.oskey: li.append("OSKEY")
                            li.append(evt.type)
                            set_edit_keys(li)
                            Admin.REDRAW()
                            return

                w_head = Head(self, localmodal)

            l0 = layout.new_block()
            g_idname = l0.prop(bl_kmi_props, RNA_idname, title=self.w.rna.name, align=True)
            l0.sep(1)
            g_edit_keys = l0.prop(bufn_edit_keys, RNA_edit_keys)
            g_edit_keys.r_button_width = lambda: g_idname.button0.box_button.r_w()

            l1 = layout.new_block()
            g_type = l1.prop(bl_kmi_props, bl_kmi_rnas["type"], set_callback=set_callback, append=False, use_push=False)
            g_value = l1.prop(bl_kmi_props, bl_kmi_rnas["value"], set_callback=set_callback, append=False, use_push=False)
            l1.split(g_value, g_type)
            l1.sep(1)
            g_mdkeys = l1.prop_boolflag(bl_kmi_props,
                [rna  for k, rna in bl_kmi_rnas.items()  if k in {"any", "shift_ui", "ctrl_ui", "alt_ui", "oskey_ui"}],
                set_callback = set_callback,
                use_push = False
            )
            def r_button_width(): return g_type.button0.box_button.R - g_value.button0.box_button.L

            g_mdkeys.r_button_width = r_button_width
            l1.sep(1)
            g_key_modifier = l1.prop(bl_kmi_props, bl_kmi_rnas["key_modifier"], set_callback=set_callback, use_push=False)
            g_direction = l1.prop(bl_kmi_props, bl_kmi_rnas["direction"], set_callback=set_callback, use_push=False)
            g_repeat = l1.prop(bl_kmi_props, bl_kmi_rnas["repeat"], set_callback=set_callback, use_push=False)

            l2 = layout.new_block("Properties")
            l3 = layout.new_block("Modal Keymap")

            for k, rna in rnas.items():
                if k in {"modal_keymap", "drag_speed"}:
                    if k == "modal_keymap":
                        l3.prop(props, rna, title="Json String", set_callback=set_callback, use_push=False)
                        l3.items[-1].r_button_width = lambda: D_SIZE['widget_width'] * 2
                    else:
                        l3.prop(props, rna, set_callback=set_callback, use_push=False)
                else:
                    l2.prop(props, rna, set_callback=set_callback, use_push=False)

            def upd_data_callback():
                if bl_kmi_props.value == "CLICK_DRAG":
                    if g_direction.is_dark() is True: g_direction.light()
                    if g_repeat.is_dark() is False: g_repeat.dark()
                else:
                    if g_direction.is_dark() is False: g_direction.dark()
                    if bl_kmi_props.value in {"PRESS", "ANY"}:
                        if g_repeat.is_dark() is True: g_repeat.light()
                    else:
                        if g_repeat.is_dark() is False: g_repeat.dark()

                for e in self.items: e.upd_data()

            if not self.items[-1].items:
                del self.items[-1]

            self.upd_data_callback = upd_data_callback
            upd_data_callback()
            #|

        def upd_data(self):
            if hasattr(self, "upd_data_callback"): self.upd_data_callback()
            #|
        #|
        #|

    globals().update(locals())
    #|
