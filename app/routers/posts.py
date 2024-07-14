from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from cachetools import TTLCache
from typing import List
from app import models, schemas, dependencies
from app.database import get_db

router = APIRouter()

cache = TTLCache(maxsize=100, ttl=300)

@router.post("/addpost", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    db_post = models.Post(**post.model_dump(), owner_id=current_user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/", response_model=List[schemas.Post])
def read_posts(db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    if current_user.id in cache:
        return cache[current_user.id]
    posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    cache[current_user.id] = posts
    return posts

@router.delete("/deletepost/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == post_id, models.Post.owner_id == current_user.id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"detail": "Post deleted"}
