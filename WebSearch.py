import webbrowser as web
import speech_recognition as SR
import pyttsx3 as ts

engine = ts.init()

class web:

    def __init__(self, site, subject):
        self.site = site
        self.subject = subject


    def getAudioForSite(self):
        variable = SR.Recognizer()
        while 1:
            with SR.Microphone as receiver:
                self.erispeaks('speak now...')
                


    def erispeaks(self, phrase):
        print(phrase)
        engine.say(phrase)
        engine.runAndWait()




url = 'https://www.youtube.com/'
web.open(url)

