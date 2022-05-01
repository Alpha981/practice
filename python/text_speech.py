#program for text to speech
'''
import pyttsx3
engine=pyttsx3.init()
text='hi sameer'
engine.say(text)
engine.runAndWait()    '''


#program for speech to text
''' 
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    r.adjust_for_ambient_noise(source,duration=1)
    print('recording for 10 secs')
    audio = r.listen(source,timeout=10)
    print("done recording")

try:
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-ln') 
    print(f"user said: {query}\n") 
       
except Exception as e:
    print("say that again please...")  
    print(e)      '''
    
#program for audio to text
'''
import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile(filename_or_fileobject) as source:
    print("Listening...")
    audio = r.listen(source)
    print("done recording")
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-ln') 
        print(f"user said: {query}\n") 
        
    except Exception as e:
        print("say that again please...")  
        print(e)   
'''