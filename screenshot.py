import pyautogui as p
import speech_recognition as SR
import pyttsx3 as ts
import time as t

engine = ts.init()

substring = 'important'

indicators = ['important', 'take screenshot', 'need to remember this']
exits = ['no more', 'exit', 'done']

def erispeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()


def getScreenshot(input):
    if substring in input:
        ss = p.screenshot('screenshot.png')
        timestamp = 'screenshot taken in ', t.strftime("%I:%M:%S")
        erispeaks(timestamp)
    else:
        pass

def getAudio():
    variable = SR.Recognizer()

    with SR.Microphone() as receiver:
        print('speak now...')
        audioInput = variable.listen(receiver, phrase_time_limit=5)
        print('done')

        try:
            textOutput = variable.recognize_google(audioInput)
            return textOutput


        except SR.UnknownValueError:
            # either did not speak into the mic/ could not understand the input
            print('Could not process the audio!')
            return 0 

def main():
    while 1:
        voiceInput = getAudio()
        if voiceInput == 0:
            continue
            
        voiceInput = str(voiceInput).lower()
        
        if any(word in voiceInput for word in exits):
            erispeaks('Done taking screenshots')
            break
    
        getScreenshot(voiceInput)    
        
        
        
        
        

        




if __name__ == "__main__":
    main()