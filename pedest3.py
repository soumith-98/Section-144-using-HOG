#Note: You have to delete the existing audio1.mp3, if any, before running this program
#pip3 install gtts
# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio
mytext = input("Type the message to be inserted in audio file: ") 

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("audio1.mp3") 
print('Audio file successfully created as audio1.mp3')

# Playing the converted file 
#os.system("start more.mp3") 
