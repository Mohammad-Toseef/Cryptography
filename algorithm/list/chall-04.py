sample_list = [ 1, 1, 2, 3, 4, 4, 6, 9 ]
result = []

[result.append(x) for x in sample_list if x not in result]
print(result)
