import hashlib


class Encrypt:
    def get_md5(self, text: str) -> str:
        try:
            hash_id = hashlib.md5(text.encode())
            return str(hash_id.hexdigest())
        except Exception as e:
            raise e
