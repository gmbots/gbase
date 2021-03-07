import numpy as np
from services.damo.damo_service import DamoService
from services.yljs.yljs_service import YLJSService
dm1 = DamoService()
dm2 = DamoService()

yl = YLJSService()


def main():
    hwnd_idea = dm1.FindWindowEx(0, "SunAwtFrame", "")
    hwnd_edge = dm2.FindWindowEx(0, "Notepad++", "")
    print('查找结果位', hwnd_idea, hwnd_edge)
    # while True:
    #     i += 1

    #     dm_ret = dm1.FindPicEx(0, 0, 2000, 2000, "C:/Users/ysh35/Pictures/1.bmp", "020202", 1.0, 0)
    #     print(i)
    #     print(dm_ret)
    dm1.Reg('albin7a7a6b9740b219fb4db62c7865e00437', '123')
    dm2.Reg('albin7a7a6b9740b219fb4db62c7865e00437', '123')

    dm_ret_idea = dm1.BindWindowEx(
        hwnd_idea, "normal", "normal", "normal", "", 0)
    dm_ret_edge = dm2.BindWindowEx(
        hwnd_edge, "normal", "normal", "normal", "", 0)
    print('绑定结果位', dm_ret_idea, dm_ret_edge)
    # print(5, dm_ret_edge)
    # print(3, dm1.GetBindWindow())
    # print(4, dm2.GetBindWindow())
    # print(dm_ret_edge)
    print(dm1.GetWindowClass(dm1.GetBindWindow()))
    print(dm2.GetWindowClass(dm2.GetBindWindow()))
    while False:
        print(dm1.GetWindowClass(dm1.GetBindWindow()))
        print(dm2.GetWindowClass(dm2.GetBindWindow()))

    # win32gui.SetPixel(dc, 10, 10, red)  # draw red at 0,0


if __name__ == '__main__':
    main()
