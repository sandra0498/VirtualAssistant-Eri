import webbrowser as web
import speech_recognition as SR
import pyttsx3 as ts

engine = ts.init()

# default voice
voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)

websites = {'google': 'https://www.google.com/',
            'youtube': 'https://www.youtube.com/',
            'bing': 'https://www.bing.com',
            'github': 'https://github.com/'}



def getVoice():
    variable = SR.Recognizer()
    with SR.Microphone as receiver:
        print('speak now...')
        voice = variable.listen(receiver, phrase_time_limit=5)
        print('done')
            
            

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
        erispeaks('what site would you like to search?')
        


#
# web.open('youtube.com')

# url = 'https://www.youtube.com/'
# web.open(url)
