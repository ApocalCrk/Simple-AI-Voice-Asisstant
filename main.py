import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import sys
import smtplib
from wordlist import *
import random
from numberlist import *
import pyautogui
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from playsound import playsound
from googletrans import Translator


engine = pyttsx3.init('sapi5')
volume = engine.getProperty('volume')
engine.setProperty('volume', 50.0)
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    playsound('Speech on.wav')
    hour = int((datetime.datetime.now().hour))
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')

    else:
        speak("Good Evening!")

    speak("I am ur assistant, Please tell me how may i help you")

# English Language
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizer...")
        query = r.recognize_google(audio, language='en')
        print(f"user said: {query}\n")
    except:
        playsound('Speech Misrecognition.wav')
        print("Say that again please...")
        return "None"
    return query

#Indonesian Language
def takeCommand_id():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizer...")
        query = r.recognize_google(audio, language='id')
        print(f"user said: {query}\n")
    except:
        playsound('Speech Misrecognition.wav')
        print("Say that again please...")
        return "None"
    return query

def news():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en')
    except:
        return "None"
    return query

def getPerson(query):
    wordList = query.split()
    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' '+wordList[i+3]

def getSearch(query):
    wordList = query.split()
    for i in range(0, len(wordList)):
        if i + 8 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'google':
            hasil8 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]+' '+wordList[i+8]
            return hasil8
        if i + 7 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'google':
            hasil7 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]
            return hasil7
        if i + 6 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'google':
            hasil6 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]
            return hasil6
        if i + 5 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'google':
            hasil5 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]
            return hasil5
        if i + 4 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'google':
            hasil4 = wordList[i+3]+' '+wordList[i+4]
            return hasil4
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'google':
            hasil3 = wordList[i+3]
            return hasil3

def getFilm(query):
    wordList = query.split()
    for i in range(0, len(wordList)):
        if i + 8 <= len(wordList) - 1 and wordList[i].lower() == 'play' and wordList[i+1].lower() == 'film' and wordList[i+2].lower() == '':
            hasil8 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]+' '+wordList[i+8]
            return hasil8
        if i + 7 <= len(wordList) - 1 and wordList[i].lower() == 'play' and wordList[i+1].lower() == 'film' and wordList[i+2].lower() == 'name':
            hasil7 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]
            return hasil7
        if i + 6 <= len(wordList) - 1 and wordList[i].lower() == 'play' and wordList[i+1].lower() == 'film' and wordList[i+2].lower() == 'name':
            hasil6 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]
            return hasil6
        if i + 5 <= len(wordList) - 1 and wordList[i].lower() == 'play' and wordList[i+1].lower() == 'film' and wordList[i+2].lower() == 'name':
            hasil5 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]
            return hasil5
        if i + 4 <= len(wordList) - 1 and wordList[i].lower() == 'play' and wordList[i+1].lower() == 'film' and wordList[i+2].lower() == 'name':
            hasil4 = wordList[i+3]+' '+wordList[i+4]
            return hasil4
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'play' and wordList[i+1].lower() == 'film' and wordList[i+2].lower() == 'name':
            hasil3 = wordList[i+3]
            return hasil3

def getYoutube(query):
    wordList = query.split()
    for i in range(0, len(wordList)):
        if i + 9 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'youtube':
            hasil9 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]+' '+wordList[i+8]+' '+wordList[i+9]
            return hasil9
        if i + 8 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'youtube':
            hasil8 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]+' '+wordList[i+8]
            return hasil8
        if i + 7 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'youtube':
            hasil7 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]
            return hasil7
        if i + 6 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'youtube':
            hasil6 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]
            return hasil6
        if i + 5 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'youtube':
            hasil5 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]
            return hasil5
        if i + 4 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'youtube':
            hasil4 = wordList[i+3]+' '+wordList[i+4]
            return hasil4

        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'on' and wordList[i+2].lower() == 'youtube':        
            hasil3 = wordList[i+3]
            return hasil3

