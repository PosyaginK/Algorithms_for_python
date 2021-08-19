import cProfile

def erat(pos):
    result = []
    l = pos
    while len(result) != pos:
        l += 1
        s_list = [i for i in range(l)]
        s_list[1] = 0
        for i in range(2, l):
            if s_list[i] != 0:
                j = i * 2
                while j < l:
                    s_list[j] = 0
                    j += i
        result = [i for i in s_list if i != 0]
    return result[-1]


# print(erat(40))
# erat(40)

cProfile.run('erat(50)')

# "task2_1.erat(10)"
# 1000 loops, best of 3: 67.3 usec per loop

# "task2_1.erat(20)"
# 1000 loops, best of 3: 382 usec per loop

# "task2_1.erat(30)"
# 1000 loops, best of 3: 970 usec per loop

# "task2_1.erat(40)"
# 1000 loops, best of 3: 2.38 msec per loop

# "import task2_1" "task2_1.erat(50)"
# 1000 loops, best of 3: 4.11 msec per loop
