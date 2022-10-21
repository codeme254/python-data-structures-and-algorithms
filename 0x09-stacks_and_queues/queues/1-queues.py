#!/usr/bin/python3
"""Implementation of a queue"""


import queue


class Node:
    """Defines a node class"""
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """Defines a queue class"""
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        """Adds a node at the end of the queue"""
        new_node = Node(value)
        # if no nodes in the queue, make this node the first and the last
        if not self.first or self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            # set the next property on the current last to be the new node
            # what we are doing here is adding at the end
            self.last.next = new_node
            # expliciltly set the last property of the queue to be the new node
            self.last = new_node
        # increment the length of the queue and return the queue
        self.length += 1
        return self

    def dequeue(self):
        """Removes the first node of the queue and returns it"""
        # if there are no nodes, return None
        if not self.first or self.length == 0:
            return None
        # if there is only one node, set the first and last to None
        if self.length == 1:
            # store the first to return it
            old_first = self.first
            self.first = None
            self.last = None
            self.length = 0
            return old_first
        # otherwise, grab the current first to return it later
        old_first = self.first
        # set the first property to be the next of the current first
        self.first = old_first.next
        # set the next of the old first to be null
        old_first.next = None
        self.length -= 1
        return old_first

    def traverse(self):
        """Traverses the queue and prints a list represetation of the queue"""
        q_list = []
        current = self.first
        q_list.append(current.value)
        while current.next:
            current = current.next
            q_list.append(current.value)
        print(q_list)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

queue.dequeue()
print("Length of the queue: {}".format(queue.length))
print("First: {}".format(queue.first.value))
print("Last: {}".format(queue.last.value))
queue.traverse()
