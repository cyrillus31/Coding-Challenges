def intToRoman(number: int) -> str:
    i2r = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"
    }
    result = [] 
    
    for i, digit in enumerate(str(number)[::-1]):
        current = int(digit)*(10**i)
        # print(current)
        if i2r.get(current, None):
            result.insert(0, i2r.get(current))
        else:
            if 1 < current < 4:
                result.insert(0, "I"*current)
            elif 5 < current < 9:
                result.insert(0, "V"+"I"*(current-5))
            elif 10 < current < 40:
                result.insert(0, "X"*(current//10))
            elif 50 < current < 90:
                result.insert(0, "L"+"X"*((current-50)//10))
            elif 100 < current < 400:
                result.insert(0, "C"*(current//100))
            elif 500 < current < 900:
                result.insert(0, "D"+"C"*((current-500)//100))
            elif 1000 < current < 3999:
                result.insert(0, "M"*(current//1000))
        # print(result)
    return("".join(result))


# 2345
# MMCCCXLV
a = intToRoman(2345)
print(a)
