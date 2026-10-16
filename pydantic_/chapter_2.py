from pydantic import BaseModel, field_validator
from typing import Optional, List

# selt referencing model
class Comment(BaseModel):
    author: str
    text: str
    likes: int = 0
    replies: Optional[List['Comment']] = None

    @field_validator("likes")
    def likes_validator(cls, value):
        if value < 0:
            raise ValueError("Likes cannot be negative")
        return value

Comment.model_rebuild()

reply1 = Comment(author='Alice', text='Great post!', likes=5)
reply2 = Comment(author='Bob', text='I agree!', likes=3)
comment = Comment(author='John', text='Nice article!', likes=10, replies=[reply1, reply2])
print(comment.model_dump_json(indent=2))