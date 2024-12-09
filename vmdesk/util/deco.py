
def catch(func):
    def wrapper(*k, **kw):
        try: return func(*k, **kw)
        except Exception as e: return str(e)
    return wrapper
    #|
def catchNone(func):
    def wrapper(*k, **kw):
        try: return func(*k, **kw)
        except: return None
    return wrapper
    #|
def catchFalse(func):
    def wrapper(*k, **kw):
        try: return func(*k, **kw)
        except: return False
    return wrapper
    #|
def catchStr(func):
    def wrapper(*k, **kw):
        try: return func(*k, **kw)
        except: return ""
    return wrapper
    #|
def catchBug(func):
    def wrapper(*k, **kw):
        try: return func(*k, **kw)
        except Exception as e: print(str(e))
    return wrapper
    #|
def catchWith(fn_except):
    def deco(func):
        def wrapper(*k, **kw):
            try: return func(*k, **kw)
            except:
                return fn_except()
        return wrapper
    return deco
    #|
def catchWithDialog(func):
    def wrapper(*k, **kw):
        try: return func(*k, **kw)
        except:
            from .. m import call_bug_report_dialog
            return call_bug_report_dialog()
    return wrapper
    #|
def successResult(func):
    def wrapper(*k, **kw):
        try: return True, func(*k, **kw)
        except Exception as e: return False, str(e)
    return wrapper
    #|
def noRecursive(func):
    func.is_running = False
    def wrapper(*k, **kw):
        if func.is_running:

            return

        func.is_running = True
        try:
            result = func(*k, **kw)
        except Exception as ex:
            result = str(ex)



        func.is_running = False
        return result
    return wrapper
def oneRecursive(func):
    func.is_running = 0
    def wrapper(*k, **kw):
        if func.is_running == 2:

            return
        elif func.is_running == 1:
            func.is_running = 2
        else:
            func.is_running = 1

        try:
            result = func(*k, **kw)
        except Exception as ex:
            result = str(ex)



        func.is_running = 0
        return result
    return wrapper

def assign(**kw):
    def decoCls(cls):
        for k, v in kw.items():
            setattr(cls, k, v)
        return cls
    return decoCls
    #|
def annot(*k, **kw):
    if k:
        def deco(cls):
            cls.__annotations__.update(k)
            return cls
    else:
        def deco(cls):
            cls.__annotations__.update(kw)
            return cls
    return deco
    #|
