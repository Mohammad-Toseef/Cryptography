from pprint import pprint


def dictionary(D, K, V):
    if K not in D.keys():
        D[K] = V
    return D

my_dict = {'first': 1}
pprint(dictionary(my_dict, 'first', 2))
