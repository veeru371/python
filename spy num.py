n=int(input())
k=0
q=0
r=1
while n:
    k=n%10
    q=q+k
    r=r*k
    n=n//10
if q==r:
    print("spy num")
else:
    print("not spy num")
