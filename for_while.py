# -*- coding: utf-8 -*- 
# for 循环 格式：  for   x     in    ...  
#注意这里的x可以为任意之前没有出现过的变量名， 不需要提前声明
names = ['A', 'B', 'C']
for name in names:
	print name

print range(5)
# [0, 1, 2, 3, 4, 5]

sum = 0
for x in range(101):
	sum = sum + x
print sum

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print sum

# raw_input() 读取的内容永远以字符串的形式返回，
#如果需要整数可以用int(raw_input())得到一个整形
