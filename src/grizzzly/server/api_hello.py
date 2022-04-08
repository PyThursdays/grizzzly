from flask import Blueprint, request


# Create endpoint blueprint
api_hello = Blueprint(
    "hello",
    __name__,
    url_prefix="/hello"
)


# Register endpoints
@api_hello.route("/", methods=["GET"])
def hello_world():
    params = request.args.to_dict()
    name = params.get("name", "world")
    return f"Hello, {name}!"
