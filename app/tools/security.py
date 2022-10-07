import base64
import hashlib
import hmac
import jwt
import calendar
from datetime import datetime, timedelta
from flask import current_app, request

from app.exceptions import NotAuthorized


def generate_hash(password):
    """
    Generate password hash
    """
    return base64.b64encode(hashlib.pbkdf2_hmac(
        current_app.config['HASH_ALGORYTHM'],
        password.encode('utf-8'),
        current_app.config['PWD_HASH_SALT'],
        current_app.config['PWD_HASH_ITERATIONS']
    )).decode('utf-8', 'ignore')


def generate_token(data: dict, refresh=False) -> str:
    """
    Generate token using JWT

    :param data: Payload for the token
    :param refresh: False: use default short time in minutes;
                    True: set expiration time to longer in days
    """
    if refresh:
        exp_time = datetime.utcnow() + timedelta(days=current_app.config['TOKEN_EXPIRE_DAYS'])
    else:
        exp_time = datetime.utcnow() + timedelta(minutes=current_app.config['TOKEN_EXPIRE_MINUTES'])

    data['exp'] = calendar.timegm(exp_time.timetuple())
    return jwt.encode(
        data,
        current_app.config['SECRET_KEY'],
        algorithm=current_app.config['JWT_ALGORYTHM']
    )


def decode_token(token: str) -> dict | None:
    """
    Decode a JWT token
    """
    try:
        data = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=[current_app.config['JWT_ALGORYTHM']]
        )
    except jwt.exceptions.InvalidTokenError:
        return None
    return data


def compare_passwords(password: str, password_hash: str):
    other_password_hash = generate_hash(password)
    return hmac.compare_digest(password_hash, other_password_hash)


def auth_required(func):
    """
    Decorator for Flask views that checks for a valid auth token

    Adds user_data keyword argument containing payload from token
    """
    def wrapper(*args, **kwargs):
        auth_data = request.headers.get('Authorization')
        if not auth_data:
            raise NotAuthorized('Authorization header required')

        token = auth_data.split('Bearer ')[-1]
        user_data = decode_token(token)

        if not user_data:
            raise NotAuthorized('Invalid token')
        return func(user_data=user_data, *args, **kwargs)

    return wrapper
