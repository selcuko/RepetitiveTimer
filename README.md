# RepetitiveTimer


RepetitiveTimer module is wrapper for threading.Thread, makes it easy to initialize a repetitive timer.

  - No additional modules needed

### Usage
```python
import threading, time

def poo():
    print("Timer ticked.")

stopper = threading.Event()
timer = RepetitiveTimer(func=poo, interval=.5, stopper)
timer.run()   # To start timer
time.sleep(10)
stopper.set() # To stop timer
```