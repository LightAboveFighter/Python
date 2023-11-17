"""
Задача 6: самая длинная подстрока без повторяющихся символов

Вам дана строка s. 
Найдите длину ДЛИННЕЙШЕЙШЕГО ПОДСЛОВА, 
в котором нет повторяющихся символов


def1:
    слово w называется ПОДСЛОВОМ слова s, если
    существуют слова x и y, такие что: s = x * w * y,    x + w + y в питоне
    т.е. x - это префикс слова s, а y - суффикс.

def2:
    слово, состоящее только из уникальных символов,
    будем называть ОСОБЫМ.

    
Нужно найти длину самого длинного особого подслова
"""

def lengthOfLongestSubstring(s: str) -> int:
    """ Подсчёт длины самого длинного подслова
        без повторяющихся символов

        Вход:
            s : str
                исходная строка, в которой ищется особое подслово
        
        Выход:
            subs_len: int
                длина максимального особого подслова 
    """
    cnt = 0
    if len(s) < 3:
        return len(set(s))
    
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if len(s[i:j]) == len(set(s[i:j])):
                cnt = max(cnt, len(s[i:j]))
    return cnt


if __name__ == "__main__":
    assert lengthOfLongestSubstring('abcabcbb') == 3
    assert lengthOfLongestSubstring('bbbbb') == 1
    assert lengthOfLongestSubstring('pwwkew') == 3     # 'pwke' является подпоследовательностью, 
                                                       # но не подсловом
print(lengthOfLongestSubstring(" "), lengthOfLongestSubstring("au"))