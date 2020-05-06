from typing import List
import pickle

from application.Master import Master
from application.Scene import Scene
from application.SoundLibrary import SoundLibrary


class RPGAmbianceBoard:
    def __init__(self):
        self.scenes: List[Scene] = []
        self.library = SoundLibrary()
        self.master = Master()

    def save(self, filePath: str, fileName: str):
        pickle.dump(self, open(filePath + '/' + fileName + '.abs', 'wb'))

    def load(self, filePath: str):
        newBoard = pickle.load(open(filePath, 'rb'))
        self.scenes = newBoard.scenes
        self.library = newBoard.library
        self.master = newBoard.master

    def addScene(self, scene=None, name='') -> Scene:
        if scene is None:
            scene = Scene(self.master, name)
            self.scenes.append(scene)
        else:
            self.scenes.append(scene)

        return scene
