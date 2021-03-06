# -*- coding: utf-8 -*-
from multiprocessing import Process, Pipe, Lock
import time

def hoge(input_pipe, lock):
    print("Start hoge()")
    while True:
        string = input_pipe.recv()

        if (string != ""):
            lock.acquire()
            print(string)
            input_pipe.send("")
            lock.release()
            print("**************************")
            print("**************************")
            print("**************************")
            print("update shared_string")
            print("**************************")
            print("**************************")
            print("**************************")
            time.sleep(0.3)
        else:
            print("hoge")

def main():

    print("Start main()")
    lock = Lock()
    
    hoge_pipe1, hoge_pipe2 = Pipe()
    hoge_pipe1.send("Hoge")

    hoge_subprocess = Process(target=hoge, args=(hoge_pipe2, lock))
    hoge_subprocess.start()

    while True:
        lock.acquire()  
        print("main")
        hoge_pipe1.send("send from main() to hoge()")
        lock.release()  

        time.sleep(2)

if __name__ == "__main__":
    main()