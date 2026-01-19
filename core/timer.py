import time

class SchulteTimer:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.is_running = False

    def start(self):
        self.start_time = time.perf_counter()
        self.is_running = True

    def stop(self):
        if self.is_running:
            self.end_time = time.perf_counter()
            self.is_running = False
            return round(self.end_time - self.start_time, 2)
        return 0