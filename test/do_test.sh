#!/usr/bin/env bash

#AES128

echo "AES_128_test" | openssl enc -aes128 -pbkdf2 -k "test_password" -p -in - -out 'AES_128_ciphertext.enc' > 'AES_128_key.txt'

python3 ../SymPKCS8.py wrap --keyfile "AES_128_key.txt" --out "AES_128_pkcs8.pem"

python3 ../SymPKCS8.py decode --keyfile "AES_128_pkcs8.pem" --ciphertext "AES_128_ciphertext.enc" --out "AES_128_plaintext.txt"

#AES192
echo "AES_192_test" | openssl enc -aes192 -pbkdf2 -k "test_password" -p -in - -out 'AES_192_ciphertext.enc' > 'AES_192_key.txt'

python3 ../SymPKCS8.py wrap --keyfile "AES_192_key.txt" --out "AES_192_pkcs8.pem"

python3 ../SymPKCS8.py decode --keyfile "AES_192_pkcs8.pem" --ciphertext "AES_192_ciphertext.enc" --out "AES_192_plaintext.txt"

#AES256
echo "AES_256_test" | openssl enc -aes256 -pbkdf2 -k "test_password" -p -in - -out 'AES_256_ciphertext.enc' > 'AES_256_key.txt'

python3 ../SymPKCS8.py wrap --keyfile "AES_256_key.txt" --out "AES_256_pkcs8.pem"

python3 ../SymPKCS8.py decode --keyfile "AES_256_pkcs8.pem" --ciphertext "AES_256_ciphertext.enc" --out "AES_256_plaintext.txt"

#Blowfish
echo "Blowfish_test" | openssl enc -blowfish -pbkdf2 -k "test_password" -p -in - -out 'Blowfish_ciphertext.enc' > 'Blowfish_key.txt'

python3 ../SymPKCS8.py wrap --keyfile "Blowfish_key.txt" --out "Blowfish_pkcs8.pem"

python3 ../SymPKCS8.py decode --keyfile "Blowfish_pkcs8.pem" --ciphertext "Blowfish_ciphertext.enc" --out "Blowfish_plaintext.txt"

#3DES
echo "3DES_test" | openssl enc -des3 -pbkdf2 -k "test_password" -p -in - -out '3DES_ciphertext.enc' > '3DES_key.txt'

python3 ../SymPKCS8.py wrap --keyfile "3DES_key.txt" --out "3DES_pkcs8.pem"

python3 ../SymPKCS8.py decode --keyfile "3DES_pkcs8.pem" --ciphertext "3DES_ciphertext.enc" --out "3DES_plaintext.txt"
