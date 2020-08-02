from googletrans import Translator
import pyttsx3 as ts
import speech_recognition as SR

engine = ts.init()
translator = Translator()


def getVoice():
    variable = SR.Recognizer()
    with SR.Microphone() as source:
        print('speak now...')
        voice = variable.listen(source, phrase_time_limit=5)
        print('Done')

        try:
            sourcelang = variable.recognize_google(voice)
            detection = translator.detect(sourcelang)

        except:
            engine.say("I am sorry I could not understand")


if __name__ == "_main_":
    voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_ID)

    while 1:
        engine.say('What would you like to translate?')

