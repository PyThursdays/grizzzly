import os


GZ_FLASK_HOST = os.environ.get(
    "GZ_FLASK_HOST",
    default="127.0.0.1",
)


GZ_FLASK_PORT = os.environ.get(
    "GZ_FLASK_PORT",
    default="9999",
)
