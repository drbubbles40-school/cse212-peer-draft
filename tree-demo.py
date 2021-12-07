"""
Author: Nathaniel Jackson

The BST class is taken from the Week 9 prove assignment from BYUI CSE 212"""

class BST:
    """
    Implement the Binary Search Tree (BST) data structure.  The Node 
    class below is an inner class.  An inner class means that its real 
    name is related to the outer class.  To create a Node object, we will 
    need to specify BST.Node
    """

    class Node:
        """
        Each node of the BST will have data and links to the 
        left and right sub-tree. 
        """

        def __init__(self, data):
            """ 
            Initialize the node to the data provided.  Initially
            the links are unknown so they are set to None.
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Initialize an empty BST.
        """
        self.root = None

    def insert(self, data):
        """
        Insert 'data' into the BST.  If the BST
        is empty, then set the root equal to the new 
        node.  Otherwise, use _insert to recursively
        find the location to insert.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
        else:
            pass #nothing should happen.

    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if data < node.data:
            # The data is on the left side.
            if node.left is None:
                # Value is not in the tree
                return False
            else:
                # Need to keep looking.  Call 
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
        elif data > node.data:
            # The data is on the right side.
            if node.right is None:
                # Value is not in the tree
                return False
            else:
                # Need to keep looking.  Call 
                # recursively on the right sub-tree.
                return self._contains(data, node.right)
        else:
            return True #Value is a match

    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the left
        side (thus getting the smaller numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the right side (thus getting the larger numbers last).

        The use of the 'yield' will allow this function to support loops
        like:

        for value in my_bst:
            print(value)

        The keyword 'yield' will return the value for the 'for' loop to
	    use.  When the 'for' loop wants to get the next value, the code in
	    this function will start back up where the last 'yield' returned a 
	    value.  The keyword 'yield from' is used when our generator function
        needs to call another function for which a `yield` will be called.  
        In other words, the `yield` is delegated by the generator function
        to another function.

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        """
        Perform a formward traversal (in order traversal) starting from 
        the root of the BST.  This function is called when a the 
        reversed function is called and is frequently used with a for
        loop.

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.  If the node that we are given (which is the current
        sub-tree) exists, then we will keep traversing on the right
        side (thus getting the larger numbers first), then we will 
        provide the data in the current node, and finally we will 
        traverse on the left side (thus getting the smaller numbers last).

        This function is intended to be called the first time by 
        the __reversed__ function.        
        """
        if node is not None: # reverse order of forward. Goes right (greatest value) first
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
        
    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is not None:
            if self._get_height(node.right) >= self._get_height(node.left): #check which subtree is bigger
                return 1 + self._get_height(node.right)
            
            else:
                return 1 + self._get_height(node.left)

        else: # end condition, the node after last returns 0 as it is not part of the tree
            return 0
    
    def _insert_middle(self, sorted_list, first, last):
        """
        This function will attempt to insert the item in the middle
        of 'sorted_list' into the 'bst' tree.  The middle is 
        determined by using indicies represented by 'first' and 'last'.
        For example, if the function was called on:

        sorted_list = [10, 20, 30, 40, 50, 60]
        first = 0
        last = 5

        then the value 30 (index 2 which is the middle) would be added 
        to the 'bst' (the insert function above can be used to do this).   

        Subsequent recursive calls are made to insert the middle from the values 
        before 30 and the values after 30.  If done correctly, the order
        in which values are added (which results in a balanced bst) will be:

        30, 10, 20, 50, 40, 60

        This function is intended to be called the first time by 
        create_bst_from_sorted_list.

        The purpose for having the first and last parameters is so that we do 
        not need to create new sublists when we make recursive calls.  Avoid 
        using list slicing to create sublists to solve this problem.

        """

        middle = ((last - first) // 2) + first #get middle index rounded down
        if middle >= 0: #ensure index is valid
            self.insert(sorted_list[middle]) #insert value at index
            if last == first: #ends loop when there are no more values to recurse through
                return
            else:
                self._insert_middle(sorted_list, first, middle)
                self._insert_middle(sorted_list, middle + 1, last)


    ################Demo Problems####################
    #Define the empty and size methods for the BST class
    #NOTE: This BST class does not support duplicate number values
    def empty(self):
        """
        Returns True if there is nothing in the tree
        """
        if self.root == None: #If the root is None, there are no items in tree
            return True
        else:                 #If there is a root it is not empty
            return False

    def size(self):
        '''
        Returns an integer equal to the number of nodes in the bst
        '''
        size = 0

        for _ in self: #loop through the bst
            size += 1

        return size

#Demonstration Tests
tree = BST()
tree.insert(1)  #1
tree.insert(2)  #2
tree.insert(6)  #3
tree.insert(3)  #4
tree.insert(8)  #5
tree.insert(11) #6
tree.insert(13) #7
tree.insert(75) #8
tree.insert(5)  #9
tree.insert(4)  #10
tree.insert(7)  #11
print(tree.size())  #11

e_tree = BST()
print(e_tree.empty()) #True
print(tree.empty())   #False
    