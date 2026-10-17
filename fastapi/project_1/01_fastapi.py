from fastapi import FastAPI
from fastapi import Request, Query
from fastapi import HTTPException
import uvicorn
from models import UsersResponse
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]
app = FastAPI(
    title="My FastAPI Application",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def read_root():
    """
    Read the root endpoint.
    """
    # fast api will auto convert the return value to JSON
    return {"message": "World", "status": "success"}

@app.get("/hello")
def read_hello():
    """
    Read the hello endpoint.
    """
    return {"message": "Hello", "status": "success"}

@app.get("/debug/request")
def debug_request(request: Request):
    """
    Debug the request object.
    """
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "path_params": request.path_params,
    }

@app.get("/users", response_model=UsersResponse)
def get_users(limit: int = Query(10, description="Limit the number of users returned")):
    """
    Get a list of users with a limit on the number of users returned.
    """
    # Return the list of users with the specified limit
    return UsersResponse(
        users=users[:limit],
        status="success",
        success=True
    )

@app.get("/users/{user_id}")
def get_user(user_id: str):
    """
    Get a user by ID.
    """
    user = None
    for u in users:
        if u["id"] == int(user_id):
            user = u
            break
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user, "status": "success", "success": True}