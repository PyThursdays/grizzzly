from typing import Optional

import requests
import pandas as pd

from grizzzly.settings import (
    get_logger,
    GZ_ENDPOINT_ALIAS,
)


logger = get_logger(__name__)


def download_dataset(author: str, name: str) -> pd.DataFrame:
    if not name:
        logger.warning("Name was not provided; retrieving the default dataset")
    response = requests.get(
        GZ_ENDPOINT_ALIAS["download-dataset"],
        params={
            "author": author,
            "name": name,
        }
    )
    if not response.ok:
        raise ValueError("There was a problem while getting the dataset")
    data = response.json()
    return pd.DataFrame(data)
