def m0():
    a=1
    b=3.23
    c=52.3E-4
    sen='''我可以'这么'
    '''
    age=25
    name='kaka'
    info={'age':26,'name':'kaka'}
    print('{name} is {age} years old'.format(**info))
def m1():
    i=5
    print(i)
    i=i+1
    print(i)
    s='''This is a string
    This is the second line
    '''
    print(s)
def guess():
    import random
    loop=1
    ans=random.randint(1,10)
    while(loop):
        g=int(input("请输入您要猜的数字(1-10)"))
        if(g==ans):
            print("Bingo!The answer is {}".format(ans))
            loop=0
        elif(g>ans):
            print('you guess big!')
        else:
            print('you guess smanll!')
#guess()
def m2():
    for i in range(1,3):

        print(i)
    else:
        print('finished!')
def m3():
    while True:
        s=input("please input a sentence:")
        if(s=='quit'):
            break
        print('the length is ',len(s))
    print('finished!')
def m4():
    while True:
        s=input('please input:')
        if(s=='quit'):
            break
        if(len(s)<3):
            print('too small!')
            continue
        print('this is the end!')
def m5(a,b,c):
    num=[a,b,c]
    print(num)
    num.sort()
    print('the medium is:',num[1])
x=50
def m6():
    global x
    print('the formal x is:',x)
    x=2
    print('now x is %d'%(x))
def m7(a,b=5,c=10):
    print('a is %d b is %d c is %d'%(a,b,c))
def m8(initial=5,*numbers,**keywords):
    count=initial
    for number in numbers:
        count+=number
    for key in keywords:
        count+=keywords[key]
    print('result:',count)

m8(10,1,2,3,x=50,y=100)
def m9():
    import mymudule
    mymudule.sayhi()
    print(mymudule.__version__)
    print(dir(mymudule))
def m10():
    shoplist=['apple','mango','carrot','banana']
    print(shoplist[1:3])
    print('I have %d items to buy'%(len(shoplist)))
    print('These items are:',end=' ')
    for item in shoplist:
        print(item,end=' ')
    print('I also want to buy rice')
    shoplist.append('rice')
    print('I will sort my list')
    shoplist.sort()
    print('The first item i want to buy is: ',shoplist[0])
    del shoplist[0]
    print('I have bought first item')
    print('My list now:')
    print(shoplist)
def info():
    myInfo={
        'name':'lijie',
        'school':'ouc',
        'phone':15092218732
    }
    print('my name is :',(myInfo['name']))
    myInfo['major']='ML'
    print(myInfo)
    test='hello world'
    print(test[-1])
def m11():
    shoplist=['apple','mango','carrot','banana']
    print(shoplist[1:3])
    print(shoplist[2:])
m11()

class Robert:
    population=0
    def __init__(self,name):
        self.name=name
        print('(Initialize {0})'.format(self.name))
        Robert.population+=1
    def __del__(self):
        print('{0} is being destroyed!'.format(self.name))
        Robert.population-=1
        if(Robert.population==0):
            print('{0} is the last one'.format(self.name))
        else:
            print('There are still {0:d} roberts working'.format(Robert.population))
    def sayhi(self):
        print('my name is {0}:'.format(self.name))
    def count(self):
        print('we have {0:d} robets now'.format(Robert.population))
    count=staticmethod(count)
#d1=Robert('R2-D2')
#d1.sayhi()
class School:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print('my name is {0}, my age is {1},'.format(self.name,self.age),end=' ')
class Teacher(School):
    def __init__(self,name,age,salary):
        School.__init__(self,name,age)
        self.salary=salary
    def info(self):
        School.info(self)
        print('my salary is {0}'.format(self.salary),end=' ')
class Stu:
    def __init__(self,name,age,marks):
        School.__init__(self,name,age)
        self.marks=marks
    def info(self):
        School.info(self)
        print('my mark is {0}'.format(self.marks),end=' ')
t=Teacher('lijie',22,10000)
s=Stu('LI',15,100)
mem=[t,s]
for m in mem:
    m.info()
    print()
def reverse(text):
    return text[::-1]
def pd(text):
    return text==reverse(text)

