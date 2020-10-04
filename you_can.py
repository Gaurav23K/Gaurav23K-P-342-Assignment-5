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

# Defining the polynomial equation
def P(c, i, x):
    return ((c[0-i] * pow(x, 4))+(c[1-i] * pow(x, 3))+(c[2-i] * pow(x, 2))+(c[3-i] * pow(x, 1))+c[4-i])

# Defining first derivative
def P_1(P, c, i, x):
    h = 0.5
    s = (P(c, i, x+h) - P(c, i, x-h))/(2*h)
    return s

#Defining second derivative
def P_2(P, c, i, x):
    h = 0.5
    s = (P(c, i, x+h)+P(c, i, x-h)-2*P(c, i, x))/(2*h**2)
    return s


# Defining Laguerre method
def laguerre_Method(P, c, i, a0):
    e = len(c) - 1
    epsilon = math.pow(10, -4)
    if(P(c, i, a0) == 0):
        return a0
    else:
        for j in range(200):
            g = (P_1(P, c, i, a0)) / P(c, i, a0)
            h = (math.pow(g, 2)) - ((P_2(P, c, i, a0)) / P(c, i, a0))
            d1 = (g + math.sqrt(abs((e-i-1)*(( (e-i) * h ) - math.pow(g, 2)))))
            d2 = (g - math.sqrt(abs((e-i-1)*(( (e-i) * h) - math.pow(g, 2)))))
            if(abs(d1) > abs(d2)):
                a = (e-i) / d1
            else:
                a = (e-i) / d2
            a1 = a0 - a
            if(abs(a1 - a0) < epsilon):
                return a0
            a0 = a1


# Defining syntetic division method

def synthetic_Division(P, c, a0, r):
    for i in range(len(c) - 2):
        x1 = laguerre_Method(P, c, i, a0)
        for j in range(3 - i):
            c[j+1] = c[j+1] + (x1 * c[j])
        c[len(c) -1 - i] = 0
        r.append(x1)






#######################################  OTHER FUNCTIONS  ###################################


#Reading a Matrix from a file
def read_Matrix(fil , A):
    file = open(fil , 'r')
    for line in file:
        ns = line.split()
        no = [float(n) for n in ns]
        A.append(no)
    file.close()

#To print the Matrix
def write_Matrix(x):
    for r in range(len(x)):
        print(x[r])

#Factorial Method
def factorial(num):
    fact = 1
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            fact = fact * i
        return fact

#Function for partial pivoting the Augmented Matrix / Only Matrix
def partial_pivot(a, b):
    n= len(a)
    counter = 0
    for r in range(0 , n):
        if abs(a[r][r]) == 0:
            for r1 in range(r+1 , n):
                if abs(a[r1][r]) > abs(a[r][r]):
                    counter = counter + 1
                    for x in range(0,n):
                        d1= a[r][x]
                        a[r][x] = a[r1][x]
                        a[r1][x] = d1
                    if(b!= 0):
                         d1 = b[r]
                         b[r] = b[r1]
                         b[r1] = d1
    return counter

#Multiplication of Matrices
def matrix_Multiplication(a, b):
    m = len(b[0])
    l=len(b)
    n = len(a)
    p2 = [[0 for y in range(m)] for x in range(n)]
    for x in range(n):
        for i in range(m):
            for y in range(l):
                p2[x][i] = p2[x][i] + (a[x][y] * b[y][i])
    return p2

#Gauss-Jordan Method
def gauss_Jordan(a , b):
    n = len(a)
    bn = len(b[0])
    for r in range(0 , n):
        partial_pivot(a , b)
        pivot = a[r][r]
        for c in range(r , n):
            a[r][c] = a[r][c]/pivot
        for c in range(0 , bn):
            b[r][c] = b[r][c]/pivot
        for r1 in range(0, n):
            if r1==r or a[r1][r] == 0:
                continue
            else:
                factor = a[r1][r]
                for c in range(r , n):
                    a[r1][c] = a[r1][c] - factor*a[r][c]
                for c in range(0 , bn):
                    b[r1][c] = b[r1][c] - factor*b[r][c]

# Forward- Backward Substitution
def forwardbackward_Substitution(a, b):
    m = len(b[0])
    n = len(a)
    # forward substitution
    y = [[0 for y in range(m)] for x in range(n)]
    for i in range(n):
        for j in range(m):
            s = 0
            for k in range(i):
                s = s + a[i][k] * y[k][j]
            y[i][j] = b[i][j] - s
    # backward substitution
    x = [[0 for y in range(m)] for x in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            s = 0
            for k in range(i + 1, n):
                s = s + a[i][k] * x[k][j]
            x[i][j] = (y[i][j] - s) / a[i][i]

    return x

#L-U decomposition
def lu_Decomposition(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            s = 0
            if(i<=j):
                for k in range(i):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = a[i][j] - s
            else:
                for k in range(j):
                    s = s + (a[i][k] * a[k][j])
                a[i][j] = (a[i][j] - s) / a[j][j]

#Finding determinant of Upper Triangular Matrix
def uppertriangular_Determinant(a):
    n = len(a)
    p = 1
    for i in range(n-2):
        p = p * a[i][i]
    p = p * (a[n-2][n-2] * a[n-1][n-1])
    return p