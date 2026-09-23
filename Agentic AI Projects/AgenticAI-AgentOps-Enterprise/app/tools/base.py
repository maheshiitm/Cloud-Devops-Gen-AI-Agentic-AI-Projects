from abc import ABC, abstractmethod
from pydantic import BaseModel

class ToolSpec(BaseModel):
    name: str
    description: str
    permissions: list[str]
    mutating: bool = False

class BaseTool(ABC):
    spec: ToolSpec
    @abstractmethod
    def run(self, arguments): ...
