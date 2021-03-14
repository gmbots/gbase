from msl.loadlib import Client64


class DamoService(Client64):
    def __init__(self):
        super(DamoService, self).__init__(module32='services.damo.damo_server')

    def ver(self):
        return self.request32('ver')

    def Reg(self, key: str, version: str):
        return self.request32('Reg', key, version)

    # 窗口
    def FindWindowEx(self, parent: int, class_name: str, title: str):
        return self.request32('FindWindowEx', parent, class_name, title)

    def GetBindWindow(self) -> int:
        return self.request32('GetBindWindow')

    # 后台设置
    def BindWindowEx(self, hwnd: int, display: str, mouse: str, keypad: str, public: str, mode: int):
        return self.request32('BindWindowEx', hwnd, display, mouse, keypad, public, mode)

    def GetWindowClass(self, hwnd: int) -> str:
        return self.request32('GetWindowClass', hwnd)

    def GetClientSize(self, hwnd: int) -> str:
        return self.request32('GetClientSize', hwnd)

    # 图色
    def FindPicEx(self, x1, y1, x2, y2: int, pic_name: str, delta_color: str, sim: float, _dir: int) -> str:
        return self.request32('FindPicEx', x1, y1, x2, y2, pic_name, delta_color, sim, _dir)

    # 键鼠
    def MoveTo(self, x, y: int) -> float:
        return self.request32('MoveTo', x, y)

    def LeftClick(self) -> float:
        return self.request32('LeftClick')
