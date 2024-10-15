## Quick Sort

**Description**

Quick sort also uses divide-and-conquer. It uses pivotes to sort whether an element should go to the left or right of the pivot than selects another pivot till sorted. 

**How It Works**

  1. Selects pivot element
  2. Partitions array so elements less than pivot go left and greater than pivot go right
  3. Repeats for the left and right subarrays till whole list is sorted

**Python Code**

```python
def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[len(arr) // 2]
  left = [x for x in arr if x < pivot]
  middle = [x for x in arr if x == pivot]
  right [x for x in arr if x > pivot]
  return arr
```

**Time Complexity**

- Best: O(n log n)

- Average: O(n log n)

- Worst: O(n log n)

**Space Complexity**

- O(log n)

**Stability** 

- This algorithm is not stable

**Applications**

Quick sort is by FAR the most used sorting method due to its efficiency. It's used in many libraries like Python's sort() due to the "quick" aspect of the algorithm.
