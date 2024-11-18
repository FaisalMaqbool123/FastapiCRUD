from sqlalchemy.orm import Session
import models,schemas
from fastapi import status,HTTPException

def get_all(db:Session):
     blog=db.query(models.Blog).join(models.User).all()
     return blog
def create(request:schemas.Blog, db:Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
def destroy(id:int, db:Session):
      blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
      if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
      db.commit()
      return {'detail':f'Blog with id {id} deleted sucessfully'}
def update(id:int,db:Session,request: schemas.Blog):
     blog = db.query(models.Blog).filter(models.Blog.id == id)
     if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
     blog.update({"title": request.title, "body": request.body})
     db.commit()
     return {'detail': f'Blog with id {id} updated successfully'}