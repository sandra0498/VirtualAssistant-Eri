"""
@author: Sandra Chavez
Purpose: This program represents a voice assistant that takes the
        user's audio input to execute its functions
@:argument audio input via user's microphone
"""


import Translate as t  # importing the translation feature
import screenshot as sc  # importing the screenshot class
import WebSearch as WS  # will allow us to search any site
import speech_recognition as SR  # importing the speech recognition module
import pyttsx3 as ts  # will allow the text to speech feature
import time  # will allow us to format the string for time 
import os
from datetime import date
import subprocess   # this allows us to run external programs
import psutil  # will allow us to get the laptop battery percentage
import datetime as dt


engine = ts.init()
battery = psutil.sensors_battery()

# default voice
voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)

"""
@:param phrase: a string that will be converted 
    from text to speech 
"""
def eriSpeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()


""" 
Gets the audio from the users' microphone 
@:returns a string of the audio 
@:return 0 if the input is audible  
"""
def getVoice():
    variable = SR.Recognizer()
    with SR.Microphone() as source:
        print('speak now...')
        voice = variable.listen(source, phrase_time_limit=5)
        print('done')
        try:
            text = variable.recognize_google(voice)
            return text

        except SR.UnknownValueError:
            eriSpeaks("i'm sorry, couldn't get that")
            return 0


"""
Gets the formatted string of the current time 
"""
def getTime():
    local = time.localtime()
    currentTime = time.strftime("%H:%M:%S", local)
    eriSpeaks("The current time is {0}".format(currentTime))


"""
Gets the formatted string of the current date 
"""
def getDate():
    today = date.today()
    formatDate = today.strftime("%B %d, %Y")
    eriSpeaks("The current date is {0}".format(formatDate))


def openProgram(choice):
    # path to the program
    directory = "C:/Program Files"

    # still in progress
    subprocess.call([directory])

def printprogramchoices():
    choices = ""
    print(choices)

def getBatteryPercent():
    display = "Currently, your battery is at {0} percent".format(battery.percent)
    eriSpeaks(display)

def getBatteryTimeLeft():
    timeLeft = str(dt.timedelta(seconds=battery.secsleft))
    display = "You have {0} left in battery".format(timeLeft)
    eriSpeaks(display)



def main():
    eriSpeaks('Hello, my name is Eréndira, but for short, call me Eri')
    eriSpeaks('what is your name?')
    name = getVoice()

    # if input is audible, user will be called human
    if name == 0:
        name = 'human'
        eriSpeaks("I couldn't get your name, greetings anyways")
    else:
        # otherwise, user will be called by its name
        eriSpeaks('greetings, {0}'.format(name))

    while 1:

        eriSpeaks('what would you like me to do?')

        eri_command = getVoice()

        # if eri gets no input, it continues the loop and asks again
        if eri_command == 0:
            continue

        # once it gets the command, it turns input into string
        # and turns lowercase
        eri_command = str(eri_command).lower()

        if 'bye' in eri_command:
            eriSpeaks('goodbye {0}, it was a pleasure'.format(name))
            break
        
        if 'time left' and 'battery' in eri_command:
            getBatteryTimeLeft()
            
        if 'battery' in eri_command:
            getBatteryPercent()

        if 'current time' in eri_command:
            getTime()

        if 'date' in eri_command:
            getDate()

        if 'shutdown' in eri_command:
            os.system('shutdown -s')

        if 'translate' in eri_command:
            t.main()

        if 'search' in eri_command:
            WS.main()

        if 'screenshot' in eri_command:
            sc.main()


if __name__ == '__main__':
    main()
