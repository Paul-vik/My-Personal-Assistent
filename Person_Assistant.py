import pyttsx3 #pip install pywin32   #pip install pyttsx3
import datetime
import speech_recognition as SR
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb
import pyjokes
import os
import psutil
import pyautogui



engine = pyttsx3.init()

def speak(audio): #to make our edith to speak
    engine.say(audio)
    engine.runAndWait()

def time(): #to tell the user time
    CurrentTime = datetime.datetime.now().strftime("%I  %M  %S")
    speak("The current time is " + CurrentTime)

def date(): # to tell the user date 
    CurrentDate = datetime.datetime.now().strftime("%A %d : %b : %Y")
    speak("The current date is " + CurrentDate)

def greetings(): # to greet the user 
    hour = int(datetime.datetime.now().hour)
    if hour <= 12:
        greet = "Good Morning"
    elif hour <= 17:
        greet = "Good Afternoon"
    elif hour <= 24:
        greet = "Good Evening"
    speak(greet + "And Welcome sir. I am Paul, i am Your Personal Artificial Intelligence. How can i help you? ")

def userCommand(): #to take command from user for short commands
    r = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        
        try :
            print("Recognizing....")
            query = r.recognize_google(audio, language = "en-in")
            print(query)
            return query
    
        except Exception as e:
            speak("Unable to Proceed with Your request Check your internet Connection or some other problem ")
            exit()
            
def command(): # to take command from user using microphone for long scripts
    r = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
        
        try :
            print("Recognizing....")
            query =  r.recognize_google(audio, language = "en-in")
            print(query)
            return query
    
        except Exception as e:
            speak("Unable to Proceed with Your request Check your internet Connection ")
            exit()
        
def multiplication(query): #for mutliplication
    li = list(query.split(" "))
    mul = 1
    numbers = [i for i in query if i.isdigit()]
    for i in numbers:
        mul = mul *  int(i)
    speak("The Multiplication of " + "*".join(numbers) + "is " + str(mul))

def wiki(query): #to open wikipedia
    speak("Searching ")
    query = query.replace("wikipedia", "")
    print(query)
    result = wikipedia.summary(query, sentences = 2) # return first two sentences in wikipedia
    speak(result)


def sendMail(to, content): #to send mail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.echlo()
    server.starttls()
    server.login("paulvik9060@gmail.com","password")
    server.sendmail("paulvik9060@gmail.com", to, content)
    server.close()

def jokes(): #generate jokes
    speak(pyjokes.get_joke())

def cpu(): # to check for cpu usage and battery usage
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at " + str(battery.percent))

def screenshot(): # To take screen shot
    img = pyautogui.screenshot()
    # img.save("C:\Users\Yashwanth\Pictures\Screenshots\ss.png")
    img.save("I:\j")

if __name__ == "__main__":
    greetings()    
    while(True):
        query = userCommand().lower()
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'multiplication' in query:
            multiplication(query)
            
        elif 'wikipedia' in query:
            wiki(query)
            
        elif 'mail' in query:
            try:
                speak("What should i have to sir")
                content = userCommand().lower()
                print(content)
                speak("To whom should i sent it sir")
                to = userCommand().lower()
                print(to)
                sendMail(to, content)
                speak("Email has been sent sir")
            except:
                speak("unable to proceed with your information")
                
        elif 'search' in query:
            new = 2
            speak("What should I search for")
            #base_url = "http://www.google.com/?#q=" #notused
            #chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s"   #notused
            search = userCommand().lower()
            print(search)
            #final_url = base_url + search.replace(" ", "%20")      #notused       
            wb.open("www." + search + ".com", new=new)
            break
        
        elif 'logout' in query:
            os.system("shutdown -l")
        
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        
        elif 'restart' in query:
            os.system("shutdown /r")

        elif 'jokes' in query:
            jokes()
        
        elif 'cpu' in query:
            cpu()
            
        elif 'play songs' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'remember it' in query:
            speak("What should i remember sir")
            rememberData = command()
            speak("you said me to remember that " + rememberData)
            remember = open('data.text', 'w')
            remember.write(rememberData)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt','r')
            speak("You said me to remember that " + remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("Done")
            
        elif 'offline' in query:  #to stop our Edith
            speak("Thank you Sir have a great Day")
            break
    
