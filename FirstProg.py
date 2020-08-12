#import sys
#print(sys.path)

listl1=[ 2 ** x for x in range(10) ]
print(listl1)

liststr = ['p', 'y', 't', 'p', 'o', 'n']
print(liststr[2])
# append
liststr.append(8)
print(liststr)
liststr.extend([4, 5, 6])

liststr1 = ['s', 'k', 'i', 'l', 'l']
print(liststr + liststr1)
liststr.insert(3, 'h')
print(liststr)
liststr.remove('p')
print(liststr)

liststr.extend("hyderabad")
print(liststr)

list2 = []
for x in range(10):
    list2.append(2 ** x)
    print(list2)
list2 = [2 ** x for x in range(10)]
print(list2)

print('p' in liststr)
for i in [1, 4, 5, 6]:
    print(i)












