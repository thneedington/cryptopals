import base64

# conver from hex to bytes
hex_str = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
bytes_str = bytes.fromhex(hex_str)

# conver to b64
b64_str = base64.b64encode(bytes_str)
print(b64_str)

expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
assert (expected == b64_str)