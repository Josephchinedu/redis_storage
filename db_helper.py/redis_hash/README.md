```python

from redis_hash.script import RedisStorage

redis_storage = RedisStorage('user:14')
# storing user:14 details in redis

user_details = {"name": "joseph", "age": 14, "occupation": "student"}

redis_storage.set_data(user_details)

# get all user:14 details
redis_storage.get_data()

# get all user details hash keys
redis_storage.get_all_hash_keys()

# get value of a specific hash key
redis_storage.get_value_of_a_key('name')

# get value of multiple hash keys
redis_storage.get_value_of_multiple_keys("name", "age")

# delete a specific hash key
redis_storage.delete_a_key('name')

# user details hash keys
redis_storage.delete_data()

# clear db of all data
redis_storage.clear_data()
```