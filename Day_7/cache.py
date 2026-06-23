import json
import redis

redis_client = redis.Redis(
    host = "localhost",
    port = 6379,
    decode_responses = True
)

CACHE_TTL = 60

def cache_get(key: str):
    try:
        value = redis_client.get(key)
        if value:
            return json.loads(value) if value else None
    except Exception as e:
        print("REDIS ERROR:", e)
        return None

def cache_set(key, data):
    try:
        redis_client.setex(
            key,
            CACHE_TTL,
            json.dumps(data, default=str)
        )
        print("CACHE SAVED")

    except Exception as e:
        print("CACHE ERROR:", e)
        
def clear_posts_cache():
    for key in redis_client.scan_iter(
        "posts:*"
    ):
        redis_client.delete(key)