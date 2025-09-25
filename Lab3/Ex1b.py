from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)
token = cipher_suite.encrypt(b"This is. really secret message! Not for sharing.")
print (token)

decrpyted = cipher_suite.decrypt(token)
print("Decrypted token=", decrpyted)
print(decrpyted.decode()) 