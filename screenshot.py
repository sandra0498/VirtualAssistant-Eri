import pyautogui as p
import speech_recognition as SR
import pyttsx3 as ts
import time as t

engine = ts.init()

indicators = ['important', 'take screenshot', 'take a screenshot', 'need to remember this']
exits = ['no more', 'exit', 'done']

def erispeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()


def getScreenshot(voice):
    num = 1
    if any(word in voice for word in indicators):
        ss = p.screenshot('screenshot{0}.png'.format(num))
        timestamp = 'screenshot taken in ', t.strftime("%I:%M:%S")
        erispeaks(timestamp)
        num += 1



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

        getScreenshot(voiceInput)











if __name__ == "__main__":
    main()