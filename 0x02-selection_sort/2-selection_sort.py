#!/usr/bin/python3
def swap(idx1, idx2, list):
    tmp = list[idx1]
    list[idx1] = list[idx2]
    list[idx2] = tmp

def selection_sort(list):
    for i in range(0, len(list)):
        smallest_value_idx = i
        for j in range(i + 1, len(list)):
            if list[j] < list[smallest_value_idx]:
                swap(smallest_value_idx, j, list)
    return list

print(selection_sort([1, 2, 3, 4, 5]))
print(selection_sort([5, 3, 4, 1, 2]))
print(selection_sort([10, 9, 8, 7]))
print(selection_sort(['jack', 'zaph', 'andrew', 'ken']))
print(selection_sort(["alvin", "jack", "mitshell", "veronicah", "zaphenath"]))
