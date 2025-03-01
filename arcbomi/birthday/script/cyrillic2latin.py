import pandas as pd

def kazakh_to_latin(text, mapping):
    result = ""  # 初始化一个空字符串用于存储转换后的文本
    for char in text:  # 遍历输入文本中的每个字符
        if char.lower() in mapping:  # 如果字符的小写形式在映射字典中
            translated_char = mapping[char.lower()]  # 获取对应的拉丁字母
            result += translated_char.upper() if char.isupper() else translated_char  # 保持原字符的大小写
        else:
            result += char  # 如果字符不在映射表中，保持不变
    return result  # 返回转换后的文本

# Kazakh Cyrillic to Latin mapping
kazakh_latin_map = {
    "а": "a", "ә": "ä", "б": "b", "в": "v", "г": "g", "ғ": "ğ", "д": "d", "e": "e", "ё": "ö", "ж": "j", "з": "z", "и": "i",
    "й": "i", "к": "k", "қ": "q", "л": "l", "м": "m", "н": "n", "ң": "ñ", "о": "o", "ө": "ö", "п": "p", "р": "r", "с": "s",
    "т": "t", "у": "u", "ұ": "ū", "ү": "ü", "ф": "f", "х": "h", "һ": "h", "ц": "s", "ч": "ch", "ш": "ş", "щ": "ş", "ъ": "",
    "ы": "y", "і": "ı", "ь": "", "э": "e", "ю": "iu", "я": "ıa"
}

# Read CSV file
df = pd.read_csv("a.csv")

# Convert names
df["name"] = df["name"].apply(lambda x: kazakh_to_latin(x, kazakh_latin_map))

# Write to new CSV file
df.to_csv("converted_a.csv", index=False)

# Print converted names
print(df)
