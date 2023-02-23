# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#372
s = "CCCLXXII"

def romanToInt(s: str) -> int:
    r2i = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    answer = 0
    for i, letter in enumerate(s[:-1]):
        if r2i[letter] >= r2i[s[i+1]]:
            answer += r2i[letter]
            print(f"+{r2i[letter]}")
        else:
            answer -= r2i[letter]
            print(f"-{r2i[letter]}")
    answer += r2i[s[-1]]
    print(f"+{r2i[s[-1]]}")
    print(answer)

romanToInt("CCCLXXII")


        
        