from dataclasses import dataclass


@dataclass
class Post:
    user_id: int
    id: int
    title: str
    body: str