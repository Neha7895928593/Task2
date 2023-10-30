
from web import *
import os
import wikipedia
# from urllib.request import urlopen
import randfacts
import webbrowser
from weather import*

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    wishMe()
    while True:
        query = takeCommand().lower()  
        if not query:
            speak("I didn't hear your query. Please repeat.")
            continue

        if query == "exit" or query == "quit":
           speak("if you want ask  your query  again,I will be ready for you")
           speak(" Thank you for give me , your precious time,Goodbye!")
           break
        if 'what' in query and 'about' in query and "you" in query:
            speak("I am also having a good day.")
            speak("What can I do for you?")
        
      
        elif "news" in query:
            print("Sure, I will read the 5 latest news headlines for you")
            speak("Sure, I will read the 5 latest news headlines for you")

            news_list = news()  
            for news_headline in news_list:
                print(news_headline)
                speak(news_headline)
        elif "fact" in query or "facts" in query: 
            speak("Sure")
            fact = randfacts.getFact()
            speak(fact)
            print(fact)
        elif "jokes" in query or "joke" in query:  
            speak("Sure, I provide jokes for your laughter")
            smile=joke()
            
            print(smile)
            speak(smile)
        elif "who am I" in query.lower().strip():
               speak("If you talk, then definitely you're human.")
        elif "weather" in query or "mosam" in query: 
            speak("Please provide the city name")
            city_name = takeCommand()
            get_weather(city_name)
        
        elif 'open youtube' in query:
            speak("Here you go to Youtube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google chrome' in query:
            speak("Here you go to Google")
            webbrowser.open("https://www.google.com")
        elif "motivation quote" in query or "quote" in query:
            motivation_quote = get_motivational_quote()
            speak("Here's a motivational quote for you:")
            speak(motivation_quote)
            print(motivation_quote)
        elif "how to become successful" in query:
            speak("here's provide some tips how become successful in life for you ")
            message = motivational_success_message()
            speak(message)
            tipss = success_tips()
            for tip in tipss:
               speak(tip)
        elif "health" in query or "tips" in query:
               speak("here's provide healthcare tips please listen carefully")
               tipsh = health_tips()
               for tip in tipsh:
                speak(tip)
        elif "fever" in query:
               speak(" here provide general fever information and tips when you feel like fever")
               fever_info = fever_healthcare()
               for tip in fever_info:
                speak(tip)
        elif "population" in query:
            speak("Sure, please tell me the name of the state.")
            state_name = takeCommand().strip()  
            population_info = get_population_by_state(state_name)
            speak(population_info)

        elif "study guidance" in query or "guidance for study" in query:
             speak("I'll provide you with some study suggestions. Let's get started!")
    
             guidance = study_guidance()
             for tip in guidance:
               speak(tip)
        elif "calculate" in query or "calculator" in query:
              user_query = query.replace("calculate", "").replace("calculator", "").strip()
              answer = calculate(user_query)
              speak(answer)
        elif "identify color code" in query or "color name" in query:
             user_query = query.replace("identify color code", "").replace("color name", "").strip()
             answer = identify_color_code(user_query)
             speak(answer)
