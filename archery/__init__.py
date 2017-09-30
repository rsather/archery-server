from flask import Flask
from archery.archers.views import archers

app = Flask(__name__)
app.register_blueprint(archers, url_prefix='/archers')

import archery.views
