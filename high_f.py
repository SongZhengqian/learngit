#定义函数
def f(x):
	return x*x

#定义列表
l=[1,2,3,4,5,6,7,8,9]

r=map(f,l)
print(list(r))