import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))

def absolute_path(relative_path: str) -> str:
    return os.path.normpath(os.path.join(ROOT_DIR, relative_path))