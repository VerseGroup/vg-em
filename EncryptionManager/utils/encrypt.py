# crypto imports
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt_private(message, private_key):
    message = message.encode('utf-8') # encrypting requires binary
    encrypted_message = private_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        )
    return encrypted_message

def encrypt_public(message, public_key):
    message = message.encode('utf-8') # encrypting requires binary
    encrypted_message = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
        )
    return encrypted_message