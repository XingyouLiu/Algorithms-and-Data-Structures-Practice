def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    length = len(s)
    reversed_str = ''
    help_str = ''
    is_space = 1
    word_count = 0

    for i in range(length - 1, -1, -1):
        print(help_str)
        if i > 0:
            if s[i] != ' ':
                if is_space == 1:
                    is_space = 0
                    word_count += 1
                help_str += s[i]

            elif s[i] == ' ':
                if is_space == 0:
                    is_space = 1
                    if word_count > 1:
                        reversed_str += ' '
                    reversed_str += help_str[::-1]
                    help_str = ''

        elif i == 0:
            if s[i] != ' ':
                help_str += s[i]
                if word_count > 1:
                    reversed_str += ' '
                reversed_str += help_str[::-1]
            elif s[i] == ' ':
                if is_space == 0:
                    if word_count > 1:
                        reversed_str += ' '
                    reversed_str += help_str[::-1]

    return reversed_str


print(reverseWords('  hello world  '))