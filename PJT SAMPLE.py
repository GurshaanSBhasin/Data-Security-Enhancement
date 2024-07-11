import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib

# Sample financial dataset
financial_dataset = [
    {
        "transaction_id": 1,
        "name": "Gurshaan",
        "receiver_name": "Shoukat",
        "receiver_id": 123456,
        "phone_no": "123-456-7890"
    },
    {
        "transaction_id": 2,
        "name": "Ryan",
        "receiver_name": "Kavin",
        "receiver_id": 987654,
        "phone_no": "987-654-3210"
    },
    {
        "transaction_id": 3,
        "name": "Ajay",
        "receiver_name": "Kavin",
        "receiver_id": 555555,
        "phone_no": "555-555-5555"
    }

]

# Generate RSA key pair
key_rsa = RSA.generate(1024)  # Key length 

# Export public and private keys
public_key_rsa = key_rsa.publickey().export_key()
private_key_rsa = key_rsa.export_key()

# Write RSA keys to files (optional)
with open('public_rsa.pem', 'wb') as f:
    f.write(public_key_rsa)
   
with open('private_rsa.pem', 'wb') as f:
    f.write(private_key_rsa)

# Encrypt the receiver_id field of each transaction data
for transaction in financial_dataset:
    receiver_id = str(transaction["receiver_id"]).encode()
    phone_no = str(transaction["phone_no"]).encode()
    # Encryption using RSA public key
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key_rsa))
    encrypted_receiver_id = cipher_rsa.encrypt(receiver_id)
    encrypted_phone_no= cipher_rsa.encrypt(phone_no)
    # Replace the original receiver_id with the encrypted one
    transaction["receiver_id"] = encrypted_receiver_id
    transaction["phone_no"]= encrypted_phone_no
    # Decryption using RSA private key
    cipher_rsa = PKCS1_OAEP.new(key_rsa)
    decrypted_receiver_id = cipher_rsa.decrypt(encrypted_receiver_id)
    decrypted_phone_no= cipher_rsa.decrypt(encrypted_phone_no)
    # Print decrypted receiver_id
    print("Original receiver_id:", receiver_id)
    print("Encrypted receiver_id:", encrypted_receiver_id)
    print("Decrypted receiver_id:", decrypted_receiver_id)
    print("Original phone_no:", phone_no)
    print("Encrypted receiver_id:", encrypted_phone_no)
    print("Decrypted receiver_id:", decrypted_phone_no)
    
# Print the modified financial dataset
print("Modified financial dataset:", financial_dataset)
