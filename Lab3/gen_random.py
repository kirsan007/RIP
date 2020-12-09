
import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randrange(begin, end + 1)

#f = gen_random(10, 1, 212)

#for i in gen_random(10, 1, 212):
#    print(i)




