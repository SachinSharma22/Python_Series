import pyttsx3


# Problem 1 => Write twinkle twinkle little star in python

poem = '''
Twinkle Twinkle Little Star
How i wonder what you are
once above the bird so high
like the dimond in the sky
'''
# print(poem)

# Problem 2 => Use REPL and print table of 5 using it

# Install an external module and use it
engine = pyttsx3.init()
engine.say("I will speak text")
engine.runAndWait()