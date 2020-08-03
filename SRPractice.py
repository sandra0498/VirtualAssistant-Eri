import speech_recognition as SR
import time as t
import pyttsx3 as ts

engine = ts.init()

# changing the voice
voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)
variable = SR.Recognizer()

with SR.Microphone() as source:
    print('speak now...')
    audioInput = variable.record(source, duration=7)

    try:
        textOutput = variable.recognize_google(audioInput)
        print('text converted from audio: \n')
        print(textOutput)
        engine.say("You said: {0} ".format(textOutput))
        engine.runAndWait()
        print('Execution time: ', t.strftime("%I:%M:%S"))

    except Exception:
        print("Couldn't process the audio input ")
