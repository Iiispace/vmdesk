import bpy

Panel = bpy.types.Panel
P = None

class VmdPanel(Panel):
    __slots__ = ()

    bl_idname = "VMD_PT_Panel"
    bl_label = "Control Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "VMD"

    def draw(self, context):
        #|
        layout = self.layout
        sep = layout.separator

        layout.operator("wm.vmd_window_manager", text="Window Manager")

        for name in m.D_EDITOR.keys():
            e = layout.operator("wm.vmd_editor", text=name)
            e.id_class = name
            e.use_pos = False

        sep()
        layout.operator("wm.save_userpref")
        layout.operator("wm.vmd_addon_factory", text="Load Addon Factory Setting")
        layout.operator("wm.vmd_reload_icon", text="Reload Icon")
        layout.operator("wm.vmd_reload_font", text="Reload Font")
        layout.prop(P, "npanel_reg_settings", text="Show Settings")






















        header, panel = layout.panel("VMD_TEMP_PT_Panel", default_closed=True)
        header.label(text="Temporary Data")
        if panel:
            prop = panel.prop
            pp = P.temp
            for k in pp.__annotations__:
                prop(pp, k)

        if P.npanel_reg_settings: pass
        else: return


        header, panel = layout.panel("VMD_GENERAL_PT_Panel", default_closed=True)
        header.label(text="General")
        if panel:
            prop = panel.prop
            pp = P

            # <<< 1ifmatch (0prefs, 12,
            #     $lambda line: (f'prop(pp, "{line.split(":", 1)[0].lstrip()}")\n', True
            #         )  if line.find('PointerProperty') == -1 else ('', False)$,
            #     $lambda line: ('', False)  if line.find('#sep()') == -1 else ('sep()\n', True)$,
            #     ${'Property('}$)
            prop(pp, "npanel_reg_settings")
            prop(pp, "sys_auto_off")
            prop(pp, "show_length_unit")
            prop(pp, "lock_win_size")
            prop(pp, "lock_list_size")
            prop(pp, "th_drag")
            prop(pp, "th_double_click")
            prop(pp, "win_check_overlap")
            prop(pp, "win_overlap_offset")
            prop(pp, "filter_match_case")
            prop(pp, "filter_match_whole_word")
            prop(pp, "filter_match_end")
            prop(pp, "filter_autopan_active")
            prop(pp, "filter_adaptive_selection")
            prop(pp, "filter_delete_behavior")
            prop(pp, "cursor_beam_time")
            prop(pp, "use_select_all")
            prop(pp, "pan_invert")
            prop(pp, "scroll_distance")
            prop(pp, "valbox_drag_fac_int")
            prop(pp, "valbox_drag_fac_float")
            prop(pp, "button_repeat_time")
            prop(pp, "button_repeat_interval")
            prop(pp, "use_py_exp")
            prop(pp, "show_rm_keymap")
            prop(pp, "adaptive_enum_input")
            prop(pp, "adaptive_win_resize")
            prop(pp, "undo_steps_local")
            prop(pp, "format_float")
            prop(pp, "format_hex")
            prop(pp, "anim_filter")
            prop(pp, "animtime_filter")
            prop(pp, "cursor_picker")
            prop(pp, "cursor_pan")
            prop(pp, "md_lib_filepath")
            prop(pp, "md_lib_filter")
            prop(pp, "md_lib_method")
            prop(pp, "md_lib_use_essentials")
            prop(pp, "preview_scale")
            prop(pp, "preview_showname")
            prop(pp, "prop_image_dd_showicon")
            prop(pp, "fontpath_method")
            prop(pp, "fontpath_ui")
            prop(pp, "fontpath_ui_mono")
            prop(pp, "is_open_driver_editor")
            prop(pp, "blocklist_column_len")
            prop(pp, "font_shadow_method")
            prop(pp, "font_shadow_hardness")
            prop(pp, "font_shadow_offset")
            # >>>

        header, panel = layout.panel("VMD_SIZE_PT_Panel", default_closed=True)
        header.label(text="Size")
        if panel:
            prop = panel.prop
            pp = P.size
            sep = panel.separator
            oper = panel.operator

            panel.label(text='Press "Reload Icon" after changing UI size', icon="INFO")
            panel.label(text="This behavior will be performed automatically in the Settings Editor")
            oper("wm.vmd_reload_icon", text="Reload Icon")
            sep()
            oper("wm.vmd_ui_scale", text="Set UI Scale to 1.0").factor = 1.0
            oper("wm.vmd_ui_scale", text="Set UI Scale to 1.33").factor = 1.33
            oper("wm.vmd_ui_scale", text="Set UI Scale to 1.66").factor = 1.66
            oper("wm.vmd_ui_scale", text="Set UI Scale to 2.0").factor = 2.0
            sep()
            for k in pp.__annotations__:
                prop(pp, k)


        header, panel = layout.panel("VMD_COLOR_PT_Panel", default_closed=True)
        header.label(text="Color")
        if panel:
            prop = panel.prop
            label = panel.label
            pp = P.color

            label(text="This category does not provide a", icon="INFO")
            label(text="correct color space preview,")
            label(text="to preview accurate results please go")
            label(text="to the Settings Editor >")
            label(text="Personalization > UI Color")
            panel.separator()

            for k in pp.__annotations__:
                prop(pp, k)

        header, panel = layout.panel("VMD_EDITOR_PT_Panel", default_closed=True)
        header.label(text="Editor")
        if panel:
            for clsname, cls in m.D_EDITOR.items():
                header, subpanel = panel.panel(f"VMD_EDITOR_{clsname}_PT_Panel", default_closed=True)
                header.label(text=cls.name)
                if subpanel:
                    prop = subpanel.prop
                    pp = getattr(P, clsname)
                    for k in pp.__annotations__:
                        prop(pp, k)
        #|
    #|
    #|


## _file_ ##
def late_import():
    #|
    from .  import VMD

    m = VMD.m
    Admin = m.Admin
    W_MODAL = m.W_MODAL

    # <<< 1copy (assignP,, $$)
    P = bpy.context.preferences.addons[__package__].preferences
    # >>>

    globals().update(locals())
    #|
