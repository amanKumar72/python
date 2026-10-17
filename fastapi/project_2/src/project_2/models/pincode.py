from pydantic import BaseModel, field_validator

class Location(BaseModel):
    pincode: int
    city: str
    state: str
    country: str
    
    @field_validator('pincode')
    @classmethod
    def validate_pincode(cls, value: int) -> int:
        if not (100000 <= value <= 999999):
            raise ValueError("Invalid Pincode")
        return value

class LocationResponse(BaseModel):
    status: int
    message: str
    data: Location | None = None

class BulkLocationRequest(BaseModel):
    pincodes: list[int]

    @field_validator('pincodes')
    @classmethod
    def validate_pincodes(cls, values: list[int]) -> list[int]:
        for pincode in values:
            if not (100000 <= pincode <= 999999):
                raise ValueError("Invalid Pincode")
        return values

class BulkLocationResponse(BaseModel):
    status: int
    message: str
    found: list[Location] | None = None
    not_found: list[int] | None = None