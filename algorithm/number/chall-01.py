N = 120

factors = []
for i in range(2,N):
    if N%i == 0:
        factors.append(i)
print(f"Factors of {N} are ",factors)
