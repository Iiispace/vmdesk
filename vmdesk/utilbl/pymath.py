import bpy
from math import *

def calc_py_exp(s, globals=None):
    # <<< 1copy (0defevalattrs,, ${'globals = None':''}$)
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
    
    locals = None
    setattr = None
    delattr = None
    # >>>
    try:
        if globals is None:
            return eval(s)
        return eval(s, globals)
    except: return None
