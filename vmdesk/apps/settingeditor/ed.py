











import bpy, blf, json

blfSize = blf.size
blfColor = blf.color
blfPos = blf.position
blfDraw = blf.draw
blfDimen = blf.dimensions

from gpu.state import blend_set
from math import floor
from types import SimpleNamespace
from pathlib import Path
from math import floor

from .  import VMD, prop

# <<< 1mp (VMD.win
win = VMD.win
Window = win.Window
# >>>

util = VMD.util

# <<< 1mp (util.deco
deco = util.deco
successResult = deco.successResult
catch = deco.catch
# >>>

# <<< 1mp (util.types
types = util.types
RnaSubtab = types.RnaSubtab
RnaButton = types.RnaButton
RnaBool = types.RnaBool
RnaDataOps = types.RnaDataOps
LocalHistory = types.LocalHistory
HistoryValue = types.HistoryValue
Dictlist = types.Dictlist
# >>>

# <<< 1mp (VMD.area
area = VMD.area
AreaBlockTab = area.AreaBlockTab
StructAreaModal = area.StructAreaModal
AreaStringXYButton = area.AreaStringXYButton
AreaStringXYPre = area.AreaStringXYPre
# >>>

# <<< 1mp (VMD.block
block = VMD.block
ButtonString = block.ButtonString
BlockUtils = block.BlockUtils
BuStrPref = block.BuStrPref
ButtonStringPref = block.ButtonStringPref
ButtonEnumPref = block.ButtonEnumPref
ButtonBoolPref = block.ButtonBoolPref
ButtonFloatPref = block.ButtonFloatPref
ButtonStringMatchButton = block.ButtonStringMatchButton
# >>>

# <<< 1mp (VMD
m = VMD.m
# >>>

# <<< 1mp (prop
RNA_header_button = prop.RNA_header_button
RNA_header_media_text = prop.RNA_header_media_text
RNA_edit_expression = prop.RNA_edit_expression
RNA_md_lib_refresh = prop.RNA_md_lib_refresh
RNA_md_lib_edit = prop.RNA_md_lib_edit
RNA_ui_scale_100 = prop.RNA_ui_scale_100
RNA_ui_scale_133 = prop.RNA_ui_scale_133
RNA_ui_scale_166 = prop.RNA_ui_scale_166
RNA_ui_scale_200 = prop.RNA_ui_scale_200
RNA_ui_reload_icon = prop.RNA_ui_reload_icon
RNA_ui_reload_font = prop.RNA_ui_reload_font
RNA_pref_export_theme = prop.RNA_pref_export_theme
RNA_pref_import_theme = prop.RNA_pref_import_theme
RNA_pref_export = prop.RNA_pref_export
RNA_pref_import = prop.RNA_pref_import
RNA_pref_load_theme_dark = prop.RNA_pref_load_theme_dark
RNA_edit_keystroke0 = prop.RNA_edit_keystroke0
RNA_edit_keystroke1 = prop.RNA_edit_keystroke1
RNA_keycatch_save = prop.RNA_keycatch_save
RNA_keycatch_clear = prop.RNA_keycatch_clear
RNA_keycomb0 = prop.RNA_keycomb0
RNA_keycomb1 = prop.RNA_keycomb1
RNA_keycombcatch = prop.RNA_keycombcatch
RNA_keyvalue0 = prop.RNA_keyvalue0
RNA_keyvalue1 = prop.RNA_keyvalue1
RNA_keyendvalue0 = prop.RNA_keyendvalue0
RNA_keyendvalue1 = prop.RNA_keyendvalue1
RNA_keyexact0 = prop.RNA_keyexact0
RNA_keyexact1 = prop.RNA_keyexact1
RNA_keyduration0 = prop.RNA_keyduration0
RNA_keyduration1 = prop.RNA_keyduration1
RNA_text_search = prop.RNA_text_search
RNA_use_search_id = prop.RNA_use_search_id
RNA_use_search_name = prop.RNA_use_search_name
RNA_use_search_description = prop.RNA_use_search_description
RNA_use_search_cat_pref = prop.RNA_use_search_cat_pref
RNA_use_search_cat_pref_color = prop.RNA_use_search_cat_pref_color
RNA_use_search_cat_pref_size = prop.RNA_use_search_cat_pref_size
RNA_use_search_cat_pref_keymap = prop.RNA_use_search_cat_pref_keymap
RNA_use_search_cat_pref_apps = prop.RNA_use_search_cat_pref_apps
RNA_about = prop.RNA_about
RNA_ops_refresh = prop.RNA_ops_refresh
# >>>


LONGEST_TITLE = "Modifier Editor: Use Mouse Index (Copy to Selected)"
RNAS = {
    "search": {},
    "system": {
        "display": RnaSubtab("display", "Display", "Window position, Taskbar, Enable/disable features", "GpuImg_settings_system_display"),
        "control": RnaSubtab("control", "Control", "Scroll speed, Drag threshold, Pan method", "GpuImg_settings_system_control"),
        "menu": RnaSubtab("menu", "Menu", "Drop Down Menu behavior, Format, Text Box", "GpuImg_settings_system_menu"),
        "expression": RnaSubtab("expression", "Expression", "Calculator expressions and button functions", "GpuImg_settings_system_expression"),
        "library": RnaSubtab("library", "Library", "Library Data", "GpuImg_settings_system_library"),
        "all_settings": RnaSubtab("all_settings", "All Settings", "All addon properties, Import/Export settings", "GpuImg_settings_system_all_settings"),
        "about": RnaSubtab("about", "About", "Information, Support and help", "GpuImg_settings_system_about"),
    },
    "size": {
        "ui_size": RnaSubtab("ui_size", "UI Size", "Interface size", "GpuImg_settings_size_ui_size"),
    },
    "personalization": {
        "ui_color": (RnaSubtab("ui_color", "UI Color", "Interface colors", "GpuImg_settings_personalization_ui_color"), {
            "all": RnaSubtab("all", "All", "All UI color", "GpuImg_settings_system_all_settings"),
            "window": RnaSubtab("window", "Window", "Window color", "GpuImg_settings_personalization_ui_color_window"),
            "menu": RnaSubtab("menu", "Menu", "Menu color", "GpuImg_settings_system_menu"),
            "foreground": RnaSubtab("foreground", "Foreground", "Font color", "GpuImg_settings_personalization_ui_color_foreground"),
            "hover": RnaSubtab("hover", "Hover", "Widget hover color", "GpuImg_settings_personalization_ui_color_hover"),
            "taskbar": RnaSubtab("taskbar", "Taskbar", "Taskbar color", "GpuImg_settings_personalization_ui_color_taskbar"),
        }),
        "shadow": RnaSubtab("shadow", "Shadow", "Editor drop shadow appearance", "GpuImg_settings_personalization_shadow"),
        "font": (RnaSubtab("font", "Font", "UI font", "GpuImg_settings_personalization_font"), {
            "text_rendering": RnaSubtab("text_rendering", "Text Rendering", "Enable font shadow", "GpuImg_settings_personalization_font"),
            "color": RnaSubtab("color", "Color", "Foreground color", "GpuImg_settings_personalization_ui_color_foreground"),
            "path": RnaSubtab("path", "Path", "UI font path", "GpuImg_settings_personalization_font_path"),
        }),
        "theme": RnaSubtab("theme", "Theme", "UI theme", "GpuImg_settings_personalization_theme"),
    },
    "apps": {
        "ModifierEditor": RnaSubtab("ModifierEditor", "Modifier Editor", "Shows the modifiers in a specific object.", "GpuImg_ModifierEditor"),
        "SettingEditor": RnaSubtab("SettingEditor", "Settings Editor", "Current Editor.", "GpuImg_SettingEditor"),
    },
    "keymap": {
        "addon_key": (RnaSubtab("addon_key", "Addon Keystroke", "Shortcut Combinations for Current Addon.", "GpuImg_settings_keymap_addon_key"), {
            "all": RnaSubtab("all", "All", "All Addon Keymap", "GpuImg_settings_system_all_settings"),
            "global": RnaSubtab("global", "Global", "General Keymap", "GpuImg_settings_keymap_addon_key_global"),
            "text": RnaSubtab("text", "Text", "Text Input / Scroll Keymap", "GpuImg_settings_keymap_addon_key_text"),
            "area": RnaSubtab("area", "Area", "Area Event Keymap", "GpuImg_settings_keymap_addon_key_area"),
            "valuebox": RnaSubtab("valuebox", "Value Box", "Widget / Color Panel Keymap", "GpuImg_settings_keymap_addon_key_valuebox"),
        }),
        "ops": RnaSubtab("ops", "Blender Operator", "Blender Operator Shortcut.", "GpuImg_settings_keymap_ops"),
    },
}


class SettingEditor(Window):
    __slots__ = 'active_tab', 'area_list', 'area_header', 'area_tab'

    name = 'Settings Editor'

    @staticmethod
    def r_size_default():
        blfSize(FONT0, D_SIZE['font_main'])
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        border = SIZE_dd_border[0]
        border_outer_2 = border_outer + border_outer

        return (
            border_outer_2 + AreaSettingList.r_width_default() + border_inner + (SIZE_dd_border[0] + widget_rim + widget_rim) * 2 + (SIZE_block[1] + D_SIZE['font_main_dx']) * 2 + SIZE_widget[0] + floor(blfDimen(FONT0, LONGEST_TITLE)[0]) + SIZE_block[2] + D_SIZE['widget_width'],
            border_outer_2 + border + border + D_SIZE['widget_full_h'] + border_inner + P.SettingEditor.area_height * SIZE_widget[0] + (border + widget_rim + widget_rim) * 2
        )
        #| (538, 543)
    @staticmethod
    def r_size_default_area_tab():
        blfSize(FONT0, D_SIZE['font_main'])
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        border = SIZE_dd_border[0]

        return (
            (SIZE_dd_border[0] + widget_rim + widget_rim) * 2 + (SIZE_block[1] + D_SIZE['font_main_dx']) * 2 + SIZE_widget[0] + floor(blfDimen(FONT0, LONGEST_TITLE)[0]) + SIZE_block[2] + D_SIZE['widget_width'],
            P.SettingEditor.area_height * SIZE_widget[0] + (border + widget_rim + widget_rim) * 2
        )
        #|
    @staticmethod
    def r_size_default_area_header():
        blfSize(FONT0, D_SIZE['font_main'])
        widget_rim = SIZE_border[3]

        return (
            AreaSettingList.r_width_default() + SIZE_border[1] + (SIZE_dd_border[0] + widget_rim + widget_rim) * 2 + (SIZE_block[1] + D_SIZE['font_main_dx']) * 2 + SIZE_widget[0] + floor(blfDimen(FONT0, LONGEST_TITLE)[0]) + SIZE_block[2] + D_SIZE['widget_width'],
            SIZE_dd_border[0] * 2 + D_SIZE['widget_full_h']
        )
        #|

    @staticmethod
    def open_search(
                    tx = "",
                    use_pos = False,
                    use_fit = False,
                    match_case = False,
                    match_whole_word = True,
                    match_end = 0,
                    true_ids = {"id", "keymap"}):

        w = SettingEditor(id_class="SettingEditor", use_pos=use_pos, use_fit=use_fit, pos_offset=(-150, 15))
        a = w.area_tab
        a.init_tab(("search",))
        w.upd_data()
        a.items[0].set_properties(
            tx = tx,
            match_case = match_case,
            match_whole_word = match_whole_word,
            match_end = match_end,
            true_ids = true_ids)

        for e in W_DRAW.copy():
            if e.__class__.__name__.find("DropDown") != -1:
                bring_draw_to_top_safe(e)
        #|

    def fin_callfront(self):
        self.area_header.local_tabhistory.kill()
        #|

    def init(self, boxes, blfs):
        self.active_tab = ("system",)

        # /* 0ed_SettingEditor_init
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        border = SIZE_dd_border[0]
        L0 = self.box_win.L + border_outer
        T0 = self.box_win.title_B - border_outer
        B0 = T0 - border - border - D_SIZE['widget_full_h']
        T1 = B0 - border_inner

        BB = T1 - P.SettingEditor.area_height * SIZE_widget[0] - (border + widget_rim + widget_rim) * 2
        d2 = (SIZE_dd_border[0] + widget_rim + widget_rim) * 2
        offset_x = SIZE_block[1] + D_SIZE['font_main_dx']
        # */

        self.area_list = AreaSettingList(self, L0, T1) # set_size already
        L1 = self.area_list.box_area.R + border_inner
        RR = L1 + d2 + offset_x * 2 + SIZE_widget[0] + floor(blfDimen(FONT0, LONGEST_TITLE)[0]
            ) + SIZE_block[2] + D_SIZE['widget_width']

        self.area_header = AreaSettingHeader(self, L0, RR, B0, T0, r_size_default=self.r_size_default_area_header)
        self.area_tab = AreaBlockTabSettingEditor(self, L1, RR, BB, T1, r_size_default=self.r_size_default_area_tab)

        self.areas = [
            self.area_header,
            self.area_list,
            self.area_tab
        ]
        self.area_header.history_init()
        self.area_tab.init_tab(self.active_tab, push=False)
        #|
    def upd_size_areas(self):
        # <<< 1copy (0ed_SettingEditor_init,, $$)
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        border = SIZE_dd_border[0]
        L0 = self.box_win.L + border_outer
        T0 = self.box_win.title_B - border_outer
        B0 = T0 - border - border - D_SIZE['widget_full_h']
        T1 = B0 - border_inner

        BB = T1 - P.SettingEditor.area_height * SIZE_widget[0] - (border + widget_rim + widget_rim) * 2
        d2 = (SIZE_dd_border[0] + widget_rim + widget_rim) * 2
        offset_x = SIZE_block[1] + D_SIZE['font_main_dx']
        # >>>

        self.area_list.upd_size(L0, T1)
        L1 = self.area_list.box_area.R + border_inner
        RR = L1 + d2 + offset_x * 2 + SIZE_widget[0] + floor(blfDimen(FONT0, LONGEST_TITLE)[0]
            ) + SIZE_block[2] + D_SIZE['widget_width']

        self.area_header.upd_size(L0, RR, B0, T0)
        self.area_tab.upd_size(L1, RR, BB, T1)
        #|

    def evt_redo(self):

        kill_evt_except()
        if PREF_HISTORY.index + 1 >= len(PREF_HISTORY.array):
            report('Currently in last step')
            return

        try:
            PREF_HISTORY.index += 1
            his = PREF_HISTORY.array[PREF_HISTORY.index]
            his.set_value(his.value_to)
            report(f'Redo {his.info} | value to: {his.value_to}')
        except Exception as e:

            report('Unexpected error, please report to the author')
        #|
    def evt_undo(self):

        kill_evt_except()
        his = PREF_HISTORY.array[PREF_HISTORY.index]
        if PREF_HISTORY.index == 0:
            report('Currently in first step')
            return
        try:
            his.set_value(his.value_from)
            PREF_HISTORY.index -= 1
            report(f'Undo {his.info} | value from: {his.value_from}')
        except Exception as e:

            report('Unexpected error, please report to the author')
        #|
    def evt_search(self):

        kill_evt_except()
        a = self.area_header
        a.buttons[a.ITEM_IDS["search"]].fn()
        #|
    #|
    #|
