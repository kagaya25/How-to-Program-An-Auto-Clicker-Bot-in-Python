import pyautogui as pg
import multiprocessing
import time
print(pg.position())
def foo():
   pg.moveTo(411,605)
   while True:
    pg.click()  
if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo)
    p.start()
    # Wait 11 seconds for foo
    time.sleep(11)
    # Terminate foo
    p.terminate()
    # Cleanup
    p.join()