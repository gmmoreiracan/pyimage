# schemas/image.py
from pydantic import BaseModel, Field
from typing import List, Dict, Any


class ImageSchema(BaseModel):
    repo_digest: str
    local_digest: str
    repo: str
    name: str
    tag: str
    layers: List[Dict[str, Any]] = Field(default_factory=list)
    variables: List[Dict[str, Any]] = Field(default_factory=list)