class KeymapEditor(Window):
    __slots__ = 'keyinfo', 'km', 'keyinfo_check_repeat'

    name = 'Keymap'

    @ staticmethod
    def r_size_default():
        border_outer_2 = SIZE_border[0] * 2
        widget_rim = SIZE_border[3]
        border = SIZE_dd_border[0]
        return (
            border_outer_2 + round(D_SIZE["widget_width"] * 3.731),
            border_outer_2 + (border + widget_rim + widget_rim) * 2 + SIZE_widget[0] * 8 + min(SIZE_widget[2], SIZE_widget[0]) + SIZE_border[1] * 2 + AreaKeymapCatch.r_height(None, None) + (border + widget_rim + widget_rim) * 2 + SIZE_widget[0] * 4
        )
        #|

    def init(self, boxes, blfs):
        # /* 0ed_KeymapEditor_init
        editor_width = round(D_SIZE["widget_width"] * 3.731)
        row_count_info = 8
        row_count_info_check_repeat = 4
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        border = SIZE_dd_border[0]
        LL = self.box_win.L + border_outer
        T0 = self.box_win.title_B - border_outer
        RR = LL + editor_width
        B0 = T0 - (border + widget_rim + widget_rim) * 2 - SIZE_widget[0] * row_count_info - min(SIZE_widget[2], SIZE_widget[0])
        T1 = B0 - border_inner
        B1 = T1 - AreaKeymapCatch.r_height(None, None)
        T2 = B1 - border_inner
        B2 = T2 - (border + widget_rim + widget_rim) * 2 - SIZE_widget[0] * row_count_info_check_repeat
        # */

        kw = Window.INIT_DATA
        trigger_id = kw["trigger_id"]
        trigger_index = kw["trigger_index"]
        self.km = KEYMAPS[trigger_id]

        self.keyinfo = r_keyinfo(P.keymaps.bl_rna.properties[trigger_id], trigger_id, trigger_index)
        self.keyinfo_check_repeat = ""

        a0 = AreaStringXYPre(self, input_text=self.keyinfo)
        a0.upd_size(LL, RR, B0, T0)
        a1 = AreaKeymapCatch(self, LL, RR, B1, T1, trigger_id, trigger_index)
        a2 = AreaStringXYPre(self, input_text="")
        a2.upd_size(LL, RR, B2, T2)
        self.areas = [a0, a1, a2]
        #|
    def upd_size_areas(self):
        # <<< 1copy (0ed_KeymapEditor_init,, $$)
        editor_width = round(D_SIZE["widget_width"] * 3.731)
        row_count_info = 8
        row_count_info_check_repeat = 4
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        border = SIZE_dd_border[0]
        LL = self.box_win.L + border_outer
        T0 = self.box_win.title_B - border_outer
        RR = LL + editor_width
        B0 = T0 - (border + widget_rim + widget_rim) * 2 - SIZE_widget[0] * row_count_info - min(SIZE_widget[2], SIZE_widget[0])
        T1 = B0 - border_inner
        B1 = T1 - AreaKeymapCatch.r_height(None, None)
        T2 = B1 - border_inner
        B2 = T2 - (border + widget_rim + widget_rim) * 2 - SIZE_widget[0] * row_count_info_check_repeat
        # >>>

        self.areas[0].upd_size(LL, RR, B0, T0)
        self.areas[1].upd_size(LL, RR, B1, T1)
        self.areas[2].upd_size(LL, RR, B2, T2)
        #|

    def update_keymap_info(self):
        km = self.km
        a = self.areas[1]
        self.keyinfo = r_keyinfo(P.keymaps.bl_rna.properties[a.trigger_id], a.trigger_id, a.trigger_index)
        self.areas[0].from_string(self.keyinfo)
        #|
    def update_repeat_info(self, keycatch_list, current_id_index=None):
        self.keyinfo_check_repeat = r_keyrepeatinfo(keycatch_list, current_id_index)
        self.areas[2].from_string(self.keyinfo_check_repeat)
        #|
    #|
    #|

class AreaSettingHeader(StructAreaModal):
    __slots__ = (
        'w',
        'u_draw',
        'box_area',
        'buttons',
        'local_tabhistory',
        'header_media_text',
        'focus_element',
        'r_size_default')

    ITEM_IDS = {
        'save': 0,
        'search': 1,
        'back': 2,
        'next': 3,
        'up': 4,
        'text': 5}

    def __init__(self, w, LL, RR, BB, TT, r_size_default):
        self.w = w
        self.u_draw = self.i_draw
        self.header_media_text = ""
        self.r_size_default = r_size_default

        self.box_area = GpuBox_area()

        self.buttons = [
            ButtonFnImgHover(self, RNA_header_button, save_pref, 'GpuImg_save'),
            ButtonFnImgHover(self, RNA_header_button, self.evt_tab_search, 'GpuImg_search'),
            ButtonFnImgHover(self, RNA_header_button, self.evt_tab_back, 'GpuImg_arrow_left',
                'GpuImg_arrow_left_disable'),
            ButtonFnImgHover(self, RNA_header_button, self.evt_tab_next, 'GpuImg_arrow_right',
                'GpuImg_arrow_right_disable'),
            ButtonFnImgHover(self, RNA_header_button, self.evt_tab_up, 'GpuImg_arrow_up',
                'GpuImg_arrow_up_disable'),
            ButtonStringSettingHeader(self, RNA_header_media_text, self),
        ]
        self.buttons[2].dark()
        self.buttons[3].dark()
        self.buttons[4].dark()
        self.upd_size(LL, RR, BB, TT)
        #|

    def upd_size(self, LL, RR, BB, TT):
        self.box_area.LRBT_upd(LL, RR, BB, TT)
        d0 = SIZE_dd_border[0]
        widget_rim = SIZE_border[3]
        h = SIZE_widget[0]
        d1 = floor(h / 5)

        LL += d0
        TT -= d0
        BB += d0
        T = TT - widget_rim
        B = BB + widget_rim

        L = LL + widget_rim
        R = L + h
        buttons = self.buttons
        B = buttons[0].init_bat(L, R, T)
        L = R + h
        R = L + h
        B = buttons[1].init_bat(L, R, T)
        L = R + d1 + d1
        R = L + h
        B = buttons[2].init_bat(L, R, T)
        L = R
        R = L + h
        B = buttons[3].init_bat(L, R, T)
        L = R + d1
        R = L + h
        B = buttons[4].init_bat(L, R, T)
        buttons[5].init_bat(R + d1, RR - d0, TT)
        #|

    def resize_upd_end(self):
        if hasattr(self.w, "areas") and P.adaptive_win_resize:
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
        #|

    def r_focus_element(self):
        for e in self.buttons:
            if e.inside(MOUSE): return e
        return None

    def history_init(self):

        self.local_tabhistory = LocalHistory(self, P.undo_steps_local, self.r_push_tabitem)
        #|
    def r_push_tabitem(self):
        return self.w.active_tab
        #|
    def to_tabhistory_index(self, index):
        Admin.REDRAW()
        w = self.w
        e = self.local_tabhistory.array[index]
        w.active_tab = e
        a = w.area_tab
        a.active_tab = e
        a.init_tab(e, push=False)
        #|
    def tabhistory_push(self):
        self.local_tabhistory.push()
        self.update_button_darklight()
        self.buttons[AreaSettingHeader.ITEM_IDS['text']].init_buttons(self.w.active_tab)
        #|
    def evt_tab_back(self):
        Admin.REDRAW()
        kill_evt_except()
        his = self.local_tabhistory
        if his.index == 0:

            return

        his.index -= 1
        self.to_tabhistory_index(his.index)
        self.update_button_darklight()
        self.buttons[AreaSettingHeader.ITEM_IDS['text']].init_buttons(self.w.active_tab)
        self.w.upd_data()
        #|
    def evt_tab_next(self):
        Admin.REDRAW()
        kill_evt_except()
        his = self.local_tabhistory
        if his.index + 1 >= len(his.array):

            return

        his.index += 1
        self.to_tabhistory_index(his.index)
        self.update_button_darklight()
        self.buttons[AreaSettingHeader.ITEM_IDS['text']].init_buttons(self.w.active_tab)
        self.w.upd_data()
        #|
    def evt_tab_up(self):
        Admin.REDRAW()
        kill_evt_except()
        current_tab = self.w.active_tab
        if not current_tab: return
        if len(current_tab) == 1:

            return

        self.w.active_tab = current_tab[: -1]
        self.w.upd_data()
        #|
    def evt_tab_search(self):
        Admin.REDRAW()
        kill_evt_except()
        self.w.active_tab = ("search",)
        self.w.upd_data()
        a = self.w.area_tab
        a.items[0].buttons[0].to_dropdown()
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)
        for e in self.buttons: e.dxy(dx, dy)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        for e in self.buttons: e.draw_box()

        for e in self.buttons: e.draw_blf()
        #|

    def update_button_darklight(self):
        his_index = self.local_tabhistory.index
        if his_index > 0:
            self.buttons[AreaSettingHeader.ITEM_IDS["back"]].light()
        else:
            self.buttons[AreaSettingHeader.ITEM_IDS["back"]].dark()
        if his_index == len(self.local_tabhistory.array) - 1:
            self.buttons[AreaSettingHeader.ITEM_IDS["next"]].dark()
        else:
            self.buttons[AreaSettingHeader.ITEM_IDS["next"]].light()

        if self.w.active_tab and len(self.w.active_tab) != 1:
            self.buttons[AreaSettingHeader.ITEM_IDS["up"]].light()
        else:
            self.buttons[AreaSettingHeader.ITEM_IDS["up"]].dark()
        #|
    def upd_data(self):
        self.update_button_darklight()
        #|
    #|
    #|
