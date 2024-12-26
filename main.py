from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from icecream import ic

class DiaryKey:
    def __init__(self, key):
        self.key = SHA256.new(key.encode('utf-8')).digest()
    
    def encode(self, data):
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padData = pad(data.encode('utf-8'), AES.block_size)
        return iv + cipher.encrypt(padData)

    def decode(self, data):
        iv = data[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypt = cipher.decrypt(data[AES.block_size:])
        return unpad(decrypt, AES.block_size).decode('utf-8')
    