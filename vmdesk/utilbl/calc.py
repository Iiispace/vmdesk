import bpy, math, cmath, decimal
import random as Random

from decimal import Decimal
from bpy.utils.units import to_value as units_to_value

from ..  import util
from .. utilbl.pymath import calc_py_exp

r_tx_next = util.com.r_tx_next
r_chr_next = util.com.r_chr_next

# <<< 1mp (util.const
const = util.const
STR_09 = const.STR_09
STR_09dot = const.STR_09dot
STR_AZ_az = const.STR_AZ_az
STR_AZ_az_09dot = const.STR_AZ_az_09dot
D_unit_replace = const.D_unit_replace
D_length_name_to_value = const.D_length_name_to_value
S_all_area_unit = const.S_all_area_unit
S_all_volume_unit = const.S_all_volume_unit
S_all_mass_unit = const.S_all_mass_unit
S_all_time_unit = const.S_all_time_unit
S_all_temperature_unit = const.S_all_temperature_unit
# >>>


NUM_SIGN = '0123456789.()[]{}^*/+-,%!'
SIGN_ADD_MINU = '+-'
SIGN_5 = '+-*/)]}'
SIGN_CLOSE = ')]}'
SIGN_OP = '+-*/%'

S_unit = set(D_length_name_to_value.keys()).union(S_all_mass_unit, S_all_time_unit, S_all_temperature_unit)
S_unit_0 = {k[0]  for k in S_unit}
S_unit = S_unit.union(S_all_area_unit, S_all_volume_unit)

py_sum = sum

def math_split(s):
    lis = []
    def check_left(ss, i0, i1):
        for r in range(i1, i0, -1):
            if ss[r] in {")", "]"}: return None
            if ss[r] in {"(", "["}: return r
        return None

    def split(ss):
        i0 = 0
        l1 = len(ss)
        while True:
            i = ss.find(",", i0)
            if i == -1: return l1
            RET = check_left(ss, i0, i)
            if RET is None: return i
            i0 = i + 1

    while True:
        ii = split(s)
        e0 = s[: ii]
        e1 = s[ii + 1 :]
        lis.append(e0)
        if not e1: return lis
        s = e1
    #|
def round_dec(x, n=0):
    if n < 0:
        fac = 10 ** -n ; x /= fac ; s = "1."
        return float(Decimal(x).quantize(Decimal(s), rounding=decimal.ROUND_HALF_UP)) * fac
    else:
        s = "1." + "0" * n
        return float(Decimal(x).quantize(Decimal(s), rounding=decimal.ROUND_HALF_UP))
    #|
def try_R_flo_dec_round(x, n, exc = None):
    try:    return round_dec(x, n)
    except: return exc
    #|

def pow(a, b):
    if isinstance(a, int): a = float(a)
    if isinstance(b, int): b = float(b)
    return a ** b
    #
def sum(*l):
    if hasattr(l[0], "__iter__"): return py_sum(l[0])
    return py_sum(l)
    #
def round(a, b=None):
    if b is None: return int(round_dec(a, 0))
    return round_dec(a, b)
    #

def check_overflow(s):
    pass
def R_flo_by_str(s):
    try:
        if len(s) > 2:
            if s.startswith("-."):  s = "-0." +s[2:]
        return float(s)
    except: return None
def R_complex_by_str(s):
    try:    return complex(s)
    except: return None
def R_flo(z):
    if isinstance(z, complex):
        if -1e-15 <= z.imag <= 1e-15: return z.real
    return float(z)

def R_non_e_express(s, sign = "►10^"):
    ind = s.find("e")
    if ind == -1:   return s
    return s[:ind] + sign + str(int(s[ind+1:]))
def RR_sci_str_by_float(f, m_sign = " ╳ 10"): # only ^00 ~ 99
    s = "{:.6e}".format(f)  ; ind_e = s.find("e")   ; L = s[:ind_e]
    if s[ind_e + 1] == "+":
        R = s[ind_e + 2:]
        if R == "00":       R = ""
        elif R[0] == "0":   L = s[:ind_e] + m_sign ; R = R[1:]
        else:               L = s[:ind_e] + m_sign
    else:
        R = s[ind_e + 2:] ; L = s[:ind_e] + m_sign
        if R[0] == "0":     R = R[1:]
        R = "- " + R
    if L[0] == "-":         L = "- " + L[1:]
    return L, R
