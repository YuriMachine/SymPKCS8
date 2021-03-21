from Crypto.IO import PKCS8, PEM

def wrap(input, output):
    key = input.read()
    pkcs8_key = PKCS8.wrap(key, ...)
    pem_key = PEM.encode(pkcs8_key, "PRIVATE KEY")
    output.writelines(pem_key)
