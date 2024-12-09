











import bpy, blf, math

from .  import VMD

blfDimen = blf.dimensions
escape_identifier = bpy.utils.escape_identifier
floor = math.floor
degrees = math.degrees

# <<< 1mp (VMD
m = VMD.m
# >>>

# <<< 1mp (VMD.win
win = VMD.win
Window = win.Window
StructGlobalUndo = win.StructGlobalUndo
# >>>

# <<< 1mp (VMD.area
area = VMD.area
AreaBlockTab = area.AreaBlockTab
AreaBlockSimple = area.AreaBlockSimple
# >>>

Object = bpy.types.Object

class DriverEditor(Window, StructGlobalUndo):
    __slots__ = (
        'active_object',
        'active_var',
        'active_var_name',
        'active_tab',
        'props',
        'bars',
        'area_head',
        'area_info',
        'area_tab',
        'area_var',
        'area_vars',
        'set_info',
        'temp')

    name = 'Driver Editor'

    def init(self, boxes, blfs):
        bars = {}
        self.bars = bars
        self.temp = {}
        self.active_object = None
        self.active_var = None
        self.active_var_name = ""

        # /* 0ed_DriverEditor_init
        PP = self.P_editor
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_full_h = D_SIZE['widget_full_h']

        LL = self.box_win.L + border_outer
        TT = self.box_win.title_B - border_outer
        RR = LL + round(3.0 * D_SIZE['widget_width'] * PP.area_widthfac)
        B0 = TT - AreaBlock.calc_height_by_block_len(2)

        T1 = B0 - border_inner
        B1 = T1 - AreaBlock.calc_height_by_block_len(5)

        T2 = B1 - border_inner
        B2 = T2 - d0 - d0 - widget_full_h
        T3 = B2 - d1
        BB = T2 - AreaBlock.calc_height_by_block_len(10)
        R2 = LL + round((RR - LL) * 0.66)

        L3 = R2 + border_inner
        # */

        props = r_props_by_rnas(RNAS_driver)
        self.props = props
        area_head = AreaBlockHead(self, LL, RR, B0, TT)
        self.area_head = area_head
        layout = Layout(area_head)
        b0 = layout.new_block()
        bars["idtype"] = b0.prop(props, RNAS_driver["idtype"], align="", use_push=False, set_callback=False, append=False)
        bars["id"] = b0.prop(props, RNAS_driver["id"], title="", use_push=False, set_callback=False, append=False)
        b0.split(bars["idtype"], bars["id"].button0, gap=widget_rim)
        bars["driver"] = b0.prop(props, RNAS_driver["driver"], title="Driver", align="full", use_push=False, set_callback=False, option={"r_ID": lambda: props.id})

        area_info = AreaBlockSimple(self, LL, RR, B1, T1)
        self.area_info = area_info
        layout = Layout(area_info)
        b0 = layout.new_block()
        bars["enable"] = b0.prop(props, RNAS_driver["enable"], align="L", set_callback=False, append=False)
        bars["update_dependencies"] = b0.prop(self.bufn_update_dependencies, RNAS_driver["update_dependencies"], title="", use_push=False, set_callback=False, append=False)
        b0.overlay(bars["enable"], bars["update_dependencies"])
        bars["type"] = b0.prop(props, RNAS_driver["type"], align="", set_callback=False)
        bars["expression"] = b0.prop(props, RNAS_driver["expression"], align="", set_callback=False)
        bars["use_self"] = b0.prop(props, RNAS_driver["use_self"], align="R", set_callback=False, append=False)
        bars["driver_value"] = b0.prop(props, RNAS_driver["driver_value"], title="Value :", set_callback=False, append=False)
        b0.overlay(bars["use_self"], bars["driver_value"])
        Layout.no_background(bars["driver_value"].button0)

        bar_info = b0.title("")
        def set_info(s):
            bar_info.blf_title.text = s

        self.set_info = set_info

        area_var = AreaBlockFiltHead(self, L3, RR, B2, T2, [BlockActiveVar(None,
            lambda: self.active_var_name,
            lambda: self.active_var,
            self.set_active_var)])
        self.area_var = area_var

        area_vars = AreaFilterYDriverVar(self, L3, RR, BB, T3, self.r_upd_driver_vars)
        self.area_vars = area_vars

        area_tab = AreaBlockTabDriver(self, LL, R2, BB, T2)
        self.area_tab = area_tab
        area_tab.active_tab = None
        self.active_tab = None

        r_set_callback = self.r_set_callback
        for k, bar in bars.items():
            bar.button0.set_callback = r_set_callback(k)
            bar.button0.poll = poll_hard_disable

        aligntitle = "ID Type  "
        bars["idtype"].aligntitle = aligntitle
        bars["driver"].aligntitle = aligntitle
        aligntitle = "Expression  "
        bars["type"].aligntitle = aligntitle
        bars["expression"].aligntitle = aligntitle
        bars["use_self"].r_button_width = lambda: bars["expression"].button0.box_button.r_w()

        area_head.init_draw_range()
        area_info.init_draw_range()

        self.areas = [area_head, area_info, area_var, area_vars, area_tab]
        self.upd_data()
        #|

    def upd_size_areas(self):
        # <<< 1copy (0ed_DriverEditor_init,, $$)
        PP = self.P_editor
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_full_h = D_SIZE['widget_full_h']

        LL = self.box_win.L + border_outer
        TT = self.box_win.title_B - border_outer
        RR = LL + round(3.0 * D_SIZE['widget_width'] * PP.area_widthfac)
        B0 = TT - AreaBlock.calc_height_by_block_len(2)

        T1 = B0 - border_inner
        B1 = T1 - AreaBlock.calc_height_by_block_len(5)

        T2 = B1 - border_inner
        B2 = T2 - d0 - d0 - widget_full_h
        T3 = B2 - d1
        BB = T2 - AreaBlock.calc_height_by_block_len(10)
        R2 = LL + round((RR - LL) * 0.66)

        L3 = R2 + border_inner
        # >>>
        self.area_head.upd_size(LL, RR, B0, TT)
        self.area_info.upd_size(LL, RR, B1, T1)
        self.area_var.upd_size(L3, RR, B2, T2)
        self.area_vars.upd_size(L3, RR, BB, T3)
        self.area_tab.upd_size(LL, R2, BB, T2)
        #|

    def r_set_callback(self, k):
        bl_update = getattr(self, f"bl_update_{k}", None)
        if bl_update is None: return self.upd_data

        def set_callback():
            try:
                bl_update()
            except: pass
            update_scene()
            # self.sys_inside_evt()

        return set_callback
        #|
    def bl_update_enable(self):
        # <<< 1copy (0dreditor_ed_get_fc,, $$)
        bars = self.bars
        props = self.props
        bars["id"].button0.check(props.idtype)
        fc = bars["driver"].button0.check(props.id)
        # >>>

        fc.mute = not props.enable
        #|
    def bl_update_type(self):
        # <<< 1copy (0dreditor_ed_get_fc,, $$)
        bars = self.bars
        props = self.props
        bars["id"].button0.check(props.idtype)
        fc = bars["driver"].button0.check(props.id)
        # >>>

        fc.driver.type = props.type
        #|
    def bl_update_expression(self):
        # <<< 1copy (0dreditor_ed_get_fc,, $$)
        bars = self.bars
        props = self.props
        bars["id"].button0.check(props.idtype)
        fc = bars["driver"].button0.check(props.id)
        # >>>

        fc.driver.expression = props.expression
        #|
    def bl_update_use_self(self):
        # <<< 1copy (0dreditor_ed_get_fc,, $$)
        bars = self.bars
        props = self.props
        bars["id"].button0.check(props.idtype)
        fc = bars["driver"].button0.check(props.id)
        # >>>

        fc.driver.use_self = props.use_self
        fc.driver.expression = fc.driver.expression
        #|

    def r_upd_driver_vars(self):
        oj = self.active_object
        if hasattr(oj, "variables"): return tuple(oj.variables)
        return tuple()
        #|
    def set_active_var(self, **kw): # object
        Admin.REDRAW()
        self.active_var = kw["object"]
        self.active_var_name = kw["object"].name  if hasattr(kw["object"], "name") else ""
        update_data()
        # self.sys_inside_evt()
        #|
    def set_driver_to(self, datablock, dp, index=None):
        clsname = datablock.__class__.__name__
        if clsname not in D_cls_blendData: return False
        e = D_cls_blendData[clsname]
        if e not in D_blendData_id: return False
        idtype = D_blendData_id[e]
        if index is not None:
            dp = f'{dp}[{index}]'

        bars = self.bars
        bars["idtype"].button0.set(idtype)
        bars["id"].button0.set(datablock)
        bars["driver"].button0.set(dp)

        if not self.props.driver:
            dp = dp.replace('["', '[\\"')
            dp = dp.replace('"]', '\\"]')
            bars["driver"].button0.set(f'["{dp}"]')
        return True
        #|

    # def sys_inside_evt(self):
    #     1copy (0dreditor_ed_get_fc,, $$)

    #     if fc:
    #         dr = fc.driver
    #         variables = dr.variables
    #         if variables:
    #             if self.active_var is None: act_var = variables[0]
    #             else:
    #                 if self.active_var_name in variables: act_var = variables[self.active_var_name]
    #                 else: act_var = variables[0]

    #             self.temp["ob"] = r_variable_value_temp(act_var)
    #     #|

    def bufn_update_dependencies(self):

        if hasattr(self.active_object, "expression"):
            self.active_object.expression = self.active_object.expression
        #|

    def upd_data(self):
        # /* 0dreditor_ed_get_fc
        bars = self.bars
        props = self.props
        bars["id"].button0.check(props.idtype)
        fc = bars["driver"].button0.check(props.id)
        # */

        info = ""
        if fc is None:
            if bars["enable"].is_dark() is False:
                self.area_info.items[0].dark()

            props.driver_value = "0.0"
            self.active_object = None
            self.active_var = None
            self.active_var_name = ""
        else:
            editable = False  if r_library_or_override_message(props.id) else True

            if editable:
                if bars["enable"].is_dark() is True:
                    self.area_info.items[0].light()
            else:
                if bars["enable"].is_dark() is False:
                    self.area_info.items[0].dark()

            try:
                props.driver_value = value_to_display(props.id.path_resolve(props.driver))
            except:

                props.driver_value = "0.0"

            if fc.is_valid is False:
                info += "Invalid driver path, "
            dr = fc.driver
            props.enable = not fc.mute
            props.type = dr.type
            props.expression = dr.expression
            props.use_self = dr.use_self

            self.active_object = dr
            variables = dr.variables
            if self.active_var is None:
                if variables:
                    self.active_var = variables[0]
                    self.active_var_name = self.active_var.name
            else:
                if variables:
                    if self.active_var_name in variables:
                        self.active_var = variables[self.active_var_name]
                    else:
                        self.active_var = variables[0]
                        self.active_var_name = self.active_var.name
                else:
                    self.active_var = None
                    self.active_var_name = ""

            if props.type == "SCRIPTED":
                if editable and bars["expression"].is_dark() is True:
                    bars["expression"].light()
                    bars["use_self"].light()

                if dr.is_valid is False:
                    info += "Invalid driver expression, "
            else:
                if bars["expression"].is_dark() is False:
                    bars["expression"].dark()
                    bars["use_self"].dark()

        self.set_info(f"⚠ {info[ : -2]}" if info else "")

        if self.active_var is None:
            if self.active_tab is not None: self.active_tab = None
        else:
            if self.active_tab != (self.active_var.type,):
                self.active_tab = (self.active_var.type,)


        self.area_head.upd_data()
        self.area_info.upd_data()
        self.area_var.upd_data()
        self.area_vars.upd_data()
        self.area_tab.upd_data()
        #|
    #|
    #|


