from heap import *
class queue (heap):
    def __init__(self, collection = None):
        self.collection = self.getCollection(collection)
        self.insertedCount = len(self.collection)
        super().__init__(self, self.collection, False)

    def getCollection(self, collection = None):
        if collection:
            return self.addIndexToGivenList(collection)
        return []

    def addIndexToGivenList(self, collection):
        li = [(idx, element) for idx, element in enumerate(collection)]
        return li

    def insert(self, item):
        tmp = (self.insertedCount, item)
        self.insertedCount+=1
        heap.insert(self, tmp)

    def pop(self):
        tmp = heap.pop(self)
        return tmp[1]



        
