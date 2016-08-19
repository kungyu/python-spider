#!/usr/bin/python
#coding=utf-8
import sys,re
reload(sys)
sys.setdefaultencoding('utf8')
from pyquery import PyQuery as pq

#智联企业会员简介
def get_special_company_info(url):
        special_doc = pq(url=u''+url)
        company_tag = special_doc("#banner1")
	if company_tag.attr('class') == 'pngsupport':
		company_info_tag = company_tag.parent().parent().parent().next()
	else:
		company_info_tag = company_tag.parent().parent().next()
	company_info = company_info_tag.text()
	if company_info.find("getElementById") <> -1:
		company_info = company_info_tag.next().text()
	company_name = special_doc('.companyname:eq(0)').text()
        print company_name,company_info,url
#url = 'http://special.zhaopin.com/pagepublish/19908441/index.html'
#url = 'http://special.zhaopin.com/pagepublish/14499837/index.html'
#get_special_company_info(url=url)

#智联普通企业简介
def get_common_company_info(url):
	common_doc = pq(url=u''+url)
	company_tag = common_doc(".company-content")
	company_info = company_tag.text()
	company_name = common_doc("h1:eq(0)").text().strip()
	print company_name,company_info,url
