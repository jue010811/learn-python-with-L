# -*- coding: utf-8 -*-
# dict: 字典 ，使用key——value存储
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']

d['Adam'] = 67
print d['Adam']

#一个key只能对应一个value，多次对一个key放入多个value，前面的值会被冲掉
#如果key不存在，dict会报错
#为避免key不存在的错误，两种办法：
#1
'Thomas' in d
#2
d.get('Thomas')
d.get('Thomas', -1)
#其中-1为key不存在时自己指定的返回的value，不指定的话为None

#删除key
d.pop('Bob')
d

# key 应为不可变对象，list可变，不能作为key
#哈希算法： 通过key 计算位置的算法


#set : 也是一组key的集合，但是不储存value，key不能重复，
#重复元素在set中会被过滤

s = set([1, 2, 3])
print s

s.add(4)
print s

s.remove(4)
print s

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
#交集
s1 & s2
#并集
s1 | s2

s = set([1, [2, 3]])
#set只能放入不可变对象，将list放入set会报错
#TypeError: unhashable type: 'list'

#关于不可变对象的探讨
# str 是不变对象， list是可变对象

a = ['c', 'b', 'a']
a.sort()
a
#['a', 'b', 'c']

a = 'abc'
a.replace('a', 'A')
#'Abc'
a
#'abc'


#解释！replace是创建了一个新的字符串并返回。
# a是变量，  'abc'才是字符串

dict1 = {(1,2,3): 1, (2,3,4): 2}
set1 = set([(1, 2, 3), 2, 3])
# 可以实现

dict2 = {(1,[2,3]), 2, 3}
set2 = set([(1, [2, 3]), 2, 3])
#TypeError: unhashable type: 'list'
