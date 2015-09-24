# -*- coding: utf-8 -*-
#列表生成器

L = ['Hello', 'World', 18, 'Apple', None ]
v = [s.lower() for s in L if isinstance(s, str)]
print v
