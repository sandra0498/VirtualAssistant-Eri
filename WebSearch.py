"""
@author: Sandra Chavez
Purpose: This program will prompt the user for a site name
        and what would be searched
@:argument  audio input via users' microphone
"""

import webbrowser as web
import speech_recognition as SR
import pyttsx3 as ts

engine = ts.init()

# default voice
voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
engine.setProperty('voice', voice_ID)

# dictionary of common web search engines
websites = {'google': 'https://www.google.com/',
            'youtube': 'https://www.youtube.com/',
            'bing': 'https://www.bing.com'}

# words that indicate when to break the loop
exits = ['no search', 'goodbye', 'bye', 'none']

"""
gets the audio from the user's microphone
@:rtype string if microphone successfully recognizes
        the input 
@:rtype integer zero if error occurs 
"""
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


"""
@:param phrase: a string that will be converted 
    from text to speech 
"""
def erispeaks(phrase):
    print(phrase)
    engine.say(phrase)
    engine.runAndWait()


"""
gets the url path of the user's choice 
@:param choice - indicates what web search engine 
                user wants to use 
"""
def searchWeb(choice):
    print('your choice is {0}'.format(choice))
    url = ''
    if choice == 0:
        erispeaks('going to default website')
        url = websites.get('google')

    else:
        if choice in websites:
            url = websites.get(choice)
        else:
            url = 'https://%s.com/' % choice

    result = 'your url is {0}'.format(url)
    print(result)
    searchSubject(url)


"""
prompts the user for a specific subject to search 
@:param path 
"""
def searchSubject(path):
    erispeaks('would you like to search for anything specific?')
    sub = getVoice()
    if sub == 0:
        erispeaks("I'll search up the site anyway")
        web.open(path)

    signalsforNoSub = ['no', 'none', 'no thank you']

    sub = str(sub).lower()

    if any(word in sub for word in signalsforNoSub):
        pass
    else:
        if 'youtube' in path:
            ext = 'results?search_query='
            path += ext
            path += sub
        elif 'bing' or 'google' in path:
            Ext = 'search?q='
            path += Ext
            path += sub

        print('your complete url is {0}'.format(path))

    web.open(path)


"""
prints the choices for search engines 
"""
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

        command = str(command).lower()

        if any(word in command for word in exits):
            erispeaks('okay, goodbye!')
            break

        searchWeb(command)


if __name__ == "__main__":
    main()
