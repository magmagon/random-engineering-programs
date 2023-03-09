#Davis's iteration program

import math


#Input your knowns here, use 0 if not known
#Ensure your units are consistent!
g = 9.81
z = 27.43
density = 1000
viscosity = 0.001
length = 4827.8
#outer_diameter = 0.1
#thickness = 1
pressure = -206842
epsilon = 0.000045
q_dot = 0.03155
diameter = 0.154

#Place guesses here
re_g = 100
diameter_g = 0.25
pressure_g = 10

# some simple calculations
#diameter = outer_diameter - (2 * thickness)

rough = epsilon / diameter
iteration = 1

#formulas listed here
def friction (rough, re_g):
    ff = (-1.737 * math.log(abs((0.269 * rough) - ((2.185 / re_g) * math.log((0.269 * (rough)) + (14.5/re_g)))))) ** -2
    return ff

def vel (diameter, ff, density, length, pressure, g, z):
    velocity = math.sqrt(abs((diameter / (2 * ff * density * length)) * (pressure - (density * g * z))))
    return velocity

def vel2 (q_dot, diameter):
    velocity = (4*q_dot) / (math.pi * (diameter**2))
    return velocity

def reynolds (density, velocity, diameter, viscosity):
    re_new = (density * velocity * diameter) / viscosity
    return re_new

def qdot (diameter, velocity):
    q = math.pi * velocity * 0.25 * (diameter ** 2)
    return q


problem = str(input("What type of problem? enter d, p, or q "))
print("problem 1b")
if problem == "d":
    while(True):
        velocity = vel2(q_dot, diameter_g)
        re_new = reynolds(density, velocity, diameter_g, viscosity)
        roughness = epsilon / diameter_g
        ff = friction(roughness, diameter_g)
        diameter_new = ((32 * ff * density * (q_dot**2) * length) / (math.pi**2) * (pressure - (density * g * z))**0.2)

        vel_n = vel2(q_dot, diameter_new)
        ratio = vel_n/velocity
        if 0.9 <= ratio <= 1.1:
            diameter = diameter_new
            print("success" + str(iteration))
            print(diameter)
            break
        
        else:
            iteration = iteration + 1
            diameter_g = diameter_new
            print("iteration" + str(iteration))
        
        if iteration > 1000:
            break

if problem == "p":
    velocity = vel2(q_dot, diameter)
    re_new = reynolds(density, velocity, diameter, viscosity)
    roughness = epsilon / diameter
    ff = friction(roughness, re_new)
    pressure = ((2 * ff * density * (velocity**2) * length) / diameter) - (density * g * z)
    print("velocity, reynolds, roughness, friction, pressure")
    print(velocity, re_new, roughness, ff, pressure)

if problem == "q":
   
    while(True):

        ff = friction(rough, re_g)
        velocity = vel(diameter, ff, density, length, pressure, g, z)
        re_new = reynolds(density, velocity, diameter, viscosity)

        ratio = re_new / re_g
        if 0.9 <= ratio <= 1.1:
            q = qdot(diameter, velocity)
            print("success" + str(iteration))
            print(q)
            break
        
        else:
            iteration = iteration + 1
            re_g = re_new
            print("iteration" + str(iteration))
            print("reynolds" + str(re_new))
        
        if iteration > 1000:
            break