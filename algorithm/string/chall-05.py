S = "526576657273696e672e4944"

decoded_string = str(bytes.fromhex(S).decode('utf-8'))


print(bytearray.fromhex(S))
