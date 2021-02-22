from ctypes import windll

import win32gui
from typing import List
from win32con import LOGPIXELSX

from logger import logger


user32 = windll.user32


def get_screen_rect():
    return [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


def get_screen_zoom_factor():
    try:
        # Set DPI Awareness  (Windows 10 and 8)
        windll.shcore.SetProcessDpiAwareness(2)
        # Set DPI Awareness  (Windows 7 and Vista)
        windll.user32.SetProcessDPIAware()
        # Enable DPI detection
        windll.user32.SetProcessDPIAware()
        # Get Desktop DC
        hDC = windll.user32.GetDC(None)
        dpiX = windll.gdi32.GetDeviceCaps(hDC, LOGPIXELSX)
        windll.user32.ReleaseDC(None, hDC)
        # Based on https://technet.microsoft.com/en-us/library/dn528846.aspx
        return dpiX / 96.0
    except Exception as e:
        logger.error("Can't get zoom factor: %r", e)
    return 1.00


def winname(name):
    return name.encode('gbk').decode(errors="ignore")


