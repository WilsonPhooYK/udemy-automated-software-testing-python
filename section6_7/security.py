from hmac import compare_digest
from models.user import UserModel

def authenticate(username: str, password: str):
    """
    Function that gets called when a user calls the /auth endpoint
    with their username and password

    Args:
        username (str): Username in string format
        password (str): User's un-encrypted password in string format 
    """
    user = UserModel.find_by_username(username)
    if user and compare_digest(user.password, password):
        return user
    
    return None

def identity(payload: dict[str, int]):
    """
    Function that gets called when user has already authentiated, and Flask-JWT
    verified their authorization header is correct.

    Args:
        payload ([type]): A dictionary with 'identity' key, which is the user id.
    """
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)