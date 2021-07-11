import hashlib
import sys

value=sys.argv[1].encode('utf-8')


salt=b'Km5d5ivMy8iexuHcZrsD'

key = hashlib.pbkdf2_hmac('sha512',value,salt,200000)

print(key.hex())
