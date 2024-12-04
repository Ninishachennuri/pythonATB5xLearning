# Sort a dictionary by its values in descending order
#my_dict = {"a": 3, "b": 1, "c": 2}

# {b: 1 , c: 2 , a :3}

dict1 = {"a": 3, "b": 1, "c": 2}
dict2 = {"b": 1, "c": 2, "a": 3}

missing_keys = set(dict1.keys()) - set(dict2.keys())
print(missing_keys)

my_dict = {"a": 1, "b": 2, "c": 3}