def RR_ans_str_by_float(f, r=14, m_sign = " •10"):
    s = str(f)
    ind = s.find("e")
    if ind == -1:
        flo = try_R_flo_dec_round(f, r)
        if flo == None:
            return s, ""
        L = str(flo)
        if L.endswith(".0"):  L = L[ : -2]
        return L, ""
    flo = try_R_flo_dec_round(float(s[:ind]), r)
    if flo == None:     L = s[:ind]
    else:   L = str(flo)
    power = str(int(s[ind+2:]))
    if s[ind+1] == "+":     return L + m_sign, power
    return L + m_sign, "- " + power
def R_sabs(z):
    if z is None:           return None
    ty = type(z)
    if ty is complex:
        if z.imag == 0:     return z.real
        return -abs(z)  if z.real < 0 else abs(z)
    if ty is float:         return z
    if ty is int:           return z
    return None
    #
def R_word(s, ind_start, ind_end_1): # get end_range ind of word
    for r in range(ind_start, ind_end_1):
        if s[r] in NUM_SIGN: return r
    return ind_end_1
def R_pre_context(out):
    if out:
        out_last = out[-1]
        if out_last == ")":
            count_close = 1
            count_open = 0
            is_ret = False
            for r in range(len(out) - 2, -1, -1):
                c = out[r]
                if c == ")":    count_close += 1
                elif c == "(":  count_open += 1

                if is_ret:
                    if c in SIGN_ADD_MINU: return r
                else:
                    if count_close == count_open: is_ret = True
            return 0
        elif out_last in STR_09dot:
            for r in range(len(out) - 2, -1, -1):
                c = out[r]
                if c not in STR_09dot and c in SIGN_5: return r + 1
            return 0
        else:
            return len(out)

    else:
        return len(out)
    #
def R_next_context(s, i):
    ll = len(s)
    if i >= ll: return i

    c0 = s[i]
    if c0 == "(":
        count_open = 1
        count_close = 0

        for r in range(i + 1, ll):
            c = s[r]
            if c == ")": count_close += 1
            elif c == "(": count_open += 1

            if count_close == count_open: return r + 1
        return ll
    else:
        for r in range(i + 1, ll):
            if s[r] not in STR_AZ_az_09dot: return r
        return ll
    #
def R_back_context(s, i):
    ll = len(s)
    if i >= ll: return i

    c0 = s[i]
    if c0 == ")":
        same_count = False
        count_open = 0
        count_close = 1

        for r in range(i - 1, -1, -1):
            c = s[r]
            if c == ")": count_close += 1
            elif c == "(": count_open += 1

            if same_count:
                if c in SIGN_5 or c in STR_09: return r + 1
            else:
                if count_close == count_open: same_count = True

        return 0
    else:
        for r in range(i - 1, -1, -1):
            c = s[r]
            if c == "(": return r + 1
            if c == ",": return r + 1
            if c in SIGN_OP: return r + 1
        return 0
def R_unit_fac(s, unit_system, unit_length, rna_unit="LENGTH"):
    v_m = units_to_value(unit_system, rna_unit, s, str_ref_unit=unit_length)
    v_1 = units_to_value(unit_system, rna_unit, "1", str_ref_unit=unit_length)
    return v_m / v_1
    #|

def Ri_fx(s, open_ind): # if not a func, open_ind
    include_az = False
    stat = False
    for r in range(open_ind - 1, -1, -1):
        c = s[r]
        if stat is True:
            if include_az is False:
                if c in STR_AZ_az: include_az = True

            if c not in STR_AZ_az_09dot:
                rr = r + 1
                cc = s[rr]
                if cc in STR_AZ_az: return rr if include_az else open_ind

                for rrr in range(rr + 1, open_ind):
                    if s[rrr] in STR_AZ_az: return rrr if include_az else open_ind
                return open_ind - 1 if include_az else open_ind

        else: # first time
            if c in STR_AZ_az_09dot:
                stat = True
                if c in STR_AZ_az: include_az = True
            else: return open_ind

    cc = s[0]
    if cc in STR_AZ_az: return 0

    for rrr in range(1, open_ind):
        if s[rrr] in STR_AZ_az: return rrr
    return open_ind - 1
    #
