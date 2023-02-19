```python

from redis_list.script import RedisStorage

redis_storage = RedisStorage('user:14')
# storing list of data in redis

redis_storage.set_data("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")

# append data to list
redis_storage.append_data("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")

# get data
redis_storage.get_data()

# get element at index
redis_storage.get_element_by_index()

# user details hash keys
redis_storage.delete_data()

# clear db of all data
redis_storage.clear_data()
```