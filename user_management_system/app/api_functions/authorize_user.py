import ast
import base64
import hashlib
import hmac
from app.utils import current_time
from flask import request, abort
from instance import config


def generate_access_token(user_id):
    payload_dict = {
        "userId": user_id,
        "iat": current_time.get_current_epoc_time() + config.TOKEN_ACTIVATION_TIME
    }
    header = '{"alg":"HS256","typ":"JWT"}'
    payload = str(payload_dict)
    unsignedToken = base64.b64encode(header) + '.' + base64.b64encode(payload)
    signature = hmac.new(unsignedToken, config.SECRET_KEY, digestmod=hashlib.sha256).digest()
    token = base64.b64encode(header) + '.' + base64.b64encode(payload) + '.' + base64.b64encode(signature)
    return token