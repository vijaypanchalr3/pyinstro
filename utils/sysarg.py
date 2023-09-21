from pyinstro.utils import defaults




import argparse


_defaults = defaults.DefaultParams()

class makeconfig(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)
    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        _defaults.makeconfig()
        setattr(namespace, self.dest, values)

class CLI:
    """
    this is CLI argument and default setup for script
    """
    def __init__(self) -> None:

        self.argparser = argparse.ArgumentParser(
            prog='INSTRUMENT CONTROLLER',
            description='This program is controller for instument in the lab with SCPI support',
            epilog=' for more help visit https://github.com/vijaypanchalr3 \n for more help on SR830 check manual of SR830')
        self.arguments()
        self.args = self.argparser.parse_args()
        
        
    def arguments(self) ->None:
        self.argparser.add_argument('-f','--file', metavar='*.csv', type=str, default="default", help="give an file to write data")
        self.argparser.add_argument('-pa','--partitions', metavar='',type=int, default=_defaults.partitions, help="give partition for frequency division")
        self.argparser.add_argument('-le','--level', metavar='', type=int, default=_defaults.levels, help="similar to levels it take increases partitions and resolution")
        self.argparser.add_argument('-tc', '--timeconst', metavar='', type=int, choices=range(1,20), default=_defaults.time_constant, help="choose time constant from manual from following choises:  "+" ".join([str(x) for x in range(1,21)]))
        self.argparser.add_argument('-td', '--timedelay', metavar='', type=float, default=_defaults.time_delay, help="choose time delay from manual from following choises  ")
        self.argparser.add_argument('-se', '--sensitivity', metavar='', type=int, choices=range(1,27), default=_defaults.sensitivity, help="choose sensitivity from following choises:  "+" ".join([str(x) for x in range(1,28)]))
        self.argparser.add_argument('-sr', '--samplerate', metavar='', type=int, choices=range(1,15), default=_defaults.sample_rate, help="sample rate for output sampling from following choises:  "+" ".join([str(x) for x in range(1,16)]))
        self.argparser.add_argument('-dt', '--data', metavar='', type=int,choices=range(1,5),default=_defaults.data, help="give default data variable from following choises:  "+" ".join([str(x) for x in range(1,6)]))
        self.argparser.add_argument('-bd', '--baud', metavar='', type=int, default=_defaults.baud_rate, help="set baud rate for connection defaults to 9600")
        self.argparser.add_argument('-c', '--connection', metavar='', type=str, choices=range(1,5), default=_defaults.connection, help="1: GPIB, 2: RS232, 3: USB, 4: LAN")
        self.argparser.add_argument('--makeconfig', action=makeconfig, default=1,help="this will make your custom config file")

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
    
