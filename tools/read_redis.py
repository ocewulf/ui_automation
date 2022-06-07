#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/6/1 16:34 
"""
import redis


class Read_Redis(object):
    # 连接redis
    def conn_redis(self):
        # r = redis.Redis(host='127.0.0.1', port=6379, password='foobar', db=0, decode_responses=True)
        # r = redis.StrictRedis(host='127.0.0.1', port=6379, password='foobar', db=0, decode_responses=True)
        """
        创建连接池 使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，
        每个redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数redis，这样就可以实现多个redis实例共享一个连接池
        """
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='', db=0, decode_responses=True)
        r = redis.Redis(connection_pool=pool)

        # 操作redis
        r.set("sex", "male")
        print(r.get('sex'))


if __name__ == '__main__':
    Read_Redis().conn_redis()