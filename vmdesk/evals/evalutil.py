import bpy, math

def bpyeval(s):
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
    return eval(s)
    #|
def bpyeval_ob(s, ob):
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
    return eval(s)
    #|

def r_exec(code, **kw):
    try:
        localdict = {}
        builtins = {
            'bpy': bpy,
            'math': math,
            'abs': abs,
            'all': all,
            'any': any,
            'ascii': ascii,
            'bin': bin,
            'callable': callable,
            'chr': chr,
            'dir': dir,
            'divmod': divmod,
            'format': format,
            'getattr': getattr,
            'hasattr': hasattr,
            'hash': hash,
            'hex': hex,
            'id': id,
            'isinstance': isinstance,
            'issubclass': issubclass,
            'iter': iter,
            'len': len,
            'max': max,
            'min': min,
            'next': next,
            'oct': oct,
            'ord': ord,
            'pow': pow,
            'print': print,
            'repr': repr,
            'round': round,
            'setattr': setattr,
            'sorted': sorted,
            'sum': sum,
            'bool': bool,
            'memoryview': memoryview,
            'bytearray': bytearray,
            'bytes': bytes,
            'classmethod': classmethod,
            'complex': complex,
            'dict': dict,
            'enumerate': enumerate,
            'filter': filter,
            'float': float,
            'frozenset': frozenset,
            'property': property,
            'int': int,
            'list': list,
            'map': map,
            'object': object,
            'range': range,
            'reversed': reversed,
            'set': set,
            'slice': slice,
            'staticmethod': staticmethod,
            'str': str,
            'super': super,
            'tuple': tuple,
            'type': type,
            'zip': zip,
        }
        builtins.update(kw)
        exec(code, {'__builtins__': builtins}, localdict)
        return True, localdict
    except Exception as exx:
        return False, str(exx)
    #|
