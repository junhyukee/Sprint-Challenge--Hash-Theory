def stretch(a, b, c):
    s = a ^ (b ^ c)
    carry = a and b or (b and c or a and c)
    print(a, b, c, carry, s)

stretch(0,0,0)
stretch(0,0,1)
stretch(0,1,0)
stretch(0,1,1)
stretch(1,0,0)
stretch(1,0,1)
stretch(1,1,0)
stretch(1,1,1)