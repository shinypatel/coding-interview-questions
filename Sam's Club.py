# Big Data - Software Engineer

# brute force
def smallest_substr_len_with_max_unique_chars(s):
    result, max_unique_chars = 0, 0
    length = len(s)
    for i in range(length + 1, 0, -1):
        prev = result
        for start in range(length):
            end = start + i
            if end <= length:
                substr = s[start:end]
                unique_chars = len(set(substr))
                if max_unique_chars <= unique_chars:
                    max_unique_chars = unique_chars
                    result = len(substr)
        if result and result == prev:
            break
    return result


s = 'abccda'
print(smallest_substr_len_with_max_unique_chars(s))
