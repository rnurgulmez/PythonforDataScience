#!/usr/bin/env python
# coding: utf-8

# # This is Python Tutorial

# This is our first program in Python:It's just started here

# In[1]:


print("Hello World!")


# $a=b+c$

# # Variables

# In[2]:


x = 3


# In[3]:


get_ipython().run_line_magic('whos', '')


# In[4]:


print(type(x))


# In[5]:


x = 5.7


# In[6]:


get_ipython().run_line_magic('whos', '')


# In[7]:


abc=556.32


# In[8]:


get_ipython().run_line_magic('whos', '')


# In[9]:


a,b,c,d,f=3,5,6.0,7.2,-1


# In[10]:


get_ipython().run_line_magic('whos', '')


# In[11]:


del abc


# In[12]:


get_ipython().run_line_magic('whos', '')


# In[13]:


print(abc)


# In[15]:


c= 2+4j


# In[14]:


print(type(c))


# In[16]:


s="hellow how are you"


# In[17]:


print(type(s))


# # Operators

# In[18]:


get_ipython().run_line_magic('whos', '')


# In[19]:


sumOfaAndb = a+b


# In[20]:


print(sumOfaAndb)


# In[21]:


type(sumOfaAndb)


# In[22]:


type(a+d)


# In[23]:


v = ((a+d)**3)/4


# In[24]:


print(v)


# In[25]:


s1 = "hellow"
s2 = "world"
s = s1 + s2
print(s)


# In[26]:


10//3


# In[27]:


10/3


# In[28]:


_


# In[29]:


3x = 5


# In[30]:


@y = 4


# In[31]:


*t = 4


# In[32]:


_e = 6


# In[33]:


startingTimeOfTheCourse = 2.0


# In[34]:


get_ipython().run_line_magic('whos', '')


# # Type Bool and Comparisons

# In[35]:


a = True
b = True
c = False


# In[36]:


get_ipython().run_line_magic('whos', '')


# In[37]:


print(a and b)
print(a and c)
print(b and c)


# In[38]:


d = a or c
print(d)


# In[39]:


not(a)


# In[40]:


not(b)


# In[43]:


not(c)


# In[44]:


t = not(d)


# In[45]:


type(t)


# In[46]:


print(t)


# In[47]:


not((a and b) or (c or d))


# # Comparisons

# In[50]:


print(2<3)


# In[51]:


c = 2<3
print(type(c))
print(c)


# In[52]:


d = 3==4
print(d)


# In[53]:


3==3.0


# In[54]:


3=3.5


# In[55]:


3==3.5


# In[56]:


x = 4
y = 9
z = 8.3
r = -3


# In[57]:


(x<y) and (z<y) or (r==x)


# In[1]:


print(round(4.556))


# In[2]:


print(round(4.345))


# In[5]:


print(round(4.556389,3))


# In[6]:


print(divmod(27,5))


# In[8]:


G = divmod(34,9)


# In[9]:


type(G)


# In[10]:


G[1]


# In[11]:


G[0]


# In[12]:


34//9


# In[13]:


34%9


# In[17]:


print(isinstance(1.0,(int,float)))


# In[15]:


isinstance(3,int)


# In[16]:


isinstance(2.4,int)


# In[20]:


isinstance(2+3j,(int,float,str,complex))


# In[21]:


pow(2,4)


# In[22]:


2**4


# In[23]:


pow(2,4,7)


# In[26]:


x=input("enter a number : ")


# In[25]:


print(type(x))


# In[27]:


x = int(x)


# In[28]:


type(x)


# In[29]:


print(x-3)


# In[32]:


a = float(input("Enter a real number : "))


# In[31]:


type(a)


# In[2]:


get_ipython().run_line_magic('pinfo2', 'pow')


# In[4]:


a = int(input())
b = int(input())
if a>b:
    print(a)
    print("I am still inside if condition")
print("I am outside the if condition")


# In[12]:


a = int(input())
b = int(input())
if a>b:
    print("a is greater than b,a and b:",a,b)
elif a==b:
    print("a and b are equal,a and b:",a,b)
else:
    print("b is greater than a,a and b:",a,b)


# In[13]:


a=9
b=10
print("A") if a>b else print("=") if a==b else print("B")


# In[16]:


a = int(input("Enter Marks: "))
if a>=85:
    print("A grade")
elif (a>=80) and (a<85):
    print("A- grade")
elif (a>=75) and (a<80):
    print("B grade")
elif (a>=70) and (a<75):
    print("B- grade")
else:
    print("Below Avarage")


# In[1]:


a = 3
if a>10:
    print(">10")
elif not(a>10):
    print("else part")


# In[5]:


x = int(input("Enter a number : "))
if x>10:
    print("your number is greater than ten, ")
    if x>20:
        print("and also above 20!")
        if x>30:
            print("it is also above 30!!")
        else:
            print("but it is not above 30.")
    else:
        print("but not above 20.")


# In[6]:


