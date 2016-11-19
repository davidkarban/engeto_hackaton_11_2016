
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
    print("")
    return(result)

#def get_binary(binariy)


print(decimal_to_binary(130))

