a=[list(map(int,input().split())) for i in range(2)]
b=[list(map(int,input().split())) for i in range(2)]
c=[[a[i][j]+b[i][j] for j in range(2)] for i in range(2)]
print(c)
