import os
import pyautogui
import time
import psutil
import pygetwindow as gw
from pywinauto import Application

from assistant import speak
from take_command import takeCommand
# CLIENT_ID = "5adee7c8c47249e8b0b8f0ae131c6b1d"
# CLIENT_SECRET = "1b0cf9d7ecc245c9a5f55ab511f8edc8"
def press_key_combination(*keys):
    for key in keys:
        pyautogui.keyDown(key)
    for key in reversed(keys):
        pyautogui.keyUp(key)

def is_process_running(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def turn_on_spotify():
    pyautogui.press('win')
    time.sleep(0.5)
    pyautogui.write('Spotify')
    time.sleep(0.5)
    pyautogui.press('enter')

    program_name = 'Spotify.exe'


    timeout = time.time() +30 #30 sec timeout
    while True:
        #check if spotify is open
        if is_process_running(program_name):
            speak('Spotify opened!')
        else:
            speak('Cant open Spotify')
            # else:
            #     #wait not more 30 sec
            #     time.sleep(1)
            #     continue
        break
    time.sleep(2)
    pyautogui.press('space')

def find_artist_and_listen():
    os.system('start Spotify')
    while True:
        speak('Say the name of the artist you wanna listen')
        artist = takeCommand()
        speak(f'Do you wanna listen {artist}?')
        answer_first = takeCommand().lower()
        if 'yes' in answer_first:
            press_key_combination('ctrl','k')
            time.sleep(0.1)
            pyautogui.write(f'{artist}')
            time.sleep(0.1)
            pyautogui.press('Enter')
            time.sleep(0.3)
            press_key_combination('Shift','Enter')
            time.sleep(0.3)
            speak(f'Enjoy listening {artist}')
            
            
            break
        else:
            continue
find_artist_and_listen()

