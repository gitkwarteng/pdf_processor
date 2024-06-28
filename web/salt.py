import base64
from hashlib import sha256


class Salt:
    def __init__(self, salt_key: str, salt_index: int):
        self.salt_key = salt_key
        self.salt_index = salt_index

    def _get_salt_hash(self):
        return sha256(self.salt_key.encode()).digest()

    def encode(self, payload: str) -> str:
        # Generate a hash of the salt key
        salt_hash = self._get_salt_hash()
        # Ensure the salt index is within bounds
        salt_index = self.salt_index % len(salt_hash)
        # Combine the payload with the salt value at the specified index
        salted_payload = salt_hash[salt_index:].hex() + payload
        # Encode the salted payload to base64
        encoded = base64.urlsafe_b64encode(salted_payload.encode()).decode()
        return encoded

    def decode(self, encoded_payload: str) -> str:
        try:
            # Generate a hash of the salt key
            salt_hash = self._get_salt_hash()
            # Ensure the salt index is within bounds
            salt_index = self.salt_index % len(salt_hash)
            # Decode the base64 payload
            decoded = base64.urlsafe_b64decode(encoded_payload).decode()
            # Retrieve the salt value at the specified index
            expected_salt = salt_hash[salt_index:].hex()
            # Verify and remove the salt value from the decoded payload
            if decoded.startswith(expected_salt):
                return decoded[len(expected_salt):]
            else:
                raise ValueError("Invalid salt key or salt index")
        except Exception as e:
            return f"Decoding failed: {str(e)}"


# # Example usage
# payload = "Hello, World!"
# salt_key = "my_secret_salt"
# salt_index = 5
#
# salt = Salt(salt_key, salt_index)
#
# # Encoding
# encoded = salt.encode(payload)
# print("Encoded:", encoded)
#
# # Decoding
# decoded = salt.decode(encoded)
# print("Decoded:", decoded)
#
# # Trying with incorrect salt key or index
# salt.salt_key = "wrong_salt"
# incorrect_decoded = salt.decode(encoded)
# print("Incorrect Decode:", incorrect_decoded)
