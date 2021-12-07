"""
Author: Nathaniel Jackson

Much of the LinkedList class was taken from 07-prove, was starting to rewrite it
but realized I was writing the exact same thing, no point reinventing the wheel

Linked List Demo"""

class LinkedList:
    """Class for a linked list in python"""
    class Node:
        """Class for the node object which will be the base
        of the linked list."""

        def __init__(self, value):
            """Initialize node attributes"""
            self.data = value #attribute where data is stored
            self.prev = None  #stores previous node
            self.next = None  #stores next node
    
    def __init__(self):
        """Initialize linkedlist with head and tail"""
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """Adds a value to the front of the linked list"""
        new_node = LinkedList.Node(value)

        if self.head == None: #List is empty
            self.head = new_node
            self.tail = new_node

        else: #List is not empty, adjust pointers
            self.head.prev = new_node #change current heads previous node
            new_node.next = self.head #set new node's next to current head 
            self.head = new_node      #before assigning it as head

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        #Create new node
        new_node = LinkedList.Node(value)

        #If the list is empty, point head and tail to new node
        if self.tail is None:
            self.head = new_node
            self.tail = new_node

        # If the list is not empty adjust self.tail
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        #If list is only one node, set head and tail to none
        if self.head == self.tail:
            self.head = None
            self.tail = None

        #Otherwise remove tail
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev

    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        curr = self.head
        while curr is not None:
            if curr.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if curr == self.tail:
                    self.insert_tail(new_value)

                # For any other location of 'value', need to create a 
                # new node and reconnect the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr       # Connect new node to the node containing 'value'
                    new_node.next = curr.next  # Connect new node to the node after 'value'
                    curr.next.prev = new_node  # Connect node after 'value' to the new node
                    curr.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            curr = curr.next # Go to the next node to search for 'value'

    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        # Start at head to search through the list
        curr = self.head
        while curr is not None:
            if curr.data == value:

                #Check if there is only one node
                if curr == self.head:
                    self.remove_head()

                elif curr == self.tail:
                    self.remove_tail()

                # set pointers of surrounding nodes to bypass curr
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev

                    del curr #free memory

                return
            
            curr = curr.next

    def display(self):
        """
        Displays the linked list in the terminal
        for testing and error checking"""

        curr =  self.head #start at head
        display = []
        while curr is not None: #loops until the end.
            display.append(curr.data) #print data
            curr = curr.next
        
        print(display)

    def count(self, value):
        """Counts the number of times a value is in the list"""
        curr = self.head #start at the head
        count = 0 #start counter at 0

        while curr is not None:
            if curr.data == value: #if value is equal increment by one
                count += 1
            
            curr = curr.next #move on to next node
        
        return count


    ##################Problem 1#################
    #Implement the size operation for the linkedlist class
    def size(self):
        """This function returns the size of the linked list"""
        size = 0  #Initialize count to zero
        curr = self.head #start at the front of the linked list

        while curr is not None:  #loop through the whole list
            size += 1            #every time it loops size increases by 1
            curr = curr.next     #Move to the next node

        return size

    #################End Problem 1#############

    #################Problem 2####################
    #Implement the empty operation for the linkedlist class
    def empty(self):
        """This function returns True if the list is empty"""
        #If head is None list is empty, since it and tail are first to be assigned
        if self.head == None:  
            return True
        else:
            return False
    ##################End Problem 2#################

#Test Cases
print('--------Problem 1---------')
linklist1 = LinkedList()
linklist1.insert_head(1)
linklist1.insert_tail(7)
linklist1.insert_tail(1)
linklist1.insert_tail(7)
linklist1.insert_tail(9)
linklist1.insert_tail(7)
linklist1.insert_tail(2)
linklist1.insert_tail(7)

linklist2 = LinkedList()
linklist2.insert_head(6)
linklist2.insert_tail(3)
linklist2.insert_head(9)

linklist1.display()
print(f'size: {linklist1.size()}') #Correct Output: 8
linklist2.display()
print(f'size: {linklist2.size()}') #Correct Output: 3
print()

print('--------Problem 2---------')
linklist3 = LinkedList()
linklist1.display() 
print(f'List 1: {linklist1.empty()}') #Correct Output: False
linklist3.display() 
print(f'List 1: {linklist3.empty()}') #Correct Output: True