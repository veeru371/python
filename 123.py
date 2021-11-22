import random

'''data=[]
for ii in range(20):
  temp = random.randint(1,100)
  data.append(temp)'''

data=[random.randint(1,100)for ii in range(20)]
  
print(['the data:::',str(data)])

summ = sum(data)
print('the value of sum is',summ)
avg=summ/20
print('the avg value is',avg)

largest=max(data)
smallest=min(data)
print('the largest number is',largest)
print('the smallest number is',smallest)
sort_Data = sorted(data)

print(sort_Data)
largest2 =sort_Data[-2]
smallest2 =sort_Data[1]
print(largest2)
print(smallest2)
count=0
for ii in data:
  if(ii%2==0):
      count=count+1

print('number of even elements',count)
