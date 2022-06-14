# 2.14: Divide by x
'''
user_num = int(input())
x = int(input())

place = user_num//x
print(str(place), end=' ')
place = place//x
print(str(place), end=' ')
place = place//x
print(str(place))
'''
###########################################################

# 2.15: Driving Costs 
'''
miles_gallon = float(input())
dollars_gallon = float(input())
your_value1 = 20*dollars_gallon/miles_gallon
your_value2 = 75*dollars_gallon/miles_gallon
your_value3 = 500*dollars_gallon/miles_gallon

print('{:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3))
'''
###########################################################
'''
# 2.16: Using math Functions

import math

x = float(input())
y = float(input())
z = float(input())

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(math.pow(x, z), math.pow(x, math.pow(y, z)), math.fabs(x - y), math.sqrt(math.pow(x, z))))
'''

###########################################################

# 2.17: Building Height Calculator
'''
# The Height of Building Calculator program
import math
print("The Height of Building Calculator program\n")

#collect user input
distance= float(input("Enter your distance from the building(feet): "))
angle = float(input("\nEnter angle for line of sight to top of building (degrees): "))
your_height = float(input("\nEnter your height (feet): "))

#calculate the height of a building expression goes here
angle_rad = angle*math.pi/180
building_height = math.tan(angle_rad) * distance + your_height

#format and output result
building_height = int(round(building_height,0))
print("\n\nHeight of building:\t",building_height)
print()
print("Bye")

'''
###########################################################

# 2.18: Acreage calculator
'''
sq_ft = int(input('Enter the square feet of the area to convert to acres:'))
ACRE_FACTOR = int(43560)
acre = sq_ft/ACRE_FACTOR
print('{} square feet is equal to {:.2f} acres.'.format(sq_ft, acre))
'''
###########################################################

# 2.19: Pay raise calculator
'''
name = str(input('Enter your name: '))
print()
sal = int(input('Enter your current annual salary: $'))
print()
PAY_RAISE = float(1.076)

print('Retroactive pay due {} is ${:.2f}'.format(name,sal / 2 * (PAY_RAISE-1)))
print("{}'s new annual salary is ${:.2f}".format(name, sal * PAY_RAISE))
print('New monthly salary is ${:.2f}'.format(sal * PAY_RAISE / 12))
'''