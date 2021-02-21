import os
from ctypes import c_char_p

from msl.loadlib import Server32


class YLJSServer(Server32):
    def __init__(self, host, port, quiet):
        super(YLJSServer, self).__init__(f'{os.getcwd()}\\dlls\\igkmlib32.dll', 'WinDLL', host, port, quiet)

    def GetSerialNumber(self):
        return c_char_p(self.lib.GetSerialNumber()).value.decode('utf-8')

    # 鼠标接口
    def MoveMouseTo(self, x: int, y: int):
        return self.lib.MoveMouseTo(x, y)

    def MoveMouseRelative(self, x: int, y: int):
        return self.lib.MoveMouseRelative(x, y)
