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
        self.setVolume(defaultVolume)
        self.media = None

    def setSound(self, filePath: str):
        self.media = self.instance.media_new(filePath)
        self.currPlayer.set_media(self.media)

    def play(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.currPlayer.play()

    def pause(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.currPlayer.pause()

    def stop(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.currPlayer.stop()

    def setVolume(self, vol: float,  calledByMaster=False):
        print('player.setVolume')
        if not calledByMaster:
            self.volume = vol
            self.player1.audio_set_volume(int(self.volume * self.master.getVolume(True)))
            self.player2.audio_set_volume(int(self.volume * self.master.getVolume(True)))
        else:
            self.player1.audio_set_volume(int(self.volume * vol))
            self.player2.audio_set_volume(int(self.volume * vol))

    def getVolume(self, calledBySlave=False) -> float:
        return self.volume
