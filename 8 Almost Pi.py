def almost_pi(N):
    nearpi = 0
    for i in range(N):
        nearpi += (((-1)**i)/((2*i)+1))
    nearpi = 4*nearpi
    return nearpi

print(almost_pi(25))
