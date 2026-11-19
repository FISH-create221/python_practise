N=int(input())
data=list(map(int,input().split()))
ave=sum(data)/N
n=0
for i in range(N-1):
    if data[i] > ave:
        data[i]=ave
        data[i+1]+=data[i]-ave
        n+=1
    else:
        continue
if data[N-1] >ave:
    n+=1
print(n)