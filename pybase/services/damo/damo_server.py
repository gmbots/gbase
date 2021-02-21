from msl.loadlib import Server32


class DamoServer(Server32):
    def __init__(self, host, port, quiet):
        super(DamoServer, self).__init__('dm.dmsoft', 'com', host, port, quiet)

    def ver(self):
        return self.lib.ver()
