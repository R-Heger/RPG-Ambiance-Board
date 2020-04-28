from typing import List

from application.AudioPlayer import AudioPlayer
from application.Sound import Sound


class Music:
    def __init__(self):
        self.player = AudioPlayer()
        self.playlist = List[Sound]
