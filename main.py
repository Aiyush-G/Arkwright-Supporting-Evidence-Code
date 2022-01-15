from bottle import route, run, template, static_file, request, Jinja2Template
import requests
# from playsound import playsound Doesn't work on RPI instead using PyGame
from pygame import mixer
from random import randint
import pyttsx3
from time import sleep
from threading import Thread

global engine
engine = pyttsx3.init()

mixer.init()

# Variables
plant = "pear"
try:
    response = requests.get(("https://openfarm.cc/api/v1/crops/" + plant)) 
    name = response.json()["data"]["attributes"]["name"]
    binomial_name = response.json()["data"]["attributes"]["binomial_name"]
    description = response.json()["data"]["attributes"]["description"]
    short_description = str(description[ 0 : 250 ]) + "..."
    common_names = response.json()["data"]["attributes"]["common_names"]
    image = response.json()["included"][0]["attributes"]["image_url"]
    print (image)
except:
    print ("Hmm... it seems that the plant requested doesn't exist in the database")


pd = {
        "webTitle": "AG NEA",
        "pageTitle": "Aiyush G - NEA",
        "ff": plant,
        "shortDesc": short_description,
        "longDesc" : description,
        "temperature" : 27.5,
        "humidity" : 17,
        "LED": True,
        "speaker": False,
        "speakerVolume": 50,
        "image" : image,
}

greetingAudio = {
    "1":"audio/greeting/1.mp3",
    "2":"audio/greeting/2.mp3",
    "3":"audio/greeting/3.mp3",
    "4":"audio/greeting/4.mp3",
    "5":"audio/greeting/5.mp3",
    "6":"audio/greeting/6.mp3",
    "7":"audio/greeting/7.mp3",
    "8":"audio/greeting/8.mp3",
    "9":"audio/greeting/9.mp3",
    "10":"audio/greeting/10.mp3"
    
}

buttonAudio = {
    "1":"audio/buttonClick/1.mp3",
    "2":"audio/buttonClick/2.mp3",
    "3":"audio/buttonClick/3.mp3",
    "4":"audio/buttonClick/4.mp3"   
}


    
def connected(url='http://google.com'):
    timeout = 5
    try:
            request = requests.get(url, timeout=timeout)
            print("Connected to the Internet")
            return True
    except (requests.ConnectionError, requests.Timeout) as exception:
            print("No internet connection.")
            return False
    


def intro():
    engine.say("""I'm Plant Dude - your personal plant assistant - I've been dedicated a custom plant, and I'll tell you all about it and share some awesome facts!
                To learn more click the left red button. To access the web client where I've hidden some Easter Eggs then search for: plants.ooshimus.com""")
    engine.runAndWait()
    
def greeting():
    # playsound(greetingAudio[track]) DEPRECEATED
    
    
    track = greetingAudio[str(randint(1,10))]
    mixer.music.load(track)
    mixer.music.play()
    sleep(1)
    
def learn():
    engine.say("""Hi, using me is pretty simple. Use the switch on the side to turn me on or off.
               Use the buttons on the top to: 1. read these instruction again, 2. learn about the
               plant and surroundings, 3. Find about the termpature and humidity!""")
    engine.runAndWait()


def temperature(temp):

    warmWeatherGreeting = {
        "1":"Nice",
        "2":"Woah",
        "3":"Yay",
        "4":"Awesome"   
    }

    coldWeatherGreeting = {
        "1":"Oh no",
        "2":"Unfortunately",
        "3":"That is not summer weather",
        "4":"I wish it was warmer"   
    }

    warmSyn = {
        "1":"warm",
        "2":"hot",
        "3":"quite warm",
        "4":"boiling"   
    }

    coldSyn = {
        "1":"Nice",
        "2":"Woah",
        "3":"Yay",
        "4":"Awesome"   
    }

    warmWeatherGreetingAcc = warmWeatherGreeting[str(randint(1,4))]
    coldWeatherGreetingAcc = coldWeatherGreeting[str(randint(1,4))]
    warmSynAcc = warmSyn[str(randint(1,4))]
    coldSynAcc = coldSyn[str(randint(1,4))]

    
    if temp > 20:
        print(f"{warmWeatherGreetingAcc}, it is { temp } degrees celcius: that is {warmSynAcc}. Did you know that fruits such as Mangos, apple & pears can grow in this environment!")
        engine.say(f"{warmWeatherGreetingAcc}, it is { temp } degrees celcius: that is {warmSynAcc}. Did you know that fruits such as Mangos, apple & pears can grow in this environment!" )
    if temp < 20:
        print(f"{coldWeatherGreetingAcc}, it is { temp } degrees celcius: that is {coldSynAcc}. Did you know that plants such as Lavender, Chives and lettuce can grow at this temperature!")
        engine.say(f"{coldWeatherGreetingAcc}, it is { temp } degrees celcius: that is {coldSynAcc}. Did you know that plants such as Lavender, Chives and lettuce can grow at this temperature!" )

    engine.runAndWait()
    
def discoMode():
    # Easter Egg
    return

def buttonAcknowledgement():
    track = buttonAudio[str(randint(1,4))]
    mixer.music.load(track)
    mixer.music.play()
    sleep(1)

