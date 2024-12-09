import bpy

props = bpy.props
bpytypes = bpy.types

# <<< 1mp (props
StringProperty = props.StringProperty
EnumProperty = props.EnumProperty
BoolProperty = props.BoolProperty
BoolVectorProperty = props.BoolVectorProperty
IntProperty = props.IntProperty
IntVectorProperty = props.IntVectorProperty
FloatProperty = props.FloatProperty
FloatVectorProperty = props.FloatVectorProperty
PointerProperty = props.PointerProperty
# >>>

# <<< 1mp (bpytypes
PropertyGroup = bpytypes.PropertyGroup
BakeSettings = bpytypes.BakeSettings
Image = bpytypes.Image
ColorManagedInputColorspaceSettings = bpytypes.ColorManagedInputColorspaceSettings
# >>>


# /* 0prefs_CALC_EXP_DEFAULT
CALC_EXP_DEFAULT = {
    'Float': [
        ['- 0.1 ', 'x-0.1'],
        ['+ 0.1', 'x+0.1'],
        ['- 0.01 ', 'x-0.01'],
        ['+ 0.01', 'x+0.01'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
        ['Round 2', 'round(x,2)'],
        ['Ran [0,1]', 'random()']
    ],
    'Int': [
        [' - 1', 'x-1'],
        [' + 1', 'x+1'],
        [' - 10', 'x-10'],
        [' + 10', 'x+10'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
        ['= 0', '0'],
        ['Ran [0,100]', 'round(100*random())'],
    ],
    'Radians': [
        ['- π/180', 'x-pi/180'],
        ['+ π/180', 'x+pi/180'],
        ['＝ π/4', 'pi/4'],
        ['＝ π/6', 'pi/6'],
        ['＝ π/3', 'pi/3'],
        ['＝ π', 'pi'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
    ],
    'Degrees': [
        [' - 1', 'x-1'],
        [' + 1', 'x+1'],
        ['= 45', '45'],
        ['= 30', '30'],
        ['= 60', '60'],
        ['= 90', '90'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
    ],
}
# */
STR_CALC_EXP_DEFAULT = '''# Calculator Expression
# Float, Int, Radians, Degrees categories must include
# New categories added must contain 10 items
# Add a semicolon at the beginning of the expression to use python expressions
# ['Button Name', ';x + 1e-38']
# Global variables:
#     x : current value
#     o : original value
# <<< 1copy (0prefs_CALC_EXP_DEFAULT,, $$)
CALC_EXP_DEFAULT = {
    'Float': [
        ['- 0.1 ', 'x-0.1'],
        ['+ 0.1', 'x+0.1'],
        ['- 0.01 ', 'x-0.01'],
        ['+ 0.01', 'x+0.01'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
        ['Round 2', 'round(x,2)'],
        ['Ran [0,1]', 'random()']
    ],
    'Int': [
        [' - 1', 'x-1'],
        [' + 1', 'x+1'],
        [' - 10', 'x-10'],
        [' + 10', 'x+10'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
        ['= 0', '0'],
        ['Ran [0,100]', 'round(100*random())'],
    ],
    'Radians': [
        ['- π/180', 'x-pi/180'],
        ['+ π/180', 'x+pi/180'],
        ['＝ π/4', 'pi/4'],
        ['＝ π/6', 'pi/6'],
        ['＝ π/3', 'pi/3'],
        ['＝ π', 'pi'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
    ],
    'Degrees': [
        [' - 1', 'x-1'],
        [' + 1', 'x+1'],
        ['= 45', '45'],
        ['= 30', '30'],
        ['= 60', '60'],
        ['= 90', '90'],
        ['／2 ', 'x/2'],
        ['╳ 2', 'x*2'],
        ['√x', 'rt(x)'],
        ['x ²', 'x*x'],
    ],
}
# >>>
'''.replace("CALC_EXP_DEFAULT = ", "")


def upd_pref(self, context): U_UPD_PREF()
def upd_F(self, context): U_UPD_SIZE()
def upd_win_active(self, context): U_UPD_WIN_ACTIVE()
def upd_refresh(self, context): pass
def upd_pref_unit(self, context):
    U_UPD_PREF()

    from .  import m
    m.UnitSystem.update()
    #|
def upd_pref_font_render(self, context):
    from . m import make_TEXT_RENDER
    make_TEXT_RENDER()
    U_UPD_PREF()
    #|

class SharedEnumItems:
    __slots__ = ()

    window_cursor_items = (
        ("DEFAULT", "Default", ""),
        ("NONE", "None", ""),
        ("WAIT", "Wait", ""),
        ("CROSSHAIR", "Crosshair", ""),
        ("MOVE_X", "Move-X", ""),
        ("MOVE_Y", "Move-Y", ""),
        ("KNIFE", "Knife", ""),
        ("TEXT", "Text", ""),
        ("PAINT_BRUSH", "Paint Brush", ""),
        ("PAINT_CROSS", "Paint Cross", ""),
        ("DOT", "Dot Cursor", ""),
        ("ERASER", "Eraser", ""),
        ("HAND", "Hand", ""),
        ("SCROLL_X", "Scroll-X", ""),
        ("SCROLL_Y", "Scroll-Y", ""),
        ("SCROLL_XY", "Scroll-XY", ""),
        ("EYEDROPPER", "Eyedropper", ""),
        ("PICK_AREA", "Pick Area", ""),
        ("STOP", "Stop", ""),
        ("COPY", "Copy", ""),
        ("CROSS", "Cross", ""),
        ("MUTE", "Mute", ""),
        ("ZOOM_IN", "Zoom In", ""),
        ("ZOOM_OUT", "Zoom Out", ""))
    #|
    #|

class PrefsModifierEditor(PropertyGroup):
    __slots__ = ()

    pos: IntVectorProperty(
        name = "Modifier Editor: Initial Position", size = 2, min = -65535, max = 65535,
        default = (80, 739),
        description = "Window position during call",
        update = upd_pref,
        options = set())
    size: IntVectorProperty(
        name = "Modifier Editor: Initial Size", size = 2, min = 0, max = 65535,
        default = (638, 441),
        description = "Editor size when called",
        update = upd_pref,
        options = set())
    is_fold: BoolProperty(
        name = "Modifier Editor: Fold Default",
        description = "Collapse all blocks by default",
        update = upd_pref,
        options = set())
    is_sync_object: BoolProperty(
        name = "Modifier Editor: Sync Object",
        description = "Default value. Sync active object",
        default = True,
        update = upd_pref,
        options = set())
    is_sync_modifier: BoolProperty(
        name = "Modifier Editor: Sync Modifier",
        description = "Default value. Sync active modifier",
        default = True,
        update = upd_pref,
        options = set())
    is_sync_object_2: BoolProperty(
        name = "Modifier Editor: Sync Object 2",
        description = "Default value. Sync active object for non-first editors",
        default = False,
        update = upd_pref,
        options = set())
    is_sync_modifier_2: BoolProperty(
        name = "Modifier Editor: Sync Modifier 2",
        description = "Default value. Sync active modifier for non-first editors",
        default = False,
        update = upd_pref,
        options = set())
    md_copy_use_keyframe: BoolProperty(
        name = "Modifier Editor: Keep Keyframe",
        description = "Default value. Keep Keyframe in Copy modifier operation menu",
        default = True,
        update = upd_pref,
        options = set())
    md_copy_use_driver: BoolProperty(
        name = "Modifier Editor: Keep Driver",
        description = "Default value. Keep Driver in Copy modifier operation menu",
        default = True,
        update = upd_pref,
        options = set())
    md_copy_to_selected_use_keyframe: BoolProperty(
        name = "Modifier Editor: Keep Keyframe (Copy to Selected)",
        description = "Default value. Keep Keyframe in Copy to Selected menu",
        default = True,
        update = upd_pref,
        options = set())
    md_copy_to_selected_use_driver: BoolProperty(
        name = "Modifier Editor: Keep Driver (Copy to Selected)",
        description = "Default value. Keep Driver in Copy to Selected menu",
        default = True,
        update = upd_pref,
        options = set())
    md_copy_to_selected_use_mouse_index: BoolProperty(
        name = "Modifier Editor: Use Mouse Index (Copy to Selected)",
        description = "Default value. Include modifier via mouse index",
        default = False,
        update = upd_pref,
        options = set())
    md_copy_to_selected_use_selection: BoolProperty(
        name = "Modifier Editor: Use Selection (Copy to Selected)",
        description = "Default value. Include selected modifiers",
        default = True,
        update = upd_pref,
        options = set())
    md_copy_to_selected_use_self: BoolProperty(
        name = "Modifier Editor: Use Self (Copy to Selected)",
        description = "Default value. Include self-object",
        default = False,
        update = upd_pref,
        options = set())
    md_copy_to_selected_operation: EnumProperty(
        name = "Modifier Editor: Operation (Copy to Selected)",
        description = "Default value. Operation",
        items = (
            ("COPY", "Copy", ""),
            ("LINK", "Link", ""),
            ("DEEPLINK", "Deep Link", "")),
        default = "COPY",
        update = upd_pref,
        options = set())
    area_rowlen_obj: IntProperty(
        name = "Modifier Editor: Area Rows (Objects)", min = 0, max = 63, default = 6,
        description = "Default value :  Number of object filter rows.\nProperty override\n    0: (Size: Filter)",
        update = upd_F,
        options = set())
    md_copy_to_selected_use_code: BoolProperty(
        name = "Modifier Editor: Override code (Copy to Selected)",
        description = "Default value. Override the Python code",
        default = False,
        update = upd_pref,
        options = set())
    area_rowlen_mds: IntProperty(
        name = "Modifier Editor: Area Rows (Modifiers)", min = 0, max = 63, default = 10,
        description = "Default value :  Number of modifier list rows.\nProperty override\n    0: (Size: Filter)",
        update = upd_F,
        options = set())
    area_widthfac_tab: FloatProperty(
        name = "Modifier Editor: Area Width Factor (Tab)", min = 0.1, max = 63.0, default = 1.0,
        description = "Default value :  Width factor of Tab area",
        update = upd_F,
        options = set())
    area_widthfac_filter: FloatProperty(
        name = "Modifier Editor: Area Width Factor (Filter)", min = 0.1, max = 63.0, default = 1.0,
        description = "Default value :  Width factor of Filter area",
        update = upd_F,
        options = set())
    area_list_inner: IntProperty(
        name = "Modifier Editor: Area List Inner", min = 0, max = 255, default = 8,
        description = "Additional distance between Object List and Modifier List",
        update = upd_F,
        options = set())
    search_prop_use_identifier: BoolProperty(
        name = "Modifier Editor: Use Identifier",
        description = "Default value of Use Identifier in Search Properties menu",
        default = True,
        update = upd_pref,
        options = set())
    search_prop_use_name: BoolProperty(
        name = "Modifier Editor: Use Name",
        description = "Default value of Use Name in Search Properties menu",
        default = True,
        update = upd_pref,
        options = set())
    search_prop_use_description: BoolProperty(
        name = "Modifier Editor: Use Description",
        description = "Default value of Use Description in Search Properties menu",
        default = True,
        update = upd_pref,
        options = set())
    use_gn_layout: BoolProperty(
        name = "Modifier Editor: Use Custom Socket Layout",
        description = "Use custom socket layout in Geometry Nodes Modifier",
        default = True,
        update = upd_pref,
        options = set())

    SIZE_CALLBACKS = {
        "area_list_inner",
        "area_rowlen_obj",
        "area_rowlen_mds",
        "area_widthfac_tab",
        "area_widthfac_filter"}

    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences.ModifierEditor'
        #|
    #|
    #|

class PrefsDriverEditor(PropertyGroup):
    __slots__ = ()

    pos: IntVectorProperty(
        name = "Driver Editor: Initial Position", size = 2, min = -65535, max = 65535,
        default = (80, 500),
        description = "Window position during call",
        update = upd_pref,
        options = set())
    size: IntVectorProperty(
        name = "Driver Editor: Initial Size", size = 2, min = 0, max = 65535,
        default = (428, 418),
        description = "Editor size when called",
        update = upd_pref,
        options = set())
    is_fold: BoolProperty(
        name = "Driver Editor: Fold Default",
        description = "Collapse all blocks by default",
        update = upd_pref,
        options = set())
    area_widthfac: FloatProperty(
        name = "Driver Editor: Area Width Factor", min = 1.0, max = 63.0, default = 1.0,
        description = "Default value :  Width factor",
        update = upd_pref,
        options = set())

    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences.DriverEditor'
        #|
    #|
    #|

class PrefsSettingEditor(PropertyGroup):
    __slots__ = ()

    pos: IntVectorProperty(
        name = "Settings: Initial Position", size = 2, min = -65535, max = 65535,
        default = (80, 739),
        description = "Window position during call",
        update = upd_pref,
        options = set())
    size: IntVectorProperty(
        name = "Settings: Initial Size", size = 2, min = 0, max = 65535,
        default = (572, 543),
        description = "Editor size when called",
        update = upd_pref,
        options = set())
    is_fold: BoolProperty(
        name = "Settings: Fold Default",
        description = "Collapse all blocks by default",
        default = True,
        update = upd_pref,
        options = set())
    is_fold_search: BoolProperty(
        name = "Settings: Search Block Fold Default",
        description = "Collapse Search Block by default",
        default = False,
        update = upd_pref,
        options = set())
    use_search_id: BoolProperty(
        name = "Settings: Search By ID",
        description = "Default value of Search By ID",
        default = True,
        update = upd_pref,
        options = set())
    use_search_name: BoolProperty(
        name = "Settings: Search By Name",
        description = "Default value of Search By Name",
        default = True,
        update = upd_pref,
        options = set())
    use_search_description: BoolProperty(
        name = "Settings: Search By Description",
        description = "Default value of Search By Description",
        default = True,
        update = upd_pref,
        options = set())
    use_search_cat_pref: BoolProperty(
        name = "Settings: Search by General Category",
        description = "Default value of Search by General Category",
        default = True,
        update = upd_pref,
        options = set())
    use_search_cat_pref_color: BoolProperty(
        name = "Settings: Search by Color Category",
        description = "Default value of Search by Color Category",
        default = True,
        update = upd_pref,
        options = set())
    use_search_cat_pref_size: BoolProperty(
        name = "Settings: Search by Size Category",
        description = "Default value of Search by Size Category",
        default = True,
        update = upd_pref,
        options = set())
    use_search_cat_pref_keymap: BoolProperty(
        name = "Settings: Search by Keymap Category",
        description = "Default value of Search by Keymap Category",
        default = True,
        update = upd_pref,
        options = set())
    use_search_cat_pref_apps: BoolProperty(
        name = "Settings: Search by Editor Category",
        description = "Default value of Search by Editor Category",
        default = True,
        update = upd_pref,
        options = set())
    area_height: IntProperty(
        name = "Settings: Area Height", min = 2, max = 512, default = 28,
        description = "Settings Editor area height. The height is this value multiplied by Wedget Height. Effect only on new windows",
        update = upd_F,
        options = set())

    SIZE_CALLBACKS = {
        "area_height"}

    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences.SettingEditor'
        #|
    #|
    #|

class PrefsMeshEditor(PropertyGroup):
    __slots__ = ()

    pos: IntVectorProperty(
        name = "Mesh Editor: Initial Position", size = 2, min = -65535, max = 65535,
        default = (80, 739),
        description = "Window position during call",
        update = upd_pref,
        options = set())
    size: IntVectorProperty(
        name = "Mesh Editor: Initial Size", size = 2, min = 0, max = 65535,
        default = (374, 400),
        description = "Editor size when called",
        update = upd_pref,
        options = set())
    is_fold: BoolProperty(
        name = "Mesh Editor: Fold Default",
        description = "Collapse all blocks by default",
        update = upd_pref,
        options = set())
    vert_limit: IntProperty(
        name = "Mesh Editor: Vertex Limit", min = 3,
        default = 999,
        description = "Deactivate the property when the selected vertex count exceeds this value",
        update = upd_pref,
        options = set())
    area_widthfac: FloatProperty(
        name = "Mesh Editor: Area Width Factor (Tab)", min = 1.0, max = 63.0, default = 1.0,
        description = "Default value :  Width factor of Tab area",
        update = upd_pref,
        options = set())
    area_heightfac: FloatProperty(
        name = "Mesh Editor: Area Height Factor (Tab)", min = 0.1, max = 63.0, default = 1.0,
        description = "Default value :  Height factor of Tab area",
        update = upd_pref,
        options = set())
    use_ui_preview: BoolProperty(
        name = "Mesh Editor: UI Preview",
        description = "Show additional information when hovering over properties. Only affects new windows",
        default = True,
        update = upd_pref,
        options = set())

    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences.MeshEditor'
        #|
    #|
    #|


class PrefsKey(PropertyGroup):
    __slots__ = ()

    # /* 0prefs_key
    esc: IntVectorProperty(
        name = "Esc",
        description = "Key: Cancel",
        default = (65, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_esc: IntVectorProperty(
        name = "Menu Esc",
        description = "Key: Drop Down Menu Cancel",
        default = (65, 1050253722, 3, 1050253722, 513),
        size = 5, options = {"HIDDEN"})
    click: IntVectorProperty(
        name = "Click",
        description = "Key: Left Mouse Button",
        default = (1, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    title_move: IntVectorProperty(
        name = "Title Move",
        description = "Key: Move Window from Title Bar",
        default = (1, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    title_button: IntVectorProperty(
        name = "Title Button",
        description = "Key: Window Title Bar Button",
        default = (1, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    resize: IntVectorProperty(
        name = "Resize",
        description = "Key: Window Resize",
        default = (1, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    pan: IntVectorProperty(
        name = "Pan",
        description = "Key: Pan the canvas",
        default = (2, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    pan_win: IntVectorProperty(
        name = "Pan Window",
        description = "Key: Pan the global canvas",
        default = (3, 1050253722, 0, 1050253722, 261, 514),
        size = 6, options = {"HIDDEN"})
    rm: IntVectorProperty(
        name = "Context Menu",
        description = "Key: Right Click menu",
        default = (3, 1036831949, 0, 1050253722, 271),
        size = 5, options = {"HIDDEN"})
    rm_km_toggle: IntVectorProperty(
        name = "Keymap Display Toggle",
        description = "Key: Show / Hide Keymap Display in Context Menu",
        default = (7736, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    rm_km_change: IntVectorProperty(
        name = "Change Keymap",
        description = "Key: Change Keymap",
        default = (507066426, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    redo: IntVectorProperty(
        name = "Redo",
        description = "Key: Redo previous action",
        default = (2963514, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    undo: IntVectorProperty(
        name = "Undo",
        description = "Key: Undo previous action",
        default = (11576, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    detail: IntVectorProperty(
        name = "Detail",
        description = "Key: Detail",
        default = (104, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    fold_all_recursive_toggle: IntVectorProperty(
        name = "Fold All Recursive Toggle",
        description = "Key: Recursively Collapse all blocks / Recursively Expand All Blocks",
        default = (9530, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    fold_all_toggle: IntVectorProperty(
        name = "Fold All Toggle",
        description = "Key: Collapse all blocks / Expand All Blocks",
        default = (37, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    fold_recursive_toggle: IntVectorProperty(
        name = "Fold Recursive Toggle",
        description = "Key: Recursively Collapse block / Recursively Expand Block",
        default = (9274, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    fold_toggle: IntVectorProperty(
        name = "Fold Toggle",
        description = "Key: Collapse block / Expand Block",
        default = (36, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    rename: IntVectorProperty(
        name = "Rename",
        description = "Key: Rename",
        default = (1, 1050253722, 0, 1050253722, 259),
        size = 5, options = {"HIDDEN"})

    dd_match_end: IntVectorProperty(
        name = "Text Match End Toggle",
        description = "Key: Toggle Match End option in Filter",
        default = (6201, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_match_case: IntVectorProperty(
        name = "Text Match Case Toggle",
        description = "Key: Toggle Match Case option in Filter",
        default = (5689, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_match_whole_word: IntVectorProperty(
        name = "Text Match Whole Word Toggle",
        description = "Key: Toggle Match Whole Word option in Filter",
        default = (10809, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_select_all: IntVectorProperty(
        name = "Select all Text Toggle",
        description = "Key: Select all character, Deselect all if all selected",
        default = (5176, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_select_word: IntVectorProperty(
        name = "Select Word",
        description = "Key: Select Word from Beam Cursor",
        default = (1, 1050253722, 0, 1050253722, 259),
        size = 5, options = {"HIDDEN"})
    dd_cut: IntVectorProperty(
        name = "Text Cut",
        description = "Key: Cut character from selection, Cut all when no selection",
        default = (11064, 1050253722, 0, 1050253722, 65793),
        size = 5, options = {"HIDDEN"})
    dd_paste: IntVectorProperty(
        name = "Text Paste",
        description = "Key: Paste character from selection / I-Beam cursor",
        default = (10552, 1050253722, 0, 1050253722, 65793),
        size = 5, options = {"HIDDEN"})
    dd_copy: IntVectorProperty(
        name = "Text Copy",
        description = "Key: Copy character from selection / I-Beam cursor",
        default = (5688, 1050253722, 0, 1050253722, 65793),
        size = 5, options = {"HIDDEN"})
    dd_del_all: IntVectorProperty(
        name = "Delete all Text",
        description = "Key: Remove all characters",
        default = (18232, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_del: IntVectorProperty(
        name = "Delete Selection / Line",
        description = "Key: Remove all characters in selection / Remove current line",
        default = (71, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_del_word: IntVectorProperty(
        name = "Text Word Backspace",
        description = "Key: Removes whole word from the I-Beam cursor, and if there is a selection, removes the selection",
        default = (17976, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_del_chr: IntVectorProperty(
        name = "Text Backspace",
        description = "Key: Removes 1 character from the I-Beam cursor, and if there is a selection, removes the selection",
        default = (70, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_line_begin_shift: IntVectorProperty(
        name = "Text Cursor Line Begin Select",
        description = "Key: Move I-Beam Cursor to Line Begin and extend the selection",
        default = (6240314, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_line_end_shift: IntVectorProperty(
        name = "Text Cursor Line End Select",
        description = "Key: Move I-Beam Cursor to Line End and extend the selection",
        default = (6305850, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_left_word_shift: IntVectorProperty(
        name = "Text Cursor Previous Word Select",
        description = "Key: Move I-Beam Cursor to Previous Word and extend the selection",
        default = (5847098, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_right_word_shift: IntVectorProperty(
        name = "Text Cursor Next Word Select",
        description = "Key: Move I-Beam Cursor to Next Word and extend the selection",
        default = (5912634, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_left_shift: IntVectorProperty(
        name = "Text Cursor Left Select",
        description = "Key: Move I-Beam Cursor Left and extend the selection",
        default = (21562, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_right_shift: IntVectorProperty(
        name = "Text Cursor Right Select",
        description = "Key: Move I-Beam Cursor Right and extend the selection",
        default = (22074, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_down_shift: IntVectorProperty(
        name = "Text Cursor Down Select",
        description = "Key: Move I-Beam Cursor Down and extend the selection",
        default = (21818, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_up_shift: IntVectorProperty(
        name = "Text Cursor Up Select",
        description = "Key: Move I-Beam Cursor Up and extend the selection",
        default = (22330, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_line_begin: IntVectorProperty(
        name = "Text Cursor Line Begin",
        description = "Key: Move I-Beam Cursor to Line Begin",
        default = (24376, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_line_end: IntVectorProperty(
        name = "Text Cursor Line End",
        description = "Key: Move I-Beam Cursor to Line End",
        default = (24632, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_left_word: IntVectorProperty(
        name = "Text Cursor Previous Word",
        description = "Key: Move I-Beam Cursor to Previous Word",
        default = (22840, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_right_word: IntVectorProperty(
        name = "Text Cursor Next Word",
        description = "Key: Move I-Beam Cursor to Next Word",
        default = (23096, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_left: IntVectorProperty(
        name = "Text Cursor Left",
        description = "Key: Move I-Beam Cursor Left",
        default = (84, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_right: IntVectorProperty(
        name = "Text Cursor Right",
        description = "Key: Move I-Beam Cursor Right",
        default = (86, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_down: IntVectorProperty(
        name = "Text Cursor Down / Filter selection Down",
        description = "Key: Move I-Beam Cursor Down or select results in filters",
        default = (85, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_up: IntVectorProperty(
        name = "Text Cursor Up / Filter selection Up",
        description = "Key: Move I-Beam Cursor Up or select results in filters",
        default = (87, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_end_shift: IntVectorProperty(
        name = "Text Cursor End Select",
        description = "Key: Move I-Beam Cursor to End and extend the selection",
        default = (34104, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_start_shift: IntVectorProperty(
        name = "Text Cursor Start Select",
        description = "Key: Move I-Beam Cursor to Start and extend the selection",
        default = (33336, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_end: IntVectorProperty(
        name = "Text Cursor End",
        description = "Key: Move I-Beam Cursor to End",
        default = (133, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_beam_start: IntVectorProperty(
        name = "Text Cursor Start",
        description = "Key: Move I-Beam Cursor to Start",
        default = (130, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_left_most: IntVectorProperty(
        name = "Scrollbar Most Left",
        description = "Key: Move the Scrollbar to the far left",
        default = (8599864, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_right_most: IntVectorProperty(
        name = "Scrollbar Most Right",
        description = "Key: Move the Scrollbar to the far right",
        default = (8665400, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_down_most: IntVectorProperty(
        name = "Scrollbar Bottom",
        description = "Key: Move the Scrollbar to bottom",
        default = (33848, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_up_most: IntVectorProperty(
        name = "Scrollbar Top",
        description = "Key: Move the Scrollbar to Top",
        default = (33592, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_left: IntVectorProperty(
        name = "Scrollbar Left",
        description = "Key: Move the Scrollbar left",
        default = (33593, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_right: IntVectorProperty(
        name = "Scrollbar Right",
        description = "Key: Move the Scrollbar right",
        default = (33849, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_down: IntVectorProperty(
        name = "Scrollbar Down",
        description = "Key: Move the Scrollbar down",
        default = (132, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_up: IntVectorProperty(
        name = "Scrollbar Up",
        description = "Key: Move the Scrollbar up",
        default = (131, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_left_area: IntVectorProperty(
        name = "Scrollbar Left Area",
        description = "Key: Move the Scrollbar left in Scrollbar area",
        default = (18, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_right_area: IntVectorProperty(
        name = "Scrollbar Right Area",
        description = "Key: Move the Scrollbar right in Scrollbar area",
        default = (19, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_down_area: IntVectorProperty(
        name = "Scrollbar Down Area",
        description = "Key: Move the Scrollbar down in Scrollbar area",
        default = (17, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll_up_area: IntVectorProperty(
        name = "Scrollbar Up Area",
        description = "Key: Move the Scrollbar up in Scrollbar area",
        default = (16, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_scroll: IntVectorProperty(
        name = "Scrollbar Operation",
        description = "Key: Move the Scrollbar",
        default = (1, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    dd_selection_shift: IntVectorProperty(
        name = "Text Selection Shift",
        description = "Key: Text shift selection operation",
        default = (314, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    dd_selection: IntVectorProperty(
        name = "Text Selection",
        description = "Key: Text selection operation",
        default = (1, 1050253722, 0, 1050253722, 257, 514),
        size = 6, options = {"HIDDEN"})
    dd_confirm: IntVectorProperty(
        name = "Drop Down Menu / Text Confirm",
        description = "Key: Drop Down Menu confirm or Text confirm",
        default = (67, 1050253722, 102, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_confirm_area: IntVectorProperty(
        name = "Drop Down Menu Confirm Area",
        description = "Key: Drop Down Menu or Text confirm when the cursor is not in the Menu area",
        default = (1, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_linebreak: IntVectorProperty(
        name = "Text Line Break",
        description = "Key: Line Break",
        default = (17210, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_untab: IntVectorProperty(
        name = "Text Unindent",
        description = "Key: Text Unindent",
        default = (16954, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_tab: IntVectorProperty(
        name = "Text Tab",
        description = "Key: Text Indent / Autocomplete",
        default = (66, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    dd_preview: IntVectorProperty(
        name = "Preview",
        description = "Key: Preview Data-Block",
        default = (25, 1050253722, 9016, 1050253722, 257),
        size = 5, options = {"HIDDEN"})

    area_save_as_shapekey: IntVectorProperty(
        name = "Save as Shape Key Selected",
        description = "Key: Save selected element(s) as shape key in area",
        default = (339294776, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_apply_as_shapekey: IntVectorProperty(
        name = "Apply as Shape Key Selected",
        description = "Key: Apply selected element(s) as shape key in area",
        default = (1325624, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_apply: IntVectorProperty(
        name = "Apply Selected",
        description = "Key: Apply selected element(s) in area",
        default = (5178, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_del: IntVectorProperty(
        name = "Delete",
        description = "Key: Delete element in area",
        default = (71, 1050253722, 43, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_add: IntVectorProperty(
        name = "Add",
        description = "Key: Add new element from area",
        default = (5177, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_down_most_shift: IntVectorProperty(
        name = "Active Move to Bottom",
        description = "Key: Move the Active element to the bottom in the list from area",
        default = (1129017, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_up_most_shift: IntVectorProperty(
        name = "Active Move to Top",
        description = "Key: Move the Active element to the top in the list from area",
        default = (1063481, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_down_shift: IntVectorProperty(
        name = "Active Move Down",
        description = "Key: Move the Active element down in the list from area",
        default = (4410, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_up_shift: IntVectorProperty(
        name = "Active Move Up",
        description = "Key: Move the Active element up in the list from area",
        default = (4154, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_down_most: IntVectorProperty(
        name = "Select Active Bottom",
        description = "Key: Active index set to last from area",
        default = (4409, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_up_most: IntVectorProperty(
        name = "Select Active Top",
        description = "Key: Active index set to 0 from area",
        default = (4153, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_down: IntVectorProperty(
        name = "Select Active Down",
        description = "Key: Active index add 1 from area",
        default = (17, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_active_up: IntVectorProperty(
        name = "Select Active Up",
        description = "Key: Active index minus 1 from area",
        default = (16, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_sort: IntVectorProperty(
        name = "Move Element",
        description = "Key: Move element operation",
        default = (1, 1050253722, 0, 1050253722, 257, 513),
        size = 6, options = {"HIDDEN"})
    area_sort_modal_cancel: IntVectorProperty(
        name = "Cancel Elements",
        description = "Key: Cancel in Move Element operation",
        default = (3, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_sort_modal_apply: IntVectorProperty(
        name = "Apply Elements",
        description = "Key: Apply in Move Element operation",
        default = (20, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_sort_modal_del: IntVectorProperty(
        name = "Delete Elements",
        description = "Key: Delete in Move Element operation",
        default = (43, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_sort_modal_sort: IntVectorProperty(
        name = "Rearrange Elements",
        description = "Key: Rearrange in Move Element operation",
        default = (68, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_selectbox_extend: IntVectorProperty(
        name = "Select Box Extend",
        description = "Key: Extend existing selection from area",
        default = (314, 1050253722, 0, 1050253722, 261, 514),
        size = 6, options = {"HIDDEN"})
    area_selectbox_subtract: IntVectorProperty(
        name = "Select Box Subtract",
        description = "Key: Subtract existing selection from area",
        default = (80440, 1050253722, 0, 1050253722, 261, 514),
        size = 6, options = {"HIDDEN"})
    area_selectbox_new: IntVectorProperty(
        name = "Select Box",
        description = "Key: Set a new selection from area",
        default = (1, 1050253722, 0, 1050253722, 261, 514),
        size = 6, options = {"HIDDEN"})
    area_select_all_toggle: IntVectorProperty(
        name = "Select all Toggle",
        description = "Key: Select all, Deselect all if all selected",
        default = (5176, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_select_extend: IntVectorProperty(
        name = "Select Extend",
        description = "Key: Extend and change active element from area",
        default = (314, 1050253722, 0, 1050253722, 258),
        size = 5, options = {"HIDDEN"})
    area_select: IntVectorProperty(
        name = "Select",
        description = "Key: Change active element from area",
        default = (1, 1050253722, 0, 1050253722, 258),
        size = 5, options = {"HIDDEN"})
    area_copy_to_selected: IntVectorProperty(
        name = "Copy to Selected",
        description = "Key: Copy to Selected from area",
        default = (5689, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_unpin_to_last_selected: IntVectorProperty(
        name = "Unpin to Last Selected",
        description = "Key: Unpin to Last for selection from area",
        default = (2237241, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_pin_to_last_selected: IntVectorProperty(
        name = "Pin to Last Selected",
        description = "Key: Pin to Last for selection from area",
        default = (2237240, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    area_pin_to_last_toggle: IntVectorProperty(
        name = "Pin to Last Toggle",
        description = "Key: Toggle Pin to Last from area",
        default = (9017, 1050253722, 0, 1050253722, 258),
        size = 5, options = {"HIDDEN"})
    area_search: IntVectorProperty(
        name = "Search",
        description = "Key: Find from panel. Open/close the search properties panel",
        default = (6456, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})

    valbox_drag: IntVectorProperty(
        name = "UI Drag",
        description = "Key: Entering Value Box Drag Modal",
        default = (24, 1050253722, 0, 1050253722, 257, 513),
        size = 6, options = {"HIDDEN"})
    valbox_drag_modal_fast: IntVectorProperty(
        name = "UI Drag Modal Speed Factor Fast",
        description = "Key: Drag factor to fast in Value Box Drag Modal",
        default = (56, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    valbox_drag_modal_slow: IntVectorProperty(
        name = "UI Drag Modal Speed Factor Slow",
        description = "Key: Drag factor to slow in Value Box Drag Modal",
        default = (58, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    valbox_reset_all: IntVectorProperty(
        name = "UI Reset Array",
        description = "Key: Reset all to default values in Value Box",
        default = (70, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    valbox_reset_single: IntVectorProperty(
        name = "UI Reset Single",
        description = "Key: Reset single to default values in Value Box",
        default = (71, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    valbox_dd: IntVectorProperty(
        name = "Enter",
        description = "Key: Entering Value Box",
        default = (67, 1050253722, 102, 1050253722, 257),
        size = 5, options = {"HIDDEN"})

    ui_remove_from_keying_set_all: IntVectorProperty(
        name = "Remove All from Keying Set",
        description = "Key: Delete current UI-active property from current array keying set",
        default = (7993, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_add_to_keying_set_all: IntVectorProperty(
        name = "Add All to Keying Set",
        description = "Key: Add current UI-active property to current array keying set",
        default = (7992, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_remove_from_keying_set: IntVectorProperty(
        name = "Remove from Keying Set",
        description = "Key: Delete current UI-active property from current keying set",
        default = (7737, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_add_to_keying_set: IntVectorProperty(
        name = "Add to Keying Set",
        description = "Key: Add current UI-active property to current keying set",
        default = (7736, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_copy_full_data_path: IntVectorProperty(
        name = "Copy Full Data Path",
        description = "Key: Copy Full Data Path",
        default = (1456440, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_copy_data_path: IntVectorProperty(
        name = "Copy Data Path",
        description = "Key: Copy Data Path",
        default = (1456696, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_paste_full_data_path_as_driver: IntVectorProperty(
        name = "Paste Full Data Path as Driver",
        description = "Key: Paste Full Data Path as Driver",
        default = (2701624, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_delete_driver: IntVectorProperty(
        name = "Delete Driver",
        description = "Key: Remove Driver",
        default = (1521976, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_add_driver: IntVectorProperty(
        name = "Add / Edit Driver",
        description = "Key: Add / Edit Driver",
        default = (5944, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_clear_keyframe: IntVectorProperty(
        name = "Clear Keyframe",
        description = "Key: Clear all keyframes on the currently active property",
        default = (1849658, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_delete_keyframe: IntVectorProperty(
        name = "Delete Keyframe",
        description = "Key: Delete current keyframe of current UI-active property",
        default = (7225, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_insert_keyframe: IntVectorProperty(
        name = "Insert Keyframe",
        description = "Key: Add / Replace keyframe for current UI-active property",
        default = (28, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_jump_to_target: IntVectorProperty(
        name = "Jump to Target",
        description = "Key: Make the current object to active object",
        default = (7480, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_mark_asset: IntVectorProperty(
        name = "Mark as Asset",
        description = "Key: Mark / Clear Asset",
        default = (8248, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_format_toggle: IntVectorProperty(
        name = "Unit Toggle",
        description = "Key: Unit switching",
        default = (66, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_attr_toggle: IntVectorProperty(
        name = "Attribute Toggle",
        description = "Key: Input Attribute Toggle in Geometry Nodes Modifier",
        default = (20, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_batch: IntVectorProperty(
        name = "Batch Function",
        description = "Key: Assign values ​​to multiple properties",
        default = (313, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})

    ui_fold_recursive_toggle: IntVectorProperty(
        name = "Fold Button (Recursive)",
        description = "Key: Recursively Collapse block / Recursively Expand Block",
        default = (314, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    ui_fold_toggle: IntVectorProperty(
        name = "Fold Button",
        description = "Key: Collapse block / Expand Block",
        default = (1, 1050253722, 0, 1050253722, 257),
        size = 5, options = {"HIDDEN"})
    # */
    #|
    #|

class PrefsSize(PropertyGroup):
    __slots__ = ()

    # /* 0prefs_size
    widget: IntVectorProperty(
        name = "Size: Widget", size = 4, min = 1, max = 65535,
        default = (18, 2, 6, 1),
        description = "Widget height / I-Beam cursor width / Scrollbar width / Widget spacing",
        update = upd_F,
        options = set())
    title: IntVectorProperty(
        name = "Size: Title", size = 2, min = 1, max = 65535,
        default = (27, 22),
        description = "Editor and Menu Title Bar background height",
        update = upd_F,
        options = set())
    border: IntVectorProperty(
        name = "Size: Window Border", size = 4, min = 0, max = 63,
        default = (4, 3, 1, 1),
        description = "Window Border / Window Inner Border / Window Rim, Widget Rim",
        update = upd_F,
        options = set())
    dd_border: IntVectorProperty(
        name = "Size: Menu Border", size = 3, min = 0, max = 63,
        default = (1, 1, 1),
        description = "Menu Border / Inner Border / Rim size",
        update = upd_F,
        options = set())
    filter: IntVectorProperty(
        name = "Size: Filter", size = 4, min = 0, max = 65535,
        default = (200, 2, 2, 2),
        description = "Filter Height / Filter Border X / Filter Border Y / Select Box Gap",
        update = upd_F,
        options = set())
    tb: IntVectorProperty(
        name = "Size: Taskbar", size = 3, min = 1, max = 65535,
        default = (27, 300, 3),
        description = "Taskbar height / Offset / Underline",
        update = upd_F,
        options = set())
    win_shadow_offset: IntVectorProperty(
        name = "Window Shadow Offset", min = -65535, max = 65535, size = 4,
        default = (-10, 20, -23, 6),
        description = "Editor drop shadow offset (Left Right Bottom Top)",
        update = upd_F,
        options = set())
    dd_shadow_offset: IntVectorProperty(
        name = "Menu Shadow Offset", min = -65535, max = 65535, size = 4,
        default = (-6, 8, -11, 4),
        description = "Drop Down Menu drop shadow offset (Left Right Bottom Top)",
        update = upd_pref,
        options = set())
    shadow_softness: IntVectorProperty(
        name = "Shadow Softness", min = 0, max = 65535, size = 2,
        default = (57, 20),
        description = "Window and Dropdown menu shadow softness",
        update = upd_F,
        options = set())
    setting_list_border: IntVectorProperty(
        name = "Size: Settings List", size = 3, min = 0, max = 63,
        default = (8, 5, 1),
        description = "Settings List Outer Border / Settings List Inner Border / Area Hover Rim",
        update = upd_F,
        options = set())
    block: IntVectorProperty(
        name = "Size: Blocks", size = 10, min = 0, max = 63,
        default = (1, 2, 3, 3, 3, 15, 10, 1, 2, 2),
        description = "Blocks spacing / Blocks border Left / Right / Bottom / Top / Inner / Separator / Guideline / Header Top / Header Bottom",
        update = upd_F,
        options = set())
    button: IntVectorProperty(
        name = "Size: Buttons", size = 4, min = 1, max = 65535,
        default = (8, 2, 3, 256),
        description = "Color box grid / Button gap / Button separator / Color Panel Hue",
        update = upd_F,
        options = set())
    preview: IntVectorProperty(
        name = "Size: Preview", size = 2, min = 1, max = 65535,
        default = (8, 8),
        description = "Dash Line",
        update = upd_F,
        options = set())

    foreground: FloatVectorProperty(
        name = "Font Size Factor", size = 4, min = 0.0, max = 1.0,
        default = (0.56, 0.7, 0.6, 0.5),
        description = "Foreground Size Factor :  Title / Subtitle / Widget / Label",
        step = 1,
        update = upd_F,
        options = set())
    foreground_height: FloatVectorProperty(
        name = "Rows Height Factor", size = 4, min = 0.0, max = 2.0,
        default = (0.8, 0.8, 0.8, 0.77),
        description = "Rows Height factor :  Title / Subtitle / Widget / Label",
        step = 1,
        update = upd_F,
        options = set())
    widget_fac: FloatVectorProperty(
        name = "Widget Factor", size = 2, min = 0.1, max = 1.0,
        default = (0.8, 0.15),
        description = "Check Box size factor / Title Offset factor",
        step = 1,
        update = upd_F,
        options = set())
    # */

    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences.size'
        #|
    #|
    #|

class PrefsColor(PropertyGroup):
    __slots__ = ()

    # /* 0prefs_color
    win_title: FloatVectorProperty(
        name = "Color: Window Title Bar BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.018067, 0.018067, 0.018067, 0.97),
        description = "Editor Title Bar background color",
        options = set())
    win_title_inactive: FloatVectorProperty(
        name = "Color: Window Inactive Title Bar BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.028, 0.028, 0.028, 1.0),
        description = "Editor Inactive Title Bar background color",
        options = set())
    win: FloatVectorProperty(
        name = "Color: Window BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.036133, 0.036133, 0.036133, 1.0),
        description = "Editor background color",
        options = set())
    win_inactive: FloatVectorProperty(
        name = "Color: Window Inactive BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.036133, 0.036133, 0.036133, 0.9),
        description = "No function, spare.",
        options = set())
    win_rim: FloatVectorProperty(
        name = "Color: Window Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.05, 0.05, 0.05, 0.5),
        description = "Editor Rim color",
        options = set())
    win_shadow: FloatVectorProperty(
        name = "Color: Window Drop Shadow", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.012, 0.012, 0.012, 0.8),
        description = "Editor drop shadow color",
        options = set())
    dd_title: FloatVectorProperty(
        name = "Color: Menu Title Bar BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.018067, 0.018067, 0.018067, 1.0),
        description = "Menu Title Bar background color",
        options = set())
    dd: FloatVectorProperty(
        name = "Color: Menu BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.036133, 0.036133, 0.036133, 1.0),
        description = "Menu background color",
        options = set())
    dd_rim: FloatVectorProperty(
        name = "Color: Menu Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.036, 0.036, 0.036, 1.0),
        description = "Menu Rim color",
        options = set())
    dd_shadow: FloatVectorProperty(
        name = "Color: Menu Drop Shadow", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.012, 0.012, 0.012, 0.95),
        description = "Drop Down Menu drop shadow color",
        options = set())
    font_shadow: FloatVectorProperty(
        name = "Color: Font shadow", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0, 0.0, 0.0, 1.0),
        description = "Text drop shadow color. Font shadow method needs to be set to custom",
        update = upd_pref_font_render,
        options = {"HIDDEN"})
    area: FloatVectorProperty(
        name = "Color: Area BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.041504, 0.041504, 0.041504, 0.97),
        description = "Area background color",
        options = set())
    box_area_region: FloatVectorProperty(
        name = "Color: Area Region BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.032, 0.032, 0.032, 1.0),
        description = "Area Region background color",
        options = set())
    box_area_region_rim: FloatVectorProperty(
        name = "Color: Area Region Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0, 0.0, 0.0, 0.3),
        description = "Area Region Rim color",
        options = set())
    box_area_hover: FloatVectorProperty(
        name = "Color: Area Hover", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 0.005),
        description = "Area Hover color",
        options = set())
    box_area_hover_rim: FloatVectorProperty(
        name = "Color: Area Hover Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 0.01),
        description = "Area Hover Rim color",
        options = set())
    box_area_header_bg: FloatVectorProperty(
        name = "Color: Area Header BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.038, 0.038, 0.038, 1.0),
        description = "Area Header background color",
        options = set())
    block: FloatVectorProperty(
        name = "Color: Blocks BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.042, 0.042, 0.042, 1.0),
        description = "Blocks background color",
        options = set())
    block_even: FloatVectorProperty(
        name = "Color: Blocks BG Even", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.038, 0.038, 0.038, 1.0),
        description = "Even Block background color",
        options = set())
    block_title: FloatVectorProperty(
        name = "Color: Blocks Title", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.051, 0.051, 0.051, 1.0),
        description = "Blocks Title color",
        options = set())
    block_title_even: FloatVectorProperty(
        name = "Color: Blocks Title Even", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.051, 0.051, 0.051, 1.0),
        description = "Even Block Title color",
        options = set())
    block_calc_display: FloatVectorProperty(
        name = "Color: Blocks Calculator Display BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.038, 0.038, 0.038, 1.0),
        description = "Blocks Calculator Display background color",
        options = set())
    block_calc_display_fo: FloatVectorProperty(
        name = "Color: Blocks Calculator Display BG Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.042, 0.042, 0.042, 1.0),
        description = "Blocks Calculator Display focus background color",
        options = set())
    block_calc_button_bg: FloatVectorProperty(
        name = "Color: Blocks Calculator Button BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.044, 0.044, 0.044, 1.0),
        description = "Blocks Calculator Button background color",
        options = set())
    block_fo: FloatVectorProperty(
        name = "Color: Blocks Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.046, 0.046, 0.046, 1.0),
        description = "Blocks focus color",
        options = set())
    block_guideline0: FloatVectorProperty(
        name = "Color: Blocks Guideline 0", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.024, 0.024, 0.024, 1.0),
        description = "Blocks Guideline 0 color",
        options = set())
    block_guideline1: FloatVectorProperty(
        name = "Color: Blocks Guideline 1", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.06, 0.06, 0.06, 1.0),
        description = "Blocks Guideline 1 color",
        options = set())
    box_tb: FloatVectorProperty(
        name = "Color: Taskbar BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.018067, 0.018067, 0.018067, 0.99),
        description = "Taskbar background color",
        options = set())
    box_tb_multibar: FloatVectorProperty(
        name = "Color: Taskbar Underline", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.1, 0.3, 0.2, 1.0),
        description = "The appearance when there are more than 2 editors of the same type",
        options = set())
    box_text_active: FloatVectorProperty(
        name = "Color: Text Box Active BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.023, 0.023, 0.023, 1.0),
        description = "Active Text Box background color",
        options = set())
    box_text_fo: FloatVectorProperty(
        name = "Color: Text Box Focus BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.029, 0.029, 0.029, 1.0),
        description = "Text Box focus background color",
        options = set())
    box_text: FloatVectorProperty(
        name = "Color: Text Box BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.025, 0.025, 0.025, 1.0),
        description = "Text Box background color",
        options = set())
    box_text_rim: FloatVectorProperty(
        name = "Color: Text Box Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.023, 0.023, 0.023, 1.0),
        description = "Text Box Rim color",
        options = set())
    box_text_ignore: FloatVectorProperty(
        name = "Color: Text Box BG Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.025, 0.025, 0.025, 0.2),
        description = "Text Box background color (Inactive)",
        options = set())
    box_text_rim_ignore: FloatVectorProperty(
        name = "Color: Text Box Rim Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.025, 0.025, 0.025, 0.2),
        description = "Text Box Rim color (Inactive)",
        options = set())
    box_text_read: FloatVectorProperty(
        name = "Color: Read Only Text Box BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.044, 0.044, 0.044, 1.0),
        description = "Read Only Text Box background color",
        options = set())
    box_text_read_rim: FloatVectorProperty(
        name = "Color: Read Only Text Box Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.026, 0.026, 0.026, 1.0),
        description = "Read Only Text Box Rim color",
        options = set())
    box_color_rim: FloatVectorProperty(
        name = "Color: Color Box Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.023, 0.023, 0.023, 1.0),
        description = "Color Box Rim color",
        options = set())
    box_color_rim_fo: FloatVectorProperty(
        name = "Color: Color Box Rim Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0, 0.0, 0.0, 0.0),
        description = "Color Box Rim focus color",
        options = set())
    box_val: FloatVectorProperty(
        name = "Color: Value Box BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 1.0),
        description = "Value Box background color",
        options = set())
    box_val_rim: FloatVectorProperty(
        name = "Color: Value Box Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0987, 0.0987, 0.0987, 1.0),
        description = "Value Box Rim color",
        options = set())
    box_val_ignore: FloatVectorProperty(
        name = "Color: Value Box BG Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 0.2),
        description = "Value Box background color (Inactive)",
        options = set())
    box_val_rim_ignore: FloatVectorProperty(
        name = "Color: Value Box Rim Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 0.2),
        description = "Value Box Rim color (Inactive)",
        options = set())
    box_val_fo: FloatVectorProperty(
        name = "Color: Value Box Focus BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.12, 0.12, 0.12, 1.0),
        description = "Value Box focus background color",
        options = set())
    box_val_active: FloatVectorProperty(
        name = "Color: Value Box Active BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.017212, 0.017212, 0.017212, 1.0),
        description = "Active Value Box background color",
        options = set())
    box_val_bool: FloatVectorProperty(
        name = "Color: Check Box BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 1.0),
        description = "Check Box background color",
        options = set())
    box_val_bool_rim: FloatVectorProperty(
        name = "Color: Check Box Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.032, 0.032, 0.032, 1.0),
        description = "Check Box Rim color",
        options = set())
    box_val_bool_fo: FloatVectorProperty(
        name = "Color: Check Box Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.128907, 0.128907, 0.128907, 1.0),
        description = "Check Box focus color",
        options = set())
    box_val_bool_ignore: FloatVectorProperty(
        name = "Color: Check Box BG Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 0.3),
        description = "Check Box background color (Inactive)",
        options = set())
    box_val_bool_rim_ignore: FloatVectorProperty(
        name = "Color: Check Box Rim Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.032, 0.032, 0.032, 0.3),
        description = "Check Box Rim color (Inactive)",
        options = set())
    box_button: FloatVectorProperty(
        name = "Color: Button BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 1.0),
        description = "Button background color",
        options = set())
    box_button_rim: FloatVectorProperty(
        name = "Color: Button Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.13, 0.13, 0.13, 1.0),
        description = "Button Rim color",
        options = set())
    box_button_ignore: FloatVectorProperty(
        name = "Color: Button BG Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 0.25),
        description = "Button background color (Inactive)",
        options = set())
    box_button_rim_ignore: FloatVectorProperty(
        name = "Color: Button Rim Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.13, 0.13, 0.13, 0.25),
        description = "Button Rim color (Inactive)",
        options = set())
    box_button_fo: FloatVectorProperty(
        name = "Color: Button Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.1, 0.1, 0.1, 1.0),
        description = "Button focus color",
        options = set())
    box_button_rim_fo: FloatVectorProperty(
        name = "Color: Button Rim Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.14, 0.14, 0.14, 1.0),
        description = "Button Rim focus color",
        options = set())
    box_button_active: FloatVectorProperty(
        name = "Color: Button Active BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.02, 0.025, 0.03, 1.0),
        description = "Active Button background color",
        options = set())
    box_button_rim_active: FloatVectorProperty(
        name = "Color: Button Rim Active", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.09, 0.09, 0.09, 1.0),
        description = "Active Button Rim color",
        options = set())
    box_buttonoff: FloatVectorProperty(
        name = "Color: Button Switch Off BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.08545, 0.08545, 0.08545, 1.0),
        description = "Button Switch background color when button value is False",
        options = set())
    box_buttonoff_rim: FloatVectorProperty(
        name = "Color: Button Switch Off Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.13, 0.13, 0.13, 1.0),
        description = "Button Switch Rim color when button value is False",
        options = set())
    box_buttonoff_fo: FloatVectorProperty(
        name = "Color: Button Switch Off Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.1, 0.1, 0.1, 1.0),
        description = "Button Switch focus color when button value is False",
        options = set())
    box_buttonoff_rim_fo: FloatVectorProperty(
        name = "Color: Button Switch Off Rim Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.14, 0.14, 0.14, 1.0),
        description = "Button Switch Rim focus color when button value is False",
        options = set())
    box_buttonon: FloatVectorProperty(
        name = "Color: Button Switch On BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.02, 0.08, 0.063, 1.0),
        description = "Button Switch background color when button value is True",
        options = set())
    box_buttonon_rim: FloatVectorProperty(
        name = "Color: Button Switch On Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.13, 0.13, 0.13, 1.0),
        description = "Button Switch Rim color when button value is True",
        options = set())
    box_buttonon_fo: FloatVectorProperty(
        name = "Color: Button Switch On Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0225, 0.09, 0.070875, 1.0),
        description = "Button Switch focus color when button value is True",
        options = set())
    box_buttonon_rim_fo: FloatVectorProperty(
        name = "Color: Button Switch On Rim Focus", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.14, 0.14, 0.14, 1.0),
        description = "Button Switch Rim focus color when button value is True",
        options = set())
    box_buttonon_ignore: FloatVectorProperty(
        name = "Color: Button Switch On BG Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.02, 0.08, 0.063, 0.3),
        description = "Button Switch background color when button value is True (Inactive)",
        options = set())
    box_filter: FloatVectorProperty(
        name = "Color: Filter Area BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.03, 0.03, 0.03, 1.0),
        description = "Filter Area background color",
        options = set())
    box_filter_rim: FloatVectorProperty(
        name = "Color: Filter Area Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.026, 0.026, 0.026, 1.0),
        description = "Filter Area Rim color",
        options = set())
    box_filter_num_modal: FloatVectorProperty(
        name = "Color: Filter Hover Element BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.034, 0.034, 0.034, 1.0),
        description = "Sorting modal active element background color",
        options = set())
    box_filter_num_modal_rim: FloatVectorProperty(
        name = "Color: Filter Hover Element Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.04, 0.04, 0.04, 1.0),
        description = "Sorting modal active element rim color",
        options = set())
    box_filter_region: FloatVectorProperty(
        name = "Color: Filter Region BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.03, 0.03, 0.03, 1.0),
        description = "Filter Region background color, modifier list button region",
        options = set())
    box_filter_region_rim: FloatVectorProperty(
        name = "Color: Filter Region Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.03, 0.03, 0.03, 1.0),
        description = "Filter Region Rim color, modifier list button region",
        options = set())
    box_filter_active_bg: FloatVectorProperty(
        name = "Color: Filter Area Active Element BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0275, 0.055, 0.055, 1.0),
        description = "Filter Area Active Element background color",
        options = set())
    box_filter_select_bg: FloatVectorProperty(
        name = "Color: Filter Area Selected Element BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0385, 0.0385, 0.0385, 1.0),
        description = "Filter Area Selected Element background color",
        options = set())
    box_filter_hover_bg: FloatVectorProperty(
        name = "Color: Filter Area Hover BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 0.005),
        description = "Filter Area Hover background color",
        options = set())
    box_cursor_beam: FloatVectorProperty(
        name = "Color: I Beam Cursor", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.167, 0.39698, 1.0, 1.0),
        description = "I-Beam cursor color",
        options = set())
    box_cursor_beam_off: FloatVectorProperty(
        name = "Color: I Beam Cursor Off", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.167, 0.39698, 1.0, 0.2),
        description = "I-Beam cursor color off",
        options = set())
    box_text_selection: FloatVectorProperty(
        name = "Color: Text Selection", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.058594, 0.169922, 0.453125, 1.0),
        description = "Text Selection background Color in Text Box",
        options = set())
    box_text_selection_off: FloatVectorProperty(
        name = "Color: Text Selection Off", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.058594, 0.169922, 0.453125, 0.3),
        description = "Text Selection Off background Color in Text Box",
        options = set())
    box_scrollbar_bg: FloatVectorProperty(
        name = "Color: Filter Scrollbar BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.025, 0.025, 0.025, 1.0),
        description = "Filter Scrollbar background color",
        options = set())
    box_scrollbar: FloatVectorProperty(
        name = "Color: Filter Scrollbar", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.035, 0.035, 0.035, 1.0),
        description = "Filter Scrollbar color",
        options = set())
    box_block_scrollbar_bg: FloatVectorProperty(
        name = "Color: Blocks Scrollbar BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.025, 0.025, 0.025, 1.0),
        description = "Blocks Scrollbar background color",
        options = set())
    box_block_scrollbar: FloatVectorProperty(
        name = "Color: Blocks Scrollbar", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.035, 0.035, 0.035, 1.0),
        description = "Blocks Scrollbar color",
        options = set())
    box_setting_list_bg: FloatVectorProperty(
        name = "Color: Settings List BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.038, 0.038, 0.038, 1.0),
        description = "Settings List background color",
        options = set())
    box_setting_list_active: FloatVectorProperty(
        name = "Color: Settings List Active BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.05, 0.05, 0.05, 1.0),
        description = "Settings List active background color",
        options = set())
    box_setting_list_active_rim: FloatVectorProperty(
        name = "Color: Settings List Active Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 0.05),
        description = "Settings List active rim color",
        options = set())
    box_blfbutton_text_hover: FloatVectorProperty(
        name = "Color: Button Text Hover", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 0.01),
        description = "Text Button hover color",
        options = set())
    box_blfbutton_text_hover_rim: FloatVectorProperty(
        name = "Color: Button Text Hover Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 0.04),
        description = "Text Button hover rim color",
        options = set())
    box_hue_bg: FloatVectorProperty(
        name = "Color: Hue BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.02, 0.02, 0.02, 1.0),
        description = "Color Panel Hue background color",
        options = set())
    box_selectbox_bg: FloatVectorProperty(
        name = "Color: Select Box BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.275, 0.55, 0.55, 0.02),
        description = "Select Box background color",
        options = set())
    box_selectbox_rim: FloatVectorProperty(
        name = "Color: Select Box Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.5, 0.8, 0.8, 1.0),
        description = "Select Box Rim color",
        options = set())
    box_selectbox_gap: FloatVectorProperty(
        name = "Color: Select Box Gap", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.275, 0.55, 0.55, 0.02),
        description = "Select Box Gap color",
        options = set())
    box_selectbox_subtract_bg: FloatVectorProperty(
        name = "Color: Select Box Subtract BG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.55, 0.275, 0.275, 0.02),
        description = "Select Box Subtract background color",
        options = set())
    box_selectbox_subtract_rim: FloatVectorProperty(
        name = "Color: Select Box Subtract Rim", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.8, 0.3, 0.3, 1.0),
        description = "Select Box Subtract Rim color",
        options = set())
    box_selectbox_subtract_gap: FloatVectorProperty(
        name = "Color: Select Box Subtract Gap", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.55, 0.275, 0.275, 0.02),
        description = "Select Box Subtract Gap color",
        options = set())
    preview_3d_dash: FloatVectorProperty(
        name = "Color: Preview Dash Line", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 1.0),
        description = "3D viewport creen space dash line",
        options = set())
    preview_3d_dash2: FloatVectorProperty(
        name = "Color: Preview Dash Line 2", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0, 0.0, 0.0, 1.0),
        description = "3D viewport creen space dash line 2",
        options = set())
    preview_3d_arc: FloatVectorProperty(
        name = "Color: Preview Arc", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 1.0),
        description = "3D viewport arc color",
        options = set())

    win_title_fg: FloatVectorProperty(
        name = "Color: Window Title Bar FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.6, 0.6, 0.6, 1.0),
        description = "Editor Title Bar foreground color",
        options = {"HIDDEN"})
    dd_title_fg: FloatVectorProperty(
        name = "Color: Menu Title Bar FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.5, 0.5, 0.5, 1.0),
        description = "Menu Title Bar foreground color",
        options = {"HIDDEN"})
    box_text_fg: FloatVectorProperty(
        name = "Color: Text Box FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.65, 0.65, 0.65, 1.0),
        description = "Text Box foreground color",
        options = {"HIDDEN"})
    box_text_fg_ignore: FloatVectorProperty(
        name = "Color: Text Box Inactive FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.7, 0.7, 0.7, 0.15),
        description = "Text Box ignore foreground color",
        options = {"HIDDEN"})
    box_text_read_fg: FloatVectorProperty(
        name = "Color: Read Only Text Box FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.65, 0.65, 0.65, 1.0),
        description = "Read Only Text Box foreground color",
        options = {"HIDDEN"})
    box_val_fg: FloatVectorProperty(
        name = "Color: Value Box FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.8, 0.8, 0.8, 1.0),
        description = "Value Box foreground color",
        options = {"HIDDEN"})
    box_val_fg_ignore: FloatVectorProperty(
        name = "Color: Value Box FG Disable", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.8, 0.8, 0.8, 0.15),
        description = "Value Box disable foreground color",
        options = {"HIDDEN"})
    box_val_fg_error: FloatVectorProperty(
        name = "Color: Value Box FG Error", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.8, 0.05, 0.05, 1.0),
        description = "Value Box error foreground color",
        options = {"HIDDEN"})
    box_filter_fg: FloatVectorProperty(
        name = "Color: Filter FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.6, 0.6, 0.6, 1.0),
        description = "Filter foreground color",
        options = {"HIDDEN"})
    box_filter_fg_info: FloatVectorProperty(
        name = "Color: Filter Info FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.4, 0.4, 0.4, 1.0),
        description = "Filter Info foreground color",
        options = {"HIDDEN"})
    box_filter_fg_label: FloatVectorProperty(
        name = "Color: Filter Label FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.3, 0.3, 0.3, 1.0),
        description = "Filter Label foreground color, modifier list number",
        options = {"HIDDEN"})
    box_filter_fg_apply: FloatVectorProperty(
        name = "Color: Filter Label Apply FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.25, 0.8, 0.95, 1.0),
        description = "Filter Label Apply foreground color",
        options = {"HIDDEN"})
    box_filter_fg_del: FloatVectorProperty(
        name = "Color: Filter Label Delete FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.95, 0.17, 0.17, 1.0),
        description = "Filter Label Delete foreground color",
        options = {"HIDDEN"})
    box_setting_list_fg: FloatVectorProperty(
        name = "Color: Settings List FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.6, 0.6, 0.6, 1.0),
        description = "Settings List foreground color",
        options = {"HIDDEN"})
    block_fg: FloatVectorProperty(
        name = "Color: Blocks FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.7, 0.7, 0.7, 1.0),
        description = "Blocks foreground color",
        options = {"HIDDEN"})
    block_fg_ignore: FloatVectorProperty(
        name = "Color: Blocks FG Inactive", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.7, 0.7, 0.7, 0.15),
        description = "Blocks foreground color (Inactive)",
        options = {"HIDDEN"})
    block_fg_info: FloatVectorProperty(
        name = "Color: Blocks Info FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.45, 0.45, 0.45, 1.0),
        description = "Blocks Info foreground color",
        options = {"HIDDEN"})
    box_button_fg: FloatVectorProperty(
        name = "Color: Button FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.8, 0.8, 0.8, 1.0),
        description = "Button foreground color",
        options = {"HIDDEN"})
    box_button_fg_ignore: FloatVectorProperty(
        name = "Color: Button FG Disable", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.8, 0.8, 0.8, 0.15),
        description = "Button disable foreground color",
        options = {"HIDDEN"})
    box_button_fg_info: FloatVectorProperty(
        name = "Color: Button Info FG", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.45, 0.45, 0.45, 1.0),
        description = "Button Info foreground color",
        options = {"HIDDEN"})

    win_title_hover: FloatVectorProperty(
        name = "Color: Window Title Button Hover", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (1.0, 1.0, 1.0, 0.01),
        description = "Editor Title Bar hover color",
        options = set())
    win_title_hover_red: FloatVectorProperty(
        name = "Color: Window Title Close Button Hover", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.34, 0.017, 0.036, 1.0),
        description = "Editor Title Bar Close Button hover color",
        options = set())
    win_title_hover_hold: FloatVectorProperty(
        name = "Color: Window Title Button Active", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.0, 0.0, 0.0, 0.4),
        description = "Editor Title Bar hover color when pressing the key",
        options = set())
    win_title_hover_hold_red: FloatVectorProperty(
        name = "Color: Window Title Close Button Active", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, step = 1,
        default = (0.36, 0.018, 0.03852, 0.6),
        description = "Editor Title Bar Close Button hover color when pressing the key",
        options = set())
    # */

    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences.color'
        #|
    #|
    #|

class PrefsTemp(PropertyGroup):
    __slots__ = ()

    # /* 0prefs_temp
    pos: IntVectorProperty(
        name = "Active Window Position", size = 2, min = -65535, max = 65535,
        description = "The position of the upper left corner of the active editor",
        update = upd_win_active,
        options = set())
    size: IntVectorProperty(
        name = "Active Window Size", size = 2, min = 0, max = 65535,
        description = "The size of the active editor",
        update = upd_win_active,
        options = set())
    canvas: IntVectorProperty(
        name = "Active Window Canvas", size = 2, min = -65535, max = 65535,
        description = "The canvas relative position of the active editor",
        update = upd_win_active,
        options = set())
    # */

    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences.temp'
        #|
    #|
    #|


class Prefs(bpy.types.AddonPreferences):
    __slots__ = ()
    bl_idname = __package__

    refresh: BoolProperty(
        name = "", default = True, update = upd_refresh,
        options = set())
    is_first_use: BoolProperty(
        name = "First Use", default = True,
        options = set())
    de: IntVectorProperty(
        name = "Debug int", min = -65535, max = 65535, size = 4, update = upd_refresh,
        options = set())

    keymaps: PointerProperty(type = PrefsKey, name = "Window Initial", options = {"HIDDEN"})

    # /* 0prefs
    npanel_reg_settings: BoolProperty(
        name = "Register N-Panel Tabs",
        description = "Show all tabs in N-Panel",
        default = True,
        update = upd_pref,
        options = set())
    sys_auto_off: BoolProperty(
        name = "Auto off System",  default = True,
        description = "Automatically close Addon system when process is empty",
        update = upd_pref,
        options = set())
    show_length_unit: BoolProperty(
        name = "Show Length Unit",  default = True,
        description = "Show length unit in Value Box. Only affects new windows",
        update = upd_pref_unit,
        options = set())
    lock_win_size: BoolProperty(
        name = "Lock Window Size",
        description = "Do not allow window resizing via mouse events",
        update = upd_pref,
        options = set())
    lock_list_size: BoolProperty(
        name = "Lock UI List Size",
        description = "Do not allow resizing of UI list via mouse events",
        update = upd_pref,
        options = set())
    th_drag: IntProperty(
        name = "Drag Threshold", min = 0, max = 63, default = 3,
        description = "The drag distance (X and Y) that triggers the drag type keymap",
        update = upd_pref,
        options = set())
    th_double_click: IntProperty(
        name = "Double Click Threshold", min = 0, max = 63, default = 3,
        description = "If you need to trigger a Double Press or Double Release type of keymap, the click distance (X and Y) must be less than or equal to this value",
        update = upd_pref,
        options = set())
    win_check_overlap: BoolProperty(
        name = "Check Initial Overlap",  default = True,
        description = "If overlapping an existing editor (upper left), offset X and Y when calling the new editor",
        update = upd_pref,
        options = set())
    win_overlap_offset: IntVectorProperty(
        name = "Window Overlap Offset", min = -65535, max = 65535, size = 2,
        default = (14, -14),
        description = "Used when Check Initial Overlap is enabled",
        update = upd_pref,
        subtype = "TRANSLATION",
        options = set())
    filter_match_case: BoolProperty(
        name = "Filter Match Case",
        description = "Default Value. Enable Match Case option when calling filter menu",
        update = upd_pref,
        options = set())
    filter_match_whole_word: BoolProperty(
        name = "Filter Match Whole Word",
        description = "Default Value. Enable Match Whole Word option when calling filter menu",
        update = upd_pref,
        options = set())
    filter_match_end: IntProperty(
        name = "Filter Match End", min = 0, max = 2,
        description = "Default Value. Enable Match End option when calling filter menu.\n0: Disable\n1: Match End of Left\n2: Match End of Right",
        update = upd_pref,
        options = set())
    filter_autopan_active: BoolProperty(
        name = "Filter Auto Pan Active",
        description = "When you change the active index via keymap, if the active index is not in the visible range, the canvas will be automatically panned",
        default = True,
        update = upd_pref,
        options = set())
    filter_adaptive_selection: BoolProperty(
        name = "Filter Adaptive Selection",
        description = "Extend existing selection when the cursor X position is greater than starting position, otherwise subtract the selection",
        default = True,
        update = upd_pref,
        options = set())
    filter_delete_behavior: EnumProperty(
        name = "Filter Delete Behavior",
        description = "Filter item Remove/Apply behavior",
        items = (
            ("ACTIVE", "Active", ""),
            ("SELECTION", "Selection", "")),
        default = "SELECTION",
        update = upd_pref,
        options = set())
    cursor_beam_time: FloatProperty(
        name = "Text Cursor Flash Time",
        default = 0.4,
        description = "How long does the text cursor blink once. Unit: Seconds / Half Cycle",
        step = 1,
        update = upd_pref,
        options = set())
    use_select_all: BoolProperty(
        name = "Text Box Select All",
        default = True,
        description = "Select all text when clicking on text box",
        update = upd_pref,
        options = set())
    pan_invert: BoolProperty(
        name = "Pan Invert",
        description = "Flip the Pan direction",
        update = upd_pref,
        options = set())
    scroll_distance: IntProperty(
        name = "Scroll Speed", min = 1, max = 65535,
        description = "The distance the canvas moves when the Scrollbar scroll event is triggered",
        default = 20,
        subtype = "PIXEL",
        update = upd_pref,
        options = set())
    valbox_drag_fac_int: FloatProperty(
        name = "Int Value Box Drag Speed", min = 0.0001, max = 65535.0,
        description = "Integer Value Box drag factor",
        default = 0.1,
        step = 1,
        update = upd_pref,
        options = set())
    valbox_drag_fac_float: FloatProperty(
        name = "Float Value Box Drag Speed", min = 0.0001, max = 65535.0,
        description = "Float Value Box drag factor",
        default = 0.1,
        step = 1,
        update = upd_pref,
        options = set())
    button_repeat_time: FloatProperty(
        name = "Button Repeat Time", min = 0.00001, max = 65535.0,
        description = "The hold time (in seconds) for the repeat trigger button",
        default = 0.3,
        step = 1,
        update = upd_pref,
        options = set())
    button_repeat_interval: FloatProperty(
        name = "Button Repeat Interval", min = 0.00001, max = 65535.0,
        description = "The repeat trigger interval in seconds for the repeat trigger button.\nUsed when pressing button for more than x seconds (Button Repeat Time)",
        default = 0.03,
        step = 1,
        update = upd_pref,
        options = set())
    use_py_exp: BoolProperty(
        name = "Value Box: Use Python Expression",
        description = "Use Python Expression in Value Box",
        default = True,
        update = upd_pref,
        options = set())
    show_rm_keymap: BoolProperty(
        name = "Show Context Menu Keymaps",
        description = "Show Keymap on Context Menu item",
        default = False,
        update = upd_pref,
        options = set())
    adaptive_enum_input: BoolProperty(
        name = "Adaptive Drop Down Menu Input",
        description = "When the text input does not exactly match the list item, it will use the first item in the filter",
        default = True,
        update = upd_pref,
        options = set())
    adaptive_win_resize: BoolProperty(
        name = "Adaptive Window Resize",
        description = "Change window area size after resize the window",
        default = True,
        update = upd_pref,
        options = set())
    undo_steps_local: IntProperty(
        name = "Local Undo Steps", min = 1, default = 1023,
        description = "Number of undo steps available",
        update = upd_pref,
        options = set())
    format_float: EnumProperty(
        name = "Display Format: Float",
        description = "The floating point value display format of the value box.\nRestart required",
        items = (
            ("THOUSAND_SEPARATOR", "Thousand Separator", ""),
            ("THOUSAND_SEPARATOR_FULL", "Thousand Separator Full", ""),
            ("NO_SEPARATOR_LEFT", "No Separator Align Left", "")),
        default = "THOUSAND_SEPARATOR",
        update = upd_pref,
        options = set())
    format_hex: EnumProperty(
        name = "Display Format: Color Hex",
        description = "The Hex value display format of the color",
        items = (
            ("UPPERCASE_SEPARATOR", "Separator Uppercase", ""),
            ("LOWERCASE_SEPARATOR", "Separator Lowercase", ""),
            ("UPPERCASE", "Uppercase", ""),
            ("LOWERCASE", "Lowercase", "")),
        default = "UPPERCASE_SEPARATOR",
        update = upd_pref,
        options = set())
    anim_filter: BoolProperty(
        name = "Animation: Filter",
        description = "Use Animation on Filter",
        default = True,
        update = upd_pref,
        options = set())
    animtime_filter: FloatProperty(
        name = "Animation Time: Filter", min = 0.000001, max = 1.0,
        description = "How many seconds does the animation take to complete",
        default = 0.1,
        update = upd_pref,
        options = set())
    cursor_picker: EnumProperty(
        name = "Cursor Object Picker",
        description = "Object Picker cursor icon",
        items = SharedEnumItems.window_cursor_items,
        default = "EYEDROPPER",
        update = upd_pref,
        options = set())
    cursor_pan: EnumProperty(
        name = "Cursor Pan",
        description = "Pan cursor icon",
        items = SharedEnumItems.window_cursor_items,
        default = "HAND",
        update = upd_pref,
        options = set())
    md_lib_filepath: StringProperty(
        name = "Modifier Library Path",
        description = "Modifier and Geometry Node Library file path",
        default = f'directories = (# Folder, Recursive, Marked assets only\n    ("A:/YourDirectory 1", True, False),\n    ("B:/YourDirectory 2", False, False),\n)',
        update = upd_pref,
        options = set())
    md_lib_filter: StringProperty(
        name = "Modifier Library Filter",
        description = "Python eval filter function in Add Modifier list\nExample:\n    ob.name[-1].isupper()",
        default = "",
        update = upd_pref,
        options = set())
    md_lib_method: EnumProperty(
        name = "Geometry Node Library Append Method",
        description = "Default Value.\nUsed for Add Modifier Menu",
        items = (
            ("APPEND", "Append", ""),
            ("REUSE", "Append Reuse", "Reuse data when there are no name conflicts"),
            ("LINK", "Link", "")),
        default = "REUSE",
        update = upd_pref,
        options = set())
    md_lib_use_essentials: BoolProperty(
        name = "Geometry Node Library use built-in libraries",
        description = "Use blender built-in libraries, need to refresh the library manually",
        default = True,
        update = upd_pref,
        options = set())
    preview_scale: FloatProperty(
        name = "Preview Scale", min = 1.0, max = 8.0,
        default = 1.0,
        description = "Preview Panel Size",
        step = 1,
        update = upd_pref,
        options = set())
    preview_showname: BoolProperty(
        name = "Preview Show Name",
        description = "Show name in Preview Panel",
        default = True,
        update = upd_pref,
        options = set())
    prop_image_dd_showicon: BoolProperty(
        name = "UI Image Menu Show Icon",
        description = "Show small preview icon on drop down menu",
        default = True,
        update = upd_pref,
        options = set())
    fontpath_method: EnumProperty(
        name = "Font Path Method",
        description = "UI font path method. Blender restart required",
        items = (
            ("DEFAULT", "Default", ""),
            ("BLENDER", "Blender", ""),
            ("CUSTOM", "Custom", "")),
        default = "DEFAULT",
        update = upd_pref,
        options = set())
    fontpath_ui: StringProperty(
        name = "Custom Font Path Interface",
        description = "Used when Font Path Method is set to Custom. Blender restart required",
        default = "",
        subtype = "FILE_PATH",
        update = upd_pref,
        options = set())
    fontpath_ui_mono: StringProperty(
        name = "Custom Font Path Monospaced",
        description = "Used when Font Path Method is set to Custom. Blender restart required",
        default = "",
        subtype = "FILE_PATH",
        update = upd_pref,
        options = set())
    is_open_driver_editor: BoolProperty(
        name = "Auto Open Driver Editor",
        description = "Open the driver editor when adding a driver",
        default = True,
        update = upd_pref,
        options = set())
    blocklist_column_len: IntProperty(
        name = "Panel List Colume Length", min = 1, max = 63, default = 3,
        description = "Default value for the number of items displayed in the inventory panel",
        update = upd_pref,
        options = set())
    font_shadow_method: EnumProperty(
        name = "Text Rendering: Shadow Method",
        description = "Font shadow rendering method",
        items = (
            ("NONE", "None", "Disable"),
            ("DEFAULT", "Default", "Default drop shadow"),
            ("CUSTOM", "Custom", "User defined")),
        default = "DEFAULT",
        update = upd_pref_font_render,
        options = set())
    font_shadow_hardness: IntProperty(
        name = "Text Rendering: Shadow hardness", min = 0, max = 3,
        description = "Font shadow hardness. Font shadow method needs to be set to custom",
        update = upd_pref_font_render,
        options = set())
    font_shadow_offset: IntVectorProperty(
        name = "Text Rendering: Shadow Offset", min = -65535, max = 65535, size = 2,
        default = (0, 0),
        description = "Font shadow offset (pixels). Font shadow method needs to be set to custom",
        update = upd_pref_font_render,
        subtype = "TRANSLATION",
        options = set())

    color: PointerProperty(type = PrefsColor, name = "Color", options = set())
    size: PointerProperty(type = PrefsSize, name = "Size", options = set())
    ModifierEditor: PointerProperty(type = PrefsModifierEditor, name = "Modifier Editor", options = set())
    DriverEditor: PointerProperty(type = PrefsDriverEditor, name = "Driver Editor", options = set())
    SettingEditor: PointerProperty(type = PrefsSettingEditor, name = "Settings Editor", options = set())
    MeshEditor: PointerProperty(type = PrefsMeshEditor, name = "Mesh Editor", options = set())
    # */
    temp: PointerProperty(type = PrefsTemp, name = "Temporary Data", options = set())
    calc_exp: StringProperty(
        name = "Calculator Expression",
        description = "Calculator expressions",
        default = STR_CALC_EXP_DEFAULT,
        options = set())

































































































    def __repr__(self):
        return f'bpy.context.preferences.addons["{__package__}"].preferences'
        #|
    #|
    #|

classes = (
    PrefsModifierEditor,
    PrefsDriverEditor,
    PrefsSettingEditor,
    PrefsMeshEditor,
    PrefsKey,
    PrefsSize,
    PrefsColor,
    PrefsTemp,
    Prefs)


## _file_ ##
def late_import():
    #|
    from . util.com import N


    U_UPD_SIZE = N
    U_UPD_WIN_ACTIVE = N
    U_UPD_PREF = N

    OVERRIDE_SUBTYPES = {
        PrefsSize: {
            'title': ('Window', 'Menu'),
            'border': ('Outer', 'Inner', 'Rim', 'Widget Rim'),
            'dd_border': ('Outer', 'Inner', 'Rim'),
            'filter': ('Height', 'Border X', 'Border Y', 'Select Box Gap'),
            'widget': ('Height', 'Beam Cursor', 'Scrollbar', 'Spacing'),
            'tb': ('Height', 'Offset', 'Underline'),
            'win_shadow_offset': ('L', 'R', 'B', 'T'),
            'dd_shadow_offset': ('L', 'R', 'B', 'T'),
            'shadow_softness': ('Window', 'Menu'),
            'setting_list_border': ('Outer', 'Inner', 'Hover Rim'),
            'block': ('Spacing', 'Border L', 'Border R', 'Border B', 'Border T', 'Border Inner', 'Separator', 'Guideline', 'Header T', 'Header B'),
            'button': ('Color Grid', 'Gap', 'Separator', 'Hue'),
            'foreground': ('Title', 'Subtitle', 'Widget', 'Label'),
            'foreground_height': ('Title', 'Subtitle', 'Widget', 'Label'),
            'widget_fac': ('Check Box', 'Title Offset'),
            'preview': ('Dash', ''),
        }
    }

    globals().update(locals())
    #|