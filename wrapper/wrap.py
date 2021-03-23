from utils.algorithm_identifier import AlgorithmsIdentifier
from Crypto.IO import PKCS8, PEM


def openssl_key_input(key_input):
    key, iv = key_input.readlines()

    key_index = key.find('=') + 1
    iv_index = iv.find('=') + 1

    key = key[key_index:].strip()
    iv = iv[iv_index:].strip()
    return bytearray.fromhex(iv + key)


def wrap(key_input):
    key = openssl_key_input(key_input)
    pkcs8_key = PKCS8.wrap(key, AlgorithmsIdentifier.getOID("AES_128_CBC"))
    return PEM.encode(pkcs8_key, "PRIVATE KEY")
