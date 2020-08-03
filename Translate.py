from googletrans import Translator
import pyttsx3 as ts
import speech_recognition as SR

engine = ts.init()
translator = Translator()

voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)


exits = ['bye', 'exit', 'no', 'nothing', 'done']

languagesSupported = {'spanish': 'es', 'portuguese (brazil)': 'pt-BR', 'french': 'fr'}

def eriSpeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()


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
            eriSpeaks("I am sorry I could not understand")
            return 0


def getTranslation(phrase):
    eriSpeaks('To what language?')
    destination = getDestination()
    translation = translator.translate(phrase, dest=destination)
    result = "Your translation is {0}".format(translation.text)
    eriSpeaks(result)


def getDestination():
    lang = str(getVoice()).lower()
    langCode = languagesSupported.pop(lang)
    return langCode





def main():

    while 1:
        eriSpeaks('what would you like to translate?')
        command = str(getVoice()).lower()
        if command == 0:
            continue

        if any(word in command for word in exits):
            eriSpeaks('okay, goodbye!')
            break

        getTranslation(command)


if __name__ == "__main__":
    main()
