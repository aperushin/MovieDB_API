import base64
import calendar
import datetime
import hashlib
import jwt
from flask import request, abort
from datetime import datetime, timedelta

from app.config import BaseConfig


def generate_hash(password):
    return base64.b64encode(hashlib.pbkdf2_hmac(
        BaseConfig.HASH_ALGORYTHM,
        password.encode('utf-8'),
        BaseConfig.PWD_HASH_SALT,
        BaseConfig.PWD_HASH_ITERATIONS
    )).decode('utf-8', 'ignore')


def generate_token(data: dict, refresh=False) -> str:
    """
    Generate token using JWT

    :param data: Payload for the token
    :param refresh: False: use default short time in minutes;
                    True: set expiration time to longer in days
    """
    if refresh:
        exp_time = datetime.utcnow() + timedelta(days=BaseConfig.TOKEN_EXPIRE_DAYS)
    else:
        exp_time = datetime.utcnow() + timedelta(minutes=BaseConfig.TOKEN_EXPIRE_MINUTES)

    data['exp'] = calendar.timegm(exp_time.timetuple())
    return jwt.encode(
        data,
        BaseConfig.SECRET_KEY,
        algorithm=BaseConfig.JWT_ALGORYTHM
    )


def decode_token(token: str) -> dict | None:
    """
    Decode a JWT token
    """
    try:
        data = jwt.decode(
            token,
            BaseConfig.SECRET_KEY,
            algorithms=[BaseConfig.JWT_ALGORYTHM]
        )
    except jwt.exceptions.InvalidTokenError:
        return None
    return data


def auth_required(func):
    """
    Decorator for Flask views that checks for a valid auth token
    """
    def wrapper(*args, **kwargs):
        auth_data = request.headers.get('Authorization')
        if not auth_data:
            abort(401)

        token = auth_data.split('Bearer ')[-1]
        user_data = decode_token(token)

        if not user_data:
            abort(401)
        return func(user_data=user_data, *args, **kwargs)

    return wrapper
