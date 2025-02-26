def remove_char(s):
    s = list(s)
    s.remove(s[0])
    s.remove(s[-1])
    return ''.join(s)