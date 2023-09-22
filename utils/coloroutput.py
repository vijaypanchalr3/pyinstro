from termcolor import cprint

def error(string)-> None:
    cprint(string,color="red",attrs=['bold'])

def normal(string)-> None:
    cprint(string, color="yellow")

def positive(string)-> None:
    cprint(string, color='green')

def attentive(string)-> None:
    cprint(string, color="blue", attrs=['bold'])
