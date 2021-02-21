from flask import Flask

from services.damo.damo_service import DamoService
from services.yljs.yljs_service import YLJSService

dm = DamoService()
yl = YLJSService()


def main():
    print(dm.ver())
    print(yl.GetSerialNumber())
    print(yl.MoveMouseTo(0, 0))


if __name__ == '__main__':
    main()
