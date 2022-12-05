import hashlib
import os
import pickle
import redis


class Redis:
    def __init__(self):
        self.redis = redis.Redis(
            host=os.getenv("REDIS_HOST"),
            port=int(os.getenv("REDIS_PORT")),
            password=os.getenv("REDIS_PASSWORD"),
            db=0,
        )

    def check_key(self, query):  # check if key exists in redis
        key = hashlib.sha224(query).hexdigest()
        return self.redis.exists(key)

    def check_word(self, query, word):  # check if word exists in the redis key
        key = hashlib.sha224(query).hexdigest()
        data = self.redis.get(key)
        data = pickle.loads(data)
        return word in data

    def add_entry(self, query, data):  # check if key exists in redis
        key = hashlib.sha224(query).hexdigest()
        data = pickle.dumps(data)
        self.redis.set(key, data)
        self.redis.expire(key, int(os.getenv("REDIS_TTL")))

    def add_word(
        self, query, word
    ):  # add a new word into the redis key, value pair and reset the ttl
        key = hashlib.sha224(query).hexdigest()
        data = self.redis.get(key)
        data = pickle.loads(data)
        data.add(word)
        data = pickle.dumps(data)
        self.redis.set(key, data)
        self.redis.expire(key, int(os.getenv("REDIS_TTL")))
