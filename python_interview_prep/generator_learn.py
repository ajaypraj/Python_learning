import os
import time
import datetime

while True:
    os.system("echo " + "sample line with timestamp:{0}".format(datetime.datetime.now()) + " >> " + "sample.csv")
    time.sleep(5)

