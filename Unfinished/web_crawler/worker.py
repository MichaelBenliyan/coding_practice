from threading import Thread
from bs4 import BeautifulSoup
from urllib.request import urlopen
from queue import Queue


class Worker(Thread):
    def __init__(self, id):
        self.id = id
        self.running = False

    def work(self, queue, seen):
        self.running = True
        while queue.not_empty:
            current = queue.get()
            new_links = current.find_all('a', attrs={'href': re.compile("^http://")}) # whatever will return links
            for link in new_links: 
                if link not in seen: 
                    seen.add(link)
                    soup = BeautifulSoup(link, "html.parser")
                    queue.put(soup)
        self.running = False
                    
                    
    def __bool__(self):
        return self.running
            
    
        