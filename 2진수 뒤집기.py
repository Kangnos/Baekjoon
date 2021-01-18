Num = input()
BinaryNum = format(int(Num), 'b')
reversed_BinaryNum = ''.join(reversed(str(BinaryNum))) 
DecimalNum = int(bin(int(reversed_BinaryNum)),2)

calculated_list = []
LastList = 0
n = 1

for i in range(0, len(reversed_BinaryNum)):
    # reversed_DeciamlNum += (reversed_BinaryNum)[i-1] * 2 ^ i-1
    reversed_DeciamlNum = list(map(int, reversed_BinaryNum[i]))
    calculated_list += reversed_DeciamlNum
    LastList += calculated_list[i] * (2 ** (len(reversed_BinaryNum)-n))
    n += 1

print(LastList)