from pathlib import Path
import os
import djongo
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env.dev'))
if __name__ == '__main__':
    print(env('DJANGO_ALLOWED_HOSTS').split(' '))