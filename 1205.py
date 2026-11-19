N=int(input())
grid=[]
for i in range(N):
    row=list(map(int,input().split()))
    grid.append(row)

dp=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            dp[0][0]=grid[0][0]
        elif i==0 :
            dp[i][j]=dp[i][j-1]+grid[i][j]
        elif j==0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j]=grid[i][j]+max(dp[i][j-1],dp[i-1][j])
print(dp[N-1][N-1])