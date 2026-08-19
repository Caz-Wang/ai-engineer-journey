from dataclasses import asdict, dataclass
import json


@dataclass
class Post:
    user_id: int
    id: int
    title: str
    body: str

    def __post_init__(self):
        if self.user_id <= 0:
            raise ValueError("user_id must be positive")

        if self.id <= 0:
            raise ValueError("id must be positive")

        if not self.title.strip():
            raise ValueError("title cannot be empty")

        if not self.body.strip():
            raise ValueError("body cannot be empty")

    def to_dict(self) -> dict:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())