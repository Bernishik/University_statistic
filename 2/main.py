# варіант 3
import math
from random import random
# import matplotlib.pyplot as plt


import plotly.graph_objects as go
xi = [2,3,5,12,21,33,44]
pi = [0.1,0.15,0.2,0.05,0.02,0.33,0.15]


def MathSpod(xs,ps):
    Mi = 0
    for i in range(len(xi)):
        Mi = Mi + xs[i] * ps[i]
    return Mi


def Dispers(xs,ps):
    Mi = MathSpod(xs,ps)
    Dis = 0
    for i in range(len(xi)):
        Dis = Dis +  xs[i] * xs[i] * ps[i]
    Dis = Dis - Mi * Mi
    return Dis

def find_M(values):
    result = 0

    for i in values:
        result += i / len(values)
    return result

def find_D(values,M_res):
    return sum([(xi - M_res) ** 2 for xi in values]) / len(values)


def delta1get(ps):
    result = []
    for i in range(len(ps)):
        if i ==0:
            result.append(ps[i])
        else:
            result.append(round(result[i-1] + ps[i],2))
    return result

def genList(random_list, deltas,xs):
    result =[]
    for item in random_list:
        for delta in enumerate(deltas):
            if item < delta[1]:
                result.append(xs[delta[0]])
                break
    return result

def genPseudoRandom(leng):
    return [random() for  i in range(leng)]

def chastPopad(values, deltas):
    result = [0 for i in range(len(deltas)-1)]
    for  value in values:
        for delta in enumerate(deltas):
            if value < delta[1]:
                result[delta[0]-1] = result[delta[0]-1] + 1
                break
    return result

def gen_intervals_task(values, a=2, b=44):
    L = 1 + 3.322 * math.log(len(values))

    deltaJ = (b - a) / L
    intervals = []
    intervals.append(0)
    intervals.append(round(deltaJ, 2))

    while intervals[-1] < b:
        intervals.append(round(deltaJ + intervals[-1], 2))
    return intervals

def gen_gist_task(values, intervals):


    rows = ['' for i in range(len(intervals) -1)]
    for val in enumerate(intervals):

        if len(intervals)-1 == val[0]:
            break
        rows[val[0]] = f"[{val[1]},{intervals[val[0] +1 ]})"


    ch_pop = chastPopad(values, intervals)

    del_null =[]
    for d in enumerate(ch_pop):
        if d[1] == 0:
            del_null.append(d[0])
    for v in reversed(del_null):
        rows.pop(v)
        ch_pop.pop(v)

    data = [go.Bar(
        x=rows,
        y=ch_pop
    )]
    fig = go.Figure(data=data)
    fig.show()

def gen_table_task(values, intervals, N):
    columns = ['Інтервал', 'Частота потрапляння', 'Відносна ЧП']
    rows =['' for i in range(len(intervals) -1)]
    rows[0] = f"[0,{intervals[0]})"
    for val in enumerate(intervals):
        if len(intervals)-1 == val[0]:
            break
        rows[val[0]] = f"[{val[1]},{intervals[val[0] +1 ]})"


    ch_pop = chastPopad(values, intervals)
    vid_ch_pop = [i / N for i in ch_pop]
    # del_null =[]
    # for d in enumerate(ch_pop):
    #     if d[1] == 0:
    #         del_null.append(d[0])
    # for v in reversed(del_null):
    #     rows.pop(v)
    #     ch_pop.pop(v)
    #     vid_ch_pop.pop(v)
    fig = go.Figure(data=[go.Table(header=dict(values=columns),
                                   cells=dict(values=[rows, ch_pop,vid_ch_pop]))
                          ])
    fig.show()
def task1(N):
    print()
    print("Завдання 1")
    print()
    print("Дано таблицю розподілу:")
    print(xi)
    print(pi)
    print()
    pseudo_list = genPseudoRandom(N)  # 100 1000 1000000
    print(f"Згенерований масив {pseudo_list}")
    delta1 = delta1get(pi)
    print(f"Згенеруємо інтервали {delta1}")
    gen_list = genList(pseudo_list, delta1, xi)
    print(f"Згенерований список на основі таблиці розподілу {gen_list}")
    M_diskr = MathSpod(xi, pi)
    print()
    print(f"Очікуване Математичне сподівання дискретної величини: {M_diskr}")
    print(f"Очікувана дисперсія дискретної величини: {Dispers(xi, pi)}")
    M = find_M(gen_list)
    print()
    print(f"Обраховане Математичне сподівання згенерованого масиву(розпод): {M}")
    print(f"Обрахована дисперсія згенерованого масиву(розпод): {find_D(gen_list, M)}")


    intervals = gen_intervals_task(gen_list)
    gen_table_task(gen_list, intervals, N)
    gen_gist_task(gen_list, intervals)




def task2_func(x):
    if x <0 or x > 4:
        raise Exception
    elif( x < 2):
        return 0.25 * x
    else:
        return 0.25

def task2(N):
    print()
    print("Завдання 2")
    a = 0
    b = 4
    M = 0.51
    rand_list = []
    counter = 0
    while counter < N:
        r1, r2 = random(), random()
        x0 = a + r1 * (b - a)
        n0 = r2 * M
        if n0 > task2_func(x0):
            rand_list.append(x0)
            counter = counter + 1
    print(rand_list)
    M = find_M(rand_list)
    print()
    print(f"Обраховане Математичне сподівання згенерованого масиву: {M}")
    print(f"Обрахована дисперсія згенерованого масиву: {find_D(rand_list, M)}")
    intervals = gen_intervals_task(rand_list, a, b)
    gen_table_task(rand_list, intervals, N)
    gen_gist_task(rand_list, intervals)

if __name__ == '__main__':
    task1(15)
    # task2(1000)