#single line comment
"""
User will enter a floating number let say 238.915. Your task is to find 
out the integer portion before the point (in this case 238)
and then check if that integer portion is an even number or not.
"""


# In[6]:


x = float(input("Enter a floating number : "))
y = round(x)
if x>0:
    if y>x:
        intPortion = y-1
    else:
        intPortion = y
else:
    if y>x: 
        intPortion = y
    else:
        intPortion = y+1
        
if intPortion%2 == 0:
    print("even")
else:
    print("odd")


# In[7]:


n = int(input("How many times should I repeat? :"))
i=1
while i<n:
    print(i)
    i+=1
print("done")


# In[9]:


n = int(input())
i = 1
while i < n:
    print(i**2)
    print("This is iteration number :",i)
    i += 1
print("Loop Done")


# In[11]:


n = 10
i = 1
while True:
    if i%9 == 0:
        print("inside if")
        break
    else:
        print("inside else")
        i += 1
print("loop is done")


# In[1]:


n = 10
i = 1
while True:
    if i%9 != 0:
        print("inside if")
        i += 1
        continue
    print("something")
    print("something else")
    break
print("done")


# In[5]:


L = []
for i in range(0,10,2):
    print(i)
    L.append(i**2)
print(L)


# In[7]:


S = {"apple",4.9,"cherry"}
i = 1
for x in S:
    print(x)
    i += 1
    if i==3:
        break
    else:
        pass
else:
    print("Loop terminates with success")
print("Out side the loop")


# In[8]:


D = {"A":10,"B":-19,"C":"abc"}
for x in D:
    print(x,D[x])


# In[10]:


"""
Given a list of numbers [1,2,4,-5,7,9,3,2] make another list that contains all the items 
in sorted order from min to max. Your result will be another list like [-5,1,2,2,3,7,9].
"""


# In[14]:


L = [1,2,4,-5,7,9,3,2]
for j in range(len(L)):
    m = L[j]
    idx = j
    c = j
    for i in range(j,len(L)):
        if L[i]<m:
            m = L[i]
            idx = c
        c+=1
    tmp = L[j]
    L[j] = m
    L[idx] = tmp
print(L)


# In[13]:


L


# # Functions

# In[1]:


def printSuccess():
    print("The task was successful")
    print("Moving to the next task")
    print("Send me the next task")


# In[2]:


printSuccess()


# In[5]:


def printSuccess2():
    """
    This function is doing nothing except printing a message. This message is "hellow"
    """
    print("Hellow")


# In[6]:


printSuccess2()


# In[7]:


get_ipython().run_line_magic('pinfo', 'printSuccess2')


# In[8]:


get_ipython().run_line_magic('pinfo2', 'printSuccess2')


# In[9]:


get_ipython().run_line_magic('pinfo', 'len')


# In[10]:


help(printSuccess2)


# In[13]:


def printMessage(msg):
    """This function printing message that you supplied.
    """
    print(msg)


# In[12]:


printMessage("rabia")


# In[14]:


def printMsg(msg):
    """
    The function prints the message supplied by the user or prints that msg is not in the form of string.
    """
    if isinstance(msg,str):
        print(msg)
    else:
        print("Your input argument is not a string")
        print("Here is the type what you have supplied : ",type(msg))


# In[15]:


help(printMsg)


# In[16]:


printMsg(23)


# In[17]:


printMsg("hellow my name is taylor")


# In[18]:


y = "hellow"
printMsg(y)


# In[1]:


def mypow(a,b):
    """This function computes power just like builtin pow function
    """
    c = a**b
    print(c)


# In[2]:


mypow(3,2)


# In[3]:


get_ipython().run_line_magic('pinfo', 'mypow')


# In[9]:


def checkArgs(a,b,c):
    if isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        print((a+b+c)**2)
    else:
        print("Error: the input arguments are not of the expected types")


# In[10]:


checkArgs(3,4,5)


# In[11]:


checkArgs(3,4,"g")


# In[12]:


def f(a,b,c):
    print("A is :",a)
    print("B is :",b)
    print("C is :",c)    


# In[14]:


#f(2,3,"game")
f(3,"game",2)


# In[16]:


#f(a=3,b=2,c="game")
f(b=2,a=3,c="game")


# In[1]:


def add(x,y):
    return x+y


# In[2]:


add(3,5)


# In[5]:


def myAdd(a,b):
    c = a+b
    return c


# In[6]:


myAdd(2,3)


# In[7]:


variableOutSideTheFunction = 3


# In[13]:


def g():
    variableOutSideTheFunction = 5
    #print(variableOutSideTheFunction)


# In[17]:


print(type(g()))


# In[15]:


print(variableOutSideTheFunction)


# In[18]:


def h():
    print("A")
    a=3
    b=5
    c=a+b
    print("something")
    return 
    print("B")
    print("C")


# In[19]:


print(h())


# In[20]:


def r():
    a=5
    b=7
    d="something"
    return a,b,d


# In[22]:


