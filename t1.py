#!/usr/bin/python
# -*- coding: UTF-8 -*-

#!/usr/bin/python
import json


str = raw_input("请输入：")
print "你输入的内容是: ", str
data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
json = json.dumps(data)
print json


