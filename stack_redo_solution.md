``` python
global stack = []
global redo = []

def write (input):
  stack.push(input)
  return input
  
def undo(text):
  redo.push(stack.pop())
  return stack
  
  def redo():
  stack.push(redo.pop())
  return stack
```
