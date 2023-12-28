import binascii
import base64 

def bytes_xor(hex_1, hex_2):
    
    # convert hex to bytes
    bytes_1 = bytes.fromhex(hex_1)
    bytes_2 = bytes.fromhex(hex_2)

    # check length
    if len(bytes_1) != len(bytes_2):
        raise ValueError("bytestrings need to be the same length!")
    
    # XOR
    return bytes(b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2))
    

if __name__ == "__main__":
    
    # inputs and expected output
    in1 = "1c0111001f010100061a024b53535009181c"
    in2 = "686974207468652062756c6c277320657965"
    expected = "746865206b696420646f6e277420706c6179"

    print("\nInput 1: {}".format(in1))
    print("Input 2: {}".format(in2))

    xor_result = bytes_xor(in1, in2).hex()
    print("\nXOR result: {}".format(xor_result))
    print("Expected  : {}\n".format(expected))

    # check answer
    if xor_result == expected:
        print("It worked!\n")
    else:
        exit("Something went wrong...")