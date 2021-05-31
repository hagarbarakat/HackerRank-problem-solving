def camelcase(s):
    if len(s) == 0:
        return 0 
    num_of_words= 1 
    for chars in s: 
        if ord(chars)>= 65 and ord(chars)< 97: 
            num_of_words += 1
    return num_of_words