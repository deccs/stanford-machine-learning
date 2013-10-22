#!/usr/bin/python

import numpy as np
import time
import math
import random
import matplotlib.pyplot as plt
import datetime

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
    total_cost = (float(1))/(2*len(x)) * sum([(hypothesis(theta_0, theta_1, x_val) - y_val)**2 for x_val, y_val in zip(x,y)])
    return total_cost

def gradient_descent(theta_0, theta_1, x, y, learning_rate):
    """
    For our univariate linear regression, the derivatives are given below
    """
    partial_deriv_0 = (float(1)/len(x))*sum([(hypothesis(theta_0, theta_1, x_val) - y_val) for x_val, y_val in zip(x,y)])
    partial_deriv_1 = (float(1)/len(x))*sum([((hypothesis(theta_0, theta_1, x_val) - y_val)*x_val) for x_val, y_val in zip(x,y)])

    ## How accurate does the prediction need to be - change the maximum acceptable cost function value here to determine
    if cost_function(theta_0, theta_1, x, y) > 0.003:
        theta_0 = theta_0 - (learning_rate * partial_deriv_0)
        theta_1 = theta_1 - (learning_rate * partial_deriv_1)
        plt.plot(x, x*float(theta_1) + theta_0)
        ## Working with limited space legend so only keep the last 5
        if len(legend_list) > 4:
            ## We want to leave the original line legend
            del legend_list[1]
        legend_list.append("Error : " +  str(cost_function(theta_0, theta_1, x, y))[:6])
        plt.legend(legend_list, loc='upper center', fancybox=True)
        plt.draw()

        return gradient_descent(theta_0, theta_1, x, y, learning_rate)
    else:
        return (theta_0, theta_1)
   
### An example calculation
## Let's see how quickly we can get a simple linear relationship
################################################################

## Random values for the intercept and gradient
theta_0 = -1*random.random() if int(str(datetime.datetime.now())[-1]) > 4 else random.random()
theta_1 = -1*random.random() if int(str(datetime.datetime.now())[-1]) > 4 else random.random()

## Initialize the training examples
x = np.arange(-10, 10)
y = [i*theta_1 + theta_0 for i in x]

## Plotting initialization
fig = plt.figure()
plt.axis([-2,2,-2,2])
plt.ion()
legend_list = ['Actual line']
plt.legend(legend_list, loc='upper center', fancybox=True)
plt.show()
plt.plot(x,y)

## Experimentally verified as being reasonable - will likely change in future iterations

learning_rate = float(1)/20

# Generate result
final_result_tuple = gradient_descent(random.random(), random.random(), x, y, learning_rate)
print "Gradient was : ", theta_1
print "Intercept was : ", theta_0
print "Gradient guessed : ", final_result_tuple[1]
print "Intercept guessed : ", final_result_tuple[0]