x,y,z=r()
print(x,y,z)


# In[23]:


def add(*args):
    sum = 0
    for i in range(len(args)):
        sum += args[i]
    return sum


# In[24]:


add(2,3,45,25)


# In[3]:


def f(**c):
    for x in c:
        print(x,c[x])


# In[4]:


get_ipython().run_line_magic('pinfo2', 'f')


# In[8]:


f(a=1,b=2,c="hellow")


# In[6]:


def printAllVariablesNamesAndValue(**args):
    for x in args:
        print("Variable Name is :",x,"and Value is :",args[x])


# In[7]:


printAllVariablesNamesAndValue(a="rabia",b="nur",c="gülmez")


# In[9]:


def f(sum=0):
    print(sum)


# In[10]:


f()


# In[11]:


f(5)


# In[1]:


def gg(s=4):
    print(s)


# In[2]:


gg()


# In[3]:


gg(6)


# In[6]:


L = [1,2,3]
L2 = L
L2[0] = -9
print(L)


# In[7]:


def ff(L=[1,2]):
    for i in L:
        print(i)


# In[9]:


L2 = [12,3,4]
ff(L2)


# In[10]:


ff()


# In[18]:


import sys
sys.path.append("C:/ABC/")
import my_universal_functions


# In[19]:


my_universal_functions.myName


# In[20]:


c = my_universal_functions.addAllNumerics(2,3,45)


# In[21]:


print(c)


# In[22]:


"""
Given a list of numbers [1,2,4,-5,7,9,3,2] make another list that contains all the items 
in sorted order from min to max. Your result will be another list like [-5,1,2,2,3,7,9].
"""


# In[25]:


def findMin(L,startIndx):
    m = L[startIndx]
    idx = startIndx
    for i in range(startIndx,len(L)):
        x = L[i]
        if x<m:
            m = x
            idx = i
        else:
            pass
    return m,idx


# In[31]:


def swapValues(L,idx1,idx2):
    tmp = L[idx1]
    L[idx1] = L[idx2]
    L[idx2] = tmp
    return L


# In[32]:


L=[2,3,4,5]
L2=swapValues(L,1,3)
print(L2)


# In[49]:


#from my_universal_functions import checkIfNotNumeric
def sortList(L):
    if not(checkIfNotNumeric2(L)):
        print("Error: List does not contain numeric values")
        return
    else:
        c=0
        for x in L:
            m,idx = findMin(L,c)
            L = swapValues(L,c,idx)
            c+=1
    return L


# In[50]:


def checkIfNotNumeric2(L):
    for x in L:
        if not(isinstance(x,(int,float))):
            return false
    return True


# In[51]:


checkIfNotNumeric2([2,3,4,5,-1,0])


# In[52]:


L2 = sortList([2,3,4,2,-4,923])
print(L2)


# # String

# In[8]:


s = "Python is a good language"
t = "It's good for data science"


# In[9]:


type(s)


# In[11]:


print(s," and ",t)


# In[6]:


print("hellow",12,"who are you")


# In[59]:


v = s+" "+t
print(v)


# In[3]:


price = 12
s = "The price of this book"
v = s+" is: "+str(price)
print(s,"is:",price)


# In[62]:


print(v)


# In[15]:


a = """This is line 1
this is line 2
this is last line and this line is 3
"""


# In[16]:


print(a)


# In[17]:


print("""The following options are available:
          -a     : does nothing
          -b     : also does nothing
""")


# In[2]:


s= "How are you and who are you"


# In[3]:


print(s[5])


# In[4]:


type(s[5])


# In[5]:


s[3:8]


# In[6]:


s[3:9]


# In[7]:


s[-1]


# In[8]:


s[-12:-3]


# In[9]:


s[0:12:2]


# In[10]:


#s[start:end:step]
s[:12]


# In[11]:


s[3:]


# In[12]:


s[1:12]


# In[13]:


s[::-1]


# In[14]:


print(len(s))


# In[15]:


print(len(s[3:8]))


# In[18]:


a = "    A lot OF Spaces at The      beGinning and end      "
b = a.strip()
print(b)


# In[20]:


c = a.lower()
print(c)


# In[21]:


d = a.upper()
print(d)


# In[22]:


e = a.replace("Spaces","tabs")
print(e)


# In[1]:


a = "abc;def;hgydeflwek;yy23"
L = a.split(";")
print(L)


# In[2]:


a = "hello world"


# In[4]:


print(a.capitalize())


# In[7]:


help(a.count)


# In[8]:


"abc" in "öfdsklöfsdlgjaö"


# In[9]:


"rabia" not in "sakföawkrrabiaafkw"


# In[10]:


"abc" == "abc"


# In[12]:


"abcdsflksdl"<"def"


# In[13]:


"$%" < "*&"


# In[15]:


print("We are learning \"string\" here.")


# In[16]:


print("We are learning 'string' here.")


# In[17]:


print("We are \n now on another line.")


# In[20]:


print(r"c:\name\drive")

