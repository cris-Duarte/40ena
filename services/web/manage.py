from flask.cli import FlaskGroup

from project import *


cli = FlaskGroup(app)



if __name__ == "__main__":
    cli()
