import webbrowser as web
import speech_recognition as SR
import pyttsx3 as ts

engine = ts.init()

websites = {'google' : 'https://www.google.com/',
            'youtube': 'https://www.youtube.com/',
            'bing': 'https://www.bing.com'}
class web:

    def __init__(self, site, subject):
        self.site = site
        self.subject = subject

    # might move to the main class 
    # def getAudioForSite(self):
    #     variable = SR.Recognizer()
    #     while 1:
    #         with SR.Microphone as receiver:
    #             self.erispeaks('speak now...')



    def erispeaks(self, phrase):
        print(phrase)
        engine.say(phrase)
        engine.runAndWait()

    def searchWeb(self):




web.open('youtube.com')



# url = 'https://www.youtube.com/'
# web.open(url)

