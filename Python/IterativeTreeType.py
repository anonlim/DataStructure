
class NodeType:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class IterBST():
    def __init__(self):
        self.root = None
        self.order_list = []

    def insert(self, data):
        '''[10]'''
        new_node=NodeType(data)
        nodePtr,parentPtr=self.find_node(self.root,data)
        if(parentPtr==None):
            self.root=new_node
        elif(data<parentPtr.info):
            parentPtr.left=new_node
        else:
            parentPtr.right=new_node

    def find(self, key):
        '''[11]'''
        nodePtr, parentPtr=self.find_node(self.root,key)
        return nodePtr

    def find_node(self, root, key):
        '''[12]'''
        nodePtr = self.root
        parentPtr = None
        found = False
        while (nodePtr is not None and not found):
            if (key < nodePtr.info):
                parentPtr = nodePtr
                nodePtr = nodePtr.left
            elif (key > nodePtr.info):
                parentPtr = nodePtr
                nodePtr = nodePtr.right
            else:
                found = True
        return nodePtr, parentPtr

    def delete(self, key):
        '''[13]'''
        self.root, deleted=self.delete_node(self.root,key)
        return deleted

    def delete_node(self, node, key):
        '''[14]'''
        if (key < node.info):
            node.left, deleted = self.delete_node(node.left, key)
        elif (key > node.info):
            node.right, deleted = self.delete_node(node.right, key)
        else:
            if (node.left == None):
                deleted = node
                node = node.right
            elif (node.right == None):
                deleted = node
                node = node.left
            else:
                replace = node.left
                replace = replace.get_predecessor(node.left, key)
                node.info, replace.info = replace.info, node.info
                node.left, deleted = self.delete_node(node.left, replace.info)
        return node, deleted
    def inorder(self, node):
        '''[15]'''
        if(node is not None):
            self.inorder(node.left)
            self.order_list.append(node.info)
            self.inorder(node.right)
        return self.order_list
    def preorder(self, node):
        '''[16]'''
        if (node != None):
            self.order_list.append(node.info)
            self.preorder(node.left)
            self.preorder(node.right)
        return self.order_list
    def postorder(self, node):
        '''[17]'''
        if (node != None):
            self.postorder(node.left)
            self.postorder(node.right)
            self.order_list.append(node.info)
        return self.order_list
    def get_predecessor(tree):
        '''[18]'''
        while(tree.right!=None):
            tree=tree.right
        return tree
