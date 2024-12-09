











import bpy

timer_reg = bpy.app.timers.register
timer_unreg = bpy.app.timers.unregister
timer_isreg = bpy.app.timers.is_registered

from struct import pack as struct_pack
from struct import unpack as struct_unpack
from ast import literal_eval
from collections import OrderedDict

from . import util

# <<< 1mp (util.types
types = util.types
NameValue = types.NameValue
Dictlist = types.Dictlist
EnumItem = types.EnumItem
# >>>


D_KEYINT_ODD = {
    'BUTTON4MOUSE': 4,
    'BUTTON5MOUSE': 5,
    'BUTTON6MOUSE': 6,
    'BUTTON7MOUSE': 7,
    'WHEELUPMOUSE': 16,
    'WHEELDOWNMOUSE': 17,
    'WHEELINMOUSE': 18,
    'WHEELOUTMOUSE': 19,
    'MEDIA_PLAY': 134,
    'MEDIA_STOP': 135,
    'MEDIA_FIRST': 136,
    'MEDIA_LAST': 137,
    'NDOF_MOTION': 148,
    'NDOF_BUTTON_MENU': 149,
    'NDOF_BUTTON_FIT': 150,
    'NDOF_BUTTON_TOP': 151,
    'NDOF_BUTTON_BOTTOM': 152,
    'NDOF_BUTTON_LEFT': 153,
    'NDOF_BUTTON_RIGHT': 154,
    'NDOF_BUTTON_FRONT': 155,
    'NDOF_BUTTON_BACK': 156,
    'NDOF_BUTTON_ISO1': 157,
    'NDOF_BUTTON_ISO2': 158,
    'NDOF_BUTTON_ROLL_CW': 159,
    'NDOF_BUTTON_ROLL_CCW': 160,
    'NDOF_BUTTON_SPIN_CW': 161,
    'NDOF_BUTTON_SPIN_CCW': 162,
    'NDOF_BUTTON_TILT_CW': 163,
    'NDOF_BUTTON_TILT_CCW': 164,
    'NDOF_BUTTON_ROTATE': 165,
    'NDOF_BUTTON_PANZOOM': 166,
    'NDOF_BUTTON_DOMINANT': 167,
    'NDOF_BUTTON_PLUS': 168,
    'NDOF_BUTTON_MINUS': 169,
    'NDOF_BUTTON_V1': 170,
    'NDOF_BUTTON_V2': 171,
    'NDOF_BUTTON_V3': 172,
    'NDOF_BUTTON_1': 173,
    'NDOF_BUTTON_2': 174,
    'NDOF_BUTTON_3': 175,
    'NDOF_BUTTON_4': 176,
    'NDOF_BUTTON_5': 177,
    'NDOF_BUTTON_6': 178,
    'NDOF_BUTTON_7': 179,
    'NDOF_BUTTON_8': 180,
    'NDOF_BUTTON_9': 181,
    'NDOF_BUTTON_10': 182,
    'NDOF_BUTTON_A': 183,
    'NDOF_BUTTON_B': 184,
    'NDOF_BUTTON_C': 185,
    'ACTIONZONE_AREA': 186,
    'ACTIONZONE_REGION': 187,
    'ACTIONZONE_FULLSCREEN': 188,
    'XR_ACTION': 189}
D_KEYINT = {
    False: 0,
    'LEFTMOUSE': 1,
    'MIDDLEMOUSE': 2,
    'RIGHTMOUSE': 3,
    'A': 20,
    'B': 21,
    'C': 22,
    'D': 23,
    'E': 24,
    'F': 25,
    'G': 26,
    'H': 27,
    'I': 28,
    'J': 29,
    'K': 30,
    'L': 31,
    'M': 32,
    'N': 33,
    'O': 34,
    'P': 35,
    'Q': 36,
    'R': 37,
    'S': 38,
    'T': 39,
    'U': 40,
    'V': 41,
    'W': 42,
    'X': 43,
    'Y': 44,
    'Z': 45,
    'ZERO': 46,
    'ONE': 47,
    'TWO': 48,
    'THREE': 49,
    'FOUR': 50,
    'FIVE': 51,
    'SIX': 52,
    'SEVEN': 53,
    'EIGHT': 54,
    'NINE': 55,
    'LEFT_CTRL': 56,
    'LEFT_ALT': 57,
    'LEFT_SHIFT': 58,
    'RIGHT_ALT': 59,
    'RIGHT_CTRL': 60,
    'RIGHT_SHIFT': 61,
    'OSKEY': 62,
    'APP': 63,
    'GRLESS': 64,
    'ESC': 65,
    'TAB': 66,
    'RET': 67,
    'SPACE': 68,
    'LINE_FEED': 69,
    'BACK_SPACE': 70,
    'DEL': 71,
    'SEMI_COLON': 72,
    'PERIOD': 73,
    'COMMA': 74,
    'QUOTE': 75,
    'ACCENT_GRAVE': 76,
    'MINUS': 77,
    'PLUS': 78,
    'SLASH': 79,
    'BACK_SLASH': 80,
    'EQUAL': 81,
    'LEFT_BRACKET': 82,
    'RIGHT_BRACKET': 83,
    'LEFT_ARROW': 84,
    'DOWN_ARROW': 85,
    'RIGHT_ARROW': 86,
    'UP_ARROW': 87,
    'NUMPAD_2': 88,
    'NUMPAD_4': 89,
    'NUMPAD_6': 90,
    'NUMPAD_8': 91,
    'NUMPAD_1': 92,
    'NUMPAD_3': 93,
    'NUMPAD_5': 94,
    'NUMPAD_7': 95,
    'NUMPAD_9': 96,
    'NUMPAD_PERIOD': 97,
    'NUMPAD_SLASH': 98,
    'NUMPAD_ASTERIX': 99,
    'NUMPAD_0': 100,
    'NUMPAD_MINUS': 101,
    'NUMPAD_ENTER': 102,
    'NUMPAD_PLUS': 103,
    'F1': 104,
    'F2': 105,
    'F3': 106,
    'F4': 107,
    'F5': 108,
    'F6': 109,
    'F7': 110,
    'F8': 111,
    'F9': 112,
    'F10': 113,
    'F11': 114,
    'F12': 115,
    'F13': 116,
    'F14': 117,
    'F15': 118,
    'F16': 119,
    'F17': 120,
    'F18': 121,
    'F19': 122,
    'F20': 123,
    'F21': 124,
    'F22': 125,
    'F23': 126,
    'F24': 127,
    'PAUSE': 128,
    'INSERT': 129,
    'HOME': 130,
    'PAGE_UP': 131,
    'PAGE_DOWN': 132,
    'END': 133}
