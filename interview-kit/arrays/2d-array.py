# https://www.hackerrank.com/challenges/2d-array/problem

arr = []
for i in range(6):
    arr.append(list(map(int, input().split())))

max_sum = -100000

for r in range(1, 5):
    for c in range(1, 5):
        hourglass_sum = sum(arr[r-1][c-1:c+2]) + sum(arr[r+1][c-1:c+2]) + arr[r][c]
        if hourglass_sum > max_sum:
            max_sum = hourglass_sum

print(max_sum)
