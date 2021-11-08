val=int(input('enter the value'))
opt2=input('daatype for conv:::: 1::int,2::bin,3::oct,4::hex')

if(int(opt2)==1):
    op=int(val)
elif(int(opt2)==2):
    op=bin(int(val))
elif(int(opt2)==3):
    op=oct(int(val))
elif(int(opt2)==4):
    op=hex(int(val))
else:
    print('you enter a wrong option')
    op=0
print('original',val,'converted no',op,'what data type of option',op)

