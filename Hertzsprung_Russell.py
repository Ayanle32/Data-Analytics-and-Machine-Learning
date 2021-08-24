from matplotlib import pyplot as plt 
import numpy as np


with open('stars.txt') as stars:
	lines = stars.readlines()

temp = []
absolute_magnitude = []

for line in lines:
    w = line.split(' ')
    temp.append(float(w[0]))
    absolute_magnitude.append(float(w[1]))
    
plt.scatter(temp,absolute_magnitude)
plt.xlabel('Temperature (K)')
plt.ylabel('Absolute Magnitude')
plt.xlim(0,13000)
plt.ylim(-5,20)
plt.show()
