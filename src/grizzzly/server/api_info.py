import os

import pandas as pd
from flask import Blueprint, request, jsonify

from grizzzly.server.models import Dataset
from grizzzly.settings import (
    GZ_API_DEFAULT_DOWNLOAD_DATASET,
    GZ_DATASET_STORAGE_PATH,
)


# Create endpoint blueprint
api_info = Blueprint(
    name="info",
    import_name=__name__,
    url_prefix="/info"
)


# Register endpoints
@api_info.route("/", methods=["GET"])
def info():
    # Global parameters on the query string
    params = request.args.to_dict()
    dataset = Dataset.from_requests_args(**params)
    return jsonify(dataset.info)
