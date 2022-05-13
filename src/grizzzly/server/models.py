import os
from typing import Dict, List, Optional

from grizzzly.settings import GZ_DATASET_STORAGE_PATH


class Dataset:

    def __init__(self, name: str, author: str, obj_id: Optional[str] = None):
        self.name = name
        self.author = author
        self.obj_id = os.listdir(
            os.path.join(
                GZ_DATASET_STORAGE_PATH,
                author,
                name,
            )
        ).pop(0)

    @staticmethod
    def from_requests_args(**kwargs):
        name = kwargs.get("name")
        author = kwargs.get("author")
        return Dataset(name=name, author=author)

    @property
    def info(self) -> Dict:
        return {
            "author": self.author,
            "name": self.name,
            "dataset_id": self.obj_id,
            "dataset_path": self.get_fullpath(),
            "partitions": self.partitions,
        }

    def get_fullpath(self) -> str:
        return os.path.join(
            GZ_DATASET_STORAGE_PATH,
            self.author,
            self.name,
            self.obj_id,
        )

    @property
    def partitions(self) -> List[str]:
        return sorted(
            part
            for part in os.listdir(self.get_fullpath())
            if "=" in part
        )
