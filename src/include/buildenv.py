import os

try:
    os.environ['IS_HEROKU_USE']
    from src.include.buildenv_heroku import *
except KeyError:
    from src.include.buildenv_local import *