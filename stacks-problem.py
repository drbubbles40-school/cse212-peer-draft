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
        self.discard = Stack()

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
        #BONUS TYPE CODE HERE
        

    ########### Problem 1 ############
    """Modify the class below to develop a working
    redo function. This function should be able to restore any
    values removed fromthe stack by undo.
    Note: if the user continues typing after an undo, redo should
    no longer store values undone
    
    BONUS:If undo or redo are empty, print that the operation cannot be done, 
    preventing the program from crashing"""

    def undo(self):
        '''Removes the last item typed given a stack of words typed
        Temporarily records it in the discard stack'''
        #ENTER/MODIFY CODE HERE
        self.history.pop()
        #BONUS
        

    def redo(self):
        '''Restores the value that was undone to the history stack
        In other words, moves the plate from the top of discard to the 
        top of history, the opposite of undo.'''
        #ENTER CODE HERE
        pass
        #BONUS
    

#Example Test
print('---------Practice Example---------')
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

#Problem Test Cases
print('---------Problem 1---------')
processor = Word()
processor.typed('Testing')
processor.typed('the')
processor.typed('Redo')
processor.undo()
processor.redo()
processor.typed('Function')
processor.display()   #Correct Output: Testing the Redo Function

#BONUS Test Cases
print('---------Bonus Problem---------')
processor.undo()
processor.undo()
processor.undo()
processor.typed('Bonus')
processor.redo() #Displays the error message you wrote i.e.'Processor cannot redo.'
processor.undo()
processor.undo()
processor.undo() #Displays the error message you wrote i.e.'Processor cannot undo.'