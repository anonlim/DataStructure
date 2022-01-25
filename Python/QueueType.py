MAX_ITEMS = 100

class QueueType():
    def __init__(self):
        self.info = []

    def enqueue(self, data):
        '''[1]'''
        n=len(self.info)
        self.info.insert(n,data)
    def dequeue(self):
        '''[2]'''
        n=len(self.info)
        return self.info.pop(0)
    def is_empty(self):
        '''[3]'''
        n = len(self.info)
        if(n==0):return True
        else: return False
    def is_full(self):
        '''[4]'''
        n = len(self.info)
        if(n==MAX_ITEMS):return True
        else:return False
    def make_empty(self):
        '''[5]'''
        self.info.clear()