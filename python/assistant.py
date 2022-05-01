#neeeddd internet connectivity
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyaudio

print("Initializing sam")
MASTER="sameer"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#this function wish u according to time
def wishme():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour>=0 and hour <12:
        speak("Good morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("GOod afternoon" + MASTER)

    else: 
        speak("Good evening" + MASTER)        

#this function take commmand from microphone
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-ln') 
        print(f"user said: {query}\n") 
       
    except Exception as e:
        print("say that again please...")  
        return "None"      
    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail', 'password') 
    server.sendmail("senderemail", to,content)
    server.close()

if __name__=="__main__":
    #main program starts here
    speak("Initializing sam...")
    wishme()
    while True:
        query = takecommand()
        #logic  for executing tasks as per the query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences =2)
            print(results)
            speak(results)

        elif(query=='open YouTube'):
        # webbrowser.open("youtube.com")
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif(query=='open google'):
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif(query=='open instagram'):
            url = "instagram.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif(query=='the time'):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{MASTER} the time is {strTime}")

        elif(query=='open firefox'):
            codepath = "C:\\Users\\Public\\Desktop\\Firefox.lnk"
            os.startfile(codepath)

        elif(query=='email to sam'):
            try:
                speak("what should i send")
                content = takecommand()
                to = 'senderemail'
                sendEmail(to,content)
                speak("email has been sent successfully")
            except Exception as e:
                print(e)


