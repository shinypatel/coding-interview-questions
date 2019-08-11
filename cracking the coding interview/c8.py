def fibonacci(n):      # q1
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# reverse a string
def reverse(s):
    if len(s) < 2:
        return s
    else:
        return reverse(s[1:]) + s[0]


# print array elements
def print_recursively(a):
    if len(a) <= 1:
        print(a[0])
    else:
        print_recursively(a[:-1])
        print(a[-1])


# calculate a raised to the power of b
def power(a, b):
    if b == 0:
         return 1
    elif b == 1:
        return a
    else:
        return power(a, b-1) * a


def power_set(s):   # q3
    if len(s) == 0:
        return [[]]
    else:
        r1 = power_set(s[:-1])
        r2 = []
        for r in r1:
            r2.append(r + [s[-1]])
        return r1 + r2


def perms(s):   # q4
    if len(s) == 1:
        return [s]
    result=[]
    for i, v in enumerate(s):
        result += [v + p for p in perms(s[:i]+s[i+1:])]
    return result


def n_pairs_parenthesis(n):  # q5
    if n == 1:
        return ['()']
    else:
        n_pairs = set()
        for p in n_pairs_parenthesis(n - 1):
            n_pairs.add(p + '()')
            n_pairs.add('()' + p)
            if p.count('()') == 1:
                n_pairs.add('(' + p + ')')
        return n_pairs

# print(fibonacci(6))

# s = 'abcd'
# print(reverse(s))

# a = [i for i in range(5)]
# print_recursively(a)

# a, b = 3, 4
# print(power(a, b))

s = 'abc'
print(perms(s))

# s = [1, 2, 3, 4]
# print(power_set(s))

# print(n_pairs_parenthesis(3))