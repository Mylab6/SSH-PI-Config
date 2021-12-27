from Utils import Utils


class SetUp:

    def __init__(self) -> None:
        self.utils = Utils() 
        self.main_menu()
    def main_menu(self):
        print("What would you like to do")
        print("Setup SSH and Wifi access on a PI SD CARD, 1")
        print("Open a GUI since this is hard, 2")
        print("Get IP addresses of PIs on your network, 3")
        Number = int(input("Make a selection"))
        if Number == 1:
            self.setup_wifi()
        if Number == 2:
            self.open_gui() 
        if Number == 3: 
            self.list_pi_ips()
    def setup_wifi(self):
        self.restart()
    def open_gui(self):
        self.restart()
    def list_pi_ips(self):
        print( self.utils.find_pi()) 
        self.restart()
        #pass
        
    def restart(self):
        print('Restart ?')
        Number = int(input("1 to restart, 2 to exit"))
        if Number == 1 :
            self.main_menu()

SetUp()