import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
     
    elif hour>=12 and hour<18:   
        speak("Good AfterNoon!")

    else:
        speak("Good Evening!")
        
    
    speak("I am Jarvis Sir , Namaste!")

def takeCommand():
    #it takes microphone input from the user and returns string output

   r = sr.Recognizer()
   with sr.Microphone() as source: 
       print("Listening...")
       r.pause_threshold = 1
       audio = r.listen(source)
       
   try:
       print("Recognizing...")
       query = r.recognize_google(audio, language="en-IN")
       print(f"User said: {query}\n")       
       
   except Exception as e: 
       #print(e)
       print("Say that Agin please...")
       return "None"
   return query
   
if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
      query = takeCommand().lower()

      #Logic for executing tasks based on query
      if 'wikipedia' in query:
          speak('Searching Wikipedia...')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query, sentences=2)
          speak("According to Wikipedia")
          print(results)
          speak(results)

      elif 'open youtube' in query:
          webbrowser.open("youtube.com")

      elif  'open whatsapp' in query:
          webbrowser.open("https://web.whatsapp.com/")

      elif  'open google' in query:
          webbrowser.open("google.com")

      elif  'sabse badi khushi' in query:
          webbrowser.open("https://www.youtube.com/shorts/cbjZE6nG2yc")
      
      elif  'the time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir, the time is {strTime}")
    
      elif 'open vs code' in query:
          codePath = "C:\\Users\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codePath)

      elif 'play music' in query:
          codePath1 = "C:\\Users\\HP\\Desktop\\Shubham\\JARVIS\\shoorveer_3.mp3"
          os.startfile(codePath1)
      elif 'open self' in query:
          codePath2 = "http://127.0.0.1:8000/"
          os.startfile(codePath2)
      elif 'open jee' in query:
          codePath3 = "http://127.0.0.1:8000/jee/"
          os.startfile(codePath3)
      elif 'open gate' in query:
          codePath4 = "http://127.0.0.1:8000/gate/"
          os.startfile(codePath4)
      elif 'open computer courses' in query:
          codePath5 = "http://127.0.0.1:8000/computercourses/"
          os.startfile(codePath5)
      elif 'open java' in query:
          codePath6 = "http://127.0.0.1:8000/computercourses/#java"
          os.startfile(codePath6)
      elif 'open python' in query:
          codePath7 = "http://127.0.0.1:8000/computercourses/#python"
          os.startfile(codePath7)
      elif 'open c plus plus' in query:
          codePath8 = "http://127.0.0.1:8000/computercourses/#c++"
          os.startfile(codePath8)
      elif 'open html' in query:
          codePath9 = "http://127.0.0.1:8000/computercourses/#html_css"
          os.startfile(codePath9)
      elif 'open data structure' in query:
          codePath10 = "http://127.0.0.1:8000/computercourses/#data"
          os.startfile(codePath10)
      elif 'open algorithm' in query:
          codePath11 = "http://127.0.0.1:8000/computercourses/#algo"
          os.startfile(codePath11)
      elif 'open home' in query:
          codePath12 = "http://127.0.0.1:8000/home/"
          os.startfile(codePath12)

          