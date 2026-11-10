import json
import logging
import os

import redis
logger = logging.getLogger(__name__)

class CacheManager:
    def __init__(self, redis_url=None, default_ttl=None):
        redis_url = redis_url or os.environ.get("REDIS_URL", "redis://localhost:6379/0")
        self.default_ttl = default_ttl or int(os.environ.get("CACHE_TTL_SECONDS", "600"))
        timeout = float(os.environ.get("REDIS_TIMEOUT_SECONDS", "3"))
        self.client = redis.Redis.from_url(
            redis_url,
            decode_responses=True,
            socket_connect_timeout=timeout,
            socket_timeout=timeout,
        )
    
    def ping(self):
        try:
            return self.client.ping()
        except redis.exceptions.RedisError as ex:
            logger.warning("Could not connect to Redis: %s", ex)
            return False
        
    def get(self, key, refresh_ttl=False):
        try:
            if refresh_ttl:
                value = self.client.getex(key, ex=self.default_ttl)
            else: 
                value = self.client.get(key)
        except redis.exceptions.RedisError:
            logger.warning("Redis is not enabled when reading the key %s", key)
            return None
        if value is None:
            return None
        return json.loads(value)
    
    def set(self, key, value, ttl = None):
        try:
            self.client.set(key, json.dumps(value), ex=ttl or self.default_ttl)
            return True
        except redis.exceptions.RedisError:
            logger.warning("Redis is unavailable saving the key %s ", key)
            return False
        
    def delete(self, *keys):
        try:
            self.client.delete(*keys)
            return True
        except redis.exceptions.RedisError:
            logger.error("Redis is unavailable to invalidate the keys %s", keys)
            return False

    