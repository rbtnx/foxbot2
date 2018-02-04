import os
from website.picker_app import create_app
import website.config as config

config_object = eval(os.environ['FLASK_APP_CONFIG'])
app = create_app(config_object)

if __name__ == "__main__":
    app.run()
