from flask import Flask


# Import the endpoint
from grizzzly.server.api_hello import api_hello as hello
from grizzzly.server.api_upload import api_upload as upload
from grizzzly.server.api_download import api_download as download

# Flask application instance
app = Flask(__name__)

# Register the endpoints
app.register_blueprint(hello)
app.register_blueprint(upload)
app.register_blueprint(download)
