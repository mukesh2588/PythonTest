k = {4, 6, 7, 123, 999, 456}
print(k)
print(type(k))
d = {}
print(type(d))
e = set()
print(e)
s = set([345, 6667, 435, 90])
print(s)
t = [1, 4, 2, 1, 7, 9, 7]
print(set(t))


#adding
k={82,65}
print(k)
d={}
print(type(d))
k.add(88)
print(k)
# to add multiple elements
k.update([34,55,11,245])
print(k)
# subscripting the set not possible
# print(k[1])
k.remove(11)
print(k)