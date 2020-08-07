"""
@author: Sandra Chavez
Purpose: This program takes a screenshot by users' request
@:argument voice input 
"""

import pyautogui as p  # module to take the screenshot 
import speech_recognition as SR  # module to recognize the microphone's input
import pyttsx3 as ts  # module for text to speech 
import time as t  # module to give the timestamp 

engine = ts.init()

# words that indicate when screenshot will be taken
indicators = ['important', 'take screenshot', 'take a screenshot', 'need to remember this']

# words/phrases that break the while loop
exits = ['no more', 'exit', 'done']


"""
@:param phrase: string that will soon be 
    converted from text to speech 
"""
def erispeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()


def getScreenshot(voice, num):

    if any(word in voice for word in indicators):
        if num > 0:
            ss = p.screenshot('screenshot{0}.png'.format(num))
        else:
            first = p.screenshot('screenshot.png')

        timestamp = 'screenshot taken in ', t.strftime("%I:%M:%S")
        erispeaks(timestamp)
        return 'success'




def getAudio():
    variable = SR.Recognizer()

    with SR.Microphone() as receiver:
        erispeaks('listening')
        audioInput = variable.listen(receiver, phrase_time_limit=5)
        erispeaks('done listening')

        try:
            textOutput = variable.recognize_google(audioInput)
            return textOutput


        except SR.UnknownValueError:
            # either did not speak into the mic/ could not understand the input
            print('Could not process the audio!')
            return 0


def main():
    numOfScreenshots = 0  # num of total screenshots

    while 1:
        # default voice
        voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        engine.setProperty('voice', voice_ID)
        voiceInput = getAudio()
        if voiceInput == 0:
            continue

        voiceInput = str(voiceInput).lower()

        if any(word in voiceInput for word in exits):
            erispeaks('Done taking screenshots')
            break

        screenshot = getScreenshot(voiceInput, numOfScreenshots)

        if screenshot == 'success':
            numOfScreenshots += 1

        print(numOfScreenshots)


if __name__ == "__main__":
    main()
