def check(lst):
    print(*lst)


def find(i):
    if i == k:
        check(a)
        return
    a[i] = 0
    find(i + 1)
    a[i] = 1
    find(i + 1)


k = int(input())
a = [None] * k
find(0)
