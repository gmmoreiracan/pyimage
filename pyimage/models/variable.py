from dataclasses import dataclass
from typing import List


@dataclass
class EnvironmentVariable:
    key: str
    value: str
    image_ids: List[int] = None

    def __post_init__(self):
        if self.image_ids is None:
            self.image_ids = []
