import os

import pandas as pd
from flask import Blueprint, request, jsonify


from grizzzly.server.models import Dataset
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


@api_download.route("/part", methods=["GET"])
def download_part():
    # Global parameters on the query string
    params = request.args.to_dict()
    # Create dataset instance and ge partition list
    dataset = Dataset.from_requests_args(**params)
    partitions = dataset.partitions
    # Get current partition request, or fallback to first partition
    current_partition = params.get("partition") or partitions[0]
    # Identify next partition
    next_partition_index = partitions.index(current_partition)
    next_partitions = partitions[next_partition_index+1:]
    # Read partition
    partition_path = os.path.join(
        dataset.get_fullpath(),
        current_partition
    )
    partition_data = pd.read_parquet(partition_path)
    return jsonify(
        {
            "next": next_partitions[0] if len(next_partitions) else None,
            "data":  list(partition_data.T.to_dict().values())

        }
    )


# Register endpoints
@api_download.route("/", methods=["GET"])
def download():
    # Global parameters on the query string
    params = request.args.to_dict()
    dataset = Dataset.from_requests_args(**params)
    # TODO: Do it by chunks!
    df = pd.read_parquet(dataset.get_fullpath())
    # Transform the dataset into a JSON
    payload = list(df.T.to_dict().values())
    return jsonify(payload)
