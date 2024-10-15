## Merge Sort

**Description**

Merge Sort uses the classic strategy of divide-and-conquer. It recursively splits the array into halves then merges all the sub-arrays when they are sorted. 

**How It Works**

  1. Split array into two haves
  2. Recursively sort each half
  3. Merge sorted halves into one list

**Python Code**

```python
def merge_sort(arr):
  if len(arr) > 1:
    mid = len(arr) // 2
    left_half = arr[::mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = o

    while i < len(left_half) and  j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i += 1
      else:
        arr[k] = right_half[j]
        j += 1
      k += 1

    while i < len(left_half):
      arr[k] = left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      arr[k] = right_half[j]
      j += 1
      k += 1

  return arr
```

**Time Complexity**

- Best: O(n log n)

- Average: O(n log n)

- Worst: O(n log n)

**Space Complexity**

- O(n)

**Stability** 

- This algorithm is stable

**Applications**

Merge Sort is a crucial must-know as it is one of the best ways to organize large datasets due to its time complexity. It's used in search engines to combine results giving the user a stronger answer and if your big on coding, it's best for Linked Lists. 
