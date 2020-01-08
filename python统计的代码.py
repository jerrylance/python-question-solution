# Some question
# Zeyu Liu
# 2019.1.2

from collections import Counter
a = [True,False,False,True,True]
b = Counter(a)
c = len(set(a))
print(b)
print(c)

# Using one line code to let the input a has a output [0,3,4]
print(a.count(len(set(a))),a.count(True), 2*a.count(False))