D_INTKEY = (
    False,
    'LEFTMOUSE',
    'MIDDLEMOUSE',
    'RIGHTMOUSE',
    'BUTTON4MOUSE',
    'BUTTON5MOUSE',
    'BUTTON6MOUSE',
    'BUTTON7MOUSE',
    'PEN',
    'ERASER',
    'MOUSEMOVE',
    'INBETWEEN_MOUSEMOVE',
    'TRACKPADPAN',
    'TRACKPADZOOM',
    'MOUSEROTATE',
    'MOUSESMARTZOOM',
    'WHEELUPMOUSE',
    'WHEELDOWNMOUSE',
    'WHEELINMOUSE',
    'WHEELOUTMOUSE',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
    'LEFT_CTRL',
    'LEFT_ALT',
    'LEFT_SHIFT',
    'RIGHT_ALT',
    'RIGHT_CTRL',
    'RIGHT_SHIFT',
    'OSKEY',
    'APP',
    'GRLESS',
    'ESC',
    'TAB',
    'RET',
    'SPACE',
    'LINE_FEED',
    'BACK_SPACE',
    'DEL',
    'SEMI_COLON',
    'PERIOD',
    'COMMA',
    'QUOTE',
    'ACCENT_GRAVE',
    'MINUS',
    'PLUS',
    'SLASH',
    'BACK_SLASH',
    'EQUAL',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'LEFT_ARROW',
    'DOWN_ARROW',
    'RIGHT_ARROW',
    'UP_ARROW',
    'NUMPAD_2',
    'NUMPAD_4',
    'NUMPAD_6',
    'NUMPAD_8',
    'NUMPAD_1',
    'NUMPAD_3',
    'NUMPAD_5',
    'NUMPAD_7',
    'NUMPAD_9',
    'NUMPAD_PERIOD',
    'NUMPAD_SLASH',
    'NUMPAD_ASTERIX',
    'NUMPAD_0',
    'NUMPAD_MINUS',
    'NUMPAD_ENTER',
    'NUMPAD_PLUS',
    'F1',
    'F2',
    'F3',
    'F4',
    'F5',
    'F6',
    'F7',
    'F8',
    'F9',
    'F10',
    'F11',
    'F12',
    'F13',
    'F14',
    'F15',
    'F16',
    'F17',
    'F18',
    'F19',
    'F20',
    'F21',
    'F22',
    'F23',
    'F24',
    'PAUSE',
    'INSERT',
    'HOME',
    'PAGE_UP',
    'PAGE_DOWN',
    'END',
    'MEDIA_PLAY',
    'MEDIA_STOP',
    'MEDIA_FIRST',
    'MEDIA_LAST',
    'TEXTINPUT',
    'WINDOW_DEACTIVATE',
    'TIMER',
    'TIMER0',
    'TIMER1',
    'TIMER2',
    'TIMER_JOBS',
    'TIMER_AUTOSAVE',
    'TIMER_REPORT',
    'TIMERREGION',
    'NDOF_MOTION',
    'NDOF_BUTTON_MENU',
    'NDOF_BUTTON_FIT',
    'NDOF_BUTTON_TOP',
    'NDOF_BUTTON_BOTTOM',
    'NDOF_BUTTON_LEFT',
    'NDOF_BUTTON_RIGHT',
    'NDOF_BUTTON_FRONT',
    'NDOF_BUTTON_BACK',
    'NDOF_BUTTON_ISO1',
    'NDOF_BUTTON_ISO2',
    'NDOF_BUTTON_ROLL_CW',
    'NDOF_BUTTON_ROLL_CCW',
    'NDOF_BUTTON_SPIN_CW',
    'NDOF_BUTTON_SPIN_CCW',
    'NDOF_BUTTON_TILT_CW',
    'NDOF_BUTTON_TILT_CCW',
    'NDOF_BUTTON_ROTATE',
    'NDOF_BUTTON_PANZOOM',
    'NDOF_BUTTON_DOMINANT',
    'NDOF_BUTTON_PLUS',
    'NDOF_BUTTON_MINUS',
    'NDOF_BUTTON_V1',
    'NDOF_BUTTON_V2',
    'NDOF_BUTTON_V3',
    'NDOF_BUTTON_1',
    'NDOF_BUTTON_2',
    'NDOF_BUTTON_3',
    'NDOF_BUTTON_4',
    'NDOF_BUTTON_5',
    'NDOF_BUTTON_6',
    'NDOF_BUTTON_7',
    'NDOF_BUTTON_8',
    'NDOF_BUTTON_9',
    'NDOF_BUTTON_10',
    'NDOF_BUTTON_A',
    'NDOF_BUTTON_B',
    'NDOF_BUTTON_C',
    'ACTIONZONE_AREA',
    'ACTIONZONE_REGION',
    'ACTIONZONE_FULLSCREEN',
    'XR_ACTION')

D_VALINT = {
    'ANY': 0b0,
    'PRESS': 0b1,
    'RELEASE': 0b10,
    'DOUBLE_PRESS': 0b11,
    'DOUBLE_RELEASE': 0b100,
    'DRAG': 0b101,
    'NORTH': 0b110,
    'NORTH_EAST': 0b111,
    'EAST': 0b1000,
    'SOUTH_EAST': 0b1001,
    'SOUTH': 0b1010,
    'SOUTH_WEST': 0b1011,
    'WEST': 0b1100,
    'NORTH_WEST': 0b1101,
    'NOTHING': 0b1110,
    'HOLD': 0b1111}
D_INTVAL = (
    'ANY',
    'PRESS',
    'RELEASE',
    'DOUBLE_PRESS',
    'DOUBLE_RELEASE',
    'DRAG',
    'NORTH',
    'NORTH_EAST',
    'EAST',
    'SOUTH_EAST',
    'SOUTH',
    'SOUTH_WEST',
    'WEST',
    'NORTH_WEST',
    'NOTHING',
    'HOLD')
ENUMS_keymap_value = Dictlist((
    EnumItem("PRESS", "Press", "Triggered when a keystroke is pressed"),
    EnumItem("RELEASE", "Release", "Triggered when a keystroke is released"),
    EnumItem("DOUBLE_PRESS", "Double Press", "Press the keystroke twice within the timer (Duration) and the mouse movement distance of each axis is less than double-click threshold"),
    EnumItem("DOUBLE_RELEASE", "Double Release", "Release the keystroke twice within the timer (Duration) and the mouse movement distance of each axis is less than double-click threshold"),
    EnumItem("DRAG", "Drag", "Drag Threshold exceeded while holding keystroke (Default 3 pixels)"),
    EnumItem("HOLD", "Hold", "Hold down the keystroke for a specified time (Duration)")))
ENUMS_keymap_value.default = "PRESS"

TIME_KEYS = {
    'DOUBLE_PRESS',
    'DOUBLE_RELEASE',
    'HOLD'}



def kill_evt():
    PRESS.clear()
    DRAG_TRUE.clear()
    HOLD_TRUE.clear()
    RELEASE_TRUE.clear()
    PRE_RELEASE.clear()
    PRE_DRAG.clear()
    PRE_HOLD.clear()

    for e in HOLD_CHECKING.values(): timer_unreg(e)
    HOLD_CHECKING.clear()

    for e in DOU_CHECKING.values(): timer_unreg(e[4])
    DOU_CHECKING.clear()
    DOU_TRUE.clear()

    AUTO_CLEAR.clear()
    #|
