from app import db, create_app
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
