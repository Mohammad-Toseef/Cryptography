sample_list = [ 3, 0, 4, 9, 7, 9, 7, 2, 9, 4, 1, 4, 2, 5, 5, 7, 4, 0, 6, 9 ]
total = 0
for i, value in enumerate(sample_list):
    if i%2 !=0:
        total += value

print(total)
