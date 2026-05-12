import jwt

class JWTManager:

    def generate_token(self, user_id):
        return jwt.encode(
            {"user_id": user_id},
            "secret",
            algorithm="HS256"
        )

    def validate_token(self, token):
        return jwt.decode(
            token,
            "secret",
            algorithms=["HS256"]
        )