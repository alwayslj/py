
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