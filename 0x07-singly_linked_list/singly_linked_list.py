#!/usr/bin/python3
# Implementation of a singly linked list.

# The node class

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# The whole singly linked list class.


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        """Adds a new node at the end of the list"""
        new_node = Node(value)
        # if the list is empty, make this node to be the head and the tail
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            # if there is a tail, make this node the tail
            self.tail.next = new_node
            # make this new node to be the tail
            self.tail = new_node
        # increment the length of the list and return the list.
        self.length += 1
        return self

    def pop(self):
        """Removes a value from the end of the linked list and returns it"""
        # if there is no node in the list, return undefined
        if not self.head:
            return None
        # we need to loop until we reach the tail.
        # set the second to last element's next property to be None
        current = self.head
        new_tail = current  # initially, the two pointers will start together
        while current.next:
            # if there is a next node:
            # we make it current and the curren node to be the temporaray tail.
            new_tail = current
            current = current.next
        # make the node next to the current pointer which is the tail to point
        # to None
        new_tail.next = None
        self.tail = new_tail
        self.length -= 1
        # if the length is zero, we reset the list:
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def shift(self):
        """Removes a node at the start of the list and returns it"""
        # if there are no nodes, return None
        if not self.head or self.length == 0:
            return None
        else:
            old_head = self.head
            # get the element next to the head since it will be the new head.
            new_head = self.head.next
            # Make the head's next property to be None
            self.head.next = None
            # Make that node next to the head to be the new head.
            self.head = new_head
            self.length -= 1
        return old_head

    def unshift(self, value):
        """Adds a node to the beginning of the list and returns it"""
        # create a new node using the value passed into the function
        new_node = Node(value)
        # if there are no nodes, set this to be the head and the tail
        if not self.head or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # make this node's next pointer to be the current head.
            new_node.next = self.head
            # set the head property of the list to be the newly created node.
            self.head = new_node
        # increment the length and return the list.
        self.length += 1
        return self

    def get(self, idx):
        """Returns the node at a given position using zero indexing"""
        # validate the index, if less than 0 and >= list length.
        if idx < 0 or idx >= self.length:
            return None
        # if the index is 0, return the head.
        if idx == 0:
            return self.head
        # if the index is equal to length - 1, return the tail.
        if idx == self.length - 1:
            return self.tail
        # otherwise, loop the list for as many time as the index.
        # return the node at where the loop ends.
        current = self.head
        for i in range(0, idx):
            current = current.next
        return current

    def set(self, idx, new_value):
        """changes the value of a node at a given position in the list"""
        # we use the get function to get the node.
        node = self.get(idx)
        # if a node is not found, return false or None
        if not node:
            return None
        # otherwise, reassing the value of the node and return the node.
        node.value = new_value
        return node

    def insert(self, idx, new_node_value):
        """Inserts a new node at a given index"""
        # validate the index and return None if the index is bad
        if idx < 0 or idx >= self.length:
            return None
        # if the index is zero, push the node.
        if idx == 0:
            self.unshift(new_node_value)
        # if the index is equal to the length - 1, we push the value.
        elif idx == self.length - 1:
            self.push(new_node_value)
        else:
            new_node = Node(new_node_value)
            # use the get method to acces node at idx-1
            tmp_node = self.get(idx - 1)
            # store the node's next value to remember it.
            tmp_node_next = tmp_node.next
            # make tmp_node's next to be thisnew node.
            tmp_node.next = new_node
            # make the new node's next to be what tmp node next was.
            new_node.next = tmp_node_next
            # increment the length of the list and return this new node.
            self.length += 1
            return new_node

    def remove(self, idx):
        """removes a node from list at a given position and returns it"""
        # validate the index passed
        if idx < 0 or idx >= self.length:
            return None
        # if the index is zero, we should shift
        if idx == 0:
            self.shift()
        elif idx == self.length - 1:
            self.pop()
        else:
            # store the node to be removed
            removed_node = self.get(idx)
            # get node at idx - 1 and set its next to be the next of next node.
            # this will delete the node at idx.
            tmp_node = self.get(idx - 1)
            # set it's next to be next of the next node.
            tmp_node.next = removed_node.next
            # decrement the length and return the removed node.
            self.length -= 1
            return removed_node

    def traverse_list(self):
        """Traverses the singly linked list and adds the nodes into an array"""
        vals_array = []
        current = self.head
        vals_array.append(current.value)
        while current.next:
            current = current.next
            vals_array.append(current.value)
        print(vals_array)


sll = SinglyLinkedList()
sll.push(25)
sll.push(30)
sll.push(18)
sll.push(34)
# print(sll.pop())
sll.shift()
# add another node.
sll.unshift(5)
print(sll.get(3))
sll.set(2, 36)
sll.insert(2, 40)
# sll.shift()
sll.remove(2)
print(sll.length)
sll.traverse_list()
