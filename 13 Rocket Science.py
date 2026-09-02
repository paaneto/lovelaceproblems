from math import exp

v_e = 2550  # rocket exhaust velocity [m/s]
M = 250000  # rocket dry mass [kg]

def rocket_fuel(v):
    m_fuel = 0.0

    m_fuel = M*(exp(v/v_e)-1)
   
    return m_fuel

print(rocket_fuel(11186.0))