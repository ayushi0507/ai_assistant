import text_to_speech
import speech_to_text
import datetime
import webbrowser


def action(data):
  user_data = data.lower()

  if "hello" in user_data:
    text_to_speech.text_to_speech("Hello! How can I assist you today?")
    return "Hello! How can I assist you today?"

  elif "how are you" in user_data:
    text_to_speech.text_to_speech("I am just a program, but thank you for asking! How can I help you?")
    return "I am just a program, but thank you for asking! How can I help you?"

  elif "what is your name" in user_data:
    text_to_speech.text_to_speech("I am your AI assistant. How can I assist you today?")
    return "I am your AI assistant. How can I assist you today?"

  elif "thank you" in user_data:
    text_to_speech.text_to_speech("You're welcome! If you have any questions, feel free to ask.")
    return "You're welcome! If you have any questions, feel free to ask."

  elif "goodbye" in user_data:
    text_to_speech.text_to_speech("Goodbye! Have a great day!")
    return "Goodbye! Have a great day!"

  elif "what is your purpose" in user_data:   
    text_to_speech.text_to_speech("I am here to assist you with your queries and provide information. How can I help you?")
    return "I am here to assist you with your queries and provide information. How can I help you?"

  elif "tell me a joke" in user_data:
    text_to_speech.text_to_speech("Why don't scientists trust atoms? Because they make up everything!")
    return "Why don't scientists trust atoms? Because they make up everything!"

  elif "tell me a story" in user_data:
    text_to_speech.text_to_speech("Once upon a time, in a land far away, there lived a wise old owl who knew all the secrets of the forest.")
    return "Once upon a time, in a land far away, there lived a wise old owl who knew all the secrets of the forest."

  elif "good morning" in user_data:
    text_to_speech.text_to_speech("Good morning! I hope you have a wonderful day ahead.")
    return "Good morning! I hope you have a wonderful day ahead."

  elif "good night" in user_data:
    text_to_speech.text_to_speech("Good night! Sleep well and dream sweetly.")   
    return "Good night! Sleep well and dream sweetly."

  elif "what time is it" in user_data:
    current_time = datetime.datetime.now().strftime("%H:%M")
    text_to_speech.text_to_speech(f"The current time is {current_time}.")
    return f"The current time is {current_time}."

  elif "what is the date today" in user_data: 
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    text_to_speech.text_to_speech(f"Today's date is {current_date}.")
    return f"Today's date is {current_date}."

  elif "shutdown" in user_data:
    text_to_speech.text_to_speech("Shutting down. Goodbye!")
    return "Shutting down. Goodbye!"

  elif "play music" in user_data:
    text_to_speech.text_to_speech("Playing music for you.")
    webbrowser.open("https://spotify.com")
    return "Playing music for you."

  elif "open youtube" in user_data:
    text_to_speech.text_to_speech("Opening YouTube for you.")
    webbrowser.open("https://youtube.com")
    return "Opening YouTube for you."

  elif "open google" in user_data:    
    text_to_speech.text_to_speech("Opening Google for you.")
    webbrowser.open("https://google.com")
    return "Opening Google for you."


  else :
    text_to_speech.text_to_speech("I'm sorry, I didn't understand that. Can you please repeat?")
