from sqlalchemy.orm import Session
from fastapi import status,HTTPException,Depends
from hashing import Hash
import models,schemas,db
from hashing import Hash


def create(request: schemas.User, db: Session):
    # Hash the password before saving it
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    
    # Save the new user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user


def get_user(id:int,db: Session = Depends(db.get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User not found with id {id}')
    return user