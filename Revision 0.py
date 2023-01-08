import numpy as np
import matplotlib.pyplot as plt

## Variables
angle = np.deg2rad(23)      ## launch angle in degrees
g = 9.81                    ## gravity
u = 18.775                  ## initial velocity (x and y components follow)
ux = 17.277
uy = 7.345
sy = 2.75                   ## height of target (2.5 - 3 meters)
hSpread = 22                ## horizontal spread in degrees

## Revision 0
## calculate motion of projectile (equation)
xvals = []
yvals = []

def f(t):
    return uy * t - (0.5 * g * t**2)

for t in np.arange(0, 10, 0.01):
    x = ux * t
    y = f(t)
    if y < 0:
        continue

    xvals.append(x)
    yvals.append(y)


## plot 1
plt.plot(xvals, yvals, 'r', label='Projectile Motion')
plt.axhline(y=sy, color='b', linestyle="dotted", label='Max Height')
plt.xlabel('Distance X (m)')
plt.xticks(np.arange(0, 30, 2))
plt.ylabel('Distance Y (m)')
plt.yticks(np.arange(0, 3, .25))
plt.title('Clay Target Motion')

xvals = xvals[20:len(xvals)-20]
yvals = yvals[20:len(yvals)-20]

plt.plot(xvals, yvals, 'b', label='Truncated Area', linewidth=2)

plt.legend()
plt.grid()
plt.show()
