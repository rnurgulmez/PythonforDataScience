#!/usr/bin/env python
# coding: utf-8

# # Data Structure

# In[1]:


L = [1,3,4.9,"name",3]
T = (1,3,4.9,"name",3)
S = {1,3,4.9,"name",3}
D = {23:"twothree",'B':43,'C':'CCD'}


# In[2]:


print("The type of L is :",type(L))
print("The type of T is :",type(T))
print("The type of S is :",type(S))
print("The type of D is :",type(D))


# In[3]:


print(L[1])
print(T[1])
print(3 in S)
print(D[23])


# In[4]:


print(D['B'])


# In[5]:


S


# In[6]:


L


# In[7]:


L[1:3]


# In[ ]:


L[::-1]


# In[9]:


T[:3]


# In[10]:


L


# In[11]:


L = L + ["how","are","6","you"]


# In[12]:


L


# In[13]:


L.append(6.8)


# In[14]:


L


# In[15]:


T2 = ("a","b",45)
T3 = T + T2


# In[16]:


T3


# In[17]:


S.add(56)


# In[18]:


S


# In[19]:


S.update({23,"game",1})


# In[20]:


S


# In[21]:


D


# In[22]:


D["newKey"] = "newValue"


# In[23]:


D


# In[24]:


D2 = {"y":"YY","z":10}


# In[25]:


del L[3]


# In[26]:


L


# In[27]:


S.remove("game")


# In[28]:


S


# In[29]:


D


# In[30]:


del D['C']


# In[31]:


D


# In[32]:


D.update(D2)


# In[33]:


D


# In[34]:


L


# In[35]:


L2 = L


# In[36]:


L2


# In[37]:


L2[2] = "four point nine"


# In[38]:


L2


# In[39]:


L


# In[41]:


L2 = L.copy()


# In[42]:


L2


# In[43]:


L2[2] = 4.9


# In[44]:


L2


# In[45]:


L


# In[46]:


L


# In[47]:


L3 = L[1:5]


# In[48]:


L3


# In[49]:


L3[0] = "three"


# In[50]:


L


# In[51]:


help(L.append)


# In[52]:


get_ipython().run_line_magic('pinfo', 'L.clear')


# In[53]:


get_ipython().run_line_magic('pinfo', 'L.pop')


# In[54]:


L.reverse()


# In[55]:


L


# In[56]:


L[::-1]


# In[57]:


D.items()


# In[58]:


L


# In[59]:


T


# In[60]:


S


# In[61]:


D


# In[62]:


D2 = {'A':L,'B':T,'C':S,'D':D}


# In[63]:


D2['A'][3]


# In[64]:


K = D2['D']


# In[65]:


K


# In[66]:


for x in K:
    print(x,K[x])


# In[67]:


L3 = [L,T,D,"game",23]


# In[68]:


type(L3[2])


# In[69]:


L3 = [x**2 for x in range(10)]


# In[70]:


L3


# In[71]:


S3 = {x**2 for x in range(2,20,3)}


# In[72]:


S3


# In[73]:


"""
Let say you are a teacher and you have different student records containing id of a student 
and the marks in each subject where different students have taken different number of subjects.
All these records are in hard copy.You want to enter all the data in computer and want to compute 
the average marks of each student and display.
"""


# In[74]:


def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter student ID : ")
        marksList = input("Enter the marks by comma separted values : ")
        moreStudents = input('Enter "no" to quit insertion : ')
        if studentId in D:
            print(studentId,"is already insterted.")
        else:
            D[studentId] = marksList.split(",")
        if moreStudents.lower() == "no":
            return D


# In[75]:


studentData = getDataFromUser()


# In[76]:


studentData


# In[77]:


