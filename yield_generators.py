my_list = [x * x for x in range(3)]
for i in my_list:
    print(i)
# 0
# 1
# 4

# ------------------------

my_generator = (x * x for x in range(3))
for i in my_generator:
    print(i)


# 0
# 1
# 4


# ------------------------

def create_generator():
    my_list1 = range(3)
    for i in my_list1:
        yield i * i


my_generator = create_generator()  # create a generator
print(my_generator)  # mygenerator is an object!
# <generator object createGenerator at 0xb7555c34>
for i in my_generator:
    print(i)
# 0
# 1
# 4
