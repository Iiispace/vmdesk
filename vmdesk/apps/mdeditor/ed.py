import bpy

from .  import VMD

# <<< 1mp (VMD.win
win = VMD.win
Window = win.Window
StructGlobalUndo = win.StructGlobalUndo
# >>>

# <<< 1mp (VMD
m = VMD.m
# >>>

# <<< 1mp (VMD.utilbl
utilbl = VMD.utilbl
blg = utilbl.blg
# >>>

class ModifierEditor(Window, StructGlobalUndo):
    __slots__ = (
        'active_object',
        'active_object_name',
        'active_modifier',
        'active_modifier_name',
        'active_tab',
        'is_sync_object',
        'is_sync_modifier',
        'area_tab',
        'area_obj',
        'area_objs',
        'area_md',
        'area_mds')

    name = 'Modifier Editor'
    # WS = set()

    @staticmethod
    def r_size_default():
        PP = P.ModifierEditor
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_full_h = D_SIZE['widget_full_h']
        d0x2h = d0 + d0 + widget_full_h

        border_outer_2 = border_outer + border_outer
        width_min = 6 * widget_full_h

        if PP.area_rowlen_obj == 0:
            area_objs_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_objs_h = AreaFilterY.calc_best_height(PP.area_rowlen_obj)
        if PP.area_rowlen_mds == 0:
            area_mds_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_mds_h = AreaFilterY.calc_best_height(PP.area_rowlen_mds)

        return (
            border_outer_2 + max(width_min, round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac_tab)) + border_inner + max(width_min, round(1.866 * D_SIZE['widget_width'] * PP.area_widthfac_filter)),
            border_outer_2 + d0x2h + d1 + area_objs_h + border_inner + PP.area_list_inner + d0x2h + d1 + area_mds_h
        )
        #| (638, 441)
    @staticmethod
    def r_size_default_area_tab():
        PP = P.ModifierEditor
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_full_h = D_SIZE['widget_full_h']
        d0x2h = d0 + d0 + widget_full_h

        border_outer_2 = border_outer + border_outer
        width_min = 6 * widget_full_h

        if PP.area_rowlen_obj == 0:
            area_objs_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_objs_h = AreaFilterY.calc_best_height(PP.area_rowlen_obj)
        if PP.area_rowlen_mds == 0:
            area_mds_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_mds_h = AreaFilterY.calc_best_height(PP.area_rowlen_mds)

        return (
            max(width_min, round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac_tab)),
            d0x2h + d1 + area_objs_h + border_inner + PP.area_list_inner + d0x2h + d1 + area_mds_h
        )
        #|
    @staticmethod
    def r_size_default_area_objs():
        PP = P.ModifierEditor
        widget_full_h = D_SIZE['widget_full_h']
        width_min = 6 * widget_full_h

        if PP.area_rowlen_obj == 0:
            area_objs_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_objs_h = AreaFilterY.calc_best_height(PP.area_rowlen_obj)

        return (
            max(width_min, round(1.866 * D_SIZE['widget_width'] * PP.area_widthfac_filter)),
            area_objs_h
        )
        #|
    @staticmethod
    def r_size_default_area_mds():
        PP = P.ModifierEditor
        widget_full_h = D_SIZE['widget_full_h']
        width_min = 6 * widget_full_h

        if PP.area_rowlen_mds == 0:
            area_mds_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_mds_h = AreaFilterY.calc_best_height(PP.area_rowlen_mds)

        return (
            max(width_min, round(1.866 * D_SIZE['widget_width'] * PP.area_widthfac_filter)),
            area_mds_h
        )
        #|
    @staticmethod
    def r_size_default_area_obj():
        PP = P.ModifierEditor
        d0 = SIZE_dd_border[0]
        widget_full_h = D_SIZE['widget_full_h']
        width_min = 6 * widget_full_h

        return (
            max(width_min, round(1.866 * D_SIZE['widget_width'] * PP.area_widthfac_filter)),
            d0 + d0 + widget_full_h
        )
        #|

    def init(self, boxes, blfs):
        BlendDataTemp.init()
        PP = self.P_editor
        task = r_task_by_clsname("ModifierEditor")
        if task == None:
            self.is_sync_object = PP.is_sync_object
            self.is_sync_modifier = PP.is_sync_modifier
        else:
            self.is_sync_object = PP.is_sync_object_2
            self.is_sync_modifier = PP.is_sync_modifier_2

        if self.is_sync_object:
            self.active_object = None
            self.active_object_name = ""
        else:
            self.active_object = BlendDataTemp.active_object
            self.active_object_name = BlendDataTemp.active_object_name

        self.active_modifier = None
        self.active_modifier_name = ""

        self.active_tab = None

        # /* 0ed_ModifierEditor_init
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_full_h = D_SIZE['widget_full_h']
        d0x2h = d0 + d0 + widget_full_h
        LL = self.box_win.L + border_outer
        TT = self.box_win.title_B - border_outer
        width_min = 6 * widget_full_h
        if PP.area_rowlen_obj == 0:
            area_objs_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_objs_h = AreaFilterY.calc_best_height(PP.area_rowlen_obj)
        if PP.area_rowlen_mds == 0:
            area_mds_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_mds_h = AreaFilterY.calc_best_height(PP.area_rowlen_mds)

        R0 = LL + max(width_min, round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac_tab))
        B1 = TT - d0x2h
        T2 = B1 - d1
        B2 = T2 - area_objs_h
        L2 = R0 + border_inner
        R2 = L2 + max(width_min, round(1.866 * D_SIZE['widget_width'] * PP.area_widthfac_filter))
        T3 = B2 - border_inner - PP.area_list_inner
        B3 = T3 - d0x2h
        T4 = B3 - d1
        BB = T4 - area_mds_h
        # */

        area_tab = AreaBlockTabModifierEditor(self, LL, R0, BB, TT, self.r_size_default_area_tab)
        area_tab.active_tab = None
        area_tab.search_data = SearchDataArea()

        area_obj = AreaBlockFiltHead(self, L2, R2, B1, TT, [BlockActiveObjectSync(None,
            lambda: self.active_object_name,
            lambda: self.active_object,
            lambda: self.is_sync_object,
            self.set_active_object,
            self.set_sync_object_to)],
            r_size_default = self.r_size_default_area_obj)
        area_objs = AreaFilterYObject(self, L2, R2, B2, T2, r_size_default=self.r_size_default_area_objs)
        area_md = AreaBlockFiltHead(self, L2, R2, B3, T3, [BlockActiveModifierSync(None,
            lambda: self.active_modifier_name,
            lambda: self.active_modifier,
            lambda: self.is_sync_modifier,
            self.set_active_modifier,
            self.set_sync_modifier_to)],
            r_size_default = self.r_size_default_area_obj)
        area_mds = AreaFilterYModifier(self, L2, R2, BB, T4, self.r_upd_modifiers, r_size_default=self.r_size_default_area_mds)

        self.areas = [area_tab, area_obj, area_objs, area_md, area_mds]
        self.area_obj = area_obj
        self.area_objs = area_objs
        self.area_tab = area_tab
        self.area_md = area_md
        self.area_mds = area_mds

        self.upd_data()
        Admin.REDRAW()
        BlendDataTemp.kill()
        #|

    def upd_size_areas(self):
        PP = self.P_editor
        # <<< 1copy (0ed_ModifierEditor_init,, $$)
        border_outer = SIZE_border[0]
        border_inner = SIZE_border[1]
        widget_rim = SIZE_border[3]
        d0 = SIZE_dd_border[0]
        d1 = SIZE_dd_border[1]
        widget_full_h = D_SIZE['widget_full_h']
        d0x2h = d0 + d0 + widget_full_h
        LL = self.box_win.L + border_outer
        TT = self.box_win.title_B - border_outer
        width_min = 6 * widget_full_h
        if PP.area_rowlen_obj == 0:
            area_objs_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_objs_h = AreaFilterY.calc_best_height(PP.area_rowlen_obj)
        if PP.area_rowlen_mds == 0:
            area_mds_h = AreaFilterY.calc_height(max(SIZE_filter[0], widget_full_h))
        else:
            area_mds_h = AreaFilterY.calc_best_height(PP.area_rowlen_mds)

        R0 = LL + max(width_min, round(2.612 * D_SIZE['widget_width'] * PP.area_widthfac_tab))
        B1 = TT - d0x2h
        T2 = B1 - d1
        B2 = T2 - area_objs_h
        L2 = R0 + border_inner
        R2 = L2 + max(width_min, round(1.866 * D_SIZE['widget_width'] * PP.area_widthfac_filter))
        T3 = B2 - border_inner - PP.area_list_inner
        B3 = T3 - d0x2h
        T4 = B3 - d1
        BB = T4 - area_mds_h
        # >>>
        self.area_tab.upd_size(LL, R0, BB, TT)
        self.area_obj.upd_size(L2, R2, B1, TT)
        self.area_objs.upd_size(L2, R2, B2, T2)
        self.area_md.upd_size(L2, R2, B3, T3)
        self.area_mds.upd_size(L2, R2, BB, T4)
        #|

    def r_upd_modifiers(self):
        oj = self.active_object
        if hasattr(oj, "modifiers"): return tuple(oj.modifiers)
        return tuple()
        #|

    def set_active_object(self, **kw): # object
        Admin.REDRAW()
        if self.is_sync_object: object_select(kw["object"])
        else:
            self.active_object = kw["object"]
            self.active_object_name = kw["object"].name  if hasattr(kw["object"], "name") else ""
        update_data()
        #|
    def set_active_modifier(self, **kw): # object
        Admin.REDRAW()
        if self.is_sync_modifier:
            try: self.active_object.modifiers.active = kw["object"]
            except: pass
        else:
            self.active_modifier = kw["object"]
            self.active_modifier_name = kw["object"].name  if hasattr(kw["object"], "name") else ""
        update_data()
        #|
    def set_sync_object_to(self, boo):
        if boo:
            if self.is_sync_object == True: return
            self.is_sync_object = True
            BlendDataTemp.init()
            self.upd_data()
            BlendDataTemp.kill()
        else:
            if self.is_sync_object == False: return
            self.is_sync_object = False
            BlendDataTemp.init()
            self.upd_data()
            BlendDataTemp.kill()
        #|
    def set_sync_modifier_to(self, boo):
        if boo:
            if self.is_sync_modifier == True: return
            self.is_sync_modifier = True
            BlendDataTemp.init()
            self.upd_data()
            BlendDataTemp.kill()
        else:
            if self.is_sync_modifier == False: return
            self.is_sync_modifier = False
            BlendDataTemp.init()
            self.upd_data()
            BlendDataTemp.kill()
        #|

    def resize_upd_end(self):
        if hasattr(self, "areas") and P.adaptive_win_resize:
            sizeXmin, sizeYmin = self.r_size_default()
            box_win = self.box_win
            sizeXmin_objs, sizeYmin_objs = self.r_size_default_area_objs()

            border_outer = SIZE_border[0]
            border_inner = SIZE_border[1]
            widget_rim = SIZE_border[3]
            d0 = SIZE_dd_border[0]
            d1 = SIZE_dd_border[1]
            widget_full_h = D_SIZE['widget_full_h']
            d0x2h = d0 + d0 + widget_full_h
            LL = self.area_tab.box_area.L
            TT = self.area_tab.box_area.T
            width_min = 6 * widget_full_h

            if box_win.R - box_win.L > sizeXmin:
                R2 = box_win.R - border_outer
                L2 = R2 - sizeXmin_objs
                R0 = L2 - border_inner
            else:
                R0 = LL + self.r_size_default_area_tab()[0]
                L2 = R0 + border_inner
                R2 = L2 + sizeXmin_objs

            B1 = TT - d0x2h
            T2 = B1 - d1
            B2 = T2 - sizeYmin_objs
            T3 = B2 - border_inner - self.P_editor.area_list_inner
            B3 = T3 - d0x2h
            T4 = B3 - d1
            BB = min(T4 - self.r_size_default_area_mds()[1], box_win.B + border_outer)

            self.area_tab.resize_upd_end(override=(LL, R0, BB, TT))
            self.area_obj.resize_upd_end(override=(L2, R2, B1, TT))
            self.area_objs.resize_upd_end(override=(L2, R2, B2, T2))
            self.area_md.resize_upd_end(override=(L2, R2, B3, T3))
            self.area_mds.resize_upd_end(override=(L2, R2, BB, T4))
        else:
            self.area_tab.resize_upd_end()
            self.area_obj.resize_upd_end()
            self.area_objs.resize_upd_end()
            self.area_md.resize_upd_end()
            self.area_mds.resize_upd_end()
        #|

    def upd_data(self): # Need BlendDataTemp.init(), BlendDataTemp.kill()
        if self.is_sync_object:
            self.active_object = BlendDataTemp.active_object
            self.active_object_name = BlendDataTemp.active_object_name
        else:
            if self.active_object == None:
                self.active_object = BlendDataTemp.active_object
                self.active_object_name = BlendDataTemp.active_object_name
            else:
                try: self.active_object_name = self.active_object.name
                except:

                    if self.active_object_name in (
                        # <<< 1copy (bl_objects,, $$)
                        bpy.context.view_layer.objects
                        # >>>
                    ):
                        self.active_object = (
                            # <<< 1copy (bl_objects,, $$)
                            bpy.context.view_layer.objects
                            # >>>
                        )[self.active_object_name]
                        self.active_object_name = self.active_object.name
                    else:
                        self.active_object = BlendDataTemp.active_object
                        self.active_object_name = BlendDataTemp.active_object_name

        if hasattr(self.active_object, "modifiers"):
            if self.is_sync_modifier:
                if hasattr(self.active_object.modifiers, "active"):
                    self.active_modifier = self.active_object.modifiers.active
                    if hasattr(self.active_modifier, "name"):
                        self.active_modifier_name = self.active_modifier.name
                    else:
                        self.active_modifier_name = ""
                else:
                    self.active_modifier = None
                    self.active_modifier_name = ""
            else:
                if self.active_modifier in tuple(self.active_object.modifiers):
                    self.active_modifier_name = self.active_modifier.name
                else:
                    if self.active_object.modifiers:
                        self.active_modifier = self.active_object.modifiers[0]
                        self.active_modifier_name = self.active_modifier.name
                    else:
                        self.active_modifier = None
                        self.active_modifier_name = ""
        else:
            self.active_modifier = None
            self.active_modifier_name = ""

        if self.active_modifier == None:
            if self.active_tab != None: self.active_tab = None
        else:
            if self.active_tab != (self.active_modifier.type,): self.active_tab = (self.active_modifier.type,)

        self.area_obj.upd_data()
        self.area_objs.upd_data()
        self.area_md.upd_data()
        self.area_mds.upd_data()
        self.area_tab.upd_data()
        #|
    #|
    #|

