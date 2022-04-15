from flask import Blueprint, request


# Create an upload endpoint
api_upload = Blueprint(
    name="upload",
    import_name=__name__,
    url_prefix="/upload"
)


@api_upload.route("/", methods=["GET", "POST"]) # Remove GET when we stop browser testing
def upload():
    params = request.args.to_dict()
    payload = params.get("payload")
    return f"Payload received: {payload}"
