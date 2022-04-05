# tree
### Introduction
- A linked list is a data structure where data is stored in nodes, and the nodes are connected by pointers. A tree is like a linked list except that in a tree a node can be connected to multiple nodes.  



### binary tree
- A binary tree is a tree where each node only connects to two other nodes. The root of a binary tree is the node that points to other nodes and has no nodes pointing to it. A root node is also a parent node because it is pointing to other nodes. A node that is being pointed to is called a child node and the node that is doing the pointing is called a parent node. A node that has a parent node, but no child nodes is called a leaf node. A parent and its child nodes is called a subtree.
<img width="662" alt="Screen Shot 2022-03-30 at 1 59 30 PM" src="https://user-images.githubusercontent.com/97462627/160920621-959f7e8a-ff1f-4cea-bbf4-2a7fd6f72f6a.png">

### binary search tree
- A binary search tree is a tree that has certain rules for how data is stored inside it. The data is compared to the data inside the parent tree, and if it is smaller than the parent tree, it is put in the left child node, and if it is bigger it is put in the right child node. If the tree allows duplicates, it can go in either of the child nodes.
<img width="448" alt="Screen Shot 2022-03-31 at 7 14 56 AM" src="https://user-images.githubusercontent.com/97462627/161063601-5440038a-f576-44e7-9a70-ef130b228b77.png">

### inserting into a tree

- Binary search tree operations are very complicated because almost all of them require recursion to work. Inserting a number into a tree must be done with recursion because a loop can’t tell how many times it will need to run in this case because the branches of the tree can be a different length.
``` python
def insert(self, data):
  """
  This function starts at the root and checks if it is empty. if it is empty it inserts 
  the data into the root node. if it is not, it will call the search function that will 
  look thorugh the tree until it finds a node to place the data into.
  """
  if self.root is None:
      self.root = BST.Node(data)
    else:
      self._insert(data, self.root)
      
	"""
	This function is the search function that will look for an empty node to place data in.
  if the data is less than the data contained in the current node, it will try to place the 
  data in the left child node, and if it is greater than the data in the current node, it will
  place the data in the right child node. if the child node is already full, it will repeat the
  process until it finds an empty node.
	"""
  def _insert(self, data, node):
	if data < node.data:
		# The data belongs on the left side.
		if node.left is None:
			# We found an empty spot
			node.left = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the left subtree.
			self._insert(data, node.left)
	elif data >= node.data:
		# The data belongs on the right side.
		if node.right is None:
			# We found an empty spot
			node.right = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the right subtree.
			self._insert(data, node.right)
```
### traversing a tree
- When you want to display all the data in a tree, you need to traverse the tree. There are three methods of traversing a tree. The pre-order traversal, the in-order traversal, and the post-order traversal. Pre-order traversal is when we iterate through the nodes from left to right, in-order traversal is when we iterate through the tree from smallest to largest, and post-order traversal is when we iterate from the leaves of the tree to the root.
- For this lesson, we will focus on in-order traversal. 

-	The first function here is called **__iter__**. The double underscores on either side mean that the functions is part of pythons framework. For example, a **loop** calls **__iter__** to get the next item. This type of function is called a generator function.
-	The **yield** command provides the next value in a **for* loop. It functions like a ** return** statement, but it doesn’t automatically end the function. This allows it to send out a value then let the function continue where it left off. If the generator function needs to have a different function **yield** its data, it will need to use the **yield from** keywords.
``` python
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
	This function does an in-order traversal through the 
	Binary search tree. 
	It starts by checking if the current node is real, (it has
	something in it.
	If there is something in it we will keep traversing to the left
	side until we run out of nodes, This means we will get to the 
	smaller numbers first.
	we will then provide (yield) the data from the current node,
	and then traverse the right nodes.
	(getting to the larger numbers last.)
	

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

```
### uses of tree
- A binary search tree is used when you have a very large sorted list that needs to be searched through quickly. seaching through a BST has a big-O effiecncy of O(log n) because each time you iterate through the search function, it will halve the remaining data.
### example problem: inserting into a BST using a loop.
- This example shows how to imlement a function that inserts a number in a BST  using a loop instead of using recursion. 
```python
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
        
    def search(self, number):
        curr = self.root
        while curr is not None:
            if number  < curr.data:
                curr = curr.left
            elif number > curr.data:
                curr = curr.right
            else:
                return curr.data
        return "The number is not in this tree."
            
        """
        This function is the search function that will look for an empty node to place data in.
    if the data is less than the data contained in the current node, it will try to place the 
    data in the left child node, and if it is greater than the data in the current node, it will
    place the data in the right child node. if the child node is already full, it will repeat the
    process until it finds an empty node.
        """
    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
            return
        else:
            curr = self.root
            while curr is not None:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = BST.Node(data)
                        return
                    else:
                        curr = curr.left
                elif data >= curr.data:
                    if curr.right is None:
                        curr.right = BST.Node(data)
                        return
                    else:
                        curr = curr.right

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(10)

for node in tree:
    print(node)

```
### practice problem
Implement a function that searches through a tree for a certain number using a loop instead of recursion.
Here is the [problem](https://github.com/PaulMDecker/cse212final-project/blob/main/tree_problem.py).
here is the [solution](https://github.com/PaulMDecker/cse212final-project/blob/main/tree_solution.py).
### search tree syntax
common BST Operations  |  description  | Big O Performance
-----------------------|---------------|-------------------
insert(value) | Insert a value into the tree. | O(log n) - Recursively search the subtrees to find the next available spot
remove(value) | Remove a value from the tree. | O(log n) - Recursively search the subtrees to find the value and then remove it. This will require some cleanup of the adjacent nodes.
contains(value) | Determine if a value is in the tree. | O(log n) - Recursively search the subtrees to find the value.
traverse_forward | Visit all objects from smallest to largest. | O(n) - Recursively traverse the left subtree and then the right subtree. 
traverse_reverse | Visit all objects from largest to smallest. | O(n) - Recursively traverse the right subtree and then the left subtree.
height(node) | Determine the height of a node. If the height of the tree is needed, the root node is provided. | O(n) - Recursively find the height of the left and right subtrees and then return the maximum height (plus one to account for the root).
size() | Return the size of the BST. | O(1) - The size is maintained within the BST class. 
empty() | Returns true if the root node is empty. This can also be done by checking the size for 0. | O(1) - The comparison of the root node or the size.

















