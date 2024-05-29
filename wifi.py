#Showing and Connection to WIFI


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
    

# print(result)
# print(elements)
# print(show_all_network()[2])

# connect_to_wifi('CMCC-A272','Bastau2008')

# disconnect_form_wifi()
show_all_network()