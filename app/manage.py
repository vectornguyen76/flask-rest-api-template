import os
from flask_script import Manager
from main import create_app
from __init__ import api_blueprint

app = create_app()

# Register main Blueprint
app.register_blueprint(api_blueprint)

# Set up
# app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host="0.0.0.0", port=port, use_reloader=True)

if __name__ == "__main__":
    run()