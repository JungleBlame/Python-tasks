def binary_search(sorted_list, key):
    min_index=0
    max_index= len(sorted_list) - 1

    while(min_index <= max_index):
        mid= (min_index + max_index) // 2

        if sorted_list[mid] ==key:
            return mid
        elif sorted_list[mid] <key:
            min_index = mid + 1
        else:
            max_index = mid-1
    return -1 #<-- here if it is not in the list

num_list = [25,28,28,30,40,56]
#print(binary_search(num_list,30))


 #Binary Search Tree#
class Node:

    def __init__(self, data):
        self.left= None
        self.right= None

        self.data = data
    
    def get_left_child(self):
        return self.left
    
    def set_left_child(self,left):
        self.left = left
    
    def get_right_child(self):
        return self.right
    
    def set_right_child(self,right):
        self.right = right

    def get_value(self):
        return self.data

    def set_value(self,value):
        self.data=value

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

def insert(head, node):

        if head== None:
            return node
        
        if node.get_value() <= head.get_value():
            head.set_left_child(insert(head.get_left_child(), node))

        else:
            head.set_right_child(insert(head.get_right_child(), node))

        return head

def lookup (head,data):

    if head ==None:
        return print("VALUE NOT FOUND")
    
    if head.get_value()== data:
        return head
    
    if data <= head.get_value():
        return lookup(head.get_left_child(),data)
    else:
        return lookup(head.get_right_child(), data)
    
def print_node(node):
    if (node==None):
        print("Not found!")
    
    print(node.get_value())



A = Node(45)
B = Node(2)
C= Node(33)
D = Node(54)
E = Node(25)
F = Node (68)
G = Node(72)
H= Node(81)
I = Node(23)

head = insert(None, E)
#head.print_tree()

insert(head, B)
#head.print_tree()

insert(head, C)
insert(head, D)
insert(head, A)
insert(head, F)
insert(head, G)
insert(head, H)
insert(head, I)

#head.print_tree()

#print_node(lookup(head,68))

def min_value(head):
    current=head

    while(current.left != None):
        current=current.left
    
    return current.data

print(min_value(head))

def max_value(head):
    current=head

    #loop down to find right most leaf
    while(current.right != None):
        current=current.right

    return current.data

print(max_value(head))

#----------------------------Create a queue--------------------------------------------#

class MyQueue:

    def __init__(self):

        """Create a new queue."""

        self.items = []

    def is_empty(self):

        """Returns true if queue is empty"""

        return len(self.items)==0
    
    def enqueue(self,item):

        """Add a new element to end of the queue"""

        self.items.append(item)

    def dequeue(self):

        """Remove an element from the begining of queue"""

        return self.items.pop(0)
    
    def size(self):

        """Returns the size of the queue."""

        return len(self.items)
    
    def peek(self):

        """Have a lok at the first element of the queue"""

        if self.is_empty():
            raise Exception("Nothing to peek")
        
        return self.items[0]


#----------------------------------------Breath first traversal(left to right at level then down)-----------------------------------------------------------#

def breadth_first(node):

    if(node==None):
        raise Exception ("No root found!")
    
    path= []
    queue = MyQueue()
    queue.enqueue(node)

    while queue.size() >0:
        current = queue.dequeue()

        path.append(current.data)

        if current.get_left_child() != None:
            queue.enqueue(current.get_left_child())
        
        if current.get_right_child() != None:
            queue.enqueue(current.get_right_child())

    return path
        

print(breadth_first(E))

#-----------------------------------------Depth first traversal----------------------------------------------------------------------------------------------#

#Any node visit that node, its left child then right child#


def pre_order(node):
    path = []

    if node:
        path.append(node.data)

        path = path + pre_order(node.get_left_child())
        path = path + pre_order(node.get_right_child())

    return path

#pre_order(E)

# process left subtree before the node itself

def in_order(node):
    path = []

    if node:
        path = path + in_order(node.get_left_child()) #<-only when all left children have been looked at then node itself is looked at 

        path.append(node.data)

        path = path + in_order(node.get_right_child())

    return path

#in_order(E)
#[25, 2, 33, 23, 54, 45, 68, 72, 81]

#-------------------------------------Post order traversal---------------------------------------------------------------------------------------------------#

#visits left tree themn right tree the finnally the node itself

def post_order(node):
    path=[]

    if node:

        path = path + post_order(node.get_left_child())
        path = path + post_order(node.get_right_child())

        path.append(node.data)

    return path