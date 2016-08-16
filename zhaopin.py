#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,re
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq
import func
doc = pq(url=u'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=160000&in=210500%3b160400%3b160000%3b160600&jl=%E9%9D%92%E5%B2%9B&isadv=0&sg=00f311b5cd1e4fcfad9f61bbf77f3471&p=1')
lis = doc('.gsmc').find('a')
company_url_list = []
company_name_list = []
for li in lis.items():
	company_name = li.text()
	company_url  = li.attr('href')
	if company_name.find('青岛') == -1:
		continue
	else:
		company_url_list.append(company_url)
		company_name_list.append(company_name)
#print company_url_list
#print company_name_list
#for name in company_name_list:
#	print name
company_url_list = list(set(company_url_list))
for url in company_url_list:
	url_arr = url.split('/')
	if url.find('special') > 0:
		company_id = url_arr[-2]
		func.get_special_company_info(url)
	else:
		url_pam_str = url_arr[-1]
		str_p = url_pam_str.find('_')
		if str_p > 0:
			url_pam_str = url_pam_str[str_p:]
		an = re.search(r'\d+',url_pam_str)
		company_id = an.group()
		func.get_common_company_info(url)
#	print url,company_id
#	print compnay

