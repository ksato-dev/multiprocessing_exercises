# -*- coding: utf-8 -*-
from multiprocessing import Process, Pipe, Lock
import time

"""
def hoge(share_string):
    while True:
        print("Excute hoge():", share_string.value)

def piyo(share_string):
    while True:
        print("Excute piyo():", share_string.value)
"""

def hoge(input_pipe, lock):
    print("Start hoge()")
    while True:
        # lock.acquire()
        string = input_pipe.recv()
        print("Time:{}, Excute hoge():{}".format(time.time(), string))
        input_pipe.send("send from hoge()")
        time.sleep(1)
        # lock.release()

def piyo(input_pipe, lock):
    print("Start piyo()")
    while True:
        # lock.acquire()
        string = input_pipe.recv()
        print("Time:{}, Excute piyo():{}".format(time.time(), string))
        input_pipe.send("send from piyo()")
        time.sleep(1)
        # lock.release()

def main():

    print("Start main()")
    lock = Lock()
    # hoge_lock = Lock()
    # piyo_lock = Lock()
    
    hoge_pipe1, hoge_pipe2 = Pipe()
    hoge_subprocess = Process(target=hoge, args=(hoge_pipe2, lock))
    # hoge_subprocess = Process(target=hoge, args=(hoge_pipe2, hoge_lock))

    piyo_pipe1, piyo_pipe2 = Pipe()
    piyo_subprocess = Process(target=piyo, args=(piyo_pipe2, lock))
    # piyo_subprocess = Process(target=piyo, args=(piyo_pipe2, piyo_lock))

    hoge_subprocess.start()
    piyo_subprocess.start()

    while True:
        lock.acquire()  ## If this statement enables, doesn't work this program.
        hoge_pipe1.send("send from main() to hoge()")
        string = hoge_pipe1.recv()
        print("Time:{}, Excute main():{}".format(time.time(), string))

        # time.sleep(1)

        piyo_pipe1.send("send from main() to piyo()")
        string = piyo_pipe1.recv()
        print("Time:{}, Excute main():{}".format(time.time(), string))

        # time.sleep(1)
        lock.release()  ## If this statement enables, doesn't work this program.

if __name__ == "__main__":
    main()