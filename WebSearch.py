import webbrowser as web
import speech_recognition as SR
import pyttsx3 as ts

engine = ts.init()

# default voice
voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)

websites = {'google': 'https://www.google.com/',
            'youtube': 'https://www.youtube.com/',
            'bing': 'https://www.bing.com'}


exits = ['no search', 'goodbye', 'bye', 'none']


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
            erispeaks("i'm sorry, couldn't get that")
            return 0




def erispeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()

def searchWeb(choice):
    if choice in websites:
        url = websites.get(choice)


def printChoices():
    menu = 'google \n' \
           'youtube \n' \
           'bing \n'
    print(menu)

def main():

    while 1:
        erispeaks('what site would you like to search?')
        printChoices()
        command = getVoice()
        if command == 0:
            continue





if __name__ == "__main__":
    main()





#
# web.open('youtube.com')

# url = 'https://www.youtube.com/'
# web.open(url)

