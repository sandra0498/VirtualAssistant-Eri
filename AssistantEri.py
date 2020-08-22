import Translate as t  # importing the translation feature
import screenshot as sc
import WebSearch as WS
import speech_recognition as SR
import pyttsx3 as ts
import time
import os
from datetime import date


engine = ts.init()

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

        if eri_command == 0:
            continue

        eri_command = str(eri_command).lower()

        if 'bye' in eri_command:
            eriSpeaks('goodbye {0}, it was a pleasure'.format(name))
            break

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
