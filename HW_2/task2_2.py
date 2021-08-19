import cProfile

def erat(pos):
    result = [2]
    next_el = 2
    while len(result) != pos:
        next_el += 1
        check = 0
        for el in result:
            if next_el % el == 0:
                check += 1
        if check == 0:
            result.append(next_el)

    return result[-1]

# "task2_2.erat(10)"
# 1000 loops, best of 3: 10.7 usec per loop

cProfile.run('erat(50)')

# "task2_2.erat(20)"
# 1000 loops, best of 3: 42.5 usec per loop

# "task2_2.erat(30)"
# 1000 loops, best of 3: 89.5 usec per loop

# "task2_2.erat(40)"
# 1000 loops, best of 3: 183 usec per loop

# "task2_2.erat(50)"
# 1000 loops, best of 3: 292 usec per loop