class AreaSettingList(StructAreaModal):
    __slots__ = (
        'w',
        'u_draw',
        'items',
        'box_area',
        'box_background',
        'box_hover',
        'box_active',
        'active_tab',
        'focus_element')

    ITEM_IDS = {
        'system': 0,
        'size': 1,
        'personalization': 2,
        'apps': 3,
        'keymap': 4}

    @staticmethod
    def r_width_default():
        blfSize(FONT0, D_SIZE['font_main'])
        return SIZE_dd_border[0] * 2 + (SIZE_setting_list_border[0] + D_SIZE['font_main_dy']) * 2 + SIZE_widget[0] + round(
            blfDimen(FONT0, "Personalization")[0])
        #|

    def __init__(self, w, LL, TT):
        #|
        self.w = w
        self.u_draw = self.i_draw

        self.box_area = GpuBox_area()
        self.box_background = GpuBox_box_setting_list_bg()
        self.box_hover = GpuRimAreaHover()
        self.box_active = GpuRimSettingTabActive()
        self.box_active.upd()
        self.active_tab = None

        bufn = self.evt_button
        f0 = self.button_inside_evt_callback
        f1 = self.button_outside_evt_callback
        self.items = [
            ButtonFnImgList(self, None, lambda: bufn('system'),
                'GpuImg_settings_system', 'System', None, f0, f1),
            ButtonFnImgList(self, None, lambda: bufn('size'),
                'GpuImg_settings_size', 'Size', None, f0, f1),
            ButtonFnImgList(self, None, lambda: bufn('personalization'),
                'GpuImg_settings_personalization', 'Personalization', None, f0, f1),
            ButtonFnImgList(self, None, lambda: bufn('apps'),
                'GpuImg_settings_apps', 'Apps', None, f0, f1),
            ButtonFnImgList(self, None, lambda: bufn('keymap'),
                'GpuImg_settings_keymap', 'Keymap', None, f0, f1),
        ]
        self.upd_size(LL, TT)
        #|

    def upd_size(self, LL, TT):
        box_area = self.box_area
        d0 = SIZE_dd_border[0]
        scissor_win = self.w.scissor
        h = SIZE_widget[0]
        outer = SIZE_setting_list_border[0]

        L0 = LL + d0
        T0 = TT - d0
        B = T0 - outer

        # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_main'}$)
        blfSize(FONT0, D_SIZE['font_main'])
        blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
        # >>>
        ButtonFnImgList.set_offset(L0, D_SIZE['font_main_dy'], outer, h)
        gap = SIZE_setting_list_border[1]
        R = ButtonFnImgList.BLF_X + round(
            blfDimen(FONT0, "Personalization")[0]) + ButtonFnImgList.BLF_OFFSET_Y + outer

        for e in self.items: B = e.init_bat_dimen(L0, R, B) - gap

        B = B + gap - outer
        self.box_background.LRBT_upd(L0, R, B, T0)
        box_area.LRBT_upd(LL, R + d0, B - d0, TT)
        self.box_hover.LRBT_upd(0, 0, 0, 0, 0)
        # <<< 1copy (0areas_AreaSettingList_update_box_active,, $$)
        self.active_tab = self.w.active_tab
        if self.active_tab and self.active_tab[0] != "search":
            tab = self.active_tab[0]
            widget_rim = SIZE_border[3]
            e = self.items[AreaSettingList.ITEM_IDS[self.active_tab[0]]].box_button
            self.box_active.LRBT_upd(self.box_area.L, self.box_area.R,
                e.B - widget_rim, e.T + widget_rim, widget_rim)
        else:
            if self.box_active.d != 0: self.box_active.LRBT_upd(0, 0, 0, 0, 0)
        # >>>
        #|

    def r_focus_element(self):
        for e in self.items:
            if e.inside(MOUSE): return e
        return None
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)
        self.box_background.dxy_upd(dx, dy)
        self.box_hover.dxy_upd(dx, dy)
        self.box_active.dxy_upd(dx, dy)

        for e in self.items: e.dxy(dx, dy)
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        self.box_background.bind_draw()
        self.box_active.bind_draw()
        self.box_hover.bind_draw()

        for e in self.items: e.draw_box()

        blfColor(FONT0, *COL_box_setting_list_fg)
        blfSize(FONT0, D_SIZE['font_main'])
        for e in self.items:
            o = e.blf_value
            blfPos(FONT0, o.x, o.y, 0)
            blfDraw(FONT0, o.text)
        #|

    def evt_button(self, identifier):

        Admin.REDRAW()
        w = self.w
        w.active_tab = (identifier,)
        w.area_tab.init_tab(self.w.active_tab, evtkill=False)
        w.upd_data()
        #|
    def button_inside_evt_callback(self, button):
        widget_rim = SIZE_border[3]
        e = button.box_button
        self.box_hover.LRBT_upd(self.box_area.L, self.box_area.R,
            e.B - widget_rim, e.T + widget_rim, widget_rim)
        #|
    def button_outside_evt_callback(self, button):
        if self.box_hover.d != 0: self.box_hover.LRBT_upd(0, 0, 0, 0, 0)
        #|

    def upd_data(self):
        if self.active_tab == self.w.active_tab: return

        # /* 0areas_AreaSettingList_update_box_active
        self.active_tab = self.w.active_tab
        if self.active_tab and self.active_tab[0] != "search":
            tab = self.active_tab[0]
            widget_rim = SIZE_border[3]
            e = self.items[AreaSettingList.ITEM_IDS[self.active_tab[0]]].box_button
            self.box_active.LRBT_upd(self.box_area.L, self.box_area.R,
                e.B - widget_rim, e.T + widget_rim, widget_rim)
        else:
            if self.box_active.d != 0: self.box_active.LRBT_upd(0, 0, 0, 0, 0)
        # */
    #|
    #|
class AreaKeymapCatch(StructAreaModal):
    __slots__ = (
        'w',
        'u_draw',
        'items',
        'box_area',
        'box_background',
        'blf_title',
        'button_keycombcatch',
        'button_save',
        'button_clear',
        'trigger_id',
        'trigger_index',
        'keycombcatch',
        'focus_element',
        'keycatch_list',
        'km')

    @staticmethod
    def r_height(L, R):
        T = 0
        widget_rim = SIZE_border[3]
        T = T - SIZE_dd_border[0]
        offset = widget_rim + D_SIZE['font_main_dx']
        y0 = T - offset - D_SIZE['font_subtitle_dT']
        button_keycombcatch_T = y0 - offset - D_SIZE['font_subtitle_dy']
        B = button_keycombcatch_T - D_SIZE['widget_full_h']
        button_save_T = B - SIZE_button[1] * 2 - SIZE_button[2]
        B = button_save_T - D_SIZE['widget_full_h']
        B -= SIZE_border[3] + offset + widget_rim
        return - B
        #|

    def __init__(self, w, LL, RR, BB, TT, trigger_id, trigger_index):
        self.w = w
        self.km = KEYMAPS[trigger_id]
        self.u_draw = self.i_draw
        self.trigger_id = trigger_id
        self.trigger_index = trigger_index
        self.box_area = GpuBox_area()
        self.box_background = GpuBox_box_setting_list_bg()

        self.blf_title = BlfColor("Place your mouse over this area and press the desired key",
            color=COL_block_fg_info)
        self.keycombcatch = ""
        self.keycatch_list = []
        self.button_keycombcatch = ButtonString(self, RNA_keycombcatch, self)
        self.button_save = ButtonFn(self, RNA_keycatch_save, self.bufn_save)
        self.button_clear = ButtonFn(self, RNA_keycatch_clear, self.bufn_clear)

        self.upd_size(LL, RR, BB, TT)
        #|

    def upd_size(self, LL, RR, BB, TT):
        d0 = SIZE_dd_border[0]
        widget_rim = SIZE_border[3]
        self.box_area.LRBT_upd(LL, RR, BB, TT)
        L = LL + d0
        R = RR - d0
        B = BB + d0
        T = TT - d0
        self.box_background.LRBT_upd(L, R, B, T)

        offset = widget_rim + D_SIZE['font_main_dx']
        L0 = L + offset
        x0 = L0 + D_SIZE['font_subtitle_dx']
        y0 = T - offset - D_SIZE['font_subtitle_dT']
        self.blf_title.x = x0
        self.blf_title.y = y0

        B = self.button_keycombcatch.init_bat(L0, R - offset, y0 - offset - D_SIZE['font_subtitle_dy'])
        T0 = B - SIZE_button[1] * 2 - SIZE_button[2]
        self.button_save.init_bat(L0 + widget_rim, RR, T0)
        self.button_clear.init_bat(self.button_save.box_button.R + SIZE_button[1], RR, T0)
        #|

    def r_focus_element(self):
        e = None
        if self.button_keycombcatch.inside(MOUSE): e = self.button_keycombcatch
        elif self.button_save.inside(MOUSE): e = self.button_save
        elif self.button_clear.inside(MOUSE): e = self.button_clear
        return e
        #|

    def modal_focus_element_back(self, e):
        if EVT_TYPE[1] == "PRESS":
            if len(self.keycatch_list) >= 4: del self.keycatch_list[0]
            if EVT_TYPE[0] not in {None, '', 'NONE', 'MOUSEMOVE', 'INBETWEEN_MOUSEMOVE'}:
                k = f'{EVT_TYPE[0]}'
                if k not in self.keycatch_list:
                    self.keycatch_list.append(k)
                    self.button_keycombcatch.set(", ".join(self.keycatch_list), refresh=False, undo_push=False)
                    self.button_keycombcatch.upd_data()
                    self.w.update_repeat_info(self.keycatch_list, (self.trigger_id, self.trigger_index))
                    Admin.REDRAW()
        return False
        #|

    def bufn_save(self, refresh=True):

        km = KEYMAPS[self.trigger_id]
        oldvalue = ", ".join(km.types0  if self.trigger_index == 0 else km.types1)
        success = write_keytype_with_report(self.keycombcatch, self.trigger_id, self.trigger_index)
        if success:
            save_pref()
            km = KEYMAPS[self.trigger_id]
            newvalue = ", ".join(km.types0  if self.trigger_index == 0 else km.types1)
            def set_value(v):
                write_keytype_with_report(v, self.trigger_id, self.trigger_index)
                update_data()
                Admin.REDRAW()
                #|
            PREF_HISTORY.push_context = HistoryValue(oldvalue, newvalue, set_value, "KeyComb")
            PREF_HISTORY.push()
        if refresh: update_data()
        Admin.REDRAW()
        #|
    def bufn_clear(self, refresh=True):

        self.keycatch_list.clear()
        self.button_keycombcatch.set("", undo_push=False)
        self.button_keycombcatch.upd_data()
        self.w.update_repeat_info(self.keycatch_list, (self.trigger_id, self.trigger_index))
        Admin.REDRAW()
        #|

    def dxy(self, dx, dy):
        self.box_area.dxy_upd(dx, dy)
        self.box_background.dxy_upd(dx, dy)
        self.button_keycombcatch.dxy(dx, dy)
        self.button_save.dxy(dx, dy)
        self.button_clear.dxy(dx, dy)

        self.blf_title.x += dx
        self.blf_title.y += dy
        #|

    def i_draw(self):
        blend_set('ALPHA')
        self.box_area.bind_draw()
        self.box_background.bind_draw()
        self.button_keycombcatch.draw_box()
        self.button_save.draw_box()
        self.button_clear.draw_box()

        self.button_keycombcatch.draw_blf()
        self.button_save.draw_blf()
        self.button_clear.draw_blf()

        e = self.blf_title
        blfSize(FONT0, D_SIZE['font_subtitle'])
        blfColor(FONT0, *e.color)
        blfPos(FONT0, e.x, e.y, 0)
        blfDraw(FONT0, e.text)
        #|

    def upd_data(self):

        self.button_keycombcatch.upd_data()
        if self.km is KEYMAPS[self.trigger_id]: return
        self.km = KEYMAPS[self.trigger_id]

        self.w.update_repeat_info(self.keycatch_list, (self.trigger_id, self.trigger_index))
        self.w.update_keymap_info()
        #|
    #|
    #|


