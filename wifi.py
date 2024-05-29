#Showing and Connection to WIFI

from word2number import w2n
from take_command import takeCommand
import wifi
import os
import re
import subprocess
from assistant import speak

# Проверяем, соответствует ли строка шаблону "число:двоеточие"
def contains_pattern(el):
    pattern = r'^[0-9]+:'
    if re.match(pattern, el):
        return True
    return False

def show_all_network():
    devices = subprocess.check_output(['netsh', 'wlan', 'show', 'network'])
    devices = devices.decode('ascii', errors='ignore')

    devices = devices.replace('\r',"")
    elements = devices.split()
    ssids = []
    iterator = iter(elements)

    for el in iterator:
        ssids_info = []
        if el == 'SSID':
            ssid = el
            ssid_num = next(iterator)
            ssid_name = next(iterator)
            ssids_info.append(ssid)
            ssids_info.append(ssid_num)
            ssids_info.append(ssid_name)
            
        ssids.append(ssids_info)
    result = [ele for ele in ssids if ele!=[]]
    # print(result)
    return result

def connect_to_wifi(ssid, password):
    command = f'netsh wlan connect name={ssid}'
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate(input=password.encode())
    if stderr:
        # print("Error:", stderr.decode())
        return False
    else:
        # print("Connected to", ssid)
        return True

def disconnect_form_wifi():
    command = f'netsh wlan disconnect'
    os.system(command)
    speak('Disconnected from your Wifi')
    
speak("Here are all available local networks")
show_all_network()
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
