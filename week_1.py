#!/usr/bin/python

import numpy as np
import time
import math
import matplotlib.pyplot as plt

def hypothesis(theta_0, theta_1, x):
    """
    Linear univariate hypothesis
    Think a straight line with itercept theta_0 and gradient theta_1
    """
    return theta_0 + (theta_1 * x)

def cost_function(theta_0, theta_1, x, y):
    """
    A squared error cost function
    Basically, the sum of the squared differences between the training points and the hypothesis, divided by the number of points.
    Kind of like an average of absolute distance of the points from the hypothesis
    """
    total_cost = (float(total_cost)/(2*len(x))) * sum([(hypothesis(theta_0, theta_1, x_val) - y_val)**2 for x_val, y_val in zip(x,y)])
    return total_cost

def gradient_descent(theta_0, theta_1, x, y, learning_rate):
    """
    For our univariate linear regression, the derivatives are given below
    """
    partial_deriv_0 = (float(1)/len(x))*sum([(hypothesis(theta_0, theta_1, x_val) - y_val) for x_val, y_val in zip(x,y)])
    partial_deriv_1 = (float(1)/len(x))*sum([((hypothesis(theta_0, theta_1, x_val) - y_val)*x_val) for x_val, y_val in zip(x,y)])

    ## Elementary attempt at breaking out of the recursion if we reach a minimum
    # Note - doesn't really work, will fix as the course progresses (I'd have thought)
    while math.fabs(partial_deriv_0) > math.fabs(float(theta_0+1)) or math.fabs(partial_deriv_1) > math.fabs(float(theta_1 + 1)):
        theta_0 = theta_0 - (learning_rate * partial_deriv_0)
        theta_1 = theta_1 - (learning_rate * partial_deriv_1)
        plt.plot(x, (x*int(theta_1)) + theta_0)
        plt.draw()
        time.sleep(1)

        gradient_descent(theta_0, theta_1, x, y, learning_rate)

    return (theta_0, theta_1)
   
### An example calculation
## Let's see how quickly we can get a simple linear relationship
x = np.arange(20)
y = [i*2 + 1 for i in np.arange(20)]
fig = plt.figure()
plt.axis([-10,10,0,10])
plt.ion()
plt.show()
plt.plot(x,y)
final_result_tuple = gradient_descent(0, 0, x, y, 0.01)
print final_result_tuple
