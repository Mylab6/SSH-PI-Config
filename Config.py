import tkinter as tk


import subprocess

import shutil
import  os 
import tkinter.filedialog
from tkinter import *
pi_mac_address_ranges = ['B8-27-EB','DC-A6-32','E4-5F-01']
window = tk.Tk()
frame_wifi = tk.Frame(master=window, width=400, height=400,)
ssid_label = tk.Label(text="Wifi SSID",master=frame_wifi)
ssid_entry = tk.Entry(master=frame_wifi)
password_label = tk.Label(text="Wifi Password", master=frame_wifi )
password_entry = tk.Entry(master=frame_wifi)
ssid_label.pack()
ssid_entry.pack() 
password_label.pack()
password_entry.pack()
frame_wifi.pack()


drive_label = tk.Label(text="Drive....")
drive_label.pack() 

def replace_text_in_file(file_path, old_text,new_text):
        with open(file_path) as f:
            s = f.read()
        s = s.replace(old_text, new_text)
        with open(file_path, "w") as f:
            f.write(s)
def copy_file(local_file_location):    
    almost_file = os.path.join( local_file_location)
    file_to_cp = get_local_file_path(almost_file) 
    new_file_path = os.path.join(found_drive,local_file_location) 
    shutil.copy( file_to_cp, new_file_path)
    return new_file_path 

def get_local_file_path(sub_path):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path,sub_path)
def select_drive():
    global found_drive
    found_drive = tk.filedialog.askdirectory()
    print(found_drive)
    drive_label.config(text=found_drive)
    write_files_bttn['state'] = 'normal'

def write_files():
    copy_file('ssh')
    wpa_file_path = copy_file('wpa_supplicant.conf')
    replace_text_in_file(wpa_file_path,'your_network_name',ssid_entry.get())
    replace_text_in_file(wpa_file_path,'your_wifi_password',password_entry.get())

def find_pi():
    all_lines = subprocess.check_output('arp -a', universal_newlines=True).split('\n')
    arr =[] 
    for device in all_lines:
        #print(device)
        #print('1')
        for possibleMac in pi_mac_address_ranges:
            if possibleMac.lower() in device.lower():
                arr.append(device)
        #if 'dc:a6:32'.lower() in device.lower():
         #   arr.append(device)
    print(arr)
    Lb1.delete(0,'end')
    Lb1.insert(0,arr)
        
    #print(all_lines)
#tk.Label(text= "Select your PIs boot drive").pack() 
select_drive_bttn= tk.Button(master=window,   command=select_drive,  text="Select PI Boot Drive")
select_drive_bttn.pack()
global write_files_bttn
write_files_bttn= tk.Button(master=window, command=write_files,  text="Write Files")
write_files_bttn['state'] = 'disabled'

write_files_bttn.pack()

find_pi_bttn= tk.Button(master=window, command=find_pi,  text="Find PIs")

find_pi_bttn.pack()
global Lb1
Lb1 = Listbox(window, width=150)
Lb1.pack()

window.mainloop()



