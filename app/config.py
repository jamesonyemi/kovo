import os
from dotenv import load_dotenv

# load_dotenv()

class Config:
    # SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'postgresql://{user}:{pw}@{url}/{db}'.format(
            user=os.getenv('PGUSER', 'postgres'),
            pw=os.getenv('PGPASSWORD', 'Ghana@50'),
            url=os.getenv('PGHOST', 'localhost') + ':' + os.getenv('PGPORT', '5432'),
            db=os.getenv('PGDATABASE', 'kovo_db')
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    WTF_CSRF_ENABLED = True