class AreaBlockTabSettingEditor(AreaBlockTab):
    __slots__ = 'width_wrap', 'upd_data_callback'

    about = ""

    def upd_size_callback(self):
        self.width_wrap = self.width_input - D_SIZE['font_main_title_offset'] * 2
        #|

    def init_tab(self, tab, push=True, evtkill=True):
        super().init_tab(tab, push=push, evtkill=evtkill)

        for e in self.items: e.upd_data()
        #|
    def tabhistory_push(self):
        self.w.area_header.tabhistory_push()
        #|

    def init_tab_search(self):

        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold_search
        self.items[:] = [BlockPrefSearchHead(self)]
        #|

    def init_tab_system(self):
        rnas = RNAS["system"]
        bufn = self.r_init_tab("system")

        self.items[:] = [BlockSubtab(self, (v[0]  if isinstance(v, tuple) else v), bufn)  for v in rnas.values()]
        #|
    def init_tab_system_display(self):
        rnas = P.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, P, rnas[k])  for k in (
            "sys_auto_off",
            "show_length_unit",
            "win_check_overlap",
            "win_overlap_offset",
            "filter_match_case",
            "filter_match_whole_word",
            "filter_match_end",
            "cursor_beam_time",
            "use_select_all",
            "use_py_exp",
            "show_rm_keymap",
            "format_float",
            "format_hex",
            "cursor_pan",
            "cursor_picker",
            "font_shadow_method",
        )]
        #|
    def init_tab_system_control(self):
        rnas = P.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, P, rnas[k])  for k in (
            "lock_win_size",
            "lock_list_size",
            "adaptive_win_resize",
            "th_drag",
            "th_double_click",
            "win_check_overlap",
            "win_overlap_offset",
            "filter_match_case",
            "filter_match_whole_word",
            "filter_match_end",
            "filter_autopan_active",
            "filter_adaptive_selection",
            "filter_delete_behavior",
            "use_select_all",
            "pan_invert",
            "scroll_distance",
            "valbox_drag_fac_int",
            "valbox_drag_fac_float",
            "button_repeat_time",
            "button_repeat_interval",
            "use_py_exp",
            "adaptive_enum_input",
            "undo_steps_local",
            "anim_filter",
            "animtime_filter",
        )]
        #|
    def init_tab_system_menu(self):
        rnas = P.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, P, rnas[k])  for k in (
            "show_length_unit",
            "lock_win_size",
            "win_check_overlap",
            "win_overlap_offset",
            "filter_match_case",
            "filter_match_whole_word",
            "filter_match_end",
            "filter_autopan_active",
            "filter_adaptive_selection",
            "filter_delete_behavior",
            "cursor_beam_time",
            "use_select_all",
            "pan_invert",
            "scroll_distance",
            "valbox_drag_fac_int",
            "valbox_drag_fac_float",
            "button_repeat_time",
            "button_repeat_interval",
            "use_py_exp",
            "show_rm_keymap",
            "adaptive_enum_input",
            "format_float",
            "format_hex",
        )]
        #|
    def init_tab_system_expression(self):
        rnas = P.bl_rna.properties
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [self.r_block_calc_exp(self)]
        #|
    def init_tab_system_library(self):
        rnas = P.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [
            self.r_block_md_lib_refresh(self),
            self.r_block_md_lib_filepath(self),
            r_button(self, P, rnas["md_lib_filter"]),
            r_button(self, P, rnas["md_lib_method"]),
            r_button(self, P, rnas["md_lib_use_essentials"]),
        ]
        #|
    def init_tab_system_all_settings(self):

        r_button = self.r_button
        r_button_fn = self.r_button_fn
        r_button_size = self.r_button_size
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        b0 = self.r_block_pref_importexport(self)
        b0.buttons.append(ButtonSep(3))

        b_general = BlockUtilHeavy(self, None, title='General')
        b_general.items = [r_button(b_general, P, rna)  for rna in P_BL_RNA_PROPS]

        pp = P.size
        rnas = pp.bl_rna.properties
        b_size = BlockUtilHeavy(self, None, title='Size')
        b_size.use_anim_slot = False
        b_size_b0 = Blocks(b_size)
        b_size_b0.no_background()
        b_size_b0_buttons = [
            BuFunction2(b_size, [RNA_ui_scale_100, RNA_ui_scale_133],
                [
                    lambda: bpy.ops.wm.vmd_ui_scale(factor=1.0),
                    lambda: bpy.ops.wm.vmd_ui_scale(factor=1.33),
                ], False
            ),
            BuFunction2(b_size, [RNA_ui_scale_166, RNA_ui_scale_200],
                [
                    lambda: bpy.ops.wm.vmd_ui_scale(factor=1.66),
                    lambda: bpy.ops.wm.vmd_ui_scale(factor=2.0),
                ], False
            ),
            ButtonSep(),
            BuFunction(b_size, RNA_ui_reload_icon, reload_icon, False),
        ]
        for r in {0, 1, 3}:
            o = b_size_b0_buttons[r]
            o.init_bat = o.init_bat_anim

        b_size_b0.buttons = b_size_b0_buttons
        b_size.items = [b_size_b0] + [
            r_button_size(b_size, pp, rnas[k])  for k in pp.__annotations__]

        pp = P.color
        rnas = pp.bl_rna.properties
        b_color = BlockUtilHeavy(self, None, title='Color')
        b_color_b0 = self.r_block_pref_importexport_theme(b_color)
        b_color_b0.no_background()
        b_color_b0.buttons.append(ButtonSep(3))
        b_color.items = [
            b_color_b0
            ] + [r_button(b_color, pp, rnas[k])  for k in pp.__annotations__]

        b_editor = BlockUtil(self, None, title='Editor')
        b_editor_items = []

        b_keymap = BlockUtilHeavy(self, None, title='Keymap')
        b_keymap.items = [BlockPrefKeystroke(b_keymap, k)  for k in KEYMAPS]

        for clsname, cls in m.D_EDITOR.items():
            pp = getattr(P, clsname, None)
            if pp is None: continue

            newblock = BlockUtilHeavy(b_editor, None, title=cls.name)
            rnas = pp.bl_rna.properties
            edname = cls.name + ': '
            size_attrs = getattr(pp, 'SIZE_CALLBACKS', {})

            newblock.items = [(r_button_size  if k in size_attrs else r_button)(
                newblock, pp, rnas[k], title=rnas[k].name.replace(edname, ''))  for k in pp.__annotations__]

            b_editor_items.append(newblock)

        b_editor.items = b_editor_items

        b_other = BlockUtilHeavy(self, None, title='Other')
        b_other.items = [
            self.r_block_calc_exp(b_other),
            self.r_block_md_lib_refresh(b_other),
            self.r_block_md_lib_filepath(b_other),
            r_button_fn(b_other, RNA_pref_load_theme_dark, lambda: load_theme("DARK")),
        ]

        self.items[:] = [
            b0,
            b_general,
            b_size,
            b_color,
            b_keymap,
            b_editor,
            b_other,
        ]
        #|
    def init_tab_system_about(self):

        if not AreaBlockTabSettingEditor.about: AreaBlockTabSettingEditor.about = r_about()

        b0 = Blocks(self)
        b0.buttons = [AreaStringXYButton(b0, self, AreaBlockTabSettingEditor.about, self.width_input - D_SIZE['font_main_dx'] * 2, FONT0)]
        self.items[:] = [b0]
        #|

    def init_tab_size(self):

        rnas = RNAS["size"]
        r_button_fn = self.r_button_fn
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [
            BlockSubtab(self, rnas["ui_size"], lambda: self.init_tab(("size", "ui_size"))),
            r_button_fn(self, RNA_ui_scale_100, lambda: bpy.ops.wm.vmd_ui_scale(factor=1.0)),
            r_button_fn(self, RNA_ui_scale_133, lambda: bpy.ops.wm.vmd_ui_scale(factor=1.33)),
            r_button_fn(self, RNA_ui_scale_166, lambda: bpy.ops.wm.vmd_ui_scale(factor=1.66)),
            r_button_fn(self, RNA_ui_scale_200, lambda: bpy.ops.wm.vmd_ui_scale(factor=2.0)),
        ]
        #|
    def init_tab_size_ui_size(self):

        pp = P.size
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        r_button_size = self.r_button_size
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        b0 = BlockUtil(self, None, title="Background")
        b0.items = [
            r_button_size(b0, pp, rnas["widget"]),
            r_button_size(b0, pp, rnas["title"]),
            r_button_size(b0, pp, rnas["border"]),
            r_button_size(b0, pp, rnas["dd_border"]),
            r_button_size(b0, pp, rnas["filter"]),
            r_button_size(b0, pp, rnas["tb"]),
            r_button_size(b0, pp, rnas["win_shadow_offset"]),
            r_button_size(b0, pp, rnas["dd_shadow_offset"]),
            r_button_size(b0, pp, rnas["shadow_softness"]),
            r_button_size(b0, pp, rnas["setting_list_border"]),
            r_button_size(b0, pp, rnas["block"]),
            r_button_size(b0, pp, rnas["button"]),
            r_button_size(b0, pp, rnas["preview"]),
        ]

        b1 = BlockUtil(self, None, title="Foreground")
        b1.items = [
            r_button_size(b1, pp, rnas["foreground"]),
            r_button_size(b1, pp, rnas["foreground_height"]),
            r_button_size(b1, pp, rnas["widget_fac"]),
        ]

        rnas = P.bl_rna.properties
        self_items = self.items

        self_items[:] = [
            self.r_button_fn(self, RNA_ui_reload_icon, reload_icon),
            b0,
            b1,
            r_button(self, P, rnas["preview_scale"]),
            r_button(self, P, rnas["blocklist_column_len"]),
        ]

        for clsname, cls in m.D_EDITOR.items():
            pp = getattr(P, clsname, None)
            if pp is None: continue

            size_attrs = getattr(pp, 'SIZE_CALLBACKS', None)
            if size_attrs is None: continue

            rnas = pp.bl_rna.properties
            blocktitle = cls.name
            newblock = BlockUtil(self, None, title=blocktitle)
            blocktitle += ': '
            newblock.items = [r_button_size(newblock, pp, rnas[k], title=rnas[k].name.replace(blocktitle, ''))  for k in size_attrs]
            self_items.append(newblock)
        #|

    def init_tab_personalization(self):

        rnas = RNAS["personalization"]
        bufn = self.r_init_tab("personalization")

        self.items[:] = [BlockSubtab(self, (v[0]  if isinstance(v, tuple) else v), bufn)  for v in rnas.values()]
        #|
    def init_tab_personalization_ui_color(self):

        rnas = RNAS["personalization"]["ui_color"][1]
        bufn = self.r_init_tab(("personalization", "ui_color"))

        self.items[:] = [BlockSubtab(self, (v[0]  if isinstance(v, tuple) else v), bufn)  for v in rnas.values()]
        #|
    def init_tab_personalization_ui_color_all(self):

        pp = P.color
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, pp, rnas[k])  for k in pp.__annotations__]
        #|
    def init_tab_personalization_ui_color_window(self):

        pp = P.color
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, pp, rnas[k])  for k in pp.__annotations__  if (k.startswith("win_") or k == "win")]
        #|
    def init_tab_personalization_ui_color_menu(self):

        pp = P.color
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, pp, rnas[k])  for k in pp.__annotations__  if not (k.startswith("win_") or k == "win")]
        #|
    def init_tab_personalization_ui_color_foreground(self):

        pp = P.color
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, pp, rnas[k])  for k in pp.__annotations__  if rnas[k].is_hidden]
        #|
    def init_tab_personalization_ui_color_hover(self):

        pp = P.color
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, pp, rnas[k])  for k in pp.__annotations__  if k.find('_hover') != -1]
        #|
    def init_tab_personalization_ui_color_taskbar(self):

        pp = P.color
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [r_button(self, pp, rnas[k])  for k in ('box_tb', 'box_tb_multibar')]
        #|
    def init_tab_personalization_shadow(self):

        pp = P.color
        rnas = pp.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [
            r_button(self, pp, rnas["win_shadow"]),
            r_button(self, pp, rnas["dd_shadow"]),
            r_button(self, pp, rnas["font_shadow"]),
        ]

        pp = P.size
        rnas = pp.bl_rna.properties
        r_button_size = self.r_button_size

        self.items += [
            r_button_size(self, pp, rnas["win_shadow_offset"]),
            r_button_size(self, pp, rnas["dd_shadow_offset"]),
            r_button_size(self, pp, rnas["shadow_softness"]),
            r_button(self, P, P_BL_RNA_PROPS["font_shadow_method"]),
            r_button(self, P, P_BL_RNA_PROPS["font_shadow_hardness"]),
            r_button(self, P, P_BL_RNA_PROPS["font_shadow_offset"]),
        ]
        #|
    def init_tab_personalization_font(self):

        rnas = RNAS["personalization"]["font"][1]
        bufn = self.r_init_tab(("personalization", "font"))

        self.items[:] = [BlockSubtab(self, (v[0]  if isinstance(v, tuple) else v), bufn)  for v in rnas.values()]
        #|
    def init_tab_personalization_font_text_rendering(self):

        rnas = P.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        b_font_shadow_method = r_button(self, P, rnas["font_shadow_method"])
        b_font_shadow_hardness = r_button(self, P, rnas["font_shadow_hardness"])
        b_font_shadow_offset = r_button(self, P, rnas["font_shadow_offset"])
        b_font_shadow_color = r_button(self, P.color, P.color.bl_rna.properties["font_shadow"])

        self.items[:] = [
            b_font_shadow_method,
            b_font_shadow_hardness,
            b_font_shadow_offset,
            b_font_shadow_color,
        ]

        def upd_data_callback():
            if P.font_shadow_method == "CUSTOM":
                if b_font_shadow_hardness.button0.isdark is True:
                    b_font_shadow_hardness.button0.light()
                    b_font_shadow_offset.button0.light()
                    b_font_shadow_color.button0.light()
            else:
                if b_font_shadow_hardness.button0.isdark is False:
                    b_font_shadow_hardness.button0.dark()
                    b_font_shadow_offset.button0.dark()
                    b_font_shadow_color.button0.dark()

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_personalization_font_color(self): self.init_tab_personalization_ui_color_foreground()
    def init_tab_personalization_font_path(self):

        rnas = P.bl_rna.properties
        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        b_fontpath_method = r_button(self, P, rnas["fontpath_method"])
        b_fontpath_ui = r_button(self, P, rnas["fontpath_ui"])
        b_fontpath_ui_mono = r_button(self, P, rnas["fontpath_ui_mono"])

        o_fontpath_ui = b_fontpath_ui.button0
        o_fontpath_ui_mono = b_fontpath_ui_mono.button0

        self.items[:] = [
            b_fontpath_method,
            b_fontpath_ui,
            b_fontpath_ui_mono,
        ]

        def upd_data_callback():
            if P.fontpath_method == "CUSTOM":
                if o_fontpath_ui.isdark is True:
                    o_fontpath_ui.light()
                    o_fontpath_ui_mono.light()
            else:
                if o_fontpath_ui.isdark is False:
                    o_fontpath_ui.dark()
                    o_fontpath_ui_mono.dark()

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_personalization_theme(self):

        r_button = self.r_button
        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold

        self.items[:] = [
            self.r_block_pref_importexport_theme(self),
            self.r_button_fn(self, RNA_pref_load_theme_dark, lambda: load_theme("DARK"))
        ]
        #|

    def init_tab_apps(self):

        rnas = RNAS["apps"]
        bufn = self.r_init_tab("apps")

        self.items[:] = [BlockSubtab(self, (v[0]  if isinstance(v, tuple) else v), bufn)  for v in rnas.values()]
        #|
    def init_tab_except(self):

        active_tab = self.active_tab
        if isinstance(active_tab, tuple) and len(active_tab) == 2 and active_tab[0] == "apps":
            name = active_tab[1]
            if name in m.D_EDITOR:
                pp = getattr(P, name, None)
                if pp is None: return
                rnas = pp.bl_rna.properties
                r_button = self.r_button
                BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
                edname = m.D_EDITOR[name].name + ': '

                self.items[:] = [r_button(self, pp, rnas[k], title=rnas[k].name.replace(edname, ''))  for k in pp.__annotations__]
        #|

    def init_tab_keymap(self):

        rnas = RNAS["keymap"]
        bufn = self.r_init_tab("keymap")

        self.items[:] = [BlockSubtab(self, (v[0]  if isinstance(v, tuple) else v), bufn)  for v in rnas.values()]
        #|
    def init_tab_keymap_addon_key(self):

        rnas = RNAS["keymap"]["addon_key"][1]
        bufn = self.r_init_tab(("keymap", "addon_key"))

        self.items[:] = [BlockSubtab(self, (v[0]  if isinstance(v, tuple) else v), bufn)  for v in rnas.values()]
        #|
    def init_tab_keymap_addon_key_all(self):

        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
        self.items[:] = [BlockPrefKeystroke(self, k)  for k in KEYMAPS]
        #|
    def init_tab_keymap_addon_key_global(self):

        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
        self.items[:] = [BlockPrefKeystroke(self, k)  for k in (
            'esc',
            'dd_esc',
            'click',
            'title_move',
            'title_button',
            'resize',
            'pan',
            'pan_win',
            'rm',
            'rm_km_toggle',
            'rm_km_change',
            'redo',
            'undo',
            'detail',
            'fold_all_recursive_toggle',
            'fold_all_toggle',
            'fold_recursive_toggle',
            'fold_toggle',
            'rename',
        )]
        #|
    def init_tab_keymap_addon_key_text(self):

        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
        self.items[:] = [BlockPrefKeystroke(self, k)  for k in KEYMAPS  if k.startswith("dd_")]
        #|
    def init_tab_keymap_addon_key_area(self):

        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
        self.items[:] = [BlockPrefKeystroke(self, k)  for k in KEYMAPS  if k.startswith("area_")]
        #|
    def init_tab_keymap_addon_key_valuebox(self):

        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
        self.items[:] = [BlockPrefKeystroke(self, k)  for k in KEYMAPS  if k.startswith("valbox_")]
        #|
    def init_tab_keymap_ops(self):

        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
        r_button_fn = self.r_button_fn

        items = [
            BlockFull(self, ButtonFn(None, RNA_ops_refresh, self.bufn_ops_refresh)),
            BlockFull(self, ButtonSep())]

        kms = bpy.context.window_manager.keyconfigs.user.keymaps

        for cls in m.OPERATORS:
            bl_keymap = r_bl_keymap(cls.bl_idname, kms)

            rna = RnaButton(
                cls.__name__,
                name = cls.bl_label,
                button_text = "None"  if bl_keymap is None else bl_keymap.keymap_items[cls.bl_idname].to_string(),
                description = cls.bl_description)
            rna.data = RnaDataOps(
                cls.bl_idname,
                cls.bl_keycategory  if hasattr(cls, "bl_keycategory") else "Mesh")

            items.append(r_button_fn(self, rna, bufn_ops_editkey))

        self.items[:] = items
        #|

    def r_init_tab(self, parent_tab):
        if isinstance(parent_tab, tuple):
            return lambda button=None: self.init_tab(parent_tab + (button.rna.identifier, ))
        return lambda button=None: self.init_tab((parent_tab, button.rna.identifier))
        #|
    def r_button(self, w, pp, rna, title=None):
        ty = rna.type
        if ty == "BOOLEAN":
            o = BuBoolPref(None, rna, lambda: pp, None, '', False)
            o.init_bat = o.init_bat_animR
            out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
            out.use_anim_slot = False
            out.blf_title.text = rna.name  if title is None else title
            return out
        elif ty == "INT":
            if rna.is_array:
                if rna.subtype in D_subtype_display:
                    o = BuIntVecSubPref(None, rna, lambda: pp, None, '', False)
                    o.init_subtype(D_subtype_display[rna.subtype])
                    o.init_bat = o.init_bat_anim
                    out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
                    out.use_anim_slot = False
                    out.blf_title.text = rna.name  if title is None else title
                    return out
                else:
                    o = BuIntVecPref(None, rna, lambda: pp, None, '', False)
                    o.init_bat = o.init_bat_anim
                    out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
                    out.use_anim_slot = False
                    out.blf_title.text = rna.name  if title is None else title
                    return out
            else:
                o = BuIntPref(None, rna, lambda: pp, None, '', False)
                o.init_bat = o.init_bat_anim
                out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
                out.use_anim_slot = False
                out.blf_title.text = rna.name  if title is None else title
                return out
        elif ty == "FLOAT":
            if rna.is_array:
                if rna.subtype == "COLOR":
                    o = BuColorPref(None, rna, lambda: pp, None, '', False, "sRGB"  if rna.is_hidden else "GPU Shader")

                    if rna.array_length == 3:
                        o.init_bat = o.init_bat_anim_3
                    else:
                        o.init_bat = o.init_bat_anim_4

                    o.set_callback = Admin.REDRAW

                    out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
                    out.use_anim_slot = False
                    out.blf_title.text = rna.name  if title is None else title
                    return out

                elif rna.subtype in D_subtype_display:
                    o = BuFloatVecSubPref(None, rna, lambda: pp, None, '', False)
                    o.init_subtype(D_subtype_display[rna.subtype])
                    o.init_bat = o.init_bat_anim
                    out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
                    out.use_anim_slot = False
                    out.blf_title.text = rna.name  if title is None else title
                    return out
                else:
                    o = BuFloatVecPref(None, rna, lambda: pp, None, '', False)
                    o.init_bat = o.init_bat_anim
                    out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
                    out.use_anim_slot = False
                    out.blf_title.text = rna.name  if title is None else title
                    return out
            else:
                o = BuFloatPref(None, rna, lambda: pp, None, '', False)
                o.init_bat = o.init_bat_anim
                out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
                out.use_anim_slot = False
                out.blf_title.text = rna.name  if title is None else title
                return out
        elif ty == "ENUM":
            o = BuEnumPref(None, rna, lambda: pp, None, '', False)
            o.box_icon_arrow = GpuImg_unfold()
            o.enum_items = rna.enum_items
            o.init_bat = o.init_bat_anim
            out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
            out.use_anim_slot = False
            out.blf_title.text = rna.name  if title is None else title
            return out
        elif ty == "STRING":
            if rna.subtype in {"DIR_PATH", "FILE_PATH"}:
                o = BuStrFilePref(None, rna, lambda: pp, None, '', False)
                o.box_icon_arrow = GpuImg_FILE_FOLDER()
            else:
                o = BuStrPref(None, rna, lambda: pp, None, '', False)

            o.init_bat = o.init_bat_anim
            out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
            out.use_anim_slot = False
            out.blf_title.text = rna.name  if title is None else title
            return out
        else:
            TODO
        #|
    def r_button_size(self, w, pp, rna, title=None):
        if rna.is_array:
            if rna.type == "INT":
                o = BuIntVecSubPref(None, rna, lambda: pp, None, '', False)
            else:
                o = BuFloatVecSubPref(None, rna, lambda: pp, None, '', False)

            o.init_subtype(OVERRIDE_SUBTYPES_PrefsSize[rna.identifier])
        else:
            if rna.type == "INT":
                o = BuIntPref(None, rna, lambda: pp, None, '', False)
            else:
                o = BuFloatPref(None, rna, lambda: pp, None, '', False)

        o.init_bat = o.init_bat_anim

        out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
        out.use_anim_slot = False
        out.blf_title.text = rna.name  if title is None else title
        return out
        #|
    def r_button_fn(self, w, rna, fn):
        o = BuFunction(None, rna, fn, False)
        o.init_bat = o.init_bat_anim

        out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
        out.use_anim_slot = False
        out.blf_title.text = rna.name
        return out
        #|
    def r_block_calc_exp(self, w):
        rna = RNA_edit_expression
        o = BuFunction(None, rna,
            lambda: bufn_edit_expression(o, self.items[0].box_block),
            False)
        o.init_bat = o.init_bat_anim

        out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
        out.use_anim_slot = False
        out.blf_title.text = rna.name
        return out
        #|
    def r_block_md_lib_refresh(self, w):
        rna = RNA_md_lib_refresh
        o = BuFunction(None, rna, LibraryModifier.ui_refresh_path, False)
        o.init_bat = o.init_bat_anim

        out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
        out.use_anim_slot = False
        out.blf_title.text = rna.name
        return out
        #|
    def r_block_md_lib_filepath(self, w):
        rna = RNA_md_lib_edit
        o = BuFunction(None, rna, 
            lambda: LibraryModifier.ui_edit_path(o, self.items[0].box_block),
            False)
        o.init_bat = o.init_bat_anim

        out = BlockUtil(w, [AreaStringXYButton(None, self, rna.description, self.width_wrap, FONT0)], o)
        out.use_anim_slot = False
        out.blf_title.text = rna.name
        return out
        #|
    def r_block_pref_importexport_theme(self, w):
        o = BuFunction2(None,
            [RNA_pref_import_theme, RNA_pref_export_theme],
            [
                lambda: call_import_pref_menu(allow_subtypes={"COLOR"}, disable_fields={"general", "size", "keymaps"}),
                lambda: call_export_pref_menu(allow_subtypes={"COLOR"}, disable_fields={"general", "size", "keymaps"})
            ],
            False)

        o.init_bat = o.init_bat_anim_half

        e = Title("  Import / Export Theme")

        out = Blocks(w)
        out.buttons = [ButtonOverlay(out, o, e)]
        out.use_anim_slot = False
        return out
        #|
    def r_block_pref_importexport(self, w):
        o = BuFunction2(None,
            [RNA_pref_import, RNA_pref_export],
            [
                lambda: call_import_pref_menu(),
                lambda: call_export_pref_menu()
            ],
            False)

        o.init_bat = o.init_bat_anim_half

        e = Title("  Import / Export Preference Settings")

        out = Blocks(w)
        out.buttons = [ButtonOverlay(out, o, e)]
        out.use_anim_slot = False
        return out
        #|

    def bufn_ops_refresh(self):

        kms = bpy.context.window_manager.keyconfigs.user.keymaps

        for item in self.items:
            if hasattr(item, "button0"):
                button0 = item.button0
                if hasattr(button0, "rna") and hasattr(button0.rna, "data"):
                    idname = button0.rna.data.operator
                    bl_keymap = r_bl_keymap(idname, kms)
                    button0.set_button_text("None"  if bl_keymap is None else bl_keymap.keymap_items[idname].to_string())
        #|

    def init_items_tab(self):

        self.init_draw_range()
        self.get_cv_height()
        self.r_upd_scroll()()
        self.upd_data()
        #|
    def upd_data(self):
        super().upd_data()
        if hasattr(self, "upd_data_callback"): self.upd_data_callback()
        #|
    #|
    #|


