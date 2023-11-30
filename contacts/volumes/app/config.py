from datetime import timedelta

SECRET_KEY = "8bPQghx3f96WbyEUQu7pBhHiTtk111uU"
PERMANENT_SESSION_LIFETIME =  timedelta(minutes=15)
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True

LDAP_SCHEMA = 'ldap'
LDAP_DOMAIN = 'contacts.int'
LDAP_HOST = 'ldap'
LDAP_PORT = 389
LDAP_USE_SSL = False
LDAP_BASE_DN = 'OU=Domain Users,DC=contacts,DC=int'
LDAP_BIND_DIRECT_CREDENTIALS = True
LDAP_USERNAME = 'connector'
LDAP_PASSWORD = 'Password1'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:////opt/contacts/db/contacts.db'

UPLOADED_PHOTOS_DEST = "static/img/contacts"
