sample_list = [ 4, 5, 1, 6, 7, 2, 8, 9, 1, 6, 9 ]

def max_number(N):
    lst = []
    maximum = max(N)
    for i in range(N.count(maximum)):
        lst.append(maximum)
    return lst


print(max_number(sample_list))
