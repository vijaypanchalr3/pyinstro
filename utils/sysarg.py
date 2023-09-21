from pyinstro.utils import defaults




import argparse




class CLI:
    """
    this is CLI argument and default setup for script
    """
    def __init__(self) -> None:
        self.defaults = defaults.DefaultParams()
        self.argparser = argparse.ArgumentParser(
            prog='INSTRUMENT CONTROLLER',
            description='This program is controller for instument in the lab with SCPI support',
            epilog=' for more help visit https://github.com/vijaypanchalr3 \n for more help on SR830 check manual of SR830')
        self.arguments()
        self.args = self.argparser.parse_args()
        
        
    def arguments(self) ->None:
        self.argparser.add_argument('-f','--file', metavar='*.csv', type=str, default="default", help="give an file to write data")
        self.argparser.add_argument('-pa','--partitions', metavar='',type=int, default=self.defaults.partitions, help="give partition for frequency division")
        self.argparser.add_argument('-le','--level', metavar='', type=int, default=self.defaults.levels, help="similar to levels it take increases partitions and resolution")
        self.argparser.add_argument('-tc', '--timeconst', metavar='', type=int, choices=range(1,20), default=self.defaults.time_constant, help="choose time constant from manual from following choises:  "+" ".join([str(x) for x in range(1,21)]))
        self.argparser.add_argument('-td', '--timedelay', metavar='', type=float, default=self.defaults.time_delay, help="choose time delay from manual from following choises  ")
        self.argparser.add_argument('-se', '--sensitivity', metavar='', type=int, choices=range(1,27), default=self.defaults.sensitivity, help="choose sensitivity from following choises:  "+" ".join([str(x) for x in range(1,28)]))
        self.argparser.add_argument('-sr', '--samplerate', metavar='', type=int, choices=range(1,15), default=self.defaults.sample_rate, help="sample rate for output sampling from following choises:  "+" ".join([str(x) for x in range(1,16)]))
        self.argparser.add_argument('-dt', '--data', metavar='', type=int,choices=range(1,5),default=self.defaults.data, help="give default data variable from following choises:  "+" ".join([str(x) for x in range(1,6)]))
        self.argparser.add_argument('-bd', '--baud', metavar='', type=int, default=self.defaults.baud_rate, help="set baud rate for connection defaults to 9600")
        self.argparser.add_argument('-c', '--connection', metavar='', type=str, choices=range(1,5), default=self.defaults.connection, help="1: GPIB, 2: RS232, 3: USB, 4: LAN")


    def get_file(self) -> str:
        return self.args.file   

    
    def get_partitions(self)->int:
        return self.args.partitions
    
    def get_levels(self) -> int:
        return self.args.levels
    
    def get_connection(self)->str:
        return defaults.DefaultParams.connections[self.args.connection]

    def get_gpib(self)->int:
        return self.args.gpib
    
    def get_sample_rate(self)->int:
        return self.args.samplerate
    
    def get_time_constant(self)->int:
        return self.args.timeconst
    
    def get_data_var(self)-> int:
        return self.args.data
        
    def get_freq(self)->float:
        return self.args.get_freq
    
