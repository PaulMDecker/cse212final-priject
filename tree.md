# tree
### Introduction
-A linked list is a data structure where data is stored in nodes, and the nodes are connected by pointers. A tree is like a linked list except that in a tree a node can be connected to multiple nodes.  



### binary tree
-A binary tree is a tree where each node only connects to two other nodes. The root of a binary tree is the node that points to other nodes and has no nodes pointing to it. A root node is also a parent node because it is pointing to other nodes. A node that is being pointed to is called a child node and the node that is doing the pointing is called a parent node. A node that has a parent node, but no child nodes is called a leaf node. A parent and its child nodes is called a subtree.
<img width="662" alt="Screen Shot 2022-03-30 at 1 59 30 PM" src="https://user-images.githubusercontent.com/97462627/160920621-959f7e8a-ff1f-4cea-bbf4-2a7fd6f72f6a.png">

### binary search tree
-A binary search tree is a tree that has certain rules for how data is stored inside it. The data is compared to the data inside the parent tree, and if it is smaller than the parent tree, it is put in the left child node, and if it is bigger it is put in the right child node. If the tree allows duplicates, it can go in either of the child nodes.
<img width="448" alt="Screen Shot 2022-03-31 at 7 14 56 AM" src="https://user-images.githubusercontent.com/97462627/161063601-5440038a-f576-44e7-9a70-ef130b228b77.png">
### inserting into a tree
-Binary search tree operations are very complicated because almost all of them require recursion to work. Inserting a number into a tree must be done with recursion because a loop can’t tell how many times it will need to run in this case because the branches of the tree can be a different length.
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
### uses of tree
### example
- navigate with a tree without recursion
- use loop
### problem
- insert into a tree
### search tree syntax

