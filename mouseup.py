import pyautogui as pg
import multiprocessing
import time
print(pg.position())

def foo(n):
   pg.moveTo(601,395)
   pg.mouseDown(); pg.mouseUp()  # does the same thing as a left-button mouse click
   pg.mouseDown(button='left')  # press the left button down
    
   
   
if __name__ == '__main__':
    # Start foo as a process
    p = multiprocessing.Process(target=foo)
    p.start()

    # Wait 69 seconds for foo
    time.sleep(69.865)
    pg.mouseUp(button='left', x=601, y=395)
    # Terminate foo
    p.terminate()

    # Cleanup
    p.join()