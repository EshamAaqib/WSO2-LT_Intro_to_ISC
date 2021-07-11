# WSO2_Intro_to_ISC_Assignment

## Using OpenSSL to encrypt the PDF document available at https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-100.pdf with AES-256 (with sha256 message digest), using the password "wso2training"

```
openssl enc -aes-256-cbc -pass pass:wso2training -p -in nistspecialpublication800-100.pdf -out nistspecialpublication800-100.enc
```

### Screenshot

![Screenshot from 2021-07-10 23-52-49](https://user-images.githubusercontent.com/75664650/125185509-d1c50100-e242-11eb-8b7c-70a608bde72c.png)
