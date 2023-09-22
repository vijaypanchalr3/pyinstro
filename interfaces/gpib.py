# GPIB interface



import pyvisa
import sys
from termcolor import cprint




class GPIB:
    def __init__(self) -> None:                                 
        try:                        # GPIB connection check
            cprint("-----------checking GPIB connections--------",color="yellow")
            resources = pyvisa.ResourceManager()
            interface = None
            resourceslist = resources.list_resources()
            cprint(resourceslist,'blue',attrs=['bold'])
            if resourceslist==():
                cprint("ERROR: please check GPIB connection", "red")
                sys.exit()
            else:
                while True:
                    try:
                        choise = int(input("please, choose your device from this list: "))-1
                        if choise>len(resourceslist):
                            TypeError
                        interface = resourceslist[choise]
                        cprint("-------------chose resource-----------------",color="green",attrs=["bold"])
                        cprint("-------following device is connected--------",color="green",attrs=["bold"])
                        cprint(interface)
                        break
                    except:
                        cprint("choose with interger and from following...","red")

            self.interface =  resources.open_resource(interface)
        except:
            cprint("ERROR in detecting GPIB, there must be problem with setup of pyvisa or there is no connection of gpib\n you should look either in pyvisa documentation or try for RS232 interface","red",attrs=['bold'])
            sys.exit()

    def ping(self)-> None:
        self.interface.write("*IDN?\n")

    def read(self)-> None:
        self.interface.read()

    def reset(self)-> None:
        self.interface.write("*RST\n")

    def clear_status(self)-> None:
        self.interface.write("*CLS\n")

    def close(self)->None:
        self.interface.close()

    def std_event(self)->None:
        pass

