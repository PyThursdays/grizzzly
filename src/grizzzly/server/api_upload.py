import os

import pandas as pd
from flask import Blueprint, request

from grizzzly.settings import GZ_BASEPATH, get_logger


logger = get_logger(__name__)


# Create an upload endpoint
api_upload = Blueprint(
    name="upload",
    import_name=__name__,
    url_prefix="/upload"
)


@api_upload.route("/create", methods=["GET"])
def create():
    # Be sure to create the filesystem configurations
    # TODO: Allow overwriting
    params = request.args.to_dict()
    name = params.get("name")
    author = params.get("author", "generic")  # Generic public author
    if not name or not author:
        return "Missing name parameter", 400
    relative_output_path = os.path.join(author, name)
    absolute_output_path = os.path.join(
        GZ_BASEPATH,
        relative_output_path
    )

    logger.info("Creating the absolute output path")
    os.makedirs(absolute_output_path, exist_ok=True)
    return "ok!"




@api_upload.route("/chunk", methods=["POST"]) # Remove GET when we stop browser testing
def upload():
    payload = request.get_json()
    chunk = pd.DataFrame(payload.get("chunk"))
    return "ok"
