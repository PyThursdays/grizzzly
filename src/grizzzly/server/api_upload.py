from flask import Blueprint, request


# Create an upload endpoint
api_upload = Blueprint(
    name="upload",
    import_name=__name__,
    url_prefix="/upload"
)


@api_upload.route("/", methods=["GET", "POST"]) # Remove GET when we stop browser testing
def upload():
    payload = request.get_json()
    batch_data = params.get("batch_data")
    return f"Payload received: {batch_data}"
