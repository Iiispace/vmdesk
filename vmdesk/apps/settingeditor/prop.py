
from .  import VMD

# <<< 1mp (VMD.util.types
types = VMD.util.types
blRna = types.blRna
RnaButton = types.RnaButton
RnaString = types.RnaString
RnaEnum = types.RnaEnum
RnaBool = types.RnaBool
RnaFloat = types.RnaFloat
# >>>

# <<< 1mp (VMD.keysys
keysys = VMD.keysys
ENUMS_keymap_value = keysys.ENUMS_keymap_value
# >>>


RNA_header_button = RnaButton("header_button",
    name = "Header Button",
    button_text = "",
    description = "Settings Editor header button")
RNA_header_media_text = RnaString("header_media_text",
    name = "Directory Path",
    description = "Path of directory in Settings Editor")
RNA_edit_expression = RnaButton("edit_expression",
    name = "Calculator Expressions",
    button_text = "Edit Expression",
    description = "Edit expression in Text Editor")
RNA_md_lib_refresh = RnaButton("md_lib_refresh",
    name = "Refresh",
    button_text = "Update Library",
    description = "Update library paths")
RNA_md_lib_edit = RnaButton("md_lib_edit",
    name = "Modifier Library Paths",
    button_text = "Edit Directories",
    description = "Edit library paths")
RNA_ui_scale_100 = RnaButton("ui_scale_100",
    name = "UI Scale 1.0",
    button_text = "Set UI Scale to 1.0",
    description = "Set add-on UI Scale to 1.0")
RNA_ui_scale_133 = RnaButton("ui_scale_133",
    name = "UI Scale 1.33",
    button_text = "Set UI Scale to 1.33",
    description = "Set add-on UI Scale to 1.33")
RNA_ui_scale_166 = RnaButton("ui_scale_166",
    name = "UI Scale 1.66",
    button_text = "Set UI Scale to 1.66",
    description = "Set add-on UI Scale to 1.66")
RNA_ui_scale_200 = RnaButton("ui_scale_200",
    name = "UI Scale 2.0",
    button_text = "Set UI Scale to 2.0",
    description = "Set add-on UI Scale to 2.0")
RNA_ui_reload_icon = RnaButton("ui_reload_icon",
    name = "Reload Icon",
    button_text = "Reload Icon",
    description = "Reload icons after changing UI size")
RNA_ui_reload_font = RnaButton("ui_reload_font",
    name = "Reload Font",
    button_text = "Reload Font",
    description = "Reload UI Fonts after changing blender Theme / Text Rendering settings (like Subpixel Anti-Aliasing)")
RNA_pref_export = RnaButton("pref_export",
    name = "Export Preference Settings",
    button_text = "Export",
    description = "Export add-on preference settings")
RNA_pref_import = RnaButton("pref_import",
    name = "Import Preference Settings",
    button_text = "Import",
    description = "Import add-on preference settings")
RNA_pref_export_theme = RnaButton("pref_export_theme",
    name = "Export Preference Theme Settings",
    button_text = "Export",
    description = "Export add-on preference theme settings")
RNA_pref_import_theme = RnaButton("pref_import_theme",
    name = "Import Preference Theme Settings",
    button_text = "Import",
    description = "Import add-on preference theme settings")
RNA_pref_load_theme_dark = RnaButton("loadtheme_dark",
    name = "Load Theme Dark",
    button_text = "Load Default Dark",
    description = "Set all color settings to default value")

RNA_edit_keystroke0 = RnaButton("edit_keystroke0",
    name = "Edit Keystroke 1",
    button_text = "Edit 1",
    description = "Edit key combinations 1.",
    size = -3)
RNA_edit_keystroke1 = RnaButton("edit_keystroke1",
    name = "Edit Keystroke 2",
    button_text = "Edit 2",
    description = "Edit key combinations 2.",
    size = -3)
RNA_keycatch_save = RnaButton("keycatch_save",
    name = "Keymap Save",
    button_text = "Save",
    description = "Save Keystroke.",
    size = 3)
