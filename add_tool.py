from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Math Operations API",
    description="Simple API for mathematical operations"
)

# Pydantic model for request body
class AddRequest(BaseModel):
    a: float
    b: float

# Pydantic model for response (only result now)
class AddResponse(BaseModel):
    result: float

@app.post("/add", response_model=AddResponse)
async def add_numbers(request: AddRequest):
    """Add two numbers and return the result."""
    result = request.a + request.b
    return AddResponse(result=result)

@app.get("/")
async def root():
    """
    Root endpoint with basic information about the API.
    """
    return {"message": "Welcome to Math Operations API", "endpoints": ["/add"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8100)