perms = list()
total = 0

def con(o, co):
    return [o[i:i+co] for i in range(0, len(o), co)]

def y(e, f):
    if len(e) % 2 == 1: 
        e = e[:-1]  


    g = []
    while len(g) < len(e)*2:
        for c in f:
            g.append(c)

    g = g[:len(e)*2]
    k = 0

    j = list()
    for l in range(len(e)):
        if k < len(e):  
            j.append(ord(e[k]) ^ ord(g[k*2]))
            k += 1
    print(j)
    p = []
    new = con(j, 2)
    q, r, s, t = 0, len(new[0]), len(new), 0
    while q < r and t < s:
        for u in range(q, r):
            p.append(new[t][u])
        t += 1
        for v in range(t, s):
            p.append(new[v][r - 1])
        r -= 1
        if not (q < r and t < s):
            break
        for w in range(r - 1, q - 1, -1):
            p.append(new[s - 1][w])
        s -= 1
        for x in range(s - 1, t - 1, -1):
            p.append(new[x][q])
        q += 1

    z = list()
    for y in p:
        y = y % 52
        if y < 26:
            y = 65 + y  
        else:
            y = 97 + (y - 26)  
        z.append(chr(y))
    with open("output.txt", "w") as file:
        file.write("".join(z))

with open("input.txt", 'r') as file:
    e = file.read()
    f = "thisshitsasecret"
    y(e, f)
