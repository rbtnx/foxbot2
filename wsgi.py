import os
from flask_sqlalchemy import SQLAlchemy
from website.picker_app import create_app
from website.dbmodel import db
import website.config as config

config_object = eval(os.environ['FLASK_APP_CONFIG'])
app = create_app(config_object)
db.init_app(app)

if __name__ == "__main__":
    app.run()
