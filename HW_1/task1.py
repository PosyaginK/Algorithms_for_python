import cProfile

def what_year(year):
    del_yaer = abs(2000 - year)
    if year % 100 == 0:
        if year % 400 == 0:
            return f'Yes'
        else:
            return f'No.'
    else:
        if del_yaer % 4 == 0:
            return f'Yes'
        else:
            return f'No.'

# 1000 loops, best of 3: 0.245 usec per loop | 1994

# def what_year(year):
#     if year % 100 == 0 and year % 400 != 0:
#         return 'Yes!'
#     elif year % 4 == 0:
#         return 'Yes!'
#     else:
#         return 'No!'

# "task1.what_year(1998)"
# 1000 loops, best of 3: 0.178 usec per loop

cProfile.run('what_year(2000)')