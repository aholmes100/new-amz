from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import keywords

app = FastAPI()

origins = [
    "http://localhost:3000",
]

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(keywords.router)
