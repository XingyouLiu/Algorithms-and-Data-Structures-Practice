def longest_common_prefix(str_array):
    if len(str_array) == 0:
        return ''

    min_words_num = min(len(s) for s in str_array)
    common_prefix = ''

    for i in range(min_words_num):
        current_char = str_array[0][i]
        for j in range(1, len(str_array)):
            if str_array[j][i] != current_char:
                return common_prefix
        common_prefix += current_char

    return common_prefix


print(longest_common_prefix(['flower','flow','flight']))




