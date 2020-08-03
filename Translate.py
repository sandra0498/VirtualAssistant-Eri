from googletrans import Translator
import pyttsx3 as ts
import speech_recognition as SR

engine = ts.init()
translator = Translator()
voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)
exits = ['bye', 'exit', 'no', 'nothing']


def getVoice():
    variable = SR.Recognizer()
    with SR.Microphone() as source:
        print('speak now...')
        voice = variable.listen(source, phrase_time_limit=5)
        print('Done')

        try:
            sourcelang = variable.recognize_google(voice)
            return sourcelang
            # detection = translator.detect(sourcelang)

        except:
            engine.say("I am sorry I could not understand")
            return 0


def getTranslation():
    translation = translator.translate()


def main():

    while 1:
        engine.say('What would you like to translate?')
        engine.runAndWait()
        command = getVoice()
        print(type(command))
        if command == 0:
            continue

        if any(word in command for word in exits):
            engine.say('okay, goodbye!')
            engine.runAndWait()
            break


if __name__ == "__main__":
    main()
