import os


class Config(object):
    # set the SECRET_KEY value in the host server environment when this is deployed to prod
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
