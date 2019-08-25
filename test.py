#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("%s: 你好!您的话费余额为%.2f 元" %("张三",26.8))
age=int(input("请输入您的年龄："))
#判断体
if age >=18:
	print("adult")
elif age >=6:
	print("teenage")
else:
	print("kid")
#循环体
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum =sum + x 
print(sum )

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
#循环体
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum =sum + x 
print(sum )
