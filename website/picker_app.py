from flask import Flask, Blueprint
from werkzeug.utils import find_modules, import_string
from website.dbmodel import db
import website.utils as utils

def create_app(config):
    """
    Flask application factory, Development, Test, Staging, and Production
    configs may engage / disengage different application features.
    """
    # Create unconfigured flask application
    app = Flask(
        config.APP_NAME,
        template_folder="website/templates"
    )

    # Configure flask application
    app.config.from_object(config)
    app.static_folder = config.STATIC_FOLDER

    # register functions are like set-methods for blueprints, databases, etc.
    registration_functions = [
        register_blueprints,
        #register_error_pages,
        # register_database,
        # register_context_processors,
    ]

    for r in registration_functions:
        r(app)
    db.init_app(app)

    return app

def register_blueprints(app):
    """
    Will find all blueprints within website.views and update them to the app
    """
    view_modules = map(import_string, find_modules("website.views"))

    for view_module in view_modules:
        blueprints = utils.get_classes_of_type(
            view_module,
            Blueprint
        )

        for blueprint in blueprints:
            app.register_blueprint(blueprint)
