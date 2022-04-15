import logging
import posixpath
import os

from logging.config import dictConfig
from typing import Dict, Optional


# Backend

GZ_FLASK_HOST = os.environ.get(
    "GZ_FLASK_HOST",
    default="127.0.0.1",
)


GZ_FLASK_PORT = os.environ.get(
    "GZ_FLASK_PORT",
    default="9999",
)

GZ_FLASK_SSL = os.environ.get(
    "GZ_FLASK_SSL",
    default="false",
).lower().startswith("t")

GZ_API_URL = f"http{'s' if GZ_FLASK_SSL else ''}://{GZ_FLASK_HOST}:{GZ_FLASK_PORT}"

GZ_ENDPOINT_ALIAS = {
    "hello": posixpath.join(GZ_API_URL, "hello"),
    "download-dataset": posixpath.join(GZ_API_URL, "download"),
}

GZ_API_DEFAULT_DOWNLOAD_DATASET = os.environ.get(
    "GZ_API_DEFAULT_DOWNLOAD_DATASET",
    default="https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
)


GZ_LOG_LEVEL = os.environ.get(
    'GZ_LOG_LEVEL',
    default='INFO'
)


def get_logger(name: str, logger_config_dict: Optional[Dict] = None):
    default_logger_config = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',
            },
        },
        'loggers': {
            '': {
                'handlers': ['default'],
                'level': GZ_LOG_LEVEL,
                'propagate': True
            },
            '__main__': {
                'handlers': ['default'],
                'level': GZ_LOG_LEVEL,
                'propagate': True
            },
        }
    }
    config = logger_config_dict or default_logger_config
    dictConfig(config)
    return logging.getLogger(name)
