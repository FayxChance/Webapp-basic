from flask import current_app, g
import psycopg2
import click

def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(
            host="db",
            database=current_app.config['DATABASE'],
            user=current_app.config['USER'],
            password=current_app.config['PASSWORD']
        )
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
