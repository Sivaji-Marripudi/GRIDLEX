
def dexur(d,e,x,u,r):
    # pattern D
    for row in range(7):
        for col in range(7):
            if (row in {0,6} and col in {0,1,2,3,4,5}):
                D[row][col] = '#'
            elif (row in {1,2,3,4,5} and col in {0,6}):
                D[row][col] = '#'
            else:
                D[row][col] = ' '
    # pattern E
    for row in range(7):
        for col in range(7):
            if (row in {0,6} and col in {0,1,2,3,4,5,6}):
                E[row][col] = '#'
            elif (row in {1,2,4,5} and col == 0):
                E[row][col] = '#'
            elif (row == 3 and col in {0,1,2,3,4}):
                E[row][col] = '#'
            else:
                E[row][col] = ' '
    # pattern X
    i = 0
    j = 6
    for row in range(7):
        for col in range(7):
            if (row == i and col == j):
                X[row][col] = '#'
                i += 1
                j -= 1
            elif row == col:
                X[row][col] = '#'
            else:
                X[row][col] = ' '
    # pattern U
    for row in range(7):
        for col in range(7):
            if (row in {0,1,2,3,4,5} and col in {0,6}):
                U[row][col] = '#'
            elif (row == 6 and col in {1,2,3,4,5}):
                U[row][col] = '#'
            else:
                U[row][col] = ' '
    # pattern R
    for row in range(7):
        for col in range(7):
            if (row in {0,3} and col in {0,1,2,3,4,5}):
                R[row][col] = '#'
            elif (row in {1,2,6} and col in {0,6}):
                R[row][col] = '#'
            elif (row == 4 and col in {0,4}):
                R[row][col] = '#'
            elif (row == 5 and col in {0,5}):
                R[row][col] = '#'
            else:
                R[row][col] = ' '
    # nested 
    for i in range(7):
        for j in range(7):
            print(D[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(E[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(X[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(U[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(R[i][j],end='')
        print()

D = [[' ' for i in range(7)] for j in range(7)]
E = [[' ' for i in range(7)] for j in range(7)]
X = [[' ' for i in range(7)] for j in range(7)]
U = [[' ' for i in range(7)] for j in range(7)]
R = [[' ' for i in range(7)] for j in range(7)]

dexur(D,E,X,U,R)      