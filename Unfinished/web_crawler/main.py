from bs4 import BeautifulSoup
from urllib.request import urlopen
import queue
from woker import Worker
import thread
import time
from factory import Factory

def main():
     links = set()
     try:
         thread.start_new_thread(print_time, ("Thread-1", 2, ) )
         thread.start_new_thread(Worker().work(), ("Thread-2", 4, ) )
     except:
         print "Error: unable to start thread"

while 1:
   pass