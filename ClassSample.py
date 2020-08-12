class MK:
    "class example"
    a=12

    def fun(self):
        print('this is a function')

ob=MK()
print(MK.a)
print(ob.a)
print(ob.fun())

print(MK.__doc__)