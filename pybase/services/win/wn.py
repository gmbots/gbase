from typing import List

import win32gui


class WN:
    def __init__(self):
        pass

    # -------------------------------------------------
    # 窗口 ---------------------------------------------
    # -------------------------------------------------
    def GetWindowRect(self, hwnd: int):
        return win32gui.GetWindowRect(hwnd)

    def GetClientRect(self, hwnd: int):
        lw, tw, rw, bw = win32gui.GetWindowRect(hwnd)
        lc, tc, rc, bc = win32gui.GetClientRect(hwnd)
        border_x = int(((rw - lw) - (rc - lc)) / 2.0)
        border_t = bw - tw - border_x - (bc - tc)
        return lw + border_x, tw + border_t, rw - border_x, bw - border_x

    def FindWindows(self, class_name: str, title: str):
        windows = []
        win32gui.EnumWindows(lambda hd, ctx: match_window_class_name(class_name, hd, windows), None)
        return windows


def match_window_class_name(input_class: str, hd: int, windows: List[int]):
    if input_class == win32gui.GetClassName(hd):
        windows.append(hd)
