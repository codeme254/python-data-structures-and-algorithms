#!/usr/bin/python3
"""Implementation of a doubly linked list in Python"""

# The node class


class Node:
    """The  blueprint of a real dll node"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


"""The doubly linked list class"""


class DoublyLinkedList:
    """The blueprint of a doubl linked list"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        """Adds a node at the end of the doubly linked list"""
        new_node = Node(value)
        # if the list is empty, make this node the head and the tail.
        if not self.head or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # if the list has elements:
            # set the next property of the tail to be this new node.
            # then set the previous property of this new node to be the tail
            self.tail.next = new_node
            new_node.previous = self.tail
            # explicitly set the tail to be the newly created node.
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        """Removes a node at the end of the DoublyLinkedList and return it"""
        # if the list is empty, return None
        if not self.head or self.length == 0:
            return None
        # store the current tail in a variable to return it later.
        current_tail = self.tail
        # if the length of the list is 1, set the head and the tail to be None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # otherwise, update the tail to be current tail's previous node.
            self.tail = current_tail.previous
            # explicitly set the new tail's next to be None
            self.tail.next = None
        # decrement the length and return the removed value
        self.length -= 1
        return current_tail

    def shift(self):
        """Removes a node at the beginning of the list and returns it"""
        # if there are no elements in the list, return None
        if not self.head or self.length == 0:
            return None
        # otherwise, store the current head in a variable to return it later
        current_head = self.head
        # if the length of the list is 1, set the head and the tail to be None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # set the head to be head's next node.
            self.head = current_head.next
            # set the new head's previous to be None
            self.head.previous = None
            # set the old head's next property to be None
            current_head.next = None
        # decrement the length of the list and return the removed head
        self.length -= 1
        return current_head

    def unshift(self, value):
        """Adds a node at the beginning of the list, returns updated list"""
        new_node = Node(value)
        # if the list is emtpy, set the head and the tail to be this new node
        if not self.head or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # set the previous property on the current head to be this new node
            self.head.previous = new_node
            # set the next property of the new node to be the current head
            new_node.next = self.head
            # update the head of the list to be this new node.
            self.head = new_node
        # increment the length of the list and return the updated list.
        self.length += 1
        return self

    def get(self, idx):
        """Accesses a node at a list based on the index, uses zero indexing"""
        # index should be >= 0 and < length of the list minus 1, validate this
        if idx < 0 or idx >= self.length:
            return None
        # if the index is zero, return the head.
        if idx == 0:
            return self.head
        # if the idx is equal to length of list minus 1, return tail.
        if idx == self.length - 1:
            return self.tail
        # otherwise, loop for as long as idx and return the node of idx stop
        current = self.head
        for i in range(0, idx):
            current = current.next
        return current

    def set(self, idx, new_value):
        """Replaces the value of a node is a doubly linked list"""
        # grab the node using the get method
        node = self.get(idx)
        # if the get method returns a valid node, change that node's value
        # to be what has been passed into the function
        if node:
            node.value = new_value
            return node
        return None

    def insert(self, idx, new_node_value):
        """Inserts a new node into the list at a given position"""
        # validate the index:
        if idx < 0 or idx >= self.length:
            return None
        # create a new node with the value passed in
        new_node = Node(new_node_value)
        # if the index is 0, unshift this node
        if idx == 0:
            self.unshift(new_node_value)
        # if the index is equal to length - 1, push it.
        if idx == self.length - 1:
            self.push(new_node_value)
        # otherwise, use the get method to get idx - 1
        tmp_node = self.get(idx - 1)
        # make all the necessary connections
        current_tmp_node_next = tmp_node.next
        tmp_node.next = new_node
        new_node.previous = tmp_node
        new_node.next = current_tmp_node_next
        current_tmp_node_next.previous = new_node
        # increment the length and return the updated list.
        self.length += 1
        return self

    def remove(self, idx):
        """Removes a node at a given index, uses zero indexing"""
        # check if the index is valid
        if idx < 0 or idx >= self.length:
            return None
        # if the index is 0, then shift
        if idx == 0:
            self.shift()
        # if the index is equal to length - 1, then pop
        if idx == self.length - 1:
            self.pop()
        # otherwise, use the get method to retrieve the node to be removed.
        node_to_be_removed = self.get(idx)
        # change all the connections
        node_to_be_removed_next = node_to_be_removed.next
        node_to_be_removed_previous = node_to_be_removed.previous
        node_to_be_removed_previous.next = node_to_be_removed_next
        node_to_be_removed_next.previous = node_to_be_removed_previous
        # make the next and previous of the node removed to be None
        node_to_be_removed.next = None
        node_to_be_removed.previous = None
        # decrement the length and return the removed node
        self.length -= 1
        return node_to_be_removed

    def traverse(self):
        """Traverses the list and pushes the nodes' values into an list"""
        final_list = []
        current = self.head
        final_list.append(current.value)
        while current.next:
            current = current.next
            final_list.append(current.value)
        print(final_list)


dll = DoublyLinkedList()
dll.push(10)
dll.push(15)
dll.push(25)
dll.push(37)
dll.pop()
dll.shift()
dll.unshift(4)
dll.unshift(2)
dll.set(0, 8)
print(dll.set(30, 5))
dll.insert(2, 10)
dll.remove(1)
print(dll.get(1).value)

print(dll.length)
dll.traverse()