def kill_evt_except(except_keys={
        'LEFT_CTRL', 'RIGHT_CTRL', 'LEFT_SHIFT', 'RIGHT_SHIFT', 'LEFT_ALT', 'RIGHT_ALT', 'OSKEY'}):
    #|
    for k in PRESS.copy():
        if k in except_keys: continue
        del PRESS[k]

    DRAG_TRUE.clear()
    HOLD_TRUE.clear()
    RELEASE_TRUE.clear()
    PRE_RELEASE.clear()
    PRE_DRAG.clear()
    PRE_HOLD.clear()

    for e in HOLD_CHECKING.values(): timer_unreg(e)
    HOLD_CHECKING.clear()

    for e in DOU_CHECKING.values(): timer_unreg(e[4])
    DOU_CHECKING.clear()
    DOU_TRUE.clear()

    AUTO_CLEAR.clear()
    #|

def enable():
    global ENABLE
    if ENABLE: return

    ENABLE = True
    #|
def disable():
    global ENABLE
    if ENABLE == False: return

    ENABLE = False
    kill_evt()
    #|

def get_evt(evt):
    if ENABLE == False: return

    MOUSE[0] = evt.mouse_region_x
    MOUSE[1] = evt.mouse_region_y
    MOUSE_WINDOW[0] = evt.mouse_x
    MOUSE_WINDOW[1] = evt.mouse_y
    EVT_TYPE[0] = evt.type
    EVT_TYPE[1] = evt.value

    if evt.type == 'WINDOW_DEACTIVATE':
        kill_evt()
        return

    if AUTO_CLEAR:
        for e in AUTO_CLEAR: e()

    if evt.value == 'PRESS':
        if evt.type in D_KEYINT:
            PRESS[evt.type] = None
        elif evt.type in D_KEYINT_ODD:
            PRESS[evt.type] = None
            evt_type = evt.type

            def clear_fn():
                if evt_type in PRESS: del PRESS[evt_type]

            AUTO_CLEAR[clear_fn] = None
    elif evt.value == 'RELEASE':
        if evt.type in PRESS: del PRESS[evt.type]

        PRE_DRAG.clear()

        for k in HOLD_CHECKING: timer_unreg(HOLD_CHECKING[k])
        HOLD_CHECKING.clear()

    if PRE_RELEASE:
        for fx in PRE_RELEASE.copy(): fx()

    if PRE_DRAG:
        for k in PRE_DRAG.copy():
            if max(abs(evt.mouse_x - PRE_DRAG[k][0]), abs(evt.mouse_y - PRE_DRAG[k][1])) >= P.th_drag:
                MOUSE_OVERRIDE[0] = PRE_DRAG[k][2]
                MOUSE_OVERRIDE[1] = PRE_DRAG[k][3]

                del PRE_DRAG[k]
                DRAG_TRUE[k] = None
                AUTO_CLEAR[DRAG_TRUE.clear] = None

    if PRE_HOLD:
        for k in PRE_HOLD.copy():
            del PRE_HOLD[k]
            HOLD_TRUE[k] = None
            AUTO_CLEAR[HOLD_TRUE.clear] = None

    global LEN_PRESS
    LEN_PRESS = len(PRESS)
    #|

def is_first_press(identifier):
    ind = TRIGGER_IND[0]
    v = KEYMAPS[identifier].value0  if ind == 0 else KEYMAPS[identifier].value1
    if v == "PRESS":
        return EVT_TYPE[1] == "PRESS"
    else:
        return None
    #|

def r_end_trigger(identifier):
    #|
    e = TRIGGER_END[identifier][TRIGGER_IND[0]]
    if TRIGGER_IND[0] == 0:
        if KEYMAPS[identifier].end_value0 == 'PRESS':
            kill_evt_except()
            return e
    else:
        if KEYMAPS[identifier].end_value1 == 'PRESS':
            kill_evt_except()
            return e
    e()
    return e
    #|


def r_trigger_fn(km):
    is_trigger0 = D_TRIGGER_FNS[km.value0](km.types0, km.exact0, km.duration0)
    is_trigger1 = D_TRIGGER_FNS[km.value1](km.types1, km.exact1, km.duration1)

    def trigger_fn():
        if EVT_TYPE[0] == "TIMER_REPORT": return False

        if is_trigger0():
            TRIGGER_IND[0] = 0
            return True

        if is_trigger1():
            TRIGGER_IND[0] = 1
            return True

        return False

    return trigger_fn
    #|
def r_trigger_end_fn(km):
    is_trigger0 = D_TRIGGER_FNS[km.end_value0](km.types0, km.exact0, km.duration0)
    is_trigger1 = D_TRIGGER_FNS[km.end_value1](km.types1, km.exact1, km.duration1)

    return is_trigger0, is_trigger1
    #|
def r_trigger_False(km_types, km_exact, km_duration):
    return NF
    #|
def r_trigger_PRESS(km_types, km_exact, km_duration):
    ll = len(km_types)
    if ll == 0: return NF

    if km_exact:
        def is_trigger():
            if all(e in PRESS for e in km_types) and ll == LEN_PRESS:
                MOUSE_OVERRIDE[:] = MOUSE
                return True
            return False
    else:
        def is_trigger():
            if all(e in PRESS for e in km_types):
                MOUSE_OVERRIDE[:] = MOUSE
                return True
            return False

    return is_trigger
    #|
def r_trigger_RELEASE(km_types, km_exact, km_duration):
    ll = len(km_types)
    if ll == 0: return NF

    if km_exact:
        def pre_release():
            if all(e not in PRESS for e in km_types):
                del PRE_RELEASE[pre_release]
                if not PRESS:
                    RELEASE_TRUE[pre_release] = None
                    AUTO_CLEAR[RELEASE_TRUE.clear] = None

        def is_trigger():
            if pre_release in RELEASE_TRUE:
                MOUSE_OVERRIDE[:] = MOUSE
                return True

            if all(e in PRESS for e in km_types):
                PRE_RELEASE[pre_release] = None
            return False
    else:
        def pre_release():
            if any(e not in PRESS for e in km_types):
                del PRE_RELEASE[pre_release]
                RELEASE_TRUE[pre_release] = None
                AUTO_CLEAR[RELEASE_TRUE.clear] = None

        def is_trigger():
            if pre_release in RELEASE_TRUE:
                MOUSE_OVERRIDE[:] = MOUSE
                return True

            if all(e in PRESS for e in km_types):
                PRE_RELEASE[pre_release] = None
            return False

    return is_trigger
    #|
def r_trigger_DRAG(km_types, km_exact, km_duration):
    ll = len(km_types)
    if ll == 0: return NF

    if km_exact:
        def is_trigger():
            if is_trigger in DRAG_TRUE: return True
            if is_trigger in PRE_DRAG: return False

            if all(e in PRESS for e in km_types) and ll == LEN_PRESS:
                PRE_DRAG[is_trigger] = MOUSE_WINDOW[0], MOUSE_WINDOW[1], MOUSE[0], MOUSE[1]
            return False
    else:
        def is_trigger():
            if is_trigger in DRAG_TRUE: return True
            if is_trigger in PRE_DRAG: return False

            if all(e in PRESS for e in km_types):
                PRE_DRAG[is_trigger] = MOUSE_WINDOW[0], MOUSE_WINDOW[1], MOUSE[0], MOUSE[1]
            return False

    return is_trigger
    #|
