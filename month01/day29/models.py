from dataclasses import dataclass
from typing import TypedDict

class PostData(TypedDict):
    id: int
    title: str
    body: str

@dataclass
class Post:
    id: int
    title: str
    body: str

def post_from_dict(data: PostData) -> Post:
    return Post(
        id=data["id"],
        title=data["title"],
        body=data["body"],
    )
    
