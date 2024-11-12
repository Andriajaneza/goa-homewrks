def remove_char(s):
    if s is None:
        return ''
    if len(s) > 2:
        return s[1:-1]
    else:
        return ''