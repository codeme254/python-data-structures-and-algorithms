#!/usr/bin/python3
"""Implementation of a stack data structures: first in last out"""


class Node:
    """blueprint of a node"""
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """The stack class/blueprint"""
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, value):
        """Adds a new node to the top of the stack"""
        new_node = Node(value)
        # if there are no nodes in the stack, first and last is thew new node
        if self.size == 0 or not self.first:
            self.first = new_node
            self.last = new_node
        else:
            # if there are nodes, grab the current first node:
            old_first = self.first
            # reset the first property to be the newly created node
            self.first = new_node
            new_node.next = old_first
        # always increment the size and return the stack
        self.size += 1
        return self

    def pop(self):
        """Removes the node on the top of the stack and returns it"""
        # if there are no nodes in the stack, return None
        if self.size == 0 or not self.first:
            return None
        # if there is only one node, set the first and the last to be null
        if self.size == 1:
            old_first = self.first
            self.first = None
            self.last = None
            self.length = 0
            return self.first
        # store the current first node in a variable to return it later.
        old_first = self.first
        # make the first node to be the old first's next
        self.first = old_first.next
        # make the old first to have a next prop of None
        old_first.next = None
        self.size -= 1
        return old_first

    def traverse(self):
        """Traverses the stack and returns an list of all the nodes' values"""
        final_list = []
        current = self.first
        final_list.append(current.value)
        while current.next:
            current = current.next
            final_list.append(current.value)
        print(final_list)
        return final_list


stack = Stack()
stack.push(10)
stack.push(5)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(0)
stack.pop()
print("The size of the stack is: {}".format(stack.size))

print(stack.first.value)
print(stack.last.value)
stack.traverse()
