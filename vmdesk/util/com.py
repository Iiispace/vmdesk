from math import floor

from . deco import successResult
from . const import (
    STR_AZ_az_09,
    STR_AZ_az,
    STR_a_z,
    STR_break_sign,
    INT_min,
    INT_max,
    FLOAT_min,
    FLOAT_max)


def N(): pass
def NF(): return False
def NT(): return True
def NS(): return ""
def N1(x): return
def NF1(x): return False
def NT1(x): return True
def NKW(**kw): pass


def bin_search(min_ind, max_ind, v, fx, exc= lambda x: -1):
    #|
    low = min_ind
    high = max_ind
    i = 0

    while low <= high:
        i = (low + high) // 2
        fxi = fx(i)
        if fxi < v: low = i + 1
        elif fxi > v: high = i - 1
        else: return i

    return exc(i)
    #|
def bin_search_fc_anim(kp, v):
    #|
    low = 0
    high = len(kp) - 1
    i = 0

    while low <= high:
        i = (low + high) // 2
        fxi = kp[i].co[0]
        if fxi < v: low = i + 1
        elif fxi > v: high = i - 1
        else: return i

    return None
    #|

def bin_search_continue(fx, v_min, v_max, th=0.0000001):
    #|
    if fx(v_max) == False: return None

    low = v_min
    high = v_max

    while (high - low) > th:
        v = (low + high) / 2
        if fx(v) == True: high = v
        else: low = v

    return high
    #|


def filter_match_case(line, tx):
    #|
    return tx in line
    #|
def filter_ignore_case(line, tx):
    #|
    return tx.lower() in line.lower()
    #|
def filter_match_whole_word_match_case(line, tx):
    #|
    len_line = len(line)
    len_tx = len(tx)
    i = 0

    while i < len_line:
        i0 = line.find(tx, i)
        if i0 == -1: return False

        i1 = i0 + len_tx

        if i0 == 0:
            if i1 >= len_line or line[i1 - 1] in STR_break_sign: return True

            if line[i1] not in STR_AZ_az: return True
        else:
            if line[i0 - 1] not in STR_AZ_az or line[i0] in STR_break_sign:
                if i1 >= len_line or line[i1 - 1] in STR_break_sign: return True

                if line[i1] not in STR_AZ_az: return True

        i = i1

    return False
    #|
def filter_match_whole_word_ignore_case(line, tx):
    #|
    line = line.lower()
    tx = tx.lower()

    len_line = len(line)
    len_tx = len(tx)
    i = 0

    while i < len_line:
        i0 = line.find(tx, i)
        if i0 == -1: return False

        i1 = i0 + len_tx

        if i0 == 0:
            if i1 >= len_line or line[i1 - 1] in STR_break_sign: return True

            if line[i1] not in STR_a_z: return True
        else:
            if line[i0 - 1] not in STR_a_z or line[i0] in STR_break_sign:
                if i1 >= len_line or line[i1 - 1] in STR_break_sign: return True

                if line[i1] not in STR_a_z: return True

        i = i1

    return False
    #|

def filter_match_case_end_left(line, tx):
    #|
    return line[: len(tx)] == tx
    #|
def filter_ignore_case_end_left(line, tx):
    #|
    return line.lower()[: len(tx)] == tx.lower()
    #|
def filter_match_whole_word_match_case_end_left(line, tx):
    #|
    len_tx = len(tx)

    if line[: len_tx] == tx:
        if len_tx == len(line): return True

        return line[len_tx - 1] in STR_break_sign or line[len_tx] not in STR_AZ_az
    return False
    #|
def filter_match_whole_word_ignore_case_end_left(line, tx):
    #|
    line = line.lower()
    tx = tx.lower()

    len_tx = len(tx)

    if line[: len_tx] == tx:
        if len_tx == len(line): return True

        return line[len_tx - 1] in STR_break_sign or line[len_tx] not in STR_a_z
    return False
    #|
def filter_match_case_end_right(line, tx):
    #|
    return line[- len(tx) :] == tx
    #|
def filter_ignore_case_end_right(line, tx):
    #|
    return line.lower()[- len(tx) :] == tx.lower()
    #|
def filter_match_whole_word_match_case_end_right(line, tx):
    #|
    len_tx = len(tx)

    if line[- len_tx :] == tx:
        if len_tx == len(line): return True

        return line[- len_tx] in STR_break_sign or line[- len_tx - 1] not in STR_AZ_az
    return False
    #|
def filter_match_whole_word_ignore_case_end_right(line, tx):
    #|
    line = line.lower()
    tx = tx.lower()

    len_tx = len(tx)

    if line[- len_tx :] == tx:
        if len_tx == len(line): return True

        return line[- len_tx] in STR_break_sign or line[- len_tx - 1] not in STR_a_z
    return False
    #|

