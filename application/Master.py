from typing import List

from application.VolumeControllable import VolumeControllable

DefaultMasterVolume = 1.0
DefaultMusicMasterVolume = 1.0
DefaultAmbianceMasterVolume = 1.0
DefaultSoundFxMasterVolume = 1.0


class Master(VolumeControllable):
    def __init__(self, master=None, vol=DefaultMasterVolume):
        self.volume = vol
        self.slaves: List[VolumeControllable] = []
        self.master = master

    def setVolume(self, vol, calledByMaster=False):
        if not calledByMaster:
            self.volume = vol
            for slave in self.slaves:
                slave.setVolume(vol, True)
        else:
            for slave in self.slaves:
                slave.setVolume(self.volume * vol, True)

    def getVolume(self, calledBySlave=False) -> float:
        if calledBySlave:
            if self.master is None:
                return self.volume
            else:
                return self.volume * self.master.getVolume(True)
        else:
            return self.volume

    def addSalve(self, slave: VolumeControllable):
        self.slaves.append(slave)
