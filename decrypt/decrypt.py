from Crypto.IO import PKCS8, PEM
from Crypto.Util.Padding import unpad
from utils.algorithm_identifier import AlgorithmsIdentifier


def decrypt(keyfile, ciphertext):
    DER_key, _, _ = PEM.decode(keyfile)
    oid, key_iv, _ = PKCS8.unwrap(DER_key)
    block_size = AlgorithmsIdentifier.getBlockSize(oid)

    iv = key_iv[:block_size]
    key = key_iv[block_size:]
    cipher = AlgorithmsIdentifier.getAlg(oid, key, iv)

    if ciphertext[:8] == b"Salted__":
        ciphertext = ciphertext[16:]

    return unpad(cipher.decrypt(ciphertext), block_size)
