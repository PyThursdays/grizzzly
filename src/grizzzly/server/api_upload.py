import os
import uuid

import pandas as pd
from flask import Blueprint, request

from grizzzly.settings import (
    GZ_BASEPATH,
    GZ_DATASET_STORAGE_PATH,
    get_logger
)


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
    relative_output_path = os.path.join(author)
    absolute_output_path = os.path.join(
        GZ_BASEPATH,
        relative_output_path
    )

    logger.info("Creating the absolute output path")
    os.makedirs(absolute_output_path, exist_ok=True)
    return "ok!"


@api_upload.route("/chunk", methods=["POST"])
def upload():
    payload = request.get_json()
    dataset_name = payload.get("name") or "default"
    dataset_author = payload.get("author") or "generic"
    dataset_id = str(uuid.uuid5(
        uuid.NAMESPACE_OID,
        f"{dataset_author}-{dataset_name}"
    ))
    print(dataset_name, dataset_author, dataset_id)
    chunk_df = pd.DataFrame(payload.get("chunk", []))
    chunk_df.to_parquet(
        path=os.path.join(
            GZ_DATASET_STORAGE_PATH,
            dataset_author,
            dataset_name,
            dataset_id
        ),
        partition_cols=["gz_chunk_part"],
        compression="snappy",
        engine="fastparquet"
    )
    return "ok"