def getChannel(query):
    wordList = query.split()
    for i in range(0, len(wordList)):
        if i + 5 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'channel' and wordList[i+2].lower() == 'name':
            hasil5 = wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5] 
            return hasil5
        if i + 4 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'channel' and wordList[i+2].lower() == 'name':
            hasil5 = wordList[i+3]+' '+wordList[i+4] 
            return hasil5
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'channel' and wordList[i+2].lower() == 'name':
            hasil5 = wordList[i+3]+' '+wordList[i+4]
            return hasil5


def getHow(query):
    wordList = query.split()
    for i in range(0, len(wordList)):
        if i + 8 <= len(wordList) - 1 and wordList[i].lower() == 'how' and wordList[i+1].lower() == 'to':
            hasil8 = wordList[i+2]+' '+wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]+' '+wordList[i+8]
            return hasil8
        if i + 7 <= len(wordList) - 1 and wordList[i].lower() == 'how' and wordList[i+1].lower() == 'to':
            hasil7 = wordList[i+2]+' '+wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]+' '+wordList[i+7]
            return hasil7
        if i + 6 <= len(wordList) - 1 and wordList[i].lower() == 'how' and wordList[i+1].lower() == 'to':
            hasil6 = wordList[i+2]+' '+wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]+' '+wordList[i+6]
            return hasil6
        if i + 5 <= len(wordList) - 1 and wordList[i].lower() == 'how' and wordList[i+1].lower() == 'to':
            hasil5 = wordList[i+2]+' '+wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]
            return hasil5
        if i + 4 <= len(wordList) - 1 and wordList[i].lower() == 'how' and wordList[i+1].lower() == 'to':
            hasil4 = wordList[i+2]+' '+wordList[i+3]+' '+wordList[i+4]
            return hasil4
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'how' and wordList[i+1].lower() == 'to':
            hasil3 = wordList[i+2]+' '+wordList[i+3]
            return hasil3
        if i + 2 <= len(wordList) - 1 and wordList[i].lower() == 'how' and wordList[i+1].lower() == 'to':
            hasil2 = wordList[i+2]
            return hasil2

