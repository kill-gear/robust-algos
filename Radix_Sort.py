"""Script for radix-sorting numbers and strings."""

from math import log, floor
from itertools import accumulate


def counting_sort_str(a, n):
    """Counting sort for string characters."""

    index = [0 for _ in range(60)]
    for i in range(len(a)):
        if n >= len(a[i]):
            pos = 0
        else:
            pos = ord(a[i][n]) - ord('A')
        index[pos] += 1
    index = list(accumulate(index))

    ans = [0] * len(a)
    for i in range(len(a)-1,-1,-1):
        if n >= len(a[i]):
            pos = 0
        else:
            pos = ord(a[i][n]) - ord('A')
        x = index[pos]
        ans[x-1] = a[i]
        index[pos] -= 1
    return ans


def counting_sort_int(a, n):

    index = [0 for _ in range(26)]

    for i in range(len(a)):
        index[a[i]//10**n % 10] += 1
    index = list(accumulate(index))

    ans = [0 for _ in range(0,len(a))]
    for i in range(len(a)-1,-1,-1):
        x = index[a[i]//10**n % 10]
        ans[x-1] = a[i]
        index[a[i]//10**n % 10] -= 1
    return ans


def radix_sort_str(names):
    m = max([len(val) for val in names])
    for i in range(m-1, -1, -1):
        names = counting_sort_str(names,i)
    return names


# For only integers
def radix_sort_int(nums):
    m = floor(log(max(nums), 10)) + 1
    for i in range(m):
        nums = counting_sort_int(nums,i)
    return nums


vals = input("Enter space-separated names / numbers: ").split()
try:
    vals = [int(x) for x in vals]
    print(radix_sort_int(vals))
except ValueError:
    print(radix_sort_str(vals))