def Ri_close(s, open_ind): # not include
    ll = len(s)
    count_open = 1
    count_close = 0
    for r in range(open_ind + 1, ll):
        c = s[r]
        if c == '(': count_open += 1
        elif c == ')': count_close += 1

        if count_open == count_close: return r + 1
    return ll
    #
def tran_fn_bracket(s):
    i = 0
    ll = len(s)
    inds = []
    while i < ll:
        c = s[i]
        if c == "(":
            ii = Ri_fx(s, i)
            context = s[ii : i]
            if context:
                if context[0] in STR_09dot: pass
                else:
                    jj = Ri_close(s, i)
                    inds.append((ii, True))
                    inds.append((jj, False))
        i += 1

    if inds:
        offset = 0
        inds.sort(key=lambda x: x[0])
        for i, is_open in inds:
            j = i + offset
            if is_open:
                s = s[: j] + "(" + s[j :]
            else:
                s = s[: j] + ")" + s[j :]
            offset += 1

    return s
    #
def tran_pow(s):
    while True:
        i = s.rfind("**")
        if i == -1: return s

        i_back = R_back_context(s, i - 1)
        i_next = R_next_context(s, i + 2)
        s = f'{s[: i_back]}(pow({s[i_back : i]},{s[i + 2 : i_next]})){s[i_next :]}'

    #
def tran_add_star(s):
    out = s[0]
    ll = len(s)
    for r in range(1, ll):
        c = s[r]
        if c == "(":
            cc = s[r - 1]
            if cc == ")": out += "*"
            elif cc == ".": continue
            elif cc in STR_09:
                i = Ri_fx(s, r)
                if s[i : r]:
                    if s[i : r][0] in STR_09: out += "*"
                else:
                    out += "*"
        elif c == ")":
            i = r + 1
            if i < ll:
                if s[i] in STR_09:
                    out += c + "*"
                    continue
        out += c
    return out
def tran_unit(py_exp, unit_system, unit_length, rna_unit="LENGTH"):
    # 1000 in + 3feet
    out = ""
    ll = len(py_exp)
    i = 0

    while i < ll:
        s = py_exp[i]
        s_lower = s.lower()
        if s_lower in S_unit_0:
            tx = r_tx_next(py_exp[i :])
            len_tx = len(tx)
            if tx.lower() in S_unit:
                chr_next = r_chr_next(py_exp[i + len_tx :])
                if not chr_next or chr_next in '+-*/':
                    new_i = i + len_tx
                    try:
                        if tx in D_unit_replace: tx = D_unit_replace[tx]
                        if tx[-1] in "2²":
                            v = R_unit_fac(f'1{tx.lower()[: -1]}', unit_system, unit_length, rna_unit)
                            v *= v
                        elif tx[-1] in "3³":
                            v = R_unit_fac(f'1{tx.lower()[: -1]}', unit_system, unit_length, rna_unit)
                            v *= v * v
                        else:
                            v = R_unit_fac(f'1{tx.lower()}', unit_system, unit_length, rna_unit)
                        new_tx = f'*{v}'
                    except:
                        new_tx = tx

                    out += new_tx
                    i = new_i
                    continue

            new_i = i + len_tx
            out += py_exp[i : new_i]
            i = new_i
            continue
        else:
            out += s
        i += 1
    return out
    #|

D_replace = {
    "e": "(math.e)",
    "pi": "(math.pi)",
    "π": "(math.pi)",
    "tau": "(math.tau)",
    "inf": "(math.inf)",
    "nan": "(math.nan)",
    "x": "(self.ans_flo)",
    "o": "(self.org)",
    "False": "(0)",
    "True": "(1)",
}

class CalcData:
    __slots__ = (
        'ans_flo',
        'org',
        'input',
        'unit_system',
        'unit_length',
        'rna_unit')

    def __init__(self, ans_flo, org, input, unit_system, unit_length, rna_unit):
        self.ans_flo = ans_flo
        self.org = org
        self.input = input
        self.unit_system = unit_system
        self.unit_length = unit_length
        self.rna_unit = rna_unit
        #|
    #|
    #|
