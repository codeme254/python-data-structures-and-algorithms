#!/usr/bin/python3
"""Implementation of a Binary Search Tree in Python"""


class Node:
    """Anatomy of a node in the tree"""
    def __init__(self, value):
        """Initializes a node"""
        self.value = value
        self.right = None
        self.left = None
        self.number_of_occurences = 1


class BinarySearchTree:
    """Blueprint of a binary search tree"""
    def __init__(self):
        """Initializes a binary search tree"""
        self.root = None

    def insert(self, value):
        """Creates a new node with @value and puts it in the correct spot"""
        new_node = Node(value)
        # if there are no nodes in the tree, make this the root node
        if not self.root:
            self.root = new_node
            return new_node

        # otherwise, keep looping until you add that node to the correct spot
        should_keep_looping = True
        current_node = self.root
        while should_keep_looping:
            # check if the value of current node is greater than our new nodes
            if new_node.value > current_node.value:
                # we are adding to the right
                # check to see if there is a node to the right
                # if there is not, add new node if there is, make it current
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    should_keep_looping = False
            elif new_node.value < current_node.value:
                # we are adding to the left
                # check to see if there is a node to the left
                # if not, add new node there, if there is, make it current
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    should_keep_looping = False
            elif new_node.value == current_node.value:
                current_node.number_of_occurences += 1
                should_keep_looping = False
        return new_node

    def breadth_first_traversal(self):
        """Does a breadth first traversal on the tree"""
        # if there are no nodes in the tree, return None
        if not self.root:
            return None
        node_list = []
        queue = []
        # add the root node into the queue
        queue.append(self.root)
        # loop for as long as there are nodes in the queue/queue is not empty
        while len(queue) > 0:
            # remove the first element of the queue
            curr_node = queue.pop(0)
            # if the node has a left node, add it to the queue
            if curr_node.left:
                queue.append(curr_node.left)
            # if the node has a right node, add it to the queue
            if curr_node.right:
                queue.append(curr_node.right)
            # add the value of the node to node list
            node_list.append(curr_node.value)
        return node_list

    def depth_first_Preorder_Traversal(self):
        """Does depth first preorder traversal on the tree"""
        # traverse the entire left of a node then the entire right
        # if there are no nodes in the tree, return None
        if not self.root:
            return None

        # a way to store the value of the nodes visited
        visited_nodes = []
        # a helper function that accepts a node

        def traverse_helper(node):
            # push the value of the node to the variable that stores values
            visited_nodes.append(node.value)
            # if the node has a left property, call this function on the left
            if node.left:
                traverse_helper(node.left)
            # same case if the node has a right property
            if node.right:
                traverse_helper(node.right)
        # invoke the helper function with the root
        traverse_helper(self.root)
        return visited_nodes

    def depth_first_Postorder_traversal(self):
        """Does a postorder traversal on the tree"""
        # visit all the children of a node, then the node itself
        # if there are no nodes in the tree, return None
        if not self.root:
            return None

        # a variable to store all the visited nodes
        visited_nodes = []
        # a method to help in traversing, takes in a node

        def traverse_helper(node):
            # if the node has a left property, call the function on the left
            if node.left:
                traverse_helper(node.left)
            # same case to the right
            if node.right:
                traverse_helper(node.right)
            # push the value of the node itself
            visited_nodes.append(node.value)

        traverse_helper(self.root)
        return visited_nodes

    def depth_first_Inorder_traversal(self):
        """Does an inorder traversal on the tree"""
        # left, node, right
        # if there are no nodes, return None
        if not self.root:
            return None

        # a variable to store all the visited nodes
        visited_nodes = []

        def traverse_helper(node):
            # if the node has a left, call this function on the left
            if node.left:
                traverse_helper(node.left)
            # visit the node itself
            visited_nodes.append(node.value)
            # if the node has a right, call this function on the right
            if node.right:
                traverse_helper(node.right)

        traverse_helper(self.root)
        return visited_nodes


bst = BinarySearchTree()
bst.insert(50)
bst.insert(50)
bst.insert(40)
bst.insert(55)
bst.insert(30)
bst.insert(45)
bst.insert(55)
bst.insert(53)
bst.insert(60)
print(bst.breadth_first_traversal())
print(bst.depth_first_Preorder_Traversal())
print(bst.depth_first_Postorder_traversal())
print(bst.depth_first_Inorder_traversal())
