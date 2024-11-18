from fastapi import APIRouter,Depends,status,HTTPException
import schemas,models,db
import oauth2
from sqlalchemy.orm import Session
from typing import List
from repository import blog



router=APIRouter(  prefix="/blog",
                  tags=['Blog'],
                  dependencies=[Depends(oauth2.get_current_user)]
                )
   
# FOR GETTING ALL THE BLOGS
@router.get('/',response_model=List[schemas.ShowBlog])
def show_blog( db: Session = Depends(db.get_db)):
    # blog=db.query(models.Blog).join(models.User).all()
    return blog.get_all(db)
# FOR CREATING BLOG
@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(db.get_db)):
   return blog.create(request,db)
# FOR DELETING BLOGS USING ID
@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(id, db: Session = Depends(db.get_db)):
   return blog.destroy(id,db)
# FOR UPDATING BLOGS USING ID
@router.put('/{id}',status_code=status.HTTP_200_OK)
def update(id, request: schemas.Blog, db: Session = Depends(db.get_db)):
    return blog.update(id,request,db)
# FOR SHOWING BLOG WITH SPECIFIC ID
@router.get('/{id}',response_model=schemas.ShowBlog)
def show_blog(id, db: Session = Depends(db.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog not found with id {id}')
    return blog