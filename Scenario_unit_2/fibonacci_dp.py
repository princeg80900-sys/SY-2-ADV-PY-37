def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

def generate_fib_memo(n):
    return [fib_memo(i) for i in range(n)]

def generate_fib_tabulation(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    dp = [0] * n
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp

N = 10

memo_sequence = generate_fib_memo(N)
tab_sequence = generate_fib_tabulation(N)

print("1. Fibonacci Using Memoization:")
print(f"Sequence: {memo_sequence}")
print("\n2. Fibonacci Using Tabulation:")
print(f"Sequence: {tab_sequence}")

"""
OUTPUT:

1. Fibonacci Using Memoization:
Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

2. Fibonacci Using Tabulation:
Sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""
