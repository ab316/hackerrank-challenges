# https://www.hackerrank.com/challenges/game-with-cells/problem

from math import *

n, m = map(int, input().split())

if n % 2:
    n += 1

if m % 2:
    m += 1

print(n*m//4)
