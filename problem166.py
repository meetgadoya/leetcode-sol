def fractionToDecimal(numerator: int, denominator: int) -> str:
    # a = abs(numerator)
    # b = abs(denominator)

    # logic if denominator is 0 i.e perfectly divisible
    if (numerator * denominator) > 0:
        isNeg = False
    else:
        isNeg = True

    res = ''

    numerator = abs(numerator)
    denominator = abs(denominator)
    quotient = numerator // denominator
    remainder = numerator % denominator

    dic = {}

    while 1:
        if len(res) == 0:
            if remainder == 0:
                res = res + str(quotient)
                if isNeg == True:
                    return '-' + res
                return res
            else:
                res = str(quotient) + '.'
        else:
            remainder = remainder * 10
            numerator = remainder
            quotient = numerator // denominator
            remainder =  numerator % denominator
            if remainder == 0:
                res = res + str(quotient)
                if isNeg == True:
                    return '-' + res
                return res
            else:
                if str(quotient)+' '+str(remainder) in dic:
                    res = res[:dic[str(quotient)+' '+str(remainder)]] + '(' + res[dic[str(quotient)+' '+str(remainder)]:] + ')'
                    if isNeg == True:
                        return '-' + res
                    return res
                else:
                    dic[str(quotient)+' '+str(remainder)] = len(res)
                    res = res + str(quotient)


print(fractionToDecimal(1,2))