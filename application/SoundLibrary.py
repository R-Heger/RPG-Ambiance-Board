from typing import List

from application.Sound import Sound


class SoundLibrary:
    def __init__(self):
        self.library = []

    def addSound(self, filePath='', soundTypes=List[int], tags=List[str]):
        self.library.append(Sound(filePath, soundTypes, tags))

    """
        :returns list of sounds where at least one sound type and one tag is matching.
        If tags are empty every tag is accepted
    """
    def getSounds(self, soundTypes=List[int], tags=List[str]) -> List[Sound]:
        sounds = List[Sound]
        for sound in self.library:
            hasRightType = False
            if tags:
                hasRightTag = False
            else:
                # if there are no Tags given every tag is accepted
                hasRightTag = True
            for soundType in soundTypes:
                if not hasRightType and soundType in sound.soundTypes:
                    hasRightType = True

            for tag in tags:
                if not hasRightTag and tag in sound.tags:
                    hasRightTag = True

            if hasRightType and hasRightTag:
                sounds.append(sound)

        return sounds
