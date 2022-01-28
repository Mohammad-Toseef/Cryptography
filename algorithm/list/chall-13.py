sample_list = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ]
N =3

result = [sample_list[i:i+N] for i in range(0,len(sample_list),N)]
print(result)
