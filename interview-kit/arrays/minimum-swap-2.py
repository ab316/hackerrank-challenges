# https://www.hackerrank.com/challenges/minimum-swaps-2/problem

#!/bin/python3

import os


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    num_swaps = 0
    done = False

    while not done:
        done = True
        for i in range(len(arr) - 1):
            current = arr[i]
            destination = current - 1
            if i != destination:
                temp = arr[i]
                arr[i] = arr[destination]
                arr[destination] = temp
                num_swaps += 1
                done = False

    return num_swaps


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(minimumSwaps(arr))
