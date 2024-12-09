from collections import deque

# Unsupport～staticmethod～classmethod～__xx__～_x
def inher_different(base_cls, excepts):
    slots = set()
    for cls in base_cls.__mro__:
        if hasattr(cls, '__slots__'):
            slots.update({cls.__slots__} if isinstance(cls.__slots__, str) else cls.__slots__)

    class _base_cls: __slots__ = slots

    for at in dir(base_cls):
        if at.startswith("_"): continue
        if at in excepts: continue
        if at in slots: continue

        setattr(_base_cls, at, getattr(base_cls, at))

    return _base_cls
    #|

class O: pass

class Xy:
    __slots__ = 'x', 'y'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        #|
    #|
    #|


class Name:
    __slots__ = 'name'

    def __init__(self, name):
        self.name = name
        #|
    #|
    #|

class NameValue:
    __slots__ = 'name', 'value'

    def __init__(self, name, value):
        self.name = name
        self.value = value
        #|
    #|
    #|

class NameLibrary:
    __slots__ = 'name', 'library'

    def __init__(self, name, library):
        self.name = name
        self.library = library
        #|
    #|
    #|

class NameLibraryIdentifier:
    __slots__ = 'name', 'library', 'identifier'

    def __init__(self, name, library, identifier):
        self.name = name
        self.library = library
        self.identifier = identifier
        #|
    #|
    #|

class FilepathVersion:
    __slots__ = 'filepath', 'version'

    def __init__(self, filepath, version):
        self.filepath = filepath
        self.version = version
        #|
    #|
    #|

class IdentifierNameValue:
    __slots__ = 'identifier', 'name', 'value'

    def __init__(self, identifier, name, value):
        self.identifier = identifier
        self.name = name
        self.value = value
        #|
    #|
    #|

# class SettingItem:
#     __slots__ = 'identifier', 'icon', 'blf'

#     def __init__(self, identifier, blf, icon):
#         self.identifier = identifier
#         self.blf = blf
#         self.icon = icon
#         #|
#     #|
#     #|


class Lrbt:
    __slots__ = "L", "R", "B", "T"

    def __init__(self, L, R, B, T):
        self.L = L
        self.R = R
        self.B = B
        self.T = T
        #|
    #|
    #|

class BoxGroup:
    __slots__ = 'boxes', 'bind_draw'

    def __init__(self, boxes, bind_draw=None):
        self.boxes = boxes
        self.bind_draw = i_bind_draw  if bind_draw is None else bind_draw
        #|

    def i_bind_draw(self):
        for e in self.boxes: e.bind_draw()
        #|

    def dx(self, dx):
        for e in self.boxes: e.dx(dx)
        #|
    def dx_upd(self, dx):
        for e in self.boxes: e.dx_upd(dx)
        #|
    def dy(self, dy):
        for e in self.boxes: e.dy(dy)
        #|
    def dy_upd(self, dy):
        for e in self.boxes: e.dy_upd(dy)
        #|
    def dxy(self, dx, dy):
        for e in self.boxes: e.dxy(dx, dy)
        #|
    def dxy_upd(self, dx, dy):
        for e in self.boxes: e.dxy_upd(dx, dy)
        #|
    #|
    #|

class Udraw:
    __slots__ = 'u_draw'

    def __init__(self, u_draw):
        self.u_draw = u_draw
        #|
    #|
    #|

class LocalHistory:
    __slots__ = 'w', 'index', 'array', 'r_push_item', 'push_context'

    def __init__(self, w, array_len, r_push_item=None):
        self.w = w
        self.array = deque(maxlen=array_len)
        self.r_push_item = self.r_push_item_default  if r_push_item == None else r_push_item
        self.index = -1
        self.push_context = None
        self.push()
        #|
    def kill(self):
        self.array.clear()
        del self.array
        #|

    def push(self):
        if self.index != len(self.array) - 1:
            array = self.array
            new_array = deque([array[r]  for r in range(self.index + 1)], maxlen=array.maxlen)
            array.clear()
            del array
            self.array = new_array

        self.array.append(self.r_push_item())
        self.index = len(self.array) - 1
        #|

    def r_push_item_default(self):
        push_context = self.push_context
        self.push_context = None
        return push_context
        #|
    #|
    #|
