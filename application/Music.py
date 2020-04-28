from application.AudioPlayer import AudioPlayer
from application.Master import *
from application.Sound import Sound


class Music:
    def __init__(self, master: Master):
        self.musicMaster = Master(master, DefaultMusicMasterVolume)
        self.player = AudioPlayer(self.musicMaster)
        self.musicMaster.addSalve(self.player)
        self.playlist: List[Sound] = []
        self.currSong = None

    def addSong(self, song: Sound):
        self.playlist.append(song)
        if len(self.playlist) == 1:
            self.currSong = song

    def play(self):
        if self.currSong:
            self.player.setSound(self.currSong.filePath)
            self.player.play()
        else:
            print('no song in the playlist!')
