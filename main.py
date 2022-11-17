from math import *
from numpy import arange
from sympy import diff
import sys


def dichotomy():
    a, b, f = float(input("enter a: ")), float(input("enter b: ")), str(input("enter f(x) : "))
    t = ""  # variable to check if you have "n" or not
    m = (a + b) / 2  # the starting value of the "middle"
    j = 0  # increasing variable to print aj's and bj's
    n = 0  # starting value of "n" to avoid error in line 39

    f1 = str(diff(f))  # f'(x)

    def function(x):
        return eval(f.replace("X", str(x)))  # f(x)

    def function1(x):
        return eval(f1.replace("X", str(x)))  # f'(x)

    if function(a) * function(b) > 0:  # condition 1
        print("change the interval of [" + str(a) + " , " + str(b) + "]")
        dichotomy()
    for xs in arange(a, b, 0.0001):  # condition 2
        if -0.01 < function1(xs) < 0.01:
            print("f(x) is not monotonic in [" + str(a) + " , " + str(b) + "]")
            dichotomy()

    while t != "n" and t != "ep":  # Loop to avoid unwanted values of "t"
        t = input("n or ep(epsilon) : ")
        if t == "n":
            n = int(input("enter n : "))
        elif t == "ep":
            ep = input("enter epsilon : ")
            ep = eval(str("pow(" + str(ep.replace("^", ",")) + ")"))  # calculating a^b
            n = ceil(log(((b - a) / (2 * ep)), exp(1)) / log(2, exp(1))) + 1  # finding n
            print("n = ", n)

    for i in range(n):  # main loop for calculating the answer
        print("\na" + str(j) + " = " + str(a) + " , " + "b" + str(j) + " = " + str(b))  # printing aj's and bj's

        if function(a) * function(m) < 0:
            b = m
            m = (a + b) / 2
        elif function(a) * function(m) > 0:
            a = m
            m = (a + b) / 2
        else:
            if function(a) == 0:
                m = a
            else:
                m = m
        j = j + 1  # aj's and bj's

    print("\n solution = " + str(m))
    return 0


def fixedpoint():
    a, b, g, x0 = float(input("\nenter a: ")), float(input("enter b: ")), input("enter g(x) : "), float(
        input("enter x0 : "))
    g1 = str(diff(g))  # g'(x)
    t = ""  # variable to check if you have "n" or not
    n = 0  # starting value of "n" to avoid error in line 87

    def function(x):
        return eval(g.replace("X", str(x)))  # g(x)

    def function1(x):
        return eval(g1.replace("X", str(x)))  # g'(x)

    for xvalues in arange(a, b, 0.0001):  # all the possible values of x from a to b
        if not a < function(xvalues) < b:  # if f [a,b] is in [a,b] 1st condition
            print("\nerror : g [" + str(a) + " , " + str(b) + "] is not in [" + str(a) + " , " + str(b) + "]")
            fixedpoint()

    def g1_positive_value(function1):
        for xvalues in arange(a, b, 0.0001):  # adding |g(x)| values to g1_p_values
            if function1(xvalues) > 0:
                yield function1(xvalues)
            else:
                yield -function1(xvalues)

    k = max(g1_positive_value(function1))  # max of g'(x)
    if not 0 < k < 1:  # condition 2
        print("error : k =", k)
        fixedpoint()
    x1 = function(x0)
    while t != "n" and t != "ep":  # Loop to avoid unwanted values of "t"
        t = input("n or ep(epsilon) : ")
        if t == "n":
            n = int(input("enter n : "))
        elif t == "ep":
            ep = input("enter epsilon : ")
            ep = eval(str("pow(" + str(ep.replace("^", ",")) + ")"))  # calculating a^b
            n = floor(log((ep * (1 - k)) / abs(x1 - x0), exp(1)) / log(k, exp(1))) + 1  # finding n
            print("n = ", n)
    for i in range(n):  # main loop for calculating the answer
        x1 = function(x0)
        print(f"xn({i+1}) = {x0}")
        x0 = x1
        print(f"xn+1({i + 1}) = {x0}\n")
    print(
        "1) g[" + str(a) + " , " + str(b) + "] ∈ [" + str(a) + " , " + str(b) + "]\n2) k = " + str(
            k) + "\n solution = " + str(
            x1))
    return 0