m.D_EDITOR.new('ModifierEditor', ModifierEditor)

def late_import():
    #|
    from . areas import AreaBlockTabModifierEditor

    # <<< 1mp (VMD.area
    area = VMD.area
    AreaFilterY = area.AreaFilterY
    AreaFilterYObject = area.AreaFilterYObject
    AreaFilterYModifier = area.AreaFilterYModifier
    AreaBlockFiltHead = area.AreaBlockFiltHead
    SearchDataArea = area.SearchDataArea
    # >>>

    # <<< 1mp (VMD.block
    block = VMD.block
    BlockActiveObjectSync = block.BlockActiveObjectSync
    BlockActiveModifierSync = block.BlockActiveModifierSync
    # >>>

    # <<< 1mp (VMD.keysys
    keysys = VMD.keysys
    kill_evt = keysys.kill_evt
    MOUSE = keysys.MOUSE
    EVT_TYPE = keysys.EVT_TYPE
    TRIGGER = keysys.TRIGGER
    TRIGGER_END = keysys.TRIGGER_END
    TRIGGER_IND = keysys.TRIGGER_IND
    # >>>

    # <<< 1mp (VMD.m
    m = VMD.m
    P = m.P
    Admin = m.Admin
    W_MODAL = m.W_MODAL
    W_HEAD = m.W_HEAD
    W_DRAW = m.W_DRAW
    TASKS = m.TASKS
    REGION_DATA = m.REGION_DATA
    r_mouseloop = m.r_mouseloop
    r_task_by_clsname = m.r_task_by_clsname
    update_data = m.update_data
    BlendDataTemp = m.BlendDataTemp
    object_select = m.object_select
    # >>>

    # <<< 1mp (blg
    FONT0 = blg.FONT0
    D_SIZE = blg.D_SIZE
    SIZE_widget = blg.SIZE_widget
    SIZE_border = blg.SIZE_border
    SIZE_dd_border = blg.SIZE_dd_border
    SIZE_filter = blg.SIZE_filter
    # >>>

    globals().update(locals())
    #|