class HistoryValue:
    __slots__ = 'set_value', 'value_from', 'value_to', 'info'

    def __init__(self, value_from, value_to, set_value, info):
        self.value_from = value_from
        self.value_to = value_to
        self.set_value = set_value
        self.info = info
        #|
    #|
    #|



class RegionData:
    __slots__ = "L", "R", "B", "T", "border"

    def __init__(self):
        #|
        self.border = Lrbt(0, 0, 0, 0)
        #|

    def upd(self, area, region):
        #|
        L = 0
        R = 0
        B = 0
        T = 0

        for r in area.regions:
            if r.type == 'TOOLS':
                if r.alignment == "LEFT":   L += r.width
                else:                       R -= r.width
            elif r.type == 'UI':
                if r.alignment == "LEFT":   L += r.width
                else:                       R -= r.width
            elif r.type == 'TOOL_HEADER':
                if r.alignment == "TOP":    T -= r.height
                else:                       B += r.height

        b       = self.border
        b.L     = L
        b.R     = R
        b.B     = B
        b.T     = T
        self.L  = L
        self.R  = region.width + R
        self.B  = B
        self.T  = region.height + T
        #|

    def outside(self, x, y):
        return x < self.L or x > self.R or y < self.B or y > self.T
        #|
    #|
    #|


class RnaSlots:
    __slots__ = (
        'identifier',
        'name',
        'description',
        'type',
        'icon',
        'icon_default',
        'is_animatable',
        'is_hidden',
        'is_library_editable',
        'is_overridable',
        'bl_socket_idname',
        'use_attribute',
        'is_input',
        'data')
    #|
    #|
class RnaSubtab(RnaSlots):
    __slots__ = 'icon_id'

    def __init__(self, identifier, name, description, icon_id="", is_overridable=True):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.type = "RNASUBTAB"
        self.icon_id = icon_id
        self.is_overridable = is_overridable
        #|
    #|
    #|
class RnaButton(RnaSlots):
    __slots__ = (
        'is_repeat',
        'default',
        'size')

    def __init__(self, identifier, name, description, button_text, is_repeat=False, size=0, is_overridable=True):
        self.identifier = identifier
        self.name = name
        self.description = description
        self.default = button_text
        self.type = "RNABUTTON"
        self.is_repeat = is_repeat
        self.size = size
        self.is_overridable = is_overridable
        #|
    #|
    #|
class RnaString(RnaSlots):
    __slots__ = (
        'default',
        'subtype',
        'is_readonly',
        'is_never_none')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = "",
                subtype = "NONE",
                is_readonly = False,
                is_never_none = False,
                is_overridable = True,
                is_animatable = False):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default = default
        self.subtype = subtype
        self.is_readonly = is_readonly
        self.is_never_none = is_never_none
        self.type = "STRING"
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        #|
    #|
    #|
class RnaEnum(RnaSlots):
    __slots__ = (
        'default',
        'enum_items',
        'is_readonly',
        'is_never_none',
        'is_enum_flag')

    def __init__(self, identifier, enum_items,
                name = "",
                description = "",
                default = "",
                is_readonly = False,
                is_never_none = True,
                is_enum_flag = False,
                is_overridable = True,
                is_animatable = False):

        self.identifier = identifier
        self.enum_items = enum_items
        self.name = name
        self.description = description
        self.default = default
        self.is_readonly = is_readonly
        self.is_never_none = is_never_none
        self.is_enum_flag = is_enum_flag
        self.type = "ENUM"
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        #|

    @staticmethod
    def copy_from_bl_rna(rna):
        return RnaEnum(rna.identifier, rna.enum_items,
            name = rna.name,
            description = rna.description,
            default = rna.default,
            is_readonly = rna.is_readonly,
            is_never_none = rna.is_never_none,
            is_enum_flag = rna.is_enum_flag,
            is_overridable = rna.is_overridable)
        #|
    #|
    #|