def searchFile(query):
    wordList = query.split()
    for i in range(0, len(wordList)):
        if i + 5 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'file':
            hasil5 = wordList[i+2]+' '+wordList[i+3]+' '+wordList[i+4]+' '+wordList[i+5]
            return hasil5
        if i + 4 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'file':
            hasil4 = wordList[i+2]+' '+wordList[i+3]+' '+wordList[i+4]
            return hasil4
        if i + 3 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'file':
            hasil3 = wordList[i+2]+' '+wordList[i+3]
            return hasil3
        if i + 2 <= len(wordList) - 1 and wordList[i].lower() == 'search' and wordList[i+1].lower() == 'file':
            hasil2 = wordList[i+2]
            return hasil2



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'search on google' in query:
            speak("Opening Google")
            search_google = getSearch(query)
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s' 
            webbrowser.get(open_path).open("http://www.google.com/search?q="+str(search_google))
            speak("Search"+search_google+"on Google")

        elif 'search on youtube' in query:
            speak('Opening Youtube')
            search_youtube = getYoutube(query)
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s' 
            webbrowser.get(open_path).open("https://www.youtube.com/results?search_query="+str(search_youtube))
            speak("Searching"+search_youtube+"on youtube")

        elif 'how to' in query:
            howto = getHow(query)
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s' 
            webbrowser.get(open_path).open("http://www.google.com/search?q="+'how to '+str(howto))
            speak("Searching"+'how to'+' '+howto+"on Google")

        elif 'search file' in query:
            getfile = searchFile(query)
            result = []
            extensi = ['.txt','.py','.cpp','.html']
            for root, dir, files in os.walk('E:/'):
              if query in files:
                 result.append(os.path.join(root, query))
            for pharse in result:
                print(pharse,'\n')
                speak(pharse)

        elif 'search channel name' in query:
            get_channel = getChannel(query)
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(open_path).open()
            pass

        elif 'what\'s news' in query:
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()

            soup_page = soup(xml_page,"xml")
            news_list = soup_page.findAll("item")
            i = 0
            nw = takeCommand().lower()
            while True:
                if 'stop' in query:
                    break
                for news in news_list:
                    i += 1
                    print(str(i)+'.'+news.title.text)
                    speak(str(i)+'.'+news.title.text)
                    print(news.link.text)
                    print(news.pubDate.text)
                    speak(news.pubDate.text)
                    print("-"*50)
                


        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('Wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Open Youtube')
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(open_path).open("Youtube.com")

        elif 'google translate' in query:
            peak('Open Google Translate ')
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(open_path).open("https://translate.google.com/")

        elif 'translate' in query:
            speak('Choose ur language to translate')
            print('Languages: ')
            print('English to Indonesia(id)')
            print('Indonesia to English(en)')
            while True:
                trn = takeCommand().lower()
                if 'English to Indonesia':
                    speak('what do you want to translate')
                    query_en = takeCommand().lower()
                    translator = Translator()
                    translated = translator.translate(query_en, src='en', dest='id')
                    speak(translated.text)
                    print(translated.text)
                    break
                elif 'Indonesia to English':
                    speak('what do you want to translate')
                    query_id = takeCommand_id().lower()
                    translator = Translator()
                    translated = translator.translate(query_id, src='id', dest='en')
                    speak(translated.text)
                    print(translated.text)
                    break


        elif 'write' in query:
            speak('Choose ur language')
            print('Choose your language:')
            print('1.English')
            print('2.Indonesia')
            while True:
                lg = takeCommand().lower()
                if 'english' in lg:
                    while True:
                        write = takeCommand().lower()
                        if 'stop' in write:
                            speak("Writting has Stopped")
                            break
                        elif 'wikipedia' in write:
                            query = takeCommand().lower()
                            write = write.replace('Wikipedia', "")
                            wikipedia.set_lang('en')
                            results = wikipedia.summary(write, sentences=4)
                            pyautogui.write(str(results)+' ', interval=0.18)
                        elif write == 'none':
                            print('none query')
                        elif write == 'enter':
                            pyautogui.press('enter')
                        elif write == 'backspace':
                            pyautogui.press('backspace')
                        elif write == 'space':
                            pyautogui.press('space')
                        # underline
                        elif 'turn on underline' in write:
                            pyautogui.hotkey('ctrl','u')
                            speak('underline is on')
                        elif 'turn off underline' in write:
                            pyautogui.hotkey('ctrl','u')
                            speak('underline is off')
                        # italic
                        elif 'turn on italic' in write:
                            pyautogui.hotkey('ctrl','i')
                            speak('italic is on')
                        elif 'turn off italic' in write:
                            pyautogui.hotkey('ctrl','i')
                            speak('italic is off')
                        # bold
                        elif 'turn on bold' in write:
                            pyautogui.hotkey('ctrl','b')
                            speak('Bold is on')
                        elif 'turn off bold' in write:
                            pyautogui.hotkey('ctrl','b')
                            speak('bold is off')
                        elif '' in write:
                            pyautogui.write(str(write)+' ', interval=0.20)
                    break

                if 'indonesia' in lg:
                    while True:
                        write = takeCommand_id().lower()
                        if 'berhenti' in write:
                            speak("Writting has Stopped")
                            break
                        elif 'wikipedia' in write:
                            write = write.replace('Wikipedia', "")
                            wikipedia.set_lang('id')
                            results = wikipedia.summary(write, sentences=4)
                            pyautogui.write(str(results)+' ', interval=0.1)
                        elif write == 'none':
                            print('none query')
                        elif write == 'enter':
                            pyautogui.press('enter')
                        elif write == 'hapus':
                            pyautogui.press('backspace')
                        elif write == 'spasi':
                            pyautogui.press('space')
                        elif 'hidupkan italic' in write:
                            pyautogui.hotkey('ctrl','i')
                            speak('italic is on')
                        elif 'matikan italic' in write:
                            pyautogui.hotkey('ctrl','i')
                            speak('italic is off')
                        elif 'hidupkan huruf tebal' in write:
                            pyautogui.hotkey('ctrl','b')
                            speak('bold is on')
                        elif 'matikan huruf tebal' in write:
                            pyautogui.hotkey('ctrl','b')
                            speak('bold is off')
                        elif '' in write:
                            pyautogui.write(str(write)+' ', interval=0.1)
                    break
 
        elif 'open browser' in query:
            speak("what do you want to open?")
            while True:
                query = takeCommand().lower()
                if 'mozilla' in query:
                    speak("Opening Mozilla")
                    os.startfile("C:/Program Files (x86)/Mozilla Firefox/firefox.exe")
                    break
                elif 'chrome' in query:
                    speak('Opening Chrome')
                    os.startfile("C:/Users/personal7/AppData/local/Google/Chrome/Application/chrome.exe")
                    break
                elif 'internet explore' in query:
                    speak("Opening Internet Explore")
                    webbrowser.open('google.com')
                    break
                else:
                    speak("you don't have that")
                    break

        elif 'open google' in query:
            speak('Open Google')
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(open_path).open("Google.com")

        elif 'top music' in query or 'trending music' in query:
            speak('opening trending music on youtube')
            open_path = 'C:/Program Files (x86)/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(open_path).open('https://music.youtube.com/watch?v=16YnOUnbE6s&list=RDAMVM9p2wMpVVtXg')
        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'day' in query or 'month' in query or 'year' in query:
            strcal = datetime.datetime.now().strftime("%Y/%m/%d")
            print(strcal)
            speak(f"{strcal}")

        elif 'ipconfig' in query:
            ipconf = os.system("ipconfig")
            speak(ipconf)

        elif 'whatsapp' in query:
            os.startfile('C:/Users/personal7/AppData/Local/WhatsApp/WhatsApp.exe')
            speak('Opening Whatsapp')

        elif 'who is' in query:
            person = getPerson(query)
            wiki = wikipedia.summary(person, sentences=2) 
            print(wiki)
            speak(wiki)                 
                
        elif 'shut down' and 'turn off' in query:
            speak("your Laptop will be shutdown in 10 second")
            os.system("shutdown /s /t 10")

        elif 'restart' and 'reboot' in query:
            speak("your Laptop will be reboot in 10 second")
            os.system("shutdown /r /t 10")

        elif 'microsoft word' in query:
            speak("Opening Microsoft Office Word")
            os.system('start winword')

        elif 'microsoft powerpoint' in query:
            speak("Opening Microsoft Office PowerPoint")
            os.system('start powerpnt')

        elif 'microsoft excel' in query:
            speak("Opening Microsoft Office Excel")
            os.system('start excel')

        elif 'kali linux' in query:
            speak("Opening Kali Linux")
            file_path = 'C:/Users/personal7/VirtualBox VMs/Kali Linux/Kali Linux.vbox'
            os.startfile(file_path)
            speak("Starting Kali Linux")

        elif 'cmd' in query:
            speak("Opening CMD")
            os.startfile("C:/Windows/system32/cmd.exe")

        elif 'sublime text' in query:
            speak("Opening Sublime Text")
            os.startfile("C:/Program Files (x86)/Sublime Text 3/sublime_text.exe")

        elif 'visual code' in query:
            speak("Opening Visual Studio Code")
            os.startfile("C:/Users/personal7/AppData/Local/Programs/Microsoft VS Code/code.exe")


        elif 'unity' in query:
            speak('Starting Unity Engine Game')
            os.startfile("E:/Unity/2018.4.18f1/Editor/Unity.exe")

        elif 'netbeans' in query:
            speak('Starting NetBeans IDE')
            os.startfile("C:/Program Files/NetBeans 8.0.2/bin/netbeans64.exe")

        elif 'record' in query:
            speak("Starting record ur Laptop")
            os.startfile("C:/Program Files (x86)/Bandicam/bdcam.exe")

        elif 'play film name' in query:
            film = getFilm(query)
            speak("Start Playing"+query)































        # music query
        elif 'play music' in query:
            speak("Playing music")
            from pygame import mixer
            from musiclist import *
            speak('Choose the music:')
            mixer.init()
            while True:
                query = takeCommand().lower()
                if query == '1':
                    mixer.music.load("E:/ferdy/music by input/4U.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '2':
                    mixer.music.load("E:/ferdy/music by input/C U Again.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '3':
                    mixer.music.load("E:/ferdy/music by input/Dreams.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '4':
                    mixer.music.load("E:/ferdy/music by input/Everything.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '5':
                    mixer.music.load("E:/ferdy/music by input/Fearless.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '6':
                    mixer.music.load("E:/ferdy/music by input/Fight Back.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '7':
                    mixer.music.load("E:/ferdy/music by input/Get Busy.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '8':
                    mixer.music.load("E:/ferdy/music by input/Grateful.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '9':
                    mixer.music.load("E:/ferdy/music by input/Happier.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '10':
                    mixer.music.load("E:/ferdy/music by input/Heroes Tonight.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '11':
                    mixer.music.load("E:/ferdy/music by input/Inspiration.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '12':
                    mixer.music.load("E:/ferdy/music by input/Light It Up.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()
    
                elif query == '13':
                    mixer.music.load("E:/ferdy/music by input/Linked.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()
    
                elif query == '14':
                    mixer.music.load("E:/ferdy/music by input/Make Me Move.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()
    
                elif query == '15':
                    mixer.music.load("E:/ferdy/music by input/Melody.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()
    
                elif query == '16':
                    mixer.music.load("E:/ferdy/music by input/Perfect 10.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()
    
                elif query == '17':
                    mixer.music.load("E:/ferdy/music by input/Pokemon.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '18':
                    mixer.music.load("E:/ferdy/music by input/Rise.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '19':
                    mixer.music.load("E:/ferdy/music by input/Sandy Freaks.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '20':
                    mixer.music.load("E:/ferdy/music by input/Savannah.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '21':
                    mixer.music.load("E:/ferdy/music by input/Season.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '22':
                    mixer.music.load("E:/ferdy/music by input/Shootin Stars.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '23':
                    mixer.music.load("E:/ferdy/music by input/Stronger.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()    

                elif query == '24':
                    mixer.music.load("E:/ferdy/music by input/Sunflower.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()
    
                elif query == '25':
                    mixer.music.load("E:/ferdy/music by input/Sweet Scar.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '26':
                    mixer.music.load("E:/ferdy/music by input/The Next Episode.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '27':
                    mixer.music.load("E:/ferdy/music by input/Top 20 songs of NEFFEX 2018.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '28':
                    mixer.music.load("E:/ferdy/music by input/Traffic Light.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '29':
                    mixer.music.load("E:/ferdy/music by input/Vacation.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '30':
                    mixer.music.load("E:/ferdy/music by input/Weakness.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '31':
                    mixer.music.load("E:/ferdy/music by input/Why We Lose.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '32':
                    mixer.music.load("E:/ferdy/music by input/Wicked Ways.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif query == '33':
                    mixer.music.load("E:/ferdy/music by input/With You.mp3")
                    mixer.music.set_volume(0.5)
                    mixer.music.play()

                elif 'stop' in query:
                    mixer.music.stop()
                    speak("Stop Playing Music")
                    break
                elif 'pause' in query:
                    mixer.music.pause()
                    speak("Music Pause")
                elif 'resume' in query:
                    mixer.music.unpause()
                    speak("Music Resume")

        for pharse in badwords:
            if pharse in query:
                speak(random.choice(none_dictionary))
                playsound('Speech Disambiguation.wav')

        for pharse in close_list:
            if pharse in query:
                speak(random.choice(close_send))
                playsound('Speech off.wav')
                sys.exit()




        

        
