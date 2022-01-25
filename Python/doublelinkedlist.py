class NodeType:
    """ Node Type """
    def __init__(self, item):
        self.info = item
        self.next = None
        self.back = None

class DoublyLL:
    def __init__(self):
        self.head = NodeType('head')
    
    def find_item(self, item):
        moreToSearch=True
        location=self.head.next
        found= False
        while(moreToSearch and not found):
            if location!=None:
                if(item<location.info):moreToSearch=False
                elif(item==location.info):found=True
                else:
                    location=location.next
                    moreToSearch=(location!=None)
            else:moreToSearch=False
        return location
    
    def insert_item(self, item, new):
        '''[2]'''
        location=self.find_item(item)
        Newnode=NodeType(new)
        if location==None:
            self.head.next=Newnode
            Newnode.back=self.head
            Newnode.next=None
        else:
            Newnode.next=location.next
            Newnode.back=location
            if location.next==None:
                location.next=Newnode
            else:
                location.next.back = Newnode
                location.next=Newnode

    def delete_item(self, item):
        location=self.find_item(item)
        if location.next==None:
            location.back.next=None
        else:
            location.next.back=location.back
            location.back.next=location.next
        location.back=None
        location.next=None
        del location
        '''[3]'''
            
    def __str__(self):
        cur_node = self.head
        items = []
        while cur_node is not None:
            items.append("(" + str(cur_node.info) + ")\n")
            cur_node = cur_node.next
        return "".join(items)