class AreaBlockTabDriver(AreaBlockTab):
    __slots__ = 'upd_data_callback', 'props'

    def init_tab_SINGLE_PROP(self):
        self.items.clear()
        layout = Layout(self)

        active_var = self.w.active_var
        dr_tar = active_var.targets[0]
        rnas = dr_tar.bl_rna.properties
        props = r_props_by_rnas(RNAS_driver_variable)
        self.props = props
        bars = {}
        has_fallback = hasattr(dr_tar, "use_fallback_value")

        b0 = layout.new_block()
        bars["type"] = b0.prop(active_var, RNAS_driver_variable["type"], title="Variable Type", set_callback=False, align="L")

        b1 = layout.new_block()
        rna_id_type = RnaEnum.copy_from_bl_rna(rnas["id_type"])
        rna_id_type.icon = "idtype"
        bars["id_type"] = b1.prop(dr_tar, rna_id_type, title="ID Type", set_callback=False)
        bars["id"] = b1.prop(dr_tar, rnas["id"], title="ID", set_callback=False)
        bars["data_path"] = b1.prop(dr_tar, rnas["data_path"], title="Path", set_callback=False)
        if has_fallback is True:
            bars["use_fallback_value"] = b1.prop(dr_tar, rnas["use_fallback_value"], align="R", set_callback=False)
            bars["fallback_value"] = b1.prop(dr_tar, rnas["fallback_value"], set_callback=False)

        b2 = layout.new_block()
        bars["variable_value"] = b2.prop(props, RNAS_driver_variable["variable_value"], title="Value :", set_callback=False)
        Layout.no_background(bars["variable_value"].button0)
        bar_info = b2.title("")

        r_button_width = bars["type"].button0.box_button.r_w
        set_callback_button = self.set_callback_button

        for k, bar in bars.items():
            bar.button0.set_callback = set_callback_button
            bar.button0.poll = poll_hard_disable
            bar.r_button_width = r_button_width

        def upd_data_callback():
            active_var = self.w.active_var
            if not hasattr(active_var, "targets"): return
            dr_tar = active_var.targets[0]

            bars["type"].button0.pp = active_var
            bars["id_type"].button0.pp = dr_tar
            bars["id"].button0.pp = dr_tar
            bars["data_path"].button0.pp = dr_tar
            if has_fallback is True:
                bars["use_fallback_value"].button0.pp = dr_tar
                bars["fallback_value"].button0.pp = dr_tar
            info = ""

            bars["id"].button0.check(dr_tar.id_type)

            if dr_tar.id:
                if bars["data_path"].is_dark() is True:
                    bars["data_path"].light()
                    if has_fallback is True:
                        bars["use_fallback_value"].light()
                if has_fallback is True:
                    if dr_tar.use_fallback_value:
                        if bars["fallback_value"].is_dark() is True:
                            bars["fallback_value"].light()
                    else:
                        if bars["fallback_value"].is_dark() is False:
                            bars["fallback_value"].dark()

                if dr_tar.data_path:
                    try: v = dr_tar.id.path_resolve(dr_tar.data_path)
                    except:
                        info += "Invalid Data Path, "
                        v = 0.0
                        if has_fallback is True:
                            if dr_tar.use_fallback_value: v = dr_tar.fallback_value
                else:
                    v = 0.0
                if is_value(v):
                    props.variable_value = value_to_display(round(v, 8))
                else:
                    props.variable_value = str(v)
            else:
                if bars["data_path"].is_dark() is False:
                    bars["data_path"].dark()
                if has_fallback is True:
                    if bars["use_fallback_value"].is_dark() is False:
                        bars["use_fallback_value"].dark()
                    if bars["fallback_value"].is_dark() is False:
                        bars["fallback_value"].dark()

            # /* 0ed_DriverEditor_target_callback_tail
            if active_var.is_name_valid: pass
            else:
                info += "Invalid variable name, "
            if info:
                bar_info.blf_title.text = f"⚠ {info[ : -2]}"
            else:
                bar_info.blf_title.text = ""

            for e in self.items: e.upd_data()
            # */

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_TRANSFORMS(self):
        self.items.clear()
        layout = Layout(self)

        active_var = self.w.active_var
        dr_tar = active_var.targets[0]
        rnas = dr_tar.bl_rna.properties
        props = r_props_by_rnas(RNAS_driver_variable)
        self.props = props
        bars = {}

        b0 = layout.new_block()
        bars["type"] = b0.prop(active_var, RNAS_driver_variable["type"], title="Variable Type", set_callback=False, align="L")

        b1 = layout.new_block()
        bars["id"] = b1.prop(dr_tar, rnas["id"], title="Object", set_callback=False)
        bars["bone_target"] = b1.prop(dr_tar, rnas["bone_target"], title="Bone", set_callback=False, option={"r_armature": self.r_armature})
        bars["transform_type"] = b1.prop(dr_tar, rnas["transform_type"], title="Type", set_callback=False)
        bars["rotation_mode"] = b1.prop(dr_tar, rnas["rotation_mode"], title="Mode", set_callback=False)
        bars["transform_space"] = b1.prop(dr_tar, rnas["transform_space"], title="Space", set_callback=False)

        b2 = layout.new_block()
        bars["variable_value"] = b2.prop(props, RNAS_driver_variable["variable_value"], title="Value :", set_callback=False)
        Layout.no_background(bars["variable_value"].button0)
        bar_info = b2.title("")

        r_button_width = bars["type"].button0.box_button.r_w
        set_callback_button = self.set_callback_button

        for k, bar in bars.items():
            bar.button0.set_callback = set_callback_button
            bar.button0.poll = poll_hard_disable
            bar.r_button_width = r_button_width

        def upd_data_callback():
            active_var = self.w.active_var
            if not hasattr(active_var, "targets"): return
            dr_tar = active_var.targets[0]

            bars["type"].button0.pp = active_var
            bars["id"].button0.pp = dr_tar
            bars["bone_target"].button0.pp = dr_tar
            bars["transform_type"].button0.pp = dr_tar
            bars["rotation_mode"].button0.pp = dr_tar
            bars["transform_space"].button0.pp = dr_tar
            info = ""

            bars["id"].button0.check("OBJECT")

            if hasattr(dr_tar.id, "type") and dr_tar.id.type == "ARMATURE":
                if bars["bone_target"].is_dark() is True:
                    bars["bone_target"].light()

                if dr_tar.bone_target:
                    if dr_tar.bone_target in dr_tar.id.data.bones: pass
                    else: info += "Bone not found, "
            else:
                if bars["bone_target"].is_dark() is False:
                    bars["bone_target"].dark()

            is_rotation = dr_tar.transform_type.startswith("ROT_")
            if is_rotation is True:
                if bars["rotation_mode"].is_dark() is True:
                    bars["rotation_mode"].light()
            else:
                if bars["rotation_mode"].is_dark() is False:
                    bars["rotation_mode"].dark()

            if dr_tar.id is None or isinstance(dr_tar.id, Object): pass
            else:
                info += "Invalid object type, "

            if hasattr(dr_tar, "transform_type"):
                v = r_variable_value_TRANSFORMS(dr_tar)
                if v is None: props.variable_value = ""
                else:
                    if is_rotation is True:
                        props.variable_value = f"{value_to_display(round(v, 8))}  ({value_to_display(round(degrees(v), 6))}°)"
                    else:
                        props.variable_value = value_to_display(round(v, 8))

            # <<< 1copy (0ed_DriverEditor_target_callback_tail,, $$)
            if active_var.is_name_valid: pass
            else:
                info += "Invalid variable name, "
            if info:
                bar_info.blf_title.text = f"⚠ {info[ : -2]}"
            else:
                bar_info.blf_title.text = ""

            for e in self.items: e.upd_data()
            # >>>

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_ROTATION_DIFF(self):
        self.items.clear()
        layout = Layout(self)

        active_var = self.w.active_var
        dr_tar = active_var.targets[0]
        dr_tar1 = active_var.targets[1]
        rnas = dr_tar.bl_rna.properties
        props = r_props_by_rnas(RNAS_driver_variable)
        self.props = props
        bars = {}
        bars1 = {}

        b0 = layout.new_block()
        bars["type"] = b0.prop(active_var, RNAS_driver_variable["type"], title="Variable Type", set_callback=False, align="L")

        b1 = layout.new_block()
        bars["id"] = b1.prop(dr_tar, rnas["id"], title="Object 1", set_callback=False)
        bars["bone_target"] = b1.prop(dr_tar, rnas["bone_target"], title="Bone", set_callback=False, option={"r_armature": self.r_armature})

        b1_0 = layout.new_block()
        bars1["id"] = b1_0.prop(dr_tar1, rnas["id"], title="Object 2", set_callback=False)
        bars1["bone_target"] = b1_0.prop(dr_tar1, rnas["bone_target"], title="Bone", set_callback=False, option={"r_armature": lambda : self.r_armature(1)})

        b2 = layout.new_block()
        bars["variable_value"] = b2.prop(props, RNAS_driver_variable["variable_value"], title="Value :", set_callback=False)
        Layout.no_background(bars["variable_value"].button0)
        bar_info = b2.title("")

        r_button_width = bars["type"].button0.box_button.r_w
        set_callback_button = self.set_callback_button

        for k, bar in bars.items():
            bar.button0.set_callback = set_callback_button
            bar.button0.poll = poll_hard_disable
            bar.r_button_width = r_button_width
        for k, bar in bars1.items():
            bar.button0.set_callback = set_callback_button
            bar.button0.poll = poll_hard_disable
            bar.r_button_width = r_button_width

        def upd_data_callback():
            active_var = self.w.active_var
            if not hasattr(active_var, "targets"): return
            dr_tar = active_var.targets[0]

            bars["type"].button0.pp = active_var
            bars["id"].button0.pp = dr_tar
            bars["bone_target"].button0.pp = dr_tar
            info = ""

            bars["id"].button0.check("OBJECT")

            # /* 0ed_DriverEditor_ROTATION_DIFF_callback
            if hasattr(dr_tar.id, "type") and dr_tar.id.type == "ARMATURE":
                if bars["bone_target"].is_dark() is True:
                    bars["bone_target"].light()

                if dr_tar.bone_target:
                    if dr_tar.bone_target in dr_tar.id.data.bones: pass
                    else: info += "Bone not found, "
            else:
                if bars["bone_target"].is_dark() is False:
                    bars["bone_target"].dark()

            if dr_tar.id is None or isinstance(dr_tar.id, Object): pass
            else:
                info += "Invalid object type, "
            # */

            if len(active_var.targets) > 1:
                dr_tar1 = active_var.targets[1]
                bars1["id"].button0.pp = dr_tar1
                bars1["bone_target"].button0.pp = dr_tar1
                bars1["id"].button0.check("OBJECT")

                # <<< 1copy (0ed_DriverEditor_ROTATION_DIFF_callback,, ${
                #     'dr_tar': 'dr_tar1',
                #     'bars[': 'bars1['
                # }$)
                if hasattr(dr_tar1.id, "type") and dr_tar1.id.type == "ARMATURE":
                    if bars1["bone_target"].is_dark() is True:
                        bars1["bone_target"].light()

                    if dr_tar1.bone_target:
                        if dr_tar1.bone_target in dr_tar1.id.data.bones: pass
                        else: info += "Bone not found, "
                else:
                    if bars1["bone_target"].is_dark() is False:
                        bars1["bone_target"].dark()

                if dr_tar1.id is None or isinstance(dr_tar1.id, Object): pass
                else:
                    info += "Invalid object type, "
                # >>>

                if hasattr(dr_tar, "transform_type"):
                    v = r_variable_value_ROTATION_DIFF(dr_tar, dr_tar1)
                    if v is None: props.variable_value = ""
                    else:
                        props.variable_value = f"{value_to_display(round(v, 8))}  ({value_to_display(round(degrees(v), 6))}°)"
            else:
                props.variable_value = ""

            # <<< 1copy (0ed_DriverEditor_target_callback_tail,, $$)
            if active_var.is_name_valid: pass
            else:
                info += "Invalid variable name, "
            if info:
                bar_info.blf_title.text = f"⚠ {info[ : -2]}"
            else:
                bar_info.blf_title.text = ""

            for e in self.items: e.upd_data()
            # >>>

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_LOC_DIFF(self):
        self.items.clear()
        layout = Layout(self)

        active_var = self.w.active_var
        dr_tar = active_var.targets[0]
        dr_tar1 = active_var.targets[1]
        rnas = dr_tar.bl_rna.properties
        props = r_props_by_rnas(RNAS_driver_variable)
        self.props = props
        bars = {}
        bars1 = {}

        b0 = layout.new_block()
        bars["type"] = b0.prop(active_var, RNAS_driver_variable["type"], title="Variable Type", set_callback=False, align="L")

        b1 = layout.new_block()
        bars["id"] = b1.prop(dr_tar, rnas["id"], title="Object 1", set_callback=False)
        bars["bone_target"] = b1.prop(dr_tar, rnas["bone_target"], title="Bone", set_callback=False, option={"r_armature": self.r_armature})
        bars["transform_space"] = b1.prop(dr_tar, rnas["transform_space"], title="Transform", set_callback=False)

        b1_0 = layout.new_block()
        bars1["id"] = b1_0.prop(dr_tar1, rnas["id"], title="Object 2", set_callback=False)
        bars1["bone_target"] = b1_0.prop(dr_tar1, rnas["bone_target"], title="Bone", set_callback=False, option={"r_armature": lambda : self.r_armature(1)})
        bars1["transform_space"] = b1_0.prop(dr_tar1, rnas["transform_space"], title="Transform", set_callback=False)

        b2 = layout.new_block()
        bars["variable_value"] = b2.prop(props, RNAS_driver_variable["variable_value"], title="Value :", set_callback=False)
        Layout.no_background(bars["variable_value"].button0)
        bar_info = b2.title("")

        r_button_width = bars["type"].button0.box_button.r_w
        set_callback_button = self.set_callback_button

        for k, bar in bars.items():
            bar.button0.set_callback = set_callback_button
            bar.button0.poll = poll_hard_disable
            bar.r_button_width = r_button_width
        for k, bar in bars1.items():
            bar.button0.set_callback = set_callback_button
            bar.button0.poll = poll_hard_disable
            bar.r_button_width = r_button_width

        def upd_data_callback():
            active_var = self.w.active_var
            if not hasattr(active_var, "targets"): return
            dr_tar = active_var.targets[0]

            bars["type"].button0.pp = active_var
            bars["id"].button0.pp = dr_tar
            bars["bone_target"].button0.pp = dr_tar
            bars["transform_space"].button0.pp = dr_tar
            info = ""

            bars["id"].button0.check("OBJECT")

            # <<< 1copy (0ed_DriverEditor_ROTATION_DIFF_callback,, $$)
            if hasattr(dr_tar.id, "type") and dr_tar.id.type == "ARMATURE":
                if bars["bone_target"].is_dark() is True:
                    bars["bone_target"].light()

                if dr_tar.bone_target:
                    if dr_tar.bone_target in dr_tar.id.data.bones: pass
                    else: info += "Bone not found, "
            else:
                if bars["bone_target"].is_dark() is False:
                    bars["bone_target"].dark()

            if dr_tar.id is None or isinstance(dr_tar.id, Object): pass
            else:
                info += "Invalid object type, "
            # >>>

            if len(active_var.targets) > 1:
                dr_tar1 = active_var.targets[1]
                bars1["id"].button0.pp = dr_tar1
                bars1["bone_target"].button0.pp = dr_tar1
                bars1["transform_space"].button0.pp = dr_tar1

                bars1["id"].button0.check("OBJECT")

                # <<< 1copy (0ed_DriverEditor_ROTATION_DIFF_callback,, ${
                #     'dr_tar': 'dr_tar1',
                #     'bars[': 'bars1['
                # }$)
                if hasattr(dr_tar1.id, "type") and dr_tar1.id.type == "ARMATURE":
                    if bars1["bone_target"].is_dark() is True:
                        bars1["bone_target"].light()

                    if dr_tar1.bone_target:
                        if dr_tar1.bone_target in dr_tar1.id.data.bones: pass
                        else: info += "Bone not found, "
                else:
                    if bars1["bone_target"].is_dark() is False:
                        bars1["bone_target"].dark()

                if dr_tar1.id is None or isinstance(dr_tar1.id, Object): pass
                else:
                    info += "Invalid object type, "
                # >>>

                if hasattr(dr_tar, "transform_type"):
                    v = r_variable_value_LOC_DIFF(dr_tar, dr_tar1)
                    if v is None: props.variable_value = ""
                    else:
                        props.variable_value = value_to_display(round(v, 8))
            else:
                props.variable_value = ""

            # <<< 1copy (0ed_DriverEditor_target_callback_tail,, $$)
            if active_var.is_name_valid: pass
            else:
                info += "Invalid variable name, "
            if info:
                bar_info.blf_title.text = f"⚠ {info[ : -2]}"
            else:
                bar_info.blf_title.text = ""

            for e in self.items: e.upd_data()
            # >>>

        self.upd_data_callback = upd_data_callback
        #|
    def init_tab_CONTEXT_PROP(self):
        self.items.clear()
        layout = Layout(self)

        active_var = self.w.active_var
        dr_tar = active_var.targets[0]
        rnas = dr_tar.bl_rna.properties
        props = r_props_by_rnas(RNAS_driver_variable)
        self.props = props
        bars = {}
        has_fallback = hasattr(dr_tar, "use_fallback_value")

        b0 = layout.new_block()
        bars["type"] = b0.prop(active_var, RNAS_driver_variable["type"], title="Variable Type", set_callback=False, align="L")

        b1 = layout.new_block()
        bars["context_property"] = b1.prop(dr_tar, rnas["context_property"], title="Context", set_callback=False)
        bars["data_path"] = b1.prop(dr_tar, rnas["data_path"], title="Path", set_callback=False)
        if has_fallback is True:
            bars["use_fallback_value"] = b1.prop(dr_tar, rnas["use_fallback_value"], align="R", set_callback=False)
            bars["fallback_value"] = b1.prop(dr_tar, rnas["fallback_value"], set_callback=False)

        b2 = layout.new_block()
        bars["variable_value"] = b2.prop(props, RNAS_driver_variable["variable_value"], title="Value :", set_callback=False)
        Layout.no_background(bars["variable_value"].button0)
        bar_info = b2.title("")

        r_button_width = bars["type"].button0.box_button.r_w
        set_callback_button = self.set_callback_button

        for k, bar in bars.items():
            bar.button0.set_callback = set_callback_button
            bar.button0.poll = poll_hard_disable
            bar.r_button_width = r_button_width

        def upd_data_callback():
            active_var = self.w.active_var
            if not hasattr(active_var, "targets"): return
            dr_tar = active_var.targets[0]

            bars["type"].button0.pp = active_var
            bars["data_path"].button0.pp = dr_tar
            info = ""

            if has_fallback is True:
                bars["use_fallback_value"].button0.pp = dr_tar
                bars["fallback_value"].button0.pp = dr_tar
                use_fallback = dr_tar.use_fallback_value

                if use_fallback:
                    if bars["fallback_value"].is_dark() is True:
                        bars["fallback_value"].light()
                else:
                    if bars["fallback_value"].is_dark() is False:
                        bars["fallback_value"].dark()
            else:
                use_fallback = False

            if dr_tar.context_property == "ACTIVE_SCENE":
                e = bpy.context.scene
            elif dr_tar.context_property == "ACTIVE_VIEW_LAYER":
                e = bpy.context.view_layer
            else:
                e = None

            if e:
                try: v = e.path_resolve(dr_tar.data_path)
                except:
                    info += "Invalid Data Path, "
                    v = dr_tar.fallback_value  if use_fallback else 0.0
            else:
                v = 0.0
            if is_value(v):
                props.variable_value = value_to_display(round(v, 8))
            else:
                props.variable_value = str(v)

            # <<< 1copy (0ed_DriverEditor_target_callback_tail,, $$)
            if active_var.is_name_valid: pass
            else:
                info += "Invalid variable name, "
            if info:
                bar_info.blf_title.text = f"⚠ {info[ : -2]}"
            else:
                bar_info.blf_title.text = ""

            for e in self.items: e.upd_data()
            # >>>

        self.upd_data_callback = upd_data_callback
        #|

    def r_armature(self, index=0):
        if hasattr(self.w.active_var, "targets"):
            ob = self.w.active_var.targets[index].id
            if hasattr(ob, "type") and ob.type == "ARMATURE":
                return ob
        return None

    def set_callback_button(self):
        update_scene()
        # self.w.sys_inside_evt()
        #|

    def upd_data(self):
        if self.active_tab == self.w.active_tab:
            if hasattr(self, "upd_data_callback"): self.upd_data_callback()
        else:

            self.init_tab(self.w.active_tab)

            if hasattr(self, "upd_data_callback"): self.upd_data_callback()
        #|
    #|
    #|

