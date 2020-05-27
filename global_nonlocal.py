def fun1():
    # city
    # print(city)
    city = 'Jerusalem'
    print('fun1: ', city)


def fun2():
    global city
    print('fun2: ', city)
    city = 'Jerusalem'
    print('fun2 - changed: ', city)
    print('----------separator-----------')


def fun3():
    city = 'Tel Aviv'

    def fun4():
        nonlocal city
        print('fun3: ', city)
        city = 'Jerusalem'
        print('fun3: ', city)

    fun4()


city = 'Ariel'
print('Global:', city)
fun1()
print('Global:', city)
fun2()
print('Global:', city)
fun3()
print('Global:', city)
