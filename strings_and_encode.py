# -*- coding: utf-8 -*-
print 'I\'m ok.'
print 'I\' m learning\n python.'
print '\\\n\\'
print '\\\t\\'
print r'\\\t\\'
print '''line1
line2
line3'''
print r'''\tnew\n
\t\t\\\''''
print u'我爱你'

print ord('A')   #65
print chr(65)    #A

#需要在命令行中输入
u'ABC'.encode('utf-8')
u'中文'.encode('utf-8')
len('ABC')
'abc'.decode('utf-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'%2d-%02d' % (3, 1)
'%.2f' % 3.1415926
'growth rate: %d %%' % 7
