operation='4 5 + 3 *'
nums=[]
infixa=[]

for x in operation.split():
    if (x.isdigit()):
        infixa.append(x)
    else:
        digit2=infixa.pop()
        digit1=infixa.pop()

        newInfixa=f'({digit1} {x} {digit2})'
        infixa.append(newInfixa)

print(infixa[0])

for i in operation.split():
    if (i.isdigit()):
        nums.append(int(i))
    else:
        digit2=nums.pop()
        digit1=nums.pop()

        if (i=='*'):
            nums.append(digit1*digit2)
        elif (i=='/'):
            nums.append(digit1/digit2)
        elif (i=='+'):
            nums.append(digit1+digit2)
        elif (i=='-'):
            nums.append(digit1-digit2)
print(nums[0])

