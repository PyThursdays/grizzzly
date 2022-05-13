from typing import Optional

import requests
import pandas as pd

from grizzzly.settings import (
    get_logger,
    GZ_ENDPOINT_ALIAS,
)


logger = get_logger(__name__)


def download_dataset(author: str, name: str, part: Optional[str] = None) -> pd.DataFrame:
    if not name:
        logger.warning("Name was not provided; retrieving the default dataset")
    response = requests.get(
        GZ_ENDPOINT_ALIAS["download-dataset-partition"],
        params={
            "author": author,
            "name": name,
            "partition": part,
        }
    )
    if not response.ok:
        raise ValueError("There was a problem while getting the dataset")
    payload = response.json()
    next_partition = payload["next"]
    print(len(payload["data"]))
    if next_partition:
        return pd.concat([
            pd.DataFrame(payload["data"]),
            download_dataset(author=author, name=name, part=next_partition)
        ])
    return pd.DataFrame(payload["data"])
