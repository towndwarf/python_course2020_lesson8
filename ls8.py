a = [1, 2, 3]
print(a)
b = a
print(b)

if a == b:
    print('T')

if a is b:
    print('is')

c = list(a)

if a == c:
    print('T c')

if a is not c:
    if type(a) == type(c):
        print(type(a), ' == ', type(c))
    else:
        print('whatever')