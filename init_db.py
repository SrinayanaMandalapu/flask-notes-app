# init_db.py
import os
from app import create_app, db

app = create_app()

with app.app_context():
    if os.path.exists("app/db.sqlite3"):
        os.remove("app/db.sqlite3")
    db.create_all()
