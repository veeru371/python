n=int(input())
q=n
a=0
rev=0
rev2=0
t=n*n#144
while (n>0):
    k=n%10
    rev= (rev*10)+k 
    n=n//10
    a=rev
    i=a*a
    b=i
while (b>0):

    c= b%10
    rev2= (rev2*10)+c
    b=b//10
print(q)
print(rev)
print(t)
print(rev2)
print(i)

if t==rev2:
    print("true")
else:
    print("false")