class BlockPrefKeystroke(BlockUtils):
    __slots__ = (
        'km',
        'trigger_id',
        'keycomb0',
        'keycomb1',
        'keyvalue0',
        'keyvalue1',
        'keyendvalue0',
        'keyendvalue1',
        'keyexact0',
        'keyexact1',
        'keyduration0',
        'keyduration1',
        'button_duration0',
        'button_duration1')

    def __init__(self, w, trigger_id):
        self.trigger_id = trigger_id
        self.update_km_properties()
        rna = P_KEYMAPS_BL_RNA_PROPS[trigger_id]
        b_keycomb0 = ButtonStringKeyComb(None, RNA_keycomb0, self, subtype_override=("Comb 1",))
        b_keycomb1 = ButtonStringKeyComb(None, RNA_keycomb1, self, subtype_override=("Comb 2",))
        b_keycomb0.trigger_id = trigger_id
        b_keycomb1.trigger_id = trigger_id
        buttons = [
            ButtonGroupTwo(self,
                ButtonFn(None, RNA_edit_keystroke1, self.bufn_edit_keystroke1),
                ButtonFn(None, RNA_edit_keystroke0, self.bufn_edit_keystroke0)
            ),
            ButtonGroupFull(self, b_keycomb0, title=""),
            ButtonGroupFull(self, b_keycomb1, title=""),
        ]
        if trigger_id == "click":
            items = [
                ButtonSep(),
                ButtonGroup(self, ButtonBoolKeyExact(None, RNA_keyexact0, self)),
                ButtonGroup(self, ButtonBoolKeyExact(None, RNA_keyexact1, self)),
            ]
            for r in {1, 2}:
                items[r].button0.trigger_id = trigger_id
        elif self.km.use_end_key:
            items = [
                ButtonSep(),
                ButtonGroup(self, ButtonEnumKeyValue(None, RNA_keyvalue0, self)),
                ButtonGroup(self, ButtonEnumKeyEndValue(None, RNA_keyendvalue0, self)),
                ButtonGroup(self, ButtonFloatKeyDuration(None, RNA_keyduration0, self)),
                ButtonGroup(self, ButtonBoolKeyExact(None, RNA_keyexact0, self)),
                ButtonSep(),
                ButtonGroup(self, ButtonEnumKeyValue(None, RNA_keyvalue1, self)),
                ButtonGroup(self, ButtonEnumKeyEndValue(None, RNA_keyendvalue1, self)),
                ButtonGroup(self, ButtonFloatKeyDuration(None, RNA_keyduration1, self)),
                ButtonGroup(self, ButtonBoolKeyExact(None, RNA_keyexact1, self)),
                ButtonSep(),
            ]
            for r in {1, 2, 3, 4, 6, 7, 8, 9}:
                items[r].button0.trigger_id = trigger_id
            self.button_duration0 = items[3].button0
            self.button_duration1 = items[8].button0
        else:
            items = [
                ButtonSep(),
                ButtonGroup(self, ButtonEnumKeyValue(None, RNA_keyvalue0, self)),
                ButtonGroup(self, ButtonFloatKeyDuration(None, RNA_keyduration0, self)),
                ButtonGroup(self, ButtonBoolKeyExact(None, RNA_keyexact0, self)),
                ButtonSep(),
                ButtonGroup(self, ButtonEnumKeyValue(None, RNA_keyvalue1, self)),
                ButtonGroup(self, ButtonFloatKeyDuration(None, RNA_keyduration1, self)),
                ButtonGroup(self, ButtonBoolKeyExact(None, RNA_keyexact1, self)),
                ButtonSep(),
            ]
            for r in {1, 2, 3, 5, 6, 7}:
                items[r].button0.trigger_id = trigger_id
            self.button_duration0 = items[2].button0
            self.button_duration1 = items[6].button0
        self.update_darklight()
        super().__init__(w, items, buttons, title=rna.name)
        #|

    def bufn_edit_keystroke0(self):

        preserve_size = (round(D_SIZE["widget_width"] * 3.8), 20 * SIZE_widget[0] + SIZE_title[0])
        KeymapEditor(id_class="", use_pos=True, pos_offset=(-15, 15), use_fit=True,
            trigger_id=self.trigger_id, trigger_index=0, preserve_size=preserve_size)
        #|
    def bufn_edit_keystroke1(self):

        preserve_size = (round(D_SIZE["widget_width"] * 3.8), 20 * SIZE_widget[0] + SIZE_title[0])
        KeymapEditor(id_class="", use_pos=True, pos_offset=(-15, 15), use_fit=True,
            trigger_id=self.trigger_id, trigger_index=1, preserve_size=preserve_size)
        #|

    def update_km_properties(self):
        km = KEYMAPS[self.trigger_id]
        self.km = km
        self.keycomb0 = ", ".join(e.lower().replace('_', ' ').capitalize()  for e in km.types0)
        self.keycomb1 = ", ".join(e.lower().replace('_', ' ').capitalize()  for e in km.types1)
        self.keyvalue0 = km.value0
        self.keyvalue1 = km.value1
        self.keyexact0 = km.exact0
        self.keyexact1 = km.exact1
        self.keyduration0 = km.duration0
        self.keyduration1 = km.duration1
        if km.use_end_key:
            self.keyendvalue0 = km.end_value0
            self.keyendvalue1 = km.end_value1
        #|
    def update_darklight(self):
        if hasattr(self, "button_duration0"):
            km = self.km
            if km.use_end_key:
                if km.value0 in TIME_KEYS or km.end_value0 in TIME_KEYS:
                    self.button_duration0.light()
                else: self.button_duration0.dark()
                if km.value1 in TIME_KEYS or km.end_value1 in TIME_KEYS:
                    self.button_duration1.light()
                else: self.button_duration1.dark()
            else:
                if km.value0 in TIME_KEYS:
                    self.button_duration0.light()
                else: self.button_duration0.dark()
                if km.value1 in TIME_KEYS:
                    self.button_duration1.light()
                else: self.button_duration1.dark()
        #|
    def upd_data(self):
        if self.km is not KEYMAPS[self.trigger_id]:

            self.update_km_properties()
        self.update_darklight()
        super().upd_data()
        #|
    #|
    #|
