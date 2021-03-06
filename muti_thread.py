#!/usr/bin/python
#coding=utf-8
import threading
import time
import func
import re

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
	for url in list:
		url_arr = url.split('/')
		if url.find('special') > 0:
			company_id = url_arr[-2]
			t = MyThread(func.get_special_company_info,url)
		else:
			url_pam_str = url_arr[-1]
			str_p = url_pam_str.find('_')
			if str_p > 0:
				url_pam_str = url_pam_str[str_p:]
			an = re.search(r'\d+',url_pam_str)
			company_id = an.group()
			t = MyThread(func.get_common_company_info,url)
		threads.append(t)
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()

if __name__ == '__main__':
	main()
