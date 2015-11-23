def checkio(str_number, radix):
    str_number = str_number.lower()
    result = 0
    i = len(str_number) - 1
    while i > -1:
        ch = str_number[i]
	if ch.isdigit():
	    d = int(ch)
        else:
	    d = ord(ch) - ord('a') + 10
	if d >= radix:
	    return -1
        result += d * radix ** (len(str_number) - i - 1)
        i -= 1

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"AF", 16) == 175, "Hex"
    assert checkio(u"101", 2) == 5, "Bin"
    assert checkio(u"101", 5) == 26, "5 base"
    assert checkio(u"Z", 36) == 35, "Z base"
    assert checkio(u"AB", 10) == -1, "B > A > 10"
