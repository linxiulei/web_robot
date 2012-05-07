#!/usr/bin/env python
# -*- coding=utf-8 -*-

from mechanize import Browser
import re

URL = "http://www.qc5qc.com/"
QUERY_URL = URL + 'xqc/mlpxmore.php?searchbh='
PLACE_NO_DICT = {
    '001':'公交驾校',
    '002':'公交驾校',
    '003':'公交驾校',
    '004':'公交驾校',
    '005':'公交驾校',
    '006':'公交驾校',
    }


def query_order(no):
    br = Browser()
    response = br.open(QUERY_URL + no)
    return response.get_data().decode('gb2312')


data = query_order('001')
pattern = re.compile(u"可预约")
print data
orderno_match = pattern.search(data)
#print orderno_match.group()