def r_filter_function(match_case, match_whole_word, match_end):
    if match_case:
        if match_whole_word:
            if match_end == 1:
                return filter_match_whole_word_match_case_end_left
            elif match_end == 2:
                return filter_match_whole_word_match_case_end_right
            else:
                return filter_match_whole_word_match_case
        else:
            if match_end == 1:
                return filter_match_case_end_left
            elif match_end == 2:
                return filter_match_case_end_right
            else:
                return filter_match_case
    elif match_whole_word:
        if match_end == 1:
            return filter_match_whole_word_ignore_case_end_left
        elif match_end == 2:
            return filter_match_whole_word_ignore_case_end_right
        else:
            return filter_match_whole_word_ignore_case
    else:
        if match_end == 1:
            return filter_ignore_case_end_left
        elif match_end == 2:
            return filter_ignore_case_end_right
        else:
            return filter_ignore_case
    #|


def r_mouse_y_index(y, T0, B0, T1, B1):
    y -= T0
    d = T1 - T0
    i = floor(y / d)
    if y - i * d >= B0 - T0: return i
    return None
    #|


def rs_format_int6(i): # int
    if i < 0: i = -i ; sign = "-"
    else:   sign = "  "

    s = str(i)
    if i < 10000:
        if i < 100:
            if i < 10:      return f"      {sign} {s}"
            else:           return f"     {sign} {s}"
        else:
            if i < 1000:    return f"    {sign} {s}"
            else:           return f"  {sign} {s[0:1]} {s[1:]}"
    else:
        if i < 1000000:
            if i < 100000:  return f" {sign} {s[0:2]} {s[2:]}"
            else:           return f"{sign} {s[0:3]} {s[3:]}"
        else:
            if i <= 999999999:
                if i <= 9999999:    return f"{sign} {s[0:1]} {s[1:4]} {s[4:]}"
                elif i <= 99999999: return f"{sign} {s[0:2]} {s[2:5]} {s[5:]}"
                else:               return f"{sign} {s[0:3]} {s[3:6]} {s[6:]}"
            else:
                if i <= 99999999999:
                    if i <= 9999999999: return f"{sign} {s[0:1]} {s[1:4]} {s[4:7]} {s[7:]}"
                    else:               return f"{sign} {s[0:2]} {s[2:5]} {s[5:8]} {s[8:]}"
                else:
                    if i <= 999999999999:   return f"{sign} {s[0:3]} {s[3:6]} {s[6:9]} {s[9:]}"
                    else:                   return "≤ - 10 ¹²"  if sign == "-" else "≥ 10 ¹²"
    #|
def rs_format_float6(f):
    s = "{:.6f}".format(f)
    if s.startswith("-"):
        n = "-"
        s = s[1 :]
    else:
        n = "  "

    i = s.find(".")

    if i <= 4:
        if i <= 2:
            if i <= 1:  return f"      {n} {s[0:5]} {s[5:8]}"
            else:       return f"     {n} {s[0:6]} {s[6:8]}"
        else:
            if i <= 3:  return f"    {n} {s[0:7]} {s[7:8]}"
            else:       return f"  {n} {s[0:1]} {s[1:8]}"
    else:
        if i <= 6:
            if i <= 5:  return f" {n} {s[0:2]} {s[2:8]}"
            else:       return f"{n} {s[0:3]} {s[3:8]}"
        else:
            if i <= 9:
                if i <= 7:      return f"{n} {s[0:1]} {s[1:4]} {s[4:7]}"
                elif i <= 8:    return f"{n} {s[0:2]} {s[2:5]} {s[5:8]}"
                else:           return f"{n} {s[0:3]} {s[3:6]} {s[6:9]}"
            else:
                if i <= 11:
                    if i <= 10: return f"{n} {s[0:1]} {s[1:4]} {s[4:7]} {s[7:10]}"
                    else:       return f"{n} {s[0:2]} {s[2:5]} {s[5:8]} {s[8:11]}"
                else:
                    if i <= 12: return f"{n} {s[0:3]} {s[3:6]} {s[6:9]} {s[9:12]}"
                    else:       return "≤ - 10 ¹²"  if n == "-" else "≥ 10 ¹²"
    #|
