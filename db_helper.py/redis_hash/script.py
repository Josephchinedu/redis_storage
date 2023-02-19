from dataclasses import dataclass

import redis


@dataclass
class RedisStorage:
    """
    Class for storing data in Redis.
    """

    redis_key: str
    redis_client: object = redis.StrictRedis(
        host="localhost", port="6379", db=0, decode_responses=True, encoding="utf-8"
    )

    def set_data(self, data: dict):
        """
        Set dict data in Redis.
        """
        self.redis_client.hset(self.redis_key, mapping=data)

    def get_data(self):
        """
        Get dict data from Redis.
        """
        return self.redis_client.hgetall(self.redis_key)

    def get_all_hash_keys(self):
        """
        Get dict data from Redis.
        """
        return self.redis_client.hkeys(self.redis_key)

    def get_value_of_a_key(self, key):
        """
        Get dict data from Redis.
        """
        return self.redis_client.hget(self.redis_key, key)

    def get_value_of_multiple_keys(self, *required_keys):
        """
        Get dict data from Redis.
        """
        return self.redis_client.hmget(self.redis_key, required_keys)

    def delete_data(self):
        """
        Delete data from Redis.
        """
        self.redis_client.delete(self.redis_key)

    def delete_a_key(self, key):
        """
        Delete data from Redis.
        """
        self.redis_client.hdel(self.redis_key, key)

    def clear_data(self):
        """
        Clear data from Redis.
        """
        self.redis_client.flushdb()


