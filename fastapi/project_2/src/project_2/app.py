from fastapi import FastAPI
from contextlib import asynccontextmanager
from project_2.config.database import create_tables
from project_2.routes.review import router as review_router
from project_2.exceptions.review import NoReviewsFoundException, ReviewNotFoundException, handle_no_reviews_found_exception, handle_review_not_found_exception

@asynccontextmanager
async def lifespan(app: FastAPI):
    """ lifespan of the application """
    print("Application is starting...")
    create_tables()
    print("Tables created successfully")
    yield
    print("Application is shutting down...")

app = FastAPI(
    title="RangManch Review API",
    description="API for review management",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan
)
app.add_exception_handler(NoReviewsFoundException, handle_no_reviews_found_exception)
app.add_exception_handler(ReviewNotFoundException, handle_review_not_found_exception)

app.include_router(review_router)

@app.get("/")
def health_check():
    return {
        "status": 200,
        "message": "OK"
    }
