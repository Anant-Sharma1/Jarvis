import pyttsx3

# Initialize the text-to-speech engine with the "sapi5" speech API
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[4].id)
engine.setProperty('rate',180)
engine.setProperty('volume',4.8)
# Get the available voices

# Define a function to speak given text
def speak(args,**kwargs):
    print("")
    print(f"AI : {args}")
    print("")
    engine.say(args)  # Use the text-to-speech engine to say the provided text
    engine.runAndWait()
  # Wait for the speech engine to finish speaking

if __name__ == "__main__":
    # get_voices()
    speak("Hello" + "anant")
    print(f"", end="\r", flush=True)