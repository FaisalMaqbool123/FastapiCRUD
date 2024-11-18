from fastapi import FastAPI
# , Depends,status,Response,HTTPException
# from sqlalchemy.orm import Session
import models
# import schemas
from db import engine
# from typing import List
# from hashing import Hash

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

from routers import blogs,user,login
app.include_router(login.router)
app.include_router(blogs.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()  
#     try:
#         yield db 
#     finally:
#         db.close()  

# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=['Blog'])
# def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
   
#     new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# @app.delete('/blog/{id}', status_code=status.HTTP_200_OK,tags=['Blog'])
# def delete(id, db: Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
#     db.commit()
#     return {'detail':f'Blog with id {id} deleted sucessfully'}

# @app.put('/blog/{id}',status_code=status.HTTP_200_OK,tags=['Blog'])
# def update(id, request: schemas.Blog, db: Session = Depends(get_db)):
#      blog = db.query(models.Blog).filter(models.Blog.id == id)
    
#      if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
#      blog.update({"title": request.title, "body": request.body})
#      db.commit()
#      return {'detail': f'Blog with id {id} updated successfully'}
# @app.get('/blog',response_model=List[schemas.ShowBlog],tags=['Blog'])
# def blog( db: Session = Depends(get_db)):
#     blog=db.query(models.Blog).all()
#     return blog
# @app.get('/blog/{id}',response_model=schemas.ShowBlog,tags=['Blog'])
# def show_blog(id, response: Response, db: Session = Depends(get_db)):
#     blog=db.query(models.Blog).filter(models.Blog.id==id).first()
#     if not blog:
#       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog not found with id {id}')
#     return blog




# @app.post('/user',response_model=schemas.ShowUser,tags=['User'])
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     new_user=models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user{id}',response_model=schemas.ShowUser,tags=['User'])
# def show_user(id:int,db: Session = Depends(get_db)):
#     user=db.query(models.User).filter(models.User.id==id).first()
#     if not user:
#           raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User not found with id {id}')
#     return user