"""
CSE 212
Author: Nathaniel Jackson

This is a demonstration of the stack data structure, including
an example of how undo operations may work in a word processor"""

#This is the stack class that will be used in my demonstrations
class Stack:
    '''A Python Class for the Stack data structure'''
    def __init__(self):
        '''Class Constructor'''
        self.stack = []

    def push(self, value):
        """Inserts data at the end of the stack"""
        self.stack.append(value)
    
    def pop(self): 
        '''Removes and returns the data at the end of the stack'''
        temp = self.stack[-1]
        del self.stack[-1]
        return temp

    def size(self):
        '''Returns the length of the stack'''
        return len(self.stack)

    def empty(self):
        '''Returns True if the stack is empty'''
        if self.size() == 0:
            return True
        else:
            return False

#This is a demonstration of how Word's undo operation may work in python
class Word:
    '''Class to be used for demonstrating Word operation'''
    def __init__(self):
        '''Class constructor'''
        self.history = Stack()

    def display(self):
        '''This is NOT the proper use of a stack! 
        This function is SOLElY to emulate what text may look
        like in a Word processor, however it does not use the proper
        operations of a stack to do so
        You will not need to modify this function for your problem
        but it will be used in testing'''
        text = ''
        for word in self.history.stack: #Stacks should not be accessed this way
            text += f'{word} '

        print(text)

    def typed(self, value_typed):
        '''Appends a 'typed' value to history'''
        self.history.push(value_typed)

    def undo(self):
        '''Removes the last item typed given a stack of words typed'''
        self.history.pop()


#Example Test
processor = Word()
#User is typing
processor.typed('I')
processor.typed('love')
processor.typed('CSE')
processor.typed('22345') #User mistyped
processor.display()

#User hits CTRL+Z or 'undo'
processor.undo() 
processor.display()

#User can now type what they meant
processor.typed('212')
processor.display()




