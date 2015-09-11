# -*- coding: utf-8 -*-
# 递归函数
# 计算阶乘   n! = 1 * 2 * 3 * ... * n

def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

print fact(1)

print fact(5)

#使用递归函数要注意防止栈溢出，函数调用通过栈（stack）这种数据结构，
#进入一个函数调用，栈就会增加一层栈帧，每当函数返回，栈就会减一层栈帧
# 栈的大小不是无限的， 递归调用的次数过多，就会导致栈溢出
# 可以试试   fact(1000)

#解决递归调用栈溢出的方法是：尾递归

def fact(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)
