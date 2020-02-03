def sq_elements(*args):
    result = [arg**2 for arg in args]
    return result


def even_elements(*args):
    result = []
    for i in range(1, len(args), 2):
        result.append(args[i])
    return result


def cube(*args):
    result = []
    for i in range(0, len(args), 2):
        for arg in args:
            if arg % 2 == 0 and i < len(args)-1:
                result.append(args[i]**3)
                i += 2
        else:
            break
    return result


# def cube(*args):
    # result = []
    # elements = dict((index, arg) for index, arg in enumerate(args))
    # for index, arg in elements.items():
        # if index % 2 == 0:
            # index += 1
        # else:
            # if arg % 2 != 0:
                # index += 2
            # else:
                # result.append(elements[index]**3)
    # return result


args = [1, 2, 11, 48, 43, 4, -8, 1236]
sq_elements(*args)
even_elements(14, 7, 0, 123, 6, 15, 1, 1, 652)
cube(1, 18, 4, 2, -20, -5, 0, 0, 3)