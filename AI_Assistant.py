import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import pyjokes
import smtplib
import random
import pyautogui

#######################################################################################

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)                  #selecting male voice
name = "Your Name"
new_name = ""

#######################################################################################



'''Function which is used to speak the sentence'''
def speak(audio):
    engine.say(audio)
    engine.runAndWait()




''' Starter function which greetes everytime wheen the program runs '''
def Wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning " + name)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + name)
    else:
        speak("Good Evening " + name)
    speak("I am Jarvis, your personal desktop Assistant. Please tell me how may I help you")




'''The function which listen whatever instructions u say to the AI jarvis'''
def listening_function():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening commands.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-in')
        print("you said : " + query)

    except Exception as e:
        print("Failed to recognize... will you please say that again")
        speak("Failed to recognize... will you please say that again")
        return "None"
    return query



''' Function used to send Email '''
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your Email Id', 'Your Email Id password')
    server.sendmail('Your Email Id', to, content)
    server.close()


''' Main program '''
if __name__ == "__main__":
    starting_command=""
    print("Welcome")
    time.sleep(1)

    print(" To start please say 'wake up'")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        starting_command = r.recognize_google(audio, language='en-in')
        print("you said : " + starting_command)

    except Exception as e:
        pass

    starting_command = starting_command.lower()

    if 'wake up' in starting_command:
        print('Launching.....')
        time.sleep(2)
        print("Desktop Assistant Running")
        speak("Desktop Assistant Running")
        Wish()

        while True:
            query = listening_function().lower()  # converting it into lower case

            if 'wikipedia' in query:
                speak("Searching Wikipedia.....")
                query = query.replace("wikipedia", "")
                query = query.replace("search","")
                query = query.replace("from", "")
                result = wikipedia.summary(query, sentences=1)
                speak("According to wikipedia")
                print(result)
                speak(result)


            elif 'open youtube' in query:
                speak("opening you tube")
                webbrowser.open("youtube.com")
                

            elif 'open google' in query:
                speak("opening Google")
                webbrowser.open("google.com")
                

            elif 'open github' in query:
                speak("opening github")
                webbrowser.open("github.com")
                

            elif 'open disney plus hotstar' in query:
                speak("opening disney plus hot star")
                webbrowser.open("Website link")
                

            elif 'open my personal gmail account' in query:
                speak("opening your personal mail")
                webbrowser.open("Your Gamil acoount link")
                

            elif 'open my college mail' in query:
                speak("opening collage mail")
                webbrowser.open("Your Account link")
                time.sleep(7)

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"Sir, the time is {strTime}")


            elif 'open visual studio code' in query:
                speak("opening Visual studio code")
                filepath = "Path where your Visual Studio Code exe file is installed"
                os.startfile(filepath)
                time.sleep(5)

            elif 'play some music' in query:
                speak("searching songs")
                num = random.randint(1,9)                      #According to the number of songs present
                music_folder = "Path of Music Folder"
                songs = os.listdir(music_folder)
                speak("Following songs are found ....")
                print(songs)
                speak("Starting a random song...")
                os.startfile(os.path.join(music_folder, songs[num]))
                

            elif 'joke' in query:
                speak(pyjokes.get_joke())

            elif 'quit' in query:
                speak("Quitting the program, Goodbye , Have a nice day Sir!!!")
                break

            elif 'exit' in query:
                speak("Quitting the program, Goodbye , Have a nice day Sir!!!")
                break

            elif 'paint' in query:
                paint_path = "paint exe file path"
                os.startfile(paint_path)
                speak("opening paint")
                speak("Random Drawing")
                time.sleep(2)
                distance = 80

                while distance > 0:
                    pyautogui.dragRel(distance, 0, duration=0.2)  
                    distance = distance - 5
                    pyautogui.dragRel(0, distance, duration=0.2) 

                    pyautogui.dragRel(-distance, 0, duration=0.2) 
                    distance = distance - 5

                    pyautogui.dragRel(0, -distance, duration=0.2)  

            elif 'send mail to my college gmail account' in query:                    # to use this make sure you enabled less secure apps permissions
                try:
                    speak("Ok, what is the mail content you want me to send?")
                    content = listening_function()
                    to = "Receiver mail id"
                    sendEmail(to ,content)
                    speak("Email successfully sent")
                    
                except Exception as e:
                    print(e)
                    speak("Sorry due to some internal error we are not able to send mail")

            elif 'please tell me my name' in query:
                speak("Your name is " + name)

            elif 'change my name' in query:
                speak("What do you want me to call you ? ")
                with sr.Microphone() as source:
                    print("Listening new Name.....")
                    r.pause_threshold = 1
                    audio = r.listen(source)
                try:
                    print("Recognizing.....")
                    new_name = r.recognize_google(audio, language='en-in')
                    print("you said that I call you by name : " + new_name)
                    speak("name successfully changed, from now onwards I will call you by " + new_name)
                    name = new_name
                except Exception as e:
                    pass


    else:
        pass















        

    

