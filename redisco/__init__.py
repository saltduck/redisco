# -*- coding: utf-8 -*-
default_connection_settings = {}
try:
    import redislite as redis
except ImportError:
    import redis
    default_connection_settings = {
        'decode_responses': True,
        'host': 'localhost',
        'port': 6379,
        'db': 0
    }


class Client(object):
    def __init__(self, **kwargs):
        self.connection_settings = kwargs or default_connection_settings

    def redis(self):
        return redis.Redis(**self.connection_settings)

    def update(self, d):
        self.connection_settings.update(d)


def connection_setup(**kwargs):
    global connection, client
    if client:
        client.update(kwargs)
    else:
        client = Client(**kwargs)
    connection = client.redis()


def get_client():
    global connection
    return connection


client = Client()
connection = client.redis()
default_expire_time = 60

__all__ = ['connection_setup', 'get_client']
