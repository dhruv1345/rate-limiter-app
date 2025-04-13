import time
import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

RATE_LIMIT = 5  # 5 requests
TIME_WINDOW = 60  # in seconds

def is_allowed(user_id: str) -> bool:
    current_time = int(time.time())
    key = f"rate_limit:{user_id}:{current_time // TIME_WINDOW}"
    count = r.incr(key)

    if count == 1:
        r.expire(key, TIME_WINDOW)

    return count <= RATE_LIMIT