RNA_keycatch_clear = RnaButton("keycatch_clear",
    name = "Keymap Clear",
    button_text = "Clear",
    description = "Clear Keystroke.",
    size = 3)
RNA_keycomb0 = RnaString("keycomb0",
    name = "Comb 1",
    description = "Key Combination 1")
RNA_keycomb1 = RnaString("keycomb1",
    name = "Comb 2",
    description = "Key Combination 2")
RNA_keycombcatch = RnaString("keycombcatch",
    name = "Keystroke Catch",
    description = "Captures key combinations when the mouse is placed over a specific area.",
    is_readonly = True)
RNA_keyvalue0 = RnaEnum("keyvalue0", ENUMS_keymap_value,
    name = "Value 1",
    description = "Behavior that triggers the keymap Combination 1.",
    default = "PRESS")
RNA_keyvalue1 = RnaEnum("keyvalue1", ENUMS_keymap_value,
    name = "Value 2",
    description = "Behavior that triggers the keymap Combination 2.",
    default = "PRESS")
RNA_keyendvalue0 = RnaEnum("keyendvalue0", ENUMS_keymap_value,
    name = "End Value 1",
    description = "Behavior that triggers the keymap Combination 1.",
    default = "RELEASE")
RNA_keyendvalue1 = RnaEnum("keyendvalue1", ENUMS_keymap_value,
    name = "End Value 2",
    description = "Behavior that triggers the keymap Combination 2.",
    default = "RELEASE")
RNA_keyexact0 = RnaBool("keyexact0",
    name = "Is Exact 1",
    description = "When set to True, Keymap 1 will trigger when the number of keys pressed equals the key combination.")
RNA_keyexact1 = RnaBool("keyexact1",
    name = "Is Exact 2",
    description = "When set to True, Keymap 2 will trigger when the number of keys pressed equals the key combination.")
RNA_keyduration0 = RnaFloat('keyduration0',
    name = "Duration 1",
    description = "Used for Keymap 1 value in (Double Press, Double Release, Hold)",
    default = 0.3,
    hard_min = 0.0,
    hard_max = 9.0)
RNA_keyduration1 = RnaFloat('keyduration1',
    name = "Duration 2",
    description = "Used for Keymap 2 value in (Double Press, Double Release, Hold)",
    default = 0.3,
    hard_min = 0.0,
    hard_max = 9.0)

RNA_text_search = RnaString("text_search",
    name = "Search Text",
    description = "Search for properties in the Settings Editor.")
RNA_use_search_id = RnaBool("use_search_id",
    name = "Include ID",
    description = "Search properties from identifier.")
RNA_use_search_name = RnaBool("use_search_name",
    name = "Include Name",
    description = "Search properties from name.")
RNA_use_search_description = RnaBool("use_search_description",
    name = "Include Description",
    description = "Search properties from description.")
RNA_use_search_cat_pref = RnaBool("use_search_cat_pref",
    name = "Include General Properties",
    description = "Search Properties by general category.")
RNA_use_search_cat_pref_color = RnaBool("use_search_cat_pref_color",
    name = "Include Color Properties",
    description = "Search properties by color category.")
RNA_use_search_cat_pref_size = RnaBool("use_search_cat_pref_size",
    name = "Include Size Properties",
    description = "Search properties by size category.")
RNA_use_search_cat_pref_keymap = RnaBool("use_search_cat_pref_keymap",
    name = "Include Keymap Properties",
    description = "Search properties by keymap category.")
RNA_use_search_cat_pref_apps = RnaBool("use_search_cat_pref_apps",
    name = "Include Editor Properties",
    description = "Search properties by editor category.")
RNA_about = RnaString("about",
    name = "About",
    description = "Info",
    default = "",
    is_readonly = True)
RNA_ops_refresh = RnaButton("ops_refresh",
    name = "Refresh Operator List",
    button_text = "Refresh Operator List",
    description = "Refresh operator list")
