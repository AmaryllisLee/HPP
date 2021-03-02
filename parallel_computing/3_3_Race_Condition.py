import threading, logging, time
import concurrent.futures

class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        self._lock.acquire() #acquire : tx+1 can't run line 12 - 14 until t0 has releases (lock.release()). One thread runs line 12 -14 at a time.
        local_copy = self.value
        local_copy += 1 
        time.sleep(0.1) # if this line is removed , t0 can set self.value before t1 can reach line 10/read self.value
        self.value = local_copy # We can define this line as our race condition, beacue both thread t0 and t1 are overwriting self.value .
        # Line 13 : t1 is reading self.value  before self.value is being overwritten by t0. Tus t1 is overwritting self.value as 1 beacuse t1 read self.value as 0.
        self._lock.release()
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)

