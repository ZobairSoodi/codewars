import re
def duplicate_encode(word):
    temp_word = ""
    for i in word:
        i = re.escape(i)
        if len(re.findall(pattern = i, string = word, flags=re.IGNORECASE)) > 1:
            temp_word+=")"
        else:
            temp_word+="("
    return temp_word
