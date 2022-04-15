import pandas as pd
from flask import Blueprint, request, jsonify

from grizzzly.settings import GZ_API_DEFAULT_DOWNLOAD_DATASET


# Create endpoint blueprint
api_download = Blueprint(
    name="download",
    import_name=__name__,
    url_prefix="/download"
)


# Register endpoints
@api_download.route("/", methods=["GET"])
def download():
    # TODO: This is currently just a mockup
    df = pd.read_csv(GZ_API_DEFAULT_DOWNLOAD_DATASET)
    payload = list( df.T.to_dict().values())
    return jsonify(payload)
