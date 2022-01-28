my_dict = {
    "key1": 0,
    "key2": 2,
    "key3": 5,
    "key4": 5,
}
value = 5


def delete_key_having_value(dictionary, value):
    keys_to_delete = []
    for Key in dictionary.keys():
        if dictionary[Key] == value:
            keys_to_delete.append(Key)
    for Key in keys_to_delete:
        dictionary.pop(Key)
    return dictionary


print(delete_key_having_value(my_dict, value))
