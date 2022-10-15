from secret_key_generator import secret_key_generator


# DEVELOPMENT KEY
DEV_SECRET_KEY = SECRET_KEY = secret_key_generator.generate(len_of_secret_key=50)

# TESTING KEY
TEST_SECRET_KEY = secret_key_generator.generate(len_of_secret_key=50)

# PRODUCTION KEY
SECRET_KEY = secret_key_generator.generate(len_of_secret_key=50)

# DEVELOPMENT DATABASE SETTINGS
DEV_DB_HOST = 'localhost'
DEV_DB_USER = 'root'
DEV_DB_PASS = 'root'
DEV_DB_NAME = 'municipio'

# PRODUCTION DATABASE SETTINGS (Default)
DB_HOST = 'dbase'
DB_USER = 'root'
DB_PASS = 'H*a260182*Ha'
DB_NAME = 'municipio'