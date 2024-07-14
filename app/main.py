from fastapi import FastAPI
from app.routers import auth, posts
# from app.database import Base, engine

app = FastAPI()

# Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(posts.router, prefix="/posts", tags=["posts"])
