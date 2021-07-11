import hashlib
import secrets 
import sys

value=sys.argv[1].encode('utf-8')
salt=secrets.token_bytes()

key=hashlib.sha512(salt+value).hexdigest()

print(key)
