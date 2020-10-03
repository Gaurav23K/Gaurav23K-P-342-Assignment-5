'''
Assignment: 5
Q1(a): f(x) = log(x) - Sin(x)
Q2(b): f(x) = -x - Cos(x)
'''
import math
import matplotlib.pyplot as plt
import you_can


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Asking user for the desired equation from question 1.
Question = input("For question 1 which part would you like to solve?[Please give input as 'a' or 'b'.]\n")


def func_a(x):
    y = math.log(x) - math.sin(x)  # first equation
    return y
def func_b(x):
    z = -x - math.cos(x)  # second equation
    return z


if Question == 'a':
    x = [i for i in range(1, 20)]
    y = [(math.log(i) - math.sin(i)) for i in x]
# Plotting the graph of the first function(log(x) - sin(x))
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.grid()
    plt.title(" f(x) = log(x) - Sin(x)")
    plt.xlabel("x -->")
    plt.ylabel("f(x) -->")
    plt.show()

    print(you_can.bisection(1.5, 2.5, func_a))
    print(you_can.regular_falsi(1.5, 2.5, func_a))
    print(you_can.newton_raphson(1.5, func_a))
elif Question == 'b':
    x = [i for i in range(-2, 10)]
    y = [(-i - math.cos(i)) for i in x]
# Plotting the graph of the second function(-x-cos(x))
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.grid()
    plt.title(" f(x) = - x - Cos(x)")
    plt.xlabel("x -->")
    plt.ylabel("f(x) -->")
    plt.show()

    print(you_can.bisection(1.5, 2.5, func_b))
    print(you_can.regular_falsi(1.5, 2.5, func_b))
    print(you_can.newton_raphson(2.5, func_b))
else:
    print("Please follow the instructions carefully and give an appropriate input.")

'''
Q1(a):
Bisection method--> Position of root: 2.2191076278686523 ; no.of iteration = 20
Regular falsi method--> Position of root: 2.2191071418525734 ; no.of iteration = 8
Netwton Raphson method--> Position of root: 2.219107148913746 ; no.of iteration = 5
****************************************************************************************
Q1(b):
Bisection method--> Position of root: -0.739084780216217 ; no.of iteration = 23
Regular falsi method--> Position of root: -0.7390851319823046 ; no.of iteration = 10
Netwton Raphson method--> Position of root: -0.7390850544025488 ; no.of iteration = 5
'''