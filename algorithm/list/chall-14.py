import math

sample_list = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]

N =3

result = [sample_list[i:i+math.ceil(len(sample_list)/N)] for i in range(0,len(sample_list), math.ceil(len(sample_list)/N))]
print(result)
