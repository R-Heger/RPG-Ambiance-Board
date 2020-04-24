import vlc

defaultVolume = 50


class AudioPlayer:

    def __init__(self):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = None

    def setSound(self, filePath: str):
        self.media = self.instance.media_new(filePath)
        self.player.set_media(self.media)
        self.setVolume(defaultVolume)

    def play(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.player.play()

    def pause(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.player.pause()

    def stop(self):
        if self.media is None:
            print('no sound loaded')
        else:
            self.player.stop()

    def setVolume(self, vol: int):
        if self.media is None:
            print('no sound loaded')
        else:
            self.player.audio_set_volume(vol)
