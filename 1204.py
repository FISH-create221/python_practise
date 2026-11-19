N=int(input())
data=list(map(int,input().split()))
L,R=map(int,input().split())
s=sum(data)
if L*N<=s<=R*N:
    delta1=0
    delta0=0
    for i in range(N):
        if data[i]>R:
            delta1+=data[i]-R
        if data[i]<L:
            delta0+=L-data[i]
    print(max(delta1,delta0))
else:
    print(-1)