class RnaPointer(RnaSlots):
    __slots__ = (
        'default',
        'is_readonly',
        'is_never_none')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = None,
                is_readonly = False,
                is_never_none = False,
                is_overridable = True,
                is_animatable = False):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default = default
        self.is_readonly = is_readonly
        self.is_never_none = is_never_none
        self.type = "POINTER"
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        #|
    #|
    #|
class RnaBool(RnaSlots):
    __slots__ = (
        'default',
        'is_array')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = False,
                is_overridable = True,
                is_animatable = False):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default = default
        self.type = "BOOLEAN"
        self.is_array = False
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        #|
    #|
    #|
class RnaBoolVector(RnaSlots):
    __slots__ = (
        'array_length',
        'default_array',
        'is_array')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = False,
                is_overridable = True,
                is_animatable = False):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default_array = default
        self.type = "BOOLEAN"
        self.is_array = True
        self.array_length = len(default)
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        #|
    #|
    #|
class RnaInt(RnaSlots):
    __slots__ = (
        'default',
        'hard_max',
        'hard_min',
        'soft_max',
        'soft_min',
        'is_array',
        'subtype',
        'unit',
        'step')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = 0,
                hard_min = -2147483648,
                hard_max = 2147483647,
                subtype = "NONE",
                unit = "NONE",
                step = 1,
                is_overridable = True,
                is_animatable = False,
                soft_min = -2147483648,
                soft_max = 2147483647,):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default = default
        self.type = "INT"
        self.is_array = False
        self.hard_min = hard_min
        self.hard_max = hard_max
        self.subtype = subtype
        self.unit = unit
        self.step = step
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        self.soft_min = soft_min
        self.soft_max = soft_max
        #|
    #|
    #|
class RnaIntVector(RnaSlots):
    __slots__ = (
        'array_length',
        'default_array',
        'hard_max',
        'hard_min',
        'soft_max',
        'soft_min',
        'is_array',
        'subtype',
        'unit',
        'step')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = 0,
                hard_min = -2147483648,
                hard_max = 2147483647,
                subtype = "NONE",
                unit = "NONE",
                step = 1,
                is_overridable = True,
                is_animatable = False):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default_array = default
        self.type = "INT"
        self.is_array = True
        self.hard_min = hard_min
        self.hard_max = hard_max
        self.subtype = subtype
        self.unit = unit
        self.step = step
        self.array_length = len(default)
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        #|
    #|
    #|
class RnaFloat(RnaSlots):
    __slots__ = (
        'default',
        'hard_max',
        'hard_min',
        'soft_max',
        'soft_min',
        'is_array',
        'subtype',
        'unit',
        'step')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = 0.0,
                hard_min = -3.402823e+38,
                hard_max = 3.402823e+38,
                subtype = "NONE",
                unit = "NONE",
                step = 1,
                is_overridable = True,
                is_animatable = False,
                soft_min = -3.402823e+38,
                soft_max = 3.402823e+38):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default = default
        self.type = "FLOAT"
        self.is_array = False
        self.hard_min = hard_min
        self.hard_max = hard_max
        self.subtype = subtype
        self.unit = unit
        self.step = step
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        self.soft_min = soft_min
        self.soft_max = soft_max
        #|
    #|
    #|
