#! /usr/bin/python3
# Trying to optimize bubble sort
# one problem with bubble sort is that it will try to sort a sorted array.
# To fix this, we can introduce a variable to check if a swap has happened
# if in one full iteration no swap has happened, then it means that it is sorted.

def swap(idx1, idx2, list):
    tmp = list[idx1]
    list[idx1] = list[idx2]
    list[idx2] = tmp

def bubble_sort(list):
    for i in range(0, len(list)):
        has_swapped = False
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                swap(i, j, list)
                has_swapped = True
            if has_swapped:
                continue
            else:
                return list
    return list

print(bubble_sort([1, 2, 3, 4, 5]))
print(bubble_sort([5, 3, 4, 1, 2]))
print(bubble_sort([10, 9, 8, 7]))
print(bubble_sort(['jack', 'zaph', 'andrew', 'ken']))
print(bubble_sort(["alvin", "jack", "mitshell", "veronicah", "zaphenath"]))
