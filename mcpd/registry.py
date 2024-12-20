from typing import Protocol, Optional
from pydantic import BaseModel


class MCPServerSpec(BaseModel):
    name: str
    github_repo: Optional[str]
    default_dockerfile_content: Optional[str]
    env: dict[str, str]


class Registry(Protocol):
    def get(self, name: str) -> MCPServerSpec: ...
    def lookup_github_repo(self, repo: str) -> Optional[MCPServerSpec]: ...
    def search(self, query: str) -> list[MCPServerSpec]: ...
