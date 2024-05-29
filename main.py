import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime

import wikipedia
import webbrowser
import os
import winshell
from git_commit import git_commit
from word2number import w2n
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import subprocess
# import torch
# from tts.TTS.api import TTS

from assistant import speak, username, wishMe
from send_email import sendEmail
from take_command import takeCommand
from wifi import connect_to_wifi, show_all_network
from spotify import find_artist_and_listen, turn_on_spotify
# from wifi_functions import show_all_network


if __name__ == '__main__':
    clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    username()
     
    while True:
        query = takeCommand().lower()
         
        # All the commands said by user will be 
        # stored here in 'query' and will be
        # converted to lower case for easily 
        # recognition of command
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")   
 
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")    
            speak(f"Sir, the time is {strTime}")
 
        # elif 'open opera' in query:
        #     codePath = r"C:\\Users\\GAURAV\\AppData\\Local\\Programs\\Opera\\launcher.exe"
        #     os.startfile(codePath)
 
        # elif 'email to gaurav' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "Receiver email address"   
        #         sendEmail(to, content)
        #         speak("Email has been sent !")
        #     except Exception as e:
        #         print(e)
        #         speak("I am not able to send this email")
 
        # elif 'send a mail' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         speak("whome should i send")
        #         to = input()    
        #         sendEmail(to, content)
        #         speak("Email has been sent !")
        #     except Exception as e:
        #         print(e)
        #         speak("I am not able to send this email")

 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'goodbye' in query or 'bye bye' in query or 'stop' in query or 'exit' in query or 'quit' in query:
            speak("Thanks for giving me your time")
            exit()
      
        elif 'joke' in query:
            speak(pyjokes.get_joke())
             
        elif "calculate" in query: 
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text
            print("The answer is " + answer) 
            speak("The answer is " + answer) 
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query) 
 
        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20, 
                                                       0, 
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")
 
        # elif 'news' in query:
             
        #     try: 
        #         jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
        #         data = json.load(jsonObj)
        #         i = 1
                 
        #         speak('here are some top news from the times of india')
        #         print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
        #         for item in data['articles']:
                     
        #             print(str(i) + '. ' + item['title'] + '\n')
        #             print(item['description'] + '\n')
        #             speak(str(i) + '. ' + item['title'] + '\n')
        #             i += 1
        #     except Exception as e:
                 
        #         print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
 
        # elif "stop listening" or 'stop' in query:
        #     speak("for how much time you want to stop jarvis from listening commands")
        #     a = int(takeCommand())
        #     time.sleep(a)
        #     print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r") 
            print(file.read())
            speak(file.read(6))
 
        # elif "update assistant" in query:
        #     speak("After downloading file please replace this file with the downloaded one")
        #     url = '# url after uploading file'
        #     r = requests.get(url, stream = True)
             
        #     with open("Voice.py", "wb") as Pypdf:
                 
        #         total_length = int(r.headers.get('content-length'))
                 
        #         for ch in progress.bar(r.iter_content(chunk_size = 2391975),
        #                                expected_size =(total_length / 1024) + 1):
        #             if ch:
        #               Pypdf.write(ch)
                     
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
 
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather 
            api_key = "42ac2b529b3491c8fa9353c7e11b97d3"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url) 
            x = response.json() 
             
            if x["code"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            else: 
                speak(" City Not Found ")
             
        # elif "send message " in query:
        #         # You need to create an account on Twilio to use this service
        #         account_sid = 'Account Sid key'
        #         auth_token = 'Auth token'
        #         client = Client(account_sid, auth_token)
 
        #         message = client.messages \
        #                         .create(
        #                             body = takeCommand(),
        #                             from_='Sender No',
        #                             to ='Receiver No'
        #                         )
 
        #         print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant
 
        elif "what is" in query or "who is" in query:
             
            # Use the same API key 
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")

        elif 'show' and 'network' in query:
            speak("Here are all available local networks")
            wifi_list = show_all_network()
            for el in wifi_list:
                print(el)
        elif 'connect to the network' or 'connect to the wifi' in query:
            speak("Here are all available local networks")
            wifi_list = show_all_network()
            wifi_list_correct = [el for el in wifi_list if el != ':']
            for el in wifi_list_correct:
                print(el)
            speak('Say the number of the network that you want to connect')
            net_num = takeCommand()
            print('You said: ', net_num)
            
            int_net_num = w2n.word_to_num(net_num)
            net_ssid = wifi_list[int_net_num-1][2]
            print(net_ssid)
            try:
                speak('Enter password of this network: ')
                password = input(f'Password of {net_ssid}: ')
                speak('Trying to connect to the wifi...')
                if connect_to_wifi(net_ssid,password):
                    speak('Successfully connected to the wifi')
                else:
                    speak('Unsuccessul')
            except:
                pass

        elif 'open Spotify' in query or 'play music'in query or "play song" in query:
            speak('Trying to open Spotify')
            find_artist_and_listen()
            
        elif 'git' in query:
            speak('Trying to commit changes to git')
            folder_path = './'
            commit_message = 'feat: add new feature'
            git_commit(folder_path, commit_message)
        else:
            speak('I do not understand you, can you repeat, please?')