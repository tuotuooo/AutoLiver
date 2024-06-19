import configparser
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

config = configparser.ConfigParser()
config.read('kjq.cfg', encoding='utf-8')
n = config['key']['n']
e = config['key']['e']

modulus = int(n, 16)
public_exponent = int(e)

public_key = rsa.RSAPublicNumbers(public_exponent, modulus).public_key()

pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pem_public_key.decode())
