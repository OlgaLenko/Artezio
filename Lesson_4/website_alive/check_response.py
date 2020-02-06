import make_request


def check_re(c):
    if make_request.make_re(c) == 200:
        return True
    else:
        return False
