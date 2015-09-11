# -*- coding: utf-8 -*-
# h函数中设置默认参数
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s

power(5)

power(5, 3)
power(5, n=3)  #  多个可选变量时，必要时注明 n=

#设置默认参数需注意，必选参数在前，默认参数在后
# 默认参数必须指向不变对象！ 不能指向list



# 可变参数： 传入的参数个数是可变的。
# 在参数前加*， 就变成了可变参数，可以传入任意个参数，包括0个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc(1, 2)
calc()

#如果已经有一个list或者tuple, 允许在list或tuple前面加*号， 变成可变参数。
nums = [1, 2, 3]
calc(*nums)



#关键字参数， 允许传入0个或任意个含参数名的参数，这些关键字参数在函数内
#部自动组装为一个dict。

def person(name, age, **kw):
	print 'name:', name, 'age', age, 'other:', kw

person('Michael', 30)

person('Bob', 35, city = 'Beijing')

person('Adam', 45, gender='M', job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

#参数组合：参数定义的顺序必须是：必选参数，默认参数，可选参数，关键字参数
# *args 是可变参数， args接受的是一个tuple
# **kw 是关键字参数， kw接受的是一个dict
