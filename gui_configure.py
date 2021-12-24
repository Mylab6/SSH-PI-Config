import tkinter as tk


import subprocess

import shutil
import  os 
import tkinter.filedialog
from tkinter import *

from Utils import find_pi, select_drive, write_files

class GUIConfig:
    entries = {}
    def init(self):      
        self.window = tk.Tk()
        self.frame_wifi = tk.Frame(master=self.window, width=400, height=400,)
        ssid_label = tk.Label(text="Wifi_SSID",master=self.frame_wifi)
        ssid_entry = tk.Entry(master=self.frame_wifi)
        password_label = tk.Label(text="Wifi_Password", master=self.frame_wifi )
        password_entry = tk.Entry(master=self.frame_wifi)
        ssid_label.pack()
        ssid_entry.pack() 
        password_label.pack()
        password_entry.pack()
        self.frame_wifi.pack()
        drive_label = tk.Label(text="Drive....")
        drive_label.pack()
        select_drive_bttn= tk.Button(master=self.window,   command=select_drive,  text="Select PI Boot Drive")
        select_drive_bttn.pack()
        write_files_bttn= tk.Button(master=self.window, command=write_files,  text="Write Files")
        write_files_bttn['state'] = 'disabled'
        write_files_bttn.pack()
        find_pi_bttn= tk.Button(master=self.window, command=find_pi,  text="Find PIs")
        find_pi_bttn.pack()        #global Lb1
        Lb1 = Listbox(self.window, width=150)
        Lb1.pack()
        self.window.mainloop()
    def AddLabelEntryCombo(self, desc):
            label = tk.Label(text=desc,master=self.frame_wifi)
            self.entries[desc] = tk.Entry(master=self.frame_wifi)
            label.pack()
            self.entries[desc].pack()


