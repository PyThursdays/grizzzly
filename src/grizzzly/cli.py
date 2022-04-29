import time
from typing import Optional

import pandas as pd

from grizzzly.client import (
    download_dataset,
    upload_dataset,
)
from grizzzly.settings import (
    get_logger,
    GZ_FLASK_HOST,
    GZ_FLASK_PORT,
    GZ_API_DEFAULT_DOWNLOAD_DATASET,
)


logger = get_logger(__name__)


class CLIServer:

    def run(
            self,
            host: Optional[str] = None,
            port: Optional[str] = None,
            debug: bool = False,
            prod: bool = False,
    ):
        import importlib

        # Server configuration
        host = host or GZ_FLASK_HOST
        port = port or GZ_FLASK_PORT
        # Get server flask application
        server = importlib.import_module("grizzzly.server")
        app = getattr(server, "app")
        # Start the server
        if not prod:
            return app.run(
                host=host,
                port=port,
                debug=debug,
            )
        waitress = importlib.import_module("waitress")
        serve = getattr(waitress, "serve")
        return serve(
            app,
            host=host,
            port=port,
        )


class CLI:

    def __init__(self):
        self.start = time.time()
        self.backend = CLIServer()

    def hello(self, name: Optional[str] = None):
        name = name or "world"
        logger.info("This is an info log!")
        logger.warning("This is a warning log!")
        logger.error("This is an error log!")
        print(f"Hello, {name}!")

    def upload_default(self, name: str, author: str):
        df = pd.read_csv(GZ_API_DEFAULT_DOWNLOAD_DATASET)
        upload_dataset(
            name=name,
            df=df,
            author=author,
        )

    def download(self, name: str, author: str, limit: Optional[int] = None) -> str:
        df = download_dataset(
            name=name,
            author=author
        )
        subset = df if limit is None else df.head(limit)
        return subset.to_string()
