#!/usr/bin/python
#coding=utf-8
import redis

client = redis.StrictRedis(host='127.0.0.1',port=6379,db=0)
print 'Connection'
client.lpush('url-list','kung')
client.lpush('url-list','yu')
first = client.lindex('url-list',0)
print first
dicKeys = client.keys("*")
print dicKeys
urlist = client.get("url-list")
print urlist