def rs_format_float6_rstrip(f):
    s = "{:.6f}".format(f).rstrip("0")
    if s.endswith("."): s += "0"
    if s.startswith("-"):
        n = "-"
        s = s[1 :]
    else:
        n = "  "

    i = s.find(".")

    if i <= 4:
        if i <= 2:
            if i <= 1:  return f"      {n} {s[0:5]} {s[5:8]}"
            else:       return f"     {n} {s[0:6]} {s[6:8]}"
        else:
            if i <= 3:  return f"    {n} {s[0:7]} {s[7:8]}"
            else:       return f"  {n} {s[0:1]} {s[1:8]}"
    else:
        if i <= 6:
            if i <= 5:  return f" {n} {s[0:2]} {s[2:8]}"
            else:       return f"{n} {s[0:3]} {s[3:8]}"
        else:
            if i <= 9:
                if i <= 7:      return f"{n} {s[0:1]} {s[1:4]} {s[4:7]}"
                elif i <= 8:    return f"{n} {s[0:2]} {s[2:5]} {s[5:8]}"
                else:           return f"{n} {s[0:3]} {s[3:6]} {s[6:9]}"
            else:
                if i <= 11:
                    if i <= 10: return f"{n} {s[0:1]} {s[1:4]} {s[4:7]} {s[7:10]}"
                    else:       return f"{n} {s[0:2]} {s[2:5]} {s[5:8]} {s[8:11]}"
                else:
                    if i <= 12: return f"{n} {s[0:3]} {s[3:6]} {s[6:9]} {s[9:12]}"
                    else:       return "≤ - 10 ¹²"  if n == "-" else "≥ 10 ¹²"
    #|
def rs_format_float_left(f):
    s = "{:.6f}".format(f).rstrip("0")
    if s.endswith("."): s += "0"
    if s.startswith("-"):
        n = "-"
        s = s[1 :]
    else:
        n = "  "

    i = s.find(".")

    if i <= 12: return f"  {n} {s}"
    else:       return "  ≤ - 10 ¹²"  if n == "-" else "  ≥ 10 ¹²"
    #|
def rs_format_float6_vec(v):
    s = ""
    c_8199 = chr(8199)
    for f in v:
        o = rs_format_float6(f)
        s += f"{o.lstrip(c_8199)}, "
    return s[:-2].replace(c_8199, "")
    #|

def rs_format_hex_UPPERCASE_SEPARATOR(ivec3):
    return f"{'%02X' % ivec3[0]} {'%02X' % ivec3[1]} {'%02X' % ivec3[2]}"
    #|
def rs_format_hex_LOWERCASE_SEPARATOR(ivec3):
    return f"{'%02x' % ivec3[0]} {'%02x' % ivec3[1]} {'%02x' % ivec3[2]}"
    #|
def rs_format_hex_UPPERCASE(ivec3):
    return f"{'%02X' % ivec3[0]}{'%02X' % ivec3[1]}{'%02X' % ivec3[2]}"
    #|
def rs_format_hex_LOWERCASE(ivec3):
    return f"{'%02x' % ivec3[0]}{'%02x' % ivec3[1]}{'%02x' % ivec3[2]}"
    #|

def value_to_display(v):
    if isinstance(v, int):
        if v == INT_min: return "- 2 ** 31"
        if v == INT_max: return "2 ** 31 - 1"
        try: return str(v)
        except: return "Exceeds the limit"

    s = str(v)
    i = s.find("e")
    if i == -1: return s
    ss = s[i + 1 :].replace("+", "")
    if abs(float(ss)) > 6:
        if ss.startswith("-0"): ss = f'-{ss[2 : ]}'
        elif ss.startswith("0"): ss = ss[1 : ]
        return f"{s[: i]} * 10 ** {ss}"
    s = ('%f' % v).rstrip("0")
    return f"{s}0"  if s.endswith(".") else s
    #|
def complex_to_display(v):
    if isinstance(v, complex):
        v0 = v.real
        v1 = v.imag
        if v1 == 0: return value_to_display(v0)
        if v0 == 0: return f'({value_to_display(v1)}) ἰ'
        s1 = value_to_display(v1)
        if s1 and s1.startswith("-"): return f'{value_to_display(v0)} ({s1}) ἰ'
        return f'{value_to_display(v0)} + ({s1}) ἰ'
    return value_to_display(v)
    #|
def rs_format_py_type(o):
    s = str(type(o))
    if s.startswith("<class"): s = s[6 :].replace("'", "").replace(">", "")
    return s
    #|

def is_value(v):
    if isinstance(v, int): return True
    if isinstance(v, float): return True
    if isinstance(v, complex): return True
    return False
    #|

def r_chr_prev(ss):
    # "abcd" -> "d"
    for s in ss[:: -1]:
        if s != " ": return s
    return ""
    #|
def r_chr_next(ss):
    # "abcd" -> "a"
    for s in ss:
        if s != " ": return s
    return ""
    #|
def r_tx_prev(ss):
    # "a b2c" -> "b2c"]
    for i, s in enumerate(reversed(ss)):
        if s == " ": return ss[len(ss) - i :]
    return ss
    #|
def r_tx_next(ss):
    # "a2b c" -> "a2b"
    for i, s in enumerate(ss):
        if s == " ": return ss[: i]
    return ss
    #|
