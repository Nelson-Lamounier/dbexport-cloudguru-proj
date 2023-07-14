import os
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# We're caching the result of engine so that it will only configure the engine
# value once based on a given database URL, and subsequent calls will return the
# same object from the cache. This is done by using the functools.lru_cache
# decorator.
@lru_cache(maxsize =32)
def engine(db_url=None):
    db_url = db_url or os.getenv("DB_URL") # If there is no DB_URL environment variable and no string is manually passed in,then we'll raise an error.
    if not db_url:
        raise ValueError("database URL is required")
    return create_engine(db_url)

def get_connection(db_url=None):
    return engine(db_url).connect()

@lru_cache(maxsize=32)
def session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))

try:
    Session = session_class()
except:
    pass
