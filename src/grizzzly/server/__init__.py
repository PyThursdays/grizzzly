from flask import Flask


# Import the endpoint
from grizzzly.server.api_hello import api_hello as hello

# Flask application instance
app = Flask(__name__)

# Register the endpoints
app.register_blueprint(hello)
