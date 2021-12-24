import tkinter as tk


import subprocess

import shutil
import  os 
import tkinter.filedialog
from tkinter import *

class Utils:
    pi_mac_address_ranges = ['B8-27-EB','DC-A6-32','E4-5F-01']

    def replace_text_in_file(self,file_path, old_text,new_text):
        with open(file_path) as f:
            s = f.read()
        s = s.replace(old_text, new_text)
        with open(file_path, "w") as f:
            f.write(s)
    def copy_file(self,local_file_location):    
        almost_file = os.path.join( local_file_location)
        file_to_cp = self.get_local_file_path(almost_file) 
        new_file_path = os.path.join(self.found_drive,local_file_location) 
        shutil.copy( file_to_cp, new_file_path)
        return new_file_path 

    def get_local_file_path(sub_path):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(dir_path,sub_path)
    def select_drive(self):
    
        self.found_drive = tk.filedialog.askdirectory()
        print('Using ' +  self.found_drive)
        #return found_drive
   

    def write_files(self,ssid,password):
        self.copy_file('ssh')
        wpa_file_path = self.copy_file('wpa_supplicant.conf')
        self.replace_text_in_file(wpa_file_path,'your_network_name',ssid)
        self.replace_text_in_file(wpa_file_path,'your_wifi_password',password)

    def find_pi(self):
        all_lines = subprocess.check_output('arp -a', universal_newlines=True).split('\n')
        arr =[] 
        for device in all_lines:
        #print(device)
        #print('1')
            for possibleMac in self.pi_mac_address_ranges:
                if possibleMac.lower() in device.lower():
                    arr.append(device)
        #if 'dc:a6:32'.lower() in device.lower():
         #   arr.append(device)
        print(arr)

        return arr