def getAvgMarks(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s += int(marks)
        avgMarks[x] = s/len(L)
    return avgMarks


# In[78]:


avgM = getAvgMarks(studentData)


# In[79]:


for x in avgM:
    print("Student :",x,"got avg Marks as: ",avgM[x])


# # Numpy

# In[80]:


import numpy as np


# In[81]:


a = np.array([1,2,3,5,7],dtype='i')


# In[82]:


b = np.array((2,3,5),dtype='f')


# In[83]:


print(a)


# In[84]:


type(a)


# In[85]:


type(b)


# In[86]:


a.dtype


# In[87]:


b.dtype


# In[88]:


a = np.array([[1,2,3],[4,5,6]])


# In[89]:


a.ndim


# In[90]:


a[0,2]


# In[91]:


b = np.array([[1,2,3,-1],[2,4,5,9]])


# In[92]:


b.ndim


# In[93]:


b[1,2]


# In[94]:


c = np.array([[[1,2,3],[4,5,6],[0,0,-1]],[[-1,-2,-3],[-4,-5,-6],[0,0,1]]])


# In[95]:


c.ndim


# In[96]:


c[1,0,2]


# In[97]:


type(c)


# In[98]:


c.shape[0]


# In[ ]:


c.shape[1]


# In[ ]:


c.shape[2]


# In[ ]:


A = np.array([2])


# In[ ]:


A.ndim


# In[ ]:


B = np.array(3)


# In[ ]:


B.ndim


# In[ ]:


c.size


# In[ ]:


c.nbytes


# In[ ]:


A = np.arange(20,100,3) # for i in range(20,100,3)
print(A)


# In[ ]:


print(range(10))


# In[ ]:


print(list(range(10)))


# In[ ]:


a = np.random.permutation(np.arange(10))


# In[ ]:


print(a)


# In[ ]:


v = np.random.randint(20,300)


# In[ ]:


print(type(v))


# In[ ]:


a = np.random.rand(1000)


# In[ ]:


a


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


plt.hist(a,bins=100)


# In[ ]:


b = np.random.randn(100000)
plt.hist(b,bins=2000)


# In[ ]:


c = np.random.rand(2,3)


# In[ ]:


c


# In[ ]:


c.ndim


# In[ ]:


c = np.random.rand(2,3,4,2)


# In[ ]:


c


# In[ ]:


c.ndim


# In[ ]:


d = np.arange(100).reshape(4,25)


# In[ ]:


d.shape


# In[ ]:


d


# In[ ]:


d = np.arange(100).reshape(4,5,5)


# In[ ]:


d.shape


# In[ ]:


get_ipython().run_line_magic('pinfo', 'np.zeros')


# In[ ]:


get_ipython().run_line_magic('pinfo', 'np.ones')


# # Numpy (Slicing)

# In[ ]:


import numpy as np
a = np.arange(100)


# In[ ]:


b = a[3:10]
print(b)


# In[ ]:


b[0] = -1200


# In[ ]:


b


# In[ ]:


a


# In[ ]:


b = a[3:10].copy()


# In[ ]:


b[0] = -99
b


# In[ ]:


a


# In[ ]:


a[::5]


# In[ ]:


a[::-5]


# In[ ]:


a[::-1]


# In[ ]:


get_ipython().run_line_magic('pinfo', 'np.indices')


# In[ ]:


indicies = np.where(a == -1200)
print(indicies)


# In[ ]:


a


# In[ ]:


idx = np.argwhere(a == -1200)[0][0]


# In[ ]:


idx


# In[ ]:


a[idx] = 3


# In[ ]:


a


# In[ ]:


a = np.round(10*np.random.rand(5,4))


# In[ ]:


a


# In[ ]:


a[1,2]


# In[ ]:


a[1,:]


# In[ ]:


a[:,1]


# In[ ]:


a[1:3,2:4]


# In[ ]:


a


# In[ ]:


a.T


# In[ ]:


import numpy.linalg as la


# In[ ]:


la.inv(np.random.rand(3,3))


# In[ ]:


a


# In[ ]:


a.sort(axis=0)
a


# In[ ]:


a.sort(axis=1)
a


# # Numpy Masking(More Indexing)

# In[ ]:


A = np.arange(100)


# In[ ]:


B = A[[3,5,6]]


# In[ ]:


B


# In[ ]:


B[0] = -4
# it doesn't change a because it is copy rather than a view


# In[ ]:


A


# In[ ]:


B = A[A<40]
B


# In[ ]:


B = A[(A<40) & (A>30)]
B


# In[ ]:


# &,and
# |,or
# ~,not (right side : array,left side : single objects)


# # Numpy(Broadcasting)

# In[ ]:


import numpy as np
A = np.round(10*np.random.rand(2,3))


# In[ ]:


A


# In[ ]:


A + 3


# In[ ]:


A + (np.arange(2).reshape(2,1))


# In[ ]:


B = np.round(10*np.random.rand(2,2))


# In[ ]:


A


# In[ ]:


B


# In[ ]:


C = np.hstack((A,B))
C


# In[ ]:


A = np.random.permutation(np.arange(10))


# In[ ]:


A


# In[ ]:


A.sort()


# In[ ]:


A


# In[ ]:


np.sort(A)


# In[ ]:


A[::-1]


# In[ ]:


B = np.random.rand(1000000)
get_ipython().run_line_magic('timeit', 'sum(B)')
get_ipython().run_line_magic('timeit', 'np.sum(B) # B.sum()')


# In[ ]:


def mySum(G):
   s = 0
   for x in G:
        s+=x
        return s


# In[ ]:


get_ipython().run_line_magic('timeit', 'mySum(B)')


# # Pandas

# In[2]:


import pandas as pd


# In[3]:


print(pd.__version__)


# In[4]:


A = pd.Series([2,3,4,5],index=["a","b","c","d"])


# In[5]:


type(A.values)


# In[6]:


type(A)


# In[7]:


A.index


# In[8]:


A['a']


# In[9]:


A['a':'c']


# In[10]:


grads_dict = {'A':4,'B':3.5,'C':3,'D':2.5}
grads = pd.Series(grads_dict)


# In[11]:


grads.values


# In[12]:


grads.index


# In[13]:


marks_dict = {'A':85,'B':75,'C':65,'D':55}
marks = pd.Series(marks_dict)


# In[14]:


marks


# In[15]:


marks['A']


# In[16]:


marks[0:2]


# # Pandas (DataFrame)

# In[17]:


marks


# In[18]:


grads


# In[19]:


D = pd.DataFrame({'Marks':marks,'Grades':grads})


# In[20]:


D


# In[21]:


D.T


# In[22]:


D


# In[23]:


D.values


# In[24]:


D.values[2,0]


# In[25]:


D.columns


# In[26]:


D


# In[27]:


D['ScaledMarks'] = 100*(D['Marks']/90)


# In[28]:


D


# In[29]:


del D['ScaledMarks']


# In[30]:


D


# In[31]:


G = D[D['Marks']>70] #masking


# In[32]:


G


# # Pandas (NaN)

# In[33]:


A = pd.DataFrame([{'a':1,'b':4},{'b':-3,'c':9}])


# In[34]:


A


# In[35]:


A.fillna(0)


# In[36]:


A.dropna


# In[37]:


A = pd.Series(['a','b','c'],index=[1,3,5])


# In[38]:


A[1] #explicit


# In[39]:


A[1:3] #implicit


# In[40]:


A.loc[1:3]


# In[41]:


A.iloc[1:3]


# In[42]:


D


# In[43]:


D.iloc[2,:]


# In[44]:


D.iloc[::-1,:]


# In[45]:


from sklearn.impute import SimpleImputer


# In[46]:


df = pd.read_csv('C:/Users/rabia/Downloads/archive/worldometer_data.csv')


# In[47]:


df.head(10)


# In[48]:


df.drop(['NewRecovered','Population'],axis=1,inplace=True)


# In[49]:


df.head()


# In[50]:


df.rename(columns={'NewCases':'UpdatedCases','Country/Region':'Country','TotalRecovered':'Recovered'},inplace=True)


# In[51]:


df.head()


# In[52]:


# df['Date'] = pd.to_datetime(df['Date'])


# In[53]:


df.describe()


# In[54]:


df.info()


# In[55]:


df = df.fillna('NA')


# In[56]:


df.info()


# In[57]:


df.head(10)


# In[58]:


df2 = df.groupby('Country')[['Country','TotalCases','Recovered','Deaths/1M pop','ActiveCases']].sum(numeric_only=True).reset_index()


# In[59]:


df2


# In[60]:


# df2 = df.groupby(['Country','Date'])[['Country','Date','TotalCases','Recovered','Deaths/1M pop','ActiveCases']].sum(numeric_only=True).reset_index()


# In[61]:


# df3 = df2[df2['Confirmed']>100]


# # Matplotlib

# In[62]:


import numpy as np
import matplotlib.pyplot as plt


# In[63]:


x = np.linspace(0,10,1000)
y = np.sin(x)
plt.plot(x,y)


# In[64]:


plt.scatter(x[::10],y[::10],color='red')


# In[65]:


plt.plot(x,y,color='blue')
plt.plot(x,np.cos(x),color='g')


# In[66]:


plt.plot(x,x+0,'-g')  # solid green
plt.plot(x,x+1,'--c') # dashed cyan
plt.plot(x,x+2,'-.k') # dashdot black
plt.plot(x,x+3,':r')  # dotted red


# In[67]:


df.head(20)


# In[69]:


countries = df2['Country'].unique()
len(countries)


# In[ ]:


# what is recovered or death trends as the date moves on
for idx in range(0,len(countries)):
    C = df3[df3['Country'] == countries[idx]].reset_index()
    plt.scatter(np.arrange(0,len(C)),C['Confirmed'],color='blue',label='Confirmed')
    plt.scatter(np.arrange(0,len(C)),C['Recovered'],color='green',label='Recovered')
    plt.scatter(np.arrange(0,len(C)),C['Deaths'],color='red',label='Deaths')
    plt.title(countries[idx])
    plt.xlabel('Days since the first suspect')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()

