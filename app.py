from flask import Flask, render_template, request

import sys
sys.path.append("src")
from view.web import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint.blueprint)

if __name__ == "__main__":
    app.run(debug=True)
    