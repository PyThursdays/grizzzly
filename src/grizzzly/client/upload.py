import json
import requests
from typing import Optional

import pandas as pd
import numpy as np

from grizzzly.settings import (
    get_logger,
    GZ_ENDPOINT_ALIAS
)


def upload_dataset(
    name: str,
    df: pd.DataFrame,
    author: Optional[str] = None,
    batch_size: int = 1000,
):
    # Call the create endpoint
    response = requests.get(GZ_ENDPOINT_ALIAS["create-dataset"] + f"?name={name}")
    if not response.ok:
        raise ValueError("Error when calling the create-dataset endpoint")

    records = len(df)
    batches = {}
    for index in range(0, records, batch_size):
        upper_index = (
            (index + batch_size)
            if (index + batch_size) <= records
            else records
        )
        chunk = df[index: upper_index].assign(gz_chunk_part=index)
        batches[index] = requests.post(
            GZ_ENDPOINT_ALIAS["upload-dataset"],
            json={
                "name": name,
                "author": author,
                "chunk": chunk.to_dict(orient="records")
            }
        ).ok
    return batches
