
def chastPopad(xs,values):
    result = [0 for i in range(len(xs))]
    for val in values:
        for x in enumerate(xs):
            if val == x[1]:
                result[x[0]] = result[x[0]]+1
                break
    return result

def gen_table_task1(xs,delta,values,N):
    columns = ['Інтервал', 'Частота потрапляння', 'Відносна ЧП']
    rows =['' for i in delta]
    rows[0] = f"[0,{delta[0]})"
    for val in enumerate(delta):
        if val[0] == len(delta)-1:
            pass
        else:
            rows[val[0]+1] = f"[{val[1]},{delta[val[0]+1]})"
    # rows = xi # по х


    ch_pop = chastPopad(xs, values)
    vid_ch_pop = [i / N for i in ch_pop]
    fig = go.Figure(data=[go.Table(header=dict(values=columns),
                                   cells=dict(values=[rows, ch_pop,vid_ch_pop]))
                          ])
    fig.show()

def gen_gist_task1(delta,values):
    rows = ['' for i in delta]
    rows[0] = f"[0,{delta[0]})"
    for val in enumerate(delta):
        if val[0] == len(delta) - 1:
            pass
        else:
            rows[val[0] + 1] = f"[{val[1]},{delta[val[0] + 1]})"

    ch_pop = chastPopad(xi, values)
    # rows = xi #по х
    data = [go.Bar(
        x=rows,
        y=ch_pop
    )]
    fig = go.Figure(data=data)
    fig.show()
def chastPopad(xs,values):
    result = [0 for i in range(len(xs))]
    for val in values:
        for x in enumerate(xs):
            if val == x[1]:
                result[x[0]] = result[x[0]]+1
                break
    return result