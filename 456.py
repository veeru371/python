data =int(input('enter a number =  '))
list=[]
for ii in range (1,data+1):
    if(data%ii==0):
        list.append(ii)

print(list)
     
