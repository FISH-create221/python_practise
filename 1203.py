n,m=map(int,input().split())
weight=list(map(int,input().split()))
weight_=[]
for i in range(n+1-m):
    weight_.append(sum(weight[i:i+m]))
print(min(weight_))