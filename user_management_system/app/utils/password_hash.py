# import hashlib
# import hmac
# import base64
# from instance import app
#
# def create_hash_password(pass_string=app.config['DEFAULT_PASSWORD'], secret_key=app.config['SECRET_KEY']):
#     message = bytes(pass_string).encode('utf-8')
#     secret = bytes(secret_key).encode('utf-8')
#     signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
#     return signature