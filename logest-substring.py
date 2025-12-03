def logest_substring(s):
    max_len=0
    start_index = 0
    left = 0
    char_set = set()

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        max_len = max(max_len,right-left+1)

        if right-left+1 > max_len:
            max_len = right-left+1
            start_index = left
    return s[start_index:start_index+max_len]
print(logest_substring("abcabcbb"))
