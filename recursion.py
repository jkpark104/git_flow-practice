def recursion(n):
  if n == 1 or n == 2:
    return 1

  return recursion(n-1) + recursion(n-2)