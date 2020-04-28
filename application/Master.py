from typing import List

from application.VolumeControllable import VolumeControllable

DefaultMasterVolume = 1.0


class Master(VolumeControllable):
    def __init__(self):
        self.volume = DefaultMasterVolume
        self.slaves = List[VolumeControllable]

    def setVolume(self, vol, calledByMaster=False):
        if not calledByMaster:
            self.volume = vol

        for slave in self.slaves:
            slave.setVolume(self.volume * vol, True)

    def getVolume(self) -> float:
        return self.volume

