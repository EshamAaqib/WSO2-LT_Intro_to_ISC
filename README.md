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

