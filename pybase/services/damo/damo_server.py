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
