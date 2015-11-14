"""
http://www.checkio.org/mission/right-to-left/
 @author Nandakishore K
"""
import string

def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    i = 1
    result = []
    for s in phrases:
       result.append(string.replace(s, "right", "left"))
       if i < len(phrases):
           result.append(",")
       i = i + 1
    return "".join(result)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
