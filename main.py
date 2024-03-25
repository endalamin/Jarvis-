import speech_recognition as alamin
import pyttsx3
import datetime
import wikipedia
import webbrowser

#Taking voice for my pc 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#This function convart text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This function convart voice to text

def takeCommand():
    r = alamin.Recognizer()
    with alamin.Microphone() as sourec:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(sourec)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User Said:{query}\n")


    except Exception as e:
        #print(e)
        print("say that again please.....")
        return "None"
    return query 


# the function for wish me by using time 
def wish_time():
    hour = (datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good morning Al Amin Sir . How are you doing")

    elif hour>12 and hour<18:
        speak("Good afternoon Al Amin Sir . How are you doing")   

    else:
         speak("Good evening Al Amin Sir . How are you doing")  

    speak("I am jarvis. Tell me sir how can i help you")     



if __name__ == "__main__":
    wish_time()
    while True:
     query=takeCommand().lower()


     if 'time' in query:
         strTime = datetime.datetime.now().strftime("%H:%M:%S")
         speak(f"Sir the time is{strTime}")

     elif 'ifter time' in query:
          speak("Sir the time at 6.00 pm")

     elif 'exit' in query:
         print("Sure Al Amin sir")
         exit() 

     # This query for search somthing for wikipedia 
     elif 'wikipedia' in query:
         speak("searching wikipedia")
         query = query.replace("wikipedia", "")
         results = wikipedia.summary(query,sentences=2)
         speak("According to wikipedia")
         print(results)
         speak(results)


     #This query for open google
     elif 'open google' in query:
         speak("Ok sir. please type here what do you want to read")
         webbrowser.open("google.com")

     
     #This query for open facebook
     elif 'open facebook' in query:
         speak("Ok sir. please type here what do you want to read")
         webbrowser.open("facebook.com")   

     #This query for open youtube
     elif 'open youtube' in query:
         speak("Ok sir. please type here what do you want to read")
         webbrowser.open("youtube.com")

     #This query for open linkedin
     elif 'open linkedin' in query:
         speak("Ok sir. please type here what do you want to read")
         webbrowser.open("linkedin.com")   

     #This query for open github
     elif 'open github' in query:
         speak("Ok sir. please type here what do you want to read")
         webbrowser.open("github.com") 

     #This query for open google chrome
     elif 'open google  chrome' in query:
         speak("Ok sir. please type here what do you want to read")
         webbrowser.open("google chrome.com")         
      
      
            
        


   
    


    




















