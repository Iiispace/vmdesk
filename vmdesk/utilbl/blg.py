import bpy, _bpy, blf, gpu

escape_identifier = bpy.utils.escape_identifier

blfLoad = blf.load
blfSize = blf.size
blfPos = blf.position
blfDraw = blf.draw
blfDimen = blf.dimensions

scissor_test_set = gpu.state.scissor_test_set
scissor_set = gpu.state.scissor_set

get_projection_matrix = gpu.matrix.get_projection_matrix
CONTEXT = _bpy.context

from_image = gpu.texture.from_image
gpu_types = gpu.types
BUILTIN_SHADER_UNIFORM_COLOR = gpu.shader.from_builtin('UNIFORM_COLOR')
BUILTIN_SHADER_UNIFORM_COLOR_bind = BUILTIN_SHADER_UNIFORM_COLOR.bind
BUILTIN_SHADER_UNIFORM_COLOR_uniform_float = BUILTIN_SHADER_UNIFORM_COLOR.uniform_float

# <<< 1mp (gpu_types
GPUBatch = gpu_types.GPUBatch
GPUIndexBuf = gpu_types.GPUIndexBuf
GPUVertBuf = gpu_types.GPUVertBuf
GPUVertFormat = gpu_types.GPUVertFormat
# >>>

import math
# <<< 1mp (math
floor = math.floor
ceil = math.ceil
sin = math.sin
cos = math.cos
# >>>

from os import sep as os_sep

from .  import glshader

# <<< 1mp (glshader
GL_BOX = glshader.GL_BOX
GL_BOX_bind = glshader.GL_BOX_bind
GL_BOX_uniform_float = glshader.GL_BOX_uniform_float
GL_RIM = glshader.GL_RIM
GL_RIM_bind = glshader.GL_RIM_bind
GL_RIM_uniform_float = glshader.GL_RIM_uniform_float
GL_RIM_uniform_int = glshader.GL_RIM_uniform_int
GL_BUTTON = glshader.GL_BUTTON
GL_BUTTON_bind = glshader.GL_BUTTON_bind
GL_BUTTON_uniform_float = glshader.GL_BUTTON_uniform_float
GL_BUTTON_uniform_int = glshader.GL_BUTTON_uniform_int
GL_WIN = glshader.GL_WIN
GL_WIN_bind = glshader.GL_WIN_bind
GL_WIN_uniform_float = glshader.GL_WIN_uniform_float
GL_WIN_uniform_int = glshader.GL_WIN_uniform_int
GL_IMG = glshader.GL_IMG
GL_IMG_bind = glshader.GL_IMG_bind
GL_IMG_uniform_float = glshader.GL_IMG_uniform_float
GL_IMG_uniform_sampler = glshader.GL_IMG_uniform_sampler
GL_SHADOW = glshader.GL_SHADOW
GL_SHADOW_bind = glshader.GL_SHADOW_bind
GL_SHADOW_uniform_float = glshader.GL_SHADOW_uniform_float
GL_SHADOW_uniform_int = glshader.GL_SHADOW_uniform_int
GL_GRID = glshader.GL_GRID
GL_GRID_bind = glshader.GL_GRID_bind
GL_GRID_uniform_float = glshader.GL_GRID_uniform_float
GL_GRID_uniform_int = glshader.GL_GRID_uniform_int
GL_PICKER_SV = glshader.GL_PICKER_SV
GL_PICKER_SV_bind = glshader.GL_PICKER_SV_bind
GL_PICKER_SV_uniform_float = glshader.GL_PICKER_SV_uniform_float
GL_PICKER_H = glshader.GL_PICKER_H
GL_PICKER_H_bind = glshader.GL_PICKER_H_bind
GL_PICKER_H_uniform_float = glshader.GL_PICKER_H_uniform_float
GL_SELECTION = glshader.GL_SELECTION
GL_SELECTION_bind = glshader.GL_SELECTION_bind
GL_SELECTION_uniform_float = glshader.GL_SELECTION_uniform_float
GL_SELECTION_uniform_int = glshader.GL_SELECTION_uniform_int
GL_SCREENDASH_3D = glshader.GL_SCREENDASH_3D
GL_SCREENDASH_3D_bind = glshader.GL_SCREENDASH_3D_bind
GL_SCREENDASH_3D_uniform_float = glshader.GL_SCREENDASH_3D_uniform_float
# >>>

from .. util.const import FLO_0000, STR_AZaz


FONT_ACTIVE = 0
CLIPPING_END_STR = " ‧‧"
CLIPPING_FRONT_STR = "‧‧ "
CLIPPING_END_STR_DIMEN = 0
CLIPPING_FRONT_STR_DIMEN = 0
D_SIZE = {}
STR_VALBOX = '0' * 21
GPUIMGUV = ((0, 0), (1, 0), (1, 1), (0, 1))

#_c4#_c4#_c4#_c4

# def recommended_comp_type(attr_type):
#     if attr_type in {'FLOAT', 'VEC2', 'VEC3', 'VEC4', 'MAT3', 'MAT4'}:
#         return 'F32'
#     if attr_type in {'UINT', 'UVEC2', 'UVEC3', 'UVEC4'}:
#         return 'U32'
#     return 'I32'

# def recommended_fetch_mode(comp_type):
#     if comp_type == 'F32':
#         return 'FLOAT'
#     return 'INT'

VBO_FORMAT_position_F32_FLOAT = GPUVertFormat()
VBO_FORMAT_position_F32_FLOAT.attr_add(id='position', comp_type='F32', len=2, fetch_mode='FLOAT')

VBO_FORMAT_position_uv_F32_FLOAT = GPUVertFormat()
VBO_FORMAT_position_uv_F32_FLOAT.attr_add(id='position', comp_type='F32', len=2, fetch_mode='FLOAT')
VBO_FORMAT_position_uv_F32_FLOAT.attr_add(id='uv', comp_type='F32', len=2, fetch_mode='FLOAT')

VBO_FORMAT_pos_F32_2_FLOAT = GPUVertFormat()
VBO_FORMAT_pos_F32_2_FLOAT.attr_add(id='pos', comp_type='F32', len=2, fetch_mode='FLOAT')

VBO_FORMAT_pos_F32_3_FLOAT = GPUVertFormat()
VBO_FORMAT_pos_F32_3_FLOAT.attr_add(id='pos', comp_type='F32', len=3, fetch_mode='FLOAT')
#_c4#_c4#_c4#_c4

def upd_font_size():
    #|
    h = SIZE_widget[0]
    title_h = SIZE_title[0]
    dd_title_h = SIZE_title[1]
    d2 = SIZE_border[3] * 2

    font_title = floor(title_h * SIZE_foreground[0])
    font_dd_title = floor(dd_title_h * SIZE_foreground[0])
    font_subtitle = floor(h * SIZE_foreground[1])
    font_main = floor(h * SIZE_foreground[2])
    font_label = floor(h * SIZE_foreground[3])

    D_SIZE['font_title'] = font_title
    D_SIZE['font_dd_title'] = font_dd_title
    D_SIZE['font_subtitle'] = font_subtitle
    D_SIZE['font_main'] = font_main
    D_SIZE['font_label'] = font_label

    blfSize(FONT0, font_title)
    y = floor((title_h - blfDimen(FONT0, 'X')[1]) / 2 + font_title / 25)
    D_SIZE['font_title_dy'] = y
    D_SIZE['font_title_dx'] = floor(y * 1.2)
    D_SIZE['font_title_dT'] = title_h - y

    blfSize(FONT0, font_dd_title)
    y = floor((dd_title_h - blfDimen(FONT0, 'X')[1]) / 2 + font_dd_title / 25)
    D_SIZE['font_dd_title_dy'] = y
    D_SIZE['font_dd_title_dx'] = floor(y * 1.2)
    D_SIZE['font_dd_title_dT'] = dd_title_h - y

    blfSize(FONT0, font_subtitle)
    y = floor((h - blfDimen(FONT0, 'X')[1]) / 2 + font_subtitle / 25)
    D_SIZE['font_subtitle_dy'] = y
    D_SIZE['font_subtitle_dx'] = floor(y * 1.2)
    D_SIZE['font_subtitle_dT'] = h - y

    blfSize(FONT0, font_main)
    y = floor((h - blfDimen(FONT0, 'X')[1]) / 2 + font_main / 25)
    D_SIZE['font_main_dy'] = y
    D_SIZE['font_main_dx'] = floor(y * 1.2)
    D_SIZE['font_main_dT'] = h - y
    D_SIZE['font_main_title_offset'] = round((h * 4) * SIZE_widget_fac[1])
    D_SIZE['font_main_title_offset_R'] = round((h * 4) * SIZE_widget_fac[1] * 0.8)
    widget_full_h = h + d2
    D_SIZE['widget_full_h'] = widget_full_h
    D_SIZE['widget_width'] = floor(blfDimen(FONT0, STR_VALBOX)[0]) + D_SIZE['font_main_dx'] * 2 + d2
    D_SIZE['widget_bool_h'] = floor(h * SIZE_widget_fac[0])
    widget_bool_full_h = D_SIZE['widget_bool_h'] + d2
    D_SIZE['widget_bool_full_h'] = widget_bool_full_h
    h_diff = widget_full_h - widget_bool_full_h
    D_SIZE['widget_bool_dB'] = h_diff // 2
    D_SIZE['widget_bool_dT'] = h_diff - D_SIZE['widget_bool_dB']

    blfSize(FONT0, font_label)
    y = floor((h - blfDimen(FONT0, 'X')[1]) / 2 + font_label / 25)
    D_SIZE['font_label_dy'] = y
    D_SIZE['font_label_dx'] = floor(y * 1.2)
    D_SIZE['font_label_dT'] = h - y
    #|
def r_widget_font_dx_dy_dT(font_id, h):
    font_main = floor(h * SIZE_foreground[2])
    blfSize(font_id, font_main)
    y = floor((h - blfDimen(font_id, 'X')[1]) / 2 + font_main / 25)
    return floor(y * 1.2), y, h - y
    #|



def clipboard_write(s):
    bpy.context.window_manager.clipboard = s
    #|

def report(s, ty='INFO'):
    #|
    if m.ADMIN == None:
        return False

    m.ADMIN.report({ty}, s)
    return True
    #|
# @
def decoReport(ty='INFO'):
    def deco(fn):
        def wrapper(*k, **kw):
            success, message = fn(*k, **kw)
            if not success: report(message, ty)
            return success, message
        return wrapper
    return deco
    #|


class Scissor:
    __slots__ = 'x', 'y', 'w', 'h'

    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        #|

    def LRBT(self, L, R, B, T):
        self.x = L
        self.y = B
        self.w = R - L
        self.h = T - B
        #|

    def inbox(self, mouse):
        return self.x < mouse[0] < self.x + self.w and self.y < mouse[1] < self.y + self.w
        #|

    def use(self):
        scissor_set(self.x, self.y, self.w, self.h)
        #|

    def dxy(self, dx, dy):
        self.x += dx
        self.y += dy
        #|

    def intersect_with(self, sci, L, R, B, T):
        self.x = max(L, sci.x)
        self.y = max(B, sci.y)
        self.h = max(0, min(T, sci.y + sci.h) - self.y)
        self.w = max(0, min(R, sci.x + sci.w) - self.x)
        #|

    @staticmethod
    def r_intersect_scissor(sci_x, sci_y, sci_w, sci_h, L, R, B, T):
        x = max(L, sci_x)
        y = max(B, sci_y)
        return x, y, max(0, min(R, sci_x + sci_w) - x), max(0, min(T, sci_y + sci_h) - y)
    #|
    #|
class ScissorFake(Scissor):
    __slots__ = ()

    def use(self): pass
    #|
    #|



class Blf:
    __slots__ = 'color', 'text', 'size', 'x', 'y'

    def __init__(self, text="", x=0, y=0):
        self.text = text
        self.x = x
        self.y = y
        #|

    def draw_pos(self):
        blfPos(FONT0, self.x, self.y, 0)
        blfDraw(FONT0, self.text)
        #|
    #|
    #|
class BlfColor:
    __slots__ = 'color', 'text', 'size', 'x', 'y'

    def __init__(self, text="", x=0, y=0, color=None):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        #|

    def draw_pos(self):
        blfPos(FONT0, self.x, self.y, 0)
        blfDraw(FONT0, self.text)
        #|
    #|
    #|
class BlfClip(Blf):
    __slots__ = 'unclip_text'

    def __init__(self, text="", unclip_text="", x=0, y=0):
        self.text = text
        self.unclip_text = unclip_text
        self.x = x
        self.y = y
        #|
    #|
    #|
class BlfClipColor:
    __slots__ = 'color', 'text', 'size', 'x', 'y', 'unclip_text'

    def __init__(self, text="", unclip_text="", x=0, y=0, color=None):
        self.text = text
        self.unclip_text = unclip_text
        self.x = x
        self.y = y
        self.color = color
        #|
    #|
    #|

class BlfColorAnimY:
    __slots__ = 'color', 'text', 'size', 'x', 'y', 'y_anim', 'speed'

    def __init__(self, text="", x=0, y=0, color=None, y_anim=0.0, speed=1.0):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.y_anim = y_anim
        self.speed = speed
        #|

    def draw_pos(self):
        blfPos(FONT0, self.x, self.y_anim, 0)
        blfDraw(FONT0, self.text)
        #|
    #|
    #|

#| require set_size
def r_blf_y_by_cy(cy):
    #|
    return round(cy + blfDimen(FONT_ACTIVE, 'Yy')[1] / 2 - blfDimen(FONT_ACTIVE, 'X')[1])
    #|
#| require set_size
def r_blf_ind(text, x, R):
    # /* 0blg_r_blf_ind
    R -= x
    len_text = len(text)
    low = 0
    high = len_text
    i = 0

    while low <= high:
        i = (low + high) // 2
        if blfDimen(FONT_ACTIVE, text[ : i])[0] < R: low = i + 1
        else: high = i - 1

    if i == len_text:
        if i == 0: return i
        if abs(R - blfDimen(FONT_ACTIVE, text[ : i])[0]) <= abs(R - blfDimen(FONT_ACTIVE, text[ : i - 1])[0]):
            return i
        return i - 1

    ix = blfDimen(FONT_ACTIVE, text[ : i])[0]

    if R >= ix:
        if abs(R - blfDimen(FONT_ACTIVE, text[ : i + 1])[0]) <= abs(R - ix):
            return i + 1
        return i

    if abs(R - ix) <= abs(R - blfDimen(FONT_ACTIVE, text[ : i - 1])[0]):
        return i
    return i - 1
    # */
#| require set_size
def r_blf_index(text, x, R, font_id):
    # <<< 1copy (0blg_r_blf_ind,, ${'FONT_ACTIVE':'font_id'}$)
    R -= x
    len_text = len(text)
    low = 0
    high = len_text
    i = 0

    while low <= high:
        i = (low + high) // 2
        if blfDimen(font_id, text[ : i])[0] < R: low = i + 1
        else: high = i - 1

    if i == len_text:
        if i == 0: return i
        if abs(R - blfDimen(font_id, text[ : i])[0]) <= abs(R - blfDimen(font_id, text[ : i - 1])[0]):
            return i
        return i - 1

    ix = blfDimen(font_id, text[ : i])[0]

    if R >= ix:
        if abs(R - blfDimen(font_id, text[ : i + 1])[0]) <= abs(R - ix):
            return i + 1
        return i

    if abs(R - ix) <= abs(R - blfDimen(font_id, text[ : i - 1])[0]):
        return i
    return i - 1
    # >>>
    #|


#| require
#|      set_size
#|      CLIPPING_END_STR_DIMEN
def r_blf_clipping_end(text, x, R):
    if blfDimen(FONT_ACTIVE, text)[0] + x > R:
        return f'{text[ : r_blf_ind(text, x, R - CLIPPING_END_STR_DIMEN)]}{CLIPPING_END_STR}'
    else:
        return text
    #|
#| require
#|      set_size
#|      CLIPPING_END_STR_DIMEN
def r_blf_clipping_end_with(text, width):
    if blfDimen(FONT_ACTIVE, text)[0] > width:
        return f'{text[ : r_blf_ind(text, 0, width - CLIPPING_END_STR_DIMEN)]}{CLIPPING_END_STR}'
    else:
        return text
    #|
#| require
#|      set_size
def rl_blf_wrap(tx, width):
    lines = []

    while tx:
        ll = len(tx)
        low = 0
        high = ll
        while low <= high:
            i = (low + high) // 2
            dimen = blfDimen(FONT_ACTIVE, tx[: i])[0]
            if dimen < width: low = i + 1
            else: high = i - 1
        if i == 0:
            i = 1
        elif i == ll:
            if blfDimen(FONT_ACTIVE, tx[: i])[0] <= width: pass
            elif i != 1: i -= 1
        else:
            if blfDimen(FONT_ACTIVE, tx[: i + 1])[0] <= width: i += 1
            elif blfDimen(FONT_ACTIVE, tx[: i])[0] <= width: pass
            elif i != 1: i -= 1
        if i != ll:
            if tx[i - 1] in STR_AZaz and tx[i] in STR_AZaz:
                for r in range(i - 2, -1, -1):
                    if tx[r] not in STR_AZaz:
                        if r > 5: i = r + 1
                        break

        body = tx[: i]
        if body == "." and lines:
            lines[-1] += body
        else:
            s = tx[: i]
            if s and s.startswith(' ') and lines:
                lines[-1] += ' '
                lines.append(s[1 :])
            else:
                lines.append(s)
        tx = tx[i :]
    return lines
    #|
#| require
#|      set_size
def rl_blf_wrap_LR(tx, L, R, y, depth): # At least ret 1 Blf
    width = R - L
    lines = []

    while tx:
        ll = len(tx)
        low = 0
        high = ll
        while low <= high:
            i = (low + high) // 2
            dimen = blfDimen(FONT_ACTIVE, tx[: i])[0]
            if dimen < width: low = i + 1
            else: high = i - 1
        if i == 0:
            i = 1
        elif i == ll:
            if blfDimen(FONT_ACTIVE, tx[: i])[0] <= width: pass
            elif i != 1: i -= 1
        else:
            if blfDimen(FONT_ACTIVE, tx[: i + 1])[0] <= width: i += 1
            elif blfDimen(FONT_ACTIVE, tx[: i])[0] <= width: pass
            elif i != 1: i -= 1
        if i != ll:
            if tx[i - 1] in STR_AZaz and tx[i] in STR_AZaz:
                for r in range(i - 2, -1, -1):
                    if tx[r] not in STR_AZaz:
                        if r > 5: i = r + 1
                        break

        body = tx[: i]
        if body == "." and lines:
            lines[-1].text += body
        else:
            s = tx[: i]
            if s and s.startswith(' ') and lines:
                lines[-1].text += ' '
                lines.append(Blf(s[1 :], L, y))
            else:
                lines.append(Blf(s, L, y))
            y -= depth
        tx = tx[i :]

    if not lines: return [Blf('', L, y)]
    return lines
    #|


def r_icon_size(name):
    if name[0].isupper() and not name[1].isupper(): return (SIZE_tb[0], SIZE_tb[0])
    if name.startswith("tb_"): return (SIZE_tb[0], SIZE_tb[0])
    if name == "title_button": return (SIZE_title[0], SIZE_title[0] * 3)
    if name == "checkbox_fg": return (D_SIZE['widget_bool_full_h'], D_SIZE['widget_bool_full_h'])
    if name == "dropdown_close":
        inner = SIZE_title[1] // 20
        button_h = SIZE_title[1] - inner - inner - SIZE_border[3] - SIZE_border[3]
        return (button_h, button_h)
    if name.startswith("settings_"):
        if name[9 :].find("_") != -1:
            button_h = D_SIZE['font_subtitle_dT'] + D_SIZE['font_subtitle_dy']
            return (button_h, button_h)

    h = SIZE_widget[0]
    if name.startswith("hue_"):
        button_h = ceil(h / 2)
        button_h += button_h
        return (button_h, button_h)

    return (h, h)
    #|
def r_button_h(): return SIZE_widget[0]
def r_widget_rim(): return SIZE_border[3]

def is_LRBT_match(e0, e1): return e0.L == e1.L and e0.R == e1.R and e0.B == e1.B and e0.T == e1.T

class BoxFake:
    __slots__ = ()

    def bind_draw(self): pass
    def LRBT(self, L, R, B, T): pass
    def LRBT_upd(self, L, R, B, T): pass
    def inbox(self, mouse): return False
    def dx(self, dx): pass
    def dx_upd(self, dx): pass
    def dy(self, dy): pass
    def dy_upd(self, dy): pass
    def dxy(self, dx, dy): pass
    def dxy_upd(self, dx, dy): pass
    #|
    #|

