import os
import sys
import time
import subprocess
import signal
import time
import datetime

child_pid = []
child_filename = ['/getdata.py', '/learning.py']

def main():
    os.system('clear')
    print("================================================================================")
    print("FX My Expert Advisor Program")
    print("                                                                   Version 0.0.0")
    print("================================================================================")
    global child_pid

    my_pid = 0
    my_filepath = []

    my_pid = os.getpid()
    my_filepath = sys._getframe().f_code.co_filename

    setup(my_pid, my_filepath)
    signal.signal(signal.SIGTERM, sigterm_handler)
    try:
        mainmenu()
    
    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        cleanup(my_pid, my_filepath)
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

def setup(pid, filepath):
    print("[{0}: {1}] Set up now...".format(pid, filepath))
    dir = os.path.dirname(__file__)
    child_num = len(child_filename)
    for num_i in range(child_num):
        command = ["python", dir + child_filename[num_i]]
        proc = subprocess.Popen(command)
        child_pid.append(proc.pid)

    signal.signal(signal.SIGALRM, sigalrm_handler)
    signal.setitimer(signal.ITIMER_REAL, 1, 1)
    print("[{0}: {1}] Set up done.".format(pid, filepath))

def cleanup(pid, filepath):
    print("[{0}: {1}] Clean up now...".format(pid, filepath))
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
    child_num = len(child_filename)
    for num_i in range(child_num):
        os.kill(child_pid[num_i], signal.SIGTERM)
    print("[{0}: {1}] Clean up done.".format(pid, filepath))

def sigterm_handler(signum, frame):
    sys.exit(1)

def sigalrm_handler(signum, frame):
    sysclock = time.time()
    print(datetime.datetime.fromtimestamp(sysclock))
    if (int(sysclock) % 5) == 0:
        os.kill(child_pid[0], signal.SIGUSR1)
    if (int(sysclock) % 60) == 0:
        os.kill(child_pid[1], signal.SIGUSR1)

def get_menu_no():
    inn_str = input()
    if inn_str.isdecimal() == True:
        return (int(inn_str))
    else:
        return (-1)

def mainmenu():
    while True:
        print("--------------------")
        print("FX My EA Main Menu")
        print("--------------------")
        print("01. Test")
        print("99. Exit")
        print("\nPlease type Menu No.")
        print('>>', end = ' ')
        val = get_menu_no()
        if val == 1:
            print("\nSorry. This function is not implemented yet.\n")
        
        elif val == 99:
            break

        else:
            print("\nInvalid input!! Please type correct No.\n")

if __name__ == "__main__":
    sys.exit(main())
