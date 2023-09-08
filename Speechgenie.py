import pyttsx3
import datetime
import speech_recognition as am 
import webbrowser
import os
import sys
# import wikipedia
# import smtplib
# from weather_test import current_weather, current_temp
# from pas import p,g

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say ( audio )
    engine.runAndWait ()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour>= 0 and hour< 12):
        speak('Good morning')

    elif(hour >= 12 and hour < 18):
        speak('Good after noon')

    else:
        speak('Good evening')

    speak('How can i help you sir?')


def takecommand():
    # it takes input

    a = am.Recognizer ()
    with am.Microphone () as source:
        print ( 'Listening ...' )
        a.pause_threshold = 1
        a.energy_threshold = 2000
        audio = a.listen ( source )

    try:
        print ( 'Recognising ...' )
        query = a.recognize_google ( audio, language="en-in" )
        print ( f"user said: {query}\n" )

    except Exception:
        print ( "Can You Please Say That again?" )
        speak ( "Can You Please! Say That again?" )
        return "None"
    return query


def goodbye():
    hour = int ( datetime.datetime.now ().hour )
    if hour >= 0 and hour <= 19:
        speak ( 'See you later . Have a good day' )
    else:
        speak ( 'See you later . Good night' )

# def sendEmail(to, content):
#     gmail = g
#     server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#     server.login(gmail, p)
#     server.sendmail(gmail, to, content)
#     server.quit()

if __name__ == "__main__":
	
        wishme ()
    
        while True:
            query = takecommand().lower()

            if "search" in query:
                speak ( "searching..." )
                # print ( "searching..." )
                # query = query.replace ( 'wikipedia', '' )
                # result = wikipedia.summary ( query, sentences=3 )
                # print ( result )
                # speak ( f"According to wikipedia {result}" )
                        

            elif 'open youtube' in query:
                speak("Just want to open youtube or search in youtube")
                cn = takecommand().lower()
                if(cn=="just open youtube"):
                    webbrowser.open("https://www.youtube.com" )
                elif(cn=="search in youtube"or cn=="search youtube"):
                    speak("what should i search:")
                    m = takecommand().lower()
                    webbrowser.open (f"https://www.youtube.com/results?search_query={m}" )

            elif 'open google' in query:
                speak("what should i search:")
                cm = takecommand().lower()
                webbrowser.open (f"{cm}" )

            elif 'open video' in query:
                video_dir = 'D:\\VIDEOS'
                video = os.listdir ( video_dir )
                os.startfile ( video_dir )

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}") 
  

            # elif 'email' in query:
            #     try:
            #         speak("what should i write?")
            #         content = takecommand()
            #         speak("To whom should i send?")
            #         to = takecommand().replace(' ','')+'@gmail.com'
            #         sendEmail(to,content)
            #         speak("Email has been sent!")

            #     except Exception as e:
            #         print(e)
            #         speak("Sorry the email was not send")


            # elif 'weather' in query:
            #     try:
            #         speak("Tell the location")
            #         city = takecommand()
            #         weather = current_weather(city)
            #         speak(f'Current weather is {weather}')
            #         print(weather)

            #     except Exception as a:
            #         print(a)
            #         speak('failed to search')

            # elif 'temp' in query:
            #     try:
            #         speak("Tell the location")
            #         city = takecommand()
            #         temp = current_temp(city)
            #         speak(f'Current temperature is {temp}')
            #         print(temp)

            #     except Exception as b:
            #         print(b)
            #         speak('failed to search')



            elif "close" or "exit" in query:
                speak("Quitting")
                goodbye ()
                exit (0)
import pyttsx3
import datetime
import speech_recognition as am 
import webbrowser
import os
import sys
# import wikipedia
# import smtplib
# from weather_test import current_weather, current_temp
# from pas import p,g

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 145
engine.setProperty('rate',newVoiceRate)

def speak(audio):
    engine.say ( audio )
    engine.runAndWait ()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour>= 0 and hour< 12):
        speak('Good morning')

    elif(hour >= 12 and hour < 18):
        speak('Good after noon')

    else:
        speak('Good evening')

    speak('How can i help you sir?')


def takecommand():
    # it takes input

    a = am.Recognizer ()
    with am.Microphone () as source:
        print ( 'Listening ...' )
        a.pause_threshold = 1
        a.energy_threshold = 2000
        audio = a.listen ( source )

    try:
        print ( 'Recognising ...' )
        query = a.recognize_google ( audio, language="en-in" )
        print ( f"user said: {query}\n" )

    except Exception:
        print ( "Can You Please Say That again?" )
        speak ( "Can You Please! Say That again?" )
        return "None"
    return query


def goodbye():
    hour = int ( datetime.datetime.now ().hour )
    if hour >= 0 and hour <= 19:
        speak ( 'See you later . Have a good day' )
    else:
        speak ( 'See you later . Good night' )

# def sendEmail(to, content):
#     gmail = g
#     server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#     server.login(gmail, p)
#     server.sendmail(gmail, to, content)
#     server.quit()

if __name__ == "__main__":
	
        wishme ()
    
        while True:
            query = takecommand().lower()

            if "search" in query:
                speak ( "searching..." )
                # print ( "searching..." )
                # query = query.replace ( 'wikipedia', '' )
                # result = wikipedia.summary ( query, sentences=3 )
                # print ( result )
                # speak ( f"According to wikipedia {result}" )
                        

            elif 'open youtube' in query:
                speak("Just want to open youtube or search in youtube")
                cn = takecommand().lower()
                if(cn=="just open youtube"):
                    webbrowser.open("https://www.youtube.com" )
                elif(cn=="search in youtube"or cn=="search youtube"):
                    speak("what should i search:")
                    m = takecommand().lower()
                    webbrowser.open (f"https://www.youtube.com/results?search_query={m}" )

            elif 'open google' in query:
                speak("what should i search:")
                cm = takecommand().lower()
                webbrowser.open (f"{cm}" )

            elif 'open video' in query:
                video_dir = 'D:\\VIDEOS'
                video = os.listdir ( video_dir )
                os.startfile ( video_dir )

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}") 
  

            # elif 'email' in query:
            #     try:
            #         speak("what should i write?")
            #         content = takecommand()
            #         speak("To whom should i send?")
            #         to = takecommand().replace(' ','')+'@gmail.com'
            #         sendEmail(to,content)
            #         speak("Email has been sent!")

            #     except Exception as e:
            #         print(e)
            #         speak("Sorry the email was not send")


            # elif 'weather' in query:
            #     try:
            #         speak("Tell the location")
            #         city = takecommand()
            #         weather = current_weather(city)
            #         speak(f'Current weather is {weather}')
            #         print(weather)

            #     except Exception as a:
            #         print(a)
            #         speak('failed to search')

            # elif 'temp' in query:
            #     try:
            #         speak("Tell the location")
            #         city = takecommand()
            #         temp = current_temp(city)
            #         speak(f'Current temperature is {temp}')
            #         print(temp)

            #     except Exception as b:
            #         print(b)
            #         speak('failed to search')



            elif "close" or "exit" in query:
                speak("Quitting")
                goodbye ()
                exit (0)