class BlockPrefSearchHead(BlockUtils):
    __slots__ = (
        'text_search',
        'use_search_name',
        'use_search_id',
        'use_search_description',
        'use_search_cat_pref',
        'use_search_cat_pref_color',
        'use_search_cat_pref_size',
        'use_search_cat_pref_apps',
        'use_search_cat_pref_keymap')

    ID_TO_INDEX = {
        "name": 0,
        "id": 1,
        "description": 2,
        "general": 4,
        "color": 5,
        "size": 6,
        "editor": 7,
        "keymap": 8}

    def __init__(self, w):
        self.w = w
        self.text_search = ""
        self.use_search_name = P_SettingEditor.use_search_name
        self.use_search_id = P_SettingEditor.use_search_id
        self.use_search_description = P_SettingEditor.use_search_description
        self.use_search_cat_pref = P_SettingEditor.use_search_cat_pref
        self.use_search_cat_pref_color = P_SettingEditor.use_search_cat_pref_color
        self.use_search_cat_pref_size = P_SettingEditor.use_search_cat_pref_size
        self.use_search_cat_pref_apps = P_SettingEditor.use_search_cat_pref_apps
        self.use_search_cat_pref_keymap = P_SettingEditor.use_search_cat_pref_keymap

        buttons = [ButtonStringFind(self, RNA_text_search, self)]
        items = [
            ButtonGroupAlignLR(self, ButtonBoolCall(None, RNA_use_search_name, self), title="Name",
                title_head="Include"),
            ButtonGroupAlignL(self, ButtonBoolCall(None, RNA_use_search_id, self), title="ID"),
            ButtonGroupAlignL(self, ButtonBoolCall(None, RNA_use_search_description, self), title="Description"),
            BlockSep(),
            ButtonGroupAlignLR(self, ButtonBoolCall(None, RNA_use_search_cat_pref, self), title="General",
                title_head="Category"),
            ButtonGroupAlignL(self, ButtonBoolCall(None, RNA_use_search_cat_pref_color, self), title="Color"),
            ButtonGroupAlignL(self, ButtonBoolCall(None, RNA_use_search_cat_pref_size, self), title="Size"),
            ButtonGroupAlignL(self, ButtonBoolCall(None, RNA_use_search_cat_pref_apps, self), title="Editor"),
            ButtonGroupAlignL(self, ButtonBoolCall(None, RNA_use_search_cat_pref_keymap, self), title="Keymap"),
            BlockSep(),
        ]
        text_callback = self.button_text_callback
        buttons[0].set_callback = text_callback
        items[0].button0.set_callback = text_callback
        items[1].button0.set_callback = text_callback
        items[2].button0.set_callback = text_callback
        items[0].button0.get_default_value = lambda: P_SettingEditor.use_search_name
        items[1].button0.get_default_value = lambda: P_SettingEditor.use_search_id
        items[2].button0.get_default_value = lambda: P_SettingEditor.use_search_description

        items[4].button0.set_callback = text_callback
        items[5].button0.set_callback = text_callback
        items[6].button0.set_callback = text_callback
        items[7].button0.set_callback = text_callback
        items[8].button0.set_callback = text_callback
        items[4].button0.get_default_value = lambda: P_SettingEditor.use_search_cat_pref
        items[5].button0.get_default_value = lambda: P_SettingEditor.use_search_cat_pref_color
        items[6].button0.get_default_value = lambda: P_SettingEditor.use_search_cat_pref_size
        items[8].button0.get_default_value = lambda: P_SettingEditor.use_search_cat_pref_apps
        items[7].button0.get_default_value = lambda: P_SettingEditor.use_search_cat_pref_keymap
        super().__init__(w, items, buttons, title="Find")
        #|

    def button_text_callback(self, v=None):

        text = self.text_search
        a = self.w
        items = a.items
        if not text:
            items[:] = items[0 : 1]
            a.init_draw_range()
            a.get_cv_height()
            a.r_upd_scroll()()
            return

        b0 = self.buttons[0]
        use_search_name = self.use_search_name
        use_search_id = self.use_search_id
        use_search_description = self.use_search_description
        filter_function = r_filter_function(b0.is_match_case, b0.is_match_whole_word, b0.is_match_end)

        rnas = P.color.bl_rna.properties
        P_COLOR_BL_RNA_PROPS = [rnas[k]  for k in P.color.__annotations__]
        rnas = P.size.bl_rna.properties
        P_SIZE_BL_RNA_PROPS = [rnas[k]  for k in P.size.__annotations__]
        P_EDITORS = []
        for clsname, cls in m.D_EDITOR.items():
            pp = getattr(P, clsname, None)
            if pp is None: continue

            rnas = pp.bl_rna.properties
            P_EDITORS += [rnas[k]  for k in pp.__annotations__]

        def r_result(s,
                    filter_fn = None,
                    search_name = None,
                    search_id = None,
                    search_description = None,
                    use_pref = None,
                    use_color = None,
                    use_size = None,
                    use_apps = None,
                    use_keymap = None):

            if filter_fn is None:
                filter_fn = filter_function
            if search_name is None:
                search_name = use_search_name
            if search_id is None:
                search_id = use_search_id
            if search_description is None:
                search_description = use_search_description
            if use_pref is None:
                use_pref = self.use_search_cat_pref
            if use_color is None:
                use_color = self.use_search_cat_pref_color
            if use_size is None:
                use_size = self.use_search_cat_pref_size
            if use_apps is None:
                use_apps = self.use_search_cat_pref_apps
            if use_keymap is None:
                use_keymap = self.use_search_cat_pref_keymap
            out = set()

            def find_rna(rna):
                if search_name:
                    if filter_fn(rna.name, s):
                        out.add(rna)
                        return
                if search_id:
                    if filter_fn(rna.identifier, s):
                        out.add(rna)
                        return
                if search_description:
                    if filter_fn(rna.description, s):
                        out.add(rna)
                        return

            if use_pref:
                find_rna(RNA_md_lib_edit)
                find_rna(RNA_md_lib_refresh)
                find_rna(RNA_edit_expression)
                find_rna(RNA_pref_export)
                find_rna(RNA_pref_import)
                find_rna(RNA_pref_export_theme)
                find_rna(RNA_pref_import_theme)

                for rna in P_BL_RNA_PROPS:
                    find_rna(rna)
            if use_color:
                for rna in P_COLOR_BL_RNA_PROPS:
                    find_rna(rna)
            if use_size:
                find_rna(RNA_ui_scale_100)
                find_rna(RNA_ui_scale_133)
                find_rna(RNA_ui_scale_166)
                find_rna(RNA_ui_scale_200)
                find_rna(RNA_ui_reload_icon)

                for rna in P_SIZE_BL_RNA_PROPS:
                    find_rna(rna)
            if use_apps:
                for rna in P_EDITORS:
                    find_rna(rna)
            if use_keymap:
                for rna in P_KEYMAPS_BL_RNA_PROPS:
                    find_rna(rna)
            return out


        if text.startswith(";") and not text.startswith(";;"):
            exp = text[1 : ].strip()
            if exp == "vmdrootenable":
                bpy.v = VMD
                report("Get root successfully")
                return

            success, results = r_filtexp_result(exp, r_result, filter_function)
            if not success:
                DropDownOk(None, MOUSE, input_text=f'Eval Failed\n{results}')
                return
        else:
            if text.startswith(";;"):
                text = text[1 : ]
            results = r_result(text, filter_function)


        BlockUtil.DEFAULT_FOLD_STATE = P_SettingEditor.is_fold
        items[:] = items[0 : 1]

        #
        self = a
        r_button = self.r_button
        r_button_fn = self.r_button_fn
        r_button_size = self.r_button_size

        if RNA_pref_import in results or RNA_pref_export in results:
            items.append(self.r_block_pref_importexport(self))

        if RNA_pref_import_theme in results or RNA_pref_export_theme in results:
            items.append(self.r_block_pref_importexport_theme(self))

        if RNA_md_lib_refresh in results:
            items.append(self.r_block_md_lib_refresh(self))

        if RNA_md_lib_edit in results:
            items.append(self.r_block_md_lib_filepath(self))

        if RNA_edit_expression in results:
            items.append(self.r_block_calc_exp(self))

        pp = P
        items += [r_button(self, pp, rna)  for rna in P_BL_RNA_PROPS  if rna in results]

        pp = P.size
        rnas = pp.bl_rna.properties
        if RNA_ui_scale_100 in results:
            items.append(r_button_fn(self, RNA_ui_scale_100, lambda: bpy.ops.wm.vmd_ui_scale(factor=1.0)))
        if RNA_ui_scale_133 in results:
            items.append(r_button_fn(self, RNA_ui_scale_133, lambda: bpy.ops.wm.vmd_ui_scale(factor=1.0)))
        if RNA_ui_scale_166 in results:
            items.append(r_button_fn(self, RNA_ui_scale_166, lambda: bpy.ops.wm.vmd_ui_scale(factor=1.0)))
        if RNA_ui_scale_200 in results:
            items.append(r_button_fn(self, RNA_ui_scale_200, lambda: bpy.ops.wm.vmd_ui_scale(factor=1.0)))
        if RNA_ui_reload_icon in results:
            items.append(r_button_fn(self, RNA_ui_reload_icon, reload_icon))

        items += [r_button_size(self, pp, rnas[k])  for k in pp.__annotations__  if rnas[k] in results]

        pp = P.color
        rnas = pp.bl_rna.properties
        items += [r_button(self, pp, rnas[k])  for k in pp.__annotations__  if rnas[k] in results]

        items += [BlockPrefKeystroke(self, rna.identifier)  for rna in P_KEYMAPS_BL_RNA_PROPS  if rna in results]

        for clsname, cls in m.D_EDITOR.items():
            pp = getattr(P, clsname, None)
            if pp is None: continue

            rnas = pp.bl_rna.properties
            size_attrs = getattr(pp, 'SIZE_CALLBACKS', {})

            items += [(r_button_size  if k in size_attrs else r_button)(
                self, pp, rnas[k])  for k in pp.__annotations__  if rnas[k] in results]
        #

        for e in items:
            e.upd_data()

        a.init_draw_range()
        a.get_cv_height()
        a.r_upd_scroll()()
        #|

    def set_properties(self, tx, match_case, match_whole_word, match_end, true_ids):
        button0 = self.buttons[0]
        button0.set("")
        button0.evt_toggle_match_case(match_case)
        button0.evt_toggle_match_whole_word(match_whole_word)
        button0.evt_toggle_match_end(match_end)
        items = self.items

        for k, i in self.ID_TO_INDEX.items():
            items[i].button0.set(k in true_ids)

        button0.set(tx)
        #|
    #|
    #|


