def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    roman = ""
    while (num > 0):
        while num >= 1000:
            num = num - 1000
            roman = roman + "M"
        if num >= 900:
            num -= 900
            roman = roman + "CM"
        if num >= 500:
            num -= 500
            roman = roman + "D"
        if num >= 400:
            num -= 400
            roman = roman + "CD"

        while (num >= 100):
            num = num - 100
            roman = roman + "C"
        if num >= 90:
            num -= 90
            roman = roman + "XC"
        if num >= 50:
            num -= 50
            roman = roman + "L"
        if num >= 40:
            num -= 40
            roman = roman + "XL"

        while (num >= 10):
            num = num - 10
            roman = roman + "X"
        if num >= 9:
            num -= 9
            roman = roman + "IX"
        if num >= 5:
            num -= 5
            roman = roman + "V"
        if num >= 4:
            num -= 4
            roman = roman + "IV"
        while (num >= 1):
            num = num - 1
            roman = roman + "I"

    return roman