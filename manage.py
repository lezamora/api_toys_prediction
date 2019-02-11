import os
import sys
sys.path.append('./app/')


from flask_script import Manager

from app import blueprint
from app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    app.run(host='localhost', port=6060)



if __name__ == '__main__':
    manager.run()
