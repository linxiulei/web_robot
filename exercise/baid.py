# -*- coding=utf-8 -*-

from mechanize import Browser
import re

res = Browser().open('http://www.baidu.com')
data = res.get_data()
data = data.decode('gb2312')

pattern0 = re.compile(u"可预约.*\d{1,3}")

match = pattern0.search(u"公交驾校（可预约：阶段112人，阶段二75人）")
print match.group(0)
pattern1 = re.compile(u"\d{1,3}")
match = pattern1.findall(match.group(0))

reserving_no = match[0]
reserved_no = match[1]

print match

string = u'百度'
print string