class Calc:
    __slots__ = (
        'ans_flo',
        'ans_tx',
        'org',
        'dic',
        'input',
        'unit_system',
        'unit_length',
        'rna_unit')

    def __init__(self, org=0, unit_system="METRIC", unit_length="METERS", rna_unit="LENGTH"):
        self.ans_flo = org
        self.ans_tx = ""
        self.org = org
        self.dic = {}
        self.unit_system = unit_system
        self.unit_length = unit_length
        self.rna_unit = rna_unit
        #|
    def eval_input(self):
        try:
            if self.input == "":
                self.ans_tx = "ValueError"
                return None


            if self.rna_unit == "ROTATION":

                pass

            functions['self'] = CalcData(self.ans_flo, self.org, self.input, self.unit_system, self.unit_length, self.rna_unit)
            v = calc_py_exp(self.input, functions)
            if isinstance(v, int):
                try: float(v)
                except:
                    self.ans_tx = "Exceeds the limit"
                    return None

            self.ans_flo = v

            self.ans_tx = str(v)
            return True
        except ZeroDivisionError:
            self.ans_tx = "Division by 0"
            return None
        except ValueError:
            self.ans_tx = "ValueError"
            return None
        except RuntimeError:
            self.ans_tx = "RuntimeError"
            return None
        except OverflowError:
            self.ans_tx = "OverflowError"
            return None
        except:
            self.ans_tx = "SyntaxError"
            return None
        #
    def R_tran(self, s): # s must no spaces
        ll = len(s)
        out = ""
        dic = self.dic
        count_open = 0
        count_close = 0

        ind = 0
        while ind != ll:
            # print()
            # print("while ind = ", ind)
            i = R_word(s, ind, ll)
            word = s[ind : i]
            if word:
                # print(f"    word = {word}")
                if word in {'d', 'D'}:
                    word = 'd'
                    if out and out.endswith(','): word = '"d"'
                    #
                elif word in {'i', 'j'}:
                    if out and out[-1] not in STR_09dot: word = '1j'
                    else: word = 'j'
                    #
                elif word in D_replace: word = D_replace[word]

                out += word
                ind = i
                continue
            else:
                c = s[ind]
                # print(f"    not word  c = {c}")
                if c == "^":    c = "**"
                elif c == "%":  c = "(0.01)"
                elif c == "(":
                    count_open += 1
                elif c == ")":
                    count_close += 1
                elif c == "!":
                    pre_ind = R_pre_context(out)
                    out = f"{out[: pre_ind]}(factorial({out[pre_ind :]}))"
                    c = ""
                out += c

            ind += 1

        if count_open > count_close: out += ")" * (count_open - count_close)
        return out
        #|

    def calc(self, s):

        s = s.strip().replace(' ', '')

        if s:
            s = self.R_tran(s)

            s = tran_unit(s, self.unit_system, self.unit_length, self.rna_unit)

            s = tran_fn_bracket(s)

            s = tran_pow(s)

            s = tran_add_star(s)


            self.input = s
            self.eval_input()
        else:
            self.ans_flo = 0.0
            self.ans_tx = ""

        z = R_complex_by_str(self.ans_tx)
        if z == None:   return


        if -1e-15 <= z.real <= 1e-15:
            real0, real1 = RR_sci_str_by_float(0.0)
        else:
            real0, real1 = RR_sci_str_by_float(z.real)

        if -1e-15 <= z.imag <= 1e-15:
            imag0 = ""
            imag1 = ""
        else:
            imag0, imag1 = RR_sci_str_by_float(z.imag)

        if imag0 != "":
            if imag0[0] != "-":    imag0 = "+" + imag0
        self.ans_tx = (real0, real1, imag0, imag1)



def seed(a=None, version=2):
    return Random.seed(a, round(R_flo(version)))
    #
def getstate():
    return Random.getstate()
    #
def setstate(state):
    return Random.setstate(state)
    #
def randbytes(n):
    return Random.randbytes(round(R_flo(n)))
    #
def randrange(start, stop=None, step=None):
    if stop is None and step is None:
        return Random.randrange(round(R_flo(start)))
    if step is None:
        return Random.randrange(round(R_flo(start)), round(R_flo(stop)))
    return Random.randrange(round(R_flo(start)), round(R_flo(stop)), round(R_flo(step)))
    #
def randint(a, b):
    return Random.randint(round(R_flo(a)), round(R_flo(b)))
    #
def getrandbits(k):
    return Random.getrandbits(round(R_flo(k)))
    #
def choice(seq):
    return Random.choice(seq)
    #
