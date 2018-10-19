import numpy as np
'''array=np.array([[1,2,3],[4,5,6]])
print(array)
array1=np.array([[1,2,3],[2,3,4]],dtype=np.int64)
print(array1)
#生成一个全部为零的矩阵
a1=np.zeros((3,4))
a2=np.arange(10,20,2)
#12必须与shape里的(3,4)相对应
a3=np.arange(6).reshape((3,2))
a4=np.array([[1,1,1],[2,2,2]])
print(a3.dot(a4))
print('============')
a5=np.random.random((3,9))
print(np.max(a5,axis=0))
print('============')
A=np.arange(2,14).reshape(3,4)
print('index %d+index%d= %d'%(np.argmin(A),np.argmax(A),np.argmin(A)+np.argmax(A)))
B=np.arange(3,15).reshape(3,4)
C=np.arange(1,13).reshape(3,4)
D=np.vstack((B,C))
D=np.hstack((B,C))
print(np.vstack((B,C)))
print(B.shape,D.shape)
X=np.array([1,2,3])
print(X.shape)
print(X[:,np.newaxis])

#分割array
A=np.arange(12).reshape(3,4)
print(A)
print(np.split(A,4,axis=1))

#赋值
A=np.arange(4)
print(A)
b=A.copy()
A[1:3]=[22,33]
print(A)
print(b)
'''
import pandas as pd
s=pd.Series([1,2,4,55,np.nan])
dates=pd.date_range('20181029',periods=6)
df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
df1=pd.DataFrame(np.arange(12).reshape(3,4))
df2=pd.DataFrame({})
print(df1.describe())