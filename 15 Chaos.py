def logistic_map(r:float):
    x = [0.5]
    xn = 0

    for i in range(50):

        xn = r*x[i]*(1 - x[i])
        x.append(xn)
        
    return x

print(logistic_map(2.81))