def choices(population, k=1, weights=None, cum_weights=None):
    return Random.choices(population, weights=weights, cum_weights=cum_weights, k=k)
    #
def shuffle(seq):
    l = list(seq)
    Random.shuffle(l)
    return l
    #
def sample(population, k, counts=None):
    return Random.sample(population, k, counts=counts)
    #
def random():
    return Random.random()
    #
def uniform(a, b):
    return Random.uniform(R_flo(a), R_flo(b))
    #
def triangular(low, high, mode):
    return Random.triangular(R_flo(low), R_flo(high), R_flo(mode))
    #
def betavariate(alpha, beta):
    return Random.betavariate(R_flo(alpha), R_flo(beta))
    #
def expovariate(lambd):
    return Random.expovariate(R_flo(lambd))
    #
def gammavariate(alpha, beta):
    return Random.gammavariate(R_flo(alpha), R_flo(beta))
    #
def gauss(mu=0.0, sigma=1.0):
    return Random.gauss(mu=R_flo(mu), sigma=R_flo(sigma))
    #
def lognormvariate(mu, sigma):
    return Random.lognormvariate(R_flo(mu), R_flo(sigma))
    #
def normalvariate(mu=0.0, sigma=1.0):
    return Random.normalvariate(R_flo(mu), R_flo(sigma))
    #
def vonmisesvariate(mu, kappa):
    return Random.vonmisesvariate(R_flo(mu), R_flo(kappa))
    #
def paretovariate(alpha):
    return Random.paretovariate(R_flo(alpha))
    #
def weibullvariate(alpha, beta):
    return Random.weibullvariate(R_flo(alpha), R_flo(beta))
    #

def phase(z):
    return cmath.phase(z)
    #
def polar(z):
    return cmath.polar(z)
    #
def rect(r, phi):
    return cmath.rect(R_flo(r), R_flo(phi))
    #
def exp(z):
    return cmath.exp(z)
    #
def log(z, base=10):
    return cmath.log(z, base)
    #
def log10(z, base=10):
    return cmath.log(z, base)
    #
def log2(z, base=2):
    return cmath.log(z, base)
    #
def ln(z, base=None):
    if base is None: return cmath.log(z)
    return cmath.log(z, base)
    #
def sqrt(z, base=2):
    return pow(z, 1/base)
    #
def rt(z, base=2):
    return pow(z, 1/base)
    #
def acos(z, unit="r"):
    if unit == "d": return math.degrees(math.acos(R_flo(z)))
    return cmath.acos(z)
    #
def asin(z, unit="r"):
    if unit == "d": return math.degrees(math.asin(R_flo(z)))
    return cmath.asin(z)
    #
def atan(z, unit="r"):
    if unit == "d": return math.degrees(math.atan(R_flo(z)))
    return cmath.atan(z)
    #
def asec(z, unit="r"):
    if unit == "d": return math.degrees(math.acos(1/R_flo(z)))
    return cmath.acos(1/z)
    #
def acsc(z, unit="r"):
    if unit == "d": return math.degrees(math.asin(1/R_flo(z)))
    return cmath.asin(1/z)
    #
def acot(z, unit="r"):
    if unit == "d": return math.degrees(math.atan(1/R_flo(z)))
    return cmath.atan(1/z)
    #
def cos(z, unit="r"):
    if unit == "d": return math.cos(math.radians(R_flo(z)))
    return cmath.cos(z)
    #
def sin(z, unit="r"):
    if unit == "d": return math.sin(math.radians(R_flo(z)))
    return cmath.sin(z)
    #
def tan(z, unit="r"):
    if unit == "d": return math.tan(math.radians(R_flo(z)))
    return cmath.tan(z)
    #
def sec(z, unit="r"):
    if unit == "d": return 1/math.cos(math.radians(R_flo(z)))
    return 1/cmath.cos(z)
    #
def csc(z, unit="r"):
    if unit == "d": return 1/math.sin(math.radians(R_flo(z)))
    return 1/cmath.sin(z)
    #
def cot(z, unit="r"):
    if unit == "d": return 1/math.tan(math.radians(R_flo(z)))
    return 1/cmath.tan(z)
    #
def acosh(z):
    return cmath.acosh(z)
    #
def asinh(z):
    return cmath.asinh(z)
    #
