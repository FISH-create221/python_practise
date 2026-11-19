N=int(input())
data=list(map(int,input().split()))
ave=sum(data)/N
data_=[_-ave for _ in data]
n=0
for i in range(N):
    if data_[i] != 0:
        n+=1
        data_[i+1]+= data_[i]
print(n)