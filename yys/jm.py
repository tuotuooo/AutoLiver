from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import configparser

def jm(z,m):
    with open("1.pem", "rb") as key_file:
        pem_public_key = key_file.read()
    public_key = serialization.load_pem_public_key(pem_public_key)

    message_bytes = z.encode('utf-8')
    message_bytes1 = m.encode('utf-8')

    ciphertext = public_key.encrypt(
        message_bytes,
        padding.PKCS1v15()
    )
    ciphertext1 = public_key.encrypt(
        message_bytes1,
        padding.PKCS1v15()
    )

    base64_encoded = base64.b64encode(ciphertext)
    base64_encoded1 = base64.b64encode(ciphertext1)

    return base64_encoded.decode(),base64_encoded1.decode()

def main():
    canshu = {}
    config = configparser.ConfigParser()
    config.read('cnm.cfg')
    z = config['mw']['account']
    m = config['mw']['password']
    canshu['account'] = jm(z,m)[0]
    canshu['password'] = jm(z,m)[1]
    for key, value in canshu.items():
        config.set('credentials', key, value)
    with open('cnm.cfg', 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    main()