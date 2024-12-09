from shutil import rmtree
from pathlib import Path


def del_folder(s):
    try: rmtree(s)
    except: pass
    #|

def r_glob_files(folder, suffix, recursive=True):
    s = f'**/*{suffix}'  if recursive else f'*{suffix}'
    return [str(fp) for fp in Path(folder).glob(s) if fp.is_file()]
    #|
