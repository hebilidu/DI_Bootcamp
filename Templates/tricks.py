def is_alphanum(str):
    ''' Equivalent to built-in isalnum()
    codes 48 to 57: numeric (0-9) / 65 to 90: upper alpha (A-Z) / 97 to 122: lower alpha (a-z)
    '''
    for char in str:
        code = ord(char)
        if not (47 < code < 58 or 64 < code < 91 or 96 < code < 123):
            return False
    return True

def is_alpha(str):
    ''' Equivalent to built-in isalpha()
    codes 48 to 57: numeric (0-9) / 65 to 90: upper alpha (A-Z) / 97 to 122: lower alpha (a-z)
    '''
    for char in str:
        code = ord(char)
        if not(64 < code < 91 or 96 < code < 123):
            return False
    return True
