list_of_dict = [ {'id':'1', 'room': '404', 'duration': '4'}, {'id':'2', 'room':'405'} ]

for i in range(len(list_of_dict)-1):
    keys_to_delete = []
    for key in list_of_dict[i].keys():
        if key in list_of_dict[i+1].keys():
            keys_to_delete.append(key)
    if len(keys_to_delete) > 1:
        for i in range(1,len(keys_to_delete)):
            for j in range(len(list_of_dict)):
                list_of_dict[j].pop(keys_to_delete[i])

print(list_of_dict)


