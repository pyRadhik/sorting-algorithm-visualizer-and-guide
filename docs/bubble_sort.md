## Bubble Sort

**Description**

Bubble sort compares adjacent element in the array and swaps them if they are in the wrong order. This process repeats until the array is sorted. Each pass "bubbles the largest element to its correct position, hence the name.

**How It Works**

  1. Compares each adjacent pair of elements
  2. Swap them if they are in the wrong order
  3. Repeats process for every pair in the list until organized

**Python Code**

```python
def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
  return arr
```

**Time Complexity**

- Best: O(n)

- Average: O(n^2)

- Worst: O(n^2)

**Space Complexity**

- O(1)

**Stability** 

- This algorithm is stable

**Applications**

Bubble Sort is an entry-level algorithm. It is commonly usaed as the gateway to introduce students of computer science to sorting algorithms. Due to its simplicity, it can be used to sort small datasets, but don't count on it doing anything advanced.