def atanh(z):
    return cmath.atanh(z)
    #
def asech(z):
    return cmath.acosh(1/z)
    #
def acsch(z):
    return cmath.asinh(1/z)
    #
def acoth(z):
    return cmath.atanh(1/z)
    #
def cosh(z):
    return cmath.cosh(z)
    #
def sinh(z):
    return cmath.sinh(z)
    #
def tanh(z):
    return cmath.tanh(z)
    #
def sech(z):
    return 1/cmath.cosh(z)
    #
def csch(z):
    return 1/cmath.sinh(z)
    #
def coth(z):
    return 1/cmath.tanh(z)
    #
def isfinite(z):
    return cmath.isfinite(z)
    #
def isinf(z):
    return cmath.isinf(z)
    #
def isnan(z):
    return cmath.isnan(z)
    #
def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return cmath.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)
    #
def Re(z):
    if isinstance(z, complex): return z.real
    return z
    #
def Im(z):
    if isinstance(z, complex): return z.imag
    return 0.0
    #
def conj(z):
    z = complex(z)
    return complex(z.real, -1 * z.imag)

def ceil(f):
    return math.ceil(R_flo(f))
    #
def comb(n, r):
    return math.comb(round(R_flo(n)), round(R_flo(r)))
    #
def C(n, r):
    return math.comb(round(R_flo(n)), round(R_flo(r)))
    #
def copysign(x, y):
    return math.copysign(R_flo(x), R_flo(y))
    #
def fabs(f):
    return math.fabs(R_flo(f))
    #
def factorial(i):
    return math.factorial(round(R_flo(i)))
    #
def floor(f):
    return math.floor(R_flo(f))
    #
def fmod(x, y):
    return math.fmod(R_flo(x), R_flo(y))
    #
def frexp(f):
    return math.frexp(R_flo(f))
    #
def fsum(l):
    return math.fsum(l)
    #
def gcd(*i):
    return math.gcd(*i)
    #
def isqrt(i):
    return math.isqrt(round(R_flo(i)))
    #
def lcm(*i):
    return math.lcm(*i)
    #
def ldexp(x, i):
    return math.ldexp(R_flo(x), round(R_flo(i)))
    #
def modf(f):
    return math.modf(R_flo(f))
    #
def nextafter(x, y):
    return math.nextafter(R_flo(x), R_flo(y))
    #
def perm(n, r):
    return math.perm(round(R_flo(n)), round(R_flo(r)))
    #
def P(n, r):
    return math.perm(round(R_flo(n)), round(R_flo(r)))
    #
def prod(*v, start=None):
    if hasattr(v[0], "__iter__"):
        if start is None:
            if len(v) == 2: return math.prod(v[0], start=v[1])
            return math.prod(v[0])
        return math.prod(v[0], start=start)
    return math.prod(v)
    #
def remainder(x, y):
    return math.remainder(R_flo(x), R_flo(y))
    #
def trunc(f):
    return math.trunc(R_flo(f))
    #
def ulp(f):
    return math.ulp(R_flo(f))
    #
def cbrt(f):
    return math.pow(R_flo(f), 1/3)
    #
def exp2(f):
    return math.pow(2, R_flo(f))
    #
def expm1(f):
    return math.expm1(R_flo(f))
    #
def log1p(f):
    return math.log1p(R_flo(f))
    #
def atan2(y, x):
    return math.atan2(R_flo(y), R_flo(x))
    #
def dist(p, q):
    return math.dist(p, q)
    #
def hypot(*coordinates):
    return math.hypot(*coordinates)
    #
def degrees(f):
    return math.degrees(R_flo(f))
    #
def radians(f):
    return math.radians(R_flo(f))
    #
def erf(f):
    return math.erf(R_flo(f))
    #
def erfc(f):
    return math.erfc(R_flo(f))
    #
def gamma(f):
    return math.gamma(R_flo(f))
    #
def lgamma(f):
    return math.lgamma(R_flo(f))

