import re
from collections import OrderedDict
from collections import Counter


def unique_chars(s):     # q1
    return len(set(s)) == len(s)


# a[n:m:k] returns every kth element from n to m
def rev_c_str(s):     # q2
    s = s[:-1]
    s = s[::-1]
    return s + '\0'


def rmDuplicateChars(s):    # q3
    return ''.join(OrderedDict.fromkeys(s))


def anagrams(s1, s2):   # q4
    return Counter(s1.lower()) == Counter(s2.lower())


def replace_whitespace(s):    # q5
    return re.sub('\s', '%20', s)


def mod_mat(m, n, mat):     # q7
    mod_rows, mod_cols = set(), set()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                mod_rows.add(i)
                mod_cols.add(j)

    for i in range(m):
        for j in range(n):
            if i in mod_rows or j in mod_cols:
                mat[i][j] = 0

    return mat


def str_rot(s1, s2):    # q8
    return len(s1) == len(s2) and s2 in s1 + s1


s = ' aa bc '
# print(unique_chars(s))
# print(rev_c_str(s))
# print(rmDuplicateChars(s))

# s1, s2 = 'Earth', 'Heart'
# print(anagrams(s1, s2))
# print(replace_whitespace(s))

m, n = 3, 3
mat = [[1 for j in range(3)] for i in range(3)]
mat[0][2], mat[1][1] = 0, 0
# print(mod_mat(m, n, mat))

s1, s2 = 'we', 'awe'
print(str_rot(s1, s2))