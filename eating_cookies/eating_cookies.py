#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  combos = 0
  if n == 0:
    combos += 1
    return combos
  if cache is not None:
    if (cache[n] > 0):
      return cache[n]
  if (n >= 3):
    combos += eating_cookies(n - 3, cache)
    if cache is not None:
      cache[n] = combos
  if (n >= 2):
    combos += eating_cookies(n - 2, cache)
    if cache is not None:
      cache[n] = combos
  if (n >= 1):
    combos += eating_cookies(n - 1, cache)
    if cache is not None:
      cache[n] = combos

  return combos

  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')