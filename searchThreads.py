# IMPORTS
import sys, os
import threading
import time
from searchFunctions import *
# End IMPORTS

# Globals
PATH = r"C:\Users\Bartek\Desktop\ZAJECIA"
result_list = []
# End Globals


class searchThreads(threading.Thread):
    index = 0

    def __init__(self, name, pth, target=None):
        super().__init__()
        self.name = name + str(searchThreads.index)
        self.list_of_files = []
        self.list_of_threads = []
        self.pth = pth
        searchThreads.index+=1
    def run(self):
        global result_list

        for file in os.listdir(self.pth):
            if os.path.isdir(os.path.join(self.pth,file)):
                self.list_of_files.append(os.path.join(self.pth,file))
                thread = searchThreads("noob",os.path.join(self.pth,file))
                self.list_of_threads.append(thread)
            elif os.path.isfile(os.path.join(self.pth,file)):
                self.list_of_files.append(os.path.join(self.pth,file))

        result_list.append(self.list_of_files)  
        if self.list_of_threads:
            [i.start() for i in self.list_of_threads]
            [i.join() for i in self.list_of_threads]

if __name__ == "__main__":
    t = time.time()
    result_list = []
    thread1 = searchThreads("noob", PATH)
    thread1.start()
    thread1.join()
    print(len([*sum(result_list,[])]))
    