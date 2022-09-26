import sys


key = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}
big_string = ""
with open("cyrillic.txt", "r", encoding="utf-8") as file, \
        open("transliteration.txt", "w", encoding="utf-8") as file2:

    lines = [line.strip().split(' ') for line in file.readlines()]
    # big_string = ""
    for line in lines:
        string = ""
        for word in line:
            w = ""
            for ch in word:
                if ch.lower() in key and ch.isupper():
                    w += key[ch.lower()].capitalize()

                elif ch.lower() in key and ch.islower():
                    w += key[ch]

                else:
                    w += ch
            string += w + " "

        big_string += string.strip() + "\n"

    file2.write(big_string)
