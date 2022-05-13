from flask import Flask


# Import the endpoint
from grizzzly.server.api_hello import api_hello as hello
from grizzzly.server.api_upload import api_upload as upload
from grizzzly.server.api_download import api_download as download
from grizzzly.server.api_info import api_info as info

# Flask application instance
app = Flask(__name__)

# Register the endpoints
app.register_blueprint(info)
app.register_blueprint(hello)
app.register_blueprint(upload)
app.register_blueprint(download)
