# -*- coding: utf-8 -*-
from multiprocessing import Process, Manager, Lock
import time
from ctypes import c_char_p

def hoge(shared_string, lock):
    while True:
        string = shared_string.value

        if (string != ""):
            lock.acquire()
            print(shared_string.value)
            shared_string.value = ""
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
    shared_string = manager.Value(c_char_p, "Hoge")

    hoge_subprocess = Process(target=hoge, args=(shared_string, lock))
    hoge_subprocess.start()

    while True:
        lock.acquire()  
        print("main")
        shared_string.value = "Time:" + str(time.time()) + ", main() to hoge()."
        lock.release() 

        time.sleep(2)

if __name__ == "__main__":
    main()