class RnaFloatVector(RnaSlots):
    __slots__ = (
        'array_length',
        'default_array',
        'hard_max',
        'hard_min',
        'soft_max',
        'soft_min',
        'is_array',
        'subtype',
        'unit',
        'step')

    def __init__(self, identifier,
                name = "",
                description = "",
                default = 0.0,
                hard_min = -3.402823e+38,
                hard_max = 3.402823e+38,
                subtype = "NONE",
                unit = "NONE",
                step = 1,
                is_overridable = True,
                is_animatable = False,
                soft_min = -3.402823e+38,
                soft_max = 3.402823e+38):

        self.identifier = identifier
        self.name = name
        self.description = description
        self.default_array = default
        self.type = "FLOAT"
        self.is_array = True
        self.hard_min = hard_min
        self.hard_max = hard_max
        self.subtype = subtype
        self.unit = unit
        self.step = step
        self.array_length = len(default)
        self.is_animatable = is_animatable
        self.is_overridable = is_overridable
        self.soft_min = soft_min
        self.soft_max = soft_max
        #|
    #|
    #|

class Dictlist(dict):
    __slots__ = 'L_index_key', 'D_key_index', 'default', 'range_item'

    def __init__(self, ls):
        if ls:
            if hasattr(ls[0], "identifier"):
                self.update({e.identifier: e  for e in ls})
                self.L_index_key = [e.identifier  for e in ls]
            else:
                self.update({l[0]: l[1]  for l in ls})
                self.L_index_key = [k  for k, e in ls]

            self.D_key_index = {k: r  for r, k in enumerate(self.L_index_key)}
        else:
            self.L_index_key = []
            self.D_key_index = {}

        self.range_item = range(len(self))
        #|
    def __iter__(self):
        L_index_key = self.L_index_key
        for r in self.range_item:
            yield self[L_index_key[r]]
        #|
    def __getitem__(self, k):
        if isinstance(k, int):
            return super().__getitem__(self.L_index_key[k])
        return super().__getitem__(k)
        #|
    def __delitem__(self, k):
        if isinstance(k, int):
            super().__delitem__(self.L_index_key[k])
            del self.L_index_key[k]
        else:
            super().__delitem__(k)
            del self.L_index_key[self.D_key_index[k]]

        self.D_key_index.clear()
        self.D_key_index.update({k: r  for r, k in enumerate(self.L_index_key)})
        self.range_item = range(len(self))
        #|

    def keys(self):
        L_index_key = self.L_index_key
        return tuple(L_index_key[r]  for r in self.range_item)
        #|
    def values(self):
        L_index_key = self.L_index_key
        return tuple(self[L_index_key[r]]  for r in self.range_item)
        #|
    def items(self):
        L_index_key = self.L_index_key
        return tuple((k, self[k])  for k in (L_index_key[r]  for r in self.range_item))
        #|
    def find(self, k):
        return self.D_key_index.get(k, -1)
        #|

    def new(self, k, e):
        r = len(self)
        self.L_index_key.append(k)
        self.D_key_index[k] = r

        self[k] = e
        self.range_item = range(len(self))
        #|

    def foreach_get(self, attr, seq):
        for r in self.range_item:
            seq[r] = getattr(self[r], attr)
        #|
    def foreach_set(self, attr, seq):
        for r in self.range_item:
            setattr(self[r], attr, seq[r])
        #|
    #|
    #|

class EnumItem(RnaSlots):
    __slots__ = 'value'

    def __init__(self, identifier, name, description=""):
        self.identifier = identifier
        self.name = name
        self.description = description
        #|
    #|
    #|

class ArrayActive(dict):
    __slots__ = 'active_index', 'len', 'maxindex'

    def __init__(self, ls, active_index):
        self.active_index = active_index
        self.update({r: e  for r, e in enumerate(ls)})
        self.len = len(ls)
        self.maxindex = self.len - 1
        #|

    def __iter__(self):
        for r in range(self.len):
            yield self[r]
        #|

    def shiftactive(self, i):
        if i < 0:
            if self.active_index == 0: return
            old = self.active_index
            new = max(0, old + i)

            dic = {r + 1: self.pop(r)  for r in range(new, old)}
            self[new] = self.pop(old)
            self.update(dic)
            self.active_index = new
        else:
            if self.active_index == self.maxindex: return
            old = self.active_index
            new = min(self.maxindex, old + i)

            dic = {r - 1: self.pop(r)  for r in range(old + 1, new + 1)}
            self[new] = self.pop(old)
            self.update(dic)
            self.active_index = new
        #|
    #|
    #|

