from utils.algorithm_identifier import AlgorithmsIdentifier
from Crypto.IO import PKCS8, PEM


def openssl_key_parse(key_input):
    if len(key_input) == 3:
        salt, key, iv = key_input
    else:
        key, iv = key_input

    key_index = key.find('=') + 1
    iv_index = iv.find('=') + 1

    key = key[key_index:].strip()
    iv = iv[iv_index:].strip()
    return key, iv


def guess_algorithm(key, iv):
    key_len = len(key) // 2
    iv_len = len(iv) // 2

    for key, val in AlgorithmsIdentifier.algorithms.items():
        if val.get("block_size") == iv_len:
            if val.get("key_size") == key_len:
                print("Identified algorithm: " + key)
                return val.get("oid")

    return None


def wrap(key_input):
    key, iv = openssl_key_parse(key_input)

    algorithm = guess_algorithm(key, iv)
    byte_key = bytearray.fromhex(iv + key)

    pkcs8_key = PKCS8.wrap(byte_key, algorithm)
    return PEM.encode(pkcs8_key, "PRIVATE KEY")
