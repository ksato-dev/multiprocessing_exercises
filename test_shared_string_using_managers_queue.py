# -*- coding: utf-8 -*-
from multiprocessing import Process, Manager, Lock
import time
# from ctypes import c_char_p

def hoge(shared_dict, lock):
    while True:
        string = shared_dict["text"]

        if (string != ""):
            lock.acquire()
            print(string)
            shared_dict["text"] = ""
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
    
    manager = Manager()
    shared_dict = manager.dict()
    shared_dict["text"] = ""

    hoge_subprocess = Process(target=hoge, args=(shared_dict, lock))
    hoge_subprocess.start()

    while True:
        lock.acquire()  
        print("main")
        shared_dict["text"] = "Time:" + str(time.time()) + ", main() to hoge()."
        lock.release() 

        time.sleep(2)

if __name__ == "__main__":
    main()