import Translate as t  # importing the translation feature
import screenshot as sc
import WebSearch as WS
import speech_recognition as SR
import pyttsx3 as ts


engine = ts.init()

# default voice
voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)

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
    eriSpeaks('Hello my name is Erendira but for short call me Eri')
    eriSpeaks('what would you like me to do?')
    t.main()

    WS.main()


if __name__ == '__main__':
    main()
