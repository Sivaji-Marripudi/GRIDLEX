
def gridlex(g,r,i,d,l,e,x):
        # pattern G
        for row in range(6):
            for col in range(6):
                if ((row in {0,5}) and (col in {1,2,3,4})):
                    G[row][col] = '#'

                elif ((row in {1,4}) and (col in {0,5})) :
                    G[row][col] = '#'

                elif ((row == 2) and (col == 0)):
                    G[row][col] = '#'

                elif ((row == 3 and (col not in {1,2}))):
                    G[row][col] = '#'
                else:
                    G[row][col] = ' '
        # pattern R
        for row in range(6):
            for col in range(6):
                if (row in {0,3} and col in {0,1,2,3,4}):
                    R[row][col] = '#'
                elif (row in {1,2,5} and col in {0,5}):
                    R[row][col] = '#'
                elif (row == 4 and col in {0,4}):
                    R[row][col] = '#'
                else:
                    R[row][col] = ' '
        # pattern I
        for row in range(6):
            for col in range(6):
                if (row in {0,1,2,3,4,5} and col == 2):
                    I[row][col] = '#'
                else:
                    I[row][col] = ' '
        # pattern D
        for row in range(6):
            for col in range(6):
                if (row in {0,5} and col in {0,1,2,3,4}):
                    D[row][col] = '#'
                elif (row in {1,2,3,4} and col in {0,5}):
                    D[row][col] = '#'
                else:
                    D[row][col] = ' '
        # pattern L
        for row in range(6):
            for col in range(6):
                if (row in {0,1,2,3,4} and col == 0):
                    L[row][col] = '#'
                elif (row == 5) and col in {0,1,2,3,4,5}:
                    L[row][col] = '#'
                else:
                    L[row][col] = ' '
        # pattern E
        for row in range(6):
            for col in range(6):
                if (row in {0,5} and col in {0,1,2,3,4,5}):
                    E[row][col] = '#'
                elif (row in {1,3,4} and col == 0):
                    E[row][col] = '#'
                elif (row in {2} and col in {0,1,2,3,4}):
                    E[row][col] = '#'
                else:
                    E[row][col] = ' '
        # pattern X
        i = 0
        j = 5
        for row in range(6):
            for col in range(6):
                if (row == i and col == j):
                    X[row][col] = '#'
                    i += 1
                    j -= 1
                elif row == col:
                    X[row][col] = '#'
                else:
                    X[row][col] = ' '
        # nested list
        for i in range(6):
            for j in range(6):
                print(G[i][j],end='')
            print(end=' ')
            for j in range(6):
                print(R[i][j],end='')
            print(end=' ')
            for j in range(6):
                print(I[i][j],end='')
            print(end=' ')
            for j in range(6):
                print(D[i][j],end='')
            print(end=' ')
            for j in range(6):
                print(L[i][j],end='')
            print(end=' ')
            for j in range(6):
                print(E[i][j],end='')
            print(end=' ')
            for j in range(6):
                print(X[i][j],end='')
            print()
G = [[' ' for i in range(6)] for j in range(6)]
R = [[' ' for i in range(6)] for j in range(6)]
I = [[' ' for i in range(6)] for j in range(6)]
D = [[' ' for i in range(6)] for j in range(6)]
L = [[' ' for i in range(6)] for j in range(6)]
E = [[' ' for i in range(6)] for j in range(6)]
X = [[' ' for i in range(6)] for j in range(6)]
gridlex(G,R,I,D,L,E,X)
