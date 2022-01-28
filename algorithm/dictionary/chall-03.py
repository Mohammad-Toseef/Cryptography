N = int(input('Enter number : '))


def generate_dictionary(number):
    my_dict = {}
    for i in range(1, number+1):
        my_dict[i] = i**2
    return my_dict


print(generate_dictionary(N))

