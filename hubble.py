from matplotlib import pyplot as plt
import numpy as np
with open('Hubble.txt') as hubble:
	lines = hubble.readlines()

recessional_velocity = []
distance = []

for line in lines:
	w = line.split(' ')
	recessional_velocity.append(float(w[1]))
	distance.append(float(w[0]))
f, ax = plt.subplots(1)
x = np.array(distance)
y = np.array(recessional_velocity)
x = x[:,np.newaxis]
m, _, _, _ = np.linalg.lstsq(x, y, rcond=-1)

print(m)

plt.scatter(x,y)
plt.plot(x, m*x)
plt.xlabel('Distance(Mpc)')
plt.ylabel('Recessional velocity(km/s)')
plt.title("Hubble's Law")
ax.set_ylim(bottom=0)
ax.set_xlim(left=0)
plt.show()

