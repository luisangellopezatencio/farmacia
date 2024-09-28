from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from .security import get_password_hash, verify_password, create_access_token
import re


from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2scheme = OAuth2PasswordBearer(
    tokenUrl="token"
)

origins = [
    "http://localhost:5173/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users/", response_model=list[schemas.UserSchema])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    if users is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return users

@app.post("/login", response_model=schemas.UserLoginResponseSchema)
def login(user_identifier: str, password: str, db: Session = Depends(get_db)):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    user = crud.get_user_login(db, user_identifier)
    if user is None or not verify_password(password, user.password):
        raise HTTPException(status_code=404, detail="User not found")
    
    # Creamos el token
    access_token = create_access_token(data={"sub": user.username if not re.match(email_regex, user_identifier) else user.email})

    # Devolvemos el username (o email) y el password
    return {
        "success": True,
        "access_token": access_token,
        "token_type": "bearer",
        "user": user.username if not re.match(email_regex, user_identifier) else user.email
    }


@app.get("/medicamentos/", response_model=list[schemas.MedicamentoSchema])
def read_medicamentos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    medicamentos = crud.get_all_medicamentos(db, skip=skip, limit=limit)
    if medicamentos is None:
        raise HTTPException(status_code=404, detail="Medicamentos not found")
    return medicamentos

@app.get("/transacciones/", response_model=list[schemas.TransaccionMedicamentoSchema])
def read_transacciones(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    transacciones = crud.get_all_transacciones(db, skip=skip, limit=limit)
    if transacciones is None:
        raise HTTPException(status_code=404, detail="Transacciones not found")
    return transacciones

