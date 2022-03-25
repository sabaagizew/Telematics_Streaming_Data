import base64

# Encode string to bytes
incoming_Log_encoded = incoming_Log_encoded()
Print(f"string in bytes: \n {incoming_Log_encoded} \n")

# Encode bytes to base64
incoming_Log_b64 = base64.b64encode(incoming_Log_encoded)
print(f"string in b64: \n {incoming_Log_b64} \n")

# Decode base64
incoming_Log_b64_dencoded = base64.b64dencode(incoming_Log_b64)
print(f"string decoded from b64: \n {incoming_Log_b64_dencoded} \n")

# Decode bytes to string
print(f"Bytes converted to string: \n {incoming_Log_b64_dencoded.decoded()}
\n")