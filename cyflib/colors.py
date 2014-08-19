HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
def reset_color():
    return ENDC
def status(estilo, texto):
    if(estilo==0):
        return "[ " + OKGREEN + "OK" + ENDC + " ] " + texto
    elif(estilo==1):
        return "[" + OKBLUE + "INFO" + ENDC + "] " + texto
    elif(estilo==2):
        return "[" + WARNING + "WARN" + ENDC + "] " + texto
    elif(estilo==3):
        return "[" + FAIL + "FAIL" + ENDC + "] " + texto
    elif(estilo==4):
        return "[" + FAIL + "ERROR" + ENDC + "] " + texto
