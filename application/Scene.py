from application import Master
from application.Ambiance import Ambiance
from application.Music import Music
from application.SoundFx import SoundFx

playOnLoadDefault = False


class Scene:
    def __init__(self, master: Master, name=''):
        self.name = name
        self.music = Music(master)
        self.ambiance = Ambiance(master)
        self.soundFx = SoundFx(master)

        master.addSalve(self.music.musicMaster)
        master.addSalve(self.ambiance.ambianceMaster)
        master.addSalve(self.soundFx.fxMaster)

        self.playOnLoad = playOnLoadDefault



