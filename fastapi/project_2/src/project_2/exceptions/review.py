from fastapi import Request
from fastapi.responses import JSONResponse

class NoReviewsFoundException(Exception):
    def __init__(self, message: str = "No reviews found for this reviewer"):
        self.message = message
        super().__init__(self.message)

class ReviewNotFoundException(Exception):
    def __init__(self, message: str = "Review not found for this id"):
        self.message = message
        super().__init__(self.message)

def handle_no_reviews_found_exception(request: Request, exc: NoReviewsFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": exc.message}
    )

def handle_review_not_found_exception(request: Request, exc: ReviewNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": exc.message}
    )