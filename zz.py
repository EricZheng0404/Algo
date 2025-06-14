a = [1, 2, 3]

def summation(a):
    if not a:
        return 0
    return a[0] + summation(a[1:])

print(summation(a))