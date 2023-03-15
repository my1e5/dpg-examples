from __future__ import annotations

import ctypes
import ctypes.wintypes
import os

user32 = ctypes.windll.user32
WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.wintypes.BOOL,
                                 ctypes.wintypes.HWND,
                                 ctypes.wintypes.LPARAM)
user32.EnumWindows.argtypes = [WNDENUMPROC,
                               ctypes.wintypes.LPARAM]


def get_hwnd_from_pid(pid: int) -> int | None:
    result = None

    def callback(hwnd, _):
        nonlocal result
        lpdw_PID = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(lpdw_PID))
        hwnd_PID = lpdw_PID.value

        if hwnd_PID == pid:
            result = hwnd
            return False
        return True

    cb_worker = WNDENUMPROC(callback)
    user32.EnumWindows(cb_worker, 0)
    return result


def get_hwnd() -> int | None:
    return get_hwnd_from_pid(os.getpid())
