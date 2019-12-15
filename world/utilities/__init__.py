def columns(string, sep=" ", cols=2, delim=" "):
    output = ""
    count = 0
    length = round(78 / cols)
    string = string.split(sep)
    string.sort()
    for word in string:
        if count < cols:
            w = word.strip()
            output += w + delim * (length - len(w))
            count += 1
        else:
            w = word.strip()
            output += "\n" + w + delim * (length - len(w))
            count = 0
    return output