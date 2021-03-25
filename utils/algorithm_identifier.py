from Crypto.Cipher import AES, DES3, Blowfish


class AlgorithmsIdentifier:
    algorithms = {
        "AES_128_CBC": {
            "oid": "2.16.840.1.101.3.4.1.2",
            "alg": AES.new,
            "mode": AES.MODE_CBC,
            "key_size": 16,
            "block_size": AES.block_size
        },
        "AES_192_CBC": {
            "oid": "2.16.840.1.101.3.4.1.22",
            "alg": AES.new,
            "mode": AES.MODE_CBC,
            "key_size": 24,
            "block_size": AES.block_size
        },
        "AES_256_CBC": {
            "oid": "2.16.840.1.101.3.4.1.42",
            "alg": AES.new,
            "mode": AES.MODE_CBC,
            "key_size": 32,
            "block_size": AES.block_size
        },
        "Blowfish_CBC": {
            "oid": "1.3.6.1.4.1.3029.1.1.2",
            "alg": Blowfish.new,
            "mode": Blowfish.MODE_CBC,
            "key_size": 16,
            "block_size": Blowfish.block_size
        },
        "TripleDes_CBC": {
            "oid": "1.3.6.1.4.1.4929.1.8",
            "alg": DES3.new,
            "mode": DES3.MODE_CBC,
            "key_size": 24,
            "block_size": DES3.block_size
        }
    }

    @staticmethod
    def getOID(algorithm):
        return AlgorithmsIdentifier.algorithms.get(algorithm).get("oid")

    @staticmethod
    def getBlockSize(oid):
        for algorithm in AlgorithmsIdentifier.algorithms.values():
            if algorithm.get("oid") == oid:
                return algorithm.get("block_size")
        return None

    @staticmethod
    def getAlg(oid, key, iv):
        for algorithm in AlgorithmsIdentifier.algorithms.values():
            if algorithm.get("oid") == oid:
                return algorithm.get("alg")(key, algorithm.get("mode"), iv)
        return None
