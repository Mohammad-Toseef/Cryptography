def xor_two_str(str1,str2):

    return hex(str1 ^ str2)

S1 = '44355050f07a7e2df0067d45'
S2 = '165026358209174397283401'
print(xor_two_str(S1, S2))