class GpuBox:
    __slots__ = 'color', 'L', 'R', 'B', 'T', 'batdraw'

    def __init__(self, color=None, L=0, R=0, B=0, T=0):
        self.color = color
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        #|

    def upd(self):
        # <<< 1copy (0blg_Box_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_BOX'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BOX)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    # def bind_draw(self)
    # <<< 1copy (0blg_Box_bind_draw,, $$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", self.color)
        self.batdraw()
    # >>>
    # def bind_draw_color(self, color4)
    # <<< 1copy (0blg_Box_bind_draw,, ${
    #     'bind_draw(self)': 'bind_draw_color(self, color4)',
    #     'self.color': 'color4',
    # }$)
    def bind_draw_color(self, color4):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", color4)
        self.batdraw()
    # >>>

    def LRBT(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        #|
    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_Box_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_BOX'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BOX)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def copy_LRBT(self, box):
        self.L = box.L
        self.R = box.R
        self.B = box.B
        self.T = box.T
        #|
    def inset_with_depth(self, box, depth):
        self.L = box.L + depth
        self.R = box.R - depth
        self.B = box.B + depth
        self.T = box.T - depth
        #|

    def inbox(self, mouse):
        return self.L <= mouse[0] < self.R and self.B <= mouse[1] < self.T
        #|
    def out_T(self, mouse):
        return self.T <= mouse[1]
        #|
    def out_B(self, mouse):
        return self.B > mouse[1]
        #|
    def out_L(self, mouse):
        return self.L > mouse[0]
        #|
    def out_R(self, mouse):
        return self.R <= mouse[0]
        #|
    def in_T(self, mouse):
        return mouse[1] < self.T
        #|
    def in_B(self, mouse):
        return self.B <= mouse[1]
        #|
    def in_L(self, mouse):
        return self.L <= mouse[0]
        #|
    def in_R(self, mouse):
        return mouse[0] < self.R
        #|
    def in_LR(self, mouse):
        return self.L <= mouse[0] < self.R
        #|
    def in_BT(self, mouse):
        return self.B <= mouse[1] < self.T
        #|
    def r_w(self):
        return self.R - self.L
        #|
    def r_h(self):
        return self.T - self.B
        #|
    def r_center_x(self):
        return self.L + (self.R - self.L) // 2
        #|
    def r_center_y(self):
        return self.B + (self.T - self.B) // 2
        #|
    def r_center_x_float(self):
        return self.L + (self.R - self.L) / 2
        #|
    def r_center_y_float(self):
        return self.B + (self.T - self.B) / 2
        #|
    def r_LRBT(self):
        return self.L, self.R, self.B, self.T
        #|

    def dx(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        #|
    def dy(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        #|
    def dxy(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_BOX'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BOX)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Box_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_BOX'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BOX)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Box_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_BOX'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BOX)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def copy(self):
        out = GpuBox(
            [e  for e in self.color]  if hasattr(self.color, "__len__") else self.color,
            self.L,
            self.R,
            self.B,
            self.T
        )
        if hasattr(self, "batdraw"):
            out.batdraw = self.batdraw
        return out
        #|
    #|
    #|

class GpuRim(GpuBox):
    __slots__ = 'd', 'inner', 'color_rim'

    def __init__(self, color=None, color_rim=None, L=0, R=0, B=0, T=0, d=0):
        self.color = color
        self.color_rim = color_rim
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.d = d
        self.inner = [0] * 4
        #|

    def upd(self):
        # <<< 1copy (0blg_Rim_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_RIM'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def bind_draw(self):
        # <<< 1copy (0blg_GpuRim_bind_draw,, $$)
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", self.color)
        GL_RIM_uniform_float("color_rim", self.color_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
        # >>>
        #|

    def LRBT(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        self.inner[:] = L + d, R - d, B + d, T - d
        #|
    def LRBT_upd(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        # <<< 1copy (0blg_Rim_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_RIM'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Rim_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_RIM'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Rim_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_RIM'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Rim_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_RIM'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def copy(self):
        out = GpuRim(
            [e  for e in self.color]  if hasattr(self.color, "__len__") else self.color,
            [e  for e in self.color_rim]  if hasattr(self.color_rim, "__len__") else self.color_rim,
            self.L,
            self.R,
            self.B,
            self.T,
            self.d
        )
        out.inner[:] = self.inner
        if hasattr(self, "batdraw"):
            out.batdraw = self.batdraw
        return out
        #|
    #|
    #|

class GpuButton(GpuBox):
    __slots__ = 'd', 'inner', 'color_rim', 'state'

    # /* 0blg_GpuButton_init
    def __init__(self, L=0, R=0, B=0, T=0, d=0):
        self.color = COL_box_button
        self.color_rim = COL_box_button_rim
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.d = d
        self.inner = [0] * 4
        self.state = 0
    # */

    def set_state_default(self):
        if self.state == 0: return
        self.state = 0
        self.color = COL_box_button
        self.color_rim = COL_box_button_rim
        #|
    def set_state_focus(self):
        if self.state == 1: return
        self.state = 1
        self.color = COL_box_button_fo
        self.color_rim = COL_box_button_rim_fo
        #|
    def set_state_press(self):
        if self.state == 2: return
        self.state = 2
        self.color = COL_box_button_active
        self.color_rim = COL_box_button_rim_active
        #|

    def is_dark(self):
        if self.__class__ is GpuButton: return False
        return True
        #|
    def dark(self):
        self.state = 0
        self.color = COL_box_button_ignore
        self.color_rim = COL_box_button_rim_ignore
        self.__class__ = GpuButtonDark
        #|
    def light(self):
        self.state = 0
        self.color = COL_box_button
        self.color_rim = COL_box_button_rim
        self.__class__ = GpuButton
        #|

    def upd(self):
        # <<< 1copy (0blg_GpuButton_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_BUTTON'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BUTTON)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def bind_draw(self):
        GL_BUTTON_bind()
        GL_BUTTON_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BUTTON_uniform_float("color", self.color)
        GL_BUTTON_uniform_float("color_rim", self.color_rim)
        GL_BUTTON_uniform_int("inner", self.inner)
        GL_BUTTON_uniform_int("state", self.state)
        self.batdraw()
        #|

    def LRBT(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        #|
    def LRBT_upd(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        # <<< 1copy (0blg_GpuButton_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_BUTTON'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BUTTON)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuButton_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_BUTTON'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BUTTON)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuButton_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_BUTTON'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BUTTON)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuButton_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_BUTTON'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_BUTTON)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    #|
    #|
class GpuButtonDark(GpuButton):
    __slots__ = ()

    def set_state_default(self): pass
    def set_state_focus(self): pass
    def set_state_press(self): pass
    #|
    #|
class GpuButtonBool(GpuButton):
    __slots__ = ()

    # <<< 1copy (0blg_GpuButton_init,, ${
    #     'COL_box_button': 'COL_box_buttonoff',
    #     'COL_box_button_rim': 'COL_box_buttonoff_rim',
    # }$)
    def __init__(self, L=0, R=0, B=0, T=0, d=0):
        self.color = COL_box_buttonoff
        self.color_rim = COL_box_buttonoff_rim
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.d = d
        self.inner = [0] * 4
        self.state = 0
    # >>>

    def set_state_off(self):
        if self.state == 0: return
        self.state = 0
        self.color = COL_box_buttonoff
        self.color_rim = COL_box_buttonoff_rim
        #|
    def set_state_off_focus(self):
        if self.state == 1: return
        self.state = 1
        self.color = COL_box_buttonoff_fo
        self.color_rim = COL_box_buttonoff_rim_fo
        #|
    def set_state_on(self):
        if self.state == 2: return
        self.state = 2
        self.color = COL_box_buttonon
        self.color_rim = COL_box_buttonon_rim
        #|
    def set_state_on_focus(self):
        if self.state == 3: return
        self.state = 3
        self.color = COL_box_buttonon_fo
        self.color_rim = COL_box_buttonon_rim_fo
        #|

    def is_dark(self):
        if self.__class__ is GpuButtonBool: return False
        return True
        #|
    def dark(self):
        if self.state in {0, 1}:
            self.color = COL_box_button_ignore
            self.state = 0
        else:
            self.color = COL_box_buttonon_ignore
            self.state = 2
        self.color_rim = COL_box_button_rim_ignore
        self.__class__ = GpuButtonBoolDark
        #|
    def light(self):
        if self.state in {0, 1}:
            self.state = 0
            self.color = COL_box_buttonoff
            self.color_rim = COL_box_buttonoff_rim
        else:
            self.state = 2
            self.color = COL_box_buttonon
            self.color_rim = COL_box_buttonon_rim
        self.__class__ = GpuButtonBool
        #|
    #|
    #|
class GpuButtonBoolDark(GpuButtonBool):
    __slots__ = ()

    def set_state_off(self):
        if self.state == 0: return
        self.state = 0
        self.color = COL_box_button_ignore
        self.color_rim = COL_box_button_rim_ignore
        #|
    def set_state_off_focus(self):
        if self.state == 1: return
        self.state = 1
        self.color = COL_box_button_ignore
        self.color_rim = COL_box_button_rim_ignore
        #|
    def set_state_on(self):
        if self.state == 2: return
        self.state = 2
        self.color = COL_box_buttonon_ignore
        self.color_rim = COL_box_button_rim_ignore
        #|
    def set_state_on_focus(self):
        if self.state == 3: return
        self.state = 3
        self.color = COL_box_buttonon_ignore
        self.color_rim = COL_box_button_rim_ignore
        #|
    #|
    #|

class GpuGrid(GpuBox):
    __slots__ = ()

    def __init__(self, L=0, R=0, B=0, T=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        #|

    def upd(self):
        # <<< 1copy (0blg_GpuGrid_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_GRID'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_GRID)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def bind_draw(self):
        GL_GRID_bind()
        GL_GRID_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_GRID_uniform_int("gridSize", SIZE_button[0])
        self.batdraw()
        #|

    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_GpuGrid_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_GRID'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_GRID)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuGrid_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_GRID'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_GRID)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuGrid_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_GRID'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_GRID)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuGrid_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_GRID'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_GRID)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def copy(self):
        out = GpuGrid(self.L, self.R, self.B, self.T)
        if hasattr(self, "batdraw"):
            out.batdraw = self.batdraw
        return out
        #|
    #|
    #|
class GpuPickerSV(GpuBox):
    __slots__ = 'hue'

    def __init__(self, L=0, R=0, B=0, T=0, hue=0.0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.hue = hue
        #|

    def upd(self):
        # <<< 1copy (0blg_GpuPickerSV_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_SV'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_SV)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def bind_draw(self):
        GL_PICKER_SV_bind()
        GL_PICKER_SV_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_PICKER_SV_uniform_float("hue", self.hue)
        GL_PICKER_SV_uniform_float("LRBT", (self.L, self.R, self.B, self.T))
        self.batdraw()
        #|

    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_GpuPickerSV_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_SV'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_SV)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuPickerSV_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_SV'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_SV)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuPickerSV_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_SV'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_SV)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuPickerSV_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_SV'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_SV)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    #|
    #|
class GpuPickerH(GpuBox):
    __slots__ = ()

    def __init__(self, L=0, R=0, B=0, T=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        #|

    def upd(self):
        # <<< 1copy (0blg_GpuPickerH_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_H'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_H)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def bind_draw(self):
        GL_PICKER_H_bind()
        GL_PICKER_H_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_PICKER_H_uniform_float("LRBT", (self.L, self.R, self.B, self.T))
        self.batdraw()
        #|

    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_GpuPickerH_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_H'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_H)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuPickerH_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_H'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_H)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuPickerH_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_H'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_H)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuPickerH_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_PICKER_H'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_PICKER_H)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    #|
    #|
class GpuSelection(GpuBox):
    __slots__ = 'd', 'inner', 'color_rim', 'state', 'gpubox'

    def __init__(self, L=0, R=0, B=0, T=0, d=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.d = d
        self.inner = [0] * 4
        self.color = COL_box_selectbox_rim
        self.color_rim = COL_box_selectbox_gap
        self.state = 0

        self.gpubox = GpuBox(COL_box_selectbox_bg)
        #|

    def upd(self):
        # <<< 1copy (0blg_GpuSelection_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        if L > R: L, R = R, L
        if B > T: B, T = T, B

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SELECTION)
        self.batdraw = batch.draw

        L += d
        R -= d
        B += d
        T -= d
        if R <= L: R = L + 1
        if T <= B: T = B + 1

        e = self.inner
        e[0] = L
        e[1] = R
        e[2] = B
        e[3] = T

        self.gpubox.LRBT_upd(L, R, B, T)
        # >>>
        #|

    def set_state(self, state):
        if state == 0:
            self.state = 0
            self.color = COL_box_selectbox_rim
            self.color_rim = COL_box_selectbox_gap
            self.gpubox.color = COL_box_selectbox_bg
        else:
            self.state = 1
            self.color = COL_box_selectbox_subtract_rim
            self.color_rim = COL_box_selectbox_subtract_gap
            self.gpubox.color = COL_box_selectbox_subtract_bg
        #|

    def bind_draw(self):
        self.gpubox.bind_draw()
        GL_SELECTION_bind()
        GL_SELECTION_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_SELECTION_uniform_float("color", self.color)
        GL_SELECTION_uniform_float("color_rim", self.color_rim)
        GL_SELECTION_uniform_int("inner", self.inner)
        GL_SELECTION_uniform_int("gapSize", SIZE_filter[3])
        self.batdraw()
        #|

    def LRBT(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        #|
    def LRBT_upd(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        # <<< 1copy (0blg_GpuSelection_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        if L > R: L, R = R, L
        if B > T: B, T = T, B

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SELECTION)
        self.batdraw = batch.draw

        L += d
        R -= d
        B += d
        T -= d
        if R <= L: R = L + 1
        if T <= B: T = B + 1

        e = self.inner
        e[0] = L
        e[1] = R
        e[2] = B
        e[3] = T

        self.gpubox.LRBT_upd(L, R, B, T)
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuSelection_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        if L > R: L, R = R, L
        if B > T: B, T = T, B

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SELECTION)
        self.batdraw = batch.draw

        L += d
        R -= d
        B += d
        T -= d
        if R <= L: R = L + 1
        if T <= B: T = B + 1

        e = self.inner
        e[0] = L
        e[1] = R
        e[2] = B
        e[3] = T

        self.gpubox.LRBT_upd(L, R, B, T)
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuSelection_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        if L > R: L, R = R, L
        if B > T: B, T = T, B

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SELECTION)
        self.batdraw = batch.draw

        L += d
        R -= d
        B += d
        T -= d
        if R <= L: R = L + 1
        if T <= B: T = B + 1

        e = self.inner
        e[0] = L
        e[1] = R
        e[2] = B
        e[3] = T

        self.gpubox.LRBT_upd(L, R, B, T)
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuSelection_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        if L > R: L, R = R, L
        if B > T: B, T = T, B

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SELECTION)
        self.batdraw = batch.draw

        L += d
        R -= d
        B += d
        T -= d
        if R <= L: R = L + 1
        if T <= B: T = B + 1

        e = self.inner
        e[0] = L
        e[1] = R
        e[2] = B
        e[3] = T

        self.gpubox.LRBT_upd(L, R, B, T)
        # >>>
        #|
    #|
    #|


class GpuWin(GpuBox):
    __slots__ = 'title_B'

    def __init__(self, L=0, R=0, B=0, T=0, title_B=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.title_B = title_B
        self.color = COL_win_title
        #|

    def upd(self):
        # <<< 1copy (0blg_Win_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_WIN'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_WIN)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    # <<< 1copy (0blg_Win_bind_draw,, $$)
    def bind_draw(self):
        GL_WIN_bind()
        GL_WIN_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_WIN_uniform_float("color", COL_win)
        GL_WIN_uniform_float("color_title", self.color)
        GL_WIN_uniform_int("title_B", self.title_B)
        self.batdraw()
    # >>>

    def LRBT(self, L, R, B, T, title_B):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.title_B = title_B
        #|
    def LRBT_upd(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.title_B = title_B
        # <<< 1copy (0blg_Win_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_WIN'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_WIN)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def dy(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        self.title_B += dy
        #|
    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Win_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_WIN'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_WIN)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        self.title_B += dy

        # <<< 1copy (0blg_Win_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_WIN'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_WIN)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        self.title_B += dy

        # <<< 1copy (0blg_Win_upd,, $$)
        # <<< 1copy (0defBox_upd,, ${'_shader_':'GL_WIN'}$)
        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.R, self.T), (self.L, self.T), (self.L, self.B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_WIN)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    #|
    #|
class GpuDropDown(GpuWin):
    __slots__ = ()
    #|
    # <<< 1copy (0blg_Win_bind_draw,, ${'COL_win':'COL_dd', 'self.color':'COL_dd_title'}$)
    def bind_draw(self):
        GL_WIN_bind()
        GL_WIN_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_WIN_uniform_float("color", COL_dd)
        GL_WIN_uniform_float("color_title", COL_dd_title)
        GL_WIN_uniform_int("title_B", self.title_B)
        self.batdraw()
    # >>>
    #|
class GpuWinRim(GpuRim):
    __slots__ = ()

    def __init__(self, L=0, R=0, B=0, T=0, d=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.d = d
        self.inner = [0] * 4
        #|

    # <<< 1copy (0blg_WinRim_bind_draw,, $$)
    def bind_draw(self):
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", FLO_0000)
        GL_RIM_uniform_float("color_rim", COL_win_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
    # >>>
    #|
    #|
class GpuDropDownRim(GpuWinRim):
    __slots__ = ()

    # <<< 1copy (0blg_WinRim_bind_draw,, ${'COL_win_rim':'COL_dd_rim'}$)
    def bind_draw(self):
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", FLO_0000)
        GL_RIM_uniform_float("color_rim", COL_dd_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
    # >>>
    #|
    #|
class GpuRimArea(GpuWinRim):
    __slots__ = ()

    # <<< 1copy (0blg_WinRim_bind_draw,, ${
    #     'COL_win_rim': 'COL_box_area_region_rim',
    #     'FLO_0000': 'COL_box_area_region'}$)
    def bind_draw(self):
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", COL_box_area_region)
        GL_RIM_uniform_float("color_rim", COL_box_area_region_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
    # >>>
    #|
    #|
class GpuRimAreaHover(GpuWinRim):
    __slots__ = ()

    # <<< 1copy (0blg_WinRim_bind_draw,, ${
    #     'COL_win_rim': 'COL_box_area_hover_rim',
    #     'FLO_0000': 'COL_box_area_hover'}$)
    def bind_draw(self):
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", COL_box_area_hover)
        GL_RIM_uniform_float("color_rim", COL_box_area_hover_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
    # >>>
    #|
    #|
class GpuRimBlfbuttonTextHover(GpuWinRim):
    __slots__ = ()

    # <<< 1copy (0blg_WinRim_bind_draw,, ${
    #     'COL_win_rim': 'COL_box_blfbutton_text_hover_rim',
    #     'FLO_0000': 'COL_box_blfbutton_text_hover'}$)
    def bind_draw(self):
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", COL_box_blfbutton_text_hover)
        GL_RIM_uniform_float("color_rim", COL_box_blfbutton_text_hover_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
    # >>>
    #|
    #|
class GpuRimSettingTabActive(GpuWinRim):
    __slots__ = ()

    # <<< 1copy (0blg_WinRim_bind_draw,, ${
    #     'COL_win_rim': 'COL_box_setting_list_active_rim',
    #     'FLO_0000': 'COL_box_setting_list_active'}$)
    def bind_draw(self):
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", COL_box_setting_list_active)
        GL_RIM_uniform_float("color_rim", COL_box_setting_list_active_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
    # >>>
    #|
    #|
class GpuShadow(GpuRim):
    __slots__ = ()

    def __init__(self, L=0, R=0, B=0, T=0, d=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.d = d
        self.inner = [0] * 4
        #|

    # <<< 1copy (0blg_Shadow_bind_draw,, $$)
    def bind_draw(self):
        GL_SHADOW_bind()
        GL_SHADOW_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_SHADOW_uniform_float("color", COL_win_shadow)
        GL_SHADOW_uniform_int("inner", self.inner)
        GL_SHADOW_uniform_int("d", self.d)
        self.batdraw()
    # >>>

    def upd(self):
        # <<< 1copy (0blg_Shadow_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_SHADOW'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SHADOW)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def LRBT_upd(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        # <<< 1copy (0blg_Shadow_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_SHADOW'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SHADOW)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Shadow_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_SHADOW'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SHADOW)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Shadow_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_SHADOW'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SHADOW)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Shadow_upd,, $$)
        # <<< 1copy (0defRim_upd,, ${'_shader_':'GL_SHADOW'}$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        # doublE speeD oF [:] = ..
        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_SHADOW)
        self.batdraw = batch.draw
        # >>>
        # >>>
        #|
    #|
    #|
class GpuShadowDropDown(GpuShadow):
    __slots__ = ()

    # <<< 1copy (0blg_Shadow_bind_draw,, ${'COL_win_shadow':'COL_dd_shadow'}$)
    def bind_draw(self):
        GL_SHADOW_bind()
        GL_SHADOW_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_SHADOW_uniform_float("color", COL_dd_shadow)
        GL_SHADOW_uniform_int("inner", self.inner)
        GL_SHADOW_uniform_int("d", self.d)
        self.batdraw()
    # >>>
    #|
    #|

class GpuBox_box_tb(GpuBox):
    __slots__ = ()

    def __init__(self, L=0, R=0, B=0, T=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        #|

    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_box_tb'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_box_tb)
        self.batdraw()
    # >>>
    #|
    #|
class GpuBox_box_tb_multibar(GpuBox_box_tb):
    __slots__ = ()
    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_box_tb_multibar'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_box_tb_multibar)
        self.batdraw()
    # >>>
    #|
    #|
class GpuBox_area(GpuBox_box_tb):
    __slots__ = ()
    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_area'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_area)
        self.batdraw()
    # >>>
    #|
    #|
class GpuBox_block(GpuBox_box_tb):
    __slots__ = ()
    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_block'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_block)
        self.batdraw()
    # >>>
    #|
class GpuBox_box_filter_active_bg(GpuBox_box_tb):
    __slots__ = ()
    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_box_filter_active_bg'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_box_filter_active_bg)
        self.batdraw()
    # >>>
    #|
class GpuBox_box_filter_select_bg(GpuBox_box_tb):
    __slots__ = ()
    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_box_filter_select_bg'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_box_filter_select_bg)
        self.batdraw()
    # >>>
    #|
class GpuBox_box_filter_hover_bg(GpuBox_box_tb):
    __slots__ = ()
    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_box_filter_hover_bg'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_box_filter_hover_bg)
        self.batdraw()
    # >>>
    #|
class GpuBox_box_setting_list_bg(GpuBox_box_tb):
    __slots__ = ()
    # <<< 1copy (0blg_Box_bind_draw,, ${'self.color':'COL_box_setting_list_bg'}$)
    def bind_draw(self):
        GL_BOX_bind()
        GL_BOX_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_BOX_uniform_float("color", COL_box_setting_list_bg)
        self.batdraw()
    # >>>
    #|

class GpuCheckbox(GpuRim):
    __slots__ = 'bat2draw', 'value'

    def __init__(self, L=0, R=0, B=0, T=0, d=0, value=False):
        self.color = COL_box_val_bool
        self.color_rim = COL_box_val_bool_rim
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        self.d = d
        self.inner = [0] * 4
        self.value = value
        #|

    def is_dark(self):
        if self.__class__ is GpuCheckbox: return False
        return True
        #|
    def dark(self):
        self.color = COL_box_val_bool_ignore
        self.color_rim = COL_box_val_bool_rim_ignore
        self.__class__ = GpuCheckboxDark
        #|
    def light(self):
        self.color = COL_box_val_bool
        self.color_rim = COL_box_val_bool_rim
        self.__class__ = GpuCheckbox
        #|

    def upd(self):
        # <<< 1copy (0blg_GpuCheckbox_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw

        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (L, T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.bat2draw = batch.draw
        # >>>
        #|

    def bind_draw(self):
        # <<< 1copy (0blg_GpuRim_bind_draw,, $$)
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", self.color)
        GL_RIM_uniform_float("color_rim", self.color_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
        # >>>

        if self.value:
            # <<< 1copy (0blg_GpuImg_bind_draw,, ${'self.batdraw':'self.bat2draw', 'TEXTURE_ACTIVE':'IM_checkbox_fg'}$)
            GL_IMG_bind()
            GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
            GL_IMG_uniform_sampler("image", IM_checkbox_fg)
            self.bat2draw()
            # >>>
        #|

    def LRBT_upd(self, L, R, B, T, d):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        self.d = d
        # <<< 1copy (0blg_GpuCheckbox_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw

        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (L, T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.bat2draw = batch.draw
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuCheckbox_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw

        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (L, T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.bat2draw = batch.draw
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuCheckbox_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw

        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (L, T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.bat2draw = batch.draw
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuCheckbox_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        d = self.d

        e = self.inner
        e[0] = L + d
        e[1] = R - d
        e[2] = B + d
        e[3] = T - d

        vbo = GPUVertBuf(VBO_FORMAT_position_F32_FLOAT, 6)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (R, T), (L, T), (L, B)))
        batch = GPUBatch(type='TRIS', buf=vbo)
        batch.program_set(GL_RIM)
        self.batdraw = batch.draw

        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((L, B), (R, B), (R, T), (L, T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.bat2draw = batch.draw
        # >>>
        #|
    #|
    #|
class GpuCheckboxDark(GpuCheckbox):
    __slots__ = ()

    def bind_draw(self):
        # <<< 1copy (0blg_GpuRim_bind_draw,, $$)
        GL_RIM_bind()
        GL_RIM_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_RIM_uniform_float("color", self.color)
        GL_RIM_uniform_float("color_rim", self.color_rim)
        GL_RIM_uniform_int("inner", self.inner)
        self.batdraw()
        # >>>

        if self.value:
            # <<< 1copy (0blg_GpuImg_bind_draw,, ${'self.batdraw':'self.bat2draw', 'TEXTURE_ACTIVE':'IM_checkbox_fg_disable'}$)
            GL_IMG_bind()
            GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
            GL_IMG_uniform_sampler("image", IM_checkbox_fg_disable)
            self.bat2draw()
            # >>>
        #|
    #|
    #|

class GpuScreenDash:
    __slots__ = 'color', 'color2', 'coords', 'batdraw'

    def __init__(self, color, color2, coords):
        self.color = color
        self.color2 = color2
        self.coords = coords
        #|

    def upd(self):
        vbo = GPUVertBuf(VBO_FORMAT_pos_F32_3_FLOAT, 2)
        vbo.attr_fill('pos', self.coords)
        batch = GPUBatch(type='LINES', buf=vbo)
        batch.program_set(GL_SCREENDASH_3D)
        self.batdraw = batch.draw
        #|

    def bind_draw(self):
        GL_SCREENDASH_3D_bind()
        GL_SCREENDASH_3D_uniform_float("ModelViewProjectionMatrix", CONTEXT.region_data.perspective_matrix)
        GL_SCREENDASH_3D_uniform_float("viewport_size", (CONTEXT.region.width, CONTEXT.region.height))
        GL_SCREENDASH_3D_uniform_float("dash_width", SIZE_preview[0])
        GL_SCREENDASH_3D_uniform_float("color", self.color)
        GL_SCREENDASH_3D_uniform_float("color2", self.color2)
        self.batdraw()
        #|
    #|
    #|

def draw_angle_arc(angle, segments, color):
    mul = (1.0 / (segments - 1)) * angle

    vbo = GPUVertBuf(VBO_FORMAT_pos_F32_2_FLOAT, segments)
    vbo.attr_fill('pos', [(sin(i * mul), cos(i * mul)) for i in range(segments)])

    BUILTIN_SHADER_UNIFORM_COLOR_bind()
    BUILTIN_SHADER_UNIFORM_COLOR_uniform_float("color", color)
    GPUBatch(type='LINE_STRIP', buf=vbo).draw(BUILTIN_SHADER_UNIFORM_COLOR)
    #|


class GpuImg(GpuBox):
    __slots__ = 'cls'

    def __init__(self, L=0, R=0, B=0, T=0):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        #|

    def upd(self):
        # <<< 1copy (0blg_Img_upd,, $$)
        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.L, self.T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.batdraw = batch.draw
        # >>>
        #|

    def r_draw_state(self): return True
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg
            return True
        #|
    def bind_draw(self):
        # <<< 1copy (0blg_GpuImg_bind_draw,, $$)
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", TEXTURE_ACTIVE)
        self.batdraw()
        # >>>
        #|

    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_Img_upd,, $$)
        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.L, self.T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.batdraw = batch.draw
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Img_upd,, $$)
        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.L, self.T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.batdraw = batch.draw
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Img_upd,, $$)
        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.L, self.T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.batdraw = batch.draw
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_Img_upd,, $$)
        vbo = GPUVertBuf(VBO_FORMAT_position_uv_F32_FLOAT, 4)
        vbo.attr_fill('position', ((self.L, self.B), (self.R, self.B), (self.R, self.T), (self.L, self.T)))
        vbo.attr_fill('uv', GPUIMGUV)
        batch = GPUBatch(type='TRI_FAN', buf=vbo)
        batch.program_set(GL_IMG)
        self.batdraw = batch.draw
        # >>>
        #|
    #|
    #|
class GpuImgUtil(GpuImg):
    __slots__ = 'gpu_texture'

    def __init__(self, image):
        self.gpu_texture = from_image(image)
        #|

    def bind_draw(self):
        # <<< 1copy (0blg_GpuImg_bind_draw,, ${'TEXTURE_ACTIVE':'self.gpu_texture'}$)
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", self.gpu_texture)
        self.batdraw()
        # >>>
        #|
    #|
class GpuImgNull(GpuImg):
    __slots__ = ()

    def r_draw_state(self): return False
    def set_draw_state(self, boo):
        if boo:
            self.__class__ = self.cls
            return True
        return False
        #|
    def bind_draw(self): pass
    #|
    #|
class GpuImgSlot2(GpuBox):
    __slots__ = 'slot0', 'slot1', 'max_index', 'identifier'

    def __init__(self, slot0, slot1, L=0, R=0, B=0, T=0):
        self.slot0 = slot0
        self.slot1 = slot1
        self.max_index = 1
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        #|

    def upd(self):
        # /* 0blg_GpuImgSlot2_upd
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L + h, R + h, B, T)
        # */

    def bind_draw(self):
        self.slot0.bind_draw()
        self.slot1.bind_draw()
        #|

    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_GpuImgSlot2_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L + h, R + h, B, T)
        # >>>
        #|

    def inbox(self, mouse):
        return self.L <= mouse[0] < self.R + self.max_index * (self.T - self.B) and self.B <= mouse[1] < self.T
        #|
    def out_R(self, mouse):
        return self.R + self.max_index * (self.T - self.B) <= mouse[0]
        #|
    def in_R(self, mouse):
        return mouse[0] < self.R + self.max_index * (self.T - self.B)
        #|
    def in_LR(self, mouse):
        return self.L <= mouse[0] < self.R + self.max_index * (self.T - self.B)
        #|
    def r_w(self):
        return self.R + self.max_index * (self.T - self.B) - self.L
        #|
    def r_center_x(self):
        return self.L + (self.R + self.max_index * (self.T - self.B) - self.L - self.L) // 2
        #|
    def r_center_x_float(self):
        return self.L + (self.R + self.max_index * (self.T - self.B) - self.L - self.L) / 2
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuImgSlot2_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L + h, R + h, B, T)
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuImgSlot2_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L + h, R + h, B, T)
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuImgSlot2_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L + h, R + h, B, T)
        # >>>
        #|
    #|
    #|

class GpuImgSlotModifierRVEC(GpuBox):
    __slots__ = 'slot0', 'slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7'

    def __init__(self, anim_data, modifier):
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        #|
    def update_slot(self, anim_data, modifier):
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):
                self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")

            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_ON:
                self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_ON

        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):
                self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")

            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_OFF:
                self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_OFF


        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):
                self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")

            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:
                self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON

        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):
                self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")

            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:
                self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF


        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):
                self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")

            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:
                self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON

        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):
                self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")

            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:
                self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF


        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):
                self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render")

            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:
                self.slot7.__class__ = GpuImg_SHOW_RENDER_ON

        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):
                self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render")

            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:
                self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF

        #|

    def upd(self):
        # /* 0blg_GpuImgSlotModifier_upd
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B + SIZE_border[3]

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot2.LRBT_upd(L, R, B, T)
        self.slot3.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot4.LRBT_upd(L, R, B, T)
        self.slot5.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot6.LRBT_upd(L, R, B, T)
        self.slot7.LRBT_upd(L, R, B, T)
        # */

    def bind_draw(self):
        self.slot0.bind_draw()
        self.slot2.bind_draw()
        self.slot4.bind_draw()
        self.slot6.bind_draw()
        self.slot1.bind_draw()
        self.slot3.bind_draw()
        self.slot5.bind_draw()
        self.slot7.bind_draw()
        #|

    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_GpuImgSlotModifier_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B + SIZE_border[3]

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot2.LRBT_upd(L, R, B, T)
        self.slot3.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot4.LRBT_upd(L, R, B, T)
        self.slot5.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot6.LRBT_upd(L, R, B, T)
        self.slot7.LRBT_upd(L, R, B, T)
        # >>>
        #|

    def inbox(self, mouse):
        return self.L <= mouse[0] < self.R + 3 * (self.T - self.B + SIZE_border[3]) and self.B <= mouse[1] < self.T
        #|
    def out_R(self, mouse):
        return self.R + 3 * (self.T - self.B + SIZE_border[3]) <= mouse[0]
        #|
    def in_R(self, mouse):
        return mouse[0] < self.R + 3 * (self.T - self.B + SIZE_border[3])
        #|
    def in_LR(self, mouse):
        return self.L <= mouse[0] < self.R + 3 * (self.T - self.B + SIZE_border[3])
        #|
    def r_w(self):
        return self.R + 3 * (self.T - self.B + SIZE_border[3]) - self.L
        #|
    def r_center_x(self):
        return self.L + (self.R + 3 * (self.T - self.B + SIZE_border[3]) - self.L - self.L) // 2
        #|
    def r_center_x_float(self):
        return self.L + (self.R + 3 * (self.T - self.B + SIZE_border[3]) - self.L - self.L) / 2
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuImgSlotModifier_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B + SIZE_border[3]

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot2.LRBT_upd(L, R, B, T)
        self.slot3.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot4.LRBT_upd(L, R, B, T)
        self.slot5.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot6.LRBT_upd(L, R, B, T)
        self.slot7.LRBT_upd(L, R, B, T)
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuImgSlotModifier_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B + SIZE_border[3]

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot2.LRBT_upd(L, R, B, T)
        self.slot3.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot4.LRBT_upd(L, R, B, T)
        self.slot5.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot6.LRBT_upd(L, R, B, T)
        self.slot7.LRBT_upd(L, R, B, T)
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuImgSlotModifier_upd,, $$)
        L = self.L
        R = self.R
        B = self.B
        T = self.T
        h = T - B + SIZE_border[3]

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot2.LRBT_upd(L, R, B, T)
        self.slot3.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot4.LRBT_upd(L, R, B, T)
        self.slot5.LRBT_upd(L, R, B, T)
        L += h
        R += h
        self.slot6.LRBT_upd(L, R, B, T)
        self.slot7.LRBT_upd(L, R, B, T)
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierRVE(GpuImgSlotModifierRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierRVE_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierRVE_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierRV(GpuImgSlotModifierRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierRV_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierRV_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifier(GpuImgSlotModifierRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifier_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifier_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|

class GpuImgSlotModifierOverrideRVEC(GpuImgSlotModifierRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideRVEC_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideRVEC_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_ON:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_OFF:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverrideRVE(GpuImgSlotModifierOverrideRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideRVE_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideRVE_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverrideRV(GpuImgSlotModifierOverrideRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideRV_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideRV_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverride(GpuImgSlotModifierOverrideRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverride_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverride_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|

class GpuImgSlotModifierSystemOverrideRVEC(GpuImgSlotModifierOverrideRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideRVEC_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideRVEC_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_ON:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_OFF:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverrideRVE(GpuImgSlotModifierSystemOverrideRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideRVE_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideRVE_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverrideRV(GpuImgSlotModifierSystemOverrideRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideRV_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideRV_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverride(GpuImgSlotModifierSystemOverrideRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverride_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage")()
            self.slot1 = GpuImg_SHOW_ON_CAGE_DISABLE()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverride_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.show_on_cage:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_on_cage") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_SHOW_ON_CAGE_DISABLE:             self.slot1.__class__ = GpuImg_SHOW_ON_CAGE_DISABLE ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|

class GpuImgSlotModifierSplineRVES(GpuImgSlotModifierRVEC):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSplineRVES_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSplineRVES_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSplineRVE(GpuImgSlotModifierSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSplineRVE_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSplineRVE_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSplineRVS(GpuImgSlotModifierSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSplineRVS_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSplineRVS_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSplineRV(GpuImgSlotModifierSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSplineRV_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSplineRV_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSplineS(GpuImgSlotModifierSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSplineS_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSplineS_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSpline(GpuImgSlotModifierSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSpline_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSpline_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|

class GpuImgSlotModifierOverrideSplineRVES(GpuImgSlotModifierSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideSplineRVES_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideSplineRVES_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverrideSplineRVE(GpuImgSlotModifierOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideSplineRVE_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideSplineRVE_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverrideSplineRVS(GpuImgSlotModifierOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideSplineRVS_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideSplineRVS_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverrideSplineRV(GpuImgSlotModifierOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideSplineRV_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideSplineRV_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverrideSplineS(GpuImgSlotModifierOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideSplineS_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideSplineS_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierOverrideSpline(GpuImgSlotModifierOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierOverrideSpline_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierOverrideSpline_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|

class GpuImgSlotModifierSystemOverrideSplineRVES(GpuImgSlotModifierOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideSplineRVES_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideSplineRVES_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverrideSplineRVE(GpuImgSlotModifierSystemOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideSplineRVE_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_ON()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_OFF()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideSplineRVE_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_ON:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_ON ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_OFF:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_OFF ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverrideSplineRVS(GpuImgSlotModifierSystemOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideSplineRVS_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideSplineRVS_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverrideSplineRV(GpuImgSlotModifierSystemOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideSplineRV_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_ON()
        else:
            self.slot4 = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_OFF()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_ON()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_OFF()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideSplineRV_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_ON:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_ON ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off_override(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_OFF:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_OFF ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_ON:             self.slot7.__class__ = GpuImg_SHOW_RENDER_ON ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_OFF:             self.slot7.__class__ = GpuImg_SHOW_RENDER_OFF ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverrideSplineS(GpuImgSlotModifierSystemOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideSplineS_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_ON()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImg_USE_APPLY_ON_SPLINE_OFF()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideSplineS_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_ON:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_ON ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImg_USE_APPLY_ON_SPLINE_OFF:             self.slot1.__class__ = GpuImg_USE_APPLY_ON_SPLINE_OFF ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|
class GpuImgSlotModifierSystemOverrideSpline(GpuImgSlotModifierSystemOverrideSplineRVES):
    __slots__ = ()

    def __init__(self, anim_data, modifier):
        # /* 0blg_GpuImgSlotModifierSystemOverrideSpline_init
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            self.slot0 = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()
        else:
            self.slot0 = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline")()
            self.slot1 = GpuImgNull()

        if modifier.show_in_editmode:
            self.slot2 = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()
        else:
            self.slot2 = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode")()
            self.slot3 = GpuImg_SHOW_IN_EDITMODE_DISABLE()

        if modifier.show_viewport:
            self.slot4 = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()
        else:
            self.slot4 = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport")()
            self.slot5 = GpuImg_SHOW_VIEWPORT_DISABLE()

        if modifier.show_render:
            self.slot6 = r_modifier_button_BG_on(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        else:
            self.slot6 = r_modifier_button_BG_off(anim_data, dp_head + "show_render")()
            self.slot7 = GpuImg_SHOW_RENDER_DISABLE()
        # */
    def update_slot(self, anim_data, modifier):
        # <<< 1ifmatch (0blg_GpuImgSlotModifierSystemOverrideSpline_init,,
        #     $lambda line: (line.split(" = ")[0].replace("self.", "if self.") + ".__class__ is not " + line.split(" = ")[1].replace("()", ": ").replace("\n", "") + line.split(" = ")[0] + ".__class__ = " + line.split(" = ")[1].replace("()", " ;print('||blg slot changed')"), True)$,
        #     $lambda line: (line, True)$,
        #     ${'self.'}$)
        dp_head = f'modifiers["{escape_identifier(modifier.name)}"].'

        if modifier.use_apply_on_spline:
            if self.slot0.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')
        else:
            if self.slot0.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline"):             self.slot0.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "use_apply_on_spline") ;print('||blg slot changed')
            if self.slot1.__class__ is not GpuImgNull:             self.slot1.__class__ = GpuImgNull ;print('||blg slot changed')

        if modifier.show_in_editmode:
            if self.slot2.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')
        else:
            if self.slot2.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode"):             self.slot2.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_in_editmode") ;print('||blg slot changed')
            if self.slot3.__class__ is not GpuImg_SHOW_IN_EDITMODE_DISABLE:             self.slot3.__class__ = GpuImg_SHOW_IN_EDITMODE_DISABLE ;print('||blg slot changed')

        if modifier.show_viewport:
            if self.slot4.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')
        else:
            if self.slot4.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_viewport"):             self.slot4.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_viewport") ;print('||blg slot changed')
            if self.slot5.__class__ is not GpuImg_SHOW_VIEWPORT_DISABLE:             self.slot5.__class__ = GpuImg_SHOW_VIEWPORT_DISABLE ;print('||blg slot changed')

        if modifier.show_render:
            if self.slot6.__class__ is not r_modifier_button_BG_on(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_on(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        else:
            if self.slot6.__class__ is not r_modifier_button_BG_off(anim_data, dp_head + "show_render"):             self.slot6.__class__ = r_modifier_button_BG_off(anim_data, dp_head + "show_render") ;print('||blg slot changed')
            if self.slot7.__class__ is not GpuImg_SHOW_RENDER_DISABLE:             self.slot7.__class__ = GpuImg_SHOW_RENDER_DISABLE ;print('||blg slot changed')
        # >>>
        #|
    #|
    #|


class GpuImgSlotDriverVar(GpuImgSlotModifierRVEC):
    __slots__ = ()

    def __init__(self, anim_data=None, modifier=None):
        self.slot0 = GpuImgNull
        self.slot1 = GpuImgNull
        self.slot2 = GpuImgNull
        self.slot3 = GpuImgNull
        self.slot4 = GpuImgNull
        self.slot5 = GpuImgNull
        self.slot6 = GpuImgNull
        self.slot7 = GpuImgNull
        #|

    def update_slot(self, anim_data, modifier): pass
    def upd(self): pass
    def bind_draw(self): pass
    def LRBT_upd(self, L, R, B, T): pass
    def dx_upd(self, dx): pass
    def dy_upd(self, dy): pass
    def dxy_upd(self, dx, dy): pass
    #|
    #|

class GpuImgSlotEye(GpuBox):
    __slots__ = 'slot0', 'slot1'

    def __init__(self, enabled, anim_state):
        if enabled:
            if anim_state == 0:
                self.slot0 = GpuImg_MD_BG_SHOW_ON()
            elif anim_state == 1:
                self.slot0 = GpuImg_MD_BG_SHOW_ON_KEYFRAME()
            else:
                self.slot0 = GpuImg_MD_BG_SHOW_ON_DRIVER()

            self.slot1 = GpuImg_HIDE_OFF()
        else:
            if anim_state == 0:
                self.slot0 = GpuImg_MD_BG_SHOW_OFF()
            elif anim_state == 1:
                self.slot0 = GpuImg_MD_BG_SHOW_OFF_KEYFRAME()
            else:
                self.slot0 = GpuImg_MD_BG_SHOW_OFF_DRIVER()

            self.slot1 = GpuImg_HIDE_ON()
        #|
    def update_slot(self, enabled, anim_state):
        if enabled:
            if anim_state == 0:
                if self.slot0.__class__ is GpuImg_MD_BG_SHOW_ON: pass
                else:

                    self.slot0.__class__ = GpuImg_MD_BG_SHOW_ON
            elif anim_state == 1:
                if self.slot0.__class__ is GpuImg_MD_BG_SHOW_ON_KEYFRAME: pass
                else:

                    self.slot0.__class__ = GpuImg_MD_BG_SHOW_ON_KEYFRAME
            else:
                if self.slot0.__class__ is GpuImg_MD_BG_SHOW_ON_DRIVER: pass
                else:

                    self.slot0.__class__ = GpuImg_MD_BG_SHOW_ON_DRIVER

            if self.slot1.__class__ is GpuImg_HIDE_OFF: pass
            else:

                self.slot1.__class__ = GpuImg_HIDE_OFF
        else:
            if anim_state == 0:
                if self.slot0.__class__ is GpuImg_MD_BG_SHOW_OFF: pass
                else:

                    self.slot0.__class__ = GpuImg_MD_BG_SHOW_OFF
            elif anim_state == 1:
                if self.slot0.__class__ is GpuImg_MD_BG_SHOW_OFF_KEYFRAME: pass
                else:

                    self.slot0.__class__ = GpuImg_MD_BG_SHOW_OFF_KEYFRAME
            else:
                if self.slot0.__class__ is GpuImg_MD_BG_SHOW_OFF_DRIVER: pass
                else:

                    self.slot0.__class__ = GpuImg_MD_BG_SHOW_OFF_DRIVER

            if self.slot1.__class__ is GpuImg_HIDE_ON: pass
            else:

                self.slot1.__class__ = GpuImg_HIDE_ON
        #|

    def upd(self):
        # /* 0blg_GpuImgSlotEye_upd
        L = self.L ;R = self.R ;B = self.B ;T = self.T

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        # */

    def bind_draw(self):
        self.slot0.bind_draw()
        self.slot1.bind_draw()
        #|

    def LRBT_upd(self, L, R, B, T):
        # <<< 1copy (0blg_Box_LRBT,, $$)
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        # >>>
        # <<< 1copy (0blg_GpuImgSlotEye_upd,, ${'L = self.L ;R = self.R ;B = self.B ;T = self.T':''}$)
        

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        # >>>
        #|

    def dx_upd(self, dx):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_GpuImgSlotEye_upd,, $$)
        L = self.L ;R = self.R ;B = self.B ;T = self.T

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        # >>>
        #|
    def dy_upd(self, dy):
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuImgSlotEye_upd,, $$)
        L = self.L ;R = self.R ;B = self.B ;T = self.T

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        # >>>
        #|
    def dxy_upd(self, dx, dy):
        # <<< 1copy (0blg_Box_dx,, $$)
        self.L += dx
        self.R += dx
        # >>>
        # <<< 1copy (0blg_Box_dy,, $$)
        self.B += dy
        self.T += dy
        # >>>
        # <<< 1copy (0blg_GpuImgSlotEye_upd,, $$)
        L = self.L ;R = self.R ;B = self.B ;T = self.T

        self.slot0.LRBT_upd(L, R, B, T)
        self.slot1.LRBT_upd(L, R, B, T)
        # >>>
        #|
    #|
    #|


## /* build_class
class GpuImg_ADD(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ADD)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ADD
            return True
class GpuImg_ADD_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ADD_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ADD_focus
            return True
class GpuImg_apply(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_apply)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_apply
            return True
class GpuImg_area_icon_hover(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_area_icon_hover)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_area_icon_hover
            return True
class GpuImg_ARMATURE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ARMATURE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ARMATURE
            return True
class GpuImg_ARRAY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ARRAY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ARRAY
            return True
class GpuImg_arrow_left(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_arrow_left)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_arrow_left
            return True
class GpuImg_arrow_left_disable(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_arrow_left_disable)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_arrow_left_disable
            return True
class GpuImg_arrow_right(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_arrow_right)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_arrow_right
            return True
class GpuImg_arrow_right_disable(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_arrow_right_disable)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_arrow_right_disable
            return True
class GpuImg_arrow_up(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_arrow_up)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_arrow_up
            return True
class GpuImg_arrow_up_disable(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_arrow_up_disable)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_arrow_up_disable
            return True
class GpuImg_ASSET_MANAGER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ASSET_MANAGER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ASSET_MANAGER
            return True
class GpuImg_assign(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_assign)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_assign
            return True
class GpuImg_BEVEL(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_BEVEL)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_BEVEL
            return True
class GpuImg_BONE_DATA(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_BONE_DATA)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_BONE_DATA
            return True
class GpuImg_BOOLEAN(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_BOOLEAN)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_BOOLEAN
            return True
class GpuImg_BUILD(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_BUILD)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_BUILD
            return True
class GpuImg_cache_layer(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_cache_layer)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_cache_layer
            return True
class GpuImg_CAST(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_CAST)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_CAST
            return True
class GpuImg_checkbox_fg(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_checkbox_fg)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_checkbox_fg
            return True
class GpuImg_checkbox_fg_disable(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_checkbox_fg_disable)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_checkbox_fg_disable
            return True
class GpuImg_CLOTH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_CLOTH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_CLOTH
            return True
class GpuImg_COLLISION(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_COLLISION)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_COLLISION
            return True
class GpuImg_context_property(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_context_property)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_context_property
            return True
class GpuImg_copy(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_copy)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_copy
            return True
class GpuImg_copy_array(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_copy_array)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_copy_array
            return True
class GpuImg_CORRECTIVE_SMOOTH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_CORRECTIVE_SMOOTH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_CORRECTIVE_SMOOTH
            return True
class GpuImg_CURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_CURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_CURVE
            return True
class GpuImg_DATA_TRANSFER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_DATA_TRANSFER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_DATA_TRANSFER
            return True
class GpuImg_DECIMATE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_DECIMATE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_DECIMATE
            return True
class GpuImg_delete(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_delete)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_delete
            return True
class GpuImg_delete_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_delete_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_delete_dark
            return True
class GpuImg_delete_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_delete_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_delete_focus
            return True
class GpuImg_Detail(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_Detail)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_Detail
            return True
class GpuImg_DISPLACE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_DISPLACE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_DISPLACE
            return True
class GpuImg_distance(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_distance)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_distance
            return True
class GpuImg_DriverEditor(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_DriverEditor)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_DriverEditor
            return True
class GpuImg_driver_ref(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_driver_ref)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_driver_ref
            return True
class GpuImg_driver_ref_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_driver_ref_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_driver_ref_dark
            return True
class GpuImg_driver_true(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_driver_true)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_driver_true
            return True
class GpuImg_driver_true_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_driver_true_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_driver_true_dark
            return True
class GpuImg_dropdown_close(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_dropdown_close)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_dropdown_close
            return True
class GpuImg_DUPLICATE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_DUPLICATE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_DUPLICATE
            return True
class GpuImg_DUPLICATE_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_DUPLICATE_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_DUPLICATE_focus
            return True
class GpuImg_DYNAMIC_PAINT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_DYNAMIC_PAINT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_DYNAMIC_PAINT
            return True
class GpuImg_EDGE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_EDGE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_EDGE
            return True
class GpuImg_EDGE_SPLIT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_EDGE_SPLIT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_EDGE_SPLIT
            return True
class GpuImg_EMPTY_AXIS(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_EMPTY_AXIS)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_EMPTY_AXIS
            return True
class GpuImg_EXPLODE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_EXPLODE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_EXPLODE
            return True
class GpuImg_eyedropper(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_eyedropper)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_eyedropper
            return True
class GpuImg_FACE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FACE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FACE
            return True
class GpuImg_FACE_CORNER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FACE_CORNER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FACE_CORNER
            return True
class GpuImg_FAKE_USER_LIB(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_LIB)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_LIB
            return True
class GpuImg_FAKE_USER_LIB_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_LIB_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_LIB_focus
            return True
class GpuImg_FAKE_USER_LINK(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_LINK)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_LINK
            return True
class GpuImg_FAKE_USER_LINK_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_LINK_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_LINK_focus
            return True
class GpuImg_FAKE_USER_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_OFF
            return True
class GpuImg_FAKE_USER_OFF_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_OFF_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_OFF_focus
            return True
class GpuImg_FAKE_USER_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_ON
            return True
class GpuImg_FAKE_USER_ON_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_ON_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_ON_focus
            return True
class GpuImg_FAKE_USER_OVERRIDE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_OVERRIDE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_OVERRIDE
            return True
class GpuImg_FAKE_USER_OVERRIDE_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FAKE_USER_OVERRIDE_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FAKE_USER_OVERRIDE_focus
            return True
class GpuImg_FILE_FOLDER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FILE_FOLDER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FILE_FOLDER
            return True
class GpuImg_FILE_FOLDER_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FILE_FOLDER_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FILE_FOLDER_focus
            return True
class GpuImg_FILE_REFRESH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FILE_REFRESH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FILE_REFRESH
            return True
class GpuImg_filter_match_active(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_filter_match_active)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_filter_match_active
            return True
class GpuImg_filter_match_case(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_filter_match_case)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_filter_match_case
            return True
class GpuImg_filter_match_end_left(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_filter_match_end_left)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_filter_match_end_left
            return True
class GpuImg_filter_match_end_right(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_filter_match_end_right)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_filter_match_end_right
            return True
class GpuImg_filter_match_hover(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_filter_match_hover)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_filter_match_hover
            return True
class GpuImg_filter_match_whole_word(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_filter_match_whole_word)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_filter_match_whole_word
            return True
class GpuImg_FLUID(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_FLUID)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_FLUID
            return True
class GpuImg_fold(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_fold)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_fold
            return True
class GpuImg_fold_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_fold_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_fold_focus
            return True
class GpuImg_GREASEPENCIL(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASEPENCIL)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASEPENCIL
            return True
class GpuImg_GREASE_PENCIL_ARMATURE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_ARMATURE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_ARMATURE
            return True
class GpuImg_GREASE_PENCIL_ARRAY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_ARRAY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_ARRAY
            return True
class GpuImg_GREASE_PENCIL_BUILD(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_BUILD)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_BUILD
            return True
class GpuImg_GREASE_PENCIL_COLOR(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_COLOR)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_COLOR
            return True
class GpuImg_GREASE_PENCIL_DASH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_DASH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_DASH
            return True
class GpuImg_GREASE_PENCIL_ENVELOPE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_ENVELOPE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_ENVELOPE
            return True
class GpuImg_GREASE_PENCIL_HOOK(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_HOOK)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_HOOK
            return True
class GpuImg_GREASE_PENCIL_LATTICE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_LATTICE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_LATTICE
            return True
class GpuImg_GREASE_PENCIL_LENGTH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_LENGTH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_LENGTH
            return True
class GpuImg_GREASE_PENCIL_MIRROR(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_MIRROR)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_MIRROR
            return True
class GpuImg_GREASE_PENCIL_MULTIPLY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_MULTIPLY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_MULTIPLY
            return True
class GpuImg_GREASE_PENCIL_NOISE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_NOISE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_NOISE
            return True
class GpuImg_GREASE_PENCIL_OFFSET(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_OFFSET)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_OFFSET
            return True
class GpuImg_GREASE_PENCIL_OPACITY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_OPACITY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_OPACITY
            return True
class GpuImg_GREASE_PENCIL_OUTLINE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_OUTLINE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_OUTLINE
            return True
class GpuImg_GREASE_PENCIL_SHRINKWRAP(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_SHRINKWRAP)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_SHRINKWRAP
            return True
class GpuImg_GREASE_PENCIL_SIMPLIFY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_SIMPLIFY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_SIMPLIFY
            return True
class GpuImg_GREASE_PENCIL_SMOOTH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_SMOOTH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_SMOOTH
            return True
class GpuImg_GREASE_PENCIL_SUBDIV(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_SUBDIV)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_SUBDIV
            return True
class GpuImg_GREASE_PENCIL_TEXTURE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_TEXTURE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_TEXTURE
            return True
class GpuImg_GREASE_PENCIL_THICKNESS(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_THICKNESS)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_THICKNESS
            return True
class GpuImg_GREASE_PENCIL_TIME(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_TIME)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_TIME
            return True
class GpuImg_GREASE_PENCIL_TINT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_TINT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_TINT
            return True
class GpuImg_GREASE_PENCIL_VERTEX_WEIGHT_ANGLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_VERTEX_WEIGHT_ANGLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_VERTEX_WEIGHT_ANGLE
            return True
class GpuImg_GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY
            return True
class GpuImg_GROUP_UVS(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GROUP_UVS)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GROUP_UVS
            return True
class GpuImg_GROUP_VCOL(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GROUP_VCOL)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GROUP_VCOL
            return True
class GpuImg_GROUP_VERTEX(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_GROUP_VERTEX)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_GROUP_VERTEX
            return True
class GpuImg_HIDE_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_HIDE_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_HIDE_OFF
            return True
class GpuImg_HIDE_OFF_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_HIDE_OFF_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_HIDE_OFF_focus
            return True
class GpuImg_HIDE_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_HIDE_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_HIDE_ON
            return True
class GpuImg_HIDE_ON_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_HIDE_ON_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_HIDE_ON_focus
            return True
class GpuImg_HOOK(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_HOOK)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_HOOK
            return True
class GpuImg_hue_button(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_hue_button)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_hue_button
            return True
class GpuImg_hue_cursor(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_hue_cursor)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_hue_cursor
            return True
class GpuImg_ID_ACTION(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_ACTION)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_ACTION
            return True
class GpuImg_ID_ARMATURE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_ARMATURE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_ARMATURE
            return True
class GpuImg_ID_BRUSH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_BRUSH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_BRUSH
            return True
class GpuImg_ID_CACHEFILE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_CACHEFILE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_CACHEFILE
            return True
class GpuImg_ID_CAMERA(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_CAMERA)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_CAMERA
            return True
class GpuImg_ID_COLLECTION(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_COLLECTION)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_COLLECTION
            return True
class GpuImg_ID_CURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_CURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_CURVE
            return True
class GpuImg_ID_CURVES(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_CURVES)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_CURVES
            return True
class GpuImg_ID_FONT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_FONT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_FONT
            return True
class GpuImg_ID_GREASEPENCIL(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_GREASEPENCIL)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_GREASEPENCIL
            return True
class GpuImg_ID_IMAGE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_IMAGE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_IMAGE
            return True
class GpuImg_ID_KEY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_KEY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_KEY
            return True
class GpuImg_ID_LATTICE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_LATTICE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_LATTICE
            return True
class GpuImg_ID_LIBRARY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_LIBRARY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_LIBRARY
            return True
class GpuImg_ID_LIGHT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_LIGHT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_LIGHT
            return True
class GpuImg_ID_LIGHT_PROBE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_LIGHT_PROBE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_LIGHT_PROBE
            return True
class GpuImg_ID_LINESTYLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_LINESTYLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_LINESTYLE
            return True
class GpuImg_ID_MASK(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_MASK)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_MASK
            return True
class GpuImg_ID_MATERIAL(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_MATERIAL)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_MATERIAL
            return True
class GpuImg_ID_MESH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_MESH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_MESH
            return True
class GpuImg_ID_META(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_META)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_META
            return True
class GpuImg_ID_MOVIECLIP(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_MOVIECLIP)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_MOVIECLIP
            return True
class GpuImg_ID_NODETREE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_NODETREE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_NODETREE
            return True
class GpuImg_ID_OBJECT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_OBJECT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_OBJECT
            return True
class GpuImg_ID_PAINTCURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_PAINTCURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_PAINTCURVE
            return True
class GpuImg_ID_PALETTE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_PALETTE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_PALETTE
            return True
class GpuImg_ID_PARTICLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_PARTICLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_PARTICLE
            return True
class GpuImg_ID_POINTCLOUD(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_POINTCLOUD)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_POINTCLOUD
            return True
class GpuImg_ID_SCENE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_SCENE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_SCENE
            return True
class GpuImg_ID_SCREEN(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_SCREEN)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_SCREEN
            return True
class GpuImg_ID_SOUND(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_SOUND)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_SOUND
            return True
class GpuImg_ID_SPEAKER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_SPEAKER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_SPEAKER
            return True
class GpuImg_ID_TEXT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_TEXT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_TEXT
            return True
class GpuImg_ID_TEXTURE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_TEXTURE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_TEXTURE
            return True
class GpuImg_ID_VOLUME(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_VOLUME)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_VOLUME
            return True
class GpuImg_ID_WINDOWMANAGER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_WINDOWMANAGER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_WINDOWMANAGER
            return True
class GpuImg_ID_WORKSPACE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_WORKSPACE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_WORKSPACE
            return True
class GpuImg_ID_WORLD(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ID_WORLD)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ID_WORLD
            return True
class GpuImg_invert(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_invert)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_invert
            return True
class GpuImg_invert_y(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_invert_y)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_invert_y
            return True
class GpuImg_IPO_CONSTANT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_IPO_CONSTANT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_IPO_CONSTANT
            return True
class GpuImg_keyframe_current_true_even(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_current_true_even)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_current_true_even
            return True
class GpuImg_keyframe_current_true_even_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_current_true_even_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_current_true_even_dark
            return True
class GpuImg_keyframe_current_true_odd(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_current_true_odd)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_current_true_odd
            return True
class GpuImg_keyframe_current_true_odd_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_current_true_odd_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_current_true_odd_dark
            return True
class GpuImg_keyframe_false(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_false)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_false
            return True
class GpuImg_keyframe_false_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_false_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_false_dark
            return True
class GpuImg_keyframe_next_false_even(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_next_false_even)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_next_false_even
            return True
class GpuImg_keyframe_next_false_even_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_next_false_even_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_next_false_even_dark
            return True
class GpuImg_keyframe_next_false_odd(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_next_false_odd)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_next_false_odd
            return True
class GpuImg_keyframe_next_false_odd_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keyframe_next_false_odd_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keyframe_next_false_odd_dark
            return True
class GpuImg_keying_set(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_keying_set)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_keying_set
            return True
class GpuImg_KeymapEditor(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_KeymapEditor)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_KeymapEditor
            return True
class GpuImg_LAPLACIANDEFORM(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LAPLACIANDEFORM)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LAPLACIANDEFORM
            return True
class GpuImg_LAPLACIANSMOOTH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LAPLACIANSMOOTH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LAPLACIANSMOOTH
            return True
class GpuImg_LATTICE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LATTICE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LATTICE
            return True
class GpuImg_LIBRARY_DATA_BROKEN(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LIBRARY_DATA_BROKEN)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LIBRARY_DATA_BROKEN
            return True
class GpuImg_LIBRARY_DATA_DIRECT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LIBRARY_DATA_DIRECT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LIBRARY_DATA_DIRECT
            return True
class GpuImg_LIBRARY_DATA_OVERRIDE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LIBRARY_DATA_OVERRIDE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LIBRARY_DATA_OVERRIDE
            return True
class GpuImg_LIBRARY_DATA_OVERRIDE_DISABLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LIBRARY_DATA_OVERRIDE_DISABLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LIBRARY_DATA_OVERRIDE_DISABLE
            return True
class GpuImg_LINCURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LINCURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LINCURVE
            return True
class GpuImg_LINEART(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_LINEART)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_LINEART
            return True
class GpuImg_manual(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_manual)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_manual
            return True
class GpuImg_MASK(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MASK)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MASK
            return True
class GpuImg_MATCUBE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MATCUBE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MATCUBE
            return True
class GpuImg_MD_BG_SHOW_HOVER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_BG_SHOW_HOVER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_BG_SHOW_HOVER
            return True
class GpuImg_MD_BG_SHOW_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_BG_SHOW_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_BG_SHOW_OFF
            return True
class GpuImg_MD_BG_SHOW_OFF_DRIVER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_BG_SHOW_OFF_DRIVER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_BG_SHOW_OFF_DRIVER
            return True
class GpuImg_MD_BG_SHOW_OFF_KEYFRAME(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_BG_SHOW_OFF_KEYFRAME)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_BG_SHOW_OFF_KEYFRAME
            return True
class GpuImg_MD_BG_SHOW_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_BG_SHOW_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_BG_SHOW_ON
            return True
class GpuImg_MD_BG_SHOW_ON_DRIVER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_BG_SHOW_ON_DRIVER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_BG_SHOW_ON_DRIVER
            return True
class GpuImg_MD_BG_SHOW_ON_KEYFRAME(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_BG_SHOW_ON_KEYFRAME)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_BG_SHOW_ON_KEYFRAME
            return True
class GpuImg_MD_LIBRARY_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_LIBRARY_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_LIBRARY_OFF
            return True
class GpuImg_MD_LIBRARY_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_LIBRARY_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_LIBRARY_ON
            return True
class GpuImg_MD_MULTI_SORT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_MULTI_SORT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_MULTI_SORT
            return True
class GpuImg_MD_OVERRIDE_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_OVERRIDE_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_OVERRIDE_OFF
            return True
class GpuImg_MD_OVERRIDE_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MD_OVERRIDE_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MD_OVERRIDE_ON
            return True
class GpuImg_MeshEditor(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MeshEditor)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MeshEditor
            return True
class GpuImg_MESH_CACHE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MESH_CACHE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MESH_CACHE
            return True
class GpuImg_MESH_DEFORM(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MESH_DEFORM)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MESH_DEFORM
            return True
class GpuImg_MESH_SEQUENCE_CACHE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MESH_SEQUENCE_CACHE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MESH_SEQUENCE_CACHE
            return True
class GpuImg_MESH_TO_VOLUME(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MESH_TO_VOLUME)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MESH_TO_VOLUME
            return True
class GpuImg_META_CUBE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_META_CUBE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_META_CUBE
            return True
class GpuImg_MIRROR(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MIRROR)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MIRROR
            return True
class GpuImg_MODIFIER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MODIFIER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MODIFIER
            return True
class GpuImg_ModifierEditor(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ModifierEditor)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ModifierEditor
            return True
class GpuImg_MULTIRES(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_MULTIRES)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_MULTIRES
            return True
class GpuImg_NOCURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_NOCURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_NOCURVE
            return True
class GpuImg_NODES(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_NODES)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_NODES
            return True
class GpuImg_NORMAL_EDIT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_NORMAL_EDIT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_NORMAL_EDIT
            return True
class GpuImg_objectpath(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_objectpath)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_objectpath
            return True
class GpuImg_OBJECT_DATA(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OBJECT_DATA)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OBJECT_DATA
            return True
class GpuImg_object_picker(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_object_picker)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_object_picker
            return True
class GpuImg_object_picker_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_object_picker_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_object_picker_dark
            return True
class GpuImg_object_picker_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_object_picker_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_object_picker_focus
            return True
class GpuImg_OCEAN(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OCEAN)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OCEAN
            return True
class GpuImg_OUTLINER_DATA_GP_LAYER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_DATA_GP_LAYER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_DATA_GP_LAYER
            return True
class GpuImg_OUTLINER_OB_ARMATURE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_ARMATURE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_ARMATURE
            return True
class GpuImg_OUTLINER_OB_CAMERA(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_CAMERA)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_CAMERA
            return True
class GpuImg_OUTLINER_OB_CURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_CURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_CURVE
            return True
class GpuImg_OUTLINER_OB_CURVES(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_CURVES)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_CURVES
            return True
class GpuImg_OUTLINER_OB_EMPTY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_EMPTY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_EMPTY
            return True
class GpuImg_OUTLINER_OB_FONT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_FONT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_FONT
            return True
class GpuImg_OUTLINER_OB_GREASEPENCIL(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_GREASEPENCIL)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_GREASEPENCIL
            return True
class GpuImg_OUTLINER_OB_LATTICE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_LATTICE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_LATTICE
            return True
class GpuImg_OUTLINER_OB_LIGHT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_LIGHT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_LIGHT
            return True
class GpuImg_OUTLINER_OB_LIGHTPROBE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_LIGHTPROBE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_LIGHTPROBE
            return True
class GpuImg_OUTLINER_OB_MESH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_MESH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_MESH
            return True
class GpuImg_OUTLINER_OB_META(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_META)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_META
            return True
class GpuImg_OUTLINER_OB_POINTCLOUD(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_POINTCLOUD)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_POINTCLOUD
            return True
class GpuImg_OUTLINER_OB_SPEAKER(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_SPEAKER)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_SPEAKER
            return True
class GpuImg_OUTLINER_OB_SURFACE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_SURFACE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_SURFACE
            return True
class GpuImg_OUTLINER_OB_UNKNOW(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_UNKNOW)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_UNKNOW
            return True
class GpuImg_OUTLINER_OB_VOLUME(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_OUTLINER_OB_VOLUME)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_OUTLINER_OB_VOLUME
            return True
class GpuImg_PARTICLE_INSTANCE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_PARTICLE_INSTANCE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_PARTICLE_INSTANCE
            return True
class GpuImg_PARTICLE_SYSTEM(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_PARTICLE_SYSTEM)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_PARTICLE_SYSTEM
            return True
class GpuImg_paste(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_paste)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_paste
            return True
class GpuImg_PHYSICS(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_PHYSICS)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_PHYSICS
            return True
class GpuImg_pin(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_pin)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_pin
            return True
class GpuImg_POINT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_POINT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_POINT
            return True
class GpuImg_py_exp_off(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_py_exp_off)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_py_exp_off
            return True
class GpuImg_py_exp_on(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_py_exp_on)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_py_exp_on
            return True
class GpuImg_REMESH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_REMESH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_REMESH
            return True
class GpuImg_REMOVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_REMOVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_REMOVE
            return True
class GpuImg_REMOVE_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_REMOVE_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_REMOVE_focus
            return True
class GpuImg_rename(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_rename)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_rename
            return True
class GpuImg_rename_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_rename_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_rename_focus
            return True
class GpuImg_reset(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_reset)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_reset
            return True
class GpuImg_reset_override(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_reset_override)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_reset_override
            return True
class GpuImg_RESTRICT_INSTANCED_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_RESTRICT_INSTANCED_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_RESTRICT_INSTANCED_ON
            return True
class GpuImg_rna(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_rna)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_rna
            return True
class GpuImg_RNDCURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_RNDCURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_RNDCURVE
            return True
class GpuImg_ROOTCURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_ROOTCURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_ROOTCURVE
            return True
class GpuImg_rotation(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_rotation)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_rotation
            return True
class GpuImg_save(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_save)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_save
            return True
class GpuImg_SCREW(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SCREW)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SCREW
            return True
class GpuImg_search(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_search)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_search
            return True
class GpuImg_SettingEditor(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SettingEditor)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SettingEditor
            return True
class GpuImg_settings_apps(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_apps)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_apps
            return True
class GpuImg_settings_keymap(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_keymap)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_keymap
            return True
class GpuImg_settings_keymap_addon_key(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_keymap_addon_key)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_keymap_addon_key
            return True
class GpuImg_settings_keymap_addon_key_area(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_keymap_addon_key_area)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_keymap_addon_key_area
            return True
class GpuImg_settings_keymap_addon_key_global(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_keymap_addon_key_global)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_keymap_addon_key_global
            return True
class GpuImg_settings_keymap_addon_key_text(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_keymap_addon_key_text)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_keymap_addon_key_text
            return True
class GpuImg_settings_keymap_addon_key_valuebox(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_keymap_addon_key_valuebox)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_keymap_addon_key_valuebox
            return True
class GpuImg_settings_keymap_ops(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_keymap_ops)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_keymap_ops
            return True
class GpuImg_settings_personalization(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization
            return True
class GpuImg_settings_personalization_font(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_font)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_font
            return True
class GpuImg_settings_personalization_font_path(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_font_path)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_font_path
            return True
class GpuImg_settings_personalization_shadow(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_shadow)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_shadow
            return True
class GpuImg_settings_personalization_theme(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_theme)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_theme
            return True
class GpuImg_settings_personalization_ui_color(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_ui_color)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_ui_color
            return True
class GpuImg_settings_personalization_ui_color_foreground(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_ui_color_foreground)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_ui_color_foreground
            return True
class GpuImg_settings_personalization_ui_color_hover(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_ui_color_hover)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_ui_color_hover
            return True
class GpuImg_settings_personalization_ui_color_taskbar(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_ui_color_taskbar)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_ui_color_taskbar
            return True
class GpuImg_settings_personalization_ui_color_window(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_personalization_ui_color_window)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_personalization_ui_color_window
            return True
class GpuImg_settings_size(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_size)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_size
            return True
class GpuImg_settings_size_ui_size(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_size_ui_size)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_size_ui_size
            return True
class GpuImg_settings_system(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system
            return True
class GpuImg_settings_system_about(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system_about)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system_about
            return True
class GpuImg_settings_system_all_settings(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system_all_settings)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system_all_settings
            return True
class GpuImg_settings_system_control(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system_control)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system_control
            return True
class GpuImg_settings_system_display(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system_display)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system_display
            return True
class GpuImg_settings_system_expression(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system_expression)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system_expression
            return True
class GpuImg_settings_system_library(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system_library)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system_library
            return True
class GpuImg_settings_system_menu(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_settings_system_menu)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_settings_system_menu
            return True
class GpuImg_SHAPEKEY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHAPEKEY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHAPEKEY
            return True
class GpuImg_SHARPCURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHARPCURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHARPCURVE
            return True
class GpuImg_SHOW_IN_EDITMODE_DISABLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_IN_EDITMODE_DISABLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_IN_EDITMODE_DISABLE
            return True
class GpuImg_SHOW_IN_EDITMODE_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_IN_EDITMODE_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_IN_EDITMODE_OFF
            return True
class GpuImg_SHOW_IN_EDITMODE_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_IN_EDITMODE_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_IN_EDITMODE_ON
            return True
class GpuImg_SHOW_ON_CAGE_DISABLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_ON_CAGE_DISABLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_ON_CAGE_DISABLE
            return True
class GpuImg_SHOW_ON_CAGE_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_ON_CAGE_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_ON_CAGE_OFF
            return True
class GpuImg_SHOW_ON_CAGE_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_ON_CAGE_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_ON_CAGE_ON
            return True
class GpuImg_SHOW_RENDER_DISABLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_RENDER_DISABLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_RENDER_DISABLE
            return True
class GpuImg_SHOW_RENDER_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_RENDER_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_RENDER_OFF
            return True
class GpuImg_SHOW_RENDER_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_RENDER_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_RENDER_ON
            return True
class GpuImg_SHOW_VIEWPORT_DISABLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_VIEWPORT_DISABLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_VIEWPORT_DISABLE
            return True
class GpuImg_SHOW_VIEWPORT_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_VIEWPORT_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_VIEWPORT_OFF
            return True
class GpuImg_SHOW_VIEWPORT_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHOW_VIEWPORT_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHOW_VIEWPORT_ON
            return True
class GpuImg_SHRINKWRAP(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SHRINKWRAP)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SHRINKWRAP
            return True
class GpuImg_SIMPLE_DEFORM(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SIMPLE_DEFORM)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SIMPLE_DEFORM
            return True
class GpuImg_SKIN(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SKIN)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SKIN
            return True
class GpuImg_SMOOTH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SMOOTH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SMOOTH
            return True
class GpuImg_SMOOTHCURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SMOOTHCURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SMOOTHCURVE
            return True
class GpuImg_SOFT_BODY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SOFT_BODY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SOFT_BODY
            return True
class GpuImg_SOLIDIFY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SOLIDIFY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SOLIDIFY
            return True
class GpuImg_SORTALPHA(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SORTALPHA)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SORTALPHA
            return True
class GpuImg_SPHERECURVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SPHERECURVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SPHERECURVE
            return True
class GpuImg_SPREADSHEET(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SPREADSHEET)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SPREADSHEET
            return True
class GpuImg_stop(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_stop)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_stop
            return True
class GpuImg_stop_dark(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_stop_dark)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_stop_dark
            return True
class GpuImg_SUBSURF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SUBSURF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SUBSURF
            return True
class GpuImg_SURFACE_DEFORM(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_SURFACE_DEFORM)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_SURFACE_DEFORM
            return True
class GpuImg_tb_active(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_tb_active)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_tb_active
            return True
class GpuImg_tb_hover(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_tb_hover)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_tb_hover
            return True
class GpuImg_tb_start(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_tb_start)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_tb_start
            return True
class GpuImg_title_button(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_title_button)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_title_button
            return True
class GpuImg_TPAINT_HLT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TPAINT_HLT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TPAINT_HLT
            return True
class GpuImg_transform(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_transform)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_transform
            return True
class GpuImg_TRASH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TRASH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TRASH
            return True
class GpuImg_TRASH_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TRASH_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TRASH_focus
            return True
class GpuImg_TRIANGULATE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TRIANGULATE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TRIANGULATE
            return True
class GpuImg_TRIA_DOWN(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TRIA_DOWN)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TRIA_DOWN
            return True
class GpuImg_TRIA_DOWN_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TRIA_DOWN_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TRIA_DOWN_focus
            return True
class GpuImg_TRIA_UP(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TRIA_UP)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TRIA_UP
            return True
class GpuImg_TRIA_UP_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_TRIA_UP_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_TRIA_UP_focus
            return True
class GpuImg_unfold(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_unfold)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_unfold
            return True
class GpuImg_unfold_focus(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_unfold_focus)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_unfold_focus
            return True
class GpuImg_unpin(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_unpin)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_unpin
            return True
class GpuImg_USE_APPLY_ON_SPLINE_OFF(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_USE_APPLY_ON_SPLINE_OFF)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_USE_APPLY_ON_SPLINE_OFF
            return True
class GpuImg_USE_APPLY_ON_SPLINE_ON(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_USE_APPLY_ON_SPLINE_ON)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_USE_APPLY_ON_SPLINE_ON
            return True
class GpuImg_UV_PROJECT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_UV_PROJECT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_UV_PROJECT
            return True
class GpuImg_UV_WARP(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_UV_WARP)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_UV_WARP
            return True
class GpuImg_valuebox_left(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_valuebox_left)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_valuebox_left
            return True
class GpuImg_valuebox_right(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_valuebox_right)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_valuebox_right
            return True
class GpuImg_VARIABLE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_VARIABLE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_VARIABLE
            return True
class GpuImg_VERTEX_WEIGHT_EDIT(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_VERTEX_WEIGHT_EDIT)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_VERTEX_WEIGHT_EDIT
            return True
class GpuImg_VERTEX_WEIGHT_MIX(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_VERTEX_WEIGHT_MIX)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_VERTEX_WEIGHT_MIX
            return True
class GpuImg_VERTEX_WEIGHT_PROXIMITY(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_VERTEX_WEIGHT_PROXIMITY)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_VERTEX_WEIGHT_PROXIMITY
            return True
class GpuImg_VOLUME_DISPLACE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_VOLUME_DISPLACE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_VOLUME_DISPLACE
            return True
class GpuImg_VOLUME_TO_MESH(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_VOLUME_TO_MESH)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_VOLUME_TO_MESH
            return True
class GpuImg_WARP(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_WARP)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_WARP
            return True
class GpuImg_WAVE(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_WAVE)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_WAVE
            return True
class GpuImg_WEIGHTED_NORMAL(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_WEIGHTED_NORMAL)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_WEIGHTED_NORMAL
            return True
class GpuImg_WELD(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_WELD)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_WELD
            return True
class GpuImg_WIREFRAME(GpuImg):
    __slots__ = ()
    def bind_draw(self):
        GL_IMG_bind()
        GL_IMG_uniform_float("viewProjectionMatrix", get_projection_matrix())
        GL_IMG_uniform_sampler("image", IM_WIREFRAME)
        self.batdraw()
    def set_draw_state(self, boo):
        if boo: return False
        else:
            self.__class__ = GpuImgNull
            self.cls = GpuImg_WIREFRAME
            return True
## */


S_MD_BUTTON4 = {
    # <<< 1copy (0md_ModExAttr_EX4,, $$, $lambda e: f"    '{e.strip().split(' = ', 1)[0]}',\n"$)
    'ARMATURE',
    'ARRAY',
    'CAST',
    'CORRECTIVE_SMOOTH',
    'CURVE',
    'DATA_TRANSFER',
    'DISPLACE',
    'EDGE_SPLIT',
    'HOOK',
    'LAPLACIANDEFORM',
    'LAPLACIANSMOOTH',
    'LATTICE',
    'MASK',
    'MESH_DEFORM',
    'MIRROR',
    'NODES',
    'NORMAL_EDIT',
    'SHRINKWRAP',
    'SIMPLE_DEFORM',
    'SMOOTH',
    'SOLIDIFY',
    'SUBSURF',
    'SURFACE_DEFORM',
    'TRIANGULATE',
    'UV_PROJECT',
    'VERTEX_WEIGHT_EDIT',
    'VERTEX_WEIGHT_MIX',
    'VERTEX_WEIGHT_PROXIMITY',
    'WARP',
    'WAVE',
    'WEIGHTED_NORMAL',
    'WELD',
    # >>>
    }
S_MD_BUTTON3 = {
    # <<< 1copy (0md_ModExAttr_EX3,, $$, $lambda e: f"    '{e.strip().split(' = ', 1)[0]}',\n"$)
    'BOOLEAN',
    'BEVEL',
    'MESH_CACHE',
    'OCEAN',
    'PARTICLE_INSTANCE',
    'REMESH',
    'SCREW',
    'SKIN',
    'UV_WARP',
    'WIREFRAME',
    'GREASE_PENCIL_TEXTURE',
    'GREASE_PENCIL_TIME',
    'GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY',
    'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE',
    'GREASE_PENCIL_ARRAY',
    'GREASE_PENCIL_BUILD',
    'GREASE_PENCIL_DASH',
    'GREASE_PENCIL_ENVELOPE',
    'GREASE_PENCIL_LENGTH',
    'GREASE_PENCIL_MIRROR',
    'GREASE_PENCIL_MULTIPLY',
    'GREASE_PENCIL_OUTLINE',
    'GREASE_PENCIL_SIMPLIFY',
    'GREASE_PENCIL_SUBDIV',
    'LINEART',
    'GREASE_PENCIL_ARMATURE',
    'GREASE_PENCIL_HOOK',
    'GREASE_PENCIL_LATTICE',
    'GREASE_PENCIL_NOISE',
    'GREASE_PENCIL_OFFSET',
    'GREASE_PENCIL_SHRINKWRAP',
    'GREASE_PENCIL_SMOOTH',
    'GREASE_PENCIL_THICKNESS',
    'GREASE_PENCIL_COLOR',
    'GREASE_PENCIL_TINT',
    'GREASE_PENCIL_OPACITY',
    # >>>
    }
S_MD_BUTTON2 = {
    # <<< 1copy (0md_ModExAttr_EX2,, $$, $lambda e: f"    '{e.strip().split(' = ', 1)[0]}',\n"$)
    'BUILD',
    'CLOTH',
    'DECIMATE',
    'DYNAMIC_PAINT',
    'EXPLODE',
    'FLUID',
    'MESH_SEQUENCE_CACHE',
    'MESH_TO_VOLUME',
    'MULTIRES',
    'PARTICLE_SYSTEM',
    'SOFT_BODY',
    'VOLUME_DISPLACE',
    'VOLUME_TO_MESH',
    # >>>
    }
S_MD_USE_RENDER = set.union(S_MD_BUTTON4, S_MD_BUTTON3, S_MD_BUTTON2)
S_MD_USE_EDITMODE = set.union(S_MD_BUTTON4, S_MD_BUTTON3)

def geticon_Object(e):
    if e.type in D_geticon_Object:
        if e.library:
            if e.is_missing:
                return GpuImgSlot2(D_geticon_Object[e.type](), GpuImg_LIBRARY_DATA_BROKEN())
            if e.visible_get():
                return GpuImgSlot2(D_geticon_Object[e.type](), GpuImg_LIBRARY_DATA_DIRECT())
            return GpuImgSlot2(D_geticon_Object[e.type](), GpuImg_RESTRICT_INSTANCED_ON())

        if e.asset_data:
            return GpuImgSlot2(D_geticon_Object[e.type](), GpuImg_ASSET_MANAGER())

        if e.override_library:
            if e.override_library.is_system_override:
                return GpuImgSlot2(D_geticon_Object[e.type](), GpuImg_LIBRARY_DATA_OVERRIDE_DISABLE())
            return GpuImgSlot2(D_geticon_Object[e.type](), GpuImg_LIBRARY_DATA_OVERRIDE())

        return D_geticon_Object[e.type]()

    return GpuImg_OUTLINER_OB_UNKNOW()
    #|
def getinfo_Object(e):
    if e.library:
        return e.library.filepath
    return ""
    #|
def geticon_Modifier(e):
    if e.type in D_geticon_Modifier:
        if hasattr(e, "use_pin_to_last") and e.use_pin_to_last:
            return GpuImgSlot2(D_geticon_Modifier[e.type](), GpuImg_pin())
        return D_geticon_Modifier[e.type]()
    return GpuImg_OUTLINER_OB_UNKNOW()
    #|
def geticon_DriverVar(e):
    if e.type in D_geticon_DriverVar: return D_geticon_DriverVar[e.type]()
    return GpuImg_OUTLINER_OB_UNKNOW()
    #|
def geticon_dynamic_paint_canvas(e):
    try:
        o = GpuImgSlot2(D_geticon_dynamic_paint_surface_format[e.surface_format](), D_geticon_dynamic_paint_surface_type[e.surface_type]())
        o.identifier = f'{e.surface_format}{e.surface_type}'
        return o
    except:
        o = GpuImgSlot2(GpuImg_OUTLINER_OB_UNKNOW(), GpuImg_OUTLINER_OB_UNKNOW())
        o.identifier = ""
        return o
    #|
def update_icons_dynamic_paint_canvas(filt):
    match_items = filt.match_items
    for r, o in filt.icons.items():
        e = match_items[r]
        if f'{e.surface_format}{e.surface_type}' == o.identifier: continue

        try:
            o.slot0.__class__ = D_geticon_dynamic_paint_surface_format[e.surface_format]
            o.slot1.__class__ = D_geticon_dynamic_paint_surface_type[e.surface_type]
            o.identifier = f'{e.surface_format}{e.surface_type}'
        except:
            o.slot0.__class__ = GpuImg_OUTLINER_OB_UNKNOW
            o.slot1.__class__ = GpuImg_OUTLINER_OB_UNKNOW
            o.identifier = ""
    #|

def geticon_fake(e, anim_data): return GpuImgNull()
def geticon_Modifier_button(e, anim_data):
    if e.type in S_MD_BUTTON4: return GpuImgSlotModifierRVEC(anim_data, e)
    if e.type in S_MD_BUTTON3: return GpuImgSlotModifierRVE(anim_data, e)
    if e.type in S_MD_BUTTON2: return GpuImgSlotModifierRV(anim_data, e)
    return GpuImgSlotModifier(anim_data, e)
    #|
def geticon_Modifier_override_button(e, anim_data):
    if hasattr(e, "is_override_data") and e.is_override_data:
        if e.type in S_MD_BUTTON4: return GpuImgSlotModifierOverrideRVEC(anim_data, e)
        if e.type in S_MD_BUTTON3: return GpuImgSlotModifierOverrideRVE(anim_data, e)
        if e.type in S_MD_BUTTON2: return GpuImgSlotModifierOverrideRV(anim_data, e)
        return GpuImgSlotModifierOverride(anim_data, e)
    else:
        if e.type in S_MD_BUTTON4: return GpuImgSlotModifierRVEC(anim_data, e)
        if e.type in S_MD_BUTTON3: return GpuImgSlotModifierRVE(anim_data, e)
        if e.type in S_MD_BUTTON2: return GpuImgSlotModifierRV(anim_data, e)
        return GpuImgSlotModifier(anim_data, e)
    #|
def geticon_Modifier_systemoverride_button(e, anim_data):
    if hasattr(e, "is_override_data") and e.is_override_data:
        if e.type in S_MD_BUTTON4: return GpuImgSlotModifierSystemOverrideRVEC(anim_data, e)
        if e.type in S_MD_BUTTON3: return GpuImgSlotModifierSystemOverrideRVE(anim_data, e)
        if e.type in S_MD_BUTTON2: return GpuImgSlotModifierSystemOverrideRV(anim_data, e)
        return GpuImgSlotModifierSystemOverride(anim_data, e)
    else:
        if e.type in S_MD_BUTTON4: return GpuImgSlotModifierRVEC(anim_data, e)
        if e.type in S_MD_BUTTON3: return GpuImgSlotModifierRVE(anim_data, e)
        if e.type in S_MD_BUTTON2: return GpuImgSlotModifierRV(anim_data, e)
        return GpuImgSlotModifier(anim_data, e)
    #|
def geticon_Modifier_library_button(e, anim_data):
    if e.type in S_MD_BUTTON4: return GpuImgSlotModifierRVEC(anim_data, e)
    if e.type in S_MD_BUTTON3: return GpuImgSlotModifierRVE(anim_data, e)
    if e.type in S_MD_BUTTON2: return GpuImgSlotModifierRV(anim_data, e)
    return GpuImgSlotModifier(anim_data, e)
    #|
def geticon_Modifier_button_spline(e, anim_data):
    if e.type in S_MD_BUTTON4:
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
        return GpuImgSlotModifierSplineRVE(anim_data, e)
    if e.type in S_MD_BUTTON3:
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
        return GpuImgSlotModifierSplineRVE(anim_data, e)
    if e.type in S_MD_BUTTON2:
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVS(anim_data, e)
        return GpuImgSlotModifierSplineRV(anim_data, e)
    if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineS(anim_data, e)
    return GpuImgSlotModifierSpline(anim_data, e)
    #|
def geticon_Modifier_override_button_spline(e, anim_data):
    if hasattr(e, "is_override_data") and e.is_override_data:
        if e.type in S_MD_BUTTON4:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierOverrideSplineRVES(anim_data, e)
            return GpuImgSlotModifierOverrideSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON3:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierOverrideSplineRVES(anim_data, e)
            return GpuImgSlotModifierOverrideSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON2:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierOverrideSplineRVS(anim_data, e)
            return GpuImgSlotModifierOverrideSplineRV(anim_data, e)
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierOverrideSplineS(anim_data, e)
        return GpuImgSlotModifierOverrideSpline(anim_data, e)
    else:
        if e.type in S_MD_BUTTON4:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
            return GpuImgSlotModifierSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON3:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
            return GpuImgSlotModifierSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON2:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVS(anim_data, e)
            return GpuImgSlotModifierSplineRV(anim_data, e)
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineS(anim_data, e)
        return GpuImgSlotModifierSpline(anim_data, e)
    #|
def geticon_Modifier_systemoverride_button_spline(e, anim_data):
    if hasattr(e, "is_override_data") and e.is_override_data:
        if e.type in S_MD_BUTTON4:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSystemOverrideSplineRVES(anim_data, e)
            return GpuImgSlotModifierSystemOverrideSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON3:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSystemOverrideSplineRVES(anim_data, e)
            return GpuImgSlotModifierSystemOverrideSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON2:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSystemOverrideSplineRVS(anim_data, e)
            return GpuImgSlotModifierSystemOverrideSplineRV(anim_data, e)
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSystemOverrideSplineS(anim_data, e)
        return GpuImgSlotModifierSystemOverrideSpline(anim_data, e)
    else:
        if e.type in S_MD_BUTTON4:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
            return GpuImgSlotModifierSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON3:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
            return GpuImgSlotModifierSplineRVE(anim_data, e)
        if e.type in S_MD_BUTTON2:
            if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVS(anim_data, e)
            return GpuImgSlotModifierSplineRV(anim_data, e)
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineS(anim_data, e)
        return GpuImgSlotModifierSpline(anim_data, e)
    #|
def geticon_Modifier_library_button_spline(e, anim_data):
    if e.type in S_MD_BUTTON4:
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
        return GpuImgSlotModifierSplineRVE(anim_data, e)
    if e.type in S_MD_BUTTON3:
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVES(anim_data, e)
        return GpuImgSlotModifierSplineRVE(anim_data, e)
    if e.type in S_MD_BUTTON2:
        if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineRVS(anim_data, e)
        return GpuImgSlotModifierSplineRV(anim_data, e)
    if e.type in S_md_apply_on_spline: return GpuImgSlotModifierSplineS(anim_data, e)
    return GpuImgSlotModifierSpline(anim_data, e)
    #|
def r_geticon_Modifier_button(ob):
    if hasattr(ob, "library") and ob.library:
        if hasattr(ob, "type") and ob.type in S_spline_modifier_types:
            return geticon_Modifier_library_button_spline
        else: return geticon_Modifier_library_button
    elif hasattr(ob, "override_library") and ob.override_library:
        if ob.override_library.is_system_override:
            if hasattr(ob, "type") and ob.type in S_spline_modifier_types:
                return geticon_Modifier_systemoverride_button_spline
            else: return geticon_Modifier_systemoverride_button
        else:
            if hasattr(ob, "type") and ob.type in S_spline_modifier_types:
                return geticon_Modifier_override_button_spline
            else: return geticon_Modifier_override_button

    if hasattr(ob, "type") and ob.type in S_spline_modifier_types:
        return geticon_Modifier_button_spline
    else: return geticon_Modifier_button
    #|

def r_modifier_button_BG_on(anim_data, dp):
    # /* 0blg_r_modifier_button_BG_on
    if anim_data is None: return GpuImg_MD_BG_SHOW_ON
    if anim_data.action is not None and anim_data.action.fcurves:
        if anim_data.action.fcurves.find(dp) != None:
            return GpuImg_MD_BG_SHOW_ON_KEYFRAME

    if anim_data.drivers:
        if anim_data.drivers.find(dp) == None: return GpuImg_MD_BG_SHOW_ON
        return GpuImg_MD_BG_SHOW_ON_DRIVER
    return GpuImg_MD_BG_SHOW_ON
    # */
def r_modifier_button_BG_off(anim_data, dp):
    # <<< 1copy (0blg_r_modifier_button_BG_on,, ${'_ON':'_OFF'}$)
    if anim_data is None: return GpuImg_MD_BG_SHOW_OFF
    if anim_data.action is not None and anim_data.action.fcurves:
        if anim_data.action.fcurves.find(dp) != None:
            return GpuImg_MD_BG_SHOW_OFF_KEYFRAME

    if anim_data.drivers:
        if anim_data.drivers.find(dp) == None: return GpuImg_MD_BG_SHOW_OFF
        return GpuImg_MD_BG_SHOW_OFF_DRIVER
    return GpuImg_MD_BG_SHOW_OFF
    # >>>
    #|
def r_modifier_button_BG_on_override(anim_data, dp):
    # /* 0blg_r_modifier_button_BG_on_override
    if anim_data is None: return GpuImg_MD_OVERRIDE_ON
    if anim_data.action is not None and anim_data.action.fcurves:
        if anim_data.action.fcurves.find(dp) != None:
            return GpuImg_MD_BG_SHOW_ON_KEYFRAME

    if anim_data.drivers:
        if anim_data.drivers.find(dp) == None: return GpuImg_MD_OVERRIDE_ON
        return GpuImg_MD_BG_SHOW_ON_DRIVER
    return GpuImg_MD_OVERRIDE_ON
    # */
    #|
def r_modifier_button_BG_off_override(anim_data, dp):
    # <<< 1copy (0blg_r_modifier_button_BG_on_override,, ${'_ON':'_OFF'}$)
    if anim_data is None: return GpuImg_MD_OVERRIDE_OFF
    if anim_data.action is not None and anim_data.action.fcurves:
        if anim_data.action.fcurves.find(dp) != None:
            return GpuImg_MD_BG_SHOW_OFF_KEYFRAME

    if anim_data.drivers:
        if anim_data.drivers.find(dp) == None: return GpuImg_MD_OVERRIDE_OFF
        return GpuImg_MD_BG_SHOW_OFF_DRIVER
    return GpuImg_MD_OVERRIDE_OFF
    # >>>
    #|


def r_icon_subfolder():
    P = m.P
    h = SIZE_widget[0]
    if h == 18: widget = "100x"
    elif h == 24: widget = "133x"
    elif h == 30: widget = "166x"
    elif h == 36: widget = "200x"
    else: widget = "sample"
    return widget
    #|
def load_gpu_texture():
    images_load = _bpy.data.images.load
    images_remove = _bpy.data.images.remove

    icon_subfolder = r_icon_subfolder()

    p0 = f"{m.ADDON_FOLDER}Icons{os_sep}{icon_subfolder}{os_sep}"

    ## /* import_image
    global IM_ADD, IM_ADD_focus, IM_apply, IM_area_icon_hover, IM_ARMATURE, IM_ARRAY, IM_arrow_left, IM_arrow_left_disable, IM_arrow_right, IM_arrow_right_disable, IM_arrow_up, IM_arrow_up_disable, IM_ASSET_MANAGER, IM_assign, IM_BEVEL, IM_BONE_DATA, IM_BOOLEAN, IM_BUILD, IM_cache_layer, IM_CAST, IM_checkbox_fg, IM_checkbox_fg_disable, IM_CLOTH, IM_COLLISION, IM_context_property, IM_copy, IM_copy_array, IM_CORRECTIVE_SMOOTH, IM_CURVE, IM_DATA_TRANSFER, IM_DECIMATE, IM_delete, IM_delete_dark, IM_delete_focus, IM_Detail, IM_DISPLACE, IM_distance, IM_DriverEditor, IM_driver_ref, IM_driver_ref_dark, IM_driver_true, IM_driver_true_dark, IM_dropdown_close, IM_DUPLICATE, IM_DUPLICATE_focus, IM_DYNAMIC_PAINT, IM_EDGE, IM_EDGE_SPLIT, IM_EMPTY_AXIS, IM_EXPLODE, IM_eyedropper, IM_FACE, IM_FACE_CORNER, IM_FAKE_USER_LIB, IM_FAKE_USER_LIB_focus, IM_FAKE_USER_LINK, IM_FAKE_USER_LINK_focus, IM_FAKE_USER_OFF, IM_FAKE_USER_OFF_focus, IM_FAKE_USER_ON, IM_FAKE_USER_ON_focus, IM_FAKE_USER_OVERRIDE, IM_FAKE_USER_OVERRIDE_focus, IM_FILE_FOLDER, IM_FILE_FOLDER_focus, IM_FILE_REFRESH, IM_filter_match_active, IM_filter_match_case, IM_filter_match_end_left, IM_filter_match_end_right, IM_filter_match_hover, IM_filter_match_whole_word, IM_FLUID, IM_fold, IM_fold_focus, IM_GREASEPENCIL, IM_GREASE_PENCIL_ARMATURE, IM_GREASE_PENCIL_ARRAY, IM_GREASE_PENCIL_BUILD, IM_GREASE_PENCIL_COLOR, IM_GREASE_PENCIL_DASH, IM_GREASE_PENCIL_ENVELOPE, IM_GREASE_PENCIL_HOOK, IM_GREASE_PENCIL_LATTICE, IM_GREASE_PENCIL_LENGTH, IM_GREASE_PENCIL_MIRROR, IM_GREASE_PENCIL_MULTIPLY, IM_GREASE_PENCIL_NOISE, IM_GREASE_PENCIL_OFFSET, IM_GREASE_PENCIL_OPACITY, IM_GREASE_PENCIL_OUTLINE, IM_GREASE_PENCIL_SHRINKWRAP, IM_GREASE_PENCIL_SIMPLIFY, IM_GREASE_PENCIL_SMOOTH, IM_GREASE_PENCIL_SUBDIV, IM_GREASE_PENCIL_TEXTURE, IM_GREASE_PENCIL_THICKNESS, IM_GREASE_PENCIL_TIME, IM_GREASE_PENCIL_TINT, IM_GREASE_PENCIL_VERTEX_WEIGHT_ANGLE, IM_GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY, IM_GROUP_UVS, IM_GROUP_VCOL, IM_GROUP_VERTEX, IM_HIDE_OFF, IM_HIDE_OFF_focus, IM_HIDE_ON, IM_HIDE_ON_focus, IM_HOOK, IM_hue_button, IM_hue_cursor, IM_ID_ACTION, IM_ID_ARMATURE, IM_ID_BRUSH, IM_ID_CACHEFILE, IM_ID_CAMERA, IM_ID_COLLECTION, IM_ID_CURVE, IM_ID_CURVES, IM_ID_FONT, IM_ID_GREASEPENCIL, IM_ID_IMAGE, IM_ID_KEY, IM_ID_LATTICE, IM_ID_LIBRARY, IM_ID_LIGHT, IM_ID_LIGHT_PROBE, IM_ID_LINESTYLE, IM_ID_MASK, IM_ID_MATERIAL, IM_ID_MESH, IM_ID_META, IM_ID_MOVIECLIP, IM_ID_NODETREE, IM_ID_OBJECT, IM_ID_PAINTCURVE, IM_ID_PALETTE, IM_ID_PARTICLE, IM_ID_POINTCLOUD, IM_ID_SCENE, IM_ID_SCREEN, IM_ID_SOUND, IM_ID_SPEAKER, IM_ID_TEXT, IM_ID_TEXTURE, IM_ID_VOLUME, IM_ID_WINDOWMANAGER, IM_ID_WORKSPACE, IM_ID_WORLD, IM_invert, IM_invert_y, IM_IPO_CONSTANT, IM_keyframe_current_true_even, IM_keyframe_current_true_even_dark, IM_keyframe_current_true_odd, IM_keyframe_current_true_odd_dark, IM_keyframe_false, IM_keyframe_false_dark, IM_keyframe_next_false_even, IM_keyframe_next_false_even_dark, IM_keyframe_next_false_odd, IM_keyframe_next_false_odd_dark, IM_keying_set, IM_KeymapEditor, IM_LAPLACIANDEFORM, IM_LAPLACIANSMOOTH, IM_LATTICE, IM_LIBRARY_DATA_BROKEN, IM_LIBRARY_DATA_DIRECT, IM_LIBRARY_DATA_OVERRIDE, IM_LIBRARY_DATA_OVERRIDE_DISABLE, IM_LINCURVE, IM_LINEART, IM_manual, IM_MASK, IM_MATCUBE, IM_MD_BG_SHOW_HOVER, IM_MD_BG_SHOW_OFF, IM_MD_BG_SHOW_OFF_DRIVER, IM_MD_BG_SHOW_OFF_KEYFRAME, IM_MD_BG_SHOW_ON, IM_MD_BG_SHOW_ON_DRIVER, IM_MD_BG_SHOW_ON_KEYFRAME, IM_MD_LIBRARY_OFF, IM_MD_LIBRARY_ON, IM_MD_MULTI_SORT, IM_MD_OVERRIDE_OFF, IM_MD_OVERRIDE_ON, IM_MeshEditor, IM_MESH_CACHE, IM_MESH_DEFORM, IM_MESH_SEQUENCE_CACHE, IM_MESH_TO_VOLUME, IM_META_CUBE, IM_MIRROR, IM_MODIFIER, IM_ModifierEditor, IM_MULTIRES, IM_NOCURVE, IM_NODES, IM_NORMAL_EDIT, IM_objectpath, IM_OBJECT_DATA, IM_object_picker, IM_object_picker_dark, IM_object_picker_focus, IM_OCEAN, IM_OUTLINER_DATA_GP_LAYER, IM_OUTLINER_OB_ARMATURE, IM_OUTLINER_OB_CAMERA, IM_OUTLINER_OB_CURVE, IM_OUTLINER_OB_CURVES, IM_OUTLINER_OB_EMPTY, IM_OUTLINER_OB_FONT, IM_OUTLINER_OB_GREASEPENCIL, IM_OUTLINER_OB_LATTICE, IM_OUTLINER_OB_LIGHT, IM_OUTLINER_OB_LIGHTPROBE, IM_OUTLINER_OB_MESH, IM_OUTLINER_OB_META, IM_OUTLINER_OB_POINTCLOUD, IM_OUTLINER_OB_SPEAKER, IM_OUTLINER_OB_SURFACE, IM_OUTLINER_OB_UNKNOW, IM_OUTLINER_OB_VOLUME, IM_PARTICLE_INSTANCE, IM_PARTICLE_SYSTEM, IM_paste, IM_PHYSICS, IM_pin, IM_POINT, IM_py_exp_off, IM_py_exp_on, IM_REMESH, IM_REMOVE, IM_REMOVE_focus, IM_rename, IM_rename_focus, IM_reset, IM_reset_override, IM_RESTRICT_INSTANCED_ON, IM_rna, IM_RNDCURVE, IM_ROOTCURVE, IM_rotation, IM_save, IM_SCREW, IM_search, IM_SettingEditor, IM_settings_apps, IM_settings_keymap, IM_settings_keymap_addon_key, IM_settings_keymap_addon_key_area, IM_settings_keymap_addon_key_global, IM_settings_keymap_addon_key_text, IM_settings_keymap_addon_key_valuebox, IM_settings_keymap_ops, IM_settings_personalization, IM_settings_personalization_font, IM_settings_personalization_font_path, IM_settings_personalization_shadow, IM_settings_personalization_theme, IM_settings_personalization_ui_color, IM_settings_personalization_ui_color_foreground, IM_settings_personalization_ui_color_hover, IM_settings_personalization_ui_color_taskbar, IM_settings_personalization_ui_color_window, IM_settings_size, IM_settings_size_ui_size, IM_settings_system, IM_settings_system_about, IM_settings_system_all_settings, IM_settings_system_control, IM_settings_system_display, IM_settings_system_expression, IM_settings_system_library, IM_settings_system_menu, IM_SHAPEKEY, IM_SHARPCURVE, IM_SHOW_IN_EDITMODE_DISABLE, IM_SHOW_IN_EDITMODE_OFF, IM_SHOW_IN_EDITMODE_ON, IM_SHOW_ON_CAGE_DISABLE, IM_SHOW_ON_CAGE_OFF, IM_SHOW_ON_CAGE_ON, IM_SHOW_RENDER_DISABLE, IM_SHOW_RENDER_OFF, IM_SHOW_RENDER_ON, IM_SHOW_VIEWPORT_DISABLE, IM_SHOW_VIEWPORT_OFF, IM_SHOW_VIEWPORT_ON, IM_SHRINKWRAP, IM_SIMPLE_DEFORM, IM_SKIN, IM_SMOOTH, IM_SMOOTHCURVE, IM_SOFT_BODY, IM_SOLIDIFY, IM_SORTALPHA, IM_SPHERECURVE, IM_SPREADSHEET, IM_stop, IM_stop_dark, IM_SUBSURF, IM_SURFACE_DEFORM, IM_tb_active, IM_tb_hover, IM_tb_start, IM_title_button, IM_TPAINT_HLT, IM_transform, IM_TRASH, IM_TRASH_focus, IM_TRIANGULATE, IM_TRIA_DOWN, IM_TRIA_DOWN_focus, IM_TRIA_UP, IM_TRIA_UP_focus, IM_unfold, IM_unfold_focus, IM_unpin, IM_USE_APPLY_ON_SPLINE_OFF, IM_USE_APPLY_ON_SPLINE_ON, IM_UV_PROJECT, IM_UV_WARP, IM_valuebox_left, IM_valuebox_right, IM_VARIABLE, IM_VERTEX_WEIGHT_EDIT, IM_VERTEX_WEIGHT_MIX, IM_VERTEX_WEIGHT_PROXIMITY, IM_VOLUME_DISPLACE, IM_VOLUME_TO_MESH, IM_WARP, IM_WAVE, IM_WEIGHTED_NORMAL, IM_WELD, IM_WIREFRAME
    img = images_load(f"{p0}ADD.png")
    img.alpha_mode = "PREMUL"
    IM_ADD = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ADD_focus.png")
    img.alpha_mode = "PREMUL"
    IM_ADD_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}apply.png")
    img.alpha_mode = "PREMUL"
    IM_apply = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}area_icon_hover.png")
    img.alpha_mode = "PREMUL"
    IM_area_icon_hover = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ARMATURE.png")
    img.alpha_mode = "PREMUL"
    IM_ARMATURE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ARRAY.png")
    img.alpha_mode = "PREMUL"
    IM_ARRAY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}arrow_left.png")
    img.alpha_mode = "PREMUL"
    IM_arrow_left = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}arrow_left_disable.png")
    img.alpha_mode = "PREMUL"
    IM_arrow_left_disable = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}arrow_right.png")
    img.alpha_mode = "PREMUL"
    IM_arrow_right = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}arrow_right_disable.png")
    img.alpha_mode = "PREMUL"
    IM_arrow_right_disable = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}arrow_up.png")
    img.alpha_mode = "PREMUL"
    IM_arrow_up = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}arrow_up_disable.png")
    img.alpha_mode = "PREMUL"
    IM_arrow_up_disable = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ASSET_MANAGER.png")
    img.alpha_mode = "PREMUL"
    IM_ASSET_MANAGER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}assign.png")
    img.alpha_mode = "PREMUL"
    IM_assign = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}BEVEL.png")
    img.alpha_mode = "PREMUL"
    IM_BEVEL = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}BONE_DATA.png")
    img.alpha_mode = "PREMUL"
    IM_BONE_DATA = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}BOOLEAN.png")
    img.alpha_mode = "PREMUL"
    IM_BOOLEAN = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}BUILD.png")
    img.alpha_mode = "PREMUL"
    IM_BUILD = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}cache_layer.png")
    img.alpha_mode = "PREMUL"
    IM_cache_layer = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}CAST.png")
    img.alpha_mode = "PREMUL"
    IM_CAST = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}checkbox_fg.png")
    img.alpha_mode = "PREMUL"
    IM_checkbox_fg = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}checkbox_fg_disable.png")
    img.alpha_mode = "PREMUL"
    IM_checkbox_fg_disable = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}CLOTH.png")
    img.alpha_mode = "PREMUL"
    IM_CLOTH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}COLLISION.png")
    img.alpha_mode = "PREMUL"
    IM_COLLISION = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}context_property.png")
    img.alpha_mode = "PREMUL"
    IM_context_property = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}copy.png")
    img.alpha_mode = "PREMUL"
    IM_copy = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}copy_array.png")
    img.alpha_mode = "PREMUL"
    IM_copy_array = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}CORRECTIVE_SMOOTH.png")
    img.alpha_mode = "PREMUL"
    IM_CORRECTIVE_SMOOTH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}CURVE.png")
    img.alpha_mode = "PREMUL"
    IM_CURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}DATA_TRANSFER.png")
    img.alpha_mode = "PREMUL"
    IM_DATA_TRANSFER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}DECIMATE.png")
    img.alpha_mode = "PREMUL"
    IM_DECIMATE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}delete.png")
    img.alpha_mode = "PREMUL"
    IM_delete = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}delete_dark.png")
    img.alpha_mode = "PREMUL"
    IM_delete_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}delete_focus.png")
    img.alpha_mode = "PREMUL"
    IM_delete_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}Detail.png")
    img.alpha_mode = "PREMUL"
    IM_Detail = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}DISPLACE.png")
    img.alpha_mode = "PREMUL"
    IM_DISPLACE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}distance.png")
    img.alpha_mode = "PREMUL"
    IM_distance = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}DriverEditor.png")
    img.alpha_mode = "PREMUL"
    IM_DriverEditor = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}driver_ref.png")
    img.alpha_mode = "PREMUL"
    IM_driver_ref = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}driver_ref_dark.png")
    img.alpha_mode = "PREMUL"
    IM_driver_ref_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}driver_true.png")
    img.alpha_mode = "PREMUL"
    IM_driver_true = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}driver_true_dark.png")
    img.alpha_mode = "PREMUL"
    IM_driver_true_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}dropdown_close.png")
    img.alpha_mode = "PREMUL"
    IM_dropdown_close = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}DUPLICATE.png")
    img.alpha_mode = "PREMUL"
    IM_DUPLICATE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}DUPLICATE_focus.png")
    img.alpha_mode = "PREMUL"
    IM_DUPLICATE_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}DYNAMIC_PAINT.png")
    img.alpha_mode = "PREMUL"
    IM_DYNAMIC_PAINT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}EDGE.png")
    img.alpha_mode = "PREMUL"
    IM_EDGE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}EDGE_SPLIT.png")
    img.alpha_mode = "PREMUL"
    IM_EDGE_SPLIT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}EMPTY_AXIS.png")
    img.alpha_mode = "PREMUL"
    IM_EMPTY_AXIS = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}EXPLODE.png")
    img.alpha_mode = "PREMUL"
    IM_EXPLODE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}eyedropper.png")
    img.alpha_mode = "PREMUL"
    IM_eyedropper = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FACE.png")
    img.alpha_mode = "PREMUL"
    IM_FACE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FACE_CORNER.png")
    img.alpha_mode = "PREMUL"
    IM_FACE_CORNER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_LIB.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_LIB = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_LIB_focus.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_LIB_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_LINK.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_LINK = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_LINK_focus.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_LINK_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_OFF_focus.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_OFF_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_ON.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_ON_focus.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_ON_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_OVERRIDE.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_OVERRIDE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FAKE_USER_OVERRIDE_focus.png")
    img.alpha_mode = "PREMUL"
    IM_FAKE_USER_OVERRIDE_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FILE_FOLDER.png")
    img.alpha_mode = "PREMUL"
    IM_FILE_FOLDER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FILE_FOLDER_focus.png")
    img.alpha_mode = "PREMUL"
    IM_FILE_FOLDER_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FILE_REFRESH.png")
    img.alpha_mode = "PREMUL"
    IM_FILE_REFRESH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}filter_match_active.png")
    img.alpha_mode = "PREMUL"
    IM_filter_match_active = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}filter_match_case.png")
    img.alpha_mode = "PREMUL"
    IM_filter_match_case = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}filter_match_end_left.png")
    img.alpha_mode = "PREMUL"
    IM_filter_match_end_left = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}filter_match_end_right.png")
    img.alpha_mode = "PREMUL"
    IM_filter_match_end_right = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}filter_match_hover.png")
    img.alpha_mode = "PREMUL"
    IM_filter_match_hover = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}filter_match_whole_word.png")
    img.alpha_mode = "PREMUL"
    IM_filter_match_whole_word = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}FLUID.png")
    img.alpha_mode = "PREMUL"
    IM_FLUID = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}fold.png")
    img.alpha_mode = "PREMUL"
    IM_fold = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}fold_focus.png")
    img.alpha_mode = "PREMUL"
    IM_fold_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASEPENCIL.png")
    img.alpha_mode = "PREMUL"
    IM_GREASEPENCIL = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_ARMATURE.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_ARMATURE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_ARRAY.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_ARRAY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_BUILD.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_BUILD = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_COLOR.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_COLOR = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_DASH.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_DASH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_ENVELOPE.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_ENVELOPE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_HOOK.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_HOOK = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_LATTICE.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_LATTICE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_LENGTH.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_LENGTH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_MIRROR.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_MIRROR = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_MULTIPLY.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_MULTIPLY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_NOISE.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_NOISE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_OFFSET.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_OFFSET = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_OPACITY.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_OPACITY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_OUTLINE.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_OUTLINE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_SHRINKWRAP.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_SHRINKWRAP = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_SIMPLIFY.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_SIMPLIFY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_SMOOTH.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_SMOOTH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_SUBDIV.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_SUBDIV = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_TEXTURE.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_TEXTURE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_THICKNESS.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_THICKNESS = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_TIME.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_TIME = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_TINT.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_TINT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_VERTEX_WEIGHT_ANGLE.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_VERTEX_WEIGHT_ANGLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY.png")
    img.alpha_mode = "PREMUL"
    IM_GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GROUP_UVS.png")
    img.alpha_mode = "PREMUL"
    IM_GROUP_UVS = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GROUP_VCOL.png")
    img.alpha_mode = "PREMUL"
    IM_GROUP_VCOL = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}GROUP_VERTEX.png")
    img.alpha_mode = "PREMUL"
    IM_GROUP_VERTEX = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}HIDE_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_HIDE_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}HIDE_OFF_focus.png")
    img.alpha_mode = "PREMUL"
    IM_HIDE_OFF_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}HIDE_ON.png")
    img.alpha_mode = "PREMUL"
    IM_HIDE_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}HIDE_ON_focus.png")
    img.alpha_mode = "PREMUL"
    IM_HIDE_ON_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}HOOK.png")
    img.alpha_mode = "PREMUL"
    IM_HOOK = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}hue_button.png")
    img.alpha_mode = "PREMUL"
    IM_hue_button = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}hue_cursor.png")
    img.alpha_mode = "PREMUL"
    IM_hue_cursor = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_ACTION.png")
    img.alpha_mode = "PREMUL"
    IM_ID_ACTION = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_ARMATURE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_ARMATURE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_BRUSH.png")
    img.alpha_mode = "PREMUL"
    IM_ID_BRUSH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_CACHEFILE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_CACHEFILE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_CAMERA.png")
    img.alpha_mode = "PREMUL"
    IM_ID_CAMERA = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_COLLECTION.png")
    img.alpha_mode = "PREMUL"
    IM_ID_COLLECTION = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_CURVE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_CURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_CURVES.png")
    img.alpha_mode = "PREMUL"
    IM_ID_CURVES = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_FONT.png")
    img.alpha_mode = "PREMUL"
    IM_ID_FONT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_GREASEPENCIL.png")
    img.alpha_mode = "PREMUL"
    IM_ID_GREASEPENCIL = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_IMAGE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_IMAGE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_KEY.png")
    img.alpha_mode = "PREMUL"
    IM_ID_KEY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_LATTICE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_LATTICE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_LIBRARY.png")
    img.alpha_mode = "PREMUL"
    IM_ID_LIBRARY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_LIGHT.png")
    img.alpha_mode = "PREMUL"
    IM_ID_LIGHT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_LIGHT_PROBE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_LIGHT_PROBE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_LINESTYLE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_LINESTYLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_MASK.png")
    img.alpha_mode = "PREMUL"
    IM_ID_MASK = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_MATERIAL.png")
    img.alpha_mode = "PREMUL"
    IM_ID_MATERIAL = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_MESH.png")
    img.alpha_mode = "PREMUL"
    IM_ID_MESH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_META.png")
    img.alpha_mode = "PREMUL"
    IM_ID_META = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_MOVIECLIP.png")
    img.alpha_mode = "PREMUL"
    IM_ID_MOVIECLIP = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_NODETREE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_NODETREE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_OBJECT.png")
    img.alpha_mode = "PREMUL"
    IM_ID_OBJECT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_PAINTCURVE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_PAINTCURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_PALETTE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_PALETTE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_PARTICLE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_PARTICLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_POINTCLOUD.png")
    img.alpha_mode = "PREMUL"
    IM_ID_POINTCLOUD = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_SCENE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_SCENE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_SCREEN.png")
    img.alpha_mode = "PREMUL"
    IM_ID_SCREEN = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_SOUND.png")
    img.alpha_mode = "PREMUL"
    IM_ID_SOUND = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_SPEAKER.png")
    img.alpha_mode = "PREMUL"
    IM_ID_SPEAKER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_TEXT.png")
    img.alpha_mode = "PREMUL"
    IM_ID_TEXT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_TEXTURE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_TEXTURE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_VOLUME.png")
    img.alpha_mode = "PREMUL"
    IM_ID_VOLUME = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_WINDOWMANAGER.png")
    img.alpha_mode = "PREMUL"
    IM_ID_WINDOWMANAGER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_WORKSPACE.png")
    img.alpha_mode = "PREMUL"
    IM_ID_WORKSPACE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ID_WORLD.png")
    img.alpha_mode = "PREMUL"
    IM_ID_WORLD = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}invert.png")
    img.alpha_mode = "PREMUL"
    IM_invert = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}invert_y.png")
    img.alpha_mode = "PREMUL"
    IM_invert_y = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}IPO_CONSTANT.png")
    img.alpha_mode = "PREMUL"
    IM_IPO_CONSTANT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_current_true_even.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_current_true_even = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_current_true_even_dark.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_current_true_even_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_current_true_odd.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_current_true_odd = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_current_true_odd_dark.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_current_true_odd_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_false.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_false = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_false_dark.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_false_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_next_false_even.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_next_false_even = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_next_false_even_dark.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_next_false_even_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_next_false_odd.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_next_false_odd = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keyframe_next_false_odd_dark.png")
    img.alpha_mode = "PREMUL"
    IM_keyframe_next_false_odd_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}keying_set.png")
    img.alpha_mode = "PREMUL"
    IM_keying_set = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}KeymapEditor.png")
    img.alpha_mode = "PREMUL"
    IM_KeymapEditor = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LAPLACIANDEFORM.png")
    img.alpha_mode = "PREMUL"
    IM_LAPLACIANDEFORM = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LAPLACIANSMOOTH.png")
    img.alpha_mode = "PREMUL"
    IM_LAPLACIANSMOOTH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LATTICE.png")
    img.alpha_mode = "PREMUL"
    IM_LATTICE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LIBRARY_DATA_BROKEN.png")
    img.alpha_mode = "PREMUL"
    IM_LIBRARY_DATA_BROKEN = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LIBRARY_DATA_DIRECT.png")
    img.alpha_mode = "PREMUL"
    IM_LIBRARY_DATA_DIRECT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LIBRARY_DATA_OVERRIDE.png")
    img.alpha_mode = "PREMUL"
    IM_LIBRARY_DATA_OVERRIDE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LIBRARY_DATA_OVERRIDE_DISABLE.png")
    img.alpha_mode = "PREMUL"
    IM_LIBRARY_DATA_OVERRIDE_DISABLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LINCURVE.png")
    img.alpha_mode = "PREMUL"
    IM_LINCURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}LINEART.png")
    img.alpha_mode = "PREMUL"
    IM_LINEART = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}manual.png")
    img.alpha_mode = "PREMUL"
    IM_manual = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MASK.png")
    img.alpha_mode = "PREMUL"
    IM_MASK = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MATCUBE.png")
    img.alpha_mode = "PREMUL"
    IM_MATCUBE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_BG_SHOW_HOVER.png")
    img.alpha_mode = "PREMUL"
    IM_MD_BG_SHOW_HOVER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_BG_SHOW_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_MD_BG_SHOW_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_BG_SHOW_OFF_DRIVER.png")
    img.alpha_mode = "PREMUL"
    IM_MD_BG_SHOW_OFF_DRIVER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_BG_SHOW_OFF_KEYFRAME.png")
    img.alpha_mode = "PREMUL"
    IM_MD_BG_SHOW_OFF_KEYFRAME = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_BG_SHOW_ON.png")
    img.alpha_mode = "PREMUL"
    IM_MD_BG_SHOW_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_BG_SHOW_ON_DRIVER.png")
    img.alpha_mode = "PREMUL"
    IM_MD_BG_SHOW_ON_DRIVER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_BG_SHOW_ON_KEYFRAME.png")
    img.alpha_mode = "PREMUL"
    IM_MD_BG_SHOW_ON_KEYFRAME = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_LIBRARY_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_MD_LIBRARY_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_LIBRARY_ON.png")
    img.alpha_mode = "PREMUL"
    IM_MD_LIBRARY_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_MULTI_SORT.png")
    img.alpha_mode = "PREMUL"
    IM_MD_MULTI_SORT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_OVERRIDE_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_MD_OVERRIDE_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MD_OVERRIDE_ON.png")
    img.alpha_mode = "PREMUL"
    IM_MD_OVERRIDE_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MeshEditor.png")
    img.alpha_mode = "PREMUL"
    IM_MeshEditor = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MESH_CACHE.png")
    img.alpha_mode = "PREMUL"
    IM_MESH_CACHE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MESH_DEFORM.png")
    img.alpha_mode = "PREMUL"
    IM_MESH_DEFORM = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MESH_SEQUENCE_CACHE.png")
    img.alpha_mode = "PREMUL"
    IM_MESH_SEQUENCE_CACHE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MESH_TO_VOLUME.png")
    img.alpha_mode = "PREMUL"
    IM_MESH_TO_VOLUME = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}META_CUBE.png")
    img.alpha_mode = "PREMUL"
    IM_META_CUBE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MIRROR.png")
    img.alpha_mode = "PREMUL"
    IM_MIRROR = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MODIFIER.png")
    img.alpha_mode = "PREMUL"
    IM_MODIFIER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ModifierEditor.png")
    img.alpha_mode = "PREMUL"
    IM_ModifierEditor = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}MULTIRES.png")
    img.alpha_mode = "PREMUL"
    IM_MULTIRES = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}NOCURVE.png")
    img.alpha_mode = "PREMUL"
    IM_NOCURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}NODES.png")
    img.alpha_mode = "PREMUL"
    IM_NODES = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}NORMAL_EDIT.png")
    img.alpha_mode = "PREMUL"
    IM_NORMAL_EDIT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}objectpath.png")
    img.alpha_mode = "PREMUL"
    IM_objectpath = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OBJECT_DATA.png")
    img.alpha_mode = "PREMUL"
    IM_OBJECT_DATA = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}object_picker.png")
    img.alpha_mode = "PREMUL"
    IM_object_picker = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}object_picker_dark.png")
    img.alpha_mode = "PREMUL"
    IM_object_picker_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}object_picker_focus.png")
    img.alpha_mode = "PREMUL"
    IM_object_picker_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OCEAN.png")
    img.alpha_mode = "PREMUL"
    IM_OCEAN = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_DATA_GP_LAYER.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_DATA_GP_LAYER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_ARMATURE.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_ARMATURE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_CAMERA.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_CAMERA = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_CURVE.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_CURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_CURVES.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_CURVES = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_EMPTY.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_EMPTY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_FONT.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_FONT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_GREASEPENCIL.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_GREASEPENCIL = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_LATTICE.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_LATTICE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_LIGHT.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_LIGHT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_LIGHTPROBE.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_LIGHTPROBE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_MESH.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_MESH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_META.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_META = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_POINTCLOUD.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_POINTCLOUD = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_SPEAKER.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_SPEAKER = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_SURFACE.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_SURFACE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_UNKNOW.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_UNKNOW = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}OUTLINER_OB_VOLUME.png")
    img.alpha_mode = "PREMUL"
    IM_OUTLINER_OB_VOLUME = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}PARTICLE_INSTANCE.png")
    img.alpha_mode = "PREMUL"
    IM_PARTICLE_INSTANCE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}PARTICLE_SYSTEM.png")
    img.alpha_mode = "PREMUL"
    IM_PARTICLE_SYSTEM = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}paste.png")
    img.alpha_mode = "PREMUL"
    IM_paste = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}PHYSICS.png")
    img.alpha_mode = "PREMUL"
    IM_PHYSICS = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}pin.png")
    img.alpha_mode = "PREMUL"
    IM_pin = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}POINT.png")
    img.alpha_mode = "PREMUL"
    IM_POINT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}py_exp_off.png")
    img.alpha_mode = "PREMUL"
    IM_py_exp_off = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}py_exp_on.png")
    img.alpha_mode = "PREMUL"
    IM_py_exp_on = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}REMESH.png")
    img.alpha_mode = "PREMUL"
    IM_REMESH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}REMOVE.png")
    img.alpha_mode = "PREMUL"
    IM_REMOVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}REMOVE_focus.png")
    img.alpha_mode = "PREMUL"
    IM_REMOVE_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}rename.png")
    img.alpha_mode = "PREMUL"
    IM_rename = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}rename_focus.png")
    img.alpha_mode = "PREMUL"
    IM_rename_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}reset.png")
    img.alpha_mode = "PREMUL"
    IM_reset = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}reset_override.png")
    img.alpha_mode = "PREMUL"
    IM_reset_override = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}RESTRICT_INSTANCED_ON.png")
    img.alpha_mode = "PREMUL"
    IM_RESTRICT_INSTANCED_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}rna.png")
    img.alpha_mode = "PREMUL"
    IM_rna = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}RNDCURVE.png")
    img.alpha_mode = "PREMUL"
    IM_RNDCURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}ROOTCURVE.png")
    img.alpha_mode = "PREMUL"
    IM_ROOTCURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}rotation.png")
    img.alpha_mode = "PREMUL"
    IM_rotation = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}save.png")
    img.alpha_mode = "PREMUL"
    IM_save = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SCREW.png")
    img.alpha_mode = "PREMUL"
    IM_SCREW = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}search.png")
    img.alpha_mode = "PREMUL"
    IM_search = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SettingEditor.png")
    img.alpha_mode = "PREMUL"
    IM_SettingEditor = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_apps.png")
    img.alpha_mode = "PREMUL"
    IM_settings_apps = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_keymap.png")
    img.alpha_mode = "PREMUL"
    IM_settings_keymap = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_keymap_addon_key.png")
    img.alpha_mode = "PREMUL"
    IM_settings_keymap_addon_key = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_keymap_addon_key_area.png")
    img.alpha_mode = "PREMUL"
    IM_settings_keymap_addon_key_area = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_keymap_addon_key_global.png")
    img.alpha_mode = "PREMUL"
    IM_settings_keymap_addon_key_global = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_keymap_addon_key_text.png")
    img.alpha_mode = "PREMUL"
    IM_settings_keymap_addon_key_text = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_keymap_addon_key_valuebox.png")
    img.alpha_mode = "PREMUL"
    IM_settings_keymap_addon_key_valuebox = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_keymap_ops.png")
    img.alpha_mode = "PREMUL"
    IM_settings_keymap_ops = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_font.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_font = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_font_path.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_font_path = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_shadow.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_shadow = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_theme.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_theme = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_ui_color.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_ui_color = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_ui_color_foreground.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_ui_color_foreground = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_ui_color_hover.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_ui_color_hover = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_ui_color_taskbar.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_ui_color_taskbar = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_personalization_ui_color_window.png")
    img.alpha_mode = "PREMUL"
    IM_settings_personalization_ui_color_window = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_size.png")
    img.alpha_mode = "PREMUL"
    IM_settings_size = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_size_ui_size.png")
    img.alpha_mode = "PREMUL"
    IM_settings_size_ui_size = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system_about.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system_about = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system_all_settings.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system_all_settings = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system_control.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system_control = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system_display.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system_display = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system_expression.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system_expression = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system_library.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system_library = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}settings_system_menu.png")
    img.alpha_mode = "PREMUL"
    IM_settings_system_menu = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHAPEKEY.png")
    img.alpha_mode = "PREMUL"
    IM_SHAPEKEY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHARPCURVE.png")
    img.alpha_mode = "PREMUL"
    IM_SHARPCURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_IN_EDITMODE_DISABLE.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_IN_EDITMODE_DISABLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_IN_EDITMODE_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_IN_EDITMODE_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_IN_EDITMODE_ON.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_IN_EDITMODE_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_ON_CAGE_DISABLE.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_ON_CAGE_DISABLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_ON_CAGE_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_ON_CAGE_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_ON_CAGE_ON.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_ON_CAGE_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_RENDER_DISABLE.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_RENDER_DISABLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_RENDER_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_RENDER_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_RENDER_ON.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_RENDER_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_VIEWPORT_DISABLE.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_VIEWPORT_DISABLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_VIEWPORT_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_VIEWPORT_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHOW_VIEWPORT_ON.png")
    img.alpha_mode = "PREMUL"
    IM_SHOW_VIEWPORT_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SHRINKWRAP.png")
    img.alpha_mode = "PREMUL"
    IM_SHRINKWRAP = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SIMPLE_DEFORM.png")
    img.alpha_mode = "PREMUL"
    IM_SIMPLE_DEFORM = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SKIN.png")
    img.alpha_mode = "PREMUL"
    IM_SKIN = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SMOOTH.png")
    img.alpha_mode = "PREMUL"
    IM_SMOOTH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SMOOTHCURVE.png")
    img.alpha_mode = "PREMUL"
    IM_SMOOTHCURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SOFT_BODY.png")
    img.alpha_mode = "PREMUL"
    IM_SOFT_BODY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SOLIDIFY.png")
    img.alpha_mode = "PREMUL"
    IM_SOLIDIFY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SORTALPHA.png")
    img.alpha_mode = "PREMUL"
    IM_SORTALPHA = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SPHERECURVE.png")
    img.alpha_mode = "PREMUL"
    IM_SPHERECURVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SPREADSHEET.png")
    img.alpha_mode = "PREMUL"
    IM_SPREADSHEET = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}stop.png")
    img.alpha_mode = "PREMUL"
    IM_stop = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}stop_dark.png")
    img.alpha_mode = "PREMUL"
    IM_stop_dark = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SUBSURF.png")
    img.alpha_mode = "PREMUL"
    IM_SUBSURF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}SURFACE_DEFORM.png")
    img.alpha_mode = "PREMUL"
    IM_SURFACE_DEFORM = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}tb_active.png")
    img.alpha_mode = "PREMUL"
    IM_tb_active = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}tb_hover.png")
    img.alpha_mode = "PREMUL"
    IM_tb_hover = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}tb_start.png")
    img.alpha_mode = "PREMUL"
    IM_tb_start = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}title_button.png")
    img.alpha_mode = "PREMUL"
    IM_title_button = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TPAINT_HLT.png")
    img.alpha_mode = "PREMUL"
    IM_TPAINT_HLT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}transform.png")
    img.alpha_mode = "PREMUL"
    IM_transform = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TRASH.png")
    img.alpha_mode = "PREMUL"
    IM_TRASH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TRASH_focus.png")
    img.alpha_mode = "PREMUL"
    IM_TRASH_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TRIANGULATE.png")
    img.alpha_mode = "PREMUL"
    IM_TRIANGULATE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TRIA_DOWN.png")
    img.alpha_mode = "PREMUL"
    IM_TRIA_DOWN = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TRIA_DOWN_focus.png")
    img.alpha_mode = "PREMUL"
    IM_TRIA_DOWN_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TRIA_UP.png")
    img.alpha_mode = "PREMUL"
    IM_TRIA_UP = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}TRIA_UP_focus.png")
    img.alpha_mode = "PREMUL"
    IM_TRIA_UP_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}unfold.png")
    img.alpha_mode = "PREMUL"
    IM_unfold = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}unfold_focus.png")
    img.alpha_mode = "PREMUL"
    IM_unfold_focus = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}unpin.png")
    img.alpha_mode = "PREMUL"
    IM_unpin = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}USE_APPLY_ON_SPLINE_OFF.png")
    img.alpha_mode = "PREMUL"
    IM_USE_APPLY_ON_SPLINE_OFF = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}USE_APPLY_ON_SPLINE_ON.png")
    img.alpha_mode = "PREMUL"
    IM_USE_APPLY_ON_SPLINE_ON = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}UV_PROJECT.png")
    img.alpha_mode = "PREMUL"
    IM_UV_PROJECT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}UV_WARP.png")
    img.alpha_mode = "PREMUL"
    IM_UV_WARP = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}valuebox_left.png")
    img.alpha_mode = "PREMUL"
    IM_valuebox_left = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}valuebox_right.png")
    img.alpha_mode = "PREMUL"
    IM_valuebox_right = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}VARIABLE.png")
    img.alpha_mode = "PREMUL"
    IM_VARIABLE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}VERTEX_WEIGHT_EDIT.png")
    img.alpha_mode = "PREMUL"
    IM_VERTEX_WEIGHT_EDIT = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}VERTEX_WEIGHT_MIX.png")
    img.alpha_mode = "PREMUL"
    IM_VERTEX_WEIGHT_MIX = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}VERTEX_WEIGHT_PROXIMITY.png")
    img.alpha_mode = "PREMUL"
    IM_VERTEX_WEIGHT_PROXIMITY = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}VOLUME_DISPLACE.png")
    img.alpha_mode = "PREMUL"
    IM_VOLUME_DISPLACE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}VOLUME_TO_MESH.png")
    img.alpha_mode = "PREMUL"
    IM_VOLUME_TO_MESH = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}WARP.png")
    img.alpha_mode = "PREMUL"
    IM_WARP = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}WAVE.png")
    img.alpha_mode = "PREMUL"
    IM_WAVE = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}WEIGHTED_NORMAL.png")
    img.alpha_mode = "PREMUL"
    IM_WEIGHTED_NORMAL = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}WELD.png")
    img.alpha_mode = "PREMUL"
    IM_WELD = from_image(img)
    images_remove(img)
    img = images_load(f"{p0}WIREFRAME.png")
    img.alpha_mode = "PREMUL"
    IM_WIREFRAME = from_image(img)
    images_remove(img)
    ## */

    global GPU_ICON_STATE
    GPU_ICON_STATE = icon_subfolder
    #|
