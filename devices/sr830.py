from pyinstro.utils import sysarg
from pyinstro.utils import datafile

### TASK -make local defaults for instruments-
# from pyinstro.utils import defaults

### TASK -make local cli arguments-


new_instance = sysarg.CLI()

if new_instance.get_connection()=="GPIB":
    from pyinstro.interfaces import gpib
    
    class SR830(gpib.GPIB):
        def __init__(self) -> None:
            super().__init__()

            file_init = datafile.Get_File(new_instance.get_file())
            
            self.get_levels = new_instance.get_levels
            self.get_partitions = new_instance.get_partitions
            self.writerow = file_init.writerow
            self.longwriterow = file_init.longwriterow
            self.fmin = new_instance.get_fmin
            self.fmax = new_instance.get_fmax
            self.freq = new_instance.get_freq

        def local_defaults(self)-> None:
            pass

        def local_arguments(self)-> None:
            new_instance.argparser.add_argument('-fl','--fmin', metavar='', type=float, default=4545, help="give lower limit for reference frequency")
            new_instance.argparser.add_argument('-fr','--freq', metavar='', type=float, default=7888, help="give reference frequency")
            new_instance.argparser.add_argument('-fh','--fmax', metavar='', type=float, default=1, help="give upper limit for reference frequency")
    
        def set_frequency(self, value, errdelay = 3) -> None:
            """change reference frequency"""
            self.interface.write("FREQ "+"{:.4E}".format(value))
            pass

        def autogain(self)->None:
            self.interface.write("AGAN")

        def set_phase(self,value) -> None:
            self.interface.write("PHAS "+str(value))
            pass

        def time_constant(self,choise) -> None:
            self.interface.write("OFLT "+str(choise))
            pass

        def sensitivity(self,choise) -> None:
            self.interface.write("SENS "+str(choise))
            pass

        def set_sample_rate(self, choise)->None:
            self.interface.write("SRAT "+str(choise))

        def start_data_acquision(self) -> None:
            self.interface.write("STRT")
            pass

        def pause_data_acquision(self) -> None:
            self.interface.write("PAUS")
            pass

        def reset_data_acquision(self) -> None:
            self.interface.write("REST")
            pass

        def get_data(self) -> None:
            pass

        def get_data_explicitly(self, data_variable=3, errdelay=3):
            """
            two params, give resource object and the second params is parameter to variable read,
            default to data_variable = 3 which is equievalent to reading R.
            as SR830manual, 
            data_variable = 1 => X,
            data_variable = 2 => Y,
            data_variable = 3 => R,
            data_variable = 4 => phase
            """
            return self.interface.query("OUTP? "+str(data_variable))

        
else:

    from pyinstro.interfaces import rs232
    
    class SR830(rs232.RS232):
        """
        
        """
        
        def __init__(self) -> None:
            super().__init__()
            file_init = datafile.Get_File(new_instance.get_file())
            
            self.get_levels = new_instance.get_levels
            self.get_partitions = new_instance.get_partitions
            self.writerow = file_init.writerow
            self.longwriterow = file_init.longwriterow
            self.fmin = new_instance.get_fmin
            self.fmax = new_instance.get_fmax
            self.freq = new_instance.get_freq
            pass

        def local_defaults(self)-> None:
            pass

        def local_arguments(self)-> None:
            new_instance.argparser.add_argument('-fl','--fmin', metavar='', type=float, default=4545, help="give lower limit for reference frequency")
            new_instance.argparser.add_argument('-fr','--freq', metavar='', type=float, default=1000, help="give reference frequency")
            new_instance.argparser.add_argument('-fh','--fmax', metavar='', type=float, default=1, help="give upper limit for reference frequency")

        def get_fmin(self) -> float:
            return new_instance.args.fmin
    
        def get_fmax(self) -> float:
            return new_instance.args.fmax
        
        def set_frequency(self, value, errdelay = 3) -> None:
            pass

        def autogain(self):
            pass

        def set_phase(self,value) -> None:
            pass

        def time_constant(self,choise) -> None:
            pass

        def sensitivity(self,choise) -> None:
            pass

        def set_sample_rate(self, choise)->None:
            pass

        def start_data_acquision(self) -> None:
            pass

        def pause_data_acquision(self) -> None:
            pass

        def reset_data_acquision(self) -> None:
            pass

        def get_data(self) -> None:
            pass

        def get_data_explicitly(self, data_variable=3, errdelay=3):
            """
            two params, give resource object and the second params is parameter to variable read,
            default to data_variable = 3 which is equievalent to reading R.
            as SR830manual, 
            data_variable = 1 => X,
            data_variable = 2 => Y,
            data_variable = 3 => R,
            data_variable = 4 => phase
            """
            return 0