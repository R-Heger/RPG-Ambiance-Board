import vlc

from application.Master import Master
from application.VolumeControllable import VolumeControllable

defaultVolume = 75


class AudioPlayer(VolumeControllable):

    def __init__(self, master: Master):
        self.master = master
        self.instance = vlc.Instance()
        self.player1 = self.instance.media_player_new()
        self.player2 = self.instance.media_player_new()
        self.currPlayer = self.player1
        self.volume = defaultVolume
        self.media = None

    def setSound(self, filePath: str):
        self.media = self.instance.media_new(filePath)
        self.player1.set_media(self.media)

    def play(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.player1.play()

    def pause(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.player1.pause()

    def stop(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.player1.stop()

    def setVolume(self, vol: float,  calledByMaster=False):
        if not calledByMaster:
            self.volume = vol
            self.player1.audio_set_volume(int(self.volume * self.master.getVolume()))
        else:
            self.player1.audio_set_volume(int(self.volume * vol))

    def getVolume(self, calledBySlave=False) -> float:
        return self.volume
