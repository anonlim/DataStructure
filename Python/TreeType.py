class TreeNode:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
    
class BST():

    def __init__(self):
        self.root = None
        self.order_list = []
    
    def is_empty(self):
        return (self.root == None)
    
    def count_nodes(self, tree):
        '''[1]'''
        if(tree==None):return 0
        else:
            return self.count_nodes(tree.left) + self.count_nodes(tree.right)+1
    def length_is(self):
        return self.count_nodes(self.root)

    def insert(self, item):
        '''[2]'''
        self.root=self.insert_item(self.root,item)
        return self.root
    def insert_item(self, node, item):
        '''[3]'''
        if node is None:
            node=TreeNode(item)
        elif(item<node.info):
            node.left=self.insert_item(node.left,item)
        else:
            node.right=self.insert_item(node.right,item)
        return node
    def inorder(self, node):
        '''[4]'''
        if(node is not None):
            self.inorder(node.left)
            self.order_list.append(node.info)
            self.inorder(node.right)
        return self.order_list
    def preorder(self, node):
        '''[5]'''
        if(node!=None):
            self.order_list.append(node.info)
            self.preorder(node.left)
            self.preorder(node.right)
        return self.order_list
    def postorder(self, node):
        '''[6]'''
        if(node!=None):
            self.postorder(node.left)
            self.postorder(node.right)
            self.order_list.append(node.info)
        return self.order_list
    def delete(self, item):
        '''[7]'''
        self.root, deleted=self.delete_node(self.root, item)
        return deleted
    def delete_node(self, current, item):
        '''[8]'''
        if(item<current.info):
            current.left, deleted=self.delete_node(current.left,item)
        elif(item>current.info):
            current.right, deleted=self.delete_node(current.right,item)
        else:
            if(current.left==None):
                deleted = current
                current = current.right
            elif(current.right==None):
                deleted=current
                current=current.left
            else:
                replace=current.left
                replace=replace.get_predecessor(current.left,item)
                current.info, replace.info=replace.info,current.info
                current.left,deleted=self.delete_node(current.left,replace.info)
        return current, deleted
    def get_predecessor(tree, data):
        '''[9]'''
        while(tree.right!=None):
            get_predecessor(tree.right,data)
        data=tree.info
        return tree
