def recursion(n, dp):
  if n == 1:
    dp[1] = 1
    return dp[1]
  elif n == 2:
    dp[2] = 1
    return dp[2]
  if not dp[n]:
    dp[n] = recursion(n-1, dp) + recursion(n-2, dp)
  return dp[n]

n = int(input())
print(recursion(n, [0] * (n+1)))