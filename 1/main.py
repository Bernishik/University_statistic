import random
import matplotlib.pyplot as plt


# def M_rozp():
#     res = 0.0
#     for i in range(1,max+1):
#         res +=i
#     res /= max
#     return res

def build_diagram(min_v,max_v, values):
    names = [i for i in range(min_v,max_v+1)]
    fig, ax = plt.subplots(figsize=(4, 5))
    n, bin, patches = plt.hist(values,range=(1,6),bins=12)

    ax.spines['top'].set_visible(False)
    for rect in ax.patches:
        height = rect.get_height()
        ax.annotate(f'{int(height) if height> 0 else ""}', xy=(rect.get_x() + rect.get_width() / 2, height -0.9),
                    xytext=(0, 5), textcoords='offset points', ha='center', va='bottom')
    plt.show()

def find_M(values):
    result = 0

    for i in values:
        # print(f"{i} * {p_cube}")
        result += i / N
        # print(result)
    return result



if __name__ == '__main__':
    min = 1
    max = 6
    N = 1000
    p_cube = 1/max
    m_rozp = sum([i for i in range(0,max+1)]) *p_cube
    dispers = sum([((i-m_rozp)**2)  for i in range(1,max+1)]) * p_cube
    print(f"теоретичне математичне сподівання = {m_rozp}")
    print(f"теоретична дисперсія  = {dispers}")
    x_s = [(random.randint(min,max)) for i in range(0,N)]
    print(x_s)

    build_diagram(min,max,x_s)

    M_res =  find_M(x_s)
    D_res = sum([(xi - M_res)**2 for xi in x_s]) / len(x_s)


    print(f"Математичне сподівання з згенерованого масиву = {M_res}")
    print(f"Дисперсія з згенерованого масиву = {D_res}")


