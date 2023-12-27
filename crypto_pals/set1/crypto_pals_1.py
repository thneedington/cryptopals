import base64


def hex_to_b64(hex_str):
    """
    input: a string in hex
    output: that same string as base64 bytes
    """
    
    # convert from hex to bytes
    bytes_str = bytes.fromhex(hex_str)

    # convert to b64 and return
    b64_str = base64.b64encode(bytes_str)
    return b64_str



if __name__ == "__main__":
    hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b64_str = hex_to_b64(hex_str)

    print("\nHex str: {}".format(hex_str))
    print("\nB64 str: {}\n".format(b64_str))

    # check if it worked
    expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    if (b64_str == expected):
        print("It worked!\n")
    else:
        print("Something went wrong...\n")