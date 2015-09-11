#list:列表，可以修改
#在命令行中操作
classmates = ['A', 'B', 'C']
classmates
len(classmates)   #3
classmates[0]
classmates[1]
classmates[2]
classmates[-1]
classmates.append('Adam')
classmates.insert(1, 'S')
classmates
classmates.pop()
classmates
classmates.pop(1)
classmates
classmates[1] = 'Sarah'
classmates


L = ['Apple', 123, True]

p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
p[1]
s[2][1]   #都可以得到'php'

L = []
len(L)


#tuple:元组，一旦初始化就不能修改
classmates = ('A', 'B', 'C')
classmates[0]
classmates[-1]
#可以索引，不能修改，没有append, insert这样的方法。

#   一个非常有意思的例子！    tuple可变？！
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
t
#('a', 'b', ['X', 'Y'])
# tuple 不可变的是每个元素的指向，指向一个list，就不能指向其他对象
#但这个list本身是可变的。
