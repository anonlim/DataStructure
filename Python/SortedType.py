from enum import Enum

MAX_ITEMS = 100

class Compare(Enum):
    LESS = 0
    GREATER = 1
    EQUAL = 2
    
class ItemType:
    def __init__(self, val):
        self.value=val

    def compared_to(self, otherItem):
        if self.value < otherItem.value:
            return Compare.LESS
        elif self.value > otherItem.value:
            return Compare.GREATER
        return Compare.EQUAL
    
    def __str__(self):
        return str(self.value)

class SortedType:
    """ Chapter 3: Sorted List """

    def __init__(self):
        self.length=0
        self.info=[0]*MAX_ITEMS
        self.current_pos=-1

    def make_empty(self):
        self.length = 0

    def length_is(self):
        return self.length

    def is_full(self):
        if self.length == MAX_ITEMS:
            return True
        return False

    def insert_item(self, item):
        loc=0
        while loc<self.length:
            "아이템이 더 작음"
            if item.compared_to(self.info[loc]).value==0:
                break
            else:
                loc+=1
        for i in range(self.length, loc, -1):
            self.info[i]=self.info[i-1]
        self.info[loc]=item
        self.length+=1

    def retrieve_item(self, item): # Binary Search
        first=0
        last=self.length-1
        mid=(first+last)//2
        while first<=last:
            if item.compared_to(self.info[mid])==1:
                first=mid+1
            elif item.compared_to(self.info[mid])==0:
                last=mid-1
            else:
                return mid

    def delete_item(self, item):
        loc=0
        while item.compared_to(self.info[loc]).value != 2:
            loc +=1
        index=loc +1
        for i in range(index, self.length):
            self.info[i-1]=self.info[i]
        self.length-=1


    def reset_list(self):
        self.current_pos = -1

    def get_next_item(self):
        self.current_pos += 1
        return self.info[self.current_pos]

    def __str__(self):
        self.reset_list()
        
        print_list = []
        for i in range(self.length):
            print_list.append(str(self.get_next_item()))
        
        return str(" ".join(print_list))