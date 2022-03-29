# Stacks
### Introduction
- a stack is a Python data storage method where the last piece of data placed into the 
stack is the first to be withdrawn and the first is the last to be withdrawn. This is known as 
Last-In/First-Out data storage. Stacks are one of the most common methods of data storage because
there are many times when you will do something, then need to reverse it.
### How to use stacks
- there are two times you would use a stack, first when you are typing something, make a mistake, and need to reverse it, and when you have functions that call other functions.

### Undo action and stacks
- When you type something into a word processor, the word you type is printed on the screen and is added to a stack. When you call the undo function, it will look at the item on top of the stack, because that would be the most recent thing added, remove it from the word processor document, then remove it from the stack. This will cause the next most recent item in the stack to be on top and using undo again would cause that items action to be undone.

### stacking functions
-	The other time you will be using stacks will be when you call a function that calls a different function. Simply calling a function is part of the code, but you will be needing tell the computer that if function A calls function B, it needs to go back to function A when function B ends. This becomes even more complicated when function B itself calls several more functions.
-	Using a stack, here called a function stack, will allow the computer to keep track of which function is currently running as well as which part of a function you were in when it called a new function, as having to start over from function A when function B ends would result in an infinite loop.

### example: undo
when using a word processor, sometimes you will make a mistake. this function will let you undo that mistake. 
```  python
global stack = []

def write (input):
  stack.push(input)
  return input
def undo(text):
  
  stack.pop()
  print(" ".join(stack))
```
### practice: redo
Now implement a function that reverses the undo function. You many need to add another stack and alter the other functions.

### stack syntax
There are five basic parts to stack syntax
(note my_stack is just a placeholder; you can name your stack whatever you want)

Stack Operation|  description  | code                 | Big O Performance
---------------|---------------|----------------------|----------------
create(stack) |creates a new stack| **my_stack = []**|O(1)- Performance of creating the stack|
push(value)|adds the value to the back of the stack. |**my_stack.append(value)**|O(1) - Performance of adding to the end of a dynamic array|
pop()| Remove and return item from the back of the stack| **value = my_stack.pop()**|O(1) - Performance of removing from the end of a dynamic array|
size()| Return the size of the stack.| **length = len(my_stack)**| O(1) - Performance of returning the size of the dynamic array|
empty()| Returns true if the length of the stack is zero.| **if len(my_stack) == 0:**| O(1) - Performance of checking the size of the dynamic array|























