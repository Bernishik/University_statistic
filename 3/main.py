# варіант 3
import math
from random import random
# import matplotlib.pyplot as plt
N = 100






#
# from math import factorial, exp  # probability of 5 defects in an area
#
#     x = 5
#     miu = 2.5
#     poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
#     print(" % .3f" % poisson_prob)  # Answer = 0.067

def poisson_arr(lenth:int):
    # пуасон
    lamda = 3
    p = 0.1
    n = lamda / p
    result =[]
    for z in range(lenth):
        k = 0
        for i in range(int(n)):
            ri = random()
            if ri <= p:
                k = k + 1
        result.append(k)
    return result

def pokaznic_rand(lenth:int):
    #показник
    lamda= 3/ 10
    result = []
    for z in range(lenth):
        ri = random()
        x = -(math.log(ri)/lamda)
        result.append(x)
    return result

def normal_rand(lenth:int):
    #нормальне
    m = 3
    omega = 3
    result = []
    for z in range(lenth):
        datchic = [random() for i in range(12)]
        x =0
        rk = 0
        for i in datchic:
            rk = rk+ i
        x = m  + omega *(rk -6 )
        result.append(x)
    return result
if __name__ == '__main__':
    # print(poisson_arr(12)) # пуасон
    print(pokaznic_rand(1)) # показникове
    # print(normal_rand(10)) # нормальне




