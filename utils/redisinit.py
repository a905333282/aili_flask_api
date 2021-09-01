import redis
from config import config_mapper

redis = redis.StrictRedis(
    host=config_mapper["dev"].REDIS_HOST, port=config_mapper["dev"].REDIS_POST, db=0, decode_responses=True
)