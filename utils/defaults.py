from pyinstro.utils import getpath



import os
import configparser


class DefaultParams:
    """
    specify default parameters
    
    for more info:
    refer to SR830 manual for more info.
    """


    time_constant = 5
    sensitivity = 5
    # filter_slope = 

    baud_rate = 9600
    sample_rate = 10
    gpib_address = 1
    time_delay = 1

    connection = 1          # means GPIB, 1: GPIB, 2: RS232, 3: USB, 4: LAN
    connections = {1:"GPIB", 2:"RS232", 3:"USB", 4:"LAN"}

    fmin = 01E+3
    fmax = 01E+5
    
    partitions = 4
    levels = 4

    data= 3

    def __init__(self) -> None:
        self.defaults_params_list= [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        #defaults_params= dict(zip(defaults_params_list,list(" "*len(defaults_params_list))))
        
        self.target_path = getpath.getpath()
        config_file = os.path.join(self.target_path,"config.ini")

        print("checking config.ini file")
        
        if os.path.exists(config_file):
            config = configparser.ConfigParser()
            config.read(config_file)
            config_file_dict = config.defaults()
            if len(config_file_dict)==len(self.defaults_params_list):
                for keys in config_file_dict:
                    if (config_file_dict[keys].isspace() or not config_file_dict[keys]):
                        pass
                    else:
                        setattr(self, keys, config_file_dict[keys])
                        print(keys+":  "+config_file_dict[keys])
            else:
                for keys in self.defaults_params_list:
                    if not (keys in config_file_dict):
                        with open(config_file, "w") as _conf_file: 
                            config.set("DEFAULT",keys," ")
                            config.write(_conf_file) 
                    else:
                        if (config_file_dict[keys].isspace() or config_file_dict[keys] ==""):
                            pass
                        else:
                            setattr(self, keys, config_file_dict[keys])
                            print(keys+":  "+config_file_dict[keys])
                            
        else:
            pass

    def makeconfig(self):
        config_file =os.path.join(self.target_path,"config.ini")
        config = configparser.ConfigParser()
        if os.path.exists(config_file):
            config.read(config_file)
            config_file_dict = config.defaults()
            if len(config_file_dict)==len(self.defaults_params_list):
                pass
            else:
                for keys in self.defaults_params_list:
                    if not (keys in config_file_dict):
                        with open(config_file, "w") as _conf_file: 
                            config.set("DEFAULT",keys," ")
                            config.write(_conf_file)
                            
                    else:
                        pass
                print("I had appened to full option to config file!")
        else:
            with open(config_file,'w') as config_file:
                config_file.write("[DEFAULT]\n")
                for params in self.defaults_params_list:
                    config_file.write(params+" = \n")
            print("I had made config file in present directory !")
