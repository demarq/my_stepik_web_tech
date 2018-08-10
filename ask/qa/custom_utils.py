import re


def startsWithWrongSymbol(login):
    return login.startswith(re.sub('[\w,\d]', '', login))


def containWrongSymbols(strng):
    return re.findall('[^\d,\w,\_]', strng)