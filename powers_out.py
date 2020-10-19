import random
from datetime import datetime as date
import os
import subprocess
prefix = "/home/pi/redbull/audio/"
BORED_MP3_LIST = ['Ambience1.mp3', 'Ambience2.mp3', 'Ambience3.mp3', 'Ambience4.mp3']
THANKS_MP3 = 'BasicReceipts.mp3'
KNOCK_MP3 = 'Prompt.mp3'
RECEIPTS_LIST = []


def playback(filename, can_interrupt=False):
    # check if audio is playing.
    #   if so, and can_interrupt is False,
    #       return.
    # play prefix + filename # do so non blocking and return
    print "Playing audio: {}".format(filename)
    pass

def playback_rand(file_list):
    if len(file_list) == 0:
        playback_error("Empty playlist")
        return
    track_number = random.randint(0,len(file_list))
    playback(file_list[track_number])


def playback_error(message):
    print "No playback! {}".format(message)

def bored_play():
    print "Bored *yawn* playing track"
    playback_rand(BORED_MP3_LIST)

def get_infra_reading():
    # might want to drop in the actual code here
    return int(subprocess.check_output("python /home/pi/redbull/adc_infrared.py").strip())

def print_receipt():
    if len(RECEIPTS_LIST) == 0:
        playback_error("Empty receipts list")
        return
    track_number = random.randint(0,len(RECIEPTS_LIST))
    filename = "/home/pi/redbull/receipts/" + RECEIPTS_LIST[track_number]
    os.system("lp -o fit-to-page {} && lprm -".format(filename))

def get_accel_reading():
    return int(subprocess.check_output("python /home/pi/redbull/accel_code.py").strip())

def listen_letter():
    reading = get_infra_reading() 
    if reading > 11300:
        print "Found a letter!"
        playback(THANKS_MP3, can_interrupt=True)
        print_receipt()

def listen_knock():
    reading = get_accel_reading()
    if reading < -7000:
        playback(KNOCK_MP3)
    

if __name__ == "__main__":
    # create a timer for bored ness
    while True:
        time = date.now()
        # lol trying to trigger this randomly
        if (time.minute % 3 == 0) and (time.second == 0) and (random.randint(0,2) == 0 ):
             bored_play()
        listen_knock()
        listen_letter()
