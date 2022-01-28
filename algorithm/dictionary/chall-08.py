list_of_dict = [ {'key': 1}, {'key': 10}, {'key': 5} ]

def secondvalue(dic):
    for key in dic.keys():
        return dic[key]

list_of_dict.sort(key=secondvalue)
print(list_of_dict)


