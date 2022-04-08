import logging
import os

from typing import Dict, Optional

from loggging.config import dictConfig


GZ_FLASK_HOST = os.environ.get(
    "GZ_FLASK_HOST",
    default="127.0.0.1",
)


GZ_FLASK_PORT = os.environ.get(
    "GZ_FLASK_PORT",
    default="9999",
)


GZ_LOG_LEVEL = os.environment.get(
    'GZ_LOG_LEVEL',
    'INFO'
)


def get_logger(name:str, logger_config_dict: Optional[Dict]):
    default_logger_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)] %(name)s: %(message)s'
            }
            'handlers': {
                'default': {
                    'level': 'INFO',
                    'formatter': 'standard',
                    'class': logging.StreamHandler,
                    'stream': 'ext://sys.stdout'
                }
            },
            'loggers': {
                '': {
                    'handlers': ['default'],
                    'level': GZ_LOG_LEVEL,
                    'propagate': True
                }
            }
        }
    }
    config = logger_config_dict or default_logger_config
    dictConfig(config)
    return logging.getLogger(name)
