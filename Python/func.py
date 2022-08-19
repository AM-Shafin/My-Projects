from unittest import result


def myfnc(x, y=10, z=0):
    print("x =", x, "y =", y, "z =", z)

x,y,z = 4,5,6
myfnc(x, y, z)
myfnc(x, y)
myfnc(x)
print("\n\n\n")