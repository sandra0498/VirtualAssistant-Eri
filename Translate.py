from googletrans import Translator
import pyttsx3 as ts
import speech_recognition as SR


engine = ts.init()
translator = Translator()

def getVoice():
    variable = SR.Recognizer()
    with SR.Microphone() as source:
        print('speak now...')



if __name__ == "_main_":
    voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_ID)

    while 1:
        engine.say('What would you like to translate?')



# print(translator.translate('hola como estas?'))
