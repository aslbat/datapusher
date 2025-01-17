import os
import uuid
import sys
import logging

DEBUG = False
TESTING = False
SECRET_KEY = str(uuid.uuid4())
USERNAME = str(uuid.uuid4())
PASSWORD = str(uuid.uuid4())

NAME = 'datapusher'

#
# Webserver host and port
#
HOST = os.environ.get('DATAPUSHER_HOST', '0.0.0.0')
PORT = os.environ.get('DATAPUSHER_PORT', 8800)

#
# Database
#
SQLALCHEMY_DATABASE_URI = os.environ.get('DATAPUSHER_SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/job_store.db')

#
# Download and streaming settings
#
MAX_CONTENT_LENGTH = int(os.environ.get('DATAPUSHER_MAX_CONTENT_LENGTH', '1024000'))
CHUNK_SIZE = int(os.environ.get('DATAPUSHER_CHUNK_SIZE', '16384'))
CHUNK_INSERT_ROWS = int(os.environ.get('DATAPUSHER_CHUNK_INSERT_ROWS', '250'))
DOWNLOAD_TIMEOUT = int(os.environ.get('DATAPUSHER_DOWNLOAD_TIMEOUT', '30'))

#
# Verify SSL (Prevent overlapping with CKAN SSL_VERIFY)
#
DATAPUSHER_SSL_VERIFY = os.environ.get('DATAPUSHER_SSL_VERIFY', True)
