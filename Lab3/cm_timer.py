from datetime import datetime
from contextlib import contextmanager
from time import sleep, time


@contextmanager
def cm_timer_1():
    start = datetime.now()
    yield
    result = datetime.now() - start
    print(result)


@contextmanager
def cm_timer_2():
    start = time()
    yield
    print('Duration: {}'.format(time() - start))