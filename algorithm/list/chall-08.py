from itertools import chain
# 2-d list
list_of_lists = [ [2, 4, 3], [1, 5, 6], [9], [7, 9] ]
# 1-d list
result = list(chain.from_iterable(list_of_lists))

print(result)