def r_trigger_HOLD(km_types, km_exact, km_duration):
    #|
    ll = len(km_types)
    if ll == 0: return NF

    if km_exact:
        def is_trigger():
            if all(e in PRESS for e in km_types) and ll == LEN_PRESS:
                if is_trigger in HOLD_TRUE:
                    MOUSE_OVERRIDE[:] = MOUSE
                    return True

                if is_trigger in HOLD_CHECKING: return False

                def hold_fn():
                    if is_trigger in HOLD_CHECKING: del HOLD_CHECKING[is_trigger]
                    PRE_HOLD[is_trigger] = None
                    push_modal_safe()

                HOLD_CHECKING[is_trigger] = hold_fn
                timer_reg(hold_fn, first_interval=km_duration)
            return False
    else:
        def is_trigger():
            if all(e in PRESS for e in km_types):
                if is_trigger in HOLD_TRUE:
                    MOUSE_OVERRIDE[:] = MOUSE
                    return True

                if is_trigger in HOLD_CHECKING: return False

                def hold_fn():
                    if is_trigger in HOLD_CHECKING: del HOLD_CHECKING[is_trigger]
                    PRE_HOLD[is_trigger] = None
                    push_modal_safe()

                HOLD_CHECKING[is_trigger] = hold_fn
                timer_reg(hold_fn, first_interval=km_duration)
            return False

    return is_trigger
    #|
def r_trigger_DOUBLE_PRESS(km_types, km_exact, km_duration):
    ll = len(km_types)
    if ll == 0: return NF

    if km_exact:
        def is_trigger():
            if is_trigger in DOU_CHECKING and LEN_PRESS == 0:
                DOU_TRUE[is_trigger] = None
                return False

            if all(e in PRESS for e in km_types) and ll == LEN_PRESS:
                if is_trigger in DOU_CHECKING:
                    if is_trigger in DOU_TRUE:
                        del DOU_TRUE[is_trigger]
                        mou = DOU_CHECKING[is_trigger]
                        if max(abs(MOUSE_WINDOW[0] - mou[0]), abs(MOUSE_WINDOW[1] - mou[1])) >= P.th_double_click:
                            MOUSE_OVERRIDE[0] = mou[2]
                            MOUSE_OVERRIDE[1] = mou[3]
                            return True
                    return False

                def dou_fn():
                    if is_trigger in DOU_CHECKING: del DOU_CHECKING[is_trigger]
                    if is_trigger in DOU_TRUE: del DOU_TRUE[is_trigger]

                DOU_CHECKING[is_trigger] = MOUSE_WINDOW[0], MOUSE_WINDOW[1], MOUSE[0], MOUSE[1], dou_fn
                timer_reg(dou_fn, first_interval=km_duration)
            return False
    else:
        def is_trigger():
            if is_trigger in DOU_CHECKING and LEN_PRESS == 0:
                DOU_TRUE[is_trigger] = None
                return False

            if all(e in PRESS for e in km_types):
                if is_trigger in DOU_CHECKING:
                    if is_trigger in DOU_TRUE:
                        del DOU_TRUE[is_trigger]
                        mou = DOU_CHECKING[is_trigger]
                        if max(abs(MOUSE_WINDOW[0] - mou[0]), abs(MOUSE_WINDOW[1] - mou[1])) <= P.th_double_click:
                            MOUSE_OVERRIDE[0] = mou[2]
                            MOUSE_OVERRIDE[1] = mou[3]
                            return True
                    return False

                def dou_fn():
                    if is_trigger in DOU_CHECKING: del DOU_CHECKING[is_trigger]
                    if is_trigger in DOU_TRUE: del DOU_TRUE[is_trigger]

                DOU_CHECKING[is_trigger] = MOUSE_WINDOW[0], MOUSE_WINDOW[1], MOUSE[0], MOUSE[1], dou_fn
                timer_reg(dou_fn, first_interval=km_duration)
            return False

    return is_trigger
    #|
def r_trigger_DOUBLE_RELEASE(km_types, km_exact, km_duration):
    ll = len(km_types)
    if ll == 0: return NF

    is_trigger_release = r_trigger_RELEASE(km_types, km_exact, km_duration)

    def is_trigger():
        if is_trigger in DOU_CHECKING:
            if is_trigger_release():
                mou = DOU_CHECKING[is_trigger]
                return max(abs(MOUSE_WINDOW[0] - mou[0]), abs(MOUSE_WINDOW[1] - mou[1])) <= P.th_double_click
        elif is_trigger_release():
            def dou_fn():
                if is_trigger in DOU_CHECKING: del DOU_CHECKING[is_trigger]

            DOU_CHECKING[is_trigger] = MOUSE_WINDOW[0], MOUSE_WINDOW[1], MOUSE[0], MOUSE[1], dou_fn
            timer_reg(dou_fn, first_interval=km_duration)
        return False

    return is_trigger
    #|


def r_tran_types(int32):
    #| ret list[str], len: 0 to 4
    uint = r_unsign32(int32)
    k0 = D_INTKEY[uint & 255]
    if k0 is False: return []

    uint >>= 8
    k1 = D_INTKEY[uint & 255]
    if k1 is False: return [k0]

    uint >>= 8
    k2 = D_INTKEY[uint & 255]
    if k2 is False: return [k0, k1]

    uint >>= 8
    k3 = D_INTKEY[uint & 255]
    if k3 is False: return [k0, k1, k2]

    return [k0, k1, k2, k3]
    #|
def r_tran_duration(int32):
    #| ret float
    return struct_unpack('>f', struct_pack('>l', r_unsign32(int32)))[0]
    #|
def r_tran_value_exact(int32):
    #| ret tuple: value0, value1, exact0, exact1
    uint = r_unsign32(int32)
    v0 = D_INTVAL[uint & 255]

    uint >>= 8
    v1 = D_INTVAL[uint & 255]

    uint >>= 8
    e0 = bool(uint & 1)

    return v0, v1, e0, bool(uint >> 1 & 1)
    #|
def r_tran_end_value(int32):
    #| ret tuple: value0, value1
    uint = r_unsign32(int32)
    return D_INTVAL[uint & 255], D_INTVAL[uint >> 8 & 255]
    #|

def r_encry_types(ks):
    ks += [False] * (4 - len(ks))
    k1, k2, k3, k4 = ks

    v = D_KEYINT[k1]  if k1 in D_KEYINT else D_KEYINT_ODD[k1]
    v |= (D_KEYINT[k2]  if k2 in D_KEYINT else D_KEYINT_ODD[k2]) << 8
    v |= (D_KEYINT[k3]  if k3 in D_KEYINT else D_KEYINT_ODD[k3]) << 16
    v |= (D_KEYINT[k4]  if k4 in D_KEYINT else D_KEYINT_ODD[k4]) << 24
    v = r_sign32(v)
    return v
    #|
def r_encry_value_exact(value0, value1, exact0, exact1):
    return r_sign32(D_VALINT[value0] | D_VALINT[value1] << 8 | exact0 << 16 | exact1 << 17)
    #|
def r_encry_end_value(value0, value1):
    return r_sign32(D_VALINT[value0] | D_VALINT[value1] << 8)
    #|


