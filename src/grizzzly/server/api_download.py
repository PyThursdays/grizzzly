import os

import pandas as pd
from flask import Blueprint, request, jsonify

from grizzzly.settings import (
    GZ_API_DEFAULT_DOWNLOAD_DATASET,
    GZ_DATASET_STORAGE_PATH,
)


# Create endpoint blueprint
api_download = Blueprint(
    name="download",
    import_name=__name__,
    url_prefix="/download"
)


# Register endpoints
@api_download.route("/", methods=["GET"])
def download():
    # Global parameters on the query string
    params = request.args.to_dict()
    # Dataset parameters
    dataset_author = params.get("author")
    dataset_name = params.get("name")
    # Verify if both author and dataset name are provided
    if not all([dataset_author, dataset_name]):
        raise ValueError(
            "You should provide both dataset name & author."
        )
    # Re-build the dataset path
    dataset_path = os.path.join(
        GZ_DATASET_STORAGE_PATH,
        dataset_author,
        dataset_name
    )
    # Read the dataset back into memory
    # TODO: Do it by chunks!
    df = pd.read_parquet(dataset_path)
    # Transform the dataset into a JSON
    payload = list(df.T.to_dict().values())
    return jsonify(payload)
