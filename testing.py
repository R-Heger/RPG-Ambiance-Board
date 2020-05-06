import vlc
import time

from application.AudioPlayer import AudioPlayer
from application.Master import Master
from application.RPGAmbianceBoard import RPGAmbianceBoard
from application.Sound import Sound

path1 = 'D:/Musik/RPG Ambient/Fantasy - Ambient Music/Relaxing Medieval Music 10 Hours.mp3'
path2 = 'D:/Musik/RPG Ambient/Caves - Ambience/Dark Humid Cave.mp3'


def vlcTest():
    print('vlc test...')
    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new(path1)
    player.set_media(media)
    player.play()
    time.sleep(7)
    print(player.audio_get_volume())
    player.audio_set_volume(20)
    time.sleep(5)
    player.audio_toggle_mute()
    time.sleep(1)
    player.audio_toggle_mute()
    time.sleep(5)
    player.stop()
    print('vlc  test done')

def audioTest():
    print('start audio test...')
    print('init master')
    master = Master()
    print('init player')
    player = AudioPlayer(master)
    print('add sound')
    player.setSound(path1)
    print('play')
    player.play()
    time.sleep(5)
    print('change Volume')
    player.setVolume(50)
    time.sleep(10)



def masterVolTest(board):
    print('add example Scene')
    scene = board.addScene()
    print('add Song to exampleScene')
    scene.music.addSong(Sound('music', path1, [0]))
    print('play Music')
    scene.music.play()
    time.sleep(3)
    print('change Volume')
    board.master.setVolume(0.5)
    time.sleep(5)
    print('Volume test Done')


def testSaveAndLoad(board):
    print('add example Scene')
    scene = board.addScene()
    print('add Song to exampleScene')
    song = Sound('music', path1, [0])
    scene.music.addSong(song)
    print('play Music')
    scene.music.play()
    time.sleep(5)
    board.save('testSaves', 'test')
    scene.music.removeSong(song)
    scene.music.play()
    board.load('testSaves/test.abs')
    scene.music.play()
    time.sleep(5)


print('Starting tests...')

ambianceBoard = RPGAmbianceBoard()

# vlcTest()

# audioTest()

# masterVolTest(ambianceBoard)


testSaveAndLoad(ambianceBoard)




