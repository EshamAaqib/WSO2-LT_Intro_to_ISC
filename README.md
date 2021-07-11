# WSO2_Intro_to_ISC_Assignment

## 1. Using OpenSSL to encrypt the PDF document available at https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-100.pdf with AES-256 (with sha256 message digest), using the password "wso2training"

```
openssl enc -aes-256-cbc -pass pass:wso2training -p -in nistspecialpublication800-100.pdf -out nistspecialpublication800-100.enc
```

### Screenshot

![Screenshot from 2021-07-10 23-52-49](https://user-images.githubusercontent.com/75664650/125185509-d1c50100-e242-11eb-8b7c-70a608bde72c.png)

###### Encrypted file uploaded to the Question 1 folder (Link at the bottom of the document)

## 2. Using OpenSSL to encrypt the PDF document available at https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-100.pdf with AES-256 (with sha256 message digest) using the password "wso2training" while setting following parameters.

```
IV = 4702A2949A628E975C12A0CD459E2646
Key = 458354644CC9C1AFB8E6F3C6DC90B2734C5B19E5BBB839A870B81125C3208320
```

### Executed Command 

```
openssl enc -aes-256-cbc -pass pass:wso2training -p -in nistspecialpublication800-100.pdf -K '458354644CC9C1AFB8E6F3C6DC90B2734C5B19E5BBB839A870B81125C3208320' -iv '4702A2949A628E975C12A0CD459E2646' -out nistspecialpublication800-100.enc
```

### Screenshot

![Screenshot from 2021-07-11 00-08-33](https://user-images.githubusercontent.com/75664650/125185906-fde18180-e244-11eb-8425-204af572fc6b.png)

###### Encrypted file uploaded to Question 2 Folder (Link at the bottom of the document)

## 3. Creating a RSA key pair using a 4096-bit key

### Creating the private key 

```
openssl genrsa -out privatekey.pem 4096
```

### Extracting the public key from the key pair

```
openssl rsa -in privatekey.pem -outform PEM -pubout -out publickey.pem
```

### Screenshot

![Screenshot from 2021-07-11 00-17-54](https://user-images.githubusercontent.com/75664650/125186164-5402f480-e246-11eb-992d-8caff358bf87.png)

###### Public key file uploaded to the Question 3 folder (Link at the bottom of the document)

## 4. Using the RSA public key stored at https://drive.google.com/file/d/18E4pYx8o04o0PlhC9Dmboaz68ApU3V3N/view?usp=sharing to encrypt the PDF https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-100.pdf

### As the PDF file is a larger file I went ahead and created a random key by executing the following

```
openssl rand -base64 32 > key.bin
```

### Then I went ahead and encrypted the random key using the public key mentioned above. I executed the following

```
openssl rsautl -encrypt -inkey public.pem -pubin -in key.bin -out key.bin.enc
```

### Now I encrypted the large PDF file using the random key by executing the following 

```
penssl enc -aes-256-cbc -salt -in nistspecialpublication800-100.pdf -out nistspecialpublication800-100.pdf.enc -pass file:./key.bin
```

###### At this point the user will have to decrypt the random key file (key.bin) using the private key and use the decrypted key file to decrypt the encrypted PDF file

### Screenshot 

![Screenshot from 2021-07-11 00-47-43](https://user-images.githubusercontent.com/75664650/125187009-0b9a0580-e24b-11eb-8f90-ba063dbeeb03.png)

###### Encrypted key file and the encrypted pdf file has been uploaded to the Question 4 folder (Link at the bottom of this document)

## 5. Calculating the SHA512 hash of the file https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-100.pdf

```
openssl dgst -sha512 nistspecialpublication800-100.pdf
```

### Screenshot

![Screenshot from 2021-07-11 01-03-07](https://user-images.githubusercontent.com/75664650/125187334-c70f6980-e24c-11eb-99c8-ee8b0d98eb67.png)

## 6. Writing a simple Python program to accept a value as a command line argument and return only the PBKDF2 hash of the value

### Python Script

```
import hashlib
import sys

value=sys.argv[1].encode('utf-8')
salt=b'Km5d5ivMy8iexuHcZrsD'
key = hashlib.pbkdf2_hmac('sha512',value,salt,200000)
print(key.hex())
```

###### Code has been uploaded to the Question 6 folder as well. (Link at the bottom of the document)

### Screenshot

![Screenshot from 2021-07-11 02-19-44](https://user-images.githubusercontent.com/75664650/125189859-dd6ef280-e257-11eb-8d1b-a8d6cdd32c6b.png)


## 7. Modifying the script in Q6 to use a secure random as the salt value of PBKDF2 hash generation

### Python Script

```
import hashlib
import secrets 
import sys

value=sys.argv[1].encode('utf-8')
salt=secrets.token_bytes()
key = hashlib.pbkdf2_hmac('sha512',value,salt,200000)
print(key.hex())
```

###### Code has been uploaded to the Question 7 folder as well. (Link at the bottom of the document)

## 8. Modifiying the script in Q7 to use a secure random as the salt value and generate a SHA512 hash

### Python Script

```
import hashlib
import secrets 
import sys

value=sys.argv[1].encode('utf-8')
salt=secrets.token_bytes()
key=hashlib.sha512(salt+value).hexdigest()
print(key)
```
###### Code has been uploaded to the Question 8 folder as well. (Link at the bottom of the document)


## 9. Using https://hashcat.net/hashcat/ and the wordlist available at https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/phpbb.txt to crack the MD5 value "3c2223212b6dde34bcf86b580bdb71d4" and recover the password

### Cracked Password  -  woohooyeah

### Screenshots 

![Screenshot from 2021-07-11 04-53-26](https://user-images.githubusercontent.com/75664650/125194025-11084780-e26d-11eb-8d65-04fbe2450648.png)

![Screenshot from 2021-07-11 04-53-29](https://user-images.githubusercontent.com/75664650/125194029-15ccfb80-e26d-11eb-8505-ee6f104619a7.png)


## 10.  Using the GPG key located at https://keys.openpgp.org/search?q=ayomawdb%40gmail.com to encrypt the PDF document at https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-100.pdf

### First I downloaded the gpg key and executed the following to import the key 

```
gpg --import 34FB0BA2155A9D20D248BD0E7D11327265445CF2.asc
```

### Then I executed the following to encrypt the file

```
gpg --recipient ayomawdb@gmail.com --encrypt nistspecialpublication800-100.pdf
```

###### Encrypted file uploaded to Question 10 folder. (Link at the bottom of the document)

### Screenshots

![Screenshot from 2021-07-11 05-01-07](https://user-images.githubusercontent.com/75664650/125194299-419cb100-e26e-11eb-9dbc-3cd97ba72f9d.png)

## 11. Creating a GPG key for yourself and upload the public key to any public keyserver

### GPG Key - https://keys.openpgp.org/vks/v1/by-fingerprint/80FC07695162673596C2C75296C3E1C8CE31F236


## 12. Calculate the CVSS 3.1 score for a security issue that can be exploited over the network, with the help of a person-in-the-middle attack, via an admin user of an application, without any additional user interactions and without having an impact on any other systems

### CVSS 3.1 vector string - CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:U/C:L/I:H/A:N

## 13. Using https://testssl.sh/ to assess the TLS security levels of google.com domain

### Screenshot

![Screenshot from 2021-07-11 05-48-41](https://user-images.githubusercontent.com/75664650/125195736-9b07de80-e274-11eb-9133-5caff3e707fb.png)



