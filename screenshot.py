import pyautogui as p
import speech_recognition as SR
import pyttsx3 as ts
import time as t

engine = ts.init()

substring = 'important'


def erispeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()
    

def getAudio():
    variable = SR.Recognizer()

    with SR.Microphone() as receiver:
        audioInput = variable.record(receiver, duration=5)

        try:
            textOutput = variable.recognize_google(audioInput)
            if substring in textOutput:
                ss = p.screenshot('screenshot.png')
                timestamp = 'screenshot taken in ', t.strftime("%I:%M:%S")
                erispeaks(timestamp)
            else:
                erispeaks('Did not take the screenshot!')
    
        except SR.UnknownValueError:
            # either did not speak into the mic/ could not understand the input
            print('Could not process the audio!')

def main():
    while 1:
        
        getAudio()
        
    
    
    
if __name__ == "__main__":
    main()