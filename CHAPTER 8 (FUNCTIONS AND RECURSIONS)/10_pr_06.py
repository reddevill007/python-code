def remove(string, word):
    newstr=string.replace(word, "")
    return newstr.strip()

this="    Harry is a good boy   "
n=remove(this,"Harry")
print(n)