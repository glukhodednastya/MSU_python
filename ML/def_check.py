"""
Требуется написать функцию check(s, filename), которая принимает на вход
строку – последовательность слов, разделенных пробелом и имя файла;
функция должна вывести в файл для каждого уникального слова в этой строке
число его повторений (без учёта регистра) в формате «слово количество»
"""
def check(s, filename):
    fname = open(filename, 'w')
    s = s.lower().split(" ")
    new_text = sorted(set(s))
    for i in new_text:
        res = i + ' ' + str(s.count(i))
        fname.write(res + '\n')
    fname.close()

