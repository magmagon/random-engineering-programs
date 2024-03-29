import numpy as np
import math
from scipy.optimize import fsolve

#BELOW IS AN EXAMPLE OF NONLINEAR EQUATION SOLVER

"""
def func1(x):
    return [ x[5] - x[4] - x[3],
            0 + x[0] - (0 + 156.6 - (0.00752 * (x[4]**2))),
            0 + x[1] - (0 + 117.1 - (0.00427 * (x[3]**2))),
            0 + (4636 * (x[2] - x[0])/(62.4 * 32.2)) + ((4.01* 0.00698 * 125 * (x[4]**2))/(32.2*(2.0667**5))),
            0 + (4636 * (x[2] - x[1])/(62.4 * 32.2)) + ((4.01 * 0.00698 * 125 * (x[3]**2))/(32.2*(1.278**5))),
            70 + (4636 * (0- x[2])/(62.4*32.2)) + ((4.01 * 0.00698 * 145 * (x[5]**2))/(32.2*(2.469**5)))
    ]

result = fsolve(func1, [1,2,3,4,5,6], xtol = 10e-6, maxfev=500)
print(result)
"""
"""
def func2(x):
    return [x[0] + x[1] - 3,
            ((x[2] * 0.09 * math.pi)/4) - x[0],
            ((x[3] * 0.2025 * math.pi)/4) - x[1],
            ((x[4] * (x[2]**2) * 500)/(9.81 * 0.3)) - ((x[5] * (x[3]**2) * 800)/(9.81*0.45)),
            ((876 * x[2] * 0.3)/0.2177) - x[6],
            ((876 * x[3] * 0.45)/0.2177) - x[7],
            (1.737 * (np.log((0.269* 0.000045/0.3) + (1.257/(x[6] * (x[4]**0.5)))))) + (1/(x[4]**0.5)),
            (1.737 * (np.log((0.269* 0.000045/0.45) + (1.257/(x[7] * (x[5]**0.5)))))) + (1/(x[5]**0.5)),
    ]
result = fsolve(func2, [10,10,5,5,0.0001,0.0001,69420,69420], xtol = 10e-06)
print(result) 
"""

def func(x):
    return [(8000*0.68) - (x[0]*998*9.81*7),
    x[1] - x[2] - 7,
    x[2] - x[3],
    x[2] - x[4],
    x[5] - ((4*x[7])/(math.pi * (0.03**2))),
    x[6] - ((4*x[8])/(math.pi * (0.05**2))),
    ((998 * x[5] * 0.03)/0.0011375) - x[9],
    ((998 * x[6] * 0.05)/0.0011375) - x[10],    
    (1.737 * (np.log((0.269* 0/0.3) + (1.257/(x[9] * (x[11]**0.5)))))) + (1/(x[11]**0.5)),
    (1.737 * (np.log((0.269* 0/0.45) + (1.257/(x[10] * (x[12]**0.5)))))) + (1/(x[12]**0.5)),
    x[0] - x[7] - x[8],
    ((x[11] * 25 * (x[5]**2))/(0.03 * 9.81)) - x[3],
    ((x[12] * 25 * (x[6]**2))/(0.03 * 9.81)) - x[4]
    ]
result = fsolve(func, [10,100,10,10,10,20,20,3,3,20000,20000,0.0001,0.0001], xtol = 10e-06)
print(result)
