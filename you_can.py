import math
import matplotlib.pyplot as plt


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Defining bracketing :
def bracketing(a, b, func):
    i = 0
    while i < 12:  # Limiting no.of iterations to 12
        if func(a) * func(b) < 0:
            print("The bracketing has been done properly it required " + str(i) + " iterations")
            break
        elif func(a) * func(b) == 0:
            if func(a) == 0:
                print("{} is the root of the nonlinear equation.".format(a))
            if func(b) == 0:
                print("{} is the root of the nonlinear equation.".format(b))
        elif func(a) * func(b) > 0:
            if abs(func(a)) < abs(func(b)):
                a = a - 1.5 * (b - a)
            else:
                b = b + 1.5 * (b - a)
        i += 1
    if i > 12:
        print("It took more than 12 iterations to bracket the root! Please choose new points.")
    else:
        return a, b


# Defining the bisection method
def bisection(a, b, func):
    file_1 = open('Q1_itr(bisection).txt', 'w')
    a, b = bracketing(a, b, func)  # Recalling the function
    i = 1
    print(color.BOLD + "Bisection method" + color.END)
    file_1.write(color.BOLD + "Bisection method" + color.END + "\n{:>3}       {:>10} ".format("Iterations",
                                                                                              "Absolute error") + "\n")
    while abs(a - b) > 0.000001 and i < 200:  # Limiting no.of iterations to 12
        c = (a + b) / 2
        if func(a) * func(c) < 0:
            file_1.write("{:>3}         {:>10.20f} ".format(i, abs(c - b)) + "\n")
            b = c
        elif func(a) * func(c) > 0:
            file_1.write("{:>3}         {:>10.20f} ".format(i, abs(c - a)) + "\n")
            a = c
        else:
            print("While iterating through the points one of the point has landed on the root of the equation.")
            print(a, b)
            break
        i += 1
    return "The root has been found to be at " + str(b) + " and it required " + str(i - 1) + " iterations" \
                                                                                             "\n_________________________________________________________________________________."

# Defining regular falsi method
def regular_falsi(a, b, func):
    file_2 = open('Q1_itr(regular_falsi).txt', 'w')
    bracketing(a, b, func)
    i = 1
    print(color.BOLD + "False Position method." + color.END)
    file_2.write(color.BOLD + "False Position method." + color.END + "\n{:>3}       {:>10} ".format("Iterations",
                                                                                                    "Absolute error") + "\n")
    c = 1
    c_n1 = a
    while abs(c - c_n1) > 0.000001 and i < 200:  # Limiting no.of iterations to 200
        c = b - ((b - a) * func(b)) / (func(b) - func(a))
        if func(a) * func(c) < 0:
            c_n1 = b
            file_2.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
            b = c
        elif func(a) * func(c) > 0:
            c_n1 = a
            file_2.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
            a = c
        else:
            if func(a) == 0:
                print(a, " is the root.")
            elif func(b) == 0:
                print(b, " is the root.")
        i += 1
    file_2.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
    return "The root has been found to be at " + str(c) + " and it required " + str(i) + " iterations." \
            "\n_________________________________________________________________________________. "

# Defining newton raphson method
def newton_raphson(x_o, func):
    file_3 = open('Q1_itr(Newton_Raphson).txt', 'w')
    h = 0.01
    der = (func(x_o+h) - func(x_o-h))/(2*h)  # Derivative of the function
    x = x_o - (func(x_o) / der)
    copy = 1
    i = 1
    print(color.BOLD + "Newton-Raphson method." + color.END)
    file_3.write(color.BOLD + "Newton-Raphson method." + color.END + "\n{:>3}       {:>10} ".format("Iterations",
                                                                                                    "Absolute error") + "\n")
    while abs(x - copy) > 0.000001 and i < 200:  # Limiting no.of iterations to 200
        copy = x
        x_o = x
        der = (func(x_o + h) - func(x_o - h)) / (2 * h)
        x = x_o - (func(x_o) / der)
        file_3.write("{:>3}         {:>10.20f} ".format(i, abs(x - copy)) + "\n")
        i += 1
    file_3.write("{:>3}         {:>10.20f} ".format(i, abs(x - copy)) + "\n")
    return "The root has been found to be at " + str(x) + " and it required " + str(i) + " iterations."
