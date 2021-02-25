from services.damo.damo_service import DamoService
from services.yljs.yljs_service import YLJSService
import pyglet
import win32api
import win32gui
import numpy as np

# dm = DamoService()
yl = YLJSService()


def main():
    print(11)
    pyglet.graphics.draw(2, pyglet.gl.GL_POINTS,
        ('v2i', (10, 15, 30, 35))
    )
    # dc = win32gui.GetDC(0)
    # red = win32api.RGB(255, 0, 0)
    # print(dm.ver())
    # print(yl.GetSerialNumber())
    print(yl.MoveMouseTo(0, 0))
    #
    # win32gui.SetPixel(dc, 10, 10, red)  # draw red at 0,0


if __name__ == '__main__':
    main()
