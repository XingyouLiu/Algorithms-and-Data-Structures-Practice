def removeStars(s):
    """
    :type s: str
    :rtype: str
    """
    ans = []
    for char in s:
        if char != '*':
            ans.append(char)
        else:
            ans.pop()

    return ''.join(ans)