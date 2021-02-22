import ctypes
import os

from logger import logger
from tools.km.keys import Keys


class KM:
    origin_x = 0
    origin_y = 0
    origin_w = 1024
    origin_h = 768

    def __init__(self):
        try:
            dll_abs_path = os.getcwd() + os.path.sep + "dlls" + os.path.sep + 'kmdll.dll'
            self.km = ctypes.windll.LoadLibrary(dll_abs_path)
            self.km.DllOpenDevice()
            logger.info(f"[键鼠] - 硬件版本 - {self.km.DllGetFireWareVersion()}")
            logger.info(f"[键鼠] - 芯片序列号 - {self.km.DllGetChipID()}")

        except Exception as e:
            logger.error(f"[键鼠] - 初始化失败")
            print(e)

    def __del__(self):
        self.km.DllStop()

    def set_origin(self, x: int, y: int, w: int, h: int):
        self.origin_x = x
        self.origin_y = y
        self.origin_w = w
        self.origin_h = h

    # -------------------------------------------------
    # 键盘 ---------------------------------------------
    # -------------------------------------------------
    def key_down(self, key_name: str):
        if len(key_name) > 1:
            self.km.Dllkey_eventW(1, key_name)
        else:
            self.km.Dllkey_eventA(1, key_name)

    def key_up(self, key_name: str):
        if len(key_name) > 1:
            self.km.Dllkey_eventW(2, key_name)
        else:
            self.km.Dllkey_eventA(2, key_name)

    def key_tap(self, key_name: str):
        if key_name.isupper():
            self.key_down(Keys.LShift.name)
            self.key_down(key_name)
            self.key_up(key_name)
            self.key_up(Keys.LShift.name)
        else:
            self.key_down(key_name)
            self.key_up(key_name)

    def key_type(self, key_name: str):
        for w in key_name:
            self.key_tap(w)

    def key_up_all(self):
        self.km.Dllkey_eventW(3)

    # -------------------------------------------------
    # 鼠标 ---------------------------------------------
    # -------------------------------------------------
    def mouse_left_down(self):
        self.km.Dllmouse_event(1)

    def mouse_left_up(self):
        self.km.Dllmouse_event(2)

    def mouse_left_click(self):
        self.mouse_left_down()
        self.mouse_left_up()

    def mouse_left_double_click(self):
        self.mouse_left_click()
        self.mouse_left_click()

    def mouse_right_down(self):
        self.km.Dllmouse_event(3)

    def mouse_right_up(self):
        self.km.Dllmouse_event(4)

    def mouse_middle_down(self):
        self.km.Dllmouse_event(5)

    def mouse_middle_up(self):
        self.km.Dllmouse_event(6)

    def mouse_to(self, x: int, y: int):
        self.km.Dllmouse_event(8, self.origin_x + x, self.origin_y + y)

    def mouse_to_r(self, x: int, y: int):
        self.km.Dllmouse_event(9, x, y)

    def mouse_wheel(self, length: int):
        self.km.Dllmouse_event(10, length)

    def mouse_to_s(self, x: int, y: int):
        self.km.Dllmouse_event(11, self.origin_x + x, self.origin_y + y)

    def mouse_wheel(self):
        self.km.Dllmouse_event(7)
