

## What is Recursion?
- recursion is a problem solving method
- in code, recursion is implemented using a function that calls itself

- The opposite of a recursive algorithm would be an iterative algorithm
  - Iterative algos use for loops and while loops to simulate repetition
  - Recursive algorithms use function calls to simulate the same logic

Iterateve Algorithm
- print numbers from 1 to 10
```python
for (i = 1; i <= 10; i++) {
    print(i)
}
```

Recursive Algo
```python
def fn(i):
  if i > 3:
    return 

  print(i)
  fn(i + 1)
  print(f'End of call where i = {i}')
  return

fn(1)
```

### Breaking Problems Down
- where recursion shines is when you use it to break down a problem into "subproblems"
  - subproblem solutions can then be combined to solve the original problem.

- we need base cases with any recursive function

```python
def F(n):
    if n <= 1:
        return n

    oneBack = F(n - 1)
    twoBack = F(n - 2)
    return oneBack + twoBack
```