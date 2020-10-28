def india2020(i,n,d,a,t,z):
    # pattern I
    for row in range(7):
        for col in range(7):
            if (row in {1,2,3,4,5} and col == 2) or (row in {0,6} and col in {1,2,3}):
                I[row][col] = '#'
            else:
                I[row][col] = ' '
    # pattern N
    for row in range(7):
        for col in range(7):
            if (row in {0,1,2,3,4,5,6} and col in {0,6}) or (row == col):
                N[row][col] = '#'
            else:
                N[row][col] = ' '
    # pattern D
    for row in range(7):
        for col in range(7):
            if (row in {0,6} and col in range(0,6)) or (row in {1,2,3,4,5} and col in {0,6}):
                D[row][col] = '#'
            else:
                D[row][col] = ' '
    # pattern A
    for row in range(7):
        for col in range(7):
            if (row in {3,5,6} and col in {0,6}) or (row == 4 and col in range(0,7)):
                A[row][col] = '#'
            elif (row in {0} and col == 3) or (row == 1 and col in {2,4}) or (row == 2 and col in {1,5}):
                A[row][col] = '#'
            else:
                A[row][col] = ' '

    # pattern TWO
    for row in range(7):
        for col in range(7):
            if (row in {0,3} and col in {1,2,3,4,5}) or (row in {4,5} and col == 0) or (row == 2 and col == 6):
                T[row][col] = '#'
            elif (row in {6} and col in {0,1,2,3,4,5,6}) or (row == 1 and col in {0,6}):
                T[row][col] = '#'
            
            else:
                T[row][col] = ' '
    # pattern ZERO
    for row in range(7):
        for col in range(7):
            if (row in {0,6} and col in {2,3,4}) or (row in {1,5} and col in {1,5}):
                Z[row][col] = '#'
            elif (row == 2 and col in {0,2,6}) or (row == 3 and col in {0,3,6}) or (row == 4 and col in {0,4,6}):
                Z[row][col] = '#'
            else:
                Z[row][col] = ' '
    # nested 
    for i in range(7):
        for j in range(7):
            print(I[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(N[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(D[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(I[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(A[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(T[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(Z[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(T[i][j],end='')
        print(end=' ')
        for j in range(7):
            print(Z[i][j],end='')
        print()
        
I = [[' ' for i in range(7)] for j in range(7)]
N = [[' ' for i in range(7)] for j in range(7)]
D = [[' ' for i in range(7)] for j in range(7)]
A = [[' ' for i in range(7)] for j in range(7)]
T = [[' ' for i in range(7)] for j in range(7)]
Z = [[' ' for i in range(7)] for j in range(7)]

india2020(I,N,D,A,T,Z)   