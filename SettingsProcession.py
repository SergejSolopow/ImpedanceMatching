import time
from time import sleep
from time import time

class SettingsProcessing():
    def __init__(self):
        print("class works")
    
    def timeDiff(self):
        t1 = time()
        sleep(2)
        print(time() - t1)


if __name__ == "__main__":
    myClass = SettingsProcessing()
    myClass.timeDiff()