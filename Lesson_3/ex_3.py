number = 0


def foo(a, b, c, d):
    result1 = (a + b + c + d) / 4
    result2 = max(a, b, c, d)
    global number
    if number < result2:
        number = result2
    return result1, number


foo(1, 2, 3, 4)
foo(-3, -2, 10, 1)
foo(7, 8, 8, 1)
