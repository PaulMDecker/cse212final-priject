``` python
global stack = []
global redo = []

def write (input):
  stack.push(input)
  return input
  
def undo(text):
  redo.push(stack.pop())
  print(" ".join(stack))
  
  def redo():
  stack.push(redo.pop())
  print(" ".join(stack))
```
