if (n <= 0):
    return False
a = math.log(n, 3)
if (a % 1.0 == 0.0 or a % 1.0 >= 0.99999999999999):
    return True
return False