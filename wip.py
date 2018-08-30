from collections import OrderedDict

def rmDuplicateChars(s):
    return ''.join(OrderedDict.fromkeys(s))





s = 'abcc'
print(rmDuplicateChars(s))
