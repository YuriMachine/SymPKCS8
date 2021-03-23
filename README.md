# SymPKCS8

```
Usage: SymPKCS8.py [OPTIONS] [wrap|decode]

  WRAP: Wrap symmetric key in a PKCS8 container.

  DECODE: Decodes a symmetric ciphertext wrapped in a PKCS8 container.

Options:
  --keyfile FILENAME     The symmetric key to wrap or decode (PKCS8 required
                         for decode).  [required]

  --ciphertext FILENAME  The ciphertext to decode.  [required for decode]
  --out TEXT             The PKCS8 wrapped key or the decoded plaintext.
                         [required]

  --help                 Show this message and exit.
  ```