class KeyMap:
    __slots__ = (
        'identifier',
        'types0',
        'types1',
        'duration0',
        'duration1',
        'value0',
        'value1',
        'exact0',
        'exact1',
        'use_end_key',
        'end_value0',
        'end_value1')

    def __init__(self, identifier, encrypted):
        #|
        self.use_end_key = len(encrypted) == 6

        self.identifier = identifier
        self.types0 = r_tran_types(encrypted[0])
        self.duration0 = r_tran_duration(encrypted[1])
        self.types1 = r_tran_types(encrypted[2])
        self.duration1 = r_tran_duration(encrypted[3])
        self.value0, self.value1, self.exact0, self.exact1 = r_tran_value_exact(encrypted[4])
        if self.use_end_key:
            self.end_value0, self.end_value1 = r_tran_end_value(encrypted[5])
        #|
    #|
    #|

def init_keymaps(P, recompile=True):

    try:
        KEYMAPS.clear()
        TRIGGER.clear()
        TRIGGER_END.clear()

        PP = P.keymaps
        # <<< 1ifmatch (0prefs_key, 8,
        #     $lambda line: (f'KEYMAPS["{line.split(":", 1)[0].lstrip()}"] = KeyMap("{line.split(
        #         ":", 1)[0].lstrip()}", PP.{line.split(":", 1)[0].lstrip()})\n', True)$,
        #     $lambda line: ('', False)$,
        #     ${'Property('}$)
        KEYMAPS["esc"] = KeyMap("esc", PP.esc)
        KEYMAPS["dd_esc"] = KeyMap("dd_esc", PP.dd_esc)
        KEYMAPS["click"] = KeyMap("click", PP.click)
        KEYMAPS["title_move"] = KeyMap("title_move", PP.title_move)
        KEYMAPS["title_button"] = KeyMap("title_button", PP.title_button)
        KEYMAPS["resize"] = KeyMap("resize", PP.resize)
        KEYMAPS["pan"] = KeyMap("pan", PP.pan)
        KEYMAPS["pan_win"] = KeyMap("pan_win", PP.pan_win)
        KEYMAPS["rm"] = KeyMap("rm", PP.rm)
        KEYMAPS["rm_km_toggle"] = KeyMap("rm_km_toggle", PP.rm_km_toggle)
        KEYMAPS["rm_km_change"] = KeyMap("rm_km_change", PP.rm_km_change)
        KEYMAPS["redo"] = KeyMap("redo", PP.redo)
        KEYMAPS["undo"] = KeyMap("undo", PP.undo)
        KEYMAPS["detail"] = KeyMap("detail", PP.detail)
        KEYMAPS["fold_all_recursive_toggle"] = KeyMap("fold_all_recursive_toggle", PP.fold_all_recursive_toggle)
        KEYMAPS["fold_all_toggle"] = KeyMap("fold_all_toggle", PP.fold_all_toggle)
        KEYMAPS["fold_recursive_toggle"] = KeyMap("fold_recursive_toggle", PP.fold_recursive_toggle)
        KEYMAPS["fold_toggle"] = KeyMap("fold_toggle", PP.fold_toggle)
        KEYMAPS["rename"] = KeyMap("rename", PP.rename)
        KEYMAPS["dd_match_end"] = KeyMap("dd_match_end", PP.dd_match_end)
        KEYMAPS["dd_match_case"] = KeyMap("dd_match_case", PP.dd_match_case)
        KEYMAPS["dd_match_whole_word"] = KeyMap("dd_match_whole_word", PP.dd_match_whole_word)
        KEYMAPS["dd_select_all"] = KeyMap("dd_select_all", PP.dd_select_all)
        KEYMAPS["dd_select_word"] = KeyMap("dd_select_word", PP.dd_select_word)
        KEYMAPS["dd_cut"] = KeyMap("dd_cut", PP.dd_cut)
        KEYMAPS["dd_paste"] = KeyMap("dd_paste", PP.dd_paste)
        KEYMAPS["dd_copy"] = KeyMap("dd_copy", PP.dd_copy)
        KEYMAPS["dd_del_all"] = KeyMap("dd_del_all", PP.dd_del_all)
        KEYMAPS["dd_del"] = KeyMap("dd_del", PP.dd_del)
        KEYMAPS["dd_del_word"] = KeyMap("dd_del_word", PP.dd_del_word)
        KEYMAPS["dd_del_chr"] = KeyMap("dd_del_chr", PP.dd_del_chr)
        KEYMAPS["dd_beam_line_begin_shift"] = KeyMap("dd_beam_line_begin_shift", PP.dd_beam_line_begin_shift)
        KEYMAPS["dd_beam_line_end_shift"] = KeyMap("dd_beam_line_end_shift", PP.dd_beam_line_end_shift)
        KEYMAPS["dd_beam_left_word_shift"] = KeyMap("dd_beam_left_word_shift", PP.dd_beam_left_word_shift)
        KEYMAPS["dd_beam_right_word_shift"] = KeyMap("dd_beam_right_word_shift", PP.dd_beam_right_word_shift)
        KEYMAPS["dd_beam_left_shift"] = KeyMap("dd_beam_left_shift", PP.dd_beam_left_shift)
        KEYMAPS["dd_beam_right_shift"] = KeyMap("dd_beam_right_shift", PP.dd_beam_right_shift)
        KEYMAPS["dd_beam_down_shift"] = KeyMap("dd_beam_down_shift", PP.dd_beam_down_shift)
        KEYMAPS["dd_beam_up_shift"] = KeyMap("dd_beam_up_shift", PP.dd_beam_up_shift)
        KEYMAPS["dd_beam_line_begin"] = KeyMap("dd_beam_line_begin", PP.dd_beam_line_begin)
        KEYMAPS["dd_beam_line_end"] = KeyMap("dd_beam_line_end", PP.dd_beam_line_end)
        KEYMAPS["dd_beam_left_word"] = KeyMap("dd_beam_left_word", PP.dd_beam_left_word)
        KEYMAPS["dd_beam_right_word"] = KeyMap("dd_beam_right_word", PP.dd_beam_right_word)
        KEYMAPS["dd_beam_left"] = KeyMap("dd_beam_left", PP.dd_beam_left)
        KEYMAPS["dd_beam_right"] = KeyMap("dd_beam_right", PP.dd_beam_right)
        KEYMAPS["dd_beam_down"] = KeyMap("dd_beam_down", PP.dd_beam_down)
        KEYMAPS["dd_beam_up"] = KeyMap("dd_beam_up", PP.dd_beam_up)
        KEYMAPS["dd_beam_end_shift"] = KeyMap("dd_beam_end_shift", PP.dd_beam_end_shift)
        KEYMAPS["dd_beam_start_shift"] = KeyMap("dd_beam_start_shift", PP.dd_beam_start_shift)
        KEYMAPS["dd_beam_end"] = KeyMap("dd_beam_end", PP.dd_beam_end)
        KEYMAPS["dd_beam_start"] = KeyMap("dd_beam_start", PP.dd_beam_start)
        KEYMAPS["dd_scroll_left_most"] = KeyMap("dd_scroll_left_most", PP.dd_scroll_left_most)
        KEYMAPS["dd_scroll_right_most"] = KeyMap("dd_scroll_right_most", PP.dd_scroll_right_most)
        KEYMAPS["dd_scroll_down_most"] = KeyMap("dd_scroll_down_most", PP.dd_scroll_down_most)
        KEYMAPS["dd_scroll_up_most"] = KeyMap("dd_scroll_up_most", PP.dd_scroll_up_most)
        KEYMAPS["dd_scroll_left"] = KeyMap("dd_scroll_left", PP.dd_scroll_left)
        KEYMAPS["dd_scroll_right"] = KeyMap("dd_scroll_right", PP.dd_scroll_right)
        KEYMAPS["dd_scroll_down"] = KeyMap("dd_scroll_down", PP.dd_scroll_down)
        KEYMAPS["dd_scroll_up"] = KeyMap("dd_scroll_up", PP.dd_scroll_up)
        KEYMAPS["dd_scroll_left_area"] = KeyMap("dd_scroll_left_area", PP.dd_scroll_left_area)
        KEYMAPS["dd_scroll_right_area"] = KeyMap("dd_scroll_right_area", PP.dd_scroll_right_area)
        KEYMAPS["dd_scroll_down_area"] = KeyMap("dd_scroll_down_area", PP.dd_scroll_down_area)
        KEYMAPS["dd_scroll_up_area"] = KeyMap("dd_scroll_up_area", PP.dd_scroll_up_area)
        KEYMAPS["dd_scroll"] = KeyMap("dd_scroll", PP.dd_scroll)
        KEYMAPS["dd_selection_shift"] = KeyMap("dd_selection_shift", PP.dd_selection_shift)
        KEYMAPS["dd_selection"] = KeyMap("dd_selection", PP.dd_selection)
        KEYMAPS["dd_confirm"] = KeyMap("dd_confirm", PP.dd_confirm)
        KEYMAPS["dd_confirm_area"] = KeyMap("dd_confirm_area", PP.dd_confirm_area)
        KEYMAPS["dd_linebreak"] = KeyMap("dd_linebreak", PP.dd_linebreak)
        KEYMAPS["dd_untab"] = KeyMap("dd_untab", PP.dd_untab)
        KEYMAPS["dd_tab"] = KeyMap("dd_tab", PP.dd_tab)
        KEYMAPS["dd_preview"] = KeyMap("dd_preview", PP.dd_preview)
        KEYMAPS["area_save_as_shapekey"] = KeyMap("area_save_as_shapekey", PP.area_save_as_shapekey)
        KEYMAPS["area_apply_as_shapekey"] = KeyMap("area_apply_as_shapekey", PP.area_apply_as_shapekey)
        KEYMAPS["area_apply"] = KeyMap("area_apply", PP.area_apply)
        KEYMAPS["area_del"] = KeyMap("area_del", PP.area_del)
        KEYMAPS["area_add"] = KeyMap("area_add", PP.area_add)
        KEYMAPS["area_active_down_most_shift"] = KeyMap("area_active_down_most_shift", PP.area_active_down_most_shift)
        KEYMAPS["area_active_up_most_shift"] = KeyMap("area_active_up_most_shift", PP.area_active_up_most_shift)
        KEYMAPS["area_active_down_shift"] = KeyMap("area_active_down_shift", PP.area_active_down_shift)
        KEYMAPS["area_active_up_shift"] = KeyMap("area_active_up_shift", PP.area_active_up_shift)
        KEYMAPS["area_active_down_most"] = KeyMap("area_active_down_most", PP.area_active_down_most)
        KEYMAPS["area_active_up_most"] = KeyMap("area_active_up_most", PP.area_active_up_most)
        KEYMAPS["area_active_down"] = KeyMap("area_active_down", PP.area_active_down)
        KEYMAPS["area_active_up"] = KeyMap("area_active_up", PP.area_active_up)
        KEYMAPS["area_sort"] = KeyMap("area_sort", PP.area_sort)
        KEYMAPS["area_sort_modal_cancel"] = KeyMap("area_sort_modal_cancel", PP.area_sort_modal_cancel)
        KEYMAPS["area_sort_modal_apply"] = KeyMap("area_sort_modal_apply", PP.area_sort_modal_apply)
        KEYMAPS["area_sort_modal_del"] = KeyMap("area_sort_modal_del", PP.area_sort_modal_del)
        KEYMAPS["area_sort_modal_sort"] = KeyMap("area_sort_modal_sort", PP.area_sort_modal_sort)
        KEYMAPS["area_selectbox_extend"] = KeyMap("area_selectbox_extend", PP.area_selectbox_extend)
        KEYMAPS["area_selectbox_subtract"] = KeyMap("area_selectbox_subtract", PP.area_selectbox_subtract)
        KEYMAPS["area_selectbox_new"] = KeyMap("area_selectbox_new", PP.area_selectbox_new)
        KEYMAPS["area_select_all_toggle"] = KeyMap("area_select_all_toggle", PP.area_select_all_toggle)
        KEYMAPS["area_select_extend"] = KeyMap("area_select_extend", PP.area_select_extend)
        KEYMAPS["area_select"] = KeyMap("area_select", PP.area_select)
        KEYMAPS["area_copy_to_selected"] = KeyMap("area_copy_to_selected", PP.area_copy_to_selected)
        KEYMAPS["area_unpin_to_last_selected"] = KeyMap("area_unpin_to_last_selected", PP.area_unpin_to_last_selected)
        KEYMAPS["area_pin_to_last_selected"] = KeyMap("area_pin_to_last_selected", PP.area_pin_to_last_selected)
        KEYMAPS["area_pin_to_last_toggle"] = KeyMap("area_pin_to_last_toggle", PP.area_pin_to_last_toggle)
        KEYMAPS["area_search"] = KeyMap("area_search", PP.area_search)
        KEYMAPS["valbox_drag"] = KeyMap("valbox_drag", PP.valbox_drag)
        KEYMAPS["valbox_drag_modal_fast"] = KeyMap("valbox_drag_modal_fast", PP.valbox_drag_modal_fast)
        KEYMAPS["valbox_drag_modal_slow"] = KeyMap("valbox_drag_modal_slow", PP.valbox_drag_modal_slow)
        KEYMAPS["valbox_reset_all"] = KeyMap("valbox_reset_all", PP.valbox_reset_all)
        KEYMAPS["valbox_reset_single"] = KeyMap("valbox_reset_single", PP.valbox_reset_single)
        KEYMAPS["valbox_dd"] = KeyMap("valbox_dd", PP.valbox_dd)
        KEYMAPS["ui_remove_from_keying_set_all"] = KeyMap("ui_remove_from_keying_set_all", PP.ui_remove_from_keying_set_all)
        KEYMAPS["ui_add_to_keying_set_all"] = KeyMap("ui_add_to_keying_set_all", PP.ui_add_to_keying_set_all)
        KEYMAPS["ui_remove_from_keying_set"] = KeyMap("ui_remove_from_keying_set", PP.ui_remove_from_keying_set)
        KEYMAPS["ui_add_to_keying_set"] = KeyMap("ui_add_to_keying_set", PP.ui_add_to_keying_set)
        KEYMAPS["ui_copy_full_data_path"] = KeyMap("ui_copy_full_data_path", PP.ui_copy_full_data_path)
        KEYMAPS["ui_copy_data_path"] = KeyMap("ui_copy_data_path", PP.ui_copy_data_path)
        KEYMAPS["ui_paste_full_data_path_as_driver"] = KeyMap("ui_paste_full_data_path_as_driver", PP.ui_paste_full_data_path_as_driver)
        KEYMAPS["ui_delete_driver"] = KeyMap("ui_delete_driver", PP.ui_delete_driver)
        KEYMAPS["ui_add_driver"] = KeyMap("ui_add_driver", PP.ui_add_driver)
        KEYMAPS["ui_clear_keyframe"] = KeyMap("ui_clear_keyframe", PP.ui_clear_keyframe)
        KEYMAPS["ui_delete_keyframe"] = KeyMap("ui_delete_keyframe", PP.ui_delete_keyframe)
        KEYMAPS["ui_insert_keyframe"] = KeyMap("ui_insert_keyframe", PP.ui_insert_keyframe)
        KEYMAPS["ui_jump_to_target"] = KeyMap("ui_jump_to_target", PP.ui_jump_to_target)
        KEYMAPS["ui_mark_asset"] = KeyMap("ui_mark_asset", PP.ui_mark_asset)
        KEYMAPS["ui_format_toggle"] = KeyMap("ui_format_toggle", PP.ui_format_toggle)
        KEYMAPS["ui_attr_toggle"] = KeyMap("ui_attr_toggle", PP.ui_attr_toggle)
        KEYMAPS["ui_batch"] = KeyMap("ui_batch", PP.ui_batch)
        KEYMAPS["ui_fold_recursive_toggle"] = KeyMap("ui_fold_recursive_toggle", PP.ui_fold_recursive_toggle)
        KEYMAPS["ui_fold_toggle"] = KeyMap("ui_fold_toggle", PP.ui_fold_toggle)
        # >>>

        for k, km in KEYMAPS.items():
            TRIGGER[k] = r_trigger_fn(km)

            if km.use_end_key:
                TRIGGER_END[k] = r_trigger_end_fn(km)
        return True
    except:
        (print("WARNING: Keymap compile error"))
        if recompile:
            for k, rna in PP.bl_rna.properties.items():
                setattr(PP, k, rna.default_array)

            init_keymaps(P, recompile=False)
        return False
    #|

