K = [ "name", "hp", "mp" ]
V = [ "xathrya", "100", "32" ]


def generate_dictionary(list1, list2):
    my_dict = {}
    for i in range(len(list1)):
        my_dict[list1[i]] = list2[i]
    return my_dict


dictionary = generate_dictionary(K, V)
print(dictionary)