def div_weird(val: float, divisor: float) -> float:
    n = 0
    try:
        n = val/divisor
        print(':', n)

        if divisor == 1000.0:  # y != 0 or y != False or y != None):
            raise ValueError('מה אתה דפוק?')  # throw
        else:
            pass

    except Exception as e:
        print('inside exepti:', e)
        print('ex: ', n)
        n = 100

    finally:
        print('fin: ', n)

    return n


print('RESULT:', div_weird(112432.43, 0))
print('============sep===============')
print('RESULT:', div_weird(112432.43, 1000.0))
print('============sep===============')
print('RESULT:', div_weird(112432.43, 5243879.1))