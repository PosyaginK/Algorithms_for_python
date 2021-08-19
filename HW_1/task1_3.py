import cProfile

def fun(start, finish):
    result = {}
    for i in range(2, 10):
        count = 0
        for el in range(start, finish):
            if el % i == 0:
                count += 1
        result[i] = count
    return result

# "task1_3.fun(2, 100)"
# 1000 loops, best of 3: 40.4 usec per loop

# "task1_3.fun(2, 1000)"
# 1000 loops, best of 3: 421 usec per loop

# "task1_3.fun(2, 10000)"
# 1000 loops, best of 3: 4.24 msec per loop

cProfile.run('fun(2, 100)')