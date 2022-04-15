import requests
import pandas as pd

from grizzzly.settings import (
    GZ_ENDPOINT_ALIAS,
    GZ_FLASK_HOST,
    GZ_FLASK_PORT,
)



def download_dataset(name: str) -> pd.DataFrame:
    url = f"http://{GZ_FLASK_HOST}:{GZ_FLASK_PORT}/download"
    response = requests.get(GZ_ENDPOINT_ALIAS["download-dataset"])
    if not response.ok:
        raise ValueError("There was a problem while getting the dataset")
    data = response.json()
    return pd.DataFrame(data)
