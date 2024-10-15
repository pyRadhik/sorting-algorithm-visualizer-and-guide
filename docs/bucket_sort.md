## Bucket Sort
**Description**

Bucket sort works by dividing elements into many 'buckets,' then sorts each bucket individually, often involving another sorting algorithm.

**How It Works**

  1. Distribute elements into bucket based on value
  2. Sort each bucket using sorting algorithm *(Insertion Sort is often used here)*
  3. Concatenate (chain together) the sorted buckets

**Python Code**

```python
def bucket_sort(arr):
    bucket = [[] for _ in range(len(arr))]

    for num in arr:
        index = int(num * len(arr))
        bucket[index].append(num)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    result = []
    for i in range(len(arr)):
        result.extend(bucket[i])

    return result
```

**Time Complexity**

- Best: O(n + k)

- Average: O(n + k)

- Worst: O(n + k)

**Space Complexity**

- O(n + k)

**Stability** 

- This algorithm is stable

**Applications**

Bucket Sort is the best for sorting floating=point numbers within a specific range. 
