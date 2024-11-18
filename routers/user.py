from fastapi import APIRouter,Depends,status,HTTPException
import schemas,models,db
from sqlalchemy.orm import Session
from repository import users
import oauth2

router=APIRouter(
     prefix="/user",
     tags=['User'],
     dependencies=[Depends(oauth2.get_current_user)]
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(db.get_db)):
   new_user=users.create(request,db)
   return new_user

@router.get('/{id}',response_model=schemas.ShowUser)
def show_user(id:int,db: Session = Depends(db.get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User not found with id {id}')
    return user