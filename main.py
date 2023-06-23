from search import binary_search
from sort import bubble_sort

num = [5, 6, 7, 4, 8, 9, 1, 2, 3]
sorted_num = bubble_sort(num)
print(sorted_num)

val = 5
index = binary_search(val, sorted_num)
print(index)