class RnaDataOps:
    __slots__ = 'operator', 'keymap_category'

    def __init__(self, operator, keymap_category="Mesh"):
        self.operator = operator
        self.keymap_category = keymap_category
        #|
    #|
    #|
class RnaDataDefaultValue:
    __slots__ = 'default_value_path'

    def __init__(self, default_value_path):
        self.default_value_path = default_value_path
        #|
    #|
    #|

def r_enum_items_create(tuple3_items):
    return Dictlist([EnumItem(identifier, name, description)  for identifier, name, description in tuple3_items])
    #|
def r_rna_enum_from_bl_rna(rna, tuple3_items, default, values=True):
    enumitems = Dictlist([EnumItem(identifier, name, description)  for identifier, name, description in tuple3_items])
    enumitems.default = default

    if values is True:
        for r, e in enumerate(enumitems):
            e.value = r
    elif values is None: pass
    else:
        for r, e in zip(values, enumitems):
            e.value = r

    out = RnaEnum(rna.identifier, enumitems,
        name = rna.name,
        description = rna.description,
        default = default,
        is_never_none = rna.is_never_none,
        is_overridable = rna.is_overridable,
        is_animatable = rna.is_animatable)
    out.is_hidden = rna.is_hidden
    out.is_library_editable = rna.is_library_editable
    return out
    #|
def r_rna_string_from_bl_rna(rna):
    out = RnaString(rna.identifier,
        name = rna.name,
        description = rna.description,
        default = rna.default,
        subtype = rna.subtype,
        is_readonly = rna.is_readonly,
        is_never_none = rna.is_never_none,
        is_overridable = rna.is_overridable,
        is_animatable = rna.is_animatable)
    out.is_hidden = rna.is_hidden
    out.is_library_editable = rna.is_library_editable
    return out
    #|


class BlRna:
    __slots__ = (
        'properties')

    def __init__(self, properties):
        self.properties = properties
        #|
    #|
    #|
class IDFake:
    __slots__ = (
        'asset_data',
        'id_type',
        'is_editable',
        'is_library_indirect',
        'is_missing',
        'library',
        'name',
        'name_full',
        'override_library')

    def __init__(self):
        self.asset_data = None
        self.id_type = "NONE"
        self.is_editable = True
        self.is_library_indirect = False
        self.is_missing = False
        self.library = None
        self.name = ""
        self.name_full = ""
        self.override_library = None
        #|
    #|
    #|

OB_FAKE = IDFake()


def blRna(rnas):
    class PpBase:
        __slots__ = (rna.identifier  for rna in rnas)

        id_data = OB_FAKE
        bl_rna = BlRna(Dictlist(rnas))

        def __init__(self, w):
            self.w = w

            for rna in rnas:
                if hasattr(rna, "default"):
                    setattr(self, rna.identifier, rna.default)
                else:
                    setattr(self, rna.identifier, [e  for e in rna.default_array])

    return PpBase
    #|

class PpOverrideCreate(blRna((
    RnaBool("remap_local_usages",
        name = "Remap Local Usages",
        description = "Whether local usages of the linked ID should be remapped to the new library override of it",
        default = False),
    ))):
    __slots__ = 'w'
class PpOverrideClear(blRna((
    RnaBool("remap_local_usages",
        name = "Remap Local Usages",
        description = "Remap all users to original library data-block",
        default = False),
    RnaBool("delete_unused",
        name = "Delete Unused",
        description = "Delete the overridden data-block if there is no user",
        default = True),
    ))):
    __slots__ = 'w'
