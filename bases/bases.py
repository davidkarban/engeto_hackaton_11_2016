
# convert decimal to binary
def decimal_to_binary(decimal):
    result = ""
    while(decimal != 0): 
        rest = decimal % 2
        decimal = decimal >> 1
        if(rest == 0):
            result = "0" + result
        else: 
            result = "1" + result
    return(result)

def binary_to_decimal(binary):
    strlen = len(binary)
    result = 0
    for x in range(strlen):
        result = (result << 1) + int(binary[x])
    return(result)

print(decimal_to_binary(130))

print(binary_to_decimal("10000010"))

