#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#输出语句
print("你好世界！")

#list和tuple
classlist=["小明","小刚","小美","小飞"]
classtuple=("王大","李二","张三","刘四")


#判断语句
age=int(input("请输入数字1或者2："))
if age == 1:
	print(classlist)
else:
	print(classtuple)
	
#循环语句
for x in classlist:
	print(x)
n=0
while n<5:
	print(classtuple)
	n+=1