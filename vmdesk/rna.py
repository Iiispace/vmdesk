
def r_props_by_rnas(rnas):
    class RnaProps:
        __slots__ = tuple(e  for e in rnas)

        def __init__(self):
            for k, e in rnas.items():
                if hasattr(e, "type"):
                    if e.type == "RNABUTTON": continue
                    if hasattr(e, "is_array") and e.is_array:
                        setattr(self, k, list(e.default_array))
                    else:
                        setattr(self, k, e.default)

    return RnaProps()
    #|

## _file_ ##
def late_import():
    #|
    from .  import VMD

    # <<< 1mp (VMD.util.types
    types = VMD.util.types
    RnaString = types.RnaString
    RnaBool = types.RnaBool
    RnaEnum = types.RnaEnum
    RnaButton = types.RnaButton
    EnumItem = types.EnumItem
    Dictlist = types.Dictlist
    # >>>

    ENUMITEMS_copy_operation = Dictlist((
        EnumItem("COPY", "Copy", ""),
        EnumItem("LINK", "Link", ""),
        EnumItem("DEEPLINK", "Deep Link", "")))
    ENUMITEMS_copy_operation.default = "COPY"

    ENUMITEMS_local_space = Dictlist((
        EnumItem("LOCAL", "Local", ""),
        EnumItem("GLOBAL", "Global", "")))
    ENUMITEMS_local_space.default = "GLOBAL"

    ENUMITEMS_sort_order = Dictlist((
        EnumItem("ALPHABET", "Alphabet", ""),
        EnumItem("INVERT", "Invert", "")))
    ENUMITEMS_sort_order.default = set()

    RNA_md_use_keyframe = RnaBool("md_use_keyframe", name="Keyframe")
    RNA_md_use_driver = RnaBool("md_use_driver", name="Driver")
    RNA_md_copy = RnaButton("md_copy", "Copy", "", "Copy")
    RNA_md_move = RnaButton("md_move", "Move", "", "Move")
    RNA_md_link = RnaButton("md_link", "Link", "", "Link")
    RNA_md_deeplink = RnaButton("md_deeplink", "Deep Link", "", "Deep Link")
    RNA_md_copy_operation = RnaEnum("md_copy_operation",
        ENUMITEMS_copy_operation,
        name="Operation", is_never_none=False)
    RNA_md_use_mouse_index = RnaBool("md_use_mouse_index", name="Mouse Index")
    RNA_md_use_selection = RnaBool("md_use_selection", name="Selection")
    RNA_md_use_code = RnaBool("md_use_code", name="Override Code")
    RNA_ob_use_self = RnaBool("ob_use_self", name="Self")

    RNA_run = RnaButton("run", "Run", "", "Run")
    RNA_cancel = RnaButton("cancel", "Cancel", "", "Cancel")
    RNA_confirm = RnaButton("confirm", "Confirm", "", "Confirm")
    RNA_importfile = RnaButton("importfile", "Import File", "", "Import File")


    RNA_active_object = RnaButton("active_object",
        name = "Active Object",
        button_text = "",
        description = "Set active object.")
    RNA_active_object_sync = RnaButton("active_object_sync",
        name = "Active Object Sync",
        button_text = "",
        description = "Sync active object.")
    RNA_active_modifier = RnaButton("active_modifier",
        name = "Active Modifier",
        button_text = "",
        description = "Set active modifier.")
    RNA_active_modifier_sync = RnaButton("active_modifier_sync",
        name = "Active Modifier Sync",
        button_text = "",
        description = "Sync active modifier.")
    RNA_new_modifier = RnaButton("new_modiifer",
        name = "New Modifier",
        button_text = "",
        description = "Add a modifier.")
    RNA_remove_modifier = RnaButton("remove_modifier",
        name = "Remove Modifier",
        button_text = "",
        description = "Remove active modifier.")
    RNA_active_item = RnaButton("active_item",
        name = "Active Item",
        button_text = "",
        description = "Set active Item.")
    RNA_new_item = RnaButton("new_item",
        name = "New Item",
        button_text = "",
        description = "Add a item.")
    RNA_remove_item = RnaButton("remove_item",
        name = "Remove Item",
        button_text = "",
        description = "Remove active item.")
    RNA_button_keyframe = RnaButton("button_keyframe",
        name = "Button Keyframe",
        button_text = "",
        description = "Keyframe Button.")


    RNA_local_space = RnaEnum("local_space",
        ENUMITEMS_local_space,
        name = "Space",
        is_never_none = False)
    RNA_sort_order = RnaEnum("sort_order",
        ENUMITEMS_sort_order,
        name = "Sort Order",
        default = set(),
        is_never_none = True,
        is_enum_flag = True)

    RNA_refresh = RnaButton("refresh",
        name = "Refresh",
        button_text = "",
        description = "Refresh")

    RNA_copy_to_clipboard = RnaButton("copy_to_clipboard",
        name = "Copy to Clipboard",
        button_text = "Copy to Clipboard",
        description = "")
    RNA_save_as = RnaButton("save_as",
        name = "Save as",
        button_text = "Save as",
        description = "")

    globals().update(locals())
    #|