my_dict = {
    "key1": 0,
    "key2": 2,
    "key3": 5,
         }
key = "key2"


def delete_key_if_exist(dictionary, Key):
    if Key in dictionary.keys():
        my_dict.pop(Key)
    return dictionary


print(delete_key_if_exist(my_dict, key))
