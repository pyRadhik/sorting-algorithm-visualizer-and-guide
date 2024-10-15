## Selection Sort

**Description**

Selection sort repeatedly selects the minimum element from the unsorted portion of the array and swaps it with the first unsorted element.

**How It Works**

  1. Find the smallest element in the array
  2. Swap it with the first element in the array
  3. Repeat till list sorted

**Python Code**

```python
def selection_sort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i] 
  return arr
```

**Time Complexity**

- Best: O(n^2)

- Average: O(n^2)

- Worst: O(n^2)

**Space Complexity**

- O(1)

**Stability** 

- This algorithm is not stable

**Applications**

Honestly, it's not really used much outside of demonstration due to its inefficiency. But, it is a staple if you want a slow sorting process for any reason. 
