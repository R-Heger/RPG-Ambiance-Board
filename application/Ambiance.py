from application.AudioPlayer import AudioPlayer
from application.Master import *
from application.Sound import Sound


class Ambiance:
    def __init__(self, master: Master):
        self.ambianceMaster = Master(master, DefaultAmbianceMasterVolume)
        self.ambianceSounds: List[AudioPlayer] = []

    def addSound(self):
        # DENK DRAN DIE MASTER ZU VERBINDEN !
        pass

