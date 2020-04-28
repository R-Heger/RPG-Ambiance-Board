from abc import ABC, abstractmethod


class VolumeControllable(ABC):
    @abstractmethod
    def setVolume(self, vol: float,  calledByMaster: bool):
        pass

    @abstractmethod
    def getVolume(self, calledBySlave: bool) -> float:
        pass

