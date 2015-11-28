TABLE = ["one", "two", "three", "four", "five", "six", "seven",
         "eight", "nine", "ten", "eleven", "twelve", "thirteen",
         "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
         "nineteen", "twenty", "thirty", "forty", "fifty", "sixty",
         "seventy", "eighty", "ninety"]

def checkio(number):

    output = []
    first_two = number % 100
    if first_two <= 20 and first_two > 0:
        output.insert(0, TABLE[first_two - 1])
    else:
        units = number % 10
        if units > 0:
            output.insert(0, TABLE[units - 1])
        tens = (number / 10) % 10
        if tens > 0:
            output.insert(0, TABLE[19 + (tens - 2)])
    if number >= 100:
        hundreds = number / 100
        output.insert(0, TABLE[hundreds - 1] + " hundred")

    return " ".join(output)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    assert checkio(100) == 'one hundred', "last example"
