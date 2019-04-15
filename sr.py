import speech_recognition as sr
import os
import sys
import webbrowser

from gtts import gTTS

def talk(words):
    print(words)
    obj = gTTS(text=words, lang='en', slow=False)
    obj.save("sound.mp3")
    os.system("mpg321 sound.mp3 > /dev/null 2>&1")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print(" say ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio).lower()
        print("You said: " + task)
    except sr.UnknownValueError:
        talk(" i don't understand you ")
        task = command()

    return task

def makeSomething(task):
    if 'open website' in task:
        talk('please wait ...')
        url = 'https://google.com/'
        webbrowser.open(url)
    elif 'stop' in task:
        talk(" Yes, no problem ")
        sys.exit()

if __name__ == "__main__":
    talk(" hello, ask me something")
    while True:
        makeSomething(command())
