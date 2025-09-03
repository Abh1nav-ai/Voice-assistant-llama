import speech_recognition as sp
import pyttsx3         #pythonTexttoSpeech
import pywhatkit
import datetime

from llama_cpp import Llama
# Load LLaMA model locally
llm = Llama(
    model_path = "C:/Users/asus/Models/Llama/Meta-Llama-3-8B-Instruct.Q3_K_M.gguf",
    n_ctx=2048,
    n_threads=6  # Use based on your CPU cores
)



ear = sp.Recognizer()
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)




def ask_llama(question):
    prompt = f"### Instruction:\n{question}\n\n### Response:"
    response = llm(prompt, max_tokens=200, stop=["###"])
    speak(response["choices"][0]["text"].strip())


def speak(text):
    speaker.say(text)
    print("🤖:", text)
    speaker.runAndWait()

def takecommand():
    try:  # in case microphone is  not working
        with sp.Microphone() as source:
            print("🎙️ Listening...")
            voice = ear.listen(source)
            command = ear.recognize_google(voice)
            command = command.lower()
            if 'king' in command:  # listens only when her name is spkoen
                #speak(command)
                command=command.replace('king', '')
                print("📢 Command:", command)

    except:
        pass
    return command

def run_pajji():

        command = takecommand()
        print(command)


        # === Stop Command ===
        if 'thanks stop' in command or 'stop' in command:
            speak("You're welcome. Goodbye!")
            break

    if 'play' in command:
        song = command.replace('play','')
        speak('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        speak('current time is ' +datetime.datetime.now().strftime('%I:%M %p'))

    else:
        command=command.replace('king','')
        ask_llama(command)


run_pajji()

