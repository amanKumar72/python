from fastapi import Request
from fastapi.responses import JSONResponse

class InvalidPincodeError(Exception):
    def __init__(self, message: str = "Invalid Pincode") -> None:
        self.message = message
        super().__init__(self.message)

class PincodeNotFoundError(Exception):
    def __init__(self, message: str = "Pincode Not Found") -> None:
        self.message = message
        super().__init__(self.message)

def invalid_pincode_error_handler(request: Request, exc: InvalidPincodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "invalid_pincode",
            "message": exc.message,
        }
    )

def pincode_not_found_error_handler(request: Request, exc: PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "pincode_not_found",
            "message": exc.message,
        }
    )