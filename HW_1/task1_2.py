import cProfile

# def rev(num):
#     rev_num = ''
#
#     while num / 10 > 0:
#         el = str(num % 10)
#         num = num // 10
#         rev_num = rev_num + el
#
#     rev_num = int(rev_num)
#     return rev_num

# python -m timeit -n 1000 -s "import task1_2" "task1_2.rev(1234)"
# "task1_2.rev(1234)"
# 1000 loops, best of 3: 2.05 usec per loop

# "task1_2.rev(12345)"
# 1000 loops, best of 3: 1.68 usec per loop

# "task1_2.rev(123456)"
# 1000 loops, best of 3: 1.77 usec per loop

# "task1_2.rev(1234567)"
# 1000 loops, best of 3: 1.91 usec per loop
#
# "task1_2.rev(123456789101112)"
# 1000 loops, best of 3: 3.2 usec per loop
#
# def rev(num):
#     num = str(num)
#     for i in num:
#         num = num[1:] + i
#     num = int(num)
#     return num

# print(rev(1234))

# python -m timeit -n 1000 -s "import task1_2" "task1_2.rev(1234)"
# "task1_2.rev(1234)"
# 1000 loops, best of 3: 1.34 usec per loop

# "task1_2.rev(12345)"
# 1000 loops, best of 3: 1.47 usec per loop

# "task1_2.rev(123456)"
# 1000 loops, best of 3: 1.39 usec per loop

# "task1_2.rev(1234567)"
# 1000 loops, best of 3: 1.43 usec per loop

# "task1_2.rev(123456789101112)"
# 1000 loops, best of 3: 2.16 usec per loop

# def rev(num):
#     num = str(num)[::-1]
#     return num

# python -m timeit -n 1000 -s "import task1_2" "task1_2.rev(1234)"

# "task1_2.rev(1234)"
# 1000 loops, best of 3: 0.467 usec per loop

# "task1_2.rev(12345)"
# 1000 loops, best of 3: 0.38 usec per loop

# "task1_2.rev(123456)"
# 1000 loops, best of 3: 0.469 usec per loop

# "task1_2.rev(1234567)"
# 1000 loops, best of 3: 0.51 usec per loop

# "task1_2.rev(123456789101112)"
# 1000 loops, best of 3: 0.538 usec per loop

cProfile.run('rev(1234)')