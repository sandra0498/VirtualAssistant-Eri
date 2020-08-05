import pyttsx3 as ts
engine = ts.init()
# voice_ID = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
# engine.setProperty('voice', voice_ID)

voices = engine.getProperty('voices')

for voice in voices:
    print('___Voice____')
    print('ID: {0}'.format(voice.id))
    print('Name: {0}'.format(voice.name))
    engine.setProperty('voice', voice.id )
    engine.say("hello")
    engine.runAndWait()