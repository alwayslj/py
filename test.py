def test1():
    print('i like it')
    greeting='hello world'
    print(greeting[0])
    test=[1,2,3,4,6]
    print(max(test))
    test[0]=10
    print(max(test))
    boil=list('we win!')
    boil[2:2]=list('china')
    boil.append(list('lijie'))
    print(boil)


def test2():
    field='just do itt'
    print(field[-3:-1])
    a=field.find('do',)
    print(field.upper())
    print('i am %.2f'%(3/4))
    intab='abcde'
    outtab='12345'
    transtab=str.maketrans(intab,outtab)
    st='abddd'
    print('the result is:',st.translate(transtab))


def dictionanry():
    stu={'li':'1408010213','jie':'21180231288'}
    print('li的学号为：%(li)s'%(stu))
    print (stu)
    s1=stu.copy()
    print('jie的学号为：%(jie)s'%(s1))
    print('jie的学号为：%s'%s1.get('jie'))
    print(s1.items())
    for value in s1.values():
        print(value)
    seq={'name','age','sex'}
    info=dict.fromkeys(seq)
    print('信息如下：\n 姓名：%(name)s'%(info))
    info=dict.fromkeys(seq,'lijie')
    print('信息如下：\n 姓名：%(name)s' % (info))

def ch6():
    import math
    print(math.pi)
    x,y,z=1,2,3
    print(y)
    x=3
    assert x>0,"x is not zero or negative"
    n=1
    while n<=100:
        print(n)
        n=n+1
def pd(x):
    right=x
    num=str(x)
    n=len(num)
    print("长度为：%s"%n)
    count=1
    result=0
    while count<n:
        one=int(x/(10**(n-count)))
        result+=one**3
        x=x%(10**(n-count))
        count+=1
    result=result+x**3
    print(result)
    if(result==right):
        print("%d是阿姆斯特朗数"%right)
    else:
        print("%d不是阿姆斯特朗数"%right)

def func(arg,*vartuple):
    print(arg)
    for var in vartuple:
        print("我是不定长部分:",var)
    return
#           ';  [  func('li',21,'男')

def exp(p1,p2,df=0,*vart,**kw):
    print('p1=',p1,'p2=',p2,'df=',df,'var=',vart,'kw=',kw)
exp(1,2)

exp(1,2,c=3)


class Myclass(object):
    i=123
    def __init__(self,name):
        self.name=name
        print('我是初始化方法，先执行我')
    def greeting(self):
        return 'hello '+self.name

cl=Myclass('xiaoming')
print(cl.i)
print(cl.greeting())

class test(object):
    def __init__(self,a,b):
        self.a=a;
        self.b=b
    def out(self):
        return (self.a,self.b)

t=test(3,5)
print(t.out())
class default(object):
    i=123
    def __init__(self):
        print('我是不带参数的构造方法')
    def __init__(self,name):
        print('我是带参数的构造方法，参数值为：',name)
d=default('lijie')
print(d.i)

class Stu(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def info(self):
        print('%s的成绩为%d'%(self.name,self.score))
s=Stu('lijie',100)
s.info()
s.score=101
s.info()

class Stud(object):
    def __init__(self,name,score):
        self.__name=name
        self.score=score
    def info(self):
        print('成绩为：',self.score)
        print('name:',self.__name)
s1=Stud('lijie',200)
s1.info()
s1.score=211
s1.info()
s1.name='xiujun'
s1.info()

class Teacher(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def get(self):
        return self.__score
    def set(self,score):
        self.__score=score
    def __play(self):
        print('我是一个私有方法')
    def info(self):
        print('name:',self.__name)
        print('score',self.__score)
        self.__play()
t=Teacher('huang',100)
t.info()
t.set(200)
t.info()

class Animal(object):
    def __init__(self,name):
        self.name=name
    def info(self):
        print('名字为:',self.name)
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def pr(self):
        print('name:',self.name)
a=Animal('jack')
d=Dog('mary')
print('a是否是Animal类型？',isinstance(a,Animal))
print('d是Animal类型吗？',isinstance(d,Animal))
print('d是Dog类型吗？',isinstance(d,Dog))

d.info()

def exp(x,y):
    try:
        a=x/y
        print('a=',a)
        return a
        raise ValueError('这是一个无效的参数')
    except:
        print('出现错误，0不能做除数！')
exp(2,1)

def mul(x,y):
    try:
        a=x/y
        b=name
    except(NameError,ZeroDivisionError,ValueError) as e:
        print(e)
mul(2,1)
def testError(x,y):
    try:
        a=x/y
        print('a:',a)
    except(NameError,ZeroDivisionError,ValueError) as e:
        print(e)
    finally:
        print('No matter what happend,I will show in front of you')
testError(2,0)
#pd(1012)
#ch6()
import time,datetime
print(time.time())
print(time.localtime())
print(datetime.datetime.today())
print(datetime.datetime.now())
path="e:/test1.txt"
f_name=open(path,'r')
print(f_name.read(12))
f_name.close()
f_name=open(path,'a')
f_name.write('there is a warming greeting from ouc!\n')
f_name=open(path,'r')
print(f_name.readline(50))
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender='17685807197@163.com'
pwd='woaiwoziji093'
receivers=['1692916750@qq.com']
message=MIMEText('Python邮件测试')

def find():
    n=int(input('请输入数组长度'))
    str_in = input('请以空格为间隔连续输入一个数组:')
    given = [int(n) for n in str_in.split()]
    t=int(input('请输入target:'))
    for i in range(0,n):
        for j in range(i,n):
            if(t-given[i]==given[j]):
                print(i,j)
            else:
                j=j+1
        i=i+1
find()

from urllib import request
