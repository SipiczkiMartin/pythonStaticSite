import shutil

path_public = "public/"
path_static = "static/"

def copy_dirs():
    shutil.copytree(src=path_static,dst=path_public)