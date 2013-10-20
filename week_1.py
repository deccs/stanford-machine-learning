#!/usr/bin/python

import numpy as np
import time
import math

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
    total_cost = 0
    for training_item in x:
        total_cost += (hypothesis(theta_0, theta_1, x) - y)**2
    total_cost = float(total_cost)/(2*len(x))
    return total_cost

def gradient_descent(theta_0, theta_1, x, y, learning_rate):
    """
    For our univariate linear regression, the derivatives are given below
    """
    partial_deriv_0 = (float(1)/len(x))*sum([(hypothesis(theta_0, theta_1, x_val) - y_val) for x_val, y_val in zip(x,y)])
    partial_deriv_1 = (float(1)/len(x))*sum([((hypothesis(theta_0, theta_1, x_val) - y_val)*x_val) for x_val, y_val in zip(x,y)])
    print partial_deriv_0
    print partial_deriv_1
    ## Elementary attempt at breaking out of the recursion if we reach a minimum
    while math.fabs(partial_deriv_0) > float(theta_0+1) or math.fabs(partial_deriv_1) > float(theta_1 + 1):
        theta_0 = theta_0 - learning_rate * partial_deriv_0
        theta_1 = theta_1 - learning_rate * partial_deriv_1
        print "Intercept : ", theta_0
        print "Gradient : ", theta_1
        time.sleep(0.5)
        gradient_descent(theta_0, theta_1, x, y, learning_rate)

    return (theta_0, theta_1)
   
### An example calculation
## Let's see how quickly we can get a simple linear relationship
x = range(100)
y = [i*3 - 8 for i in range(10)]
z = gradient_descent(0, 0, x, y, 0.01)
print z
