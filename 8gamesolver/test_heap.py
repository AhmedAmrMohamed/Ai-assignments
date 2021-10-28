from heap import *
import random as ran
class Testing:
    def __init__(self,tests = 10,max_lenght = 30,onlypositive=False,max = True):
        self.tests=tests
        self.max_lenght=max_lenght
        self.sign = 1 if not onlypositive else -1
        self.max = max
        self.testing()
    def fill(self,n):
        li=[ran.randint(-n,n)*self.sign for i in range(n)]
        x=heap(max=self.max)
        for i in li:
            x.insert(i)
        return x,li

    def pop(self,x,li):
        li.sort(reverse=self.max)
        for i in li:
            if i!=x.pop():
                return False
        return True
    def checksorting(self,x,li):
        li.sort(reverse=self.max)
        x=heap.sort(list=li)
        for i,ii in zip(li,x):
            if i!=ii:
                return False
        return True

    def testing(self):
        ret=[]
        for test in range(self.tests):
            leng = ran.randint(1,self.max_lenght)
            x,l=self.fill(leng)
            fillp='passed' if self.pop(x,l) else 'failed'
            sortp='passed' if self.checksorting(x,l) else 'failed'
            print('test :{} len : {} poping : {} sorting : {}'.format(test,leng,fillp,sortp))
            if fillp =='failed':
                print(l)
                ret.append((test,'pop'))
            elif sortp =='failed':
                print(l)
                ret.append((test,'sort'))
        print(ret)

