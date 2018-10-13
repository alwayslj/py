
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
f8()