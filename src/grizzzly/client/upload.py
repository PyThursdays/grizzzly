import json
import requests
from typing import Optional

import pandas as pd

from grizzzly.settings import (
    get_logger,
    GZ_ENDPOINT_ALIAS
)

def upload_dataset(
    dataset_name: str,
    df: pd.DataFrame,
    batch_size: Optional[int] = 1000
):
    json_data = json.loads(df.to_json(orient="records"))
    for index in range(0, len(json_data), batch_size):
        upper_index = (
            (index + batch_size)
            if (index + batch_size) <= len(json_data)
            else len(json_data)
        )
        response = requests.post(
            GZ_ENDPOINT_ALIAS["upload-dataset"],
            data={"batch_data": str(json_data[index:upper_index])}
        )
