import random
N = 10
S = 5
E = 8
# bytes(random.sample(range(S, E+1), E-S+1),'utf-8')
for i in range(S,E):
    print(bytearray([i] * N))
