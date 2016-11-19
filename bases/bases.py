
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

# convert binary to decimal
def binary_to_decimal(binary):
    result = 0
    for x in binary:
        result = (result << 1) + int(x)
    return(result)

# universal 
def convert_to_decimal(number, srcbase):
    result = 0
    for x in number:
        result = (result * srcbase) + int(x, srcbase)
    return(result)


