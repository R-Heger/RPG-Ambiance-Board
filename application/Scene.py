from application.Ambiance import Ambiance
from application.Music import Music
from application.SoundFx import SoundFx

playOnLoadDefault = False


class Scene:
    def __init__(self, name=''):
        self.name = name
        self.music = Music()
        self.ambiance = Ambiance()
        self.soundFx = SoundFx()

        self.playOnLoad = playOnLoadDefault



