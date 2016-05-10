import base64

def base64_decode(encoded_string):
    return base64.b64decode(encoded_string)

def base64_encode(data):
    return base64.encode(data)
