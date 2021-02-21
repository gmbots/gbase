from msl.loadlib import Client64


class YLJSService(Client64):
    def __init__(self):
        super(YLJSService, self).__init__(module32='services.yljs.yljs_server')

    def GetSerialNumber(self):
        return self.request32('GetSerialNumber')

    # 鼠标接口
    def MoveMouseTo(self, x: int, y: int):
        return self.request32('MoveMouseTo', x, y)

    def MoveMouseRelative(self, x: int, y: int):
        return self.request32('MoveMouseRelative', x, y)
