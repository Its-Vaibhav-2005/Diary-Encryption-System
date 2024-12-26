# **Diary Encryption System**
This project offers an encryption and decryption system for protecting diary entries using AES encryption. It uses the SHA-256 hashing algorithm for key generation and employs padding to ensure data integrity. The system provides a straightforward yet secure method for encrypting and decrypting text-based data, such as personal diary entries.

## Libraries Used
- `pycryptodome`:
  - `AES` for encryption/decryption.
  - `SHA256` for generating the key.
  - `pad` and `unpad` for padding the data to AES block size.
- `icecream`: For debugging purposes.

## Code Explanation

### 1. **Input Key**:
   The user provides an input key. This key is hashed using `SHA256` to generate a 256-bit encryption key.

```python
inputKey = input("Entry Key: ").encode('utf-8')
key = SHA256.new(inputKey).digest()
```

### 2. **DiaryKey Class**:
   The `DiaryKey` class contains methods to encrypt and decrypt data using AES `Advanced Encryption Standard`

#### Constructor
   - The constructor accepts a key and hashes it using `SHA256` to generate a 256-bit key.

```python
class DiaryKey:
    def __init__(self, key):
        self.key = SHA256.new(key).digest()
```

#### `encode` Method
   - This method encrypts the data using AES with ECB mode.
   - The input data is padded to the block size before encryption.

```python
    def encode(self, data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        padData = pad(data.encode('utf-8'), AES.block_size)
        return cipher.encrypt(padData)
```

#### `decode` Method
   - This method decrypts the data using AES in ECB mode.
   - It removes the padding after decryption.

```python
    def decode(self, data):
        cipher = AES.new(self.key, AES.MODE_ECB)
        decrypt = cipher.decrypt(data)
        return unpad(decrypt, AES.block_size).decode('utf-8')
```

### 3. **Using the `DiaryKey` Class**
   After defining the class, you can create an instance of `DiaryKey` with the user-provided key and use the `encode` and `decode` methods to encrypt and decrypt data.

```python
# Example usage
diary = DiaryKey(key)
encrypted_data = diary.encode("This is a secret message")
decrypted_data = diary.decode(encrypted_data)

print("Encrypted:", encrypted_data)
print("Decrypted:", decrypted_data)
```

### 4. **Libraries Installation**
   You need the following libraries to run this script:

```bash
pip install pycryptodome icecream
```

### 5. **Security Notes**
   - **AES.MODE_CBC** is a more secure mode than ECB as it uses an initialization vector (IV), which ensures that identical plaintext blocks will be encrypted differently. However, it's important to ensure that the IV is random and unique for each encryption operation. Reusing an IV with the same key can compromise security. The IV should be stored alongside the ciphertext to allow proper decryption.

   - The key used for encryption should be stored securely. If someone gains access to the key, they can decrypt the data. For added protection, consider using secure key management practices.

---

This script provides basic encryption and decryption for any data using AES in CBC mode. While CBC mode is more secure than ECB, it still requires careful handling of the initialization vector (IV) and key. For production environments or sensitive data, it's crucial to implement additional security measures, such as secure key management, unique IV generation for each encryption, and consideration of other secure configurations or cipher modes (e.g., authenticated encryption modes like GCM).
