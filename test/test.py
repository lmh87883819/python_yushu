import threading
import time

def worker():
    print('i am thread-worker')
    t = threading.current_thread()
    time.sleep(3)
    print(t.getName())

new_t = threading.Thread(target=worker,name='lmh_thread')
new_t.start()

t = threading.current_thread()
print(t.getName())