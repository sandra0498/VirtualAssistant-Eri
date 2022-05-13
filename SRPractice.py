import speech_recognition as SR
import time as t
import pyttsx3 as ts

engine = ts.init()

# changing the voice
voice_ID = 'com.apple.speech.synthesis.voice.daniel'
engine.setProperty('voice', voice_ID)
variable = SR.Recognizer()

with SR.Microphone() as source:
    print('speak now...')
    audioInput = variable.record(source, duration=7)
    print(audioInput)

    try:
        print("goes into try statement ")
        
        textOutput = variable.recognize_google_cloud(audioInput)
        print('text converted from audio: \n')
        print(textOutput)
        engine.say("You said: {0} ".format(textOutput))
        engine.runAndWait()
        print('Execution time: ', t.strftime("%I:%M:%S"))

    except Exception:
        print("Couldn't process the audio input ")

