'''accessing a value in dict1
key=input()
values=input()
d[key]=values
'''

l=[]
print(type(l))
t=()
print(type(t))
s={}
print(type(s))
v=set()
print(type(v))

'''
1.creating and accessing the elements:
2.adding and updating elemnets:
3.removing elememts:
'''
d={1:'pavani',2:'tavva',3:'karimnagar'}
print(d.get(4))
d[4]='B.tech'
d[2]='Tavva'
print(d)
d.pop(4)
#d.pop(5) it gets erorr if we remove the elememt which is not available but if we remove the element which is avail then it removes that ele only.
#print(d.pop(4,"its not there"))  for this the ouput will be its not there it is not presnt but we r giving a value so its returns value
print(d)

'''1.iterating over dict:in 1st loop only keys should be then in 2nd for loop only values in 3rd for loop both keys and values
'''
d={1:'pavani',2:'tavva',3:'karimnagar'}
for i in d:
    print(f"keys:{i}")  
for i in d:
    print(f"values={d[i]}") 
for i in d:
    print(f"key :{i} and value :{d[i]}")
    
    
'''1.count the frequency of elements: 
2.string="hello world" '''     
string="hello world"
freq={}
for i in string:       
    if i in freq:
        freq[i] +=1
    else:
        freq[i]=1
print(freq)            
   #or  .get is a method which retuwns the values mentioned or given
   
freq[i]=freq.get(i,0)+1
print(freq)
'''
find the max value:
scores={'Alice':90,'Bob':82,'Charlie':95}
'''
scores={'Alice':90,'Bob':82,'Charlie':95}
max_score=0
char=''
for i,j in scores.items():
    if(j>max_score):
        max_score=j
        char=i
print(f" max_score of {char} is {max_score}")



'''  '''
    