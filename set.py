#given input as list[1,2,2,3,4,4] and remove duplicate elememts and print as list
l=[1,2,2,3,4,4]
s=set(l)
print(list(s))

#given two sets find union,intersection,and difference
A={1,2,3,4}
B={3,4,5,6}
print(A|B)
print(A&B)
print(A-B)


#create a list containing sets snd tuples and access the 2nd element of the tuple and check if 5 exixst in a set.
l=[(1,2,3),{67,67,55,5,7,2,3}]
l2=l[0][1]
l3=l[1]
print(l2)
print(5 in l3)


#write a python program to merge 2 lists into a set to remove duplicate,then convert the set back to a sorted list.
l1=[17,35,98,34,76,56]
l2=[34,68,90,52,45,76]
s=set((l1+l2))
l=list(s)
l.sort()
print(l)# instead of line 26 and 27 we can directly use l=sorted(s) sorted is built-in function takes set or tuple and sort them and returns only in list format 
'''
treasure Hunt(list indexing ) u r a treasure hunt, and you have a list of directions to follow: directions=['north','east,'south','west','north','north','east]
task:1.find out how many times u go north
2.replace the 3rd direction with 'up' because there is a hill in a way
3.reverse the order of the directions''' 
l=['North','East','South','West','North','North','East']
print(l.count('North'))
'''or without any built-in function 
count=0
for item in l:
    if(item=='North')
      count=count+1
print(count)      
'''
l[2]='Up'
print(l)
print(l[::-1]) #or print(l.reverse())
''' or 
low=0
high=len(l)-1
while(low<high)
    l(low),l[high]=l[high],l[low]
    low=low+1
    high=high-1
'''

''' lucky draw(unique entries using sets)
ur organising a lucky draw event where participants write their names on chits.accidebtatlly,some names were written more than once!here is a list:names=[].
task:
1.remove duplicate names using set.
2.add a new participants 'frank' to tha set.
3.convert the set back into a sorted list to find the winner(alphabetically first)
'''
names=['Alice','Bob','Charlie','Alice','Eve','Bob','David']
s=set(names)
print(s)
s.add('Frank')
print(s)
l=sorted(s)
print(l[0])

'''find the odd ones out 
there are 2 set of students:
Math Enthusiasts:math_students={'Alice','Bob','Charlie','Eve'}
Science Enthusiasts:science_students={'Charlie','Eve','Frank',''Grace}
Task:
1.find the students who are only intrested in Math(not science).
2.find the students who are intrested in both math and science.
3.combine both groups to get a list of all unique students.
'''
math_students={'Alice','Bob','Charlie','Eve'}
science_students={'Charlie','Eve','Frank','Grace'}
print(math_students-science_students)
print(math_students&
      science_students)
s=list(math_students|science_students)
print(s)
'''secret code(list and string manipulation)
ur decoding a secret message where every letter in the string is hidden in a list.
letters=[]
task:
1.remove the '-' from the list.
2.combine the letter into a single string
3.reverse the string to get the secret message.
'''
letters=['h','e','l','l','o','-','w','o','r','l','d']
letters.remove('-')
print(letters)
str=''
for item in letters:
    str=str+item  #instead of 98 and 99 just use str=''.join(letters)
print(str)
print(str[::-1])