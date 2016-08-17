#!/usr/bin/python
#coding=utf-8
import threading
import time

class MyThread(threading.Thread):
	"""
	属性:
	target:传入外部函数,用户线程调用
	args:函数参数
	"""
	def __init__(self,target,args):
		super(MyThread,self).__init__()
		self.target =  target
		self.args   = args

	def run(self):
		self.target(self.args)


def print_time(counter):
	while counter:
		print "counter = %d" % counter
		counter-=1
		time.sleep(1)

def main(list=None):
	if list is None:
		list = [10,20,30,40]
	files = range(len(list))
	threads = []
	for val in list:
		t = MyThread(print_time,val)
		threads.append(t)
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()

if __name__ == '__main__':
	main()