class ButtonStringSettingHeader(ButtonString):
    __slots__ = 'buttons', 'box_hover', 'focus_element'

    def __init__(self, w, rna, pp):
        self.w = w
        self.rna = rna
        self.pp = pp
        self.box_button = GpuRim(COL_box_text, COL_box_text_rim)
        v = getattr(pp, rna.identifier)
        self.blf_value = BlfClipColor(v, v, 0, 0, COL_box_text_fg)
        self.box_hover = GpuRimBlfbuttonTextHover()
        #|

    def r_init_tab_fn(self, tabs):
        def _init_tab():
            self.w.w.active_tab = tabs
            self.w.w.upd_data()
        return _init_tab
        #|

    def init_buttons(self, tabs):
        if tabs:
            f0 = self.button_inside_evt_callback
            f1 = self.button_outside_evt_callback
            r_init_tab_fn = self.r_init_tab_fn
            self.buttons = [
                ButtonFnBlf(self, None, r_init_tab_fn(tabs[: r + 1]),
                    "", COL_box_text_fg, f0, f1)
                for r in range(len(tabs))
            ]
            L, R, B, T = self.box_button.inner
            h = SIZE_widget[0]
            font_main_dx = D_SIZE['font_main_dx']
            # <<< 1copy (init_blf_clipping_end,, ${'font_size':'font_main'}$)
            blfSize(FONT0, D_SIZE['font_main'])
            blg.CLIPPING_END_STR_DIMEN = floor(blfDimen(FONT0, blg.CLIPPING_END_STR)[0])
            # >>>
            ButtonFnBlf.set_offset(L, font_main_dx, D_SIZE['font_main_dy'], h)

            e = self.buttons[0]
            for r, e in enumerate(self.buttons):
                if r == 0:
                    name = tabs[0].title()
                else:
                    name = r_tab_rna(tabs[: r + 1]).name

                e.blf_value.unclip_text = name
                ButtonFnBlf.BLF_X = L + font_main_dx
                R = ButtonFnBlf.BLF_X + round(blfDimen(FONT0, name)[0]) + font_main_dx
                e.init_bat_dimen(L, R, T)
                L = R + h
        else:
            self.buttons = []
        #|

    def init_bat(self, L, R, T):
        B = super().init_bat(L, R, T)
        self.init_buttons(self.w.w.active_tab)
        self.box_hover.LRBT_upd(0, 0, 0, 0, 0)
        return B
        #|

    def inside_evt(self):
        for e in self.buttons:
            if e.inside(MOUSE):
                self.focus_element = e
                return e.inside_evt()

        self.focus_element = None
        super().inside_evt()
        #|
    def outside_evt(self):
        super().outside_evt()
        if self.box_hover.d != 0: self.box_hover.LRBT_upd(0, 0, 0, 0, 0)
        #|

    def button_inside_evt_callback(self, button):
        self.box_hover.LRBT_upd(*button.box_button.r_LRBT(), SIZE_border[3])
        #|
    def button_outside_evt_callback(self, button):
        if self.box_hover.d != 0: self.box_hover.LRBT_upd(0, 0, 0, 0, 0)
        #|

    def modal(self):
        focus_button = None
        for e in self.buttons:
            if e.inside(MOUSE):
                focus_button = e
                break

        if focus_button is None:
            if self.focus_element != None:
                self.focus_element = None
                self.box_button.color = COL_box_text_active

            if self.box_hover.d != 0: self.box_hover.LRBT_upd(0, 0, 0, 0, 0)
            Admin.REDRAW()
            return super().modal()
        else:
            if self.focus_element != focus_button:
                if hasattr(self.focus_element, "outside_evt"): self.focus_element.outside_evt()
                self.focus_element = focus_button
                self.box_button.color = COL_box_text
                focus_button.inside_evt()

            return focus_button.modal()
        return False
        #|

    def to_dropdown(self, killevt=True, select_all=None):
        return DropDownString(self, self.box_button.r_LRBT(), r_tab_as_string(self.w.w.active_tab))
        #|
    def evt_area_copy(self, is_report=True):

        kill_evt_except()
        bpy.context.window_manager.clipboard = r_tab_as_string(self.w.w.active_tab)
        if is_report: report("Copy to Clipboard")
        #|

    def dxy(self, dx, dy):
        self.box_button.dxy_upd(dx, dy)
        self.blf_value.x += dx
        self.blf_value.y += dy
        for e in self.buttons: e.dxy(dx, dy)
        self.box_hover.dxy_upd(dx, dy)
        #|

    def draw_box(self):
        self.box_button.bind_draw()
        self.box_hover.bind_draw()
        #|
    def draw_blf(self):
        for e in self.buttons: e.draw_blf()
        #|

    def set(self, v, refresh=True, undo_push=True):
        tabs = r_tabs_by_string(v)
        if tabs != None:
            self.w.w.active_tab = tabs
            self.w.w.upd_data()
        #|
    #|
    #|

class ButtonStringKeyComb(ButtonStringPref):
    __slots__ = 'trigger_id'

    def set(self, v, refresh=True, undo_push=True):
        oldvalue = self.get()
        write_keytype_with_report(v, self.trigger_id, 0  if self.rna.identifier.endswith("0") else 1)
        if refresh: update_data()
        self.evt_undo_push(undo_push, oldvalue)
        Admin.REDRAW()
        #|

    def r_default_value(self):
        km = KeyMap("", P_KEYMAPS_BL_RNA_PROPS[self.trigger_id].default_array)
        return ",".join(km.types0  if self.rna.identifier.endswith("0") else km.types1)
        #|
    #|
    #|
class ButtonEnumKeyValue(ButtonEnumPref):
    __slots__ = 'trigger_id'

    def set(self, v, refresh=True, undo_push=True):
        oldvalue = self.get()
        write_keyvalue_with_report(v, self.trigger_id, 0  if self.rna.identifier.endswith("0") else 1)
        if refresh: update_data()
        self.evt_undo_push(undo_push, oldvalue)
        Admin.REDRAW()
        #|

    def r_default_value(self):
        km = KeyMap("", P_KEYMAPS_BL_RNA_PROPS[self.trigger_id].default_array)
        return km.value0  if self.rna.identifier.endswith("0") else km.value1
        #|
    #|
    #|
class ButtonEnumKeyEndValue(ButtonEnumPref):
    __slots__ = 'trigger_id'

    def set(self, v, refresh=True, undo_push=True):
        write_keyendvalue_with_report(v, self.trigger_id, 0  if self.rna.identifier.endswith("0") else 1)
        if refresh: update_data()
        #|

    def r_default_value(self):
        km = KeyMap("", P_KEYMAPS_BL_RNA_PROPS[self.trigger_id].default_array)
        return km.end_value0  if self.rna.identifier.endswith("0") else km.end_value1
        #|
    #|
    #|
class ButtonBoolKeyExact(ButtonBoolPref):
    __slots__ = 'trigger_id'

    def set(self, v, refresh=True, undo_push=True):
        oldvalue = self.get()
        write_keyexact_with_report(v, self.trigger_id, 0  if self.rna.identifier.endswith("0") else 1)
        if refresh: update_data()
        self.evt_undo_push(undo_push, oldvalue)
        Admin.REDRAW()
        #|

    def r_default_value(self):
        km = KeyMap("", P_KEYMAPS_BL_RNA_PROPS[self.trigger_id].default_array)
        return km.exact0  if self.rna.identifier.endswith("0") else km.exact1
        #|
    #|
    #|
class ButtonFloatKeyDuration(ButtonFloatPref):
    __slots__ = 'trigger_id'

    def set(self, v, refresh=True, undo_push=True):
        oldvalue = self.get()
        write_duration_with_report(v, self.trigger_id, 0  if self.rna.identifier.endswith("0") else 1)
        if refresh: update_data()
        self.evt_undo_push(undo_push, oldvalue)
        Admin.REDRAW()
        #|

    def r_default_value(self):
        km = KeyMap("", P_KEYMAPS_BL_RNA_PROPS[self.trigger_id].default_array)
        return km.duration0  if self.rna.identifier.endswith("0") else km.duration1
        #|
    #|
    #|

class ButtonStringFind(ButtonStringMatchButton):
    __slots__ = ()

    OFFSET_FAC = 1
    OFFSET_TEXT = "find"
    #|
    #|


def r_tab_rna(tabs): # need len >= 2
    e = RNAS[tabs[0]]
    for identifier in tabs[1 :]:
        if isinstance(e, tuple): e = e[1][identifier]
        else: e = e[identifier]
    if isinstance(e, tuple): return e[0]
    else: return e
    #|
def r_tab_as_string(tabs):
    if tabs:
        if len(tabs) == 1: return tabs[0].title()
        s = f'{tabs[0].title()}\\'
        e = RNAS[tabs[0]]
        for identifier in tabs[1 :]:
            if isinstance(e, tuple): e = e[1][identifier]
            else: e = e[identifier]
            if isinstance(e, tuple): s += f'{e[0].name}\\'
            else: s += f'{e.name}\\'
        return s[: -1]
    return ""
    #|
def r_tabs_by_string(s):
    if not isinstance(s, str): return None
    s = s.strip().replace("/", "\\")
    if s.endswith("\\"): s = s[: -1]
    if not s: return None
    li = s.split("\\")
    if not li: return None

    id0 = li[0].strip().lower()
    if id0 not in RNAS: return None
    tabs = [id0]
    if len(li) == 1: return tuple(tabs)

    its = RNAS[id0]
    for name in li[1 :]:
        name = name.strip().lower()
        name_to_id = {e[0].name.lower()  if isinstance(e, tuple) else e.name.lower(): k  for k, e in its.items()}
        if name not in name_to_id: return None
        identifier = name_to_id[name]
        tabs.append(identifier)
        its = its[identifier]
        if isinstance(its, tuple): its = its[1]
    return tuple(tabs)
    #|

def bufn_edit_expression(button0=None, box_block=None):
    L, R, B, T = button0.box_button.r_LRBT()

    def confirm_fn(s):
        exc = write_calc_exp(s, P)
        if exc == None:
            save_pref()
            return False
        return f'Compile Error.\n{exc}'

    def r_default_value(): return P.bl_rna.properties["calc_exp"].default

    DropDownText(button0, (box_block.L, R, T), P.calc_exp, confirm_fn, r_default_value)
    #|
def bufn_ops_editkey(button0=None):

    rna_data = button0.rna.data
    idname = rna_data.operator
    bl_keymap = r_bl_keymap(idname, bpy.context.window_manager.keyconfigs.user.keymaps)

    if bl_keymap is None:
        ddw = DropDownAddOpsShortcut(None, MOUSE, idname, rna_data.keymap_category)
    else:
        ddw = DropDownEditOpsShortcut(None, MOUSE, idname, bl_keymap.name)

    def fin_callback():
        bl_keymap = r_bl_keymap(idname, bpy.context.window_manager.keyconfigs.user.keymaps)
        button0.set_button_text("None"  if bl_keymap is None else bl_keymap.keymap_items[idname].to_string())
    ddw.data["fin_callback"] = fin_callback
    #|
@ catch
def load_theme(theme="DARK"):
    if theme == "DARK":
        pp = P.color
        for k, rna in pp.bl_rna.properties.items():
            if hasattr(rna, "subtype") and rna.subtype == "COLOR":
                setattr(pp, k, rna.default_array)
    else:
        report("Theme input error", ty="ERROR")
        return

    Admin.REDRAW()
    report("Theme loaded successfully. Requires manual saving of preferences")
    #|
def call_export_pref_menu(self=None, allow_subtypes=None, disable_fields=None):
    if not P: return

    def button_fn_cancel(button=None):
        ddw.fin_from_area()
        #|
    def button_fn_save_as():
        success, result = r_export_pref_as_string(props, allow_subtypes=allow_subtypes)
        if not success: return
        def write_json(s):
            try:
                with open(s, 'w') as file:
                    pafh = Path(s)
                    if pafh.is_file() and pafh.suffix != ".json":
                        report("Existing file cannot be overwritten", ty="WARNING")
                        return
                    file.write(result)
                report(f"File has been written to {s}")
            except:
                report("Failed to write file", ty="WARNING")

        OpScanFile.end_fn = write_json
        bpy.ops.wm.vmd_scan_file("INVOKE_DEFAULT", filepath="untitled.json", check_existing=True)
        #|
    def button_fn_copy_to_clipboard():
        success, result = r_export_pref_as_string(props, allow_subtypes=allow_subtypes)
        if success:
            bpy.context.window_manager.clipboard = result
            report("Copy to Clipboard")
        #|

    gap = SIZE_button[1]
    button_cancel = ButtonFn(None, RNA_cancel, button_fn_cancel)
    button_copy_to_clipboard = ButtonFn(None, RNA_copy_to_clipboard, button_fn_copy_to_clipboard)
    button_save_as = ButtonFn(None, RNA_save_as, button_fn_save_as)
    area_items = []

    if allow_subtypes is None:
        input_text = "Save as Json File"
        row_count = 2
    else:
        input_text = f"Save as Json File\nSubtype filter :  {allow_subtypes}"
        row_count = 3

    ddw = DropDownInfoUtil(None, MOUSE,
        [ButtonSplit(None, button_copy_to_clipboard,
            ButtonSplit(None, button_save_as, button_cancel, gap), gap)],
        area_items = area_items,
        title = "Export Preference Settings",
        input_text = input_text,
        row_count=row_count, width_fac=3.0, block_size=8)

    props = SimpleNamespace()
    fields = ["general", "color", "size", "keymaps"] + [k  for k in m.D_EDITOR.keys()  if hasattr(P, k)]

    area_tab = ddw.r_area_tab()
    layout = Layout(area_tab)
    l0 = layout.new_block()
    if disable_fields is None: disable_fields = set()

    for k in fields:
        setattr(props, k, False  if k in disable_fields else True)
        l0.prop(props, RnaBool(k, m.D_EDITOR[k].name  if k in m.D_EDITOR else k.title()), use_push=False, set_callback=True)

    area_tab.init_items_tab()
    #|