def init_calc_exp(P):
    try:
        CALC_EXP.clear()
        CALC_EXP.update(literal_eval(P.calc_exp))

        success = True
    except:
        CALC_EXP.clear()
        CALC_EXP.update(prefs.CALC_EXP_DEFAULT)

        success = False

    ITEMS_CALC_TAB[:] = [NameValue(name, i)  for i, name in enumerate(CALC_EXP)]
    return success
    #
    # r = len(ITEMS_CALC_TAB)
    # for r in range(len(ITEMS_CALC_TAB), 20):
    #     ITEMS_CALC_TAB.append(NameValue(f"test {r}", r))
    #
    #|
def write_calc_exp(tx, P):
    CALC_EXP_copy = CALC_EXP.copy()
    ITEMS_CALC_TAB_copy = ITEMS_CALC_TAB[:]
    calc_exp_copy = P.calc_exp
    try:
        dic = literal_eval(tx)
        if not isinstance(dic, dict): return "The output is not a dictionary."
        for k in {"Float", "Int", "Radians", "Degrees"}:
            if k not in dic: return f"The '{k}' key must be included in the dictionary."
        for k, o in dic.items():
            if not isinstance(k, str): return f"key '{k}' in dictionary is not a string."
            if isinstance(o, tuple) or isinstance(o, list): pass
            else: return f"value of key '{k}' in dictionary is not a list or tuple."
            if len(o) != 10: return f"The length of value in key '{k}' must be equal to 10."
            for oo in o:
                if isinstance(oo, tuple) or isinstance(oo, list): pass
                else: return f"{oo} is not a list or tuple in key '{k}'"
                if len(oo) != 2: return f"{oo} must contain 2 item in Key '{k}'.\n['Name', 'Experssion']"
                name, exp = oo
                if not isinstance(name, str): return f"{oo} first item is not a string.\nError In Key '{k}'"
                if not isinstance(exp, str): return f"{oo} second item is not a string.\nError In Key '{k}'"

        ITEMS_CALC_TAB[:] = [NameValue(name, i)  for i, name in enumerate(dic)]
        CALC_EXP.clear()
        CALC_EXP.update(dic)
        P.calc_exp = tx
        return None
    except Exception as e:
        CALC_EXP.clear()
        CALC_EXP.update(CALC_EXP_copy)
        ITEMS_CALC_TAB[:] = ITEMS_CALC_TAB_copy
        P.calc_exp = calc_exp_copy
        return e
    #|

