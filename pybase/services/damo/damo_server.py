import ctypes
import os

from msl.loadlib import Server32


class DamoServer(Server32):
    def __init__(self, host, port, quiet):

        try:
            # dll_abs_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + 'DmReg.dll'
            dms = ctypes.windll.LoadLibrary(f'{os.getcwd()}\\dlls\\DmReg.dll')
            dms.SetDllPathW(f'{os.getcwd()}\\dlls\\dm.dll', 0)
        except Exception:
            print('[大漠] - 注册失败')

        super(DamoServer, self).__init__('dm.dmsoft', 'com', host, port, quiet)

    def ver(self):
        return self.lib.ver()

    def Reg(self, key: str, version: str):
        return self.lib.Reg(key, version)

    def FindWindowEx(self, parent: int, class_name: str, title: str):
        return self.lib.FindWindowEx(parent, class_name, title)

    # 后台设置
    def BindWindowEx(self, hwnd: int, display: str, mouse: str, keypad: str, public: str, mode: int):
        return self.lib.BindWindowEx(hwnd, display, mouse, keypad, public, mode)

    def GetBindWindow(self) -> int:
        return self.lib.GetBindWindow()

    def GetWindowClass(self, hwnd: int) -> str:
        return self.lib.GetWindowClass(hwnd)

    # 图色
    def FindPicEx(self, x1, y1, x2, y2: int, pic_name: str, delta_color: str, sim: float, _dir: int):
        return self.lib.FindPicEx(x1, y1, x2, y2, pic_name, delta_color, sim, _dir)
