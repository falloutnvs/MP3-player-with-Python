#MP3 PLAYER PROJECT

#import libs
import pygame
import os
import random
import msvcrt

#initialize Pygame Mixer
pygame.mixer.init()

#set the mp3 folder
mp3_path = ' ' #enter the mp3 folder path

#mp3 file
mp3_file = [f for f in os.listdir(mp3_path) if f[-3:].lower() == 'mp3']

#function for play random song
shuffle_size = random.randint(0,len(mp3_file)-1)
def random_mp3 (mp3, shuffle_count):
    pygame.mixer.music.load(mp3_path+'/'+mp3[shuffle_count])
    pygame.mixer.music.play()

#Control button
print ("1. Press 'p' to pause \n2. 'r' to resume the music \n3. 'e' to exit \n4.'s' switch music")

#play the song
random_mp3(mp3_file,shuffle_size)

#variable for pause and unpause.
is_paused = False

#Loop for control action
while True:
    if msvcrt.kbhit() == True:
        #pause music
        getch = msvcrt.getch()
        if getch == b'p':
            is_paused = True
            pygame.mixer.music.pause()
        #resume music
        elif getch == b'r' and is_paused == True:
            is_paused = False
            pygame.mixer.music.unpause()
        #switch music
        elif getch == b's' and is_paused == False:
            shuffle_size = random.randint(0,len(mp3_file)-1)
            random_mp3(mp3_file,shuffle_size)
        #exit music
        elif getch == b'e':
            pygame.mixer.music.stop()
            break
    #continue to next song after the current song end
    if not pygame.mixer.music.get_busy() and is_paused == False:
        shuffle_size = random.randint(0,len(mp3_file)-1)
        random_mp3(mp3_file,shuffle_size)
    pygame.time.Clock().tick(10)

#note
# pygame.mixer.music.get_busy() check if music is playing.
# using msvcrt.kbhit() because using input cause the music cannot continue to the next music after it ended
# msvcrt.getch() return bytes so we need to convert string to bytes literal (ex: b'a' , b'b', etc)
