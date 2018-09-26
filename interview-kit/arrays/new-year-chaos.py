# https://www.hackerrank.com/challenges/new-year-chaos/problem


# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0

    carry_on = True
    while carry_on:
        carry_on = False
        last_briber = 0
        last_briber_count = 0
        for i in range(len(q) - 1):
            if q[i] > q[i + 1]:
                if last_briber != q[i]:
                    last_briber = q[i]
                    last_briber_count = 1
                else:
                    last_briber_count += 1
                    if last_briber_count > 2:
                        print('Too chaotic')
                        return

                temp = q[i]
                q[i] = q[i + 1]
                q[i + 1] = temp

                bribes += 1
                carry_on = True
    print(bribes)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
