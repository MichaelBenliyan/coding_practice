from queue import Queue
from bs4 import BeautifulSoup
from urllib.request import urlopen
from woker import Worker
from time import sleep

class Factory(): 
    def __init__(self, start_url, num_threads) -> None:
        self.links = set()
        self.queue = Queue()
        self.thread_count = num_threads
        self.start = start_url
        self.workers = [Worker(i) for i in range(num_threads)]
        
    def start(self): 
        self.links.add(self.start_url)
        page = urlopen(self.start_url())
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        self.queue.put(soup)
        for worker in self.workers: 
            worker.start()
            worker.work(self.queue, self.links)
        for worker in self.workers: 
            worker.join()
        while any(self.workers):
            sleep(1);
        print(self.links)