import concurrent.futures
import time 
import math 
# Source for merge sort implementation:https://medium.com/@tuvo1106/merge-sort-in-python-5d9617fb9ee1
# Python program for implementation of MergeSort 
  
 
def merge(list1, list2):
    """Merges two sorted lists."""
    left = 0
    right = 0
    res = []
    while left < len(list1) and right < len(list2):
        if list1[left] <= list2[right]:
            res.append(list1[left])
            left += 1
        else:
            res.append(list2[right])
            right += 1
    while left < len(list1):
        res.append(list1[left])
        left += 1
    while right < len(list2):
        res.append(list2[right])
        right += 1
    return res
  
def merge_sort(arr):
    """Sorts a list using recursion and helper merge function."""
    if len(arr) < 2:
        return arr
    mid = int(math.floor(len(arr) / 2))
    left = arr[0:mid]
    right = arr[mid:len(arr)]
    return merge(merge_sort(left), merge_sort(right))
  
# Determine by test the run-time complexity of your implementation when using 1, 2, 4, ... threads / processes. Plot this in a graph.
if __name__ == "__main__":
        t1 = time.perf_counter()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            arr = [12, 11, 13, 5, 6, 7]
            f1 = executor.submit(merge_sort,arr)
            print(f1.result())
        t2 = time.perf_counter()

    print("Finished in {} seconds".format(round(t2 - t1, 2)))
    







 
  