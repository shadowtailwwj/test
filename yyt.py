#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# ����̨MV���������

import urllib2
import urllib
import re

mv_id = '2278607'  # ��������mv��id����http://v.yinyuetai.com/video/2275893��������
url = "http://www.yinyuetai.com/insite/get-video-info?flex=true&videoId=" + mv_id
timeout = 30
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
}



req = urllib2.Request(url, None, headers)
res = urllib2.urlopen(req,None, timeout)
html = res.read()
reg = r"http://\w*?\.yinyuetai\.com/uploads/videos/common/.*?(?=&br)"
pattern=re.compile(reg)
findList = re.findall(pattern,html)   # �ҵ�mv���а汾����������


if len(findList) >= 3:
	mvurl = findList[2]   # �������������塢���������汾ʱ���س���
else:
	mvurl = findList[0]   # �汾��ʱ����������Ƶ

local = 'MV.flv'

try:
	print 'downloading...please wait...'
	urllib.urlretrieve(mvurl,local)
	print "[:)] Great! The mv has been downloaded.\n"
except:
	print "[:(] Sorry! The action is failed.\n"