def call_import_pref_menu(self=None, allow_subtypes=None, disable_fields=None):
    if not P: return

    def button_fn_cancel(button=None):
        ddw.fin_from_area()
        #|
    def button_fn_import():
        def read_json(s):
            try:
                with open(s) as file:
                    dic = json.load(file)
            except Exception as ex:
                report(f"Failed to load file. {ex}", ty="WARNING")
                return

            success, result = import_pref_by_dict(props, dic, allow_subtypes=allow_subtypes)
            if success:
                good_keymap = init_keymaps(P)
                good_calcexp = init_calc_exp(P)

                if isinstance(result, str): report(result)
                else:
                    tx = f"{len(result)} Failure(s) :\n    " + "\n    ".join(result)
                    report(tx, ty="WARNING")
                    ddw.set_area_info(tx, beam_start=True)

                if not good_keymap:
                    ss = "WARNING: Keymap compile error. All keymaps are set to default"
                    report(ss, ty="WARNING")
                    ddw.set_area_info(f"{ss}\n" + ddw.r_area_info(), beam_start=True)
                if not good_calcexp:
                    ss = "WARNING: Calculator Expression compile error. Set as default"
                    report(ss, ty="WARNING")
                    ddw.set_area_info(f"{ss}\n" + ddw.r_area_info(), beam_start=True)
            else:
                report(result, ty="WARNING")

        OpScanFile.end_fn = read_json
        bpy.ops.wm.vmd_scan_file("INVOKE_DEFAULT", filepath=".json")
        #|

    gap = SIZE_button[1]
    button_cancel = ButtonFn(None, RNA_cancel, button_fn_cancel)
    button_import = ButtonFn(None, RNA_importfile, button_fn_import)
    area_items = []

    if allow_subtypes is None:
        input_text = "Import Json File\nThis process will not push a undo event"
        row_count = 3
    else:
        input_text = f"Import Json File\nThis process will not push a undo event\nSubtype filter :  {allow_subtypes}"
        row_count = 4

    ddw = DropDownInfoUtil(None, MOUSE,
        [ButtonSplit(None, button_import, button_cancel, gap)],
        area_items = area_items,
        title = "Import Preference Settings",
        input_text = input_text,
        row_count=row_count, width_fac=3.0, block_size=8)

    props = SimpleNamespace()
    fields = ["general", "color", "size", "keymaps"] + [k  for k in m.D_EDITOR.keys()  if hasattr(P, k)]

    area_tab = ddw.r_area_tab()
    layout = Layout(area_tab)
    l0 = layout.new_block()
    if disable_fields is None: disable_fields = set()

    for k in fields:
        setattr(props, k, False  if k in disable_fields else True)
        l0.prop(props, RnaBool(k, m.D_EDITOR[k].name  if k in m.D_EDITOR else k.title()), use_push=False, set_callback=True)

    area_tab.init_items_tab()
    #|
@ successResult
def r_export_pref_as_string(props, indent=4, allow_subtypes=None):
    def format_value(rna, v):
        if isinstance(v, str): return v
        if isinstance(v, bytes): return str(v)[2 :]
        if hasattr(v, "__getitem__"): return [v  for v in v]
        return v
    def r_sub_dic(pp):
        return {k: format_value(rna, getattr(pp, k))  for k, rna in pp.bl_rna.properties.items()
            if (k not in {'bl_idname', 'name', 'rna_type'} and rna.type != "POINTER" and (
            allow_subtypes is None or (hasattr(rna, "subtype") and rna.subtype in allow_subtypes)))}

    if props.general is True:
        dic = {k: format_value(rna, getattr(P, k))  for k, rna in P_BL_RNA_PROPS.items() if (
            allow_subtypes is None or (hasattr(rna, "subtype") and rna.subtype in allow_subtypes))}
    else:
        dic = {}

    if props.size is True:
        dic["size"] = r_sub_dic(P.size)
    if props.color is True:
        dic["color"] = r_sub_dic(P.color)
    if props.keymaps is True:
        dic["keymaps"] = r_sub_dic(P.keymaps)

    for k in m.D_EDITOR.keys():
        if hasattr(P, k) and getattr(props, k) is True: dic[k] = r_sub_dic(getattr(P, k))

    return json.dumps(dic, indent=indent)
    #|
@ successResult
def import_pref_by_dict(props, dic, allow_subtypes=None): # do byte str
    fails = []
    if not isinstance(dic, dict): return "Failed to load file. Data is not a dictionary"
    if not dic: return "Skipped. Data is empty"

    def assign_pref(dick, pp, catname=None):
        rnas = pp.bl_rna.properties
        for k, e in dick.items():
            if isinstance(e, dict):
                ppp = getattr(pp, k, None)
                if ppp is None:
                    fails.append(k  if catname is None else f"{catname}.{k}")
                else:
                    assign_pref(e, ppp, k)
            else:
                if pp is P:
                    if props.general is not True: continue
                else:
                    if hasattr(props, k) and getattr(props, k) is not True: continue

                if allow_subtypes is None: pass
                else:
                    try:
                        if not hasattr(rnas[k], "subtype"): continue
                        if rnas[k].subtype not in allow_subtypes: continue
                    except:
                        fails.append(k  if catname is None else f"{catname}.{k}")
                        continue

                try: setattr(pp, k, e)
                except: fails.append(k  if catname is None else f"{catname}.{k}")

    assign_pref(dic, P)

    if fails: return fails
    return "Import successful. Requires manual saving of preferences"
    #|


def write_with_report(success, message, is_save_pref):
    if success:
        if message: report(message)
        if is_save_pref: save_pref()
    else:
        report(message, "WARNING")
    #|
def write_keytype_with_report(s, trigger_id, trigger_index, is_save_pref=False):
    success, message = write_keytype(s, trigger_id, trigger_index)
    write_with_report(success, message, is_save_pref)
    return success
    #|
def write_keyvalue_with_report(s, trigger_id, trigger_index, is_save_pref=False):
    success, message = write_keyvalue(s, trigger_id, trigger_index)
    write_with_report(success, message, is_save_pref)
    return success
    #|
def write_keyendvalue_with_report(s, trigger_id, trigger_index, is_save_pref=False):
    success, message = write_keyendvalue(s, trigger_id, trigger_index)
    write_with_report(success, message, is_save_pref)
    return success
    #|
def write_keyexact_with_report(s, trigger_id, trigger_index, is_save_pref=False):
    success, message = write_keyexact(s, trigger_id, trigger_index)
    write_with_report(success, message, is_save_pref)
    return success
    #|
def write_duration_with_report(s, trigger_id, trigger_index, is_save_pref=False):
    success, message = write_keyduration(s, trigger_id, trigger_index)
    write_with_report(success, message, is_save_pref)
    return success
    #|

def r_about():
    BL_INFO = VMD.handle.BL_INFO
    addon_version = ".".join(str(e)  for e in BL_INFO["version"])
    # if BL_INFO["version"][2] == 0: addon_version += " (Alpha)"

    return f'''Information
        Blender Version :  {bpy.app.version_string}
        Addon Version :  {BL_INFO["name"]} {addon_version}

        \nBug Report
        Blender Market inbox (Login required) :\n                https://blendermarket.com/creators/iiispace
        E-mail :\n                oorcer@gmail.com
        GitHub (Login required) :\n                https://github.com/Iiispace/vmdesk/issues
    '''
    #|


m.D_EDITOR.new('SettingEditor', SettingEditor)

def late_import():
    # <<< 1mp (VMD.block
    block = VMD.block
    Layout = block.Layout
    Blocks = block.Blocks
    BlockUtil = block.BlockUtil
    BlockUtilHeavy = block.BlockUtilHeavy
    BlockSubtab = block.BlockSubtab
    BlockSep = block.BlockSep
    BlockFull = block.BlockFull
    ButtonFn = block.ButtonFn
    ButtonSep = block.ButtonSep
    ButtonOverlay = block.ButtonOverlay
    ButtonSplit = block.ButtonSplit
    ButtonGroup = block.ButtonGroup
    ButtonGroupAlignL = block.ButtonGroupAlignL
    ButtonGroupAlignLR = block.ButtonGroupAlignLR
    ButtonGroupFull = block.ButtonGroupFull
    ButtonGroupTwo = block.ButtonGroupTwo
    ButtonGroupTwoHalf = block.ButtonGroupTwoHalf
    ButtonFnImgHover = block.ButtonFnImgHover
    ButtonString = block.ButtonString
    ButtonFnImgList = block.ButtonFnImgList
    ButtonFnBlf = block.ButtonFnBlf
    ButtonBoolCall = block.ButtonBoolCall
    BuBoolPref = block.BuBoolPref
    BuIntPref = block.BuIntPref
    BuFloatPref = block.BuFloatPref
    BuIntVecPref = block.BuIntVecPref
    BuIntVecSubPref = block.BuIntVecSubPref
    BuFloatVecPref = block.BuFloatVecPref
    BuFloatVecSubPref = block.BuFloatVecSubPref
    BuEnumPref = block.BuEnumPref
    BuStrFilePref = block.BuStrFilePref
    BuFunction = block.BuFunction
    BuFunction2 = block.BuFunction2
    BuColorPref = block.BuColorPref
    PREF_HISTORY = block.PREF_HISTORY
    Title = block.Title
    D_subtype_display = block.D_subtype_display
    # >>>

    # <<< 1mp (VMD.dd
    dd = VMD.dd
    DropDownText = dd.DropDownText
    DropDownString = dd.DropDownString
    DropDownAddOpsShortcut = dd.DropDownAddOpsShortcut
    DropDownEditOpsShortcut = dd.DropDownEditOpsShortcut
    DropDownInfoUtil = dd.DropDownInfoUtil
    DropDownOk = dd.DropDownOk
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    kill_evt_except = keysys.kill_evt_except
    MOUSE = keysys.MOUSE
    EVT_TYPE = keysys.EVT_TYPE
    TRIGGER = keysys.TRIGGER
    TIME_KEYS = keysys.TIME_KEYS
    r_end_trigger = keysys.r_end_trigger
    r_bl_keymap = keysys.r_bl_keymap
    init_keymaps = keysys.init_keymaps
    init_calc_exp = keysys.init_calc_exp
    KeyMap = keysys.KeyMap
    KEYMAPS = keysys.KEYMAPS
    write_keytype = keysys.write_keytype
    write_keyvalue = keysys.write_keyvalue
    write_keyendvalue = keysys.write_keyendvalue
    write_keyexact = keysys.write_keyexact
    write_keyduration = keysys.write_keyduration
    write_calc_exp = keysys.write_calc_exp
    ENUMS_keymap_value = keysys.ENUMS_keymap_value
    TRIGGER_END = keysys.TRIGGER_END
    TRIGGER_IND = keysys.TRIGGER_IND
    r_keyinfo = keysys.r_keyinfo
    r_keyrepeatinfo = keysys.r_keyrepeatinfo
    # >>>

    # <<< 1mp (m
    P = m.P
    Admin = m.Admin
    W_HEAD = m.W_HEAD
    W_DRAW = m.W_DRAW
    update_data = m.update_data
    save_pref = m.save_pref
    LibraryModifier = m.LibraryModifier
    bring_draw_to_top_safe = m.bring_draw_to_top_safe
    # >>>

    # <<< 1mp (VMD.prefs
    prefs = VMD.prefs
    OVERRIDE_SUBTYPES = prefs.OVERRIDE_SUBTYPES
    PrefsSize = prefs.PrefsSize
    # >>>

    # <<< 1mp (VMD.rna
    rna = VMD.rna
    RNA_cancel = rna.RNA_cancel
    RNA_importfile = rna.RNA_importfile
    RNA_copy_to_clipboard = rna.RNA_copy_to_clipboard
    RNA_save_as = rna.RNA_save_as
    # >>>

    # <<< 1mp (VMD.win
    win = VMD.win
    Head = win.Head
    # >>>

    utilbl = VMD.utilbl

    # <<< 1mp (utilbl.ops
    ops = utilbl.ops
    OpScanFile = ops.OpScanFile
    # >>>

    # <<< 1mp (utilbl
    blg = utilbl.blg
    # >>>

    # <<< 1mp (blg
    Blf = blg.Blf
    BlfColor = blg.BlfColor
    BlfClipColor = blg.BlfClipColor
    Scissor = blg.Scissor
    GpuBox = blg.GpuBox
    GpuRim = blg.GpuRim
    GpuBox_area = blg.GpuBox_area
    GpuBox_box_setting_list_bg = blg.GpuBox_box_setting_list_bg
    GpuRimAreaHover = blg.GpuRimAreaHover
    GpuRimBlfbuttonTextHover = blg.GpuRimBlfbuttonTextHover
    GpuRimSettingTabActive = blg.GpuRimSettingTabActive
    GpuImg_unfold = blg.GpuImg_unfold
    GpuImg_FILE_FOLDER = blg.GpuImg_FILE_FOLDER
    report = blg.report
    reload_icon = blg.reload_icon
    FONT0 = blg.FONT0
    D_SIZE = blg.D_SIZE
    SIZE_widget = blg.SIZE_widget
    SIZE_title = blg.SIZE_title
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_setting_list_border = blg.SIZE_setting_list_border
    SIZE_block = blg.SIZE_block
    SIZE_button = blg.SIZE_button
    COL_box_setting_list_fg = blg.COL_box_setting_list_fg
    COL_block_fg_info = blg.COL_block_fg_info
    COL_box_text = blg.COL_box_text
    COL_box_text_rim = blg.COL_box_text_rim
    COL_box_text_fg = blg.COL_box_text_fg
    COL_box_text_active = blg.COL_box_text_active
    # >>>

    util = VMD.util

    # <<< 1mp (util.com
    com = util.com
    r_mouse_y_index = com.r_mouse_y_index
    r_filter_function = com.r_filter_function
    r_tuple = com.r_tuple
    # >>>

    # <<< 1mp (util.filtexp
    filtexp = util.filtexp
    r_filtexp_result = filtexp.r_filtexp_result
    # >>>


    P_SettingEditor = P.SettingEditor
    OVERRIDE_SUBTYPES_PrefsSize = OVERRIDE_SUBTYPES[PrefsSize]

    RNAS_apps = RNAS["apps"]
    for k, clss in m.D_EDITOR.items():
        if k in RNAS_apps: continue
        RNAS_apps[k] = RnaSubtab(k, clss.name, "Built-in editor.", f"GpuImg_{k}")

    P_BL_RNA_PROPS = Dictlist(
        [rna  for idd, rna in P.bl_rna.properties.items() if idd not in {
        'bl_idname', 'name', 'rna_type', 'refresh', 'is_first_use', 'de'} and rna.type != "POINTER"]
    )
    P_KEYMAPS_BL_RNA_PROPS = Dictlist(
        [rna  for idd, rna in P.keymaps.bl_rna.properties.items() if idd not in {
        'bl_idname', 'name', 'rna_type'} and rna.type != "POINTER"]
    )

    globals().update(locals())
    #|