def newtonraphson():
    a, b, f, ep, x0 = float(input("\nenter a: ")), float(input("enter b: ")), input("enter f(x) : "), str(
        input("enter epsilon : ")), float(input("enter x0 : "))
    ep = eval(str("pow(" + str(ep.replace("^", ",")) + ")"))  # calculating a^b
    f1 = str(diff(f))  # f'
    f2 = str(diff(diff(f)))  # f"
    xn1 = x0
    xn = 100000000
    i = 0

    def function(x):
        return eval(f.replace("X", str(x)))  # f(x)

    def function1(x):
        return eval(f1.replace("X", str(x)))  # f'(x)

    def function2(x):
        return eval(f2.replace("X", str(x)))  # f"(x)

    print("f'(x) = " + str(f1) + "\nf\"(x) = " + str(f2))  # print the 2 derivatives
    if function(a) * function(b) > 0:  # 1st condition
        print(" error : f(a) * f(b) = " + str("f(") + str(a) + str(") * f(") + str(b) + str(") = ") + str(
            function(a) * function(b)) + str(" > 0"))
        newtonraphson()

    for xvalues in arange(a, b, 0.0001):  # all the possible values of x from a to b
        if -0.01 < function1(xvalues) < 0.01:  # if f'(x) = 0 2nd condition
            print("\nerror : f'(" + str(round(xvalues, 1)) + ") = 0 ")
            newtonraphson()
    for xvalues in arange(a, b, 0.001):  # test all the possible values
        if -0.01 < function2(xvalues) < 0.01:  # if f"(x) = 0 2nd condition
            print("\nerror : f\"(" + str(round(xvalues, 1)) + ") = 0 ")
            newtonraphson()

    if function(x0) * function2(x0) <= 0:  # 3rd condition
        print("error : f(x0) * f\"(x0) = " + str(function(x0) * function2(x0)) + " <= 0")
        newtonraphson()
    while abs(xn1 - xn) > ep:
        i += 1
        xn = xn1
        xn1 = xn - (function(xn) / function1(xn))
        print("\nxn(" + str(i) + ") = " + str(xn) + "\nxn+¹(" + str(i) + ") = " + str(xn1) + "\nⅼxn1 - xnⅼ = " + str(
            abs(xn1 - xn)))

    print("1) f(a) * f(b) = " + str(
        function(a) * function(
            b)) + " <= 0\n2) f'(x) and f\"(x) ‡ 0 and don't change their sign\n3) f(x0) * f\"(x0) = " + str(
        function(x0) * function2(x0)) + " > 0\nthe solution : " + str(xn1))
    sys.exit()


def secant():
    a, b, f, ep, x0, x1 = float(input("\nenter a: ")), float(input("enter b: ")), input("enter f(x) : "), str(
        input("enter epsilon : ")), float(input("enter x0 : ")), float(input("enter x1 : "))
    ep = eval(str("pow(" + str(ep.replace("^", ",")) + ")"))  # calculating a^b
    f1 = str(diff(f))  # f'
    f2 = str(diff(diff(f)))  # f"
    xn = x0  # first value of xnm1
    xnp1 = x1  # first value of xn
    i = 0  # counter

    def function(x):
        return eval(f.replace("X", str(x)))  # f(x)

    def function1(x):
        return eval(f1.replace("X", str(x)))  # f'(x)

    def function2(x):
        return eval(f2.replace("X", str(x)))  # f"(x)

    print("f'(x) = " + str(f1) + "\nf\"(x) = " + str(f2))  # print the 2 derivatives
    if function(a) * function(b) > 0:  # 1st condition
        print(" error : f(a) * f(b) = " + str("f(") + str(a) + str(") * f(") + str(b) + str(") = ") + str(
            function(a) * function(b)) + str(" > 0"))
        secant()
    for xvalues in arange(a, b, 0.0001):  # all the possible values of x from a to b
        if -0.01 < function1(xvalues) < 0.01:  # if f'(x) = 0 2nd condition
            print("\nerror : f'(" + str(round(xvalues, 1)) + ") = 0 ")
            secant()
    for xvalues in arange(a, b, 0.001):  # test all the possible values
        if -0.01 < function2(xvalues) < 0.01:  # if f"(x) = 0 2nd condition
            print("\nerror : f\"(" + str(round(xvalues, 1)) + ") = 0 ")
            secant()

    while abs(xnp1 - xn) > ep:  # main loop for calculating the answer
        xnm1 = xn  # first value of xnm1 line 168 + becoming xn
        xn = xnp1  # first value of xn line 169 + becoming xn+1
        i += 1  # just for printing the detailed answer
        xnp1 = xn - ((xn - xnm1) / (function(xn) - function(xnm1))) * function(xn)
        print("\nxn(" + str(i) + ") = " + str(xn) + "\nxn+¹(" + str(i) + ") = " + str(xnp1) + "\nⅼxn1 - xnⅼ = " + str(
            abs(xnp1 - xn)))
    print("\n1) f(a) * f(b) = " + str(
        function(a) * function(
            b)) + " <= 0\n2) f'(x) and f\"(x) ‡ 0 and don't change their sign\nthe solution : " + str(xnp1))

    return 0


choice = ""
while choice != "1" and choice != "2" and choice != "3" and choice != "4":
    choice = input("1)Dichotomy\n2)Fixed point\n3)Newton-Raphson\n4)Secant\n\nChoose a method : ")
    match choice:
        case "1":
            dichotomy()
        case "2":
            fixedpoint()
        case "3":
            newtonraphson()
        case "4":
            secant()
