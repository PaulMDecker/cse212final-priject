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
