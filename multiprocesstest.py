from datetime import datetime
import random
import time
import multiprocessing as mp
import os


def random_wait():
    wait = random.uniform(0, 1)
    time.sleep(wait)
    now = datetime.now().strftime("%H:%M:%S.%f")
    print(f"Process number: {os.getpid()} waited {wait:.8f} seconds. The time it captured was {now}")


if __name__ == '__main__':
    # Create a list of our processes. This isn't needed, but I'll explain in the next comment why we do this.
    process_list = []
    for process in range(3):
        p = mp.Process(target=random_wait)
        process_list.append(p)
        p.start()

    # Interestingly, this doesn't seem to be needed but the python documentation at
    # https://docs.python.org/3/library/multiprocessing.html
    # Uses it in almost EVERY example. It's supposed to make the program wait to terminate until the processes finish.
    # I tested around and set the uniform time range between 0 and 20, and added a print statement at the end of this
    # program, and it did in fact run the print statement and end the process before the 3 random_wait child processes
    # were finished. I'll definitely make note to use the join method. Neato!
    for p in process_list:
        p.join()

