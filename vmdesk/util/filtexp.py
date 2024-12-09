import bpy
from math import *

def r_filtexp_result(string_expressioN, find, filter_function):
    r_filtexp_result = None
    # <<< 1copy (0defevalattrs,, $$)
    __name__ = None
    __doc__ = None
    __package__ = None
    __loader__ = None
    __spec__ = None
    __file__ = None
    __cached__ = None
    __builtins__ = None
    __import__ = None
    __build_class__ = None
    __doc__ = None
    __spec__ = None
    input = None
    exec = None
    globals = None
    locals = None
    setattr = None
    delattr = None
    # >>>

    def each(filter_fn=lambda *k, **kw: True, **kw):
        return find('!', filter_fn, **kw)
    def union(*ss, filter_fn=filter_function, **kw):
        results = set()
        for s in ss:
            results |= find(s, filter_fn, **kw)
        return results
    def intersection(*ss, filter_fn=filter_function, **kw):
        if ss:
            results = find(ss[0], filter_fn, **kw)
            for s in ss[1 : ]:
                results &= find(s, filter_fn, **kw)
            return results
        return set()
    def difference(*ss, filter_fn=filter_function, **kw):
        if ss:
            results = find(ss[0], filter_fn, **kw)
            for s in ss[1 : ]:
                results -= find(s, filter_fn, **kw)
            return results
        return set()

    try:
        return True, eval(string_expressioN)
    except Exception as ex:
        return False, str(ex)
    #|
