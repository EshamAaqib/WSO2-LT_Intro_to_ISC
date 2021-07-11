import hashlib
import secrets 
import sys

value=sys.argv[1].encode('utf-8')


salt=secrets.token_bytes()

key = hashlib.pbkdf2_hmac('sha512',value,salt,200000)

print(key.hex())
