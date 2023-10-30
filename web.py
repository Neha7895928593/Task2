import pyttsx3 as p
import datetime
import speech_recognition as sr
import requests
from api import Key  

from webcolors import CSS3_HEX_TO_NAMES, hex_to_name


engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 130)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning ma'am!")
    elif 12 <= hour < 18:
        speak("Good Afternoon ma'am!")
    else:
        speak("Good Evening ma'am!")

    assname = "neha"
    speak("I am your voice assistant. How can I assist you today?")
    speak(assname)
def takeCommand():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
             recognizer.energy_threshold = 10000
             recognizer.adjust_for_ambient_noise(source, duration=1.2)
             print('Listening...')
             audio = recognizer.listen(source)
             print("Recognizing...")

    try:
             query = recognizer.recognize_google(audio, language="eng")
             print(f"You said: {query}\n")
             return query.lower()
    except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
    except sr.RequestError:
            print("Sorry, I couldn't request results. Check your internet connection.")
            return ""



def news():
    api_url = "https://newsapi.org/v2/everything?q=apple&from=2023-10-26&to=2023-10-26&sortBy=popularity&apiKey=" + Key

    try:
        data = requests.get(api_url).json()
        articles = data.get("articles", [])
        return [f'Number {i + 1}: {article["title"]}' for i, article in enumerate(articles[:5])]
    except requests.RequestException as e:
        print(f"Failed to fetch news: {e}")
        return []

def joke():
    url = "http://official-joke-api.appspot.com/random_joke"
    try:
        json_data = requests.get(url).json()
        return [json_data.get("setup", ""), json_data.get("punchline", "")]
    except requests.RequestException as e:
        print(f"Failed to fetch a joke: {e}")
        return ["", ""]

def get_motivational_quote():
    url = "https://zenquotes.io/api/random"
    response = requests.get(url)
    data = response.json()
    quote = data[0]['q']  
    author = data[0]['a']  
    return f"{quote} - {author}"
def success_tips():
    tips = [
        "Set clear and specific goals. Define what success means to you.",
        "Develop a strong work ethic. Consistent effort is key to success.",
        "Learn from failures. Mistakes are opportunities for growth.",
        "Continuous learning is essential. Stay curious and keep improving your skills.",
        "Build a strong support network. Surround yourself with positive and supportive people.",
        "Stay persistent and resilient. Success often involves overcoming challenges and setbacks.",
        "Manage your time effectively. Prioritize tasks and avoid procrastination.",
        "Take care of your physical and mental health. A healthy body and mind are fundamental to success.",
        "Embrace change and adapt. Success often requires flexibility and open-mindedness.",
        "Give back to others. Helping others can bring a sense of fulfillment and contribute to your success.",
    ]
    return tips          
def motivational_success_message():
    message = "Success is a journey, not a destination. Keep moving forward, and you'll achieve your dreams."
    return message
def health_tips():
    tips = [
        "Remember to drink plenty of water to stay hydrated.",
        "A balanced diet with fruits and vegetables is essential for good health.",
        "Regular exercise is important for staying fit and healthy.",
        "Don't forget to get enough sleep to recharge your body and mind.",
        "Washing your hands frequently can help prevent the spread of germs.",
    ]
    return tips
def fever_healthcare():
    tips = [
        "Fever is a common symptom of many illnesses and infections.",
        "It's important to rest and stay hydrated when you have a fever.",
        "Over-the-counter medications like acetaminophen or ibuprofen can help reduce fever and relieve discomfort. Be sure to follow the recommended dosage.",
        "If your fever persists for more than a few days or is accompanied by severe symptoms, it's advisable to consult a healthcare professional.",
    ]
    return tips


def get_population_by_state(state_name):
    try:
        
        api_key = "950f3bd3010127d3459c158a28b835194dbd5dd6"  
        url = f"https://api.census.gov/data/2019/pep/population?get=NAME,POP,REGION,STATE&for=state:{state_name.upper()}&key={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            population = data[1][1]  
            return f"The population of {state_name} is approximately {population}."
        else:
            return f"Sorry, I couldn't retrieve population data for {state_name}. Error: HTTP Status Code {response.status_code}"

    except requests.exceptions.RequestException as e:
        return f"Sorry, there was a network issue while fetching data. Please check your internet connection."

    except Exception as e:
        return f"Sorry, an error occurred while processing the request. Error: {str(e)}"




    
def study_guidance():
    advice = [
        "I understand that sometimes it's challenging to focus on studying. Here are some tips to help you get started:",
        "1. Set clear goals for what you want to achieve during your study session.",
        "2. Create a quiet and organized study space with minimal distractions.",
        "3. Break your study sessions into smaller, manageable chunks with short breaks in between.",
        "4. Use active learning techniques such as summarizing, teaching the material to someone, or using flashcards.",
        "5. Stay motivated by reminding yourself of your long-term goals and the benefits of your studies.",
        "6. Don't forget to take care of your physical and mental health. Get enough sleep and stay hydrated."
    ]
 
    return advice



def calculate(expression):
    try:
        result = eval(expression)
        return f"The result of {expression} is {result}"

    except Exception as e:
        return "I'm sorry, I couldn't calculate that. Please provide a valid expression."
    



def identify_color_code(color_name):
    try:
        color_name = color_name.lower()
        if color_name in CSS3_HEX_TO_NAMES:
            color_code = CSS3_HEX_TO_NAMES[color_name]
            return f"The color code for {color_name.capitalize()} is {color_code}."

        return f"Sorry, I couldn't identify a color code for {color_name.capitalize()}."

    except Exception as e:
        return "I'm sorry, I couldn't identify the color code at the moment."
    
