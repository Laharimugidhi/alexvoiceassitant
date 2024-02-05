import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def get_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alex' in command:
                command=command.replace('alex','')
                print(command)
    except:
        pass
    return command
while True:
    def run_alex():
        command=get_command()
        print(command)
        if 'hello' in command:
            greetings = "Hello! I am alex, your voice assistant"
            question = 'How may I help you ?'
            print(greetings)
            talk(greetings)
            print(question)
            talk(question)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk("present time is ")
            print(time)
            talk(time)
        elif 'date' in command:
            date = datetime.date.today()
            print(date)
            talk(date)
        elif 'what' in command:
            about = command.replace('what', '')
            info = wikipedia.summary(about, sentences=2)
            print(info)
            talk(info)
        elif 'who' in command:
            about = command.replace('who', '')
            info = wikipedia.summary(about, sentences=2)
            print(info)
            talk(info)
        elif 'stop' in command:
            seeyou = "See You"
            greet="have a nice day"
            print(seeyou)
            talk(seeyou)
            print(greet)
            talk(greet)
            exit()
        else:
            print("Sorry, I don't get it , Will you please repeat your command")

    run_alex()
