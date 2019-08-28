
#定义数值
tex_rate=(0.03,0.1,0.2,0.25,0.3,0.35,0.45)
num=(0,210,1410,2660,4410,7160,15160)
#tex_class=()

#定义函数:计算个人所得税
def tex(x):
	if x<=3000:
		i=0
		print(x*tex_rate[i]-num[i])
	elif 3000<x<=12000:
		i=1
		print(x*tex_rate[i]-num[i])
	elif 12000<x<=25000:
		i=2
		print(x*tex_rate[i]-num[i])
	elif 25000<x<=35000:
		i=3
		print(x*tex_rate[i]-num[i])
	elif 35000<x<=55000:
		i=4
		print(x*tex_rate[i]-num[i])
	elif 55000<x<=80000:
		i=5
		print(x*tex_rate[i]-num[i])
	else:
		i=6
		print(x*tex_rate[i]-num[i])
		
#调用函数
money=int(input("请输入您的工资："))
tex(money)

input("Prease <enter>")