import random
import speech_recognition as sr
import pyttsx3

def greet():
  greetings = ["Hello", "Hi", "Howdy", "Hey there"]
  return random.choice(greetings)

def help():
  help_messages = ["I can help you with basic tasks on your computer.", "What can I do for you?", "Just ask me what you need help with."]
  return random.choice(help_messages)

def quit():
  return "Goodbye!"

def take_command():
  recognizer = sr.Recognizer()
  with sr.Microphone() as mic:
    print("Speak now...")
    recognizer.pause_threshold = 1
    audio = recognizer.listen(mic)

  try:
    command = recognizer.recognize_google(audio)
    print("You said: " + command)
  except:
    command = ""

  return command

def main():
  print(greet())
  while True:
    command = take_command()

    if command == "quit":
      break
    elif command == "help":
      print(help())
    else:
      print("I don't know how to do that.")

if __name__ == "__main__":
  main()
