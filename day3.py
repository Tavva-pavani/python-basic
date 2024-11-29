#table
num=5
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")
    
    
    
#factorial
fact=1
for i in range(1,6): #or (5,0,-1):
    fact=fact*i
print(fact)


#count the no of input number given and ouput for ex if i/p=4597 then o/p should be 4
num=12345
count=0
while(num!=0):
    num=num//10
    count=count+1 
print(count)        






#sum of input numbers for ex:234 as input as u/p should be 9(sum of nums)
num=2458
sum=0
while(num!=0):
    temp=num%10
    num=num//10
    sum=sum+temp
print(sum)  





#chech i/p is prime or not using loops
#flag is ntg but just a symbol
num=25
flag=False
for i in range(2,num):
    if(num%i==0):
        flag=True
        break
if(flag==True):   
    print(f"{num} is not a prime.")
else:
    print(f"{num} is a prime number.")


'''task for today
#fibonacci series
#reverse a number foa given input
'''