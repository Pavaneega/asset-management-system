PG_CONFIG = {
    'LOC': {
        'host': '127.0.0.1',
        'port': '5432',
        'database': 'turbine_management_authentication',
        'username': 'rajesh',
        'password': 'rajesh@302'
    }
}


#mongo db configuration
MONGO_CONFIGS = {
        'LOC' : {
            'db_host' : '127.0.0.1',
            'db_port' : '27017',
            'db_name' : 'tubine_management_system',
            'user' : 'localmongoadmin',
            'pass' : 'localmongoadmin',
            'auth_src_db' : 'admin',
            'auth_mechanism' : 'SCRAM-SHA-1'
        },
}

APP_CONFIGS = {
    'LOC': {
        'BASE_URL': 'http://127.0.0.1',
    },
}

base_url = 'http://127.0.0.1:5004'