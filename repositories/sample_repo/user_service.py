from auth import JWTManager
from database import get_db

class UserService:

    def login_user(self, username, password):
        db = get_db()

        jwt_manager = JWTManager()

        token = jwt_manager.generate_token(1)

        return {
            "access_token": token
        }