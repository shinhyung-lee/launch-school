
# refactor the code to use memoization
def fibonacci(nth):
    memo = {}

    if nth <= 2:
        return 1
    elif nth in memo:
        return memo[nth]
    else:
        memo[nth] = memo[nth - 1] + memo[nth - 2]
        return memo[nth]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True