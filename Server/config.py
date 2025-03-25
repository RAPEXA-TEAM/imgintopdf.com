#!/usr/bin/env

from os.path import join, dirname, realpath

SECRET_KEY     = "secret!"
HOST           = "0.0.0.0"
RUNNING_PORT   = 5550
DEBUG_MODE     = True

# MySQL Configs

MYSQL_HOST     = "127.0.0.1"
MYSQL_USER     = "selleruserr"
MYSQL_PASS     = "Sellerpass1!"
MYSQL_DATABASE  = "sells"

#Upload settings

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', "ico"} #TODO: add this formats too esp - webp - heic - al - vector
UPLOADS_PATH = join(dirname(realpath(__file__)), 'Uploads')