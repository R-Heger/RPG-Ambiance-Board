from typing import List
import pickle

from application.Scene import Scene
from application.SoundLibrary import SoundLibrary


class RPGAmbianceBoard:
    def __init__(self):
        self.scenes = List[Scene]
        self.library = SoundLibrary()
        self.master = None

    def save(self, filePath: str, fileName: str):
        pickle.dump(self, filePath + fileName + '.abs', 'wb')

    def load(self, filePath: str):
        newBoard = pickle.load(filePath, 'rb')
        self.scenes = newBoard.scenes
        self.library = newBoard.library
        self.master = newBoard.master