def rm_get_info_km(e):
    if e.identifier not in KEYMAPS: return ""
    km = KEYMAPS[e.identifier]
    if km.types0:
        if km.types1:
            return ", ".join(e.lower().replace('_', ' ').capitalize()  for e in km.types0) + f" [{km.value0.lower().replace('_', ' ').capitalize()}]  |  " + ", ".join(e.lower().replace('_', ' ').capitalize()  for e in km.types1) + f" [{km.value1.lower().replace('_', ' ').capitalize()}]"
        return ", ".join(e.lower().replace('_', ' ').capitalize()  for e in km.types0) + f" [{km.value0.lower().replace('_', ' ').capitalize()}]"
    elif km.types1: return ", ".join(e.lower().replace('_', ' ').capitalize()  for e in km.types1) + f" [{km.value1.lower().replace('_', ' ').capitalize()}]"
    return ""
    #|

def write_keytype(ss, trigger_id, index, refresh=True):

    try:
        ls = ss.upper().split(',')
        prop = getattr(P.keymaps, trigger_id)

        if not ls[0].strip():
            if index == 0:
                if trigger_id == "click": return False, "This Keymap cannot be None."
                prop[0] = 0
                if refresh: init_keymaps(P)
            else:
                prop[2] = 0
                if refresh: init_keymaps(P)
            return True, ""

        if len(set(ls)) > 4: return False, "Key combinations cannot exceed 4."

        ls = list(OrderedDict.fromkeys(e.strip().upper().replace(' ', '_')  for e in ls))
        message = ""
        for s in ls:
            if s in D_KEYINT or s in D_KEYINT_ODD:
                if trigger_id not in {'esc', 'dd_esc'}:
                    if s == "ESC": message = "Keymaps containing the 'ESC' key may not function properly."
            else:
                return False, f"'{s}' is not in the key list"

        prop[0  if index == 0 else 2] = r_encry_types(ls)
        if refresh: init_keymaps(P)
        return True, message
    except Exception as e:
        return False, str(e)
    #|
def write_keyvalue(ss, trigger_id, index, refresh=True):
    ss = ss.strip().upper().replace(' ', '_')
    value_allow = {'PRESS', 'RELEASE', 'DOUBLE_PRESS', 'DOUBLE_RELEASE', 'DRAG', 'HOLD'}
    if ss not in value_allow: return False, f'{ss} not in {value_allow}'

    if trigger_id == "click": return False, "This Keymap value cannot be modified"

    try:
        prop = getattr(P.keymaps, trigger_id)
        value0, value1, exact0, exact1 = r_tran_value_exact(prop[4])
        if index == 0: value0 = ss
        else: value1 = ss
        prop[4] = r_encry_value_exact(value0, value1, exact0, exact1)
        if refresh: init_keymaps(P)
        return True, ""
    except Exception as e:
        return False, str(e)
    #|
