# Imports
from fastapi import FastAPI
import uvicorn
from config import settings
from api.routers import get_api_router

#Create FastAPI app
app = FastAPI()

#Include the API router we created
app.include_router(get_api_router(app), tags=["tasks"])

# Define main function to run the server
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
    )