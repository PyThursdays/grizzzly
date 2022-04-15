import json
import requests
from typing import Optional

import pandas as pd

from grizzzly.settings import (
    GZ_FLASK_HOST,
    GZ_FLASK_PORT
)

def upload_dataset(
    dataset_name: str,
    df: pd.DataFrame,
    batch_size: Optional[int] = 1000
):
    url = f"{GZ_FLASK_HOST}:{GZ_FLASK_PORT}/upload"
    json_data = json.loads(df.to_json(orient="records"))
    for index in range(0, len(json_parsed), batch_size):
        upper_index = (
            (index + batch_size)
            if (index + batch_size) <= len(json_parsed)
            else len(json_parsed)
        )
        response = requests.post(url, data=str(json_data[index:upper_index]))
