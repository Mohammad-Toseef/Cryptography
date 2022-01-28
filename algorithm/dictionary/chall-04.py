S = input('Enter string : ')


def occurance(string):
    my_dict = {}
    for i in string:
        if i not in my_dict.keys():
            my_dict[i] = string.count(i)
    return my_dict


print(occurance(S))