def r_word_prev(ss):
    # "ab cd" -> "cd"]
    for i, s in enumerate(reversed(ss)):
        if s not in STR_AZ_az: return ss[len(ss) - i :]
    return ss
    #|
def r_word_prev_index(ss):
    # "ab cd" -> "cd"]
    for i, s in enumerate(reversed(ss)):
        if s not in STR_AZ_az: return len(ss) - i
    return 0
    #|
def r_word09_prev(ss):
    # "ab cd" -> "cd"]
    for i, s in enumerate(reversed(ss)):
        if s not in STR_AZ_az_09: return ss[len(ss) - i :]
    return ss
    #|
def r_word09_prev_index(ss):
    # "ab cd" -> "cd"]
    for i, s in enumerate(reversed(ss)):
        if s not in STR_AZ_az_09: return len(ss) - i
    return 0
    #|
def r_word09_prev_index_inv(ss):
    for i, s in enumerate(reversed(ss)):
        if s in STR_AZ_az_09: return len(ss) - i
    return 0
    #|
def r_word_next(ss):
    # "ab cd" -> "ab"
    for i, s in enumerate(ss):
        if s not in STR_AZ_az: return ss[: i]
    return ss
    #|
def r_word_next_index(ss):
    # "ab cd" -> "ab"
    for i, s in enumerate(ss):
        if s not in STR_AZ_az: return i
    return len(ss)
    #|
def r_word09_next(ss):
    # "ab cd" -> "ab"
    for i, s in enumerate(ss):
        if s not in STR_AZ_az_09: return ss[: i]
    return ss
    #|
def r_word09_next_index(ss):
    # "ab cd" -> "ab"
    # "  ab" -> "  "
    if ss.startswith(" "):
        for i, s in enumerate(ss):
            if s == " ": continue
            return i
    else:
        for i, s in enumerate(ss):
            if s not in STR_AZ_az_09: return i
    return len(ss)
    #|
def r_word09_next_index_inv(ss):
    for i, s in enumerate(ss):
        if s in STR_AZ_az_09: return i
    return len(ss)
    #|

def r_prev_word_index(s, nonword_chrs=" "): # len != 0
    i = r_word09_prev_index(s)

    while i > 0:
        if s[i - 1] in nonword_chrs:
            i -= 1
        else: break

    return i
    #|
def r_next_word_index(s, index_begin):
    return r_word09_next_index(s[index_begin :]) + index_begin
    #|
def r_word_select_index(s, ind):
    i0 = r_word09_prev_index(s[: ind])
    i1 = r_next_word_index(s, i0)
    if i0 == i1:
        i0 = r_word09_prev_index_inv(s[: i0])
        i1 = r_word09_next_index_inv(s[i0 :]) + i0
    return i0, i1
    #|

def r_py_end_bracket_index(s, open_index, open_sign="(", close_sign=")"):
    len_s = len(s)
    on_comment = False
    on_str = False
    on_multi_str = False
    sign_str = ""

    on_backslash = False
    breakcount = 0
    opencount = 0

    for r in range(open_index + 1, len_s):
        if breakcount > 0:
            breakcount -= 1
            continue

        if on_comment is True:
            if s[r] == "\n": on_comment = False
        elif on_multi_str is True:
            if on_backslash is True: on_backslash = False
            elif s[r : r + 3] == sign_str: on_multi_str = False
            elif s[r] == "\\": on_backslash = True
        elif on_str is True:
            if on_backslash is True: on_backslash = False
            elif s[r] == sign_str: on_str = False
            elif s[r] == "\\": on_backslash = True
        else:
            ss3 = s[r : r + 3]

            if ss3 == "'''":
                on_multi_str = True
                sign_str = "'''"
                breakcount = 2
                continue
            if ss3 == '"""':
                on_multi_str = True
                sign_str = '"""'
                breakcount = 2
                continue

            ss = s[r]

            if ss == "'":
                on_str = True
                sign_str = "'"
                continue
            if ss == '"':
                on_str = True
                sign_str = '"'
                continue
            if ss == "#":
                on_comment = True
                continue

            if ss == open_sign:
                opencount += 1
                continue
            if ss == close_sign:
                if opencount == 0: return r
                opencount -= 1
    return -1


def find_index(l, x):
    for i, e in enumerate(l):
        if e == x: return i

    return -1
    #|
def find_index_attr(l, x, attr):
    for i, e in enumerate(l):
        if getattr(e, attr) == x: return i

    return -1
    #|


@ successResult
def r_tuple(ls):
    if isinstance(ls, str): return (ls, )
    if len(ls) == 1 and hasattr(ls[0], "__iter__") and not isinstance(ls[0], str): ls = ls[0]
    if isinstance(ls, tuple): return ls
    return tuple(ls)
    #|
