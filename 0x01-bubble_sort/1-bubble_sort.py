#!/usr/bin/python3

# Implementation of bubble sort with python.
# Bubble sort is a sorting algorithm where larger values bubble to the top.
# we compare each item to the next
# If it is bigger than the neighbor, we swap

def swap(idx1, idx2, list):
    tmp = list[idx1]
    list[idx1] = list[idx2]
    list[idx2] = tmp


def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                swap(i, j, list)
    return list

print(bubble_sort([5, 3, 4, 1, 2]))
print(bubble_sort([10, 9, 8, 7]))
print(bubble_sort(['jack', 'zaph', 'andrew', 'ken']))
