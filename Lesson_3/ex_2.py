amount = 0
multi = 1


def foo(*args, **kwargs):
    global amount, multi
    for arg in args:
        if isinstance(arg, (list, tuple)):
            foo(*arg)
        elif arg != 0:
            amount += arg
            multi *= arg
    for value in kwargs.values():
        if isinstance(value, (list, tuple)):
            foo(*value)
        elif value != 0:
            amount += value
            multi *= value
        return multi, amount


foo(3, 4, [2, 6, [9]], (8, 5), a=(10, 11, [0, 1], []))