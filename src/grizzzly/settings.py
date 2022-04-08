import logging
import os

from typing import Dict, Optional

from loggging.config import dictConfig


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
