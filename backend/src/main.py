from fastapi import FastAPI
from src.api.upload import router as upload_router
from src.api.qna import router as qna_router
from src.middleware import add_middlewares

app = FastAPI()

# Add middleware
add_middlewares(app)

# Include routers
app.include_router(upload_router)
app.include_router(qna_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the QnA App API!"}
