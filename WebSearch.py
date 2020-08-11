import webbrowser as web
import speech_recognition as SR
import pyttsx3 as ts

engine = ts.init()

websites = {'google': 'https://www.google.com/',
            'youtube': 'https://www.youtube.com/',
            'bing': 'https://www.bing.com',
            'github': 'https://github.com/'}



def getAudio():
    variable = SR.Recognizer()
    while 1:
        with SR.Microphone as receiver:
            erispeaks('speak now...')

def erispeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()

    # def searchWeb(self):
    #     url = ''
    #
    #     if self.site in websites:
    #         url = websites.get(self.site)
    #
    #     else:
    #         url = 'https://www.{0}.com/'.format(self.site)
    #
    #     return url
    #
    # def searchsubject(self):
    #     query = self.searchWeb()
    #     query += self.subject
    #
    #     return query


def main():

    while 1:
        

#
# web.open('youtube.com')

# url = 'https://www.youtube.com/'
# web.open(url)
