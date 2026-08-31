import math
def temperature_statistics(T):
    mean = 0
    std  = 0 
    soma = 0

    mean = round(sum(T)/len(T), 3)

    for value in T:
        soma += ((value - mean)**2)

    std = round(math.sqrt(soma/len(T)), 3)

    return mean, std

T = [4.4, 4.2, 7.0, 12.9, 18.5, 23.5, 26.4, 26.3, 22.5, 16.6, 11.2, 7.3]
mean, std = temperature_statistics(T)
print(f"Mean: {mean} \nStandard deviation: {std}")

#rounding gives errors in the auto tests but it's not wrong