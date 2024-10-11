def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    length_s = len(s)
    length_t = len(t)
    i = j = 0
    while j <= length_t - 1:
        if i == length_s:
            break
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == length_s