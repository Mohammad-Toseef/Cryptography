N = [ "black", "red", "maroon", "yellow" ]
C = [ "#000000", "#FF0000", "#800000", "#FFFF00" ]


def list_of_dict(list1, list2):
    final_list = []
    for i in range(len(list1)):
        dictionary = {}
        dictionary['name'] = list1[i]
        dictionary['code'] = list2[i]
        final_list.append(dictionary)
    return final_list


print(list_of_dict(N, C))
