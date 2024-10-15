## Insertion Sort

**Description**

Insertion sort works by building the final sorted list one item at a time. The algorithm iterates through the list and inserts the element into its correct positions.

**How It Works**

  1. Assume the first element as sorted.
  2. Take the next element and insert it into the sorted party, shifting the larger element to the right
  3. Repeats process until organized

**Python Code**

```python
def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = key
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

A majority of us have subconciously been using insertion sort all the time! Say you have to line up in order of birthdays; you take one person and tell them to stand still, and then one person moves left or right according to the chronological order of their birthdays, then another person inserts himself into the those two, and this process goes on and on. You can do it with anything be it height, weight, playing cards, colors (if you have access to the color scale).
