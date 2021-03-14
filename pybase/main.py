import time

import mouse

from services.damo.damo_service import DamoService

dm = DamoService()


def main():
    dm.Reg('albin7a7a6b9740b219fb4db62c7865e00437', '123')
    hwnd = dm.FindWindowEx(0, "Warcraft III", "")

    bind_result = dm.BindWindowEx(
        hwnd, "normal", "normal", "normal", "", 0)

    print(bind_result)
    print(dm.GetClientSize(hwnd))

    dm.MoveTo(1904, 992)
    time.sleep(1)
    print(222)
    dm.MoveTo(760, 920)
    print(333)
    time.sleep(1)
    mouse.double_click(button='left')
    time.sleep(1)
    create_button_pos = dm.FindPicEx(0, 0, 1920, 1080, f'C:/Users/ysh35/Pictures/create.bmp', "000000", 1, 0)
    print(44)
    print(create_button_pos)
    print(55)


if __name__ == '__main__':
    main()
