import sys
import os
import time
import signal

def main():
    my_pid = 0
    my_filepath = []

    my_pid = os.getpid()
    my_filepath = sys._getframe().f_code.co_filename
    
    setup(my_pid, my_filepath)
    signal.signal(signal.SIGTERM, sigterm_handler)
    try:
        while True:
            time.sleep(10)
    
    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        cleanup(my_pid, my_filepath)
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)

def sigusr1_handler(signum, frame):
    print("getdata!!")
    time.sleep(10)

def sigterm_handler(signum, frame):
    sys.exit(1)

def setup(pid, filepath):
    print("[{0}: {1}] Set up now...".format(pid, filepath))
    signal.signal(signal.SIGUSR1, sigusr1_handler)
    print("[{0}: {1}] Set up done.".format(pid, filepath))

def cleanup(pid, filepath):
    print("[{0}: {1}] Clean up now...".format(pid, filepath))
    signal.signal(signal.SIGUSR1, signal.SIG_DFL)
    print("[{0}: {1}] Clean up done.".format(pid, filepath))

if __name__ == "__main__":
    sys.exit(main())
