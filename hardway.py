'''
from sys import argv
def f1():
    script,first,second,third=argv
    print("The script is called:",script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)
def f2():
    script,x1,x2=argv
    input1=input("x1= ")
    input2=input("x2= ")
    print('your %s is %s'%(x1,input1))
    print('your %s is %s' % (x2, input2))

def f3():
    script,user_name=argv
    info='>>>'
    print("Hi,%s,I am the %s script"%(user_name,script))
    print('I\'like to ask you a few questions')
    print('Where do you live,%s'%(user_name))
    address=input(info)
    print("Ok,%s, I know that you live in %s"%(user_name,address))
def f4():
    with open("e:/test1.txt",'r') as t1:
        with open("e:/copy.txt",'w') as c1:
            content=t1.read()
            c1.write(content)

f4()
class exercise:
    def break_words(self,sentence):
        return sentence.split(" ")
    def sort_words(self,sentence):
        return sorted(sentence)
    def first(self,sentence):
        return sentence.pop(0)
    def last(self,sentence):
        return sentence.pop(-1)

def f5():
    import random
    num=random.randint(1,100)
    n=0

    while(1):
        n+=1
        guess = int(input("please guess a number between(1,100)>>"))
        if(guess>num):
            print("your guess is too large,try a smaller one~")
            continue
        elif(guess<num):
            print("your guess is too small,try a larger one~")
            continue
        else:
            print('Bingo! the answer is %d !'%num)
            break
    print("用了{0}次机会".format(n))
def f6():
    shopping=['apple','banana','orange']
    blankt=[]
    for i in shopping:
        print('I have bought %s'%i)
        blankt.append(i)
    print('look at my blankt:')
    for i in range(len(blankt)):

        print('%s'%blankt[i])

def f7():
    f=open("e:/copy.txt",'r')
    n=len(f.readlines())
    print(n)
f7()
class Thing(object):
    def test(self,hi):
        print('hi')
a=Thing()
a.test('hello')
def f8():
    ten_things='Apples Oranges Crows Telephone Light Sugar'
    stuff=ten_things.split(' ')
    print(stuff)
    more_stuff=['Day','Night','Song','Banana']
    while(len(stuff)!=10):
        next_one=more_stuff.pop()
        print('Adding:',next_one)
        stuff.append(next_one)
    print('#'.join(stuff[3:8]))

def f9():
    stuff={'name':'jet','age':30,'school':'OUC',1:False}
    print(stuff[1])
    stuff['salary']=12800
    print(stuff)
    del (stuff[1])
    print(stuff)
    print('name' in stuff)
    vals=stuff.values()
    print('OUC' in vals)

def f10(sen):
    d=dict()
    for i in sen:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d.keys())
    return d
def find(d,v):
    temp=[]
    for i in d:
        if(d[i]==v):
            temp.append(i)
    return temp
sen='songnisondaoxiaoshengwai'
print(f10(sen))
print(find(f10(sen),3))

class TheThing(object):
    def __init__(self):
        self.number=0
    def some_function(self):
        print('Hello~')
    def add_me_up(self,more):
        self.number+=more
        return self.number
a=TheThing()
b=TheThing()
a.some_function()
print(b.add_me_up(20))
print(a.number,b.number)

def distance_between_points(a,b):
    import math
    dis=pow((a.x-b.x),2)+pow((a.y-b.y),2)
    distance=math.sqrt(dis)
    return distance
class Point:
    def __init__(self):
        self.x=0
        self.y=0
    def set_x(self,x1):
        self.x=x1
    def set_y(self,y1):
        self.y=y1
p1=Point()
p1.set_x(1)
p1.set_y(1)
p2=Point()
p2.set_x(2)
p2.set_y(3)
print(distance_between_points(p1,p2))

class Time(object):
    def getT(self):
        return self.hour

t=Time()
t.hour=11
t.minute=20
t.second=10
print(t.getT())
print(type(3.2))
print()

def getV(r):
    import math
    cons=float(4/3)
    print(cons)
    v=cons*math.pi*(r**3)
    return v
radius=int(input("请输入球体半径>"))
print("体积为:",getV(radius))
print(type(getV))
def empty(str):
    print(' '*(70-len(str))+str)
str='allen'
empty(str)

def huiwen(str):
    if(str==None):
        return 0
    elif(str==str[::-1]):
        return 1
    else:
        return 0
strr=input('please input a string>')
print(huiwen(strr))
def b(z):
    prod = a(z, z)
    print (z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print (c(x, y+3, x+y))

def Ack(m,n):
    if(m==0):
        return n+1
    elif(m>0 and n==0):
        return Ack(m-1,1)
    elif(m>0 and n>0):
        return Ack(m-1,Ack(m,n-1))
    else:
        return None
print(Ack(3,4))
'''
def cubpow(a,b):
    if(a%b!=0):
        return False
    if(a==b and b!=0):
        print('yes')
        return True
    else:
        a=a/b
        print(a)
        cubpow(a,b)
print(cubpow(8,2))
def is_power(a,b):
    import math
    for i in range(a):
        if(pow(b,i)==a):
            print("%d**%d次方等于%d"%(b,i,a))
            return True
    return False
is_power(8,2)

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(4,8))

def evaluate(x,start):
    import math
    count=1
    while(abs(math.sqrt(x)-start)>0.000001):
        print("第{0}次估值".format(count))
        start=(start+x/start)/2
        print(start)
        count+=1
    print("共用%d次估计"%(count-1))
evaluate(4,3)

def sec(str,num):
    for s in str:
        t=ord(s)
        t=t+num
        s=chr(t)
        print(s,end='')
str='melon'
sec(str,-10)