d={}
for i in nums:
    if i in d:
        return True
    else:
        d.update({i:1})
return False