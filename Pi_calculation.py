rank = 1000000000
value = 0

for k in range(1, 2*rank+1, 2):
    sign = -(k % 4 - 2)
    value += float(sign) / k

print(value*4)
