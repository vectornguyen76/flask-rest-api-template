import os
from flask_script import Manager
from app import create_app

app = create_app()

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=True)

if __name__ == "__main__":
    run()