def write_keyendvalue(ss, trigger_id, index, refresh=True):
    ss = ss.strip().upper().replace(' ', '_')
    value_allow = {'PRESS', 'RELEASE', 'DOUBLE_PRESS', 'DOUBLE_RELEASE', 'DRAG', 'HOLD'}
    if ss not in value_allow: return False, f'{ss} not in {value_allow}'

    if trigger_id == "click": return False, "This Keymap value cannot be modified"

    try:
        prop = getattr(P.keymaps, trigger_id)
        value0, value1 = r_tran_end_value(prop[5])
        if index == 0: value0 = ss
        else: value1 = ss
        prop[5] = r_encry_end_value(value0, value1)
        if refresh: init_keymaps(P)
        return True, ""
    except Exception as e:
        return False, str(e)
    #|
def write_keyexact(ss, trigger_id, index):
    if ss in {'True', 'TRUE', 'true', 1, 1.0, True}: boo = True
    elif ss in {'False', 'FALSE', 'false', 0, 0.0, False}: boo = False
    else: return False, "Value Error"

    try:
        prop = getattr(P.keymaps, trigger_id)
        value0, value1, exact0, exact1 = r_tran_value_exact(prop[4])
        if index == 0: exact0 = boo
        else: exact1 = boo
        prop[4] = r_encry_value_exact(value0, value1, exact0, exact1)
        init_keymaps(P)
        return True, ""
    except Exception as e:
        return False, str(e)
    #|
def write_keyduration(ss, trigger_id, index):
    try: v = float(ss)
    except: return False, "Cannot convert to Float"

    try:
        prop = getattr(P.keymaps, trigger_id)
        b = struct_pack('!f', min(max(0.0, v), 9.0))
        i = r_sign32(b[3] | b[2] << 8 | b[1] << 16 | b[0] << 24)
        if index == 0: prop[1] = i
        else: prop[3] = i
        init_keymaps(P)
        return True, ""
    except Exception as e:
        return False, str(e)
    #|

def r_keyinfo(rna, trigger_id, trigger_index):
    km = KEYMAPS[trigger_id]
    rna = P.keymaps.bl_rna.properties[trigger_id]
    if trigger_index == 0:
        km_types = ", ".join(km.types0)
        km_value = f"{km.value0}"
        km_duration = rs_format_float_left(km.duration0)
        km_exact = km.exact0
        km_end_value = km.end_value0  if km.use_end_key else ""
    else:
        km_types = ", ".join(km.types1)
        km_value = f"{km.value1}"
        km_duration = rs_format_float_left(km.duration1)
        km_exact = km.exact1
        km_end_value = km.end_value1  if km.use_end_key else ""

    s = (
        f"Name :  {rna.name}\nID :  {trigger_id}\nIndex :  {trigger_index}\n"
        f"Description :  {rna.description}\nCombination :  {km_types}\n"
        f"Is Exact :  {km_exact}\nValue :  {km_value}\n")
    if km_end_value:
        s += (
        f"End Value :  {km_end_value}\n"
        f"Duration :{km_duration} sec")
    else:
        s += (
        f"Duration :{km_duration} sec")
    return s
    #|
def r_keyrepeatinfo(keycatch_list, current_id_index=None):
    if not keycatch_list: return ""
    ls = []
    catch_set = set(keycatch_list)
    for identifier, km in KEYMAPS.items():
        if set(km.types0) == catch_set: ls.append((identifier, 0))
        if set(km.types1) == catch_set: ls.append((identifier, 1))

    if not ls: return ""
    if current_id_index == None:
        current_id = ""
        current_index = -1
    else:
        current_id, current_index = current_id_index

    rnas = P.keymaps.bl_rna.properties
    s = f"{len(ls)} existing Keymap(s) have this keybinding\n"
    for l in ls:
        if l[0] == current_id and l[1] == current_index:
            s += f'{rnas[l[0]].name} :  ID = {l[0]}, index = {l[1]}  (Current)\n'
        else:
            s += f'{rnas[l[0]].name} :  ID = {l[0]}, index = {l[1]}\n'
    return s
    #|

def r_shortcut_to_km(cats, keymap_category):
    if keymap_category not in cats: return None

    cat = cats[keymap_category]
    shortcut_to_km = {}
    for kmi in cat.keymap_items:
        if kmi.active:
            if kmi.type == "NONE": continue
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

            if km_keys in shortcut_to_km:
                shortcut_to_km[km_keys].append(f"{kmi.idname} ({kmi.name})")
            else:
                shortcut_to_km[km_keys] = [f"{kmi.idname} ({kmi.name})"]

    return shortcut_to_km
    #|
def r_shortcutrepeatinfo(tuple_keys, shortcut_to_km):
    if tuple_keys in shortcut_to_km:
        shortcuts = shortcut_to_km[tuple_keys]
        return f"{len(shortcuts)} existing Shortcut(s) have this keybinding\n    " + "\n    ".join(shortcuts)
    else:
        return ""
    #|
def r_bl_keymap(idname, keymaps):
    for km in keymaps:
        if idname in km.keymap_items:
            return km

    return None
    #|


# in handle
def late_import():
    #|
    from .  import VMD

    prefs = VMD.prefs

    # <<< 1mp (VMD.m
    m = VMD.m
    P = m.P
    Admin = m.Admin
    push_modal_safe = m.push_modal_safe
    # >>>

    util = VMD.util

    # <<< 1mp (util.com
    com = util.com
    NF = com.NF
    rs_format_float_left = com.rs_format_float_left
    # >>>

    # <<< 1mp (util.num
    num = util.num
    r_unsign32 = num.r_unsign32
    r_sign32 = num.r_sign32
    # >>>


    KEYMAPS = {}
    TRIGGER = {}
    TRIGGER_END = {}
    TRIGGER_IND = [0]
    MOUSE = [0, 0] # event.region_mouse
    MOUSE_WINDOW = [0, 0] # event.mouse
    MOUSE_OVERRIDE = [0, 0]
    EVT_TYPE = ['', ''] # type, value


    PRESS = {}

    PRE_RELEASE = {}
    RELEASE_TRUE = {}

    PRE_DRAG = {}
    DRAG_TRUE = {}

    PRE_HOLD = {}
    HOLD_TRUE = {}
    HOLD_CHECKING = {}

    DOU_TRUE = {}
    DOU_CHECKING = {}

    AUTO_CLEAR = {}
    ENABLE = True
    LEN_PRESS = 0

    CALC_EXP = {}
    ITEMS_CALC_TAB = []

    D_TRIGGER_FNS = {
        'ANY': r_trigger_False,
        'PRESS': r_trigger_PRESS,
        'RELEASE': r_trigger_RELEASE,
        'DOUBLE_PRESS': r_trigger_DOUBLE_PRESS,
        'DOUBLE_RELEASE': r_trigger_DOUBLE_RELEASE,
        'DRAG': r_trigger_DRAG,
        'NORTH': r_trigger_False,
        'NORTH_EAST': r_trigger_False,
        'EAST': r_trigger_False,
        'SOUTH_EAST': r_trigger_False,
        'SOUTH': r_trigger_False,
        'SOUTH_WEST': r_trigger_False,
        'WEST': r_trigger_False,
        'NORTH_WEST': r_trigger_False,
        'NOTHING': r_trigger_False,
        'HOLD': r_trigger_HOLD}

    globals().update(locals())
    #|
