from gtts import gTTS
import os

# Input text
text =input( "Enter the text:")

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save the speech to a file
tts.save("output.mp3")

# Optionally, play the file 
os.system("start output.mp3")
