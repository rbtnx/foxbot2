from website.dbmodel import db
from website.picker_app import create_app
from db_worker import get_games, db_update
import website.config as config

app = create_app(config.DevelopmentConfig)
app.app_context().push()
db.init_app(app)
db.create_all()
games, col = get_games("Fuchsteufel")
try: 
    db_update(db, games, col)
    print("DB successfully created")
except Exception as err:
    print("Error: ", err)