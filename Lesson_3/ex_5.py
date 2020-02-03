from math import fabs
def z():
    a=sorted(list(map(float,input().split())))
    if fabs(a[0])<fabs(a[1]):
        return a[0]
    return a[1]
z()