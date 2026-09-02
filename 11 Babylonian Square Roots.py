def babylonian_sqrt(S):
    xn = S/2
    if xn == 0:
        return 0
    xn1 = 0

    for i in range(1000):
        xn1 = (1/2)*(xn +(S/xn))
        xn = xn1

    return xn

print(babylonian_sqrt(420))
#output 20.493901531919196