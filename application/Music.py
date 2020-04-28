from application.AudioPlayer import AudioPlayer
from application.Master import *
from application.Sound import Sound


class Music:
    def __init__(self, master: Master):
        self.musicMaster = Master(master, DefaultMusicMasterVolume)
        self.player = AudioPlayer(self.musicMaster)
        self.playlist = List[Sound]
