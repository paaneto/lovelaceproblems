from math import sqrt

def habitable_exoplanet(L, r):
    habitability = ''
    innerradius = 0
    outerradius = 0

    innerradius = sqrt(L/1.1)
    outerradius = sqrt(L/0.54)

    if r > outerradius:
        habitability += "too cold"
    elif r < innerradius:
        habitability += "too hot"
    else:
        habitability += "just right"

    return habitability

print(habitable_exoplanet(1.11, 1.04))