"""
@author: Sandra Chavez
Purpose: This program will prompt a question of what phrase
    to translate and to what language.
@:argument: audio input via users' microphone
"""

from googletrans import Translator
import pyttsx3 as ts
import speech_recognition as SR

engine = ts.init()
translator = Translator()

exits = ['bye', 'exit', 'no', 'nothing', 'done', 'finished']

# only have these languages installed in computer for text-to-speech
# (excluding russian and korean)
languagesSupported = {'spanish': 'es', 'portuguese': 'pt', 'french': 'fr', 'italian': 'it',
                      'russian': 'ru', 'korean': 'ko', 'german': 'de'}

"""
@:param phrase: a string that will be converted 
    from text to speech 
"""
def eriSpeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()


""" 
Gets the audio from the users' microphone 
@:returns a string of the audio 
@:return 0 if the input is audible  
"""


def getVoice():
    variable = SR.Recognizer()
    with SR.Microphone() as source:
        print('speak now...')
        voice = variable.listen(source, phrase_time_limit=5)
        print('Done')

        try:
            sourcelang = variable.recognize_google(voice)
            print("spoken input: {0}".format(sourcelang))
            return sourcelang
            # detection = translator.detect(sourcelang)

        except Exception:
            eriSpeaks("I am sorry I could not understand")
            return 0


"""
Gets the translation of the input 
@:param phrase: users' audio input 
@:type string 
"""


def getTranslation(phrase):
    eriSpeaks('To what language?')
    destination = getDestination()
    if destination == 0 or destination == -1:
        # ask again for the language
        destination = getDestination()

    translation = translator.translate(phrase, dest=destination)
    # result = "Your translation is {0}".format(translation.text)
    # eriSpeaks(result)
    speakTranslation(translation, language=destination)

    # eriSpeaks("The prounciation is {0}".format(translation.pronunciation))


"""
gets the destination language 
@:returns the language code of the intended language 
@:return 0 if the language is not found / input is audible 
"""
def getDestination():
    lang = getVoice()

    if lang == 0:  # if input is inaudible
        eriSpeaks("input was not heard correctly, what language?")
        return -1

    print("destination language is {0}".format(lang))
    lang = str(lang).lower()

    """ if lang is not zero, it can be guaranteed that it will be a string
     then we can use the lower() function
     """
    try:
        langCode = languagesSupported.pop(lang)
        return langCode
    except KeyError:
        eriSpeaks('Language is not included, try another?')
        return 0


"""
outputs the translated text in its native language 
to speak with accurate pronunciation 
@param translation - the translated text 
@:param language - the language code 
"""
def speakTranslation(translation, language):
    # dictonary containing the language codes and the microsoft voices
    # that suit the language
    pronun = {'es':
                  'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0',
              'de':
                  'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_DE-DE_HEDDA_11.0',
              'pt':
                  'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0',
              'it':
                  'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_IT-IT_ELSA_11.0',
              'fr':
                  'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0'}

    if language in pronun:
        MVoice = pronun.get(language)
        eriSpeaks('Your translation is...')
        engine.setProperty('voice', MVoice)

    eriSpeaks(translation.text)


def main():
    while 1:
        # default voice
        voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        engine.setProperty('voice', voice_ID)

        eriSpeaks('what would you like to translate?')
        
        command = getVoice()
        
        if command == 0:
            continue

        command = str(getVoice()).lower()

        if any(word in command for word in exits):
            eriSpeaks('okay, goodbye!')
            break

        getTranslation(command)


if __name__ == "__main__":
    main()
