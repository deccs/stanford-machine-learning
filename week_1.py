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

    ## Elementary attempt at breaking out of the recursion if we reach a minimum
    # Note - doesn't really work, will fix as the course progresses (I'd have thought)
    if cost_function(theta_0, theta_1, x, y) > 0.003:
        theta_0 = theta_0 - (learning_rate * partial_deriv_0)
        theta_1 = theta_1 - (learning_rate * partial_deriv_1)
        #print "Intercept is now : ", theta_0
        #print "Gradient is now : ", theta_1
        plt.plot(x, (x*theta_1) + theta_0)
        if len(legend_list) > 4:
            del legend_list[1]
        legend_list.append("Error : " +  str(cost_function(theta_0, theta_1, x, y))[:6])
        plt.legend(legend_list, loc='upper center', fancybox=True)
        plt.draw()
        #time.sleep(1)

        return gradient_descent(theta_0, theta_1, x, y, learning_rate)
    else:
        return (theta_0, theta_1)
   
### An example calculation
## Let's see how quickly we can get a simple linear relationship
x = np.arange(-10, 10)
theta_0 = random.random()*-1 if int(str(datetime.datetime.now())[-1]) > 5 else random.random()
theta_1 = random.random()*-1 if int(str(datetime.datetime.now())[-1]) > 5 else random.random()
y = [i*theta_1 + theta_0 for i in x]
fig = plt.figure()
plt.axis([-2,2,-2,2])
plt.ion()
legend_list = ['Actual line']
plt.legend(legend_list, loc='upper center', fancybox=True)
plt.show()
plt.plot(x,y)
final_result_tuple = gradient_descent(random.random(), random.random(), x, y, float(len(x))/100)
print "Gradient was : ", theta_1
print "Intercept was : ", theta_0
print "Gradient guessed : ", final_result_tuple[1]
print "Intercept guessed : ", final_result_tuple[0]
