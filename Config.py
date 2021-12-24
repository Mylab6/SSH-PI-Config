import tkinter as tk


import tkinter.filedialog


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
def select_drive():
    found_drive = tk.filedialog.askdirectory()
    print(found_drive)
    drive_label.config(text=found_drive)

#tk.Label(text= "Select your PIs boot drive").pack() 
select_drive_bttn= tk.Button(master=window, command=select_drive,  text="Select PI Boot Drive")
select_drive_bttn.pack()
window.mainloop()

