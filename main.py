def nwp(x, y):
    m = len(x)
    n = len(y)
    L = [[None] * (n + 1) for i in range(m + 1)]

    for i in range(m+1):
        L[i][0] = 0

    for j in range(n+1):
        L[0][j] = 0

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                L[i+1][j+1] = 1+L[i][j]
            else:
                L[i+1][j+1] = max(L[i+1][j], L[i][j+1])

    NWP = ""
    i = m-1
    j = n-1
    while i >= 0 and j >= 0:
        if x[i] == y[j]:
            NWP = x[i]+NWP
            i = i-1
            j = j-1
        elif L[i+1][j] > L[i][j+1]:
            j = j-1
        else:
            i = i-1

    return "NWP: "+NWP + ", o długości " + str(L[m][n])


x = input("First string : ")
y = input("Second string: ")
print(nwp(x, y))
