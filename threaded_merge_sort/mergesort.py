import concurrent.futures
import time 
import math 
import numpy as np
import matplotlib.pyplot as plt
import random
# Source for merge sort implementation:https://medium.com/@tuvo1106/merge-sort-in-python-5d9617fb9ee1 -. I had modified the code to the design in the docx.
# Python program for implementation of MergeSort 
  
def generate_list(size, max_n):
    """Generate n inique random unmbers withn range"""
    #Bron random.sample(range(1, 100), 3)
    return list(np.random.randint(low = 0,high=max_n,size=size))
 
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
    if left == len(list1):
        res.extend(list2[right:])
    else:
        res.extend(list1[left:])
    return res
  
def merge_sort(arr):
    """Sorts a list using recursion and helper merge function."""
    if len(arr) < 2:
        return arr
    mid = int(math.floor(len(arr) / 2))
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def split_list(arr, threads):
    """Split list  based on the amount of threads. This way the data is well distributd by the  threads """
    #bron : https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
    #Divide a list into chucks of size of the threads
    for i in range(0, len(arr), threads):
        yield arr[i:i + threads]

def execute_parallel(arr,threads):
    """Execute merge sort for n threads"""
    with concurrent.futures.ThreadPoolExecutor(threads) as executor:
        lst_split = list(split_list(arr, threads))
        lst = executor.map(merge_sort, arr)
    
def calculate_duration(arr,list_threads):
    duration = []
    for thread in list_threads:
        t1 = time.perf_counter()
        execute_parallel(arr, thread)
        t2 = time.perf_counter()

        duration.append(t2 - t1)
        print("Finished in {} seconds for {} threads".format(t2 - t1, thread))

    return duration

if __name__ == "__main__":
    threads = [1, 2, 4, 8]
    for i in [1000, 1000, 30000]:
        random_arr = generate_list(i, 100)
        res = calculate_duration(random_arr, threads)
        
        # I will be visualizing the duration per amoun of threads in a scatter plot. 
        plt.plot(threads, res)
        plt.title(f"Duration per amount of threads for list of {i} numbers")
        plt.show()

        print("\n")

    #The output (durations) when run
    #1000
# Finished in 0.0276208 seconds for 1 threads
# Finished in 0.02608240000000006 seconds for 2 threads
# Finished in 0.0515158 seconds for 4 threads
# Finished in 0.039763400000000004 seconds for 8 threads

    #10000
# Finished in 0.050768299999999655 seconds for 1 threads
# Finished in 0.0670737999999993 seconds for 2 threads
# Finished in 0.03791289999999936 seconds for 4 threads
# Finished in 0.03820880000000049 seconds for 8 threads

    #30000
# Finished in 1.3795575000000007 seconds for 1 threads
# Finished in 0.7821046000000003 seconds for 2 threads
# Finished in 0.9334650000000018 seconds for 4 threads
# Finished in 1.094138300000001 seconds for 8 threads 

# In comparison to the durations for sequential merge sort in asignment 1.1, the durations are for the list of 10000 and 30000 numbers immensely faster.
# For the list of 1000, the sequential merge sort performed better. A reason for this performance is that the sequential merge sort is a little differently iplemented than the paalle one.
# A reson why the aove implementation is/could be fasterthan the squential one, is that the above merge sort is divding the list an evenly distributing it among the amountof given threads.






 
  