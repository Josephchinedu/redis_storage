from dataclasses import dataclass

import redis


@dataclass
class RedisStorage:
    """
    Class for storing data in Redis.
    """

    redis_key: str
    redis_client: object = redis.StrictRedis(host="localhost", port="6379", db=0, decode_responses=True, encoding="utf-8")

    def set_data(self, data):
        """
        Set data in Redis.
        """
        self.redis_client.set(self.redis_key, data)

    def get_data(self):
        """
        Get data from Redis.
        """
        return self.redis_client.get(self.redis_key)

    def delete_data(self):
        """
        Delete data from Redis.
        """
        self.redis_client.delete(self.redis_key)

    def clear_data(self):
        """
        Clear data from Redis.
        """
        self.redis_client.flushdb()
