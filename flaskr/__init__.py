import os

from flask import Flask

from flask import (
    redirect, render_template, g
)
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.environ["POSTGRES_DB"],
        USER=os.environ["POSTGRES_USER"],
        PASSWORD=os.environ["POSTGRES_PASSWORD"],
        
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import auth
    app.register_blueprint(auth.bp)
    
    
    

    @app.route('/')
    def index():
        return render_template("base.html", g=g)

    return app