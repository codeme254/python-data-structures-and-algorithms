#!/usr/bin/python3

# Implementation of selection sort
# Insertion sort places smaller values in the sorted position

# 1. Store the first element as the smallest value you've seen so far.
# 2. Compare this item to the next item in the array until you find the smallest
# NOTE: you save the index of the smallest value in the list
# 3. If a value is less than the minimum, swap the two of them
# 4. Repeat this with the next element in the array until the array is sorted.

def swap(idx1, idx2, list):
    tmp = list[idx1]
    list[idx1] = list[idx2]
    list[idx2] = tmp

def selection_sort(list):
    smallest_value_idx = 0
    for i in range(0, len(list)):
        smallest_value_idx = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest_value_idx]:
                swap(smallest_value_idx, j, list)
        smallest_value_idx += 1
    return list

print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 3, 4, 1, 2]))
print(selection_sort([10, 9, 8, 7]))
print(selection_sort(['jack', 'zaph', 'andrew', 'ken']))
print(selection_sort(["alvin", "jack", "mitshell", "veronicah", "zaphenath"]))
