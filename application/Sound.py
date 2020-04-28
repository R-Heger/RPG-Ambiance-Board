from typing import List


ST = {'MUSIC': 0, 'AMBIANCE': 1, 'FX': 2}


class Sound:
    def __init__(self, name: str,  filePath: str, soundTypes=List[int], tags=List[str]):
        self.name = name
        self.filePath = filePath
        self.soundTypes = soundTypes
        self.tags = tags

