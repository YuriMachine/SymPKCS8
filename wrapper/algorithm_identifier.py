class AlgorithmsIdentifier:
    pass


class AES(AlgorithmsIdentifier):
    AES_128_CBC = "2.16.840.1.101.3.4.1.2"
    AES_192_CBC = "2.16.840.1.101.3.4.1.22"
    AES_256_CBC = "2.16.840.1.101.3.4.1.42"


class ARIA(AlgorithmsIdentifier):
    ARIA_128_CBC = "1.2.410.200046.1.1.2"
    ARIA_192_CBC = "1.2.410.200046.1.1.7"
    ARIA_256_CBC = "1.2.410.200046.1.1.12"


class Blowfish(AlgorithmsIdentifier):
    BLOWFISH_CBC = "1.3.6.1.4.1.3029.1.1.2"


class TripleDes(AlgorithmsIdentifier):
    TRIPLE_DES_CBC = "1.3.6.1.4.1.4929.1.8"
