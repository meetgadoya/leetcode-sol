l=len(digits)-1
r=1
while(l>=0):
    c=digits[l]
    c+=r
    if c<=9:
        r=0
        digits[l]=c
        return digits
    else:
        r=1
        digits[l]=0
        l-=1
if r==1:
    digits.insert(0,1)
return digits