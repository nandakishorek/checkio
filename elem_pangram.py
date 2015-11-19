import string

def check_pangram(text):
    counts = dict.fromkeys(string.ascii_lowercase, 0)
    for ch in text.lower():
        try:
            counts[ch] += 1
        except KeyError:
            pass
    
    for ch, count in counts.iteritems():
        if count < 1:
            return False
    
    return True
        

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
