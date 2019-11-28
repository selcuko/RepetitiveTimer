import threading
class RepetitiveTimer(threading.Thread):
    def __init__(self, func, interval:float, event:threading.Event):
        threading.Thread.__init__(self)
        self.stopped = event
        self.function = func
        self.interval = interval

    def run(self):
        while not self.stopped.wait(self.interval):
            self.function()