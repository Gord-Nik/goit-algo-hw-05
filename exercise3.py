def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def boyer_moore_search(text, pattern):
    def bad_char_heuristic(string, size):
        bad_char = {}
        for i in range(size):
            bad_char[string[i]] = i
        return bad_char

    m = len(pattern)
    n = len(text)
    bad_char = bad_char_heuristic(pattern, m)
    s = 0
    while(s <= n - m):
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

def rabin_karp_search(text, pattern, d=256, q=101):
    M = len(pattern)
    N = len(text)
    i = j = 0
    p = 0    # hash value for pattern
    t = 0    # hash value for text
    h = 1

    for i in range(M-1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N-M + 1):
        if p == t:
            for j in range(M):
                if text[i+j] != pattern[j]:
                    break
            else:
                return i
        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i+M])) % q
            if t < 0:
                t = t + q
    return -1


import timeit

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

text1 = read_file('article1.txt')

pattern1_exist = "ключові слова"  # Існуючий підрядок
pattern1 = "вигаданий текст"  # Вигаданий підрядок

text2 = read_file('article2.txt')
pattern2 = "зберігання даних"

def measure_time(func, text, pattern):
    setup_code = f"from __main__ import {func.__name__} as func"
    # Використання трійних кавичок для багаторядкових рядків
    stmt = f'''func("""{text}""", "{pattern}")'''
    times = timeit.repeat(stmt=stmt, setup=setup_code, repeat=3, number=10)
    return min(times)

kmp_time1 = measure_time(kmp_search, text1, pattern1)
bm_time1 = measure_time(boyer_moore_search, text1, pattern1)
rk_time1 = measure_time(rabin_karp_search, text1, pattern1)

kmp_time2 = measure_time(kmp_search, text2, pattern2)
bm_time2 = measure_time(boyer_moore_search, text2, pattern2)
rk_time2 = measure_time(rabin_karp_search, text2, pattern2)

print("------------------- Текст 1 -------------------------")
print("Кнута-Морріса-Пратта " + str(kmp_time1))
print("Боєра-Мура " + str(bm_time1))
print("Рабіна-Карпа " + str(rk_time1))

print("------------------- Текст 2 -------------------------")
print("Кнута-Морріса-Пратта " + str(kmp_time2))
print("Боєра-Мура " + str(bm_time2))
print("Рабіна-Карпа " + str(rk_time2))