my_dict={'Krishna':20,'Medha':21,'Anu':26}
sorted_by_key_asc=dict(sorted(my_dict.items()))
sorted_by_key_desc=dict(sorted(my_dict.items(),reverse=True))
print("Sorted by keys in ascending order : ",sorted_by_key_asc)
print("Sorted by keys in descending order : ",sorted_by_key_desc)
