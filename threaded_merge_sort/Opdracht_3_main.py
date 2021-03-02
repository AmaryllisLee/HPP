from merge_Sort_example import MergeSort

lst = [38, 27, 43, 3, 9, 82, 10]
print(lst)
first = MergeSort(lst, 0, len(lst)-1)
first.start()
first.join()

print(lst)
