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


def make_header(string):
    """
    Create a header for the different portions of the room parent.
    """
    length = 78 - (len(string) + 4)
    return "|113[|w " + string + " |113]|n" + "|113-|n" * length + "\n"


def wrap(string="", width=78):
        str_list = string.split()
        
        output = ""
        line = ""
        for w in str_list:
            if len(w + line) >= width:
                output += ("%s\n" % line).lstrip()
                line = "%s " % w
            else:
                line += "%s " % w
        output += line
        return output

def display_time(seconds):
    N = int(seconds)
    min = 60
    hour = 60 * 60
    day = 60 * 60 * 24
    output = "" 
    HOUR = N // hour
    MINUTE = (N - (HOUR * hour)) // min
    SECONDS = N - ((HOUR * hour) + (MINUTE * min))
    
    if HOUR: 
        output += "%sh " % HOUR
    
    if MINUTE:
        output += "%sm " % MINUTE
    
    if seconds:
        output +=  "%ss" % SECONDS
    
    return output
