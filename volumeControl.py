# sudo apt-get install python-alsaaudio
# DO THIS INSTEAD: amixer sset 'Master' 50%
"""
import alsaaudio as audio

# 1. Collecting actual mixers available (will provide a list of available cards): 
scanCards = audio.cards()
print("cards:", scanCards)
"""