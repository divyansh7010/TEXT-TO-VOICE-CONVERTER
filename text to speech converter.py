import pyttsx3

engine = pyttsx3.init()
# whatever text you will enter the system will repeat it.
text = "MY NAME IS DIVYANSH RAGHUWANSHI"

engine.say(text)

engine.runAndWait()