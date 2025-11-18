import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data = np.loadtxt("marsh_stats.csv", delimiter=",", dtype=str)



x = data[1:,0].astype(np.float32)
y = data[1:,1].astype(np.float32)

print("y = ", y)
print("x = ", x)

params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

### EXCERCISE 1

print_equation(slope,intercept,'g','cm')

#The equation of the line is: y = -0.002478023766442128 cm/g x + 6.089514217566841 cm

###EXCERCISE 2

plt.figure()
plt.scatter(x, y, label='Data')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit')
plt.legend(loc='best')
plt.xlabel("grahms (g)")
plt.ylabel("distance in x direction (cm)")
plt.show()
