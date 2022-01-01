from Utils import Utils

import getpass

class SetUp:

    def __init__(self) -> None:
        self.utils = Utils() 
        self.main_menu()
    def main_menu(self):
        print("What would you like to do")
        print("Setup SSH and Wifi access on a PI SD CARD, 1")
        print("Open a GUI since this is hard, 2")
        print("Get IP addresses of PIs on your network, 3 \n")
        Number = int(input("Make a selection \n"))
        if Number == 1:
            self.setup_wifi()
        if Number == 2:
            self.open_gui() 
        if Number == 3: 
            self.list_pi_ips()
    def setup_wifi(self):
        #Number = int(input("Make a selection \n"))
        target_drive =     input("Target Drive \n") 
        config_path , right_dir = self.utils.set_drive(target_drive) 
        
        if  right_dir:          
          

            ssid = input("SSID \n")
            password = self.get_password()
            self.utils.write_files(ssid,password)
        self.restart() 

    def get_password(self):
        password = getpass.getpass("Password \n")
        password_confirm = getpass.getpass("Confirm Password \n")

        
        if password != password_confirm:
            print("Passwords do not match")
            return self.get_password()
        return password   
    def open_gui(self):
        self.restart()
    def list_pi_ips(self):
        print( self.utils.find_pi()) 
        self.restart()
        #pass
        
    def restart(self):
        print('Restart ?')
        Number = int(input("1 to restart, 2 to exit\n"))
        if Number == 1 :
            self.main_menu()

SetUp()