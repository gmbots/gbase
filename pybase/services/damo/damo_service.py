from msl.loadlib import Client64


class DamoService(Client64):
    def __init__(self):
        super(DamoService, self).__init__(module32='services.damo.damo_server')

    def ver(self):
        return self.request32('ver')
