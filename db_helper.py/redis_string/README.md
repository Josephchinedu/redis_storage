```python

from redis_string.script import RedisStorage

redis_storage = RedisStorage('joseph')
# storing number of lottery ticket played by user 'joseph'
ticket_number = 1
redis_storage.set_data(ticket_number)

# getting number of lottery ticket played by user 'joseph'

redis_storage.get_data()

# deleting number of lottery ticket played by user 'joseph'

redis_storage.delete_data()

# clear db of all data
redis_storage.clear_data()
```