import Translate as t  # importing the translation feature
import screenshot as sc
import WebSearch as ws
import speech_recognition as SR
import pyttsx3 as ts


engine = ts.init()

def eriSpeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()

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

def main():
    t.main()


if __name__ == '__main__':
    main()
