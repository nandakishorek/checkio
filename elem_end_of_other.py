def checkio(words_set):
    for (i,str1) in enumerate(words_set):
        for (j,str2) in enumerate(words_set):
            if i != j and len(str1) > len(str2):
                if str1.rfind(str2) == len(str1)-len(str2):
                    return True                
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({u"hello", u"lo", u"he"}) == True, "helLO"
    assert checkio({u"hello", u"la", u"hellow", u"cow"}) == False, "hellow la cow"
    assert checkio({u"walk", u"duckwalk"}) == True, "duck to walk"
    assert checkio({u"one"}) == False, "Only One"
    assert checkio({u"helicopter", u"li", u"he"}) == False, "Only end"