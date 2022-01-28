import random
sample_list = [ 1,  2, 3, 4, 6, 9 ]

#choose random value
value = random.choice(sample_list)

#chosen item is kept
print(sample_list)
#chosen item is discarded
sample_list.pop(value)
print(sample_list)