def r_variable_value_TRANSFORMS(dr_tar):
    return None
    #|
def r_variable_value_ROTATION_DIFF(dr_tar, dr_tar1):
    return None
    #|
def r_variable_value_LOC_DIFF(dr_tar, dr_tar1):
    return None
    #|

m.D_EDITOR.new('DriverEditor', DriverEditor)

def late_import():
    #|
    from . prop import (
        RNAS_driver,
        RNAS_driver_variable)

    # <<< 1mp (VMD.api
    api = VMD.api
    D_blendData_id = api.D_blendData_id
    D_cls_blendData = api.D_cls_blendData
    # >>>

    # <<< 1mp (VMD.area
    area = VMD.area
    AreaBlock = area.AreaBlock
    AreaBlockHead = area.AreaBlockHead
    AreaFilterYDriverVar = area.AreaFilterYDriverVar
    AreaBlockFiltHead = area.AreaBlockFiltHead
    # >>>

    # <<< 1mp (VMD.block
    block = VMD.block
    Layout = block.Layout
    poll_hard_disable = block.poll_hard_disable
    BlockActiveVar = block.BlockActiveVar
    # >>>

    # <<< 1mp (VMD.m
    m = VMD.m
    P = m.P
    Admin = m.Admin
    BlendDataTemp = m.BlendDataTemp
    update_data = m.update_data
    # >>>

    # <<< 1mp (VMD.rna
    rna = VMD.rna
    r_props_by_rnas = rna.r_props_by_rnas
    # >>>

    # <<< 1mp (VMD.util.algebra
    algebra = VMD.util.algebra
    mat4_to_volume_scale = algebra.mat4_to_volume_scale
    # >>>

    # <<< 1mp (VMD.util.com
    com = VMD.util.com
    value_to_display = com.value_to_display
    is_value = com.is_value
    # >>>

    # <<< 1mp (VMD.util.types
    types = VMD.util.types
    RnaEnum = types.RnaEnum
    # >>>

    # <<< 1mp (VMD.utilbl.blg
    blg = VMD.utilbl.blg
    D_SIZE = blg.D_SIZE
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    # >>>

    # <<< 1mp (VMD.utilbl.general
    general = VMD.utilbl.general
    r_library_or_override_message = general.r_library_or_override_message
    update_scene = general.update_scene
    copy_driver_variable = general.copy_driver_variable
    # >>>

    globals().update(locals())
    #|
