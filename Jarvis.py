import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command() -> object:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "jarvis" in command:
                command = command.replace("jarvis", "")
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I%M %p")
        print(time)
        talk("current time is" + time)
    elif "what is" in command:
        object = command.replace("what is", "")
        info = wikipedia.summary(object, 1)
        print(info)
        talk(info)

    elif "who is" in command:
        object = command.replace("who is", "")
        info = wikipedia.summary(object, 1)
        print(info)
        talk(info)
    else:
        talk("Lord KAYODE, could you repeat that again")


while (True):
    run_jarvis()