def getPlantInfo(plant):
    response = requests.get(("https://openfarm.cc/api/v1/crops/" + plant))
    
    name = response.json()["data"]["attributes"]["name"]
    binomial_name = response.json()["data"]["attributes"]["binomial_name"]
    description = response.json()["data"]["attributes"]["description"]
    common_names = response.json()["data"]["attributes"]["common_names"]


    intro = {
        "1" : "I'm going to tell you about the",
        "2" : "Well, this is what I found on the",
        "3" : "Well that is interesting! Here is what I found about the",
        "4" : "Awesome, I've always wanted to know more about the"
        }

    facts = {
        "1" : "I did a quick search and this is what I found about the",
        "2" : "Using an intelligent algorithm this is what I found about the",
        "3" : "Using my cool processor this is what I found about the",
        "4" : "Brilliant! This is what I found about thee"
        }

    introSeq = intro[(str(randint(1,4)))]
    factsSeq = facts[(str(randint(1,4)))]

    print(name)
    print(binomial_name)
    print(description)
    print(common_names)

    finalMessage=[]

    if name != None:
        message = f"""

        {introSeq} {name} species. 
        """
    
        finalMessage.append(message)
        #engine.say(message)
        #engine.runAndWait()
    else:
        #engine.say(f"Hmm.. I couldn't find anything about {plant}, try a different one!")
        #engine.runAndWait()

        message = f"Hmm.. I couldn't find anything about {plant}, try a different one!"
        finalMessage.append(message)
        
    if binomial_name != None:
        message = f"""
                    Or should I say {binomial_name} as it is binomially named.
                """

        finalMessage.append(message)
        #engine.say(message)
        #engine.runAndWait()
        
    if description != None:
        message = f"""
                    {factsSeq} {name}! {description}
                """

        finalMessage.append(message)
        #engine.say(message)
        #engine.runAndWait()
    else:
        message = f"Oh no! I couldn't find any cool facts on {plant}, maybe try a different one?"
        finalMessage.append(message)
        #engine.say(f"Oh no! I couldn't find any cool facts on {plant}, maybe try a different one?")
        #engine.runAndWait()

    finalMessage = " ".join(str(x) for x in finalMessage)
    engine.say(finalMessage)
    engine.runAndWait()
        
def discoMode():
    mixer.music.load("audio/easterEgg.mp3")
    mixer.music.play()
        
# WEB SERVER
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/')
def index():
    return template('index.tpl', pd)

@route('/', method="POST")
def index():

    # THIS MIGHT NEED TO BE REMOVED... THERE IS AN ERROR WHEN SOMEONE CLICKS MULTIPLE BUTTONS

    
            
    LED = request.forms.get('LED')
    speaker = request.forms.get('speaker')
    speakerVolume = request.forms.get('speakerVolume')
    
    howToUse = request.forms.get('howToUse')
    forcast = request.forms.get('forcast')
    restart = request.forms.get('restart')

    disco = request.forms.get('disco')
    
    print(howToUse, "how to use")
    print(forcast, "forcast")
    

    if True:
        # Change Speaker Volume

        if engine._inLoop:
            engine.endLoop()
    
        print ("Speaker Volume")
        pd["speakerVolume"] = speakerVolume
        print(pd["speakerVolume"])

        # Conversion is needed since max vol = 1, lowest = 0
        engine.setProperty('volume',(int(pd["speakerVolume"]) * 0.02))

    if LED == "Lighting":
        # Change LEDs
        print ("LED")
        pd["LED"] =  not pd["LED"]
        print (pd["LED"], type(pd["LED"]))
        return template('index.tpl', pd)

    elif restart == "Kill Engine":
        #os.execv(sys.executable, ['python'] + sys.argv)
        engine.stop()
        #engine = pyttsx3.init()

    elif disco == "Disco Mode":
        discoMode()
        
    elif forcast == "Local Forcast":
        print ("forcast clicked")
        temp = pd["temperature"]

        try:
            
            Thread(target=temperature, args=(temp, )).start()
        except:
            print ("Hmm... I cannot get the temperature")
        

    elif howToUse == "How to Use":
        try:
            Thread(target=learn).start()
        except:
            print ("Hmm I cannot tell you how to use me")
        
        
    elif speaker == "Speaker":
        # Speaker Starts
        print("Speaker")
        pd["speaker"] =  not pd["speaker"]
        print (pd["speaker"], type(pd["speaker"]))

        try:
            # Speak about the plant
            #getPlantInfo((pd["ff"]))
            plantInfo = pd["ff"]
            Thread(target=getPlantInfo, args=(plantInfo, )).start()
        except:
            print("Hmmm... I couldn't tell you about the plant!")
        
        return template('index.tpl', pd)
    

    return template('index.tpl', pd)

# buttonAcknowledgement()

# On Plant Info Button Clicked
#getPlantInfo("mango")
#greeting()
#intro()


def startWebserver():
    if connected():
        run(host='0.0.0.0', port=8080, debug=True)
    else:
        print ("AI Speech To Text and Audio is not currently available - please connect to the internet")
        engine.say("You are currently not connected to the internet - you're missing out on some awesome features. For example, real-time weather location, flora and fauna information, weather forcasting and much more.")
        engine.runAndWait()

def GPIO():
    # Check for Button Clicks Here
    # 1. Instructions - learn()
    # 2. Plants
    # 3. Temperature & Humidity
    #### TESTING ####
    return

if __name__ == '__main__':
    #greeting()
    #intro()
    Thread(target = startWebserver).start()
    Thread(target = GPIO).start()
    



