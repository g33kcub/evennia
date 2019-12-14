def wrap(string="", width=78):
    str_list = string.split()
    
    output = ""
    line = ""
    for w in str_list:
        if len(w + line) > width:
            output += ("\n%s" % line).lstrip()
            line = "%s " % w
        else:
             line += "%s " % w
    output +=  " " + line + "\n"
    return output