def m1():
    p=(1,2,3)
    x,y,z=p
    data=['ACMILAN',1,2]
    x,y,z=data
    print(x)
    print(x[3])
    print(y)
def m2():

    d=deque([1,2,4,5,6])
    d.append(3)
    d.pop()
    d.popleft()
    print(d)
def find():
    from collections import Counter
    words=[1,2,3,4,4,4,4,4,4,5,5,5,6,7,8]
    word_counters=Counter(words)
    x=word_counters.most_common()
    print(x)

find()
class A:
    def li(self):
        x=10
        print(x)

class B(A):
    def li(self):
        x=20
        x2=super().li()
        print(x2)
d={'1':'kakak','2':2,'3':3}
for key in d:
    print(d[key])
def it():
    it=iter([1,3,5,7,9])
    while True:
        try:
            x=next(it)
            print(x)
        except StopIteration:
            break
    print('finished')
def read():
    with open('e://test1.txt') as f:
        while True:
            try:
                line=next(f)
                print(line,end=' ')
            except StopIteration:
                break
    print('read finish!')
def gene():
    g=(x*x for x in range(10))
    print(next(g))
    print(next(g))
def fib(max):
    n,a,b=0,0,1
    while(n<max):
        yield (b)
        a,b=b,a+b
        n+=1
    return 'done!'
f=fib(6)
for i in f:
    print(i)
print(f)