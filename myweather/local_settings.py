from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ========== SQLite ==========
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========== PostgreSQL ==========
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'incomeexpensesdb',
#         'USER': 'postgres',
#         'PASSWORD': '1309',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# ========== MySQL ==========
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': 'root',
#         'PASSWORD': '1309',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }
