val=input('enter a number::')
sum=0
temp=int(val)
for ii in range(len(val)):
    sum=sum+temp%10
    temp=int(temp/10)
def sum_digits(temp):
    sum=0
    for ii in range(len(val)):
        sum=sum+temp%10
        temp=int(temp/10)
        return sum
val=input('enter a number ::')
temp=int(val)
sum=sum_digits(temp)


print(sum)
