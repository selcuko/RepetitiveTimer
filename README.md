# RepetitiveTimer


RepetitiveTimer module is wrapper for threading.Thread, makes it easy to initialize a repetitive timer.

  - No additional modules needed

### Usage
```python
import threading, time
from RepetitiveTimer.RepetitiveTimer import RepetitiveTimer

def poo():
    print("Timer ticked.")

stopper = threading.Event()
timer = RepetitiveTimer(poo, .5, stopper) # function, interval (seconds), stopper flag
timer.run()   # To start timer
time.sleep(10)
stopper.set() # To stop timer
```
