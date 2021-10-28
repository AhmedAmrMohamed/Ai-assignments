class heap:
    def __init__(self,list=None,max=True,key = None):
        self.li = [None]
        self.max=max
        self.size = 0
        self.parent = lambda a: a//2 if a//2 > 0 else 1
        self.left   = lambda a:a<<1
        self.right  = lambda a:(a<<1)|1
        if not key:
            self.cmp    = lambda a,b:a>b if max else a<b
        else:
            self.cmp = key

        if list !=None:
            self.constructHeap(list)
    def __str__(self):
        return str(self.li)

    def __repr__(self):
        return self.__str__()

    def __next__(self):
        if self.itr>=self.size:
             raise StopIteration
        self.itr+=1
        return self.li[self.itr]

    def __len__(self):
        return self.size

    def __iter__(self):
        self.itr=0
        return self

    def empty(self):
        return self.size == 0

    def swim(self,pos):
        li=self.li
        while(pos > 1 and self.cmp(li[pos],li[self.parent(pos)])):
            parent_pos=self.parent(pos)
            li[pos],li[parent_pos] = li[parent_pos],li[pos]
            pos=parent_pos

    def sink(self,pos):
        li=self.li
        left=self.left
        right=self.right
        while right(pos)<=self.size:
                cpos=left(pos)
                if not self.cmp(li[cpos],li[cpos+1]):
                    cpos+=1
                if self.cmp(li[pos],li[cpos]):
                    break
                li[pos],li[cpos]=li[cpos],li[pos]
                pos=cpos

    def insert(self,item):
        self.li.append(item)
        self.size+=1
        self.swim(self.size)

    def pop(self):
        try:
            ret = self.li[1]
        except:
            raise ValueError('Empty Queue')
        self.li[1]=self.li[self.size]
        self.sink(1)
        self.size-=1
        self.li.pop()
        return ret

    def getmax(self):
        if self.empty():
            return None
        return self.li[1]

    def constructHeap(self,li):
        for i in li:
            self.li.append(i)
        self.size = len(self.li)-1
        pos = self.parent(self.size)
        while pos>0:
            self.sink(pos)
            pos-=1


    def sort(list,max=True):
        tmp = heap(list,max)
        li=[]
        for i in range(tmp.size):
            li.append(tmp.pop())
        return li

