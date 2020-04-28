from application.AudioPlayer import AudioPlayer
from application.Master import *
from application.Sound import Sound


class SoundFx:
    def __init__(self, master: Master):
        self.fxMaster = Master(master, DefaultSoundFxMasterVolume)
        self.soundFxs = List[AudioPlayer]
