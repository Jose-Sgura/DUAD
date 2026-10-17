import datetime

import jwt

class JWTManager:
    def __init__(self, private_key, public_key, algorithm="RS256"):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm
    
    def encode(self, data, expires_delta = None):
        try:
            payload = dict(data)
            if expires_delta is not None:
                now = datetime.datetime.now(datetime.timezone.utc)
                payload["iat"] = now
                payload["exp"] = now + expires_delta
            encoded = jwt.encode(payload, self.private_key, algorithm=self.algorithm)
            return encoded
        except Exception:
            return None
    def decode(self, token):
        decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
        return decoded