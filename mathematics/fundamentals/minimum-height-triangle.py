# https://www.hackerrank.com/challenges/lowest-triangle/problem

from math import *

base, area = map(int, input().split())
print(ceil(2 * area / base))
