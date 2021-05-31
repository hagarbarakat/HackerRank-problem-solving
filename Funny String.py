def funnyString(s):
    rev = []
    org = []
    for i in range(len(s)): 
        org.append(ord(s[i]))
    for i in range(len(s)-1, 0, -1):
        rev.append(ord(s[i]))
    for i in range(len(org)-2):
        if abs(org[i]-org[i+1]) != abs(rev[i]-rev[i+1]):
            return "Not Funny"
    return "Funny"
