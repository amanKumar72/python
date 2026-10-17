from fastapi import APIRouter, Depends, Query
from project_2.models.review import ReviewCreate, ReviewUpdate, ReviewRead, Review, AverageRating
from project_2.exceptions.review import NoReviewsFoundException, ReviewNotFoundException
from project_2.config.database import get_session
from sqlmodel import Session, select, func
from datetime import datetime, timezone
router = APIRouter(prefix="/review", tags=["Review"])

@router.post("/", response_model=ReviewRead)
def create_review(
    review: ReviewCreate,
    session: Session = Depends(get_session)
):
    db_review = Review(**review.model_dump())

    session.add(db_review)
    session.commit()
    session.refresh(db_review)

    return db_review

@router.get("/", response_model=list[ReviewRead])
def get_all_reviews(
    reviewer_name: str | None = Query(default=None, description="Filter by reviewer name"),
    skip: int = Query(default=0, description="Number of records to skip"),
    limit: int = Query(default=10,ge=0, le=50, description="Number of records to return"),
    session: Session = Depends(get_session)
):
    query = select(Review)
    if reviewer_name:
        query = query.where(Review.reviewer_name == reviewer_name)
    query = query.offset(skip).limit(limit)
    reviews = session.exec(query).all()
    return reviews

@router.get("/average/{reviewer_name}", response_model=AverageRating)
def get_average_rating(
    reviewer_name: str,
    session: Session = Depends(get_session)
):
    query = select(
        func.avg(Review.rating).label("average_rating"),
        func.count(Review.id).label("total_reviews"),
    ).where(Review.reviewer_name == reviewer_name).group_by(Review.reviewer_name)

    average_rating: float | None = None
    total_reviews: int = 0

    result = session.exec(query).first()
    if result:
        average_rating, total_reviews = result
    else:
        average_rating = None
        total_reviews = 0
    if total_reviews == 0:
        raise NoReviewsFoundException()
    result = AverageRating(
        average_rating=average_rating,
        total_reviews=total_reviews,
        reviewer_name=reviewer_name
    )
    return result

@router.get("/{review_id}", response_model=ReviewRead)
def get_review(
    review_id: int,
    session: Session = Depends(get_session)
):
    review = session.get(Review, review_id)
    if not review:
        raise ReviewNotFoundException()
    return review

@router.put("/{review_id}", response_model=ReviewRead)
def update_review(
    review_id: int,
    review: ReviewUpdate,
    session: Session = Depends(get_session)
):
    db_review = session.get(Review, review_id)
    if not db_review:
        raise ReviewNotFoundException()
    review_data = review.model_dump(exclude_unset=True)
    for key, value in review_data.items():
        setattr(db_review, key, value)
    db_review.updated_at = datetime.now(timezone.utc)
    session.add(db_review)
    session.commit()
    session.refresh(db_review)
    return db_review

@router.delete("/{review_id}", response_model=ReviewRead)
def delete_review(
    review_id: int,
    session: Session = Depends(get_session)
):
    db_review = session.get(Review, review_id)
    if not db_review:
        raise ReviewNotFoundException()
    session.delete(db_review)
    session.commit()
    return db_review
