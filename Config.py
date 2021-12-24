import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

window = tk.Tk()

frame_wifi = tk.Frame()

ssid_label = tk.Label(text="Wifi SSID",master=frame_wifi)
ssid_entry = tk.Entry(master=frame_wifi)
password_label = tk.Label(text="Wifi Password", master=frame_wifi )
password_entry = tk.Entry(master=frame_wifi)

ssid_label.pack()
ssid_entry.pack() 
password_label.pack()
password_entry.pack()
frame_wifi.pack()

tk.Label(text= "Select your PIs boot drive").pack() 


window.mainloop()