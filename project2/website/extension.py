# create extension.py to fix ImportError: cannot import name 'db' from partially initialized module 'website' (most likely due to a circular impo

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()