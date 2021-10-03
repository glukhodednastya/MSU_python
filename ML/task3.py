"""
Требуется написать функцию
longestCommonPrefix(x), которая принимает список строк и возвращает
наибольший общий префикс для строк в списке строк.
"""
def longestCommonPrefix(x):
    if not x:
        return ''
    short_word = min(x).strip()
    long_word = max(x).strip()
    for count, value in enumerate(short_word):
        if value != long_word[count]:
            return short_word[:count]
    return short_word



