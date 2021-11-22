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
