#!/usr/bin/python
#coding=utf-8
from muti_thread import main
a = [5, 2, 5, 1, 4, 3, 4]  
print set(a)
b =  list(set(a)) 
main(b)
