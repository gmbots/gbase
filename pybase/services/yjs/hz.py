import ctypes
import os

from logger import logger


class HZ:
    def __init__(self):
        try:
            dll_abs_path = os.getcwd() + os.path.sep + "dlls" + os.path.sep + 'msdk.dll'
            self.hezhi = ctypes.windll.LoadLibrary(dll_abs_path)
            # self.km = self.hezhi.M_Open_VidPid(0xC317, 1)
            self.km = self.hezhi.M_Open_VidPid(0x1602, 0x0301)
            # self.km = self.hezhi.M_Open_VidPid(0xC216, 0x0102)
            if self.km <= 0:
                logger.info("[易键鼠盒子] - 注册失败")
                raise Exception("[易键鼠盒子] - 注册失败")
            else:
                logger.info("[易键鼠盒子] - 注册成功")
                logger.info(f"[易键鼠盒子] - 句柄：{self.km} -----")
        except:
            print("易键鼠盒子注册失败")

    def close(self):
        self.hezhi.M_Close(self.km)