functions = {
    'math': math,
    'seed': seed,
    'getstate': getstate,
    'setstate': setstate,
    'randbytes': randbytes,
    'randrange': randrange,
    'randint': randint,
    'getrandbits': getrandbits,
    'choice': choice,
    'choices': choices,
    'shuffle': shuffle,
    'sample': sample,
    'random': random,
    'uniform': uniform,
    'triangular': triangular,
    'betavariate': betavariate,
    'expovariate': expovariate,
    'gammavariate': gammavariate,
    'gauss': gauss,
    'lognormvariate': lognormvariate,
    'normalvariate': normalvariate,
    'vonmisesvariate': vonmisesvariate,
    'paretovariate': paretovariate,
    'weibullvariate': weibullvariate,
    'phase': phase,
    'polar': polar,
    'rect': rect,
    'exp': exp,
    'log': log,
    'log10': log10,
    'log2': log2,
    'ln': ln,
    'sqrt': sqrt,
    'rt': rt,
    'acos': acos,
    'asin': asin,
    'atan': atan,
    'asec': asec,
    'acsc': acsc,
    'acot': acot,
    'cos': cos,
    'sin': sin,
    'tan': tan,
    'sec': sec,
    'csc': csc,
    'cot': cot,
    'acosh': acosh,
    'asinh': asinh,
    'atanh': atanh,
    'asech': asech,
    'acsch': acsch,
    'acoth': acoth,
    'cosh': cosh,
    'sinh': sinh,
    'tanh': tanh,
    'sech': sech,
    'csch': csch,
    'coth': coth,
    'isfinite': isfinite,
    'isinf': isinf,
    'isnan': isnan,
    'isclose': isclose,
    'Re': Re,
    'Im': Im,
    'conj': conj,
    'ceil': ceil,
    'comb': comb,
    'C': C,
    'copysign': copysign,
    'fabs': fabs,
    'factorial': factorial,
    'floor': floor,
    'fmod': fmod,
    'frexp': frexp,
    'fsum': fsum,
    'gcd': gcd,
    'isqrt': isqrt,
    'lcm': lcm,
    'ldexp': ldexp,
    'modf': modf,
    'nextafter': nextafter,
    'perm': perm,
    'P': P,
    'prod': prod,
    'remainder': remainder,
    'trunc': trunc,
    'ulp': ulp,
    'cbrt': cbrt,
    'exp2': exp2,
    'expm1': expm1,
    'log1p': log1p,
    'atan2': atan2,
    'dist': dist,
    'hypot': hypot,
    'degrees': degrees,
    'radians': radians,
    'erf': erf,
    'erfc': erfc,
    'gamma': gamma,
    'lgamma': lgamma,
}


def _calc_vec_3(s): # Return a list for unit vector, len=3
    ss = math_split(s)
    ll = len(ss)
    if ll > 3 or ll == 0:
        return "SyntaxError"

    ans = []
    for e in ss:
        ca = Calc()
        ca.calc(e)
        if isinstance(ca.ans_tx, str):
            return ca.ans_tx

        n = ca.ans_flo
        ans.append(abs(n) if isinstance(n, complex) else n)

    if ll == 2:
        n0 = ans[0]
        n1 = ans[1]
        n2_2 = 1 - n0 * n0 - n1 * n1
        if n2_2 < 0: return "Wrong unit vector"
        ans.append(math.sqrt(n2_2))
    elif ll == 1:
        n0 = ans[0]
        n2_2 = (1 - n0 * n0) / 2
        if n2_2 < 0: return "Wrong unit vector"
        n2 = math.sqrt(n2_2)
        ans.append(n2)
        ans.append(n2)
    return ans
    #|
def calc_vec_3(s):
    ans = _calc_vec_3(s)
    if isinstance(ans, list): return ans

    return _calc_vec_3(s[1 : -1])
    #|
def _calc_vec(s):
    ss = math_split(s)
    ll = len(ss)
    if ll == 0:
        return "SyntaxError"

    ans = []
    for e in ss:
        ca = Calc()
        ca.calc(e)
        if isinstance(ca.ans_tx, str):
            return ca.ans_tx

        n = ca.ans_flo
        ans.append(abs(n) if isinstance(n, complex) else n)
    return ans
def calc_vec(s):
    ans = _calc_vec(s)
    if isinstance(ans, list): return ans

    return _calc_vec(s[1 : -1])
    #|


# def test(s):
#     x = Calc()
#     x.calc(s)
#     print(x.ans_flo)
#     print(x.ans_tx)
#     print()

# test("betavariate(2, 3)")
# s = "1000 in + 3feet"
# print(tran_unit(s, "METRIC", "METERS"))
