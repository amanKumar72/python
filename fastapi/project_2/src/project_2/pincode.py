from fastapi import FastAPI
from project_2.models.pincode import Location, LocationResponse, BulkLocationRequest, BulkLocationResponse
from project_2.exceptions.pincode import InvalidPincodeError, PincodeNotFoundError, invalid_pincode_error_handler, pincode_not_found_error_handler
from project_2.data.pincode import pincodes

app = FastAPI(
    title="Pincode API",
    description="API for pincode information",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

app.add_exception_handler(InvalidPincodeError, invalid_pincode_error_handler)
app.add_exception_handler(PincodeNotFoundError, pincode_not_found_error_handler)

@app.get("/pincode/{pincode}", response_model=LocationResponse, status_code=200)
async def get_pincode(pincode: int) -> LocationResponse:
    """
    Get pincode information
    """
    try:
        pincode_data = pincodes.get(pincode)
        if pincode_data is None:
            raise PincodeNotFoundError(f"Pincode {pincode} not found")
        else:
            location = Location(
                pincode=pincode,
                city=pincode_data['city'],
                state=pincode_data['state'],
                country=pincode_data['country']
            )
            return LocationResponse(
                status=200,
                message="Pincode found",
                data=location
            )
    except ValueError as e:
        raise InvalidPincodeError(str(e))

@app.post("/pincodes", response_model=BulkLocationResponse, status_code=200)
async def get_pincodes(bulk_location_request: BulkLocationRequest) -> BulkLocationResponse:
    """
    Get pincode information
    """
    try:
        locations = []
        not_found_pincodes = []

        for pincode in bulk_location_request.pincodes:
            pincode_data = pincodes.get(pincode)
            if pincode_data is None:
                not_found_pincodes.append(pincode)
            else:
                location = Location(
                    pincode=pincode,
                    city=pincode_data['city'],
                    state=pincode_data['state'],
                    country=pincode_data['country']
                )
                locations.append(location)
        
        return BulkLocationResponse(
            status=200,
            message="Pincodes found",
            found=locations,
            not_found=not_found_pincodes
        )
    except ValueError as e:
        raise InvalidPincodeError(str(e))

@app.get("/")
def health_check():
    return {
        "status": 200,
        "message": "OK"
    }
