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

    def set_data(self, *args):
        """
        Set data in Redis.
        """
        self.redis_client.lpush(self.redis_key, *args)

    def append_data(self, *args):
        """
        Append data in Redis.
        """
        self.redis_client.rpush(self.redis_key, *args)

    def get_data(self):
        """
        Get data from Redis.
        """
        return self.redis_client.lrange(self.redis_key, 0, -1)

    def get_element_by_index(self, index):
        """
        Get data from Redis.
        """
        return self.redis_client.lindex(self.redis_key, index)

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


if __name__ == "__main__":
    redis_db = RedisStorage("my_plan")
    # redis_db.set_data("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
    # redis_db.append_data("11", "12", "13", "14", "15", "16", "17", "18", "19", "20")
    # print(redis_db.get_data())

    print(redis_db.get_element_by_index(1))
