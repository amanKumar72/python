from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime, timezone

# for table
class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rating: int = Field(ge=0, le=5)
    reviewer_name: Optional[str] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    
# for validation
class ReviewCreate(SQLModel):
    rating: int = Field(ge=0, le=5)
    reviewer_name: Optional[str] = Field(default=None)
    comment: Optional[str] = Field(default=None)

class ReviewRead(SQLModel):
    id: int
    rating: int
    reviewer_name: Optional[str] = Field(default=None)
    comment: Optional[str] = Field(default=None)
    created_at: datetime
    updated_at: datetime
    
# for update
class ReviewUpdate(SQLModel):
    rating: Optional[int] = Field(default=None, ge=0, le=5)
    comment: Optional[str] = Field(default=None)

class AverageRating(SQLModel):
    average_rating: float
    reviewer_name: str
    total_reviews: int