def reload_icon():

    load_gpu_texture()
    try: Admin.REDRAW()
    except: pass
    #|
def reload_font():


    blfLoad(handle.PATH_FONT0)
    blfLoad(handle.PATH_FONT1)

    try: Admin.REDRAW()
    except: pass
    #|


#| Level 2
def late_import():
    from ..  import VMD

    global m, handle, Admin, FONT0, FONT1, FONT_ACTIVE, D_geticon_Object, D_geticon_Modifier, D_geticon_DriverVar, D_geticon_dynamic_paint_surface_format, D_geticon_dynamic_paint_surface_type, D_geticon_init_color_type, D_icon_rm, D_geticon_falloff, D_geticon_domain, S_md_apply_on_spline, S_spline_modifier_types, S_icon_keyframe_true

    m = VMD.m
    handle = VMD.handle

    FONT_IDS = handle.FONT_IDS

    P = m.P
    col = P.color
    size = P.size
    Admin = m.Admin

    FONT0 = FONT_IDS[0]
    FONT1 = FONT_IDS[1]
    FONT_ACTIVE = FONT0
    from . md import S_md_apply_on_spline, S_spline_modifier_types

    # <<< 1line (0blg_global_color, 4,
    #     $lambda s: f'{s.split("=", 1)[0].strip()}, '$,
    #     $lambda s: f'global {s[: -2]}' + '\n'$,
    #     $lambda s: False  if s.lstrip()[0] == "#" else True$)
    global COL_win_title, COL_win_title_inactive, COL_win, COL_win_inactive, COL_win_rim, COL_win_shadow, COL_dd_title, COL_dd, COL_dd_rim, COL_dd_shadow, COL_font_shadow, COL_area, COL_box_area_region, COL_box_area_region_rim, COL_box_area_hover, COL_box_area_hover_rim, COL_box_area_header_bg, COL_block, COL_block_even, COL_block_title, COL_block_title_even, COL_block_calc_display, COL_block_calc_display_fo, COL_block_calc_button_bg, COL_block_fo, COL_block_guideline0, COL_block_guideline1, COL_box_tb, COL_box_tb_multibar, COL_box_text_active, COL_box_text_fo, COL_box_text, COL_box_text_rim, COL_box_text_ignore, COL_box_text_rim_ignore, COL_box_text_read, COL_box_text_read_rim, COL_box_color_rim, COL_box_color_rim_fo, COL_box_val, COL_box_val_rim, COL_box_val_ignore, COL_box_val_rim_ignore, COL_box_val_fo, COL_box_val_active, COL_box_val_bool, COL_box_val_bool_rim, COL_box_val_bool_fo, COL_box_val_bool_ignore, COL_box_val_bool_rim_ignore, COL_box_button, COL_box_button_rim, COL_box_button_ignore, COL_box_button_rim_ignore, COL_box_button_fo, COL_box_button_rim_fo, COL_box_button_active, COL_box_button_rim_active, COL_box_buttonoff, COL_box_buttonoff_rim, COL_box_buttonoff_fo, COL_box_buttonoff_rim_fo, COL_box_buttonon, COL_box_buttonon_rim, COL_box_buttonon_fo, COL_box_buttonon_rim_fo, COL_box_buttonon_ignore, COL_box_filter, COL_box_filter_rim, COL_box_filter_num_modal, COL_box_filter_num_modal_rim, COL_box_filter_region, COL_box_filter_region_rim, COL_box_filter_active_bg, COL_box_filter_select_bg, COL_box_filter_hover_bg, COL_box_cursor_beam, COL_box_cursor_beam_off, COL_box_text_selection, COL_box_text_selection_off, COL_box_scrollbar_bg, COL_box_scrollbar, COL_box_block_scrollbar_bg, COL_box_block_scrollbar, COL_box_setting_list_bg, COL_box_setting_list_active, COL_box_setting_list_active_rim, COL_box_blfbutton_text_hover, COL_box_blfbutton_text_hover_rim, COL_box_hue_bg, COL_box_selectbox_bg, COL_box_selectbox_rim, COL_box_selectbox_gap, COL_box_selectbox_subtract_bg, COL_box_selectbox_subtract_rim, COL_box_selectbox_subtract_gap, COL_preview_3d_dash, COL_preview_3d_dash2, COL_preview_3d_arc, COL_win_title_fg, COL_dd_title_fg, COL_box_text_fg, COL_box_text_fg_ignore, COL_box_text_read_fg, COL_box_val_fg, COL_box_val_fg_ignore, COL_box_val_fg_error, COL_box_filter_fg, COL_box_filter_fg_info, COL_box_filter_fg_label, COL_box_filter_fg_apply, COL_box_filter_fg_del, COL_box_setting_list_fg, COL_block_fg, COL_block_fg_ignore, COL_block_fg_info, COL_box_button_fg, COL_box_button_fg_ignore, COL_box_button_fg_info, COL_win_title_hover, COL_win_title_hover_red, COL_win_title_hover_hold, COL_win_title_hover_hold_red
    # >>>
    # <<< 1line (0blg_global_size, 4,
    #     $lambda s: f'{s.split("=", 1)[0].strip()}, '$,
    #     $lambda s: f'global {s[: -2]}' + '\n'$,
    #     $lambda s: False  if s.lstrip()[0] == "#" else True$)
    global SIZE_widget, SIZE_title, SIZE_border, SIZE_dd_border, SIZE_filter, SIZE_tb, SIZE_win_shadow_offset, SIZE_dd_shadow_offset, SIZE_shadow_softness, SIZE_setting_list_border, SIZE_block, SIZE_button, SIZE_preview, SIZE_foreground, SIZE_foreground_height, SIZE_widget_fac
    # >>>

    # /* 0blg_global_color
    # <<< 1ifmatch (0prefs_color, 4,
    #     $lambda line: (f'COL_{line.split(":", 1)[0].lstrip()} = col.{line.split(":", 1
    #         )[0].lstrip()}\n', True)$,
    #     $lambda line: ('', False)$,
    #     ${'Property('}$)
    COL_win_title = col.win_title
    COL_win_title_inactive = col.win_title_inactive
    COL_win = col.win
    COL_win_inactive = col.win_inactive
    COL_win_rim = col.win_rim
    COL_win_shadow = col.win_shadow
    COL_dd_title = col.dd_title
    COL_dd = col.dd
    COL_dd_rim = col.dd_rim
    COL_dd_shadow = col.dd_shadow
    COL_font_shadow = col.font_shadow
    COL_area = col.area
    COL_box_area_region = col.box_area_region
    COL_box_area_region_rim = col.box_area_region_rim
    COL_box_area_hover = col.box_area_hover
    COL_box_area_hover_rim = col.box_area_hover_rim
    COL_box_area_header_bg = col.box_area_header_bg
    COL_block = col.block
    COL_block_even = col.block_even
    COL_block_title = col.block_title
    COL_block_title_even = col.block_title_even
    COL_block_calc_display = col.block_calc_display
    COL_block_calc_display_fo = col.block_calc_display_fo
    COL_block_calc_button_bg = col.block_calc_button_bg
    COL_block_fo = col.block_fo
    COL_block_guideline0 = col.block_guideline0
    COL_block_guideline1 = col.block_guideline1
    COL_box_tb = col.box_tb
    COL_box_tb_multibar = col.box_tb_multibar
    COL_box_text_active = col.box_text_active
    COL_box_text_fo = col.box_text_fo
    COL_box_text = col.box_text
    COL_box_text_rim = col.box_text_rim
    COL_box_text_ignore = col.box_text_ignore
    COL_box_text_rim_ignore = col.box_text_rim_ignore
    COL_box_text_read = col.box_text_read
    COL_box_text_read_rim = col.box_text_read_rim
    COL_box_color_rim = col.box_color_rim
    COL_box_color_rim_fo = col.box_color_rim_fo
    COL_box_val = col.box_val
    COL_box_val_rim = col.box_val_rim
    COL_box_val_ignore = col.box_val_ignore
    COL_box_val_rim_ignore = col.box_val_rim_ignore
    COL_box_val_fo = col.box_val_fo
    COL_box_val_active = col.box_val_active
    COL_box_val_bool = col.box_val_bool
    COL_box_val_bool_rim = col.box_val_bool_rim
    COL_box_val_bool_fo = col.box_val_bool_fo
    COL_box_val_bool_ignore = col.box_val_bool_ignore
    COL_box_val_bool_rim_ignore = col.box_val_bool_rim_ignore
    COL_box_button = col.box_button
    COL_box_button_rim = col.box_button_rim
    COL_box_button_ignore = col.box_button_ignore
    COL_box_button_rim_ignore = col.box_button_rim_ignore
    COL_box_button_fo = col.box_button_fo
    COL_box_button_rim_fo = col.box_button_rim_fo
    COL_box_button_active = col.box_button_active
    COL_box_button_rim_active = col.box_button_rim_active
    COL_box_buttonoff = col.box_buttonoff
    COL_box_buttonoff_rim = col.box_buttonoff_rim
    COL_box_buttonoff_fo = col.box_buttonoff_fo
    COL_box_buttonoff_rim_fo = col.box_buttonoff_rim_fo
    COL_box_buttonon = col.box_buttonon
    COL_box_buttonon_rim = col.box_buttonon_rim
    COL_box_buttonon_fo = col.box_buttonon_fo
    COL_box_buttonon_rim_fo = col.box_buttonon_rim_fo
    COL_box_buttonon_ignore = col.box_buttonon_ignore
    COL_box_filter = col.box_filter
    COL_box_filter_rim = col.box_filter_rim
    COL_box_filter_num_modal = col.box_filter_num_modal
    COL_box_filter_num_modal_rim = col.box_filter_num_modal_rim
    COL_box_filter_region = col.box_filter_region
    COL_box_filter_region_rim = col.box_filter_region_rim
    COL_box_filter_active_bg = col.box_filter_active_bg
    COL_box_filter_select_bg = col.box_filter_select_bg
    COL_box_filter_hover_bg = col.box_filter_hover_bg
    COL_box_cursor_beam = col.box_cursor_beam
    COL_box_cursor_beam_off = col.box_cursor_beam_off
    COL_box_text_selection = col.box_text_selection
    COL_box_text_selection_off = col.box_text_selection_off
    COL_box_scrollbar_bg = col.box_scrollbar_bg
    COL_box_scrollbar = col.box_scrollbar
    COL_box_block_scrollbar_bg = col.box_block_scrollbar_bg
    COL_box_block_scrollbar = col.box_block_scrollbar
    COL_box_setting_list_bg = col.box_setting_list_bg
    COL_box_setting_list_active = col.box_setting_list_active
    COL_box_setting_list_active_rim = col.box_setting_list_active_rim
    COL_box_blfbutton_text_hover = col.box_blfbutton_text_hover
    COL_box_blfbutton_text_hover_rim = col.box_blfbutton_text_hover_rim
    COL_box_hue_bg = col.box_hue_bg
    COL_box_selectbox_bg = col.box_selectbox_bg
    COL_box_selectbox_rim = col.box_selectbox_rim
    COL_box_selectbox_gap = col.box_selectbox_gap
    COL_box_selectbox_subtract_bg = col.box_selectbox_subtract_bg
    COL_box_selectbox_subtract_rim = col.box_selectbox_subtract_rim
    COL_box_selectbox_subtract_gap = col.box_selectbox_subtract_gap
    COL_preview_3d_dash = col.preview_3d_dash
    COL_preview_3d_dash2 = col.preview_3d_dash2
    COL_preview_3d_arc = col.preview_3d_arc
    COL_win_title_fg = col.win_title_fg
    COL_dd_title_fg = col.dd_title_fg
    COL_box_text_fg = col.box_text_fg
    COL_box_text_fg_ignore = col.box_text_fg_ignore
    COL_box_text_read_fg = col.box_text_read_fg
    COL_box_val_fg = col.box_val_fg
    COL_box_val_fg_ignore = col.box_val_fg_ignore
    COL_box_val_fg_error = col.box_val_fg_error
    COL_box_filter_fg = col.box_filter_fg
    COL_box_filter_fg_info = col.box_filter_fg_info
    COL_box_filter_fg_label = col.box_filter_fg_label
    COL_box_filter_fg_apply = col.box_filter_fg_apply
    COL_box_filter_fg_del = col.box_filter_fg_del
    COL_box_setting_list_fg = col.box_setting_list_fg
    COL_block_fg = col.block_fg
    COL_block_fg_ignore = col.block_fg_ignore
    COL_block_fg_info = col.block_fg_info
    COL_box_button_fg = col.box_button_fg
    COL_box_button_fg_ignore = col.box_button_fg_ignore
    COL_box_button_fg_info = col.box_button_fg_info
    COL_win_title_hover = col.win_title_hover
    COL_win_title_hover_red = col.win_title_hover_red
    COL_win_title_hover_hold = col.win_title_hover_hold
    COL_win_title_hover_hold_red = col.win_title_hover_hold_red
    # >>>
    # */
    # /* 0blg_global_size
    # <<< 1ifmatch (0prefs_size, 4,
    #     $lambda line: (f'SIZE_{line.split(":", 1)[0].lstrip()} = size.{line.split(":", 1
    #         )[0].lstrip()}\n', True)$,
    #     $lambda line: ('', False)$,
    #     ${'Property('}$)
    SIZE_widget = size.widget
    SIZE_title = size.title
    SIZE_border = size.border
    SIZE_dd_border = size.dd_border
    SIZE_filter = size.filter
    SIZE_tb = size.tb
    SIZE_win_shadow_offset = size.win_shadow_offset
    SIZE_dd_shadow_offset = size.dd_shadow_offset
    SIZE_shadow_softness = size.shadow_softness
    SIZE_setting_list_border = size.setting_list_border
    SIZE_block = size.block
    SIZE_button = size.button
    SIZE_preview = size.preview
    SIZE_foreground = size.foreground
    SIZE_foreground_height = size.foreground_height
    SIZE_widget_fac = size.widget_fac
    # >>>
    # */

    upd_font_size()

    blg = VMD.utilbl.blg

    if hasattr(blg, "IM_ADD"):
        pass

    else:
        load_gpu_texture()

    D_geticon_Object = {
        'MESH': GpuImg_OUTLINER_OB_MESH,
        'CURVE': GpuImg_OUTLINER_OB_CURVE,
        'SURFACE': GpuImg_OUTLINER_OB_SURFACE,
        'META': GpuImg_OUTLINER_OB_META,
        'FONT': GpuImg_OUTLINER_OB_FONT,
        'CURVES': GpuImg_OUTLINER_OB_CURVES,
        'POINTCLOUD': GpuImg_OUTLINER_OB_POINTCLOUD,
        'VOLUME': GpuImg_OUTLINER_OB_VOLUME,
        'GPENCIL': GpuImg_OUTLINER_OB_GREASEPENCIL,
        'GREASEPENCIL': GpuImg_OUTLINER_OB_GREASEPENCIL,
        'ARMATURE': GpuImg_OUTLINER_OB_ARMATURE,
        'LATTICE': GpuImg_OUTLINER_OB_LATTICE,
        'EMPTY': GpuImg_OUTLINER_OB_EMPTY,
        'LIGHT': GpuImg_OUTLINER_OB_LIGHT,
        'LIGHT_PROBE': GpuImg_OUTLINER_OB_LIGHTPROBE,
        'CAMERA': GpuImg_OUTLINER_OB_CAMERA,
        'SPEAKER': GpuImg_OUTLINER_OB_SPEAKER
        }
    D_geticon_Modifier = {
        'DATA_TRANSFER': GpuImg_DATA_TRANSFER,
        'MESH_CACHE': GpuImg_MESH_CACHE,
        'MESH_SEQUENCE_CACHE': GpuImg_MESH_SEQUENCE_CACHE,
        'NORMAL_EDIT': GpuImg_NORMAL_EDIT,
        'WEIGHTED_NORMAL': GpuImg_WEIGHTED_NORMAL,
        'UV_PROJECT': GpuImg_UV_PROJECT,
        'UV_WARP': GpuImg_UV_WARP,
        'VERTEX_WEIGHT_EDIT': GpuImg_VERTEX_WEIGHT_EDIT,
        'VERTEX_WEIGHT_MIX': GpuImg_VERTEX_WEIGHT_MIX,
        'VERTEX_WEIGHT_PROXIMITY': GpuImg_VERTEX_WEIGHT_PROXIMITY,
        'ARRAY': GpuImg_ARRAY,
        'BEVEL': GpuImg_BEVEL,
        'BOOLEAN': GpuImg_BOOLEAN,
        'BUILD': GpuImg_BUILD,
        'DECIMATE': GpuImg_DECIMATE,
        'EDGE_SPLIT': GpuImg_EDGE_SPLIT,
        'NODES': GpuImg_NODES,
        'MASK': GpuImg_MASK,
        'MIRROR': GpuImg_MIRROR,
        'MESH_TO_VOLUME': GpuImg_MESH_TO_VOLUME,
        'MULTIRES': GpuImg_MULTIRES,
        'REMESH': GpuImg_REMESH,
        'SCREW': GpuImg_SCREW,
        'SKIN': GpuImg_SKIN,
        'SOLIDIFY': GpuImg_SOLIDIFY,
        'SUBSURF': GpuImg_SUBSURF,
        'TRIANGULATE': GpuImg_TRIANGULATE,
        'VOLUME_TO_MESH': GpuImg_VOLUME_TO_MESH,
        'WELD': GpuImg_WELD,
        'WIREFRAME': GpuImg_WIREFRAME,
        'ARMATURE': GpuImg_ARMATURE,
        'CAST': GpuImg_CAST,
        'CURVE': GpuImg_CURVE,
        'DISPLACE': GpuImg_DISPLACE,
        'HOOK': GpuImg_HOOK,
        'LAPLACIANDEFORM': GpuImg_LAPLACIANDEFORM,
        'LATTICE': GpuImg_LATTICE,
        'MESH_DEFORM': GpuImg_MESH_DEFORM,
        'SHRINKWRAP': GpuImg_SHRINKWRAP,
        'SIMPLE_DEFORM': GpuImg_SIMPLE_DEFORM,
        'SMOOTH': GpuImg_SMOOTH,
        'CORRECTIVE_SMOOTH': GpuImg_CORRECTIVE_SMOOTH,
        'LAPLACIANSMOOTH': GpuImg_LAPLACIANSMOOTH,
        'SURFACE_DEFORM': GpuImg_SURFACE_DEFORM,
        'WARP': GpuImg_WARP,
        'WAVE': GpuImg_WAVE,
        'VOLUME_DISPLACE': GpuImg_VOLUME_DISPLACE,
        'CLOTH': GpuImg_CLOTH,
        'COLLISION': GpuImg_COLLISION,
        'DYNAMIC_PAINT': GpuImg_DYNAMIC_PAINT,
        'EXPLODE': GpuImg_EXPLODE,
        'FLUID': GpuImg_FLUID,
        'OCEAN': GpuImg_OCEAN,
        'PARTICLE_INSTANCE': GpuImg_PARTICLE_INSTANCE,
        'PARTICLE_SYSTEM': GpuImg_PARTICLE_SYSTEM,
        'SOFT_BODY': GpuImg_SOFT_BODY,

        'GREASE_PENCIL_TEXTURE': GpuImg_GREASE_PENCIL_TEXTURE,
        'GREASE_PENCIL_TIME': GpuImg_GREASE_PENCIL_TIME,
        'GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY': GpuImg_GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY,
        'GREASE_PENCIL_VERTEX_WEIGHT_ANGLE': GpuImg_GREASE_PENCIL_VERTEX_WEIGHT_ANGLE,
        'GREASE_PENCIL_ARRAY': GpuImg_GREASE_PENCIL_ARRAY,
        'GREASE_PENCIL_BUILD': GpuImg_GREASE_PENCIL_BUILD,
        'GREASE_PENCIL_DASH': GpuImg_GREASE_PENCIL_DASH,
        'GREASE_PENCIL_ENVELOPE': GpuImg_GREASE_PENCIL_ENVELOPE,
        'GREASE_PENCIL_LENGTH': GpuImg_GREASE_PENCIL_LENGTH,
        'GREASE_PENCIL_MIRROR': GpuImg_GREASE_PENCIL_MIRROR,
        'GREASE_PENCIL_MULTIPLY': GpuImg_GREASE_PENCIL_MULTIPLY,
        'GREASE_PENCIL_OUTLINE': GpuImg_GREASE_PENCIL_OUTLINE,
        'GREASE_PENCIL_SIMPLIFY': GpuImg_GREASE_PENCIL_SIMPLIFY,
        'GREASE_PENCIL_SUBDIV': GpuImg_GREASE_PENCIL_SUBDIV,
        'LINEART': GpuImg_LINEART,
        'GREASE_PENCIL_ARMATURE': GpuImg_GREASE_PENCIL_ARMATURE,
        'GREASE_PENCIL_HOOK': GpuImg_GREASE_PENCIL_HOOK,
        'GREASE_PENCIL_LATTICE': GpuImg_GREASE_PENCIL_LATTICE,
        'GREASE_PENCIL_NOISE': GpuImg_GREASE_PENCIL_NOISE,
        'GREASE_PENCIL_OFFSET': GpuImg_GREASE_PENCIL_OFFSET,
        'GREASE_PENCIL_SHRINKWRAP': GpuImg_GREASE_PENCIL_SHRINKWRAP,
        'GREASE_PENCIL_SMOOTH': GpuImg_GREASE_PENCIL_SMOOTH,
        'GREASE_PENCIL_THICKNESS': GpuImg_GREASE_PENCIL_THICKNESS,
        'GREASE_PENCIL_COLOR': GpuImg_GREASE_PENCIL_COLOR,
        'GREASE_PENCIL_TINT': GpuImg_GREASE_PENCIL_TINT,
        'GREASE_PENCIL_OPACITY': GpuImg_GREASE_PENCIL_OPACITY,
        }
    D_geticon_DriverVar = {
        'SINGLE_PROP': GpuImg_rna,
        'TRANSFORMS': GpuImg_transform,
        'ROTATION_DIFF': GpuImg_rotation,
        'LOC_DIFF': GpuImg_distance,
        'CONTEXT_PROP': GpuImg_context_property,
        }
    D_geticon_dynamic_paint_surface_format = {
        'VERTEX': GpuImg_ID_MESH,
        'IMAGE': GpuImg_ID_IMAGE,
        }
    D_geticon_dynamic_paint_surface_type = {
        'PAINT': GpuImg_TPAINT_HLT,
        'DISPLACE': GpuImg_DISPLACE,
        'WEIGHT': GpuImg_VERTEX_WEIGHT_PROXIMITY,
        'WAVE': GpuImg_WAVE,
        }
    D_geticon_init_color_type = {
        'COLOR': GpuImg_ID_PALETTE,
        'TEXTURE': GpuImg_ID_TEXTURE,
        'VERTEX_COLOR': GpuImg_GROUP_VCOL,
        }
    D_geticon_falloff = {
        "SMOOTH": GpuImg_SMOOTHCURVE,
        "SPHERE": GpuImg_SPHERECURVE,
        "ROOT": GpuImg_ROOTCURVE,
        "INVERSE_SQUARE": GpuImg_ROOTCURVE,
        "SHARP": GpuImg_SHARPCURVE,
        "LINEAR": GpuImg_LINCURVE,
        "CONSTANT": GpuImg_NOCURVE,
        "CURVE": GpuImg_RNDCURVE,
        "RANDOM": GpuImg_RNDCURVE,
        "STEP": GpuImg_IPO_CONSTANT,
        "ICON_SPHERECURVE": GpuImg_SPHERECURVE,
        "RND": GpuImg_NOCURVE,
        }
    D_geticon_domain = {
        "POINT": GpuImg_POINT,
        "EDGE": GpuImg_EDGE,
        "FACE": GpuImg_FACE,
        "CORNER": GpuImg_FACE_CORNER,
        "CURVE": GpuImg_CURVE,
        "INSTANCE": GpuImg_PARTICLE_INSTANCE,
        "LAYER": GpuImg_cache_layer,
        }

    D_icon_rm = {
        "dd_copy": GpuImg_copy,
        "dd_paste": GpuImg_paste,
        "valbox_reset_single": GpuImg_reset,
        "detail": GpuImg_manual,
        "rename": GpuImg_rename,
        "ui_add_to_keying_set": GpuImg_keying_set,
        "ui_copy_data_path": GpuImg_rna,
        "ui_copy_full_data_path": GpuImg_context_property,
        "ui_add_driver": GpuImg_driver_true,
        "ui_insert_keyframe": GpuImg_keyframe_current_true_even,
        "ui_delete_keyframe": GpuImg_keyframe_next_false_odd,
        "ui_clear_keyframe": GpuImg_keyframe_false,
        "ui_attr_toggle": GpuImg_SPREADSHEET,

        "Assign Operator Shortcut": GpuImg_assign,
        }

    S_icon_keyframe_true = {
        GpuImg_keyframe_current_true_even,
        GpuImg_keyframe_current_true_odd,
        GpuImg_keyframe_current_true_even_dark,
        GpuImg_keyframe_current_true_odd_dark,
        GpuImg_driver_ref,
        GpuImg_driver_ref_dark,
        }
    #|
