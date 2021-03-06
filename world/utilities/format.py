from evennia.utils.ansi import strip_ansi


def header(string, fill="|113-|n", length="78", lframe="|113[|n", rframe="|113]|n", just="left", offset=0):
    """
    Create a header for different areas of the game.
    """
    str_len = int(length) - round(len(strip_ansi(string)) + len(strip_ansi(lframe)) +  len(strip_ansi(lframe))) - offset
    if just.lower() == "left":
        return fill * offset + lframe + string + rframe + fill * str_len + "\n"
    else: return fill * str_len + lframe + string + rframe + fill * offset +  "\n" 


def wrap(string="", width=78, indent=0, fill=" "):
    "Wrao a string to fit a specified width"
    str_list = string.split()
    
    output = fill * indent
    line = ""
    for w in str_list:
        if len(w + line) >= width - indent:
            output += ("%s\n" % line).lstrip()
            line = "|n" + fill * indent + "%s " % w
        else:
            line += "%s " % w
    output += line
    return output


def columns(string, sep=" ", cols=2, delim=" ", offset=0):
    "Split a string into columns"
    output = ""
    count = 0
    length = round(78 / cols)
    string = string.split(sep)
    string.sort()
    for word in string:
        if count < cols:
            output += trail(delim * offset + word, length=length, delim=delim)
            count += 1
        else:
            output += "\n" + trail(delim * offset + word, length=length, delim=delim)
            count = 1
    return output


def display_time(seconds):
    "Format the idle time of players from seconds into (d h m s) format."
    N = int(seconds)
    container = []
    min = 60
    hour = 60 * 60
    day = 60 * 60 * 24
    
    DAY = N // day
    HOUR = N // hour
    MINUTE = (N - (HOUR * hour)) // min
    SECONDS = N - ((HOUR * hour) + (MINUTE * min))
    
    if N == 0: return "0s"
    else: 
        if DAY: container.append("%sd" % DAY)
        if HOUR: container.append( "%sh" % HOUR)
        if MINUTE: container.append("%sm" % MINUTE)
        if seconds: container.append( "%ss" % SECONDS)

    return " ".join(container[:2]) + "|n" if not DAY else "".join(container[:1])


def trail(string, length=26, tail="...", dir ="left", delim=" "):
    l = length - len(tail)
    
    if len(strip_ansi(string)) <= l:
        if dir.lower() == 'left': return string + delim * (length - len(strip_ansi(string)))
        else: return  delim * (length - len(strip_ansi(string))) + string
    else: return string[:l] + tail


def cap_str(string):
    return " ".join(map(lambda x: "".join(x[0].upper() + x[1:]), string.split()))
