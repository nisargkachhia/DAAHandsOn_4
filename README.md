# DAAHandsOn_4

Fibonacci Function Analysis**

```markdown
# Fibonacci Function Analysis

## Problem Statement:
Analyze the time complexity of the Fibonacci function using recursion.

## Fibonacci Function (Recursive):
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
## Input Example:
fib(5)
## Expected Output:
5

```
# Problem 1: Merge K Sorted Arrays

## Problem Statement:
Given K sorted arrays of size N each, the task is to merge them all while maintaining their sorted order.

## Input Example:
```python
K = 3
N = 4
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]

## Expected Output:
Merged array:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```
## Time Complexity:

Using a min heap (priority queue), the time complexity of merging K sorted arrays is O(N * log K), where N is the total number of elements and K is the number of arrays.

# Problem 2: Remove Duplicates from a Sorted Array**

## Problem Statement:
Given a sorted array, the task is to remove duplicate elements in place.

## Input Example:
```bash
Enter a sorted array: 2 1 2
Original array (sorted):  [1, 2, 2]
Array after removing the duplicate elements:  [1, 2]

Process finished with exit code 0
