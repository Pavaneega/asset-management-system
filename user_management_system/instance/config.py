import os
import sys
from instance.dbconfig import PG_CONFIG,MONGO_CONFIGS


#db_conf = db_config.postgres
# parameterizing db configs as per env set



PG_URI = 'postgresql://{username}:{password}@{host}/{database}'.format(
username=PG_CONFIG['LOC']['username'],
password=PG_CONFIG['LOC']['password'],
host=PG_CONFIG['LOC']['host'],
database=PG_CONFIG['LOC']['database'])


SQLALCHEMY_DATABASE_URI= PG_URI


SECRET_KEY = 'xwJU0A54ThRQIUSxBsLn'
TOKEN_ACTIVATION_TIME = 86400000

# MONGO_URI = 'mongodb://{user}:{pass}@{db_host}:{db_port}/{db_name}?authSource={auth_src_db}&authMechanism={auth_mechanism}'.\
#         format(**MONGO_CONFIGS['LOC'])


