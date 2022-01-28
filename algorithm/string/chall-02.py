D = "MII CyberSec Consulting Service"
S = 4
E = 11
# Manipulation on string
result = D[0:S] + ("x" * (E-S+1)) + D[E+1:]

byt = bytes(D, 'utf-8')
# Manipulation on bytes
result2 = byt[0:S] + bytes("x" * (E-S+1),'utf-8') + byt[E+1:]

print(result)
print(result2)


