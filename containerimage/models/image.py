from dataclasses import dataclass
from typing import List


@dataclass
class Image:
    repo_digest: str
    local_digest: str
    repo: str
    name: str
    tag: str
    layer_ids: List[int] = None
    variable_ids: List[int] = None

    def __post_init__(self):
        if self.layer_ids is None:
            self.layer_ids = []
        if self.variable_ids is None:
            